

from numpy import *
import scipy
import matplotlib
import sys
from PIL import Image
#import cv2 as cv
#print(cv.__version__)




print("My version is", sys.version)
a=arange(15).reshape(3,5)
print(a) #printing the array
print(a.ndim) #printig the dimension
print(a.shape) #printing the shape

im= Image.open("abhi.jpg");
if(size(img,3)!=1)
{
    img = rgb2gray(img);
    img=uint8(img);
}

print(im.format, im.size,im.mode);      #Prints image format, size and color mode

im.show();
out1 = im.point(lambda i: i * 1.2)   #Performing point operations
out1.show();
out2 = im.point(lambda i: i * 5)   #Performing point operations
out2.show();
out3 = im.point(lambda i: i * 0.4)   #Performing point operations
out3.show();
print(a.itemsize) #size of bytes in each element
print(a.size) #printing the number of elements
b= array( [[2,3], [3,5]], dtype=complex)
c = array( [ [1,2], [3,4] ], dtype=complex )
print(b)
print(c)