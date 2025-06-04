# Gesture Controlled LEDs with MediaPipe and Arduino

This project allows you to control 5 LEDs connected to an Arduino using hand gestures detected via a webcam in Python. The hand gesture is analyzed using MediaPipe, and finger states are sent to the Arduino over a serial connection as a 5-bit binary string.

---

## How It Works

- The Python script uses **MediaPipe** to detect a single hand and determine which fingers are raised.
- Each finger state is represented as a binary digit (`1 = up`, `0 = down`).
- The resulting 5-bit binary string (e.g., `10101`) is sent via serial to an Arduino.
- The Arduino receives the string and lights up LEDs connected to digital pins 8–12 based on the bit values.

---

##  Requirements

### Python Side
- Python 3
- OpenCV (`cv2`)
- MediaPipe
- PySerial

Install dependencies:
```bash
pip install opencv-python mediapipe pyserial
