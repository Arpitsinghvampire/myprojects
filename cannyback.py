#The canny edge detection has five steps
#noise reduction
#gradient calculation
#non max suppression
#double threshold
# edge tracking hysterisis
import numpy as np
import cv2 as cv

from scipy import ndimage

def gaussian_kernel(size,sigma=1):
    size=int(size)//2
    x,y=np.mgrid[-size:size+1,-size:size+1]
    normal=1/(2*np.pi*sigma**2)
    g=normal*np.exp(-(x**2+y**2)/2*sigma**2)
    return g
#in the next step we would be applying the gradient calculation part
#so we would be applying the sobel filter 
#we apply filters to highlight the intensity change in both directions the x axis and the y axis

def sobel_filters(img):
    kx=np.array([[-1,0,1],[-2,0,2],[-1,0,1]])
    ky=np.array([[1,2,1],[0,0,0],[-1,-2,-1]])

    ix=ndimage.filters.convolve(img,kx)
    iy=ndimage.filters.convolve(img,ky)

    g=np.hypot(ix,iy)
    g=g/g.max()*255
    theta=np.arctan2(iy,ix)

    return g,theta

#now we go for non max suppression
def non_max_suppression(img, D):
    M, N = img.shape
    Z = np.zeros((M,N), dtype=np.int32)
    angle = D * 180. / np.pi
    angle[angle < 0] += 180

    
    for i in range(1,M-1):
        for j in range(1,N-1):
            try:
                q = 255
                r = 255
                
               #angle 0
                if (0 <= angle[i,j] < 22.5) or (157.5 <= angle[i,j] <= 180):
                    q = img[i, j+1]
                    r = img[i, j-1]
                #angle 45
                elif (22.5 <= angle[i,j] < 67.5):
                    q = img[i+1, j-1]
                    r = img[i-1, j+1]
                #angle 90
                elif (67.5 <= angle[i,j] < 112.5):
                    q = img[i+1, j]
                    r = img[i-1, j]
                #angle 135
                elif (112.5 <= angle[i,j] < 157.5):
                    q = img[i-1, j-1]
                    r = img[i+1, j+1]

                if (img[i,j] >= q) and (img[i,j] >= r):
                    Z[i,j] = img[i,j]
                else:
                    Z[i,j] = 0

            except IndexError as e:
                pass
    
    return Z
#now we go for the threshold part , here we decide what all edges to be detected
#the strong pixels are those which have a high intensity and hence would be present in the image
#whereas the weak pixels are those whose intensity is low and are likely to be ignored
#other pixels are considered as non relevant for the edge

#high threshold is ised for identifying the strong pixels
#low threshold for weak pixels
#and all the other pixels are cosidered as irrelevant

def threshold(img, lowThresholdRatio=0.05, highThresholdRatio=0.09):
    
    highThreshold = img.max() * highThresholdRatio;
    lowThreshold = highThreshold * lowThresholdRatio;
    
    M, N = img.shape
    res = np.zeros((M,N), dtype=np.int32)
    
    weak = np.int32(25)
    strong = np.int32(255)
    
    strong_i, strong_j = np.where(img >= highThreshold)
    zeros_i, zeros_j = np.where(img < lowThreshold)
    
    weak_i, weak_j = np.where((img <= highThreshold) & (img >= lowThreshold))
    
    res[strong_i, strong_j] = strong
    res[weak_i, weak_j] = weak
    
    return (res, weak, strong)


#now we go to the last step
def hysteresis(img, weak, strong=255):
    M, N = img.shape  
    for i in range(1, M-1):
        for j in range(1, N-1):
            if (img[i,j] == weak):
                try:
                    if ((img[i+1, j-1] == strong) or (img[i+1, j] == strong) or (img[i+1, j+1] == strong)
                        or (img[i, j-1] == strong) or (img[i, j+1] == strong)
                        or (img[i-1, j-1] == strong) or (img[i-1, j] == strong) or (img[i-1, j+1] == strong)):
                        img[i, j] = strong
                    else:
                        img[i, j] = 0
                except IndexError as e:
                    pass
    return img