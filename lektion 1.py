import cv2

tinypic_logo = cv2.imread("tinypic.png")
print(f"Type of variable: {type(tinypic_logo)}")
print(f"Type of data in array: {tinypic_logo.dtype}")
print(f"Shape of array: {tinypic_logo.shape}")

pixel_value = tinypic_logo[1,1] # B, G, R
print(pixel_value)



cv2.imshow("Original logo", tinypic_logo)
cv2.waitKey(0)