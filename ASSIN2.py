import cv2
img=cv2.imread("D:\wp2568544.jpg")
img = cv2.resize(img, (720, 600))
print(img)
h = img.shape[0]
w = img.shape[1]
print (h,"",w)
c=(h/2,w/2)
m=cv2.getRotationMatrix2D(center=c,angle=-90,scale=.5)
n=cv2.warpAffine(src=img,M=m,dsize=(h,w))
cv2.imshow("rotate",n)
'''#Here is anti-clockwise rotation---- 
m=cv2.getRotationMatrix2D(center=c,angle=90,scale=.5)
n=cv2.warpAffine(src=img,M=m,dsize=(h,w))
cv2.imshow("rotate",n)'''
cv2.waitKey(0)
