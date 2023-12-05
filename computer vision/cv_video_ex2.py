import cv2
import numpy as np

video = cv2.VideoCapture(r"c:\Users\acer\Videos\Captures\DATA SCIENCE revised set.pdf - Google Drive - Google Chrome 2023-09-05 22-56-51.mp4")
while True:
    status, frame = video.read()
    if not status: break
    frame = cv2.resize(frame, (0,0), fx=0.3, fy=0.3)
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    inv_frame = rgb_frame * 255
    print('rgb',rgb_frame[:1, :2])
    print('invert',inv_frame[:1, :2])
    cv2.imshow("Video output", frame)
    cv2.imshow("Video output2", gray_frame)
    cv2.imshow("Video output3", rgb_frame)
    cv2.imshow("Video output4", inv_frame)
    if cv2.waitKey(1) == 27: #escape key
        break
video.release()
cv2.destroyAllWindows()