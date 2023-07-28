'''
Harrcasscasde is nothing but the algor that detetctes the object in the image 
irrespective of there scale and location 

this algorithm is not so complex can be used to detect the objects like car,bike,building,etc

'''
import cv2 as cv 

t=cv.imread("my.jpg")

gray=cv.cvtColor(t,cv.COLOR_BGR2GRAY)

# cv.imshow("gray",gray)

haar_cascade=cv.CascadeClassifier("facial.xml")

face_rec=haar_cascade.detectMultiScale(gray,scaleFactor=1.3,minNeighbors=3)
for (w,x,y,z) in face_rec:
    cv.rectangle(t,(w,x),(w+y,x+z),(0,255,0),thickness=2)
print(face_rec)
cv.imshow("pic",t)
cv.waitKey(0)