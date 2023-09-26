import cv2
import numpy as np

# Load the image
image = cv2.imread('mini projekt/1.jpg')

# Your database of tile images (each image corresponds to a tile type)
tile_images = {
    'grass': cv2.imread('mini projekt/grass.png', cv2.IMREAD_GRAYSCALE),
    'water': cv2.imread('mini projekt/Water.png', cv2.IMREAD_GRAYSCALE),
    # Add more tile types as needed
}

# Function to match a tile to the closest tile in the database
def match_tile(tile):
    best_match = None
    min_diff = float('inf')
    
    for tile_type, template in tile_images.items():
        result = cv2.matchTemplate(tile, template, cv2.TM_SQDIFF_NORMED)
        min_val, _, _, _ = cv2.minMaxLoc(result)
        
        if min_val < min_diff:
            min_diff = min_val
            best_match = tile_type
    
    return best_match

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Canny edge detection
edges = cv2.Canny(gray, threshold1=50, threshold2=150)

# Find contours
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Filter out small contours (noise) based on area
min_contour_area = 1000
valid_contours = [cnt for cnt in contours if cv2.contourArea(cnt) > min_contour_area]

# Loop through the valid contours (tiles)
for contour in valid_contours:
    # Extract the tile region from the image
    x, y, w, h = cv2.boundingRect(contour)
    tile = gray[y:y+h, x:x+w]
    
    # Match the tile to a known tile type
    tile_type = match_tile(tile)
    
    # Calculate points based on the tile type and placement (simplified example)
    points = calculate_points(tile_type, (x, y))  # You need to implement this function
    
    # Display the tile type and points on the image
    cv2.putText(image, f'Tile: {tile_type}', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
    cv2.putText(image, f'Points: {points}', (x, y + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

# Display the image with detected tiles and points
cv2.imshow('King Domino Board with Tiles and Points', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
