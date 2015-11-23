#include "NTC.h"

NTC::NTC(int pin) {
    this->pin = pin;
}

unsigned short int NTC::getReading() {
    unsigned int readingSum = 0;
    for(int i = 0; i < MEASURES_NUM; i++) {
        readingSum += analogRead(this->pin);
    }

    return (readingSum / MEASURES_NUM);
}