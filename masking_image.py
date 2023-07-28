import cv2 as cv 
import numpy as np 

blank=np.zeros((500,500),dtype='uint8')

img=cv.imread("gal.jpg")

circle=cv.circle(blank,(200,100),80,(255,0,0),thickness=-1)
rectangle=cv.rectangle(blank,(200,200),(100,100),(255,0,0),thickness=-1)
resized=cv.resize(img,(500,500))
cv.imshow("blank",blank)
cv.imshow("org",resized)
shape_mask=cv.bitwise_and(circle,rectangle)

mask=cv.bitwise_and(resized,resized,mask=shape_mask)
cv.imshow("masked image ",mask)

cv.waitKey(0)