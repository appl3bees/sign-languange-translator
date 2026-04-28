import mediapipe as mp
import VideoExceptions #import custom exception class
import cv2 # import the cv2 library




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

        return frame


    def draw(self):



