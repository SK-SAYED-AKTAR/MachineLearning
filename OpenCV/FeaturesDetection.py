import cv2
import numpy as np

img = cv2.imread("./images/football.png")
grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

orb = cv2.ORB_create()
kp, des = orb.compute(grayImg, None)
orb_img = cv2.drawKeypoints(img, kp, None, color=(255,0,0), flags=0)


sift = cv2.SIFT_create()
kp = sift.detect(grayImg, None)
shift_img=cv2.drawKeypoints(img, kp, None)

# surf = cv2.xfeatures2d.SURF_create()
# kp, des = surf.detectAndCompute(grayImg,None)
# surf_img=cv2.drawKeypoints(grayImg, kp, img)

cv2.imshow("Original", img)
cv2.imshow("ORB Features Detection", orb_img)
cv2.imshow("SHIFT Features Detection", shift_img)
# cv2.imshow("SURF Features Detection", surf_img)
cv2.waitKey(0)
cv2.destroyAllWindows()