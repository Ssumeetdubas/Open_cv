import cv2 as cv
#converting the normal coloured image to the black and white image 

r=cv.imread("my.jpg")
# gray=cv.cvtColor(r,cv.COLOR_BGR2GRAY)

#bluring image 

# blur=cv.GaussianBlur(r,(11,11),cv.BORDER_DEFAULT)

# edge cascade 
#this represnt the image in doted form 
t=cv.resize(r,(300,300))
canny_1=cv.Canny(t,0,200)


cv.imshow("org",t)
cv.imshow("gry",canny_1)

cv.waitKey(0)
