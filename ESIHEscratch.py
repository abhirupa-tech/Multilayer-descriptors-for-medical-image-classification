
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
printI"Histogram of the image:")
print (hist) #Histogram of the image calculate

