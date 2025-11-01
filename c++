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
