import cv2
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(3, 800)
cap.set(4, 600)
while True:
    success, img = cap.read()
    hsvImg = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h, w, c = hsvImg.shape
    blackImg = np.zeros((h, w, c), dtype=np.uint8)

    ch, cw = h//2, w//2

    cv2.circle(img, (cw, ch), 10, (0, 0, 0), 10)

    hsv = hsvImg[ch, cw]

    blackImg[:] = hsv

    blackImg = cv2.cvtColor(blackImg, cv2.COLOR_HSV2RGB)
    

    stackImg = cv2.hconcat([img, blackImg])
    cv2.imshow("Color Detection", stackImg)
    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()