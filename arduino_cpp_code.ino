// Arduino Sketch: Control 5 LEDs with binary string from Python

void setup() {
  Serial.begin(9600);
  for (int i = 8; i <= 12; i++) {
    pinMode(i, OUTPUT);
  }
}

void loop() {
  if (Serial.available()) {
    String data = Serial.readStringUntil('\n');  // Read line

    if (data.length() == 5) {
      for (int i = 0; i < 5; i++) {
        if (data.charAt(i) == '1') {
          digitalWrite(8 + i, HIGH);
        } else {
          digitalWrite(8 + i, LOW);
        }
      }
    }
  }
}