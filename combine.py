import cv2
import numpy as np

# Load your texture image (replace this path with your actual file path)
texture_path = "/Users/geovane/Downloads/2c2eda66fa46dc5dbd2c7b41deae5ab9.jpg"
texture = cv2.imread(texture_path)

if texture is not None:
    # Convert the texture to grayscale
    grayscale_texture = cv2.cvtColor(texture, cv2.COLOR_BGR2GRAY)

    # Apply a simple blur to the grayscale texture
    blurred_texture = cv2.GaussianBlur(grayscale_texture, (5, 5), 0)

    # Normalize the blurred texture to the range [0, 1]
    normalized_texture = blurred_texture / 255.0

    # Invert the values to create ambient occlusion
    ambient_occlusion_map = 1.0 - normalized_texture

    # Display the original texture and the ambient occlusion map (for visualization purposes)
    cv2.imshow("Original Texture", texture)
    cv2.imshow("Ambient Occlusion Map", ambient_occlusion_map)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Save the ambient occlusion map as an image
    cv2.imwrite("/Users/geovane/Downloads/ambient_occlusion_map.jpg", (ambient_occlusion_map * 255).astype(np.uint8))
else:
    print("Error loading the texture image.")
