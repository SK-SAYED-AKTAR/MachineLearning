import cv2

img = cv2.imread("./images/panda.jpg") #BGR

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

img = cv2.resize(img, (600, 300))
gray_img = cv2.resize(gray_img, (600, 300))

# img[0:200, 0:50, :] = (0, 255, 255)

cv2.imwrite("./images/gray.jpg", gray_img)

cv2.imshow("My Image", img)
cv2.imshow("My Gray Image", gray_img)

k = cv2.waitKey(0)

print("You have pressed", k)