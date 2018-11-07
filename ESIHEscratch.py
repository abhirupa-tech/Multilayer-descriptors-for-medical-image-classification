
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
print("l:",l)

clipthreshold =0

s=0
for i in range(1,l+1):
   s+=hist[i-1]
clipthreshold = (1.0/l)*s

hist_c=[]

for i in range(1, l+1):
    if(hist[i-1]>clipthreshold):
        hist_c.append(clipthreshold)
    else:
        hist_c.append(hist[i-1]);

print("Clipped Histogram of the image:")
print (hist_c) #Clipped Histogram of the image
print("Rounded exp value:", int(round(xa)))
#Step 4 Histogram Sub Division and Equalization
undexp= []
overexp= []
underexp= hist[0:int(round(xa+1))]
overexp= hist[int(round(xa+1)):l]
nl=len(underexp)
nu=len(overexp)


pl=[None] * l
pu=[None] * l
for i in range(0,int(round(xa+1))):
    pl[i]=hist_c[i]/nl

for i in range(int(round(xa+1)),l):
    pu[i]=hist_c[i]/nu
    # print(pu[i], ":::", i)


#Get corresponding CDF
cl =0
cu =0

for i in range(0,int(round(xa+1))):
    cl+=pl[i]

for i in range(int(round(xa+1)),l):
    # print(pu[i],":::",i)
    cu+=pu[i]

fl=xa*cl
fu=(xa+1) + (l-xa+1)*cu





