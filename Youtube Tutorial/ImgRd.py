import cv2

# img = cv2.imread("./images/panda.jpg", 0) # BGR -> Blue, Green, Red
img = cv2.imread("./images/panda.jpg") # BGR -> Blue, Green, Red
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# RGB = Red, Green, Blue
img2 = cv2.resize(img, (800, 600))
gray_img = cv2.resize(gray_img, (800, 600))

cv2.imwrite("./images/grayimg.jpg", gray_img)

# cv2.imshow("Original", img)
cv2.imshow("Sayed", img2)
cv2.imshow("Gray image", gray_img)

k = cv2.waitKey(0)
print("You have pressed:",k)
