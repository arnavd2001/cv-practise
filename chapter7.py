#colour detection
import cv2
import numpy as np
def empty(a):
    pass
cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars",640,240)
cv2.createTrackbar("Hue Min", "TrackBars",0,179, empty)
#we will need 6 values, as we will need saturation minimum, saturation maximum etc. so 6
cv2.createTrackbar("Hue Max", "TrackBars",0,179, empty)
cv2.createTrackbar("Sat Min", "TrackBars",0,179, empty)
cv2.createTrackbar("Sat Max", "TrackBars",0,179, empty)
cv2.createTrackbar("Val Min", "TrackBars",0,179, empty)
cv2.createTrackbar("Val Max", "TrackBars",0,179, empty)
while True:
    img = cv2.imread('sample.jpg')
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    h_min = cv2.getTrackbarPos("Hue Min", "TrackBars")
    h_max = cv2.getTrackbarPos("Hue Max", "TrackBars")
    s_min = cv2.getTrackbarPos("Sat Min", "TrackBars")
    s_max = cv2.getTrackbarPos("Sat Max", "TrackBars")
    v_min = cv2.getTrackbarPos("Val Min", "TrackBars")
    v_max = cv2.getTrackbarPos("Val Max", "TrackBars")
    cv2.imshow("Basic Output Image", img)
    cv2.imshow("Basic Output Image", imgHSV)
    cv2.waitKey(0)
