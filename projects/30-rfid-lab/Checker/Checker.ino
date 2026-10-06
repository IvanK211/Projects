// New reference wiring for an Arduino Uno-compatible lab board; not a real setup.
// MFRC522 breakout power and logic-level requirements must be checked before wiring.
#include <SPI.h>
#include <MFRC522.h>
constexpr byte SS_PIN = 10;
constexpr byte RST_PIN = 9;
MFRC522 reader(SS_PIN, RST_PIN);

void setup() {
  Serial.begin(9600);
  SPI.begin();
  reader.PCD_Init();
  Serial.println(F("Reader communication check; no card writes."));
  reader.PCD_DumpVersionToSerial();
}
void loop() {
  if (!reader.PICC_IsNewCardPresent() || !reader.PICC_ReadCardSerial()) return;
  Serial.print(F("Detected card type: "));
  Serial.println(reader.PICC_GetTypeName(reader.PICC_GetType(reader.uid.sak)));
  reader.PICC_HaltA();
  reader.PCD_StopCrypto1();
}
