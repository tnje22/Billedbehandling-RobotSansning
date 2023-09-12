import cv2


# Open picture
python_logo = cv2.imread("python.png")

# Display the picture
cv2.imshow("Our window", python_logo)
cv2.waitKey(0)
