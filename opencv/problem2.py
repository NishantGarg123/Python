# Program to Display (Slide Show ) the images from a particular directory.

import cv2
import os

img_names = os.listdir('pictures')  #here pictures are the directory that contain the n number of pictures
# print(img_names)

for img_name in img_names :
    img = cv2.imread("pictures"+"/"+img_name)
    img = cv2.resize(img , (1280,720))
    cv2.imshow('image', img)
    cv2.waitKey(600)

cv2.destroyAllWindows()