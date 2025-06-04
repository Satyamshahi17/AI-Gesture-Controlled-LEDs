import cv2
import mediapipe as mp
import serial
import time

# Serial setup
arduino = serial.Serial('COM10', 9600, timeout=1)
time.sleep(2)

# MediaPipe setup
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
cap = cv2.VideoCapture(0)

def get_finger_states(hand_landmarks):
    lm = hand_landmarks.landmark
    finger_states = [1 if lm[4].x < lm[3].x else 0]

    # Thumb

    # Fingers: Index, Middle, Ring, Pinky
    tips = [8, 12, 16, 20]
    for tip in tips:
        finger_states.append(1 if lm[tip].y < lm[tip - 2].y else 0)

    return finger_states

while True:
    success, frame = cap.read()
    if not success:
        continue

    img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(img_rgb)

    if result.multi_hand_landmarks:
        for hand in result.multi_hand_landmarks:
            states = get_finger_states(hand)
            binary_string = ''.join(map(str, states))
            arduino.write((binary_string + '\n').encode())
            print("Sent:", binary_string)
            break  # Only use one hand

    cv2.imshow("Gesture Control", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
arduino.close()
