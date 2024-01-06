import random
from PIL import Image, ImageDraw

def create_water_drops_texture(size, num_drops, drop_size_range=(5, 20), color=(0, 0, 255, 150), background=(255, 255, 255, 0)):
    # Create a blank image with an RGBA mode
    image = Image.new("RGBA", size, background)

    # Create a drawing object
    draw = ImageDraw.Draw(image)

    # Draw random water drops
    for _ in range(num_drops):
        drop_size = random.randint(*drop_size_range)
        drop_position = (random.randint(0, size[0] - drop_size), random.randint(0, size[1] - drop_size))
        draw.ellipse([drop_position, (drop_position[0] + drop_size, drop_position[1] + drop_size)], fill=color)

    return image

if __name__ == "__main__":
    texture_size = (256, 256)
    num_water_drops = 100  # Adjust the number of drops as needed
    water_drop_color = (0, 0, 255, 150)  # RGBA color for the water drop (adjust as needed)
    background_color = (255, 255, 255, 0)  # RGBA color for the background (transparent)

    water_drops_texture = create_water_drops_texture(texture_size, num_water_drops, color=water_drop_color, background=background_color)
    water_drops_texture.save("/home/geovane/Desktop/water_drop_texture.png")
    water_drops_texture.show()

