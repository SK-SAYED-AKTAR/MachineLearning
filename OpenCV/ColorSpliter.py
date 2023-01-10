import cv2

img = cv2.imread("./images/rgb.png")
img = cv2.resize(img, (100, 100))
r = img[:, :, 2]
g = img[:, :, 1]
b = img[:, :, 0]
cv2.imshow("R Window", r)
cv2.imshow("G Window", g)
cv2.imshow("B Window", b)

cv2.waitKey(0)
cv2.destroyAllWindows()