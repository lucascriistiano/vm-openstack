#include <Arduino.h>
#include "Light.h"

//OPERATIONS
#define TURN_OFF        1
#define TURN_ON         2
#define CHANGE_BRIGHT   3

class LightController {
private:
    Light* light;

public:
    LightController();
    void execute(unsigned char byte);
};