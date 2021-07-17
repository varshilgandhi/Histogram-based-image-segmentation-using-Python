# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 02:15:39 2021

@author: abc
"""

from skimage.restoration import denoise_nl_means,estimate_sigma
from skimage import img_as_float,img_as_ubyte,io

import numpy as np

from matplotlib import pyplot as plt

img = img_as_float(io.imread("C:\\Users\\abc\\Desktop\\image\\aeroplane\\test_image.jpg"))

sigma_est = np.mean(estimate_sigma(img,multichannel=True))

denoise = denoise_nl_means(img,h=1.15 * sigma_est,fast_mode = True,patch_size=5,
                           patch_distance=3,multichannel= True)

denoise_ubyte = img_as_ubyte(denoise)

#plt.imshow(denoise_ubyte,cmap='gray')

#plt.hist(denoise_ubyte.flat, bins=100,range=(0,100))

segm1= (denoise_ubyte <= 55)

#segm2 = (denoise_ubyte > 55) & (denoise_ubyte <= 110)

#segm3 = (denoise_ubyte > 110) & (denoise_ubyte <= 210)

#segm4 = (denoise_ubyte > 210) 

all_segments = np.zeros((denoise_ubyte.shape[0],denoise_ubyte.shape[1],3))

#all_segments[segm1] = (1,0,0)
#all_segments[segm2] = (0,1,0)
#all_segments[segm3] = (0,0,1)
#all_segments[segm4] = (1,1,0)

plt.imshow(all_segments)


















