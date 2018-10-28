
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

# Flatten the image into 1 dimension: pixels
pixels = data.flatten()

# Generate a cumulative histogram
cdf, bins, patches = plt.hist(pixels, bins=256, range=(0,256), normed=True, cumulative=True)
new_pixels = np.interp(pixels, bins[:-1], cdf*255)

# Reshape new_pixels as a 2-D array: new_image
new_image = new_pixels.reshape(data.shape)

# Display the new image with 'gray' color map
plt.subplot(2,1,1)
plt.title('Equalized image')
plt.axis('off')
plt.imshow(new_image, cmap='gray')

a1=np.asarray( np.clip(new_image,0,255), dtype="uint8")

img = Image.fromarray( a1, "RGB" )
img.show()

outimg = Image.fromarray( new_image,"RGB" )
outimg.show();