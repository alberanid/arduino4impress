/*
 * The value of the potentiometer (normalized to a
 * 0 - 99 range) is periodically sent to the serial.
 *
 * Copyright: 2012, Davide Alberani <da@erlug.linux.it>
 * License: GPLv3
*/

const int POT_PIN = 0;
const int SLEEP_TIME = 1000;
const int SP_BAUD = 9600;
const int LED_PINS[] = {8, 9, 10, 11, 12};


void setup() {
  Serial.begin(SP_BAUD);
  for (int i = 0; i < 5; i++) {
    pinMode(LED_PINS[i], OUTPUT);
  }
}


void turnOnSomeLEDs(int howMany) {
  for (int i = 0; i < 5; i++) {
    if (i < howMany) {
      digitalWrite(LED_PINS[i], HIGH);
    } else {
      digitalWrite(LED_PINS[i], LOW);
    }
  }
}


void loop() {
  int potValue = analogRead(POT_PIN);
  int outValue = map(potValue, 0, 1023, 0, 99);
  int ledsToTurnOn = map(potValue, 0, 1023, 0, 5);

  Serial.println(outValue);
  turnOnSomeLEDs(ledsToTurnOn);

  delay(SLEEP_TIME);
}
