#include "LightController.h"

#define MAX_MILLIS_TO_WAIT 1000

LightController::LightController() {
    this->light = new Light(6);
}

void LightController::execute(unsigned char byte) {
    unsigned char operation = Serial.read();

    switch(operation) {
        case TURN_OFF:
            this->light->turnOff();
            break;
        case TURN_ON:
            this->light->turnOn();
            break;
        case CHANGE_BRIGHT:
        {
            unsigned long starttime = millis();
            int bytesToWait = 1;

            while ((Serial.available() < bytesToWait) && ((millis() - starttime) < MAX_MILLIS_TO_WAIT)) {
            // hang in this loop until we either get 9 bytes of data or 1 second
            // has gone by
            }

            unsigned char bright = Serial.read();
            this->light->changeBright(bright);
            break;
        }
        default:
            break;
    }
}