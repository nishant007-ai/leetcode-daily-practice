// ------------------------------
// PET FEEDER SYSTEM WITH RFID + FIREBASE + SERVO
// ------------------------------
// Compatible with ESP32 (Arduino IDE)
// Libraries Required:
// 1️⃣ Firebase ESP Client (by Mobizt)
// 2️⃣ MFRC522 (by Gijs van Zanten)
// 3️⃣ ESP32Servo
// ------------------------------

#include <WiFi.h>
#include <time.h>
#include <ESP32Servo.h>
#include <Firebase_ESP_Client.h>
#include <MFRC522.h>
#include <SPI.h>

// --- 1. WIFI & FIREBASE CONFIGURATION ---

#define WIFI_SSID "suha"
#define WIFI_PASSWORD "11111111"

// Replace with your Firebase Project details
#define FIREBASE_API_KEY "AIzaSyBvinpuJDqmTrNERZKraF-4gR736TrBQEA"
#define FIREBASE_PROJECT_ID "pet-feeder-project-896ba"

// IDs (must match your web app)
const String APP_ID = "default-pet-feeder-app-id";
const String OWNER_USER_ID = "ab7ceb20-f372-4d2c-acbc-c155c14c6722";

// --- 2. HARDWARE CONFIGURATION ---

#define SERVO_PIN 27
Servo feederServo;
unsigned long lastFeedMillis = 0;

// RFID Pins
#define RST_PIN 32
#define SS_PIN 33
MFRC522 mfrc522(SS_PIN, RST_PIN);
const String AUTHORIZED_TAG_UID = "YOUR_PETS_AUTHORIZED_RFID_TAG_UID";

// --- 3. TIME CONFIGURATION ---
const char* ntpServer = "pool.ntp.org";
const long gmtOffset_sec = 19800; // India GMT +5:30
const int daylightOffset_sec = 0;

// --- 4. FIREBASE OBJECTS ---
FirebaseData fbdo;
FirebaseAuth auth;
FirebaseConfig config;

// --- 5. HELPER FUNCTIONS ---

String uidToString(byte *buffer, byte bufferSize) {
  String result = "";
  for (byte i = 0; i < bufferSize; i++) {
    if (buffer[i] < 0x10) result += "0";
    result += String(buffer[i], HEX);
    if (i < bufferSize - 1) result += " ";
  }
  result.toUpperCase();
  return result;
}

void dispenseFood(String portionSize) {
  Serial.printf("[HW] Dispensing %s portion...\n", portionSize.c_str());

  int rotationDegrees = 0;
  if (portionSize == "small") rotationDegrees = 30;
  else if (portionSize == "medium") rotationDegrees = 60;
  else if (portionSize == "large") rotationDegrees = 90;

  feederServo.write(rotationDegrees);
  delay(1000);
  feederServo.write(0);

  Serial.println("[HW] Dispense complete.");
}

void logFeedToFirestore(String portionSize, String feedType) {
  String logPath = "artifacts/" + APP_ID + "/users/" + OWNER_USER_ID + "/pet_feeder_logs";

  FirebaseJson content;
  content.set("fields/timestamp/timestampValue", "0");
  content.set("fields/type/stringValue", feedType.c_str());
  content.set("fields/portion/stringValue", portionSize.c_str());

  if (Firebase.Firestore.createDocument(&fbdo, FIREBASE_PROJECT_ID, "", logPath.c_str(), content.raw())) {
    Serial.printf("[CLOUD] Logged %s feed to Firestore.\n", feedType.c_str());
  } else {
    Serial.printf("[ERROR] Firestore log failed: %s\n", fbdo.errorReason().c_str());
  }
}

void initWiFi() {
  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
  Serial.print("Connecting to WiFi");
  while (WiFi.status() != WL_CONNECTED) {
    Serial.print(".");
    delay(500);
  }
  Serial.println();
  Serial.print("Connected, IP: ");
  Serial.println(WiFi.localIP());
}

void initTime() {
  configTime(gmtOffset_sec, daylightOffset_sec, ntpServer);
  Serial.println("Waiting for NTP sync...");
  time_t now = time(nullptr);
  while (now < 1000) {
    delay(500);
    now = time(nullptr);
  }
  Serial.println("Time synchronized.");
}

// --- 6. SETUP ---

void setup() {
  Serial.begin(115200);
  delay(1000);

  initWiFi();
  initTime();

  // Initialize Servo
  feederServo.attach(SERVO_PIN);
  feederServo.write(0);

  // Initialize RFID
  SPI.begin();
  mfrc522.PCD_Init();
  Serial.printf("[INIT] RFID initialized. Version: 0x%X\n", mfrc522.PCD_ReadRegister(mfrc522.VersionReg));

  // Firebase setup
  config.api_key = FIREBASE_API_KEY;
  Firebase.begin(&config, &auth);
  Firebase.reconnectWiFi(true);

  Serial.println("[INIT] Feeder Ready!");
}

// --- 7. MAIN LOOP ---

void loop() {
  if (!Firebase.ready()) {
    delay(1000);
    return;
  }

  // --- RFID CHECK ---
  if (!mfrc522.PICC_IsNewCardPresent()) {
    delay(500);
    return;
  }
  if (!mfrc522.PICC_ReadCardSerial()) return;

  String detectedUID = uidToString(mfrc522.uid.uidByte, mfrc522.uid.size);
  Serial.printf("[RFID] Detected Tag UID: %s\n", detectedUID.c_str());

  if (detectedUID != AUTHORIZED_TAG_UID) {
    Serial.printf("[RFID] Unauthorized Tag: %s\n", detectedUID.c_str());
    mfrc522.PICC_HaltA();
    mfrc522.PCD_StopCrypto1();
    return;
  }

  Serial.println("[RFID] Authorized pet detected!");

  // --- TIME CHECK ---
  struct tm timeinfo;
  if (!getLocalTime(&timeinfo)) {
    Serial.println("Failed to obtain time.");
    mfrc522.PICC_HaltA();
    mfrc522.PCD_StopCrypto1();
    return;
  }

  char currentTime[6];
  strftime(currentTime, sizeof(currentTime), "%H:%M", &timeinfo);
  unsigned long currentMillis = millis();

  if (currentMillis - lastFeedMillis > 61000) {
    String schedulesPath = "artifacts/" + APP_ID + "/users/" + OWNER_USER_ID + "/pet_feeder_schedules";
    FirebaseJson schedulesJson;

    if (Firebase.Firestore.getDocuments(&fbdo, FIREBASE_PROJECT_ID, "", schedulesPath.c_str(), "")) {
      schedulesJson.setJsonData(fbdo.jsonString());
      size_t count = schedulesJson.iteratorBegin();
      FirebaseJsonData result;

      for (size_t i = 0; i < count; i++) {
        schedulesJson.get(result, i, "fields/time/stringValue");
        String scheduledTime = result.stringValue;
        schedulesJson.get(result, i, "fields/portion/stringValue");
        String portion = result.stringValue;

        if (scheduledTime == currentTime) {
          Serial.printf("[TRIGGER] Feeding at %s. Portion: %s\n", scheduledTime.c_str(), portion.c_str());
          dispenseFood(portion);
          logFeedToFirestore(portion, "scheduled_rfid_match");
          lastFeedMillis = currentMillis;
          break;
        }
      }
   