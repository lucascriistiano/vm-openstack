#include "Fan.h"

//OPERATIONS
#define TURN_OFF        1
#define TURN_ON         2
#define CHANGE_SPEED    3

class FanController {
private:
    Fan* fan;

public:
    FanController();
    void execute(unsigned char byte);
};