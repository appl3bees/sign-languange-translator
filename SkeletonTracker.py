import mediapipe as mp
import VideoExceptions #import custom exception class
import cv2 # import the cv2 library

HAND_CONNECTIONS = frozenset([
    (0, 1), (1, 2), (2, 3), (3, 4),        # thumb
    (0, 5), (5, 6), (6, 7), (7, 8),         # index finger
    (5, 9), (9, 10), (10, 11), (11, 12),    # middle finger
    (9, 13), (13, 14), (14, 15), (15, 16),  # ring finger
    (0, 17), (13, 17), (17, 18), (18, 19), (19, 20)  # pinky + palm
])




class SkeletonTracker:
    def __init__(self):
        self.base_options = mp.tasks.BaseOptions
        self.mp_hands = mp.tasks.vision.HandLandmarker
        self.options = mp.tasks.vision.HandLandmarkerOptions(
            base_options=self.base_options(
                model_asset_path='hand_landmarker.task'
            ),
            num_hands=2
        )
        self.hands = self.mp_hands.create_from_options(self.options)

    def detect_hands(self, frame):

        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

        results = self.hands.detect(mp_image)

        if not results.hand_landmarks:
            cv2.putText(frame, "Hand Not Detected", (10, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        else:
            self.draw_landmarks(frame, results)

        return frame

    def draw_landmarks(self, frame, results):
        h, w, _ = frame.shape
        connections = HAND_CONNECTIONS
        for hand_landmarks in results.hand_landmarks:
            for landmark in hand_landmarks:
                cx, cy = int(landmark.x * w), int(landmark.y * h)
                cv2.circle(frame, (cx, cy), 5, (0, 255, 0), -1)

            for start_idx, end_idx in connections:
                start = hand_landmarks[start_idx]
                end = hand_landmarks[end_idx]
                sx, sy = int(start.x * w), int(start.y * h)
                ex, ey = int(end.x * w), int(end.y * h)
                cv2.line(frame, (sx, sy), (ex, ey), (255, 255, 255), 2)





