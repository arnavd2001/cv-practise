#shapes and texts
#how to draw shapes on images, how to draw text on images
import cv2
import numpy as np
img = np.zeros((512,512,3),np.uint8)#512,512,3 is giving us a 3D layout to the image
#uint gives us values from 0 to 255
#print(img.shape)
#img[200:300, 100:350]=255,0,0#cropping wale limits of height and width respectively
cv2.imshow("empty black image",img)
#how to create lines
cv2.line(img, (0,0), (300,300), (0,255,0), 3)#starting point and the ending point, then we define the colour, and then we define the thickness
cv2.imshow("empty black image with a green line",img)
cv2.line(img, (0,0), (img.shape[1],img.shape[0]), (0,255,0), 3)#starting point and the ending point, then we define the colour, and then we define the thickness
cv2.imshow("empty black image with a green line across the whole image",img)

cv2.line(img, (0,0), (300,300), (0,255,0), 3)#starting point and the ending point, then we define the colour, and then we define the thickness
cv2.rectangle(img, (0,0), (250,350), (0,0,255), 3)#cv2.FILLED didnt workout
cv2.circle(img,(400,50), 40, (255,25,0), 5)#centre, radius, colour, thickness
#now lets put the text
cv2.putText(img, "OPEN CV",(300,200), cv2.FONT_HERSHEY_COMPLEX, 1, (0,21,211), 3 )#text, origin, font, scale, colour, thickness
#the scale can be in decimals too
cv2.imshow("plot",img)


cv2.waitKey(0)