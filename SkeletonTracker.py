import mediapipe as mp

class SkeletonTracker:
    def __init__(self):
        self.mpHands = mp.Solutions.hands
        self.hands = mp.solutions.hands.Hands()
