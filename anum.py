import cv2
import numpy as np

def toonify(image_path, output_path):
    # Read the input image
    img = cv2.imread(image_path)

    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply bilateral filter to smooth the image while preserving edges
    smooth = cv2.bilateralFilter(gray, 1, 300, 75)

    # Apply edge detection using adaptive thresholding
    edges = cv2.adaptiveThreshold(smooth, 255,
                                  cv2.ADAPTIVE_THRESH_MEAN_C,
                                  cv2.THRESH_BINARY, 9, 9)

    # Combine the edges with the original image using bitwise_and
    cartoon = cv2.bitwise_and(img, img, mask=edges)

    # Save the result
    cv2.imwrite(output_path, cartoon)

# Example usage:
input_image_path = '/Users/geovane/Downloads/2c2eda66fa46dc5dbd2c7b41deae5ab9.jpg'
output_image_path = '/Users/geovane/Downloads/output_image_toonified.jpg'

toonify(input_image_path, output_image_path)
