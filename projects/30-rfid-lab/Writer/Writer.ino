// New reference wiring for an Arduino Uno-compatible lab board; not a real setup.
// MFRC522 breakout power and logic-level requirements must be checked before wiring.
#include <SPI.h>
#include <MFRC522.h>
constexpr byte SS_PIN = 10;
constexpr byte RST_PIN = 9;
MFRC522 reader(SS_PIN, RST_PIN);

// Writes a fixed harmless label only to block 4 of an owned, disposable Classic lab tag.
// No UID modification, key recovery, trailer writes or access-card duplication.
constexpr bool ENABLE_LAB_WRITE = false; // Deliberately disabled until reviewed.
constexpr byte DATA_BLOCK = 4;
bool armed = false;
void setup() {
  Serial.begin(9600); Serial.setTimeout(500); SPI.begin(); reader.PCD_Init();
  Serial.println(F("Use only a disposable owned lab tag. Compile-time writes are disabled."));
  Serial.println(F("After enabling in source, type WRITE to arm one write."));
}
void loop() {
  if (Serial.available()) {
    String command=Serial.readStringUntil('\n'); command.trim();
    armed=ENABLE_LAB_WRITE && command=="WRITE";
    Serial.println(armed ? F("Armed for one tag.") : F("Not armed."));
  }
  if (!armed || !reader.PICC_IsNewCardPresent() || !reader.PICC_ReadCardSerial()) return;
  armed=false;
  auto type=reader.PICC_GetType(reader.uid.sak);
  if(type!=MFRC522::PICC_TYPE_MIFARE_1K && type!=MFRC522::PICC_TYPE_MIFARE_4K && type!=MFRC522::PICC_TYPE_MIFARE_MINI) {
    Serial.println(F("Unsupported tag type; nothing written."));
    reader.PICC_HaltA(); reader.PCD_StopCrypto1(); return;
  }
  MFRC522::MIFARE_Key key;
  for(byte i=0;i<6;i++) key.keyByte[i]=0xFF; // Factory lab key, not a recovered credential.
  auto status=reader.PCD_Authenticate(MFRC522::PICC_CMD_MF_AUTH_KEY_A,DATA_BLOCK,&key,&reader.uid);
  if(status==MFRC522::STATUS_OK) {
    byte data[16]={0}; const char label[]="LAB SAMPLE";
    for(byte i=0;i<sizeof(label)-1;i++) data[i]=label[i];
    status=reader.MIFARE_Write(DATA_BLOCK,data,16);
    if(status==MFRC522::STATUS_OK) {
      byte buffer[18]; byte length=sizeof(buffer);
      status=reader.MIFARE_Read(DATA_BLOCK,buffer,&length);
      bool matches=status==MFRC522::STATUS_OK;
      if(matches) for(byte i=0;i<16;i++) if(buffer[i]!=data[i]) matches=false;
      Serial.println(matches ? F("Lab data verified.") : F("Read-back verification failed."));
    } else Serial.println(F("Write failed; no retries attempted."));
  } else Serial.println(F("Factory-key authentication failed; stopping."));
  reader.PICC_HaltA(); reader.PCD_StopCrypto1();
}
