# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import VideoExceptions #import custom exception class
import cv2 # import the cv2 library

cap = cv2.VideoCapture(0) #Global variable: initialize the cap variable to the video caputre device
opencam = cv2.VideoCapture.open(cap)

def getframe(): #method to check if the frames are being captured called from main
    ret, frame = cap.read()
    try:
        if frame is None:
            raise VideoExceptions.FrameReadError()
    except VideoExceptions.FrameReadError as e:
        print("Error:", e)
        return frame

def getcamera(): #method to check if the camera is able can be accessed called from main
    try:
        if not cap.isOpened():
            raise VideoExceptions.CameraNotFoundError()
    except VideoExceptions.CameraNotFoundError as e:
        print("Error:", e)
        return

if __name__ == '__main__':

   # apiID = cv2.getBackendName()



   # ret, frame = cap.read()
    getframe()
    getcamera()
    opencam()


