import numpy as np
import cv2

def empty(x):
    pass

cv2.namedWindow("Tracker")

img = 10*np.ones((600, 800, 3), dtype = np.float32)
print(img)

cv2.createTrackbar("B", "Tracker", 0, 179, empty)
cv2.createTrackbar("G", "Tracker", 0, 255, empty)
cv2.createTrackbar("R", "Tracker", 0, 255, empty)

while True:
    B = cv2.getTrackbarPos("B", "Tracker")
    G = cv2.getTrackbarPos("G", "Tracker")
    R = cv2.getTrackbarPos("R", "Tracker")
    img[:] = [B, G, R]

    cv2.imshow("Tracker", img)
    k = cv2.waitKey(1)
    if k == 27:
        break

cv2.destroyAllWindows()

