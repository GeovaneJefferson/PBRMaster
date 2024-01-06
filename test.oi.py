import cv2
import numpy as np

def futuristic_screen_effect(image_path, output_path, pixel_size):
    # Read the image
    img = cv2.imread(image_path)

    # Get the image dimensions
    height, width, _ = img.shape

    # Resize the image to a smaller size
    small_img = cv2.resize(img, (width // pixel_size, height // pixel_size), interpolation=cv2.INTER_NEAREST)

    # Resize the small image back to the original size
    pixelated_img = cv2.resize(small_img, (width, height), interpolation=cv2.INTER_NEAREST)

    # Save the result
    cv2.imwrite(output_path, pixelated_img)

# Example usage:
input_image_path = '/home/geovane/Desktop/75b60a9ca5e781d69c2f0bebdbeefb77.jpg'
output_image_path = '/home/geovane/Desktop/output_futuristic_image.jpg'

pixel_size = 10  # Adjust the pixel size for the screen effect

futuristic_screen_effect(input_image_path, output_image_path, pixel_size)
