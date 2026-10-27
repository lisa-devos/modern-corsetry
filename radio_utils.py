import numpy as np
from scipy.signal import savgol_filter
import cv2 as cv
import matplotlib.pyplot as plt

def vertical_means(img):
    edges = [k for k in range(img.shape[0]+1)]
    count = []
    for k in range(img.shape[0]):
        count.append(np.mean(img[k,:]))
    
    return count,edges

def find_valleys(signal):
    valleys = []
    for k in range(1,len(signal)-1):
        if (signal[k-1]>signal[k] and signal[k]<signal[k+1]):
            valleys.append(k)
    return valleys

def make_rectangles(img,max_div=5):
    count,edges = vertical_means(img)
    div=100
    k=0
    while div>max_div and k<1000:
        count = savgol_filter(count, window_length=11, polyorder=3)
        valleys = find_valleys(count)
        div = len(valleys)+2
        k+=1
    # check if two div are too close
    inter = img.shape[1]*0.2
    for k in range(1, len(valleys)):
        if abs(valleys[k-1]-valleys[k]) < inter:
            valleys[k] = int(np.mean(valleys[k-1:k+1]))
            del valleys[k-1]
    # rectangles
    val=[0]+valleys+[img.shape[0]]
    rectangles=[]
    for k in range(len(val)-1):
        rectangles.append([val[k],val[k+1]])
    return valleys,rectangles

def thresholding(img,fig=True,thresholds=None):
    if thresholds==None:
        count,edges = np.histogram(img,bins=255)
        # find maximum 10 thresholds
        div=100
        k=0
        while div>10 and k<1000:
            count = savgol_filter(count, window_length=11, polyorder=3)
            thresholds = find_valleys(count)
            div = len(thresholds)
            k+=1

    img_res=np.zeros(img.shape)
    if fig==True:
        plt.figure()
        plt.subplot(1,len(thresholds)+1,1)
        plt.imshow(img,cmap='gray')
    for k in range(len(thresholds)):
        _,th_img = cv.threshold(img,thresholds[k],255,3)
        img_res += th_img
        if fig==True:
            plt.subplot(1,len(thresholds)+1,k+2)
            plt.imshow(th_img,cmap='gray')
            plt.xlabel(f"th={thresholds[k]}")
    return img_res

    

