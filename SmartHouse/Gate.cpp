#include "Gate.h"

Gate::Gate(int pinOpen, int pinClose) {
    this->pinOpen = pinOpen;
    this->pinClose = pinClose;

    pinMode(this->pinOpen, OUTPUT);
    pinMode(this->pinClose, OUTPUT);
}

void Gate::open() {
    digitalWrite(this->pinOpen, HIGH);
    digitalWrite(this->pinClose, LOW);
}

void Gate::close() {
    digitalWrite(this->pinClose, HIGH);
    digitalWrite(this->pinOpen, LOW);
}