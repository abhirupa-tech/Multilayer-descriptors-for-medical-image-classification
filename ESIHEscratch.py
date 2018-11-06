
import numpy as np
import scipy
import matplotlib.pyplot as plt
import sys
#import flatten-dict
#import mcat

from PIL import Image
#import pillow as plt

# Load the image into an array: image
image = Image.open('abhi.jpg')
image.load()
data = np.asarray(image, dtype="int32")
print("Matrix:", data);
hist,bins = np.histogram(data.ravel(),256,[0,256])
print("Histogram of the image:")
print (hist) #Histogram of the image calculate

#Step2, calculate Xa
num =0
denum=0
l=len(hist);
for i in range(1,l+1) :
    num+= hist[i-1]*i
    denum+=hist[i-1]

#Step3 Clipping threshold and calculate clipping hstogram
exposure = (1.0/l)*(num/(1.0*denum))
xa=l*(1-exposure)
print("Exposure value:", exposure)
print("Threshold value:", xa)
clipthreshold =0

s=0
for i in range(1,l+1):
   s+=hist[i-1]
clipthreshold = (1.0/l)*s

for i in range(1, l+1):
    if(hist[k]>clipthreshold):
        hist[k]=clipthreshold

