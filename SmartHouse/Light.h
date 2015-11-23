#include <Arduino.h>

class Light{
private:
    int pin;

public:
    Light(int pin);
    void turnOff();
    void turnOn();
    void changeBright(unsigned char bright);
};