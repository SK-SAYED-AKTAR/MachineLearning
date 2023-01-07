import cv2
import numpy as np

img = cv2.imread("./images/fruits.jpg")
img = cv2.resize(img, (800, 600))
imgHsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower_blue = np.array([90, 50, 70])
upper_blue = np.array([128, 255, 255])

lower_red = np.array([159, 50, 70])
upper_red = np.array([180, 255, 255])

# mask = cv2.inRange(imgHsv, lower_blue, upper_blue)
mask = cv2.inRange(imgHsv, lower_red, upper_red)

contours, h = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

cv2.drawContours(image=img, contours=contours, contourIdx=-1, color=(255, 0, 0), thickness=5)


cv2.imshow("Sayed", img)
cv2.imshow("The Mask", mask)
cv2.waitKey(0)
cv2.destroyAllWindows()