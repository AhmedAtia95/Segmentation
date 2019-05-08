from skimage.color import rgb2gray
import numpy as np
import cv2
import matplotlib.pyplot as plt
from scipy import ndimage

#Open and plot real img
image = plt.imread('messi.jpg')
plt.figure()
plt.imshow(image)
plt.colorbar()
plt.show()

#convert image to gray scale
grayimg = rgb2gray(image)
plt.figure()
plt.imshow(grayimg, cmap="gray")
plt.colorbar()
plt.show()

#image size
grayimg.shape  # (192,263)

#User inputs threshold value in range 0-1
x = input("Input the threshold value from 0 to 1  -->  ")
y = float(x)

#img matrix
#print("grayimg = " , grayimg)

#Convert image matrix to array
gray_r = grayimg.reshape(grayimg.shape[0]*grayimg.shape[1])
#print("gray_r" , gray_r)

#Apply threshold value
for i in range(gray_r.shape[0]):
    if gray_r[i] > y:
        gray_r[i] = 1
    else:
        gray_r[i] = 0
plt.figure()
plt.imshow(grayimg, cmap="Greys_r")
plt.colorbar()
plt.show()

