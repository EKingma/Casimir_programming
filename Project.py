import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from scipy import ndimage

def rgb2gray(rgb):
    gray = np.dot(rgb[...,:3],[0.299,0.587,0.114])
    return gray


img = mpimg.imread('img/results_L3.jpg')
imggray = rgb2gray(img)
imgplot = plt.imshow(imggray, cmap = plt.get_cmap('gray'))

sx = ndimage.sobel(imggray, axis=0, mode='constant')
sy = ndimage.sobel(imggray, axis=1, mode='constant')
sob = np.hypot(sx, sy)

sob = sob/np.max(sob)
sob_ups = (sob > 0.3) * sob
sob_min = np.min(sob_ups[sob_ups>0])
sob_ups = (sob_ups-sob_min)/(np.max(sob_ups)-sob_min)
sob_ups[sob_ups>0] = 1


plt.imshow(sob_ups)
print(np.min(sob_ups[sob_ups>0]))
