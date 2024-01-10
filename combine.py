import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
pygame.init()

# Load textures
texture_surface = pygame.image.load("/Users/geovane/Downloads/19b3b1f1120101da355a73a7489084b7.jpg")
normal_map_surface = pygame.image.load("/Users/geovane/Downloads/19b3b1f1120101da355a73a7489084b7_normal.png")

texture_data = pygame.image.tostring(texture_surface, "RGB", 1)
normal_map_data = pygame.image.tostring(normal_map_surface, "RGB", 1)

roughness_map_surface = pygame.image.load("/Users/geovane/Downloads/19b3b1f1120101da355a73a7489084b7_roughness.png")
roughness_map_data = pygame.image.tostring(roughness_map_surface, "P", 1)

width, height = texture_surface.get_width(), texture_surface.get_height()
normal_map_width, normal_map_height = normal_map_surface.get_width(), normal_map_surface.get_height()
roughness_map_width, roughness_map_height = roughness_map_surface.get_width(), roughness_map_surface.get_height()


# Define the cube vertices and edges
vertices = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
)

edges = (
    (0, 1),
    (1, 2),
    (2, 3),
    (3, 0),
    (4, 5),
    (5, 6),
    (6, 7),
    (7, 4),
    (0, 4),
    (1, 5),
    (2, 6),
    (3, 7)
)

# Set up textures
def load_textures():
    glEnable(GL_TEXTURE_2D)
    textures = glGenTextures(3)  # Generate three textures

    # Load color texture
    glBindTexture(GL_TEXTURE_2D, textures[0])
    glTexImage2D(GL_TEXTURE_2D, 0, 3, width, height, 0, GL_RGB, GL_UNSIGNED_BYTE, texture_data)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)

    # Load normal map
    glBindTexture(GL_TEXTURE_2D, textures[1])
    glTexImage2D(GL_TEXTURE_2D, 0, 3, normal_map_width, normal_map_height, 0, GL_RGB, GL_UNSIGNED_BYTE, normal_map_data)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)

    # Load roughness map
    glBindTexture(GL_TEXTURE_2D, textures[2])
    glTexImage2D(GL_TEXTURE_2D, 0, 3, roughness_map_width, roughness_map_height, 0, GL_LUMINANCE, GL_UNSIGNED_BYTE, roughness_map_data)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)

    return textures

# Draw cube with textures
def draw_textured_cube(textures):
    glBindTexture(GL_TEXTURE_2D, textures[0])  # Bind color texture
    glActiveTexture(GL_TEXTURE1)
    
    glBindTexture(GL_TEXTURE_2D, textures[1])  # Bind normal map texture
    glActiveTexture(GL_TEXTURE2)
    
    glBindTexture(GL_TEXTURE_2D, textures[2])  # Bind roughness map texture
    glActiveTexture(GL_TEXTURE3)

    glBegin(GL_QUADS)
    for surface in surfaces:
        for vertex in surface:
            glMultiTexCoord2fv(GL_TEXTURE0, tex_coords[surface.index(vertex)])  # Use GL_TEXTURE0 for color texture
            glMultiTexCoord2fv(GL_TEXTURE1, tex_coords[surface.index(vertex)])  # Use GL_TEXTURE1 for normal map
            glMultiTexCoord2fv(GL_TEXTURE2, tex_coords[surface.index(vertex)])  # Use GL_TEXTURE2 for roughness map
            glVertex3fv(vertices[vertex])
    glEnd()

# Set up lighting
def set_lighting():
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)  # Use light source 0

    # Increase ambient light for a brighter scene
    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, [10, 10, 10, 1.0])

    glLightfv(GL_LIGHT0, GL_POSITION, [1, 1, 1, 0])  # Directional light from the positive XYZ direction
    glLightfv(GL_LIGHT0, GL_DIFFUSE, [1.0, 1.0, 1.0, 1.0])  # Diffuse light color

    glMaterialfv(GL_FRONT, GL_SPECULAR, [2, 2, 2, 1.0])
    glMaterialfv(GL_FRONT, GL_SHININESS, 0.8 * 128)


surfaces = (
    (0, 1, 2, 3),
    (4, 5, 6, 7),  # Reversed the order to make it consistent
    (3, 2, 7, 6),
    (6, 7, 5, 4),
    (4, 5, 1, 0),
    (1, 5, 7, 2),
    (4, 0, 3, 6)
)

tex_coords = [
    (0, 0),
    (1, 0),
    (1, 1),
    (0, 1)
]

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    glEnable(GL_DEPTH_TEST)  # Enable depth testing
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)

    textures = load_textures()
    set_lighting()  # Enable lighting

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glRotatef(1, 3, 1, 1)  # Rotate the cube

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # Clear depth buffer as well
        draw_textured_cube(textures)
        pygame.display.flip()
        pygame.time.wait(10)
        

if __name__ == "__main__":
    main()
