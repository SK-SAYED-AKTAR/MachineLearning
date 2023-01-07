import cv2

def empty(a):
    print("Empty Called", a)

cap = cv2.VideoCapture(0)
cap.set(3, 800)
cap.set(4, 600)

cv2.namedWindow("Sayed")
cv2.createTrackbar("Color", "Sayed", 0, 1, empty)

while True:
    _, img = cap.read()
    newImg = img.copy()
    if _:
        color = cv2.getTrackbarPos("Color", "Sayed")
        if color == 1:
            newImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        else:
            pass

        cv2.imshow("Sayed", newImg)
        key = cv2.waitKey(1)
        if key == 27:
            break

cap.release()
cv2.destroyAllWindows()