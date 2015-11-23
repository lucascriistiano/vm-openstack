#include <Arduino.h>

class Gate{
private:
    int pinOpen;
    int pinClose;

public:
    Gate(int pinOpen, int pinClose);
    void open();
    void close();
};