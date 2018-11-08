#libraries import

import numpy as np
from scipy import ndimage,misc
import imageio
import matplotlib.pyplot as plt
import PIL
from PIL import Image
import cv2
from skimage import data, color
from skimage.transform import hough_circle, hough_circle_peaks
from skimage.feature import canny
from skimage.draw import circle_perimeter
from skimage.util import img_as_ubyte


# Load picture and detect edges
image = imageio.imread("results_L3.jpg")

#convert to grayscale
image = color.rgb2gray(image)

#sx = ndimage.sobel(image, axis=0, mode='constant')
#sy = ndimage.sobel(image, axis=1, mode='constant')
#edges = np.hypot(sx, sy)

edges = canny(image, sigma=1.7)# this work better
plt.imshow(edges)

# Detect two radii
hough_radii = np.arange(70, 120, 2)
hough_res = hough_circle(edges, hough_radii)

# Select the most prominent 10 circles
accums, cx, cy, radii = hough_circle_peaks(hough_res, hough_radii,
                                           total_num_peaks=10)

# Draw them
fig, ax = plt.subplots(ncols=1, nrows=1, figsize=(25, 20))
image = color.gray2rgb(image)
for center_y, center_x, radius in zip(cy, cx, radii):
    circle = plt.Circle((center_x, center_y), radius, color='r')
    ax.add_artist(circle)
#     circy, circx = circle_perimeter(center_y, center_x, radius)
#     image[circy, circx] = (220, 20, 20)

ax.imshow(image, cmap=plt.cm.gray)
plt.show()

list(zip(cy, cx, radii)) # list of all the center and radii of the detected circles

####Histogram############
image=Image.open("results_L3.jpg")
image.show()
h=image.histogram()
plt.plot(h)

# Take only the Red counts

l1 = h[0:256]

# Take only the Blue counts

l2 = h[256:512]

# Take only the Green counts

l3 =h[512:768]

for i in range(1, 256):

    plt.bar(i, l1[i], color ='r', edgecolor='r', alpha=0.3)
    plt.bar(i, l2[i], color ='b', edgecolor='b', alpha=0.3)
    plt.bar(i, l3[i], color ='g', edgecolor='g', alpha=0.3)
