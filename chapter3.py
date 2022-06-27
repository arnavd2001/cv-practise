#resize and cropping
#in normal cartesian coordinate system the positive X axis is in the East Direction, and Positive Y axis is in the North Direction
#But in Open CV, the Positive Y Axis is in the South direction
import cv2
import numpy as np
# for resizing the image we need to knoe the current size of the imahe
img = cv2.imread('sample.jpg')
"""
imgResize = cv2.resize(img, (300,200))
print(img.shape)
cv2.imshow('sample 480p image', img)
cv2.imshow('sample 480p image resized', imgResize)
#you can even increase the size of the image, but that doesnt increase the quality of the image
print(imgResize.shape)
cv2.waitKey(0)
"""
#Cropping
imgCropped = img[0:200, 200:570 ]#you dont require a opencv function for that.
#here too, height first, and then width
cv2.imshow('Cropped Image', imgCropped)
cv2.waitKey(0)
