import cv2 as cv
import matplotlib as mt
t=cv.imread("gal.jpg")

# cv.imshow("gallery",t)
resize=cv.resize(t,(500,500))
cv.imshow("resized",resize)

# BGR to GRAY
gray=cv.cvtColor(resize,cv.COLOR_BGR2GRAY)
cv.imshow("gray",gray)

# BGR to HSV
hsv=cv.cvtColor(resize,cv.COLOR_BGR2HSV)
cv.imshow("HSV",hsv)

#BGR to LAB 
lab=cv.cvtColor(resize,cv.COLOR_BGR2LAB)
cv.imshow("lab",lab)

# BGR to RGB
rgb=cv.cvtColor(resize,cv.COLOR_BGR2RGB)
cv.imshow("rgb",rgb)

# display image in matplotlib

# HSV to BGR 
hsv2bgr=cv.cvtColor(hsv,cv.COLOR_HSV2BGR)
cv.imshow("hsv2bgr",hsv2bgr)
cv.waitKey(0)