# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import cv2 
# cascade is not neural network
# work on black and white images
 # We load the cascade for the face.
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# We load the cascade for the eyes.
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml') # We load the cascade for the eyes.

# Defining a function that will do the detections
# We create a function that takes as input the image in black and white (gray) and the original image (frame), and that will return the same image with the detector rectangles.
# the orignal image is frame and gray just defination for black and white
def detect(gray, frame):
    # now we need cordinates of rectangle that will detect the face
    # x and y= are cordinates of upper left corner
    # w= width of rectangle 
    # h = height of rectangle
    # We apply the detectMultiScale method from the face cascade to locate one or several faces in the image.
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    # first arg = b/w, 2nd = scale factor = size of image will be reduced to 1.3 times
    #3rd = min no of neighbors
    #1.3 and 5 ae selected beacuse it most of the time best value
    for (x, y, w, h) in faces: # For each detected face:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        # We paint a rectangle around the face.
        # 3rd arg = rgb color, 4th arg = rectangle border
        roi_gray = gray[y:y+h, x:x+w]
        # We get two the region of interest i.e. black and white image and other region is colored image because we will need this to draw a rectangle on colored img
        roi_color = frame[y:y+h, x:x+w]
        # We get the region of interest in the colored image.
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 3)
        # We apply the detectMultiScale method to locate one or several eyes in the image.
        for (ex, ey, ew, eh) in eyes: # For each detected eye:
            cv2.rectangle(roi_color,(ex, ey),(ex+ew, ey+eh), (0, 255, 0), 2) 
            # We paint a rectangle around the eyes, but inside the referential of the face.
        return frame # We return the image with the detector rectangles.
 
    # Doing some Face Recognition with the webcam
video_capture = cv2.VideoCapture(0)
 # We turn the webcam on.
 #video_capture is and object of class VideoCapture
 # arg is 0 if webcam is inbuilt and 1 if webcam is external device
while True: # We repeat infinitely (until break):
     _, frame = video_capture.read() # We get the last frame.
     #we will get two elemts but we are only interested in second so we put _ in first pos
     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
     # We do some colour transformations of frame.
     canvas = detect(gray, frame) 
     # We get the output of our detect function.
     cv2.imshow('Video', canvas)
     # We display the outputs in live stream format :>
     if cv2.waitKey(1) & 0xFF == ord('q'): # If we type q on the keyboard vedio stream will stop:
         break # We stop the loop.
         
     
video_capture.release() # We turn the webcam off.
cv2.destroyAllWindows() # We destroy all the windows inside which the images were displayed    
 
    
