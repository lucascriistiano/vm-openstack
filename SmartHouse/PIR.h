#include <Arduino.h>

class PIR{
private:
    unsigned short int pin;

public:
    PIR(int pin);
    unsigned char getReading();
};