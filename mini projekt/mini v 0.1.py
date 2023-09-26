# Import packages
import cv2
import numpy as np
 
img = cv2.imread('mini projekt/1.jpg')
#print(img.shape) # Print image shape
cv2.imshow("original", img)
 
# Cropping an image [y:y2, x:x2]
square1 = img[0:100, 0:100]
# taking the average color of the Cropend image
acsquare1 = np.average(square1, axis=0)
average_color1 = np.average(acsquare1, axis=0)
# Display cropped image
#cv2.imshow("square1", square1)
# Printing  average color 
print(average_color1)


square2 = img[0:100, 100:200]
acsquare2 = np.average(square2, axis=0)
average_color2 = np.average(acsquare2, axis=0)
#cv2.imshow("square2", square2)
print(average_color2)


cv2.waitKey(0)
cv2.destroyAllWindows()