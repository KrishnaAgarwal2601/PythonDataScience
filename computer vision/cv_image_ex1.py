import cv2
import numpy as np
im1 = cv2.imread("computer vision/image.jpeg")
print(im1.shape)
print(im1.ndim)
im1 = im1[0:1000:2]
cv2.imshow("image 1",im1)
cv2.waitKey(0)