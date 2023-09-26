# import opencv
import cv2
import numpy as np

# Load the input image
image = cv2.imread('mini projekt/1.jpg')

cv2.imshow('Plade', image)
cv2.waitKey(0) 
#print(image.shape)
cropped_image = image[0:0, 100:100]
cv2.imshow('croppedPlade', cropped_image)
# Window shown waits for any key pressing event
cv2.waitKey(0) 
