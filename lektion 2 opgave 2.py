import cv2

letter = cv2.imread("letter.png")
print(f"Type of variable: {type(letter)}")
print(f"Type of data in array: {letter.dtype}")
print(f"Shape of array: {letter.shape}")

pixel_value = letter[1,1] # B, G, R
print(pixel_value)



cv2.imshow("Original logo", letter)
cv2.waitKey(0)