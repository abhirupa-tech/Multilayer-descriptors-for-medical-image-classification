
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
print(im.format, im.size,im.mode);      #Prints image format, size and color mode
im.show();

print(a.itemsize) #size of bytes in each element
print(a.size) #printing the number of elements
b= array( [[2,3], [3,5]], dtype=complex)
c = array( [ [1,2], [3,4] ], dtype=complex )
print(b)
print(c)