import cv2


# Open picture
python_logo = cv2.imread("C:\Users\tnj70\Desktop\python.png" cv2.IMREAD_GRAYSCALE)

# Display the picture
cv2.imshow("Our window", python_logo)
cv2.waitKey(0)