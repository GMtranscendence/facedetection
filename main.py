import cv2 as cv
import numpy as np


def resize(frame, scale=10):
    width = frame.shape[1] * scale
    heigth = frame.shape[0]
    dimensions = (width, heigth)

    return cv.resize(frame, dimensions)


capture = cv.VideoCapture(0)
while True:
    isTrue, frame = capture.read()
    resized_frame = resize(frame)
    cv.imshow('webcam',resized_frame)
    if cv.waitKey(1) == ord('q'):
        break
capture.release()
cv.destroyAllWindows()
