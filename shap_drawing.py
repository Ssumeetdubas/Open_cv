import cv2 as cv
import numpy as np

b=np.zeros((400,400,3),dtype='uint8')

# cv.imshow("b",b)
# b[23:340,0:55]=0,255,0 

#drawing rectangle 

# c=cv.rectangle(b,(0,0),(250,250),(255,0,0),thickness=3)

#                (x,y),( x  , y ),colour
#             (origin),(main_rect
# )

#cicrcle drawing 
# c=cv.circle(b,(24,24),10,(24,255,40),thickness=2)

#line drawing 
# c=cv.line(b,(34,78),(45,67),(255,45,55),thickness=4)

#text on image 

c=cv.putText(b,"this is me",(98,56),cv.FONT_HERSHEY_SIMPLEX,1.6,(255,0,255),thickness=10)
cv.imshow('Green',c)
cv.waitKey(0)