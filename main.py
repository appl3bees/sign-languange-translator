# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import VideoExceptions
import cv2 # import the cv2 library

cap = cv2.VideoCapture(0) #Global variable: initialize the cap variable to the video caputre device

def getframe():
    ret, frame = cap.read()
    try:
        if frame is None:
            raise VideoExceptions.FrameReadError()
    except VideoExceptions.FrameReadError as e:
        print("Error:", e)
        return frame

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

   # ret, frame = cap.read()
    getframe()


