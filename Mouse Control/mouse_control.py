import cv2
import numpy as np
import mediapipe as mp
import pyautogui

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils

# Initialize webcam
cap = cv2.VideoCapture(0)

# Get screen size
screen_width, screen_height = pyautogui.size()

while True:
    success, img = cap.read()
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            lm_list = []
            for id, lm in enumerate(hand_landmarks.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lm_list.append([id, cx, cy])

            # Define box coordinates
            box_top_left = (100, 100)
            box_bottom_right = (300, 300)

            # Draw box on the frame
            cv2.rectangle(img, box_top_left, box_bottom_right, (0, 255, 0), 2)

            if lm_list:
                # Index finger tip
                x1, y1 = lm_list[8][1], lm_list[8][2]
                # Middle finger tip
                x2, y2 = lm_list[12][1], lm_list[12][2]

                # Check if fingertip is within the box
                if box_top_left[0] <= x1 <= box_bottom_right[0] and box_top_left[1] <= y1 <= box_bottom_right[1]:
                    # Convert coordinates
                    screen_x = np.interp(x1, [box_top_left[0], box_bottom_right[0]], [0, screen_width])
                    screen_y = np.interp(y1, [box_top_left[1], box_bottom_right[1]], [0, screen_height])

                    # Get current mouse position
                    current_mouse_x, current_mouse_y = pyautogui.position()

                    # Introduce a scaling factor to smooth the cursor movement
                    scaling_factor = 0.2  # Adjust this value to control the speed (0 < scaling_factor <= 1)
                    smooth_x = current_mouse_x + (screen_x - current_mouse_x) * scaling_factor
                    smooth_y = current_mouse_y + (screen_y - current_mouse_y) * scaling_factor

                    # Move mouse
                    pyautogui.moveTo(smooth_x, smooth_y)

                    # Check for click gesture (distance between index and middle finger)
                    length = np.hypot(x2 - x1, y2 - y1)
                    if length < 40:
                        pyautogui.click()

    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()