import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True: 
    _, frame = cap.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_blue = np.array([50, 150, 30])
    upper_blue = np.array([180, 255, 255])

    #Mask out other colors to reamin with blue
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    res = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow('filtered', res)
    cv2.imshow('frame',frame)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()    