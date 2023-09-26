# Import packages
import cv2
import numpy as np
 
img = cv2.imread('mini projekt/1.jpg')
cv2.imshow("original", img)

# Cropping an image [y:y2, x:x2]
square1 = img[0:100, 0:100]
square2 = img[0:100, 100:200]
square3 = img[0:100, 200:300]
square4 = img[0:100, 300:400]
square5 = img[0:100, 400:500]
#------------------------------
square6 = img[100:200, 0:100]
square7 = img[100:200, 100:200]
square8 = img[100:200, 200:300]
square9 = img[100:200, 300:400]
square10 = img[100:200, 400:500]
#------------------------------
square11 = img[200:300, 0:100]
square12 = img[200:300, 100:200]
square13 = img[200:300, 200:300]
square14 = img[200:300, 300:400]
square15 = img[200:300, 400:500]
#------------------------------
square16 = img[300:400, 0:100]
square17 = img[300:400, 100:200]
square18 = img[300:400, 200:300]
square19 = img[300:400, 300:400]
square20 = img[300:400, 400:500]
#------------------------------
square21 = img[400:500, 0:100]
square22 = img[400:500, 100:200]
square23 = img[400:500, 200:300]
square24 = img[400:500, 300:400]
square25 = img[400:500, 400:500]
#---------------------------------
# taking the average color of the Cropend image
acsquare1 = np.average(square1, axis=0); average_color1 = np.average(acsquare1, axis=0)
acsquare2 = np.average(square2, axis=0); average_color2 = np.average(acsquare2, axis=0)
acsquare3 = np.average(square3, axis=0); average_color3 = np.average(acsquare3, axis=0)
acsquare4 = np.average(square4, axis=0); average_color4 = np.average(acsquare4, axis=0)
acsquare5 = np.average(square5, axis=0); average_color5 = np.average(acsquare5, axis=0)
acsquare6 = np.average(square6, axis=0); average_color6 = np.average(acsquare6, axis=0)
acsquare7 = np.average(square7, axis=0); average_color7 = np.average(acsquare7, axis=0)
acsquare8 = np.average(square8, axis=0); average_color8 = np.average(acsquare8, axis=0)
acsquare9 = np.average(square9, axis=0); average_color9 = np.average(acsquare9, axis=0)
acsquare10 = np.average(square10, axis=0); average_color10 = np.average(acsquare10, axis=0)
acsquare11 = np.average(square11, axis=0); average_color11 = np.average(acsquare11, axis=0)
acsquare12 = np.average(square12, axis=0); average_color12 = np.average(acsquare12, axis=0)
acsquare13 = np.average(square13, axis=0); average_color13 = np.average(acsquare13, axis=0)
acsquare14 = np.average(square14, axis=0); average_color14 = np.average(acsquare14, axis=0)
acsquare15 = np.average(square15, axis=0); average_color15 = np.average(acsquare15, axis=0)
acsquare16 = np.average(square16, axis=0); average_color16 = np.average(acsquare16, axis=0)
acsquare17 = np.average(square17, axis=0); average_color17 = np.average(acsquare17, axis=0)
acsquare18 = np.average(square18, axis=0); average_color18 = np.average(acsquare18, axis=0)
acsquare19 = np.average(square19, axis=0); average_color19 = np.average(acsquare19, axis=0)
acsquare20 = np.average(square20, axis=0); average_color20 = np.average(acsquare20, axis=0)
acsquare21 = np.average(square21, axis=0); average_color21 = np.average(acsquare21, axis=0)
acsquare22 = np.average(square22, axis=0); average_color22 = np.average(acsquare22, axis=0)
acsquare23 = np.average(square23, axis=0); average_color23 = np.average(acsquare23, axis=0)
acsquare24 = np.average(square24, axis=0); average_color24 = np.average(acsquare24, axis=0)
acsquare25 = np.average(square25, axis=0); average_color25 = np.average(acsquare25, axis=0)
#---------------------------------
#sea=b=121-173 g= 74-92 r=9-56



print("-----------")
print(average_color2)
print(average_color18)
print(average_color22)
print(average_color23)
print("-----------")

cv2.waitKey(0)
cv2.destroyAllWindows()