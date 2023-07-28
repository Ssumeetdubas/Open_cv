import cv2 as cv 
import numpy as np

img=np.zeros((500,500),dtype='uint8')

rect=cv.rectangle(img.copy(),(30,30),(450,450),(255,0,0),thickness=-1)
circle=cv.circle(img.copy(),(250,250),250,(255,0,0),thickness=-1)
cv.imshow("circle",circle)
cv.imshow("rectangle",rect)

# AND this is bitwise anding operations which basically and the pixals and show the result
anding=cv.bitwise_and(rect,circle)
cv.imshow("AND",anding)

# OR this is bit wise or opertations which will or the pixals and show the result
oring=cv.bitwise_or(rect,circle)
cv.imshow("OR",oring)

# EXOR
exor=cv.bitwise_xor(rect,circle)
cv.imshow("exor",exor)

cv.waitKey(0)