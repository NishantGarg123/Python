import cv2
img_path=r"img-path"


img = cv2.imread(img_path,1)        #second argument contain 3 flags either(0,-1,1){1->RGB , 0->gray scale  , -1->RGB and transparency}
img = cv2.resize(img , (500 , 400))
# print(img)

cv2.imshow('my-image',img)

cv2.waitKey(0)
cv2.destroyAllWindows()