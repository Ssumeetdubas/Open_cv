import cv2 as cv
import sys
def re_scalling(frame,scale=0.200):
    height=int(frame.shape[0]*scale)        #height is acessed using the frame.shape[0]
    width=int(frame.shape[1]*scale)         #width is acessed using the frame.shape[1]
    dimensions=(height,width)
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

t=cv.imread("pp.png")
# cv.imshow("org",t)
# a=re_scalling(t)

b=cv.resize(t,(200,200))   
cv.imshow("resized",b)
cv.waitKey(0)

