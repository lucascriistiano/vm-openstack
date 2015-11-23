#include <Arduino.h>

#define MEASURES_NUM 10

class NTC{
private:
    unsigned short int pin;

public:
    NTC(int pin);
    unsigned short int getReading();
};