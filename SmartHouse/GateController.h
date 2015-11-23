#include <Arduino.h>
#include "Gate.h"

//OPERATIONS
#define OPEN       1
#define CLOSE      2

class GateController {
private:
    Gate* gate;

public:
    GateController();
    void execute(unsigned char byte);
};