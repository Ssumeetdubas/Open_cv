# contour is nothing but the boundries of the objects 
# this contour detections is usefull in shape analysis , object detections and recognition 

import cv2 as cv
import numpy as np 


img=cv.imread("gal.jpg")
# cv.imshow("gallery",img)


res=cv.resize(img,(600,600))
# cv.imshow("gallery",res)


blank=np.zeros(res.shape[:2], dtype="uint8")

# cv.imshow("bnalk",blank)

bw=cv.cvtColor(res,cv.COLOR_BGR2GRAY)
# cv.imshow("bw",bw)

blur=cv.GaussianBlur(res,(3,3),cv.BORDER_DEFAULT)
cv.imshow("bw",blur)

canny=cv.Canny(blur,100,100)
# cv.imshow("bw",canny)
thrs=cv.threshold(bw,200,255,cv.THRESH_BINARY)
#find contour method 
# cv.imshow("thresholded",thrs)
contours, hir=cv.findContours(canny,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE )
''' this method basically takes three parmters 
1: canny image 
2: how we want our contours (RETR_TREE,RETR_EXTERNAL,RETR_LIST)
3: contour approximantions method 

This findcontour method basically returs the two parameters 
1: contours: this is basically returs the list of all cordiants of the contorur 
2:
cv.RETER_TREE = if we want heirical contour 
cv.RETR_EXTERNL = if we wnat all external contours 
cv.RETR_LIST = if we want all the contours from the image  
'''

'''Other than using the canny method to find the conturs 
we can also use the threshold method to get the corners of the 
image 
'''

print("contours",len(contours))

# drawing image i.e converting the contour to image form

redr=cv.drawContours(blank,contours,-1,(255,0,0),1)
cv.imshow("redr",redr)
cv.waitKey(0)