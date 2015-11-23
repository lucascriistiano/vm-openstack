#include "GateController.h"

#define MAX_MILLIS_TO_WAIT 1000

GateController::GateController() {
    this->gate = new Gate(3,4);
}

void GateController::execute(unsigned char byte) {
    unsigned char operation = Serial.read();

    switch(operation) {
        case OPEN:
            this->gate->open();
            break;
        case CLOSE:
            this->gate->close();
            break;
        default:
            break;
    }
}