import cv2
import numpy as np
import matplotlib.pyplot as plt
from scipy import misc


i = misc.ascent()

plt.gray()
plt.grid(False)
plt.axis('off')
plt.imshow(i) #Finish drawing
plt.show() #Show image

#Make a copy and get dimensions
i_transformed = np.copy(i)
size_x = i_transformed.shape[0]
size_y = i_transformed.shape[1]


#All the digits in the filter must add to 0 or 1.
#If they don't, set a weight and multiply the total by the weight
#so they do. This will normalize them.
#Eg: Total: 5, weight = 0.2
filter = [[0,1,0], [1,-4,1], [0,1,0]]
weight = 1

#Create the convolution
#Multiply the 3x3 square by the filter and add together for new value.
#Then set the pixel on the transformed image at that location to the new value
for y in range(1, size_y-1):
    for x in range(1, size_x-1):
        convolution = 0.0
        convolution = convolution + (i[x-1, y-1] * filter[0][0])
        convolution = convolution + (i[x, y-1] * filter[0][1])
        convolution = convolution + (i[x+1, y-1] * filter[0][2])
        convolution = convolution + (i[x-1, y] * filter[1][0])
        convolution = convolution + (i[x, y] * filter[1][1])
        convolution = convolution + (i[x+1, y] * filter[1][2])
        convolution = convolution + (i[x-1, y+1] * filter[2][0])
        convolution = convolution + (i[x, y+1] * filter[2][1])
        convolution = convolution + (i[x+1, y+1] * filter[2][2])
        if convolution < 0:
            convolution = 0
        elif convolution > 255:
            convolution = 255
        i_transformed[x, y] = convolution

#Show the filtered image
plt.gray()
plt.grid(False)
plt.imshow(i_transformed)
plt.show()


#Pool the image

new_x = int(size_x/2)
new_y = int(size_y/2)
#Get an empty image that's half the size
newImage = np.zeros((new_x, new_y))
for x in range(0, size_x, 2):
    for y in range(0, size_y, 2):
        #Get all four pixels of the 2x2 square in an array
        pixels = []
        pixels.append(i_transformed[x, y])
        pixels.append(i_transformed[x+1, y])
        pixels.append(i_transformed[x, y+1])
        pixels.append(i_transformed[x+1, y+1])
        #Pick the pixel with the largest value and plot it on the new image.
        pixels.sort(reverse=True) #Descending order
        #Plot the largest value pixels on the new image which is half the size.
        #x/2 and y/2 must be converted from float to int.
        newImage[int(x/2), int(y/2)] = pixels[0]

#Plot the image. Notice the axis are halved
plt.gray()
plt.grid(False)
plt.imshow(newImage)
plt.show()