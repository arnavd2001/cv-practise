#opencvtutorial - Cameras, Webcam, Images
import cv2
from cv2 import waitKey
"""
importing an image
img=cv2.imread('samai.jpg')
cv2.imshow("Output",img)
#waitkey. if argument is 0, infinite delay. if a natural no. that many miliseconds
cv2.waitKey(0)"""
cap = cv2.VideoCapture(0)
cap.set(3,640)#width
cap.set(4,480)#height
cap.set(10,50)#setting the brightness
while True:
    success, img = cap.read()
    cv2.imshow("VideoCamera",img)
    if 0xFF ==ord('q') & cv2.waitKey(1):
        break
