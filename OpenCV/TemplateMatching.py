import cv2
import numpy as np

img = cv2.imread("./images/f_ground.jpeg")
grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
template = cv2.imread("./images/sayed.png", cv2.IMREAD_GRAYSCALE)

h, w = template.shape

result = cv2.matchTemplate(grayImg, template, cv2.TM_CCOEFF_NORMED)
loc = np.where(result >= 0.7)

pt1 = loc[1]
pt2 = loc[0]

for x, y in zip(pt1, pt2):
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 1)


cv2.imshow("The Window", img)
cv2.waitKey(0)