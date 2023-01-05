import cv2 
import numpy as np

def handle_mouse(event, x, y, flag, params):
    global counter

    if counter < 4:
        if event == cv2.EVENT_LBUTTONDOWN:
            pt1[counter] = x, y
            cv2.circle(img, (x, y), 5, (0, 0, 255), cv2.FILLED)
            cv2.imshow("Sayed", img)
            counter += 1
    else:
        matrix = cv2.getPerspectiveTransform(pt1, pt2)
        output_img = cv2.warpPerspective(img, matrix, (w, h))
        cv2.imshow("Warpped image", output_img)
    





if __name__ == "__main__":
    # Declare some required variable
    w, h = 200, 200
    counter = 0
    pt1 = np.zeros((4, 2), dtype=np.float32)
    pt2 = np.array([[0, 0], [w, 0], [0, h], [w, h]], dtype=np.float32)

    # Load the image
    img = cv2.imread("./images/ai.png")
    img = cv2.resize(img, (600, 600))
    cv2.imshow("Sayed", img)

    # Set Mouse Callback
    cv2.setMouseCallback("Sayed", handle_mouse)
    cv2.waitKey(0)