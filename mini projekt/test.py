# Import packages
import cv2
import numpy as np
 
img = cv2.imread('mini projekt/1.jpg')
print(img.shape) # Print image shape
cv2.imshow("original", img)
 
# Cropping an image [x:x2, y:y2]
cropped_image = img[100:200, 0:100]
 
# Display cropped image
cv2.imshow("cropped", cropped_image)
 
# Save the cropped image
cv2.imwrite("Cropped Image.jpg", cropped_image)
 
cv2.waitKey(0)
cv2.destroyAllWindows()