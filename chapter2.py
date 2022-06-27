#basic functionality in OpenCV projects
import cv2
import numpy as np
img=cv2.imread('samai.jpg')
#lets convert it to grayscale
kernel = np.ones((5,5), np.uint8)
img2gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)#will convert your image to different colour spaces, here to grayscale
img2blur = cv2.GaussianBlur(img, (7,7), 0 )#kernel size should be an odd number, sigmax is 0
img2blur_gray = cv2.GaussianBlur(img2gray, (7,7), 0 )
imgCanny = cv2.Canny(img, 100,100)#canny edge detector. Two Thresholds, values are 100 and 100
imgDilation = cv2.dilate(imgCanny, kernel, iterations =1 )#we need a kernel here, which is a matrix with 1s. We Need Numpy to manage the Matrix
imgEroded = cv2.erode(imgCanny, kernel, iterations =1 )
cv2.imshow("Eroded Canny",imgEroded)#the eroded image gives an output that has thinner lines  
#cv2.imshow("Dilated Canny",imgDilation)#the dilated image gives an output that has thicker lines  
#cv2.imshow("Canny",imgCanny)
#cv2.imshow("Grayscale",img2gray)
#cv2.imshow("Colour Blur", img2blur)
#cv2.imshow("Gray Blur", img2blur_gray)
cv2.waitKey(0)

