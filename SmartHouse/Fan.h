#include <Arduino.h>

class Fan{
private:
    int pin;

public:
    Fan(int pin);
    void turnOff();
    void turnOn();
    void changeSpeed(unsigned char speed);
};