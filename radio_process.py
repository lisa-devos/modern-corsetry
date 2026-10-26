import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("../../radios/31-17-2027-frontal.jpg")
print(img.shape,np.min(img),np.max(img))
img = img[:,:,0]

hist,bin_edges = np.histogram(img,bins=255)
plt.stairs(hist,bin_edges)

plt.figure()
thresholds=[20,56,75,94,110,125,150]
plt.subplot(1,len(thresholds)+1,1)
plt.imshow(img,cmap='gray')
for k in range(len(thresholds)):
    _,th_img = cv.threshold(img,thresholds[k],255,3)
    plt.subplot(1,len(thresholds)+1,k+2)
    plt.imshow(th_img,cmap='gray')
    plt.xlabel(str(thresholds[k]))


upper_img = img[100:400,:280]
hist,bin_edges = np.histogram(upper_img,bins=255)
plt.figure()
plt.stairs(hist,bin_edges)


plt.figure()
thresholds=[35,52,66]
plt.subplot(1,len(thresholds)+1,1)
plt.imshow(upper_img,cmap='gray')
for k in range(len(thresholds)):
    _,th_img = cv.threshold(upper_img,thresholds[k],255,3)
    plt.subplot(1,len(thresholds)+1,k+2)
    plt.imshow(th_img,cmap='gray')
    plt.xlabel(str(thresholds[k]))
plt.show()

