# import opencv
import cv2
import numpy as np

# Load the input image
image = cv2.imread('mini projekt/1.jpg')
cv2.imshow('Plade', image)
print(image.shape)
# Window shown waits for any key pressing event
cv2.waitKey(0) 
