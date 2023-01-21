import cv2
# import numpy as np


# img = cv2.imread("./images/panda.jpg")
# color_img = cv2.imread("./images/color.jpg")
# color_img = cv2.resize(color_img, (200, 100))
# print(img.shape) # 900, 1600 ===> H, W
# crp_img = img[600:700, 600:800]
# img[0:100, 0:200] = color_img
# cv2.imshow("Image", img)
# cv2.imshow("Cropped Image", crp_img)

# cv2.waitKey(0)


cap = cv2.VideoCapture("./video/fast_move.mp4")


while True:
    success, img = cap.read()
    if success == True:
        cv2.imshow("My Video", img)
        cv2.waitKey(1)
    else:
        print("Video is end")
        break



