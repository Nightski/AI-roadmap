import cv2
import mediapipe as mp
import csv

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

label = input("Enter sign label (example: sign1): ")

with open("data.csv", "a", newline="") as f:
    writer = csv.writer(f)

    print("Press Q to stop collecting")

    while True:
        ret, frame = cap.read()
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = hands.process(frame_rgb)

        if result.multi_hand_landmarks:
            for hand in result.multi_hand_landmarks:
                landmarks = []
                for lm in hand.landmark:
                    landmarks.append(lm.x)
                    landmarks.append(lm.y)

                landmarks.append(label)
                writer.writerow(landmarks)

                mp_draw.draw_landmarks(frame, hand, mp_hands.HAND_CONNECTIONS)

        cv2.imshow("Collecting Data", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
