#include "Fan.h"

Fan::Fan(int pin) {
    this->pin = pin;
    pinMode(this->pin, OUTPUT);
}

void Fan::turnOff() {
    digitalWrite(this->pin, LOW);
}

void Fan::turnOn() {
    digitalWrite(this->pin, HIGH);
}

void Fan::changeSpeed(unsigned char speed) {
  analogWrite(this->pin, speed);
}