import numpy as np
from scipy import ndimage
import tifffile as tiff
import scipy
import matplotlib.pyplot as plt
import sys
#import flatten-dict
#import mcat

from PIL import Image
#import pillow as plt


# ------- Changes start here -------

def int16_to_int8(img16):
    image8 = (img16/256).astype('uint8')
    return image8


path = 'hoech001.tif'
if path[path.rfind('.'):] in ['.tiff', '.tif']:
    img16 = tiff.imread(path)
else:
    img16 = ndimage.imread(path)

# Converting all the 16bit image into 8bit
if img16.dtype == 'uint16':
    data = int16_to_int8(img16)
else:
    data = img16

for x in data:
    print(x)

# print(data.ndim) = 2.. hence a 2d image

# ------- Changes end here -------

w=len(data)
l1=len(data[0])
hist,bins = np.histogram(data.ravel(),256,[0,256])
print("Histogram of the image:")
print (hist) #Histogram of the image calculate

#Step2, calculate Xa
num =0
denum=0
l=len(hist)
for i in range(1,l+1) :
    num+= hist[i-1]*i
    denum+=hist[i-1]

#Step3 Clipping threshold and calculate clipping hstogram
exposure = (1.0/l)*(num/(1.0*denum))
xa=int(round(l*(1-exposure)))
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
        hist_c.append(hist[i-1])

# print("Clipped Histogram of the image:")
# print (hist_c) #Clipped Histogram of the image
# print("Rounded exp value:", int(round(xa)))
#Step 4 Histogram Sub Division and Equalization
undexp= []
overexp= []
underexp= hist[0:int(round(xa+1))]
overexp= hist[int(round(xa+1)):l]

nl=0
nu=0

for i in range (0,xa+1):
    nl+=hist_c[i]
for i in range (xa+1, l):
    nu+=hist_c[i]

pl=[]
pu=[]
for i in range(0,int(round(xa+1))):
    # print(hist_c[i],"and", nl)
    pl.append(hist_c[i]/nl)

for i in range(int(round(xa+1)),l):
    pu.append(hist_c[i]/nu)
    # print(pu[i], ":::", i)


#Get corresponding CDF
cl =[]
cu =[]

cl.append(pl[0])
print("len",len(pl))
for r in range(1,len(pl)):
    cl.append(pl[r]+cl[r-1])

cu.append(pu[0])
for r in range(1,(len(pu))):
    cu.append(pu[r]+cu[r-1])

ESIHEoutput = [[0 for x in range(l1)] for y in range(w)]
# print("row and col",w, "and",l1)

# print("Data:",data[0]) #Check this output @Nikhil
for r in range(0,w ):
    for s in range (0,l1):
        if data[r][s]<(xa+1):
            f=xa*cl[data[r][s]+1]
            # print("r",r,"s",s)
            ESIHEoutput[r][s]=round(f)
            # print("ESIHE", r," n ", s, ":",ESIHEoutput[r][s])
        else:
            f=(xa+1)+(255-xa)*cu[(data[r][s]-(xa+1))+1]
            ESIHEoutput[r][s]=round(f)


print("\nRESULT:")

print("Output matrix:\n\n")
print(ESIHEoutput)