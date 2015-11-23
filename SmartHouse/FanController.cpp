#include "FanController.h"

#define MAX_MILLIS_TO_WAIT 1000

FanController::FanController() {
    this->fan = new Fan(5);
}

void FanController::execute(unsigned char byte) {
    unsigned char operation = Serial.read();

    switch(operation) {
        case TURN_OFF:
            this->fan->turnOff();
            break;
        case TURN_ON:
            this->fan->turnOn();
            break;
        case CHANGE_SPEED:
        {
            unsigned long starttime = millis();
            int bytesToWait = 1;

            while ((Serial.available() < bytesToWait) && ((millis() - starttime) < MAX_MILLIS_TO_WAIT)) {
            // hang in this loop until we either get 9 bytes of data or 1 second
            // has gone by
            }

            unsigned char speed = Serial.read();
            this->fan->changeSpeed(speed);
            break;
        }
        default:
            break;
    }
}