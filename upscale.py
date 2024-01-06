from skimage import io, transform
import numpy as np

def upscale_image(input_path, output_path, scale_factor):
    # Read the low-resolution image
    low_res_img = io.imread(input_path)

    # Upscale the image using bilinear interpolation
    high_res_img = transform.resize(low_res_img,
                                     (low_res_img.shape[0] * scale_factor, low_res_img.shape[1] * scale_factor),
                                     mode='reflect',
                                     anti_aliasing=True)

    # Convert the image array to uint8 before saving
    high_res_img_uint8 = (high_res_img * 255).astype(np.uint8)

    # Save the high-resolution image
    io.imsave(output_path, high_res_img_uint8)

# Example usage:
input_image_path = '/home/macbook/Desktop/gournd_base_color.jpg'
output_image_path = '/home/macbook/Desktop/higher_resolution_image.jpg'
scale_factor = 2  # Adjust the scale factor based on your requirements

upscale_image(input_image_path, output_image_path, scale_factor)
