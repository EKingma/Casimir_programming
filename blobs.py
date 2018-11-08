###Image Manipulation 
"""Tasks
Simple filters
load the image "square.png" into a Numpy array
show it with pyplot.imshow
rotate the square by 45 degrees
apply a sobel (gradient) filter to show the edges in the image
sharpen the image using a gaussian filter (see page 9 here)

Feature identification
load the image "blobs.png" into a Numpy array
identify (label) the distinct blobs in the image
find the "centre of mass" of each of the blobs
plot the blobs and mark their centres of mass
estimate the area (in pixels) of each of the blobs
(note that each of these tasks is not as difficult as it first appears)"""

import numpy as np
from scipy import ndimage,misc
import imageio
import matplotlib.pyplot as plt

%matplotlib inline

a= imageio.imread("square.png") #reading the image onto an array
plt.imshow(a) #showing the figure
b=ndimage.rotate(a,45)#rotate the figure by 45 degrees
plt.figure() #create a new figure
plt.imshow(b) #plot the new rotated square
c=ndimage.sobel(a) # applying a sobel filter to the original image
plt.figure()
plt.imshow(c)
d=ndimage.gaussian_filter(a,sigma=5)
plt.imshow(d)

a=imageio.imread("blobs.png")
# to convert the image to grayscale, meaning we have one value per pixel, it makes easier for further analysis

def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.299, 0.587, 0.114])

a = rgb2gray(a)
plt.imshow(a)
#it finds the features of the image
b,num_feat=ndimage.label(a) 
plt.figure()
plt.imshow(b)

#find the centre of mass of each of the blobs

c = ndimage.find_objects(b)
d = []
for i in range(len(c)):
    d.append(ndimage.center_of_mass(b[c[i]]))
    
d=np.array(d)
x=np.linspace(0,1,len(d[:,0]))
#plotting the center of mass of each plot in a separate figure
for i in range(1,len(d)):
    plt.subplot(1,7,i)
    plt.scatter(d[i,1],d[i,0],s=20) #center of mass
    plt.imshow(b[c[i]]) #each blob


