import cv2 as cv
t=cv.imread("ty.png")
cv.imshow("this",t)

k=cv.waitKey(0)   # this triggres the wait time of the window 
print(t.shape)

z=cv.imread("pp.png")
if k=="s":      
    cv.show("nothing",z)
    cv.waitkey(1000)

    #also if we provide the wrong path we get the error of the assersrrstion fail error -215

    