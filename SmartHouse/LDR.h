#include <Arduino.h>

#define MEASURES_NUM 10

class LDR {
private:
    unsigned short int pin;

public:
    LDR(int pin);
    unsigned short int getReading();
};