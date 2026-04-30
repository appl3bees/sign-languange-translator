import os
import cv2
import mediapipe as mp


def openfolder(frame):
    folder_path = '/home/robobo/Downloads/dataset'
    files = os.listdir(folder_path)


    for letter_folder in files:
        letter_path = os.path.join(folder_path, letter_folder)
        images = os.listdir(letter_path)

        for image in images:
            image_path = os.path.join(letter_path, image)
            frame = cv2.imread(image_path)


            mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

            #test