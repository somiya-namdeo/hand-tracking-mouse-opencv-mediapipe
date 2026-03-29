import cv2
import pyautogui
import math
import mediapipe as mp
import time

# Initialize camera
cap = cv2.VideoCapture(0)

# Screen size
screen_w, screen_h = pyautogui.size()

# Smoothening variables
prev_x, prev_y = 0, 0
smoothening = 5

# Frame reduction (stability)
frame_reduction = 100

# Disable failsafe
pyautogui.FAILSAFE = False

# Click cooldown
last_click_time = 0

# FPS variables
prev_time = 0

# ✅ Use MediaPipe SOLUTIONS (stable)
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

while True:
    success, frame = cap.read()
    if not success:
        break

    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape

    # Convert to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Detect hands
    results = hands.process(rgb_frame)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:

            # Landmarks
            x1 = int(hand_landmarks.landmark[8].x * w)   # Index
            y1 = int(hand_landmarks.landmark[8].y * h)

            x2 = int(hand_landmarks.landmark[4].x * w)   # Thumb
            y2 = int(hand_landmarks.landmark[4].y * h)

            x3 = int(hand_landmarks.landmark[12].x * w)  # Middle
            y3 = int(hand_landmarks.landmark[12].y * h)

            # Draw points
            cv2.circle(frame, (x1, y1), 10, (255, 0, 0), -1)
            cv2.circle(frame, (x2, y2), 10, (0, 255, 0), -1)
            cv2.circle(frame, (x3, y3), 10, (0, 0, 255), -1)

            # Boundary control
            x1 = max(frame_reduction, min(w - frame_reduction, x1))
            y1 = max(frame_reduction, min(h - frame_reduction, y1))

            # Map to screen
            screen_x = int((x1 - frame_reduction) * screen_w / (w - 2 * frame_reduction))
            screen_y = int((y1 - frame_reduction) * screen_h / (h - 2 * frame_reduction))

            # Smooth movement
            curr_x = prev_x + (screen_x - prev_x) / smoothening
            curr_y = prev_y + (screen_y - prev_y) / smoothening

            pyautogui.moveTo(curr_x, curr_y)
            prev_x, prev_y = curr_x, curr_y

            # Distance calculations
            distance_index_thumb = math.hypot(x2 - x1, y2 - y1)
            distance_middle_thumb = math.hypot(x3 - x2, y3 - y2)

            # LEFT CLICK
            if distance_index_thumb < 40 and time.time() - last_click_time > 0.8:
                pyautogui.click()
                last_click_time = time.time()
                cv2.putText(frame, "LEFT CLICK", (20, 50),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

            # RIGHT CLICK
            elif distance_middle_thumb < 40:
                pyautogui.rightClick()
                cv2.putText(frame, "RIGHT CLICK", (20, 50),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)

            # SCROLL
            elif abs(x1 - x3) < 40:
                if y3 < y1 - 20:
                    pyautogui.scroll(40)
                    cv2.putText(frame, "SCROLL UP", (20, 100),
                                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

                elif y3 > y1 + 20:
                    pyautogui.scroll(-40)
                    cv2.putText(frame, "SCROLL DOWN", (20, 100),
                                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

    # FPS Calculation
    curr_time = time.time()
    fps = 1 / (curr_time - prev_time) if curr_time != prev_time else 0
    prev_time = curr_time

    cv2.putText(frame, f"FPS: {int(fps)}", (20, 150),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    cv2.imshow("Virtual Mouse", frame)

    # Exit on ESC
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()