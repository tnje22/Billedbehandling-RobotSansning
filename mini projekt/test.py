import cv2
import numpy as np

# Load the image
image = cv2.imread('king_domino_board.png')

# Your database of tile images (each image corresponds to a tile type)
tile_images = {
    'grass': cv2.imread('grass_tile.png'),
    'water': cv2.imread('water_tile.png'),
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

# Your tile detection code (similar to the previous example)
# ...

# Loop through the detected tiles
for tile in detected_tiles:
    # Match the tile to the closest tile in the database
    tile_type = match_tile(tile)
    
    # Calculate points based on the tile type and placement
    points = calculate_points(tile_type, tile_position)
    
    # Display the tile type and points on the image
    cv2.putText(image, f'Tile: {tile_type}', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
    cv2.putText(image, f'Points: {points}', (x, y + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

# Display the image with detected tiles and points
cv2.imshow('King Domino Board with Tiles and Points', image)
cv2.waitKey(0)
cv2.destroyAllWindows()