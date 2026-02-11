import cv2
import mediapipe as mp
import numpy as np
import pickle

# Load model
model = pickle.load(open("model.pkl", "rb"))

# Load images
images = {
    "smile": cv2.imread("images/smile.jpg"),
    "chin": cv2.imread("images/chin.jpg")
}

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

cap = cv2.VideoCapture(0)

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

            prediction = model.predict([landmarks])[0]

            if prediction in images:
                cv2.imshow("Result", images[prediction])

    cv2.imshow("Camera", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()