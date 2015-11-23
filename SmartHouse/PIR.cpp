#include "PIR.h"

PIR::PIR(int pin) {
    pinMode(pin, INPUT);
    this->pin = pin;
}

unsigned char PIR::getReading() {
    if(digitalRead(this->pin) == HIGH) {
        return (char) 1;
    } else {
        return (char) 0;
    }
}