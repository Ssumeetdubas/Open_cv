import cv2 as cv
def delay_():
    a=1000
    b=1000
    for i in range(0,a):
        for j in range (0,b):
            pass
t=cv.VideoCapture(0)
while True:
    isTrue,frame=t.read()
    # y=cv.resize(frame,(20,20))
    cv.imshow("frame",frame)
    delay_()
    if cv.waitKey(20) & 0xff==ord('d'):
        break   