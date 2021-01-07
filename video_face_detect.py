import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

vid = cv2.VideoCapture(0) # 0 for primary webcam

while True:
    ret, frame = vid.read()
    grayframe = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(grayframe, 1.3, 5)

    #video is rendered frame by frame
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2)
        rect_color = grayframe[y:y+h, x:x+w]

    cv2.imshow('Detected', frame)

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

vid.release()
cv2.destroyAllWindows()