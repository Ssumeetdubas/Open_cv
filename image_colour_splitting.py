import cv2 as cv
import numpy as np 

t=cv.imread("gal.jpg")
# cv.imshow("orginal_image",t)
resize=cv.resize(t,(500,500))
cv.imshow("orignal",resize)

b,r,g=cv.split(resize) 
cv.imshow("blue",b)
cv.imshow("red",r)
cv.imshow("green",g)
y=cv.merge([b,r,g])
cv.imshow("merged",y)
cv.waitKey(0)