import cv2 as cv 

t=cv.imread("my.jpg")

def rot_img(img,angle,rotpoint=None):
    (height,width)=img.shape[:2]

    
    if rotpoint is None:
        rotpoint=(height//2,width//2)

    rotmat=cv.getRotationMatrix2D(rotpoint ,angle,1.0)
    dimension=(width,height)
    return cv.warpAffine(img,rotmat,dimension)

cv.imshow("org",t)

r=rot_img(t,45)
cv.imshow("rot",r)


# interpolations it the process of determining the unknown values that lies between two data points 

# image resizing 

# if you are enlarging the image then we use the inter_liner or inter_cubic 

#flipping 

r=cv.flip(t,0)
# flip code 
# 0= flip image vertically over x axise 
# 1 = flip image horizontally over the y axise this also called mirror image 
# -1= this flips both veritcally and horizontally 
cv.imshow("fliped",r)

cv.waitKey(0)