# import opencv
import cv2
key = None

while(key != 27):  
    # Load the input image
    image = cv2.imread('lion.jpg')
    cv2.imshow('Original', image)
    cv2.waitKey(0)
    
    # Use the cvtColor() function to grayscale the image
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    cv2.imshow('Grayscale', gray_image)
    key = cv2.waitKey(1)  
  
# Window shown waits for any key pressing event
#cv2.destroyAllWindows()