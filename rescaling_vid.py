import cv2 as cv

t=cv.VideoCapture(0)

while True:
    isTrue,y=t.read()
    z=cv.resize(y,(720,360))
    cv.imshow("rez",z)

    if cv.waitKey(20) & 0xff==ord('d'):
        break