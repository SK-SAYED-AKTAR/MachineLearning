import cv2
import numpy as np
from PIL import Image

def nothing(x):
    pass


cv2.namedWindow("Original Image")
l_h = cv2.createTrackbar("L-H", "Original Image", 0, 180, nothing)
l_s = cv2.createTrackbar("L-S", "Original Image", 0, 255, nothing)
l_v = cv2.createTrackbar("L-V", "Original Image", 0, 255, nothing)
h_h = cv2.createTrackbar("H-H", "Original Image", 180, 180, nothing)
h_s = cv2.createTrackbar("H-S", "Original Image", 255, 255, nothing)
h_v = cv2.createTrackbar("H-V", "Original Image", 255, 255, nothing)


while True:
    img = cv2.imread("./images/color.jpg")
    img = cv2.resize(img, (800, 400))
    hsvImg = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lh = cv2.getTrackbarPos("L-H", "Original Image")
    ls = cv2.getTrackbarPos("L-S", "Original Image")
    lv = cv2.getTrackbarPos("L-V", "Original Image")
    hh = cv2.getTrackbarPos("H-V", "Original Image")
    hs = cv2.getTrackbarPos("H-S", "Original Image")
    hv = cv2.getTrackbarPos("H-V", "Original Image")

    lower = np.array([lh, ls, lv])
    upper = np.array([hh, hs, hv])
    mask = cv2.inRange(hsvImg, lower, upper)

    im = Image.fromarray(mask)
    if im.getbbox() != None:
        x1, y1, x2, y2 = im.getbbox()
        print(x1, y1, x2, y2)
        cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 5)
    cv2.imshow("Original Image", img)
    cv2.imshow("Mask Image", mask)
    key = cv2.waitKey(1)
    if key == 27:
        break

cv2.destroyAllWindows()