import cv2

cap = cv2.VideoCapture(0)
print(cap.get(3), cap.get(4))
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
vid_codec = cv2.VideoWriter_fourcc(*"XVID")
output = cv2.VideoWriter("MyVideo.mkv", vid_codec, 6.5, (frame_width, frame_height))

if cap.isOpened() == True:
    while True:
        ret, frm = cap.read()
        if ret:
            output.write(frm)
            cv2.imshow("The Recorder", frm)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()

