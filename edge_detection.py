import cv2

webcam = cv2.VideoCapture(0)

while True:
    _, frame = cv2.imread(frame)

    edges = cv2.Canny(frame, 100, 200)

    cv2.imshow('edges', edges)

    k = cv2.waitKey(5) & 0xff

    # Close when escape key is pressed
    if k == 27:
        break

webcam.release()
cv2.destroyAllWindows()