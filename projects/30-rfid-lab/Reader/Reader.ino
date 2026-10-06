// New reference wiring for an Arduino Uno-compatible lab board; not a real setup.
// MFRC522 breakout power and logic-level requirements must be checked before wiring.
#include <SPI.h>
#include <MFRC522.h>
constexpr byte SS_PIN = 10;
constexpr byte RST_PIN = 9;
MFRC522 reader(SS_PIN, RST_PIN);

void setup() { Serial.begin(9600); SPI.begin(); reader.PCD_Init(); }
void loop() {
  if (!reader.PICC_IsNewCardPresent() || !reader.PICC_ReadCardSerial()) return;
  Serial.print(F("Public UID: "));
  for (byte i=0; i<reader.uid.size; ++i) {
    if (reader.uid.uidByte[i]<0x10) Serial.print('0');
    Serial.print(reader.uid.uidByte[i],HEX);
    if (i+1<reader.uid.size) Serial.print(':');
  }
  Serial.println();
  Serial.println(F("A UID is not a secure identity or proof of authorization."));
  reader.PICC_HaltA(); reader.PCD_StopCrypto1();
}
