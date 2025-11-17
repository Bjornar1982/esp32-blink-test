#include <Arduino.h>

void setup() {
    Serial.begin(115200);
    pinMode(2, OUTPUT);  // Intern LED på noen ESP32-kort (GPIO 2)
}

void loop() {
    digitalWrite(2, HIGH);
    delay(500);
    digitalWrite(2, LOW);
    delay(500);

    Serial.println("ESP32 virker!");
}
