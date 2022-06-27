#joining images
import cv2
import numpy as np
img = cv2.imread('sample.jpg')
hor_image = np.hstack((img,img))
ver_image = np.vstack((img,img))
cv2.imshow("Horizontal Image", hor_image)
cv2.imshow("Vertical Image", ver_image)
cv2.waitKey(0)
#you can use the image stacking functions 
#to stack more than one images in a matrix type format
