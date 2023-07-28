import cv2 as cv 

t=cv.imread("gal.jpg")
sized=cv.resize(t,(500,500))

# normal bluring technique
cv.imshow("resized",sized)
normal_blur=cv.blur(sized,(7,7))
#                         the odd vale is passed in the brackets 
cv.imshow("normal blured",normal_blur)

# gaussian blur techinque 
gaussian_blur=cv.GaussianBlur(sized,(7,7),0)
cv.imshow("gaussina blur",gaussian_blur)

# median blur techinque
median_blur=cv.medianBlur(sized,3)
# in this median blur we just pass the interger value it automatically gets the another interger
# this is smuj over the orignal paintings 
# this bluring thechnique is not much suitable for the higher kernal size like 7 
cv.imshow("median blur",median_blur)

# bilateral bluring 
# this is mostly used in advanced computer vision projects 
# this bluring technique retains the edges of the image 
bilateral_blurring=cv.bilateralFilter(sized,10,35,25)
cv.imshow("bilateral_bluring",bilateral_blurring)
# this basically removes all the textures from the picture and smooths every thing this 
# basically looks like painting 

cv.waitKey(0)