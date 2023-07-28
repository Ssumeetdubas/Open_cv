#there are basically two imprtant type of the edge detections 
# laplacian method 
# sobel method 
import cv2 as cv 
import numpy as np
t=cv.imread("my.jpg")
# cv.imshow("pic",t)

#laplacian
gray=cv.cvtColor(t,cv.COLOR_BGR2GRAY)
cv.imshow("gray",gray)
lap=cv.Laplacian(gray,cv.CV_64F)
lap=np.uint8(np.absolute(lap))
cv.imshow("laplacian",lap)
'''This laplacian basically compute the gradiant of the image 
Gradint: This is basically directional change in the intensity or colour of the image '''

# sobel 
# this basically comput the gradiant in both x and y direciton 

soble_x=cv.Sobel(gray,cv.CV_64F,1,0)
sobel_y=cv.Sobel(gray,cv.CV_64F,0,1)
combine=cv.bitwise_or(soble_x,sobel_y)
cv.imshow("sobel_x",soble_x)
cv.imshow("sobel_y",sobel_y)
cv.imshow("combine",combine)

cv.waitKey(0)