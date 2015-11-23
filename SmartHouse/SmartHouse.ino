#include <SPI.h>
#include <RFID.h>

#include "PIR.h"
#include "LDR.h"
#include "NTC.h"

#include "LightController.h"
#include "FanController.h"
#include "GateController.h"

#define SLEEP_TIME          0
#define BAUDS               9600
#define MAX_MILLIS_TO_WAIT  1000

// DEVICES CODE
// SENSORS
#define NTC_CODE     1
#define LDR_CODE     2
#define AUTH_CODE    3
#define PIR_CODE     4
// ACTUATORS
#define LIGHT_CODE   5
#define FAN_CODE     6
#define GATE_CODE    7

// PIN PORTS
// RFID PORTS
#define SS_PIN 10
#define RST_PIN 9

#define LDR_PIN  A0
#define NTC_PIN  A1
#define PIR_PIN  7

// Thermistor temp(1);
RFID rfid(SS_PIN, RST_PIN);
LDR* ldr = new LDR(LDR_PIN);
NTC* ntc = new NTC(NTC_PIN);
PIR* pir = new PIR(PIR_PIN);

LightController* lightController = new LightController();
FanController* fanController = new FanController();
GateController* gateController = new GateController();

unsigned short int lastLdrReading = 0;
unsigned short int lastNtcReading = 0;
unsigned char lastPirReading = 10;
unsigned char lastTagId[5] = { 0, 0, 0, 0, 0 };

void setup() {
  Serial.begin(9600);
  Serial.flush();

  // RFID Setup
  SPI.begin();
  rfid.init();
}

void wait(){
  delay(SLEEP_TIME);
}

void waitForData(int bytesToWait) {
  unsigned long starttime = millis();

  while ((Serial.available() < bytesToWait) && ((millis() - starttime) < MAX_MILLIS_TO_WAIT)) {
    // hang in this loop until we either get 9 bytes of data or 1 second
    // has gone by
  }
}

void serialEvent() {
  unsigned char deviceType = Serial.read();

  switch (deviceType) {
    case LIGHT_CODE:
      waitForData(1);
      lightController->execute(deviceType);
      break;
    case FAN_CODE:
      waitForData(1);
      fanController->execute(deviceType);
      break;
    case GATE_CODE:
      waitForData(1);
      gateController->execute(deviceType);
      break;
    default:
      break;
  }
}

void readLDR() {
  unsigned short int ldrReading = ldr->getReading();

  if(ldrReading != lastLdrReading) {
    Serial.print(LDR_CODE);
    Serial.print(',');
    Serial.print(ldrReading);
    Serial.print('\n');

    lastLdrReading = ldrReading;
  }
}

void readNTC() {
  unsigned short int ntcReading = ntc->getReading();

  if(ntcReading != lastNtcReading) {
    Serial.print(NTC_CODE);
    Serial.print(',');
    Serial.print(ntcReading);
    Serial.print('\n');

    lastNtcReading = ntcReading;
  }
}

void readPIR() {
  unsigned char pirReading = pir->getReading();

  if(pirReading != lastPirReading) {
    Serial.print(PIR_CODE);
    Serial.print(',');
    Serial.print(pirReading);
    Serial.print('\n');

    lastPirReading = pirReading;
  }
}

void sendId() {
  if(rfid.serNum[0] != lastTagId[0] || rfid.serNum[1] != lastTagId[1] || rfid.serNum[2] != lastTagId[2] || rfid.serNum[3] != lastTagId[3] || rfid.serNum[4] != lastTagId[4]) {
    Serial.print(AUTH_CODE);
    Serial.print(',');
    Serial.print(rfid.serNum[0]);
    Serial.print(rfid.serNum[1]);
    Serial.print(rfid.serNum[2]);
    Serial.print(rfid.serNum[3]);
    Serial.print(rfid.serNum[4]);
    Serial.print('\n');

    lastTagId[0] = rfid.serNum[0];
    lastTagId[1] = rfid.serNum[1];
    lastTagId[2] = rfid.serNum[2];
    lastTagId[3] = rfid.serNum[3];
    lastTagId[4] = rfid.serNum[4];
  }
}

void sendDefault() {
  if(lastTagId[0] != 1 || lastTagId[1] != 1 || lastTagId[2] != 1 || lastTagId[3] != 1 || lastTagId[4] != 1) {
    Serial.print(AUTH_CODE);
    Serial.print(',');
    Serial.print(1);
    Serial.print(1);
    Serial.print(1);
    Serial.print(1);
    Serial.print(1);
    Serial.print('\n');

    lastTagId[0] = 1;
    lastTagId[1] = 1;
    lastTagId[2] = 1;
    lastTagId[3] = 1;
    lastTagId[4] = 1;
  }
}

void checkRFID() {
  if (rfid.isCard()) {
    if (rfid.readCardSerial()) {
      sendId();
    } else {
      sendDefault();
    }
  } else {
    sendDefault();
  }

  rfid.halt();
}

void loop() {
  // Execute NTC Reading
  readNTC();
  delay(200);

  // Execute LDR Reading
  readLDR();
  delay(200);

  // Check AUTH Reading
  checkRFID();
  delay(200);

  // Execute PIR Reading
  readPIR();
  delay(200);
}
