import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

webcam = cv2.VideoCapture(0)

while True:
    _, frame = webcam.read()
    grayframe = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(grayframe, 1.3, 5)
    for (x, y ,w, h) in faces:
        mask = np.zeros(frame.shape[:2],np.uint8)
        mask[y:y+h, x:x+w] = 255
        res = cv2.bitwise_and(frame,frame,mask = mask)
        # mask= np.array(face)
        # print(mask)
        # res = cv2.bitwise_and(frame, frame)
        # cv2.rectangle(frame, (x,y), (x+w, y+h), (0,0,0), -1)
        # rect_color = grayframe[y:y+h, x:x+w]
        cv2.imshow('masked', res)

    # cv2.imshow('masked', res)

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

webcam.release()
cv2.destroyAllWindows()