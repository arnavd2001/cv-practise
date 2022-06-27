#warp perspective
import cv2
import numpy as np
#we use it to get a birds eye view of an image
img = cv2.imread('sample.jpg')
width, height = 100, 60
pts1=np.float32([[261,135],[504,135],[261,292],[504,292]])
#these corners can be taken from corners in MS Paint
pts2=np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix = cv2.getPerspectiveTransform(pts1,pts2)
imgOutput = cv2.warpPerspective(img, matrix, (width, height))
cv2.imshow("Image", img)
cv2.imshow("Output", imgOutput)
cv2.waitKey(0)