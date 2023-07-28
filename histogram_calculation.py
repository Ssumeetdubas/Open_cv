import cv2 as cv
import matplotlib.pyplot as mt

img=cv.imread("my.jpg")
# cv.imshow("pic",img)
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

plot_graph=cv.calcHist([gray],[0],None,[255],[0,255])

plot_graph_colour=cv.calcHist([img],[0],None,[255],[0,255])
'''this takes five arguments 
1: list of imges 
2: index of the channel [0,1,2]
3: masking parameter 
4: histsize is nothing but the number of variables used for ploting 
5: range of all possible pixal values 

'''
mt.figure()
mt.title("hist")
mt.xlabel("bins")
mt.ylabel("no. of pixals ")
mt.plot(plot_graph)
mt.xlim(0,255)


mt.figure()
mt.title("hist")
mt.xlabel("bins")
mt.ylabel("no. of pixals ")
mt.plot(plot_graph_colour)
mt.xlim(0,255)
mt.show()

mt.show()
cv.waitKey(0)