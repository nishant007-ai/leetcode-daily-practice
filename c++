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
  String logPath = "artifacts/" +