#include "LDR.h"

LDR::LDR(int pin) {
    this->pin = pin;
}

unsigned short int LDR::getReading() {
    unsigned int readingSum = 0;
    for(int i = 0; i < MEASURES_NUM; i++) {
        readingSum += analogRead(this->pin);
    }

    return (readingSum / MEASURES_NUM);
}