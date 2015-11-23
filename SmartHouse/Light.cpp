#include "Light.h"

Light::Light(int pin) {
    this->pin = pin;
    pinMode(this->pin, OUTPUT);
}

void Light::turnOff() {
    digitalWrite(this->pin, LOW);
}

void Light::turnOn() {
    digitalWrite(this->pin, HIGH);
}

void Light::changeBright(unsigned char bright) {
    analogWrite(this->pin, bright);
}