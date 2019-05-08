from skimage.color import rgb2gray
import numpy as np
import cv2
import matplotlib.pyplot as plt
from scipy import ndimage
from sklearn.cluster import KMeans


image = plt.imread('1.jpeg')/255  # dividing by 255 to bring the pixel values between 0 and 1
print(image.shape)
plt.figure()
plt.imshow(image)
plt.colorbar()
plt.show()

image_n = image.reshape(image.shape[0]*image.shape[1], image.shape[2])
print(image_n.shape)

kmeans = KMeans(n_clusters=5, random_state=0).fit(image_n)
image_n2 = kmeans.cluster_centers_[kmeans.labels_]
plt.figure()
plt.imshow(image_n2)
plt.colorbar()
plt.show()