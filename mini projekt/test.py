# Import packages
import cv2
import numpy as np
 
img = cv2.imread('mini projekt/1.jpg')
print(img.shape) # Print image shape
cv2.imshow("original", img)
 
# Cropping an image [y:y2, x:x2]
square1 = img[0:100, 0:100]
# Display cropped image
cv2.imshow("square1", square1)
 # Cropping an image [y:y2, x:x2]
square2 = img[0:100, 100:200]
# Display cropped image
cv2.imshow("square2", square2)
 
cv2.waitKey(0)
cv2.destroyAllWindows()