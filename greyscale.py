# import opencv
import cv2
key = None
I = 0 
while (I<100, I+1):
 image = cv2.imread('lion.jpg')
cv2.imshow('Original', image)
image = image +1 

""""
while(key != 27):  
    # Load the input image
    image = cv2.imread('lion.jpg')
    cv2.imshow('Original', image)
    
    image1= cv2.imread('lion.jpg')
    cv2.imshow('Original1', image1)
    key = cv2.waitKey(1)  
    
    # Use the cvtColor() function to grayscale the image
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    cv2.imshow('Grayscale', gray_image)
    key = cv2.waitKey(1)  """

  
# Window shown waits for any key pressing event
cv2.destroyAllWindows()
