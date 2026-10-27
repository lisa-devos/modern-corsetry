import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from radio_utils import *

# ########################## Read data ##########################
# img = cv.imread("../../radios/31-17-2027-frontal.jpg")
# img = img[:,:,0]

# ###############################################################
# ####################### THRESHOLDING ##########################
# ###############################################################

# ################### Image histogram ###########################
# hist,bin_edges = np.histogram(img,bins=255)
# plt.stairs(hist,bin_edges)
# plt.title("Histogram of radiography image")

# ################### Split into rectangles #####################

# valleys,rectangles = make_rectangles(img)
# print(valleys)
# print(rectangles)
# plt.figure()
# plt.imshow(img,cmap='gray')
# for v in valleys:
#     plt.plot([0,img.shape[1]],[v,v],color='red')

# plt.figure()
# count,edges = vertical_means(img)
# plt.stairs(count,edges,color='hotpink')
# for v in valleys:
#     plt.plot([v,v],[0,max(count)],color='red')


# ############# Thresholding in each rectangle ################
# # for r in rectangles[1:]:
# #     img_rect = img[r[0]:r[1],:]
# #     _,img_rect = cv.threshold(img_rect,8,255,3)
# #     img_res = thresholding(img_rect)
# #     plt.figure()
# #     plt.subplot(2,1,1)
# #     plt.imshow(img_rect,cmap='gray')
# #     plt.subplot(2,1,2)
# #     plt.imshow(img_res,cmap='gray')

# # Final thresholding
# thresholds = [56,101,125]
# #Epaules th=56
# #Poitrine th=101
# #Bassin th=125
# rectangles = rectangles[1:]
# for r in range(len(rectangles)):
#     re = rectangles[r]
#     img_rect = img[re[0]:re[1],:]
#     _,img_rect = cv.threshold(img_rect,thresholds[r],255,3)
#     cv.imwrite(f"radio_rect{r+1}.png",img_rect)

###############################################################
################## MATHEMATICAL MORPHOLOGY ####################
###############################################################

# img = cv.imread("radio_rect1.png")
# img = img[:,:,0]
# _,img = cv.threshold(img,50,255,0)



# def open(img,ker,iter=1):
#     img_res = img
#     for _ in range(iter):
#         img_res = cv.dilate(cv.erode(img_res,ker),ker)
#     return img_res
# def close(img,ker,iter=1):
#     img_res = img
#     for _ in range(iter):
#         img_res = cv.erode(cv.dilate(img_res,ker),ker)
#     return img_res

# elements = [cv.MORPH_RECT,cv.MORPH_CROSS,cv.MORPH_ELLIPSE]
# experiments = [[cv.MORPH_RECT,(1,4),1],
#                [cv.MORPH_RECT,(4,1),1],
#                [cv.MORPH_CROSS,(3,3),1],
#                [cv.MORPH_ELLIPSE,(1,4),1],
#                [cv.MORPH_ELLIPSE,(4,1),1],
#                [cv.MORPH_ELLIPSE,(3,3),1],
#                ]

# plt.figure()
# for k in range(len(experiments)):
    
#     ker = cv.getStructuringElement(experiments[k][0],experiments[k][1])
#     plt.subplot(len(experiments),3,3*k+1)
#     plt.imshow(img,cmap="gray")
#     plt.subplot(len(experiments),3,3*k+2)
#     plt.imshow(img-open(img, ker,iter=experiments[k][2]),cmap="gray")
#     plt.xlabel("Opening")
#     plt.subplot(len(experiments),3,3*k+3)
#     plt.imshow(img-close(img, ker,iter=experiments[k][2]),cmap="gray")
#     plt.xlabel("Closing")

# ker1 = cv.getStructuringElement(cv.MORPH_RECT,(1,4))
# img1 = img-open(img, ker1,iter=1)
# ker2 = cv.getStructuringElement(cv.MORPH_RECT,(4,1))
# img2 = img-open(img, ker2,iter=1)
# _,contours = cv.threshold(img1 + img2,1,2,0)
# plt.figure()
# plt.imshow(contours,cmap='gray')
# cv.imwrite("contours_rect1.png",contours*255)

img1 = cv.imread("contours_rect1.png")
img2 = cv.imread("contours_rect2.png")
img3 = cv.imread("contours_rect3.png")

img = np.concatenate([img1,img2,img3],axis=0)
plt.imshow(img)
cv.imwrite("contours.png",img)


plt.show()

