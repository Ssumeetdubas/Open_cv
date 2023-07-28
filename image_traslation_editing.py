import cv2 as cv 
import numpy as np
t=cv.imread('my.jpg')

def traslate(img,x,y):
    trasmat=np.float32([[1,0,x],[0,1,y]])
    dimensions=(img.shape[1],img.shape[0])
    return cv.warpAffine(img,trasmat,dimensions)

#  -x  this will shift image to left 
#  -y this will shift image to up
#   x this will shift image to right
#   y this will shift image to down 

q=traslate(t,100,-100)

cv.imshow("this",t)
cv.imshow("traslated",q)
cv.waitKey(0)

#image traslations is nothing but the shifting the image 
# as we want to this is done using the pixal values negative and positve values can be used 
 