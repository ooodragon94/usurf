import cv2
import numpy as np
# from math import atan2 won't work with numpy
import sys #for no truncation on matrix
np.set_printoptions(threshold=sys.maxsize)
from matplotlib import pyplot as plt

from cannyfunctions import non_max_suppression
from cannyfunctions import threshold
from cannyfunctions import hysteresis


plt.figure(figsize=(7, 7))

gauss = np.array([[2,4,5,4,2],[4,9,12,8,4],[5,12,15,12,5],[4,9,12,9,4],[2,4,5,4,2]])
gauss = gauss * 1/159
#gauss *= 1/159 this won't work
sobelx = np.array([[-1,0,1],[-2,0,2],[-1,0,1]], dtype='f')
sobely = np.array([[1,2,1],[0,0,0],[-1,-2,-1]], dtype='f')

img = cv2.imread('lena.png', cv2.IMREAD_GRAYSCALE)

img = np.float32(img)

img_blur = cv2.filter2D(img,-1,gauss)

img_sobelx = cv2.filter2D(img_blur,-1,sobelx)
img_sobely = cv2.filter2D(img_blur,-1,sobely)

grad = np.hypot(img_sobelx, img_sobely) #finds l2 norm

'''
grad = grad / grad.max() * 255
plt.subplot(221)
plt.title('gradient')
plt.imshow(grad.astype(int), cmap='gray')
'''
angle = np.arctan2(img_sobely,img_sobelx)
'''
plt.subplot(222)
plt.title('suppressed')
'''
nms = non_max_suppression(grad, angle)

'''
plt.imshow(nms, cmap='gray')
'''
th, weak, strong = threshold(nms)
'''
plt.subplot(223)
plt.title('threshold')
plt.imshow(th, cmap='gray')
'''




hy=hysteresis(th, weak, use_stack=False)
plt.plot()
plt.title('hy')
plt.imshow(hy, cmap='gray')




'''
img = np.uint8(img) #need to change back to int to imshow
canny = cv2.Canny(img,100,200)
cv2.imshow('canny', canny)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''