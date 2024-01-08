import cv2
import numpy as np
from PySide6.QtCore import QSize
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget

class ImagePreviewWidget(QLabel):
    def __init__(self):
        super().__init__()

    def set_image(self, image):
        height, width, channel = image.shape
        bytes_per_line = 3 * width
        q_image = QImage(image.data, width, height, bytes_per_line, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(q_image)
        self.setPixmap(pixmap)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.image_preview_widget = ImagePreviewWidget()

        # Load your normal map, roughness, and specular maps (replace these paths with your actual file paths)
        normal_map = cv2.imread("/Users/geovane/Downloads/8322367bd3a5eec3c54a95e0aa1bae6e_Normal.png")
        roughness_map = cv2.imread("/Users/geovane/Downloads/8322367bd3a5eec3c54a95e0aa1bae6e_Roughness.png")
        specular_map = cv2.imread("/Users/geovane/Downloads/8322367bd3a5eec3c54a95e0aa1bae6e_Specular.png")

        if normal_map is not None and roughness_map is not None and specular_map is not None:
            combined_map = self.combine_maps(normal_map, roughness_map, specular_map)
            self.image_preview_widget.set_image(combined_map)
        else:
            print("Error loading one or more image files.")

        central_widget = QWidget(self)
        layout = QVBoxLayout(central_widget)
        layout.addWidget(self.image_preview_widget)
        self.setCentralWidget(central_widget)

    def combine_maps(self, normal_map, roughness_map, specular_map):
        height, width, _ = normal_map.shape
        roughness_map = cv2.resize(roughness_map, (width, height))
        specular_map = cv2.resize(specular_map, (width, height))

        combined_map = np.zeros((height, width, 3), dtype=np.uint8)

        # Use the red channel from the normal map
        combined_map[:, :, 0] = normal_map[:, :, 2]

        # Use the green channel from the roughness map
        combined_map[:, :, 1] = roughness_map[:, :, 1]

        # Use the blue channel from the specular map
        combined_map[:, :, 2] = specular_map[:, :, 0]

        # Normalize the values to the range [0, 255]
        combined_map = np.clip(combined_map, 0, 255).astype(np.uint8)

        return combined_map

def main():
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()

if __name__ == "__main__":
    main()


