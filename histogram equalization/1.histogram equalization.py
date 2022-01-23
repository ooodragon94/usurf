import cv2
import os
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread('uneq.jpg', cv2.IMREAD_GRAYSCALE)

M = image.shape[0]
N = image.shape[1]
L = 256
cdf = []
hv = []


res = [[0 for x in range(N)] for y in range(M)]
res = np.array(res)
'''
cv2.imshow('image',image)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''

hist_uneq = cv2.calcHist([image], [0], None, [L], [0,L])
plt.figure(figsize=(22, 22))
plt.subplot(151)
plt.plot(hist_uneq)
plt.title('hist_unequalized')

cdf = [hist_uneq[0]]
for index in range(L-1):
    cdf.append(hist_uneq[index+1] + cdf[index])
    
cdf = np.array(cdf)

plt.subplot(152)
plt.plot(cdf)
plt.title('cdf')

for index in range(L-1):
    hv.append(np.round(((cdf[index]-min(cdf))/(M*N-min(cdf)))*(L-1)))

plt.subplot(153)
plt.plot(hv)
plt.title('h(v)')

for row in range(M):
    for col in range(N):
        res[row][col] = hv[image[row][col]]
res = np.array(res, np.uint8)


hist_eq = cv2.calcHist([res], [0], None, [L], [0,L])
cdf = [hist_eq[0]]
for index in range(L-1):
    cdf.append(hist_eq[index+1] + cdf[index])
'''
plt.subplot(154)
plt.title('hist_equalized')
plt.plot(hist_eq)
plt.subplot(155)
plt.plot(cdf)
plt.title('cdf_equalized')

'''
plt.subplot(325)
plt.title('original')
plt.imshow(image,cmap='gray', vmin=0, vmax=255)

plt.subplot(326)
plt.title('equalized')
plt.imshow(res,cmap='gray', vmin=0, vmax=255)
