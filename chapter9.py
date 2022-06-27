#facedetection
#viola and jones. -> positive faces + negative faces = XML Files
# OpenCV Cascades
import cv2
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
img = cv2.imread('arnav.jpg')
img = cv2.resize(img,[480,640])
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)#scale factor, minimum neighbors
for (x,y,w,h) in faces:
    cv2.rectangle(img, (x,y), (x+w,y+h),(255,0,6), 3)
cv2.imshow("Result", img)
cv2.waitKey(0)