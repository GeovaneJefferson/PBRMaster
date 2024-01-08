import os
import cv2
import numpy as np
import subprocess as sub
import platform

from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap, QImageReader, QImage
from PIL import Image
from ui.ui_mainwindow import Ui_MainWindow

preview_list = []
version_number = 'V.0.1'


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Drag And Drop
        self.ui.drag_and_drop_image.setAlignment(Qt.AlignCenter)
        self.ui.drag_and_drop_image.setText('\n\n Drop Image Here \n\n')
        self.ui.drag_and_drop_image.setStyleSheet('''
            QLabel{
                border: 4px dashed #aaa
            }
        ''')

        self.loaded_image = None
        self.stylized_image = None

        # Version label
        self.ui.version_label.setText(version_number)
        
        # Enable buttons
        self.ui.normal_map_checkbox.setChecked(True)
        self.ui.specular_map_checkbox.setChecked(True)
        self.ui.roughness_map_checkbox.setChecked(True)
        self.ui.Transparent_map_checkbox.setEnabled(False)

        # Connection
        self.ui.load_texture_btn.clicked.connect(self.load_image)
        self.ui.normal_btn.clicked.connect(self.apply_normal)
        self.ui.stylized_btn.clicked.connect(self.apply_stylization)
        self.ui.pixel_btn.clicked.connect(self.apply_pixelization)
        self.ui.toon_btn.clicked.connect(self.apply_toon)
        self.ui.update_btn.clicked.connect(self.update_preview)
        self.ui.save_btn.clicked.connect(self.save_textures)
        # self.ui.Transparent_map_checkbox.clicked.connect(self.transparent_clicked)
        # self.ui.transparent_comboBox.currentIndexChanged.connect(self.transparent_combobox_clicked)

        # Edit Finished
        # self.ui.sigma_s_spinbox.editingFinished.connect(self.update_from_input)
        # self.ui.sigma_r_spinbox.editingFinished.connect(self.update_from_input)
        # self.ui.pixel_size_spinbox.editingFinished.connect(self.apply_pixelization)
        # self.ui.transparent_size_spinbox.editingFinished.connect(self.update_transparent_range)

        # Spin box
        # Sigma s
        self.ui.sigma_s_spinbox.setMinimum(1)
        self.ui.sigma_s_spinbox.setMaximum(100)
        self.ui.sigma_s_spinbox.setValue(100)
        self.ui.sigma_s_spinbox.valueChanged.connect(self.update_stylization)
        
        # Sigma r
        self.ui.sigma_r_spinbox.setMinimum(1)
        self.ui.sigma_r_spinbox.setMaximum(100)
        self.ui.sigma_r_spinbox.setValue(1)
        self.ui.sigma_r_spinbox.valueChanged.connect(self.update_stylization)

        # Pixel Size
        self.ui.pixel_size_spinbox.setMinimum(1)
        self.ui.pixel_size_spinbox.setMaximum(100)
        self.ui.pixel_size_spinbox.setValue(8)
        self.ui.pixel_size_spinbox.valueChanged.connect(self.update_pixelization)
        
        # Normal Size
        self.ui.normal_size_spinbox.setMinimum(1)
        self.ui.normal_size_spinbox.setMaximum(100)
        self.ui.normal_size_spinbox.setValue(1)
        self.ui.normal_size_spinbox.valueChanged.connect(self.update_normal)
      
        # Toon Size
        self.ui.toon_size_spinbox.setMinimum(1)
        self.ui.toon_size_spinbox.setMaximum(100)
        self.ui.toon_size_spinbox.setValue(1)
        self.ui.toon_size_spinbox.valueChanged.connect(self.update_toon)
           
        # Transparent Size
        # self.ui.transparent_size_spinbox.setMinimum(1)
        # self.ui.transparent_size_spinbox.setMaximum(100)
        # self.ui.transparent_size_spinbox.setValue(10)
        # self.ui.transparent_size_spinbox.valueChanged.connect(self.update_transparent_range)

        # Values
        self.sigma_s_value = self.ui.sigma_s_spinbox.value()
        self.sigma_r_value = self.ui.sigma_r_spinbox.value()
        self.pixel_size_value = self.ui.pixel_size_spinbox.value()
        self.normal_size_value = self.ui.normal_size_spinbox.value()
        self.toon_size_value = self.ui.toon_size_spinbox.value()
        self.transparent_range = self.ui.transparent_size_spinbox.value()
        self.transparent_color = self.ui.transparent_comboBox.currentText()

        # Hide
        self.ui.stylized_settings.hide()
        self.ui.pixel_settings.hide()
        self.ui.transparent_settings.hide()
        self.ui.normal_settings.hide()
        self.ui.toon_settings.hide()
        
        # Disable
        self.ui.save_btn.setEnabled(False)

    def dragEnterEvent(self, event):
        if event.mimeData().hasImage:
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        if event.mimeData().hasImage:
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasImage:
            event.setDropAction(Qt.CopyAction)
            file_path = event.mimeData().urls()[0].toLocalFile()

            # Get file path
            self.file_path = file_path
            
            if file_path:
                image_reader = QImageReader(file_path)
                image_reader.setAutoTransform(True)

                self.loaded_image = QImage(image_reader.read())

                if not self.loaded_image.isNull():
                    pixmap = QPixmap.fromImage(self.loaded_image)
                    self.ui.selected_image_label.setPixmap(pixmap.scaledToWidth(350, Qt.SmoothTransformation))
                else:
                    self.ui.selected_image_label.setText("Failed to load image.")

            event.accept()
        else:
            event.ignore()

    def load_image(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_name, _ = QFileDialog.getOpenFileName(
            self, 
            "Open Image File", 
            "", 
            "Images (*.png *.jpg *.jpeg *.bmp);;All Files (*)", 
            options=options)
        
        # Get file path
        self.file_path = file_name

        if file_name:
            image_reader = QImageReader(file_name)
            image_reader.setAutoTransform(True)

            self.loaded_image = QImage(image_reader.read())

            if not self.loaded_image.isNull():
                pixmap = QPixmap.fromImage(self.loaded_image)
                self.ui.selected_image_label.setPixmap(pixmap.scaledToWidth(350, Qt.SmoothTransformation))
            else:
                self.ui.selected_image_label.setText("Failed to load image.")
       
       # Reset all settings
        self.modifield_image = ''
        self.ui.preview_1.setPixmap(QPixmap())
        self.ui.preview_2.setPixmap(QPixmap())
        self.ui.preview_3.setPixmap(QPixmap())

    # Generate
    def update_preview(self):
        self.loading()

        # Styles
        if self.choosed_style == 'style':
            self.update_stylization()
            self.apply_stylization()
        elif self.choosed_style == 'pixel':
            self.update_pixelization()
            self.apply_pixelization()
        elif self.choosed_style == 'normal':
            self.update_normal()
            self.apply_normal()
        elif self.choosed_style == 'toon':
            self.update_toon()
            self.apply_toon()
             
        self.done()

    # Get file location
    def file_location(self):
        # Get texture path name
        self.texture_name = self.file_path.split('/')[-1].split('.')[:-1][0]
        self.texture_location = '/'.join(self.file_path.split('/')[:-1])
        return f'{self.texture_location}/.{self.texture_name}'
    
    def loading(self):
        self.setCursor(Qt.WaitCursor)
    
    def done(self):
        self.unsetCursor()

    # Save
    def save_textures(self):
        # Check if the file exists before renaming
        if os.path.exists(f'{self.texture_location}/.{self.texture_name}_Color.png'):
            os.rename(f'{self.texture_location}/.{self.texture_name}_Color.png', f'{self.texture_location}/{self.texture_name}_Color.png')
        
        # Check if the file exists before renaming
        if os.path.exists(f'{self.texture_location}/.{self.texture_name}_Normal.png'):
            os.rename(f'{self.texture_location}/.{self.texture_name}_Normal.png', f'{self.texture_location}/{self.texture_name}_Normal.png')

        # Check if the file exists before renaming
        if os.path.exists(f'{self.texture_location}/.{self.texture_name}_Roughness.png'):
            os.rename(f'{self.texture_location}/.{self.texture_name}_Roughness.png', f'{self.texture_location}/{self.texture_name}_Roughness.png')
        
        # Check if the file exists before renaming
        if os.path.exists(f'{self.texture_location}/.{self.texture_name}_Specular.png'):
            os.rename(f'{self.texture_location}/.{self.texture_name}_Specular.png', f'{self.texture_location}/{self.texture_name}_Specular.png')

        # Open direectory
        system = platform.system().lower()
        if system == 'linux':
            sub.run(['xdg-open', self.texture_location])
        elif system == 'darwin':  # macOS
            sub.run(['open', self.texture_location])
        elif system == 'windows':
            os.startfile(self.texture_location)
        else:
            print("Unsupported operating system")
    
    def xxx(self, coordinates, type):
        img = Image.fromarray(coordinates)
        preview_size = 250
        
        # Get texture path name
        self.texture_name = self.file_location().split('/')[-1].split('.')[:-1][0]
        texture_location = '/'.join(self.file_location().split('/')[:-1])

        # Normal
        if type == 'Normal':
            img.save(f'{texture_location}/.{self.texture_name}_{type}.png')

            # Add to added list
            if f'{texture_location}/.{self.texture_name}_{type}.png' not in preview_list:
                preview_list.append(f'{texture_location}/.{self.texture_name}_{type}.png')
            
            # Add to preview
            pixmap = QPixmap(preview_list[1])
            self.ui.preview_2.setPixmap(pixmap.scaledToWidth(preview_size))

        # Roughness
        elif type == 'Roughness':
            img.save(f'{texture_location}/.{self.texture_name}_{type}.png')

            # Add to added list
            if f'{texture_location}/.{self.texture_name}_{type}.png' not in preview_list:
                preview_list.append(f'{texture_location}/.{self.texture_name}_{type}.png')
            
            # Add to preview
            pixmap = QPixmap(preview_list[2])
            self.ui.preview_3.setPixmap(pixmap.scaledToWidth(preview_size))

        # Specular
        elif type == 'Specular':
            img.save(f'{texture_location}/.{self.texture_name}_specular.png')

            # Add to added list
            if f'{texture_location}/.{self.texture_name}_specular.png' not in preview_list:
                preview_list.append(f'{texture_location}/.{self.texture_name}_specular.png')
            
            # Add to preview
            pixmap = QPixmap(preview_list[3])
            self.ui.preview_4.setPixmap(pixmap.scaledToWidth(preview_size))
    
        # Transparent
        elif type == 'Transparent':
            img.save(f'{texture_location}/.{self.texture_name}_{type}.png')

            # Add to added list
            if f'{texture_location}/.{self.texture_name}_{type}.png' not in preview_list:
                preview_list.append(f'{texture_location}/.{self.texture_name}_{type}.png')
       

    # STYLIZATION 
    def apply_stylization(self):
        self.loading()
     
        self.choosed_style = 'style'
        self.modifield_image = self.file_path

        self.ui.preview_1.setPixmap(QPixmap())
        
        # Enable buttons
        self.ui.save_btn.setEnabled(True)
        # Hide
        self.ui.stylized_settings.show()
        self.ui.pixel_settings.hide()
        self.ui.normal_settings.hide()
        self.ui.toon_settings.hide()
        
        # Read the input image
        img = cv2.imread(self.modifield_image)

        # Convert BGR image to RGB
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        # Apply cv2.stylization with user-defined values
        stylized_image = cv2.stylization(img_rgb,
                                        sigma_s=self.sigma_s_value,
                                        sigma_r=self.sigma_r_value)

        cv2.imwrite(
            f'{self.file_location()}_Color.png',
            cv2.cvtColor(stylized_image,
            cv2.COLOR_RGB2BGR))
        
        # Add to added list
        if f'{self.file_location()}_Color.png' not in preview_list:
            preview_list.append(f'{self.file_location()}_Color.png')

        # Preview 1
        pixmap = QPixmap.fromImage(QImage(f'{self.file_location()}_Color.png'))
        self.ui.preview_1.setPixmap(pixmap.scaledToWidth(350))

        # Unlock stylized settings
        self.ui.stylized_settings.show()
        
        self.create_normal_map()

        self.done()
    
    def update_stylization(self):
        try:
            self.sigma_s_value = self.ui.sigma_s_spinbox.value()
            self.sigma_r_value = self.ui.sigma_r_spinbox.value()  # Assuming sigma_r still uses a QSlider
            
            self.sigma_s_value = int(self.ui.sigma_s_spinbox.text())
            self.ui.sigma_s_spinbox.setValue(self.sigma_s_value)
                
            self.sigma_r_value = int(self.ui.sigma_r_spinbox.text())
            self.ui.sigma_r_spinbox.setValue(self.sigma_r_value)
        except ValueError:
            pass
    
     # Pixelization 
    
    # PIXELIZATION
    def apply_pixelization(self):
        self.choosed_style = 'pixel'
        # Enable buttons
        self.ui.save_btn.setEnabled(True)
        
        # Hide
        self.ui.normal_settings.hide()
        self.ui.stylized_settings.hide()
        self.ui.toon_settings.hide()

        if self.loaded_image is not None:
            # Convert QImage to PIL Image
            pil_image = Image.fromqpixmap(self.loaded_image)

            # Apply pixelization
            pixelated_image = pil_image.resize(
                (pil_image.width // self.pixel_size_value,
                pil_image.height // self.pixel_size_value), 
                Image.NEAREST)
            
            pixelated_image = pixelated_image.resize(
                (pil_image.width, pil_image.height), 
                Image.NEAREST)

            # Temp Save image 
            pixelated_image.save(f'{self.file_location()}_Color.png')
            self.modifield_image = f'{self.file_location()}_Color.png'

            # Add to added list
            if f'{self.file_location()}_Color.png' not in preview_list:
                preview_list.append(f'{self.file_location()}_Color.png')

            # Convert PIL Image to QImage
            q_image = QImage(pixelated_image.tobytes(), pixelated_image.width, pixelated_image.height, pixelated_image.width * 3, QImage.Format_RGB888)
            # Preview 1
            pixmap = QPixmap.fromImage(q_image)
            # Save informations
            self.saved_pixel_image = pixmap.scaledToWidth(self.ui.selected_image_label.width())
            # Add to label
            self.ui.preview_1.setPixmap(pixmap.scaledToWidth(350))
            
            # Unlock stylized settings
            self.ui.pixel_settings.show()
            
            self.create_normal_map()

    # TOON
    def apply_toon(self):
        self.choosed_style = 'toon'

        # Hide
        self.ui.normal_settings.hide()
        self.ui.stylized_settings.hide()

        # Enable buttons
        self.ui.toon_settings.show()
        
        # Read the input image
        img = cv2.imread(self.file_path)

        # Convert the image to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Apply bilateral filter to smooth the image while preserving edges
        smooth = cv2.bilateralFilter(gray, self.toon_size_value, 300, 75)

        # Apply edge detection using adaptive thresholding
        edges = cv2.adaptiveThreshold(smooth, 255,
                                    cv2.ADAPTIVE_THRESH_MEAN_C,
                                    cv2.THRESH_BINARY, 9, 9)

        # Combine the edges with the original image using bitwise_and
        cartoon = cv2.bitwise_and(img, img, mask=edges)

        # Save the result
        cv2.imwrite(
            f'{self.file_location()}_Color.png',
            cv2.cvtColor(cartoon,
            cv2.COLOR_RGB2BGR))
               # Add to added list
        
        if f'{self.file_location()}_Color.png' not in preview_list:
            preview_list.append(f'{self.file_location()}_Color.png')

        # Preview 1
        pixmap = QPixmap.fromImage(QImage(f'{self.file_location()}_Color.png'))
        self.ui.preview_1.setPixmap(pixmap.scaledToWidth(350))
        
        self.create_normal_map()
    
    # NORMAL
    def apply_normal(self):
        self.choosed_style = 'normal'
        self.modifield_image = self.file_path

        # Hide
        self.ui.stylized_settings.hide()
        self.ui.pixel_settings.hide()
        self.ui.toon_settings.hide()

        # Add to added list
        if f'{self.file_location()}_Color.png' not in preview_list:
            preview_list.append(f'{self.file_location()}_Color.png')
        
        pil_image = Image.fromqpixmap(self.loaded_image)
        pil_image.save(f'{self.file_location()}_Color.png')

        # Preview 1
        pixmap = QPixmap.fromImage(QImage(f'{self.file_location()}_Color.png'))
        self.ui.preview_1.setPixmap(pixmap.scaledToWidth(350))

        self.create_normal_map()
        # Clean preview 1
        # self.ui.preview_1.setPixmap(QPixmap())
          
        # Unlock normal settings
        self.ui.normal_settings.show()
    
    def update_pixelization(self):
        try:
            self.pixel_size_value = self.ui.pixel_size_spinbox.value()
        except ValueError:
            pass
    
    # UPDATES
    def update_normal(self):
        try:
            self.normal_size_value = self.ui.normal_size_spinbox.value()
        except ValueError:
            pass
    
    def update_toon(self):
        try:
            self.toon_size_value = self.ui.toon_size_spinbox.value()
        except ValueError:
            pass
     
    def create_normal_map(self):
        self.loading()

        self.ui.save_btn.setEnabled(True)
        
        # Get texture path name
        self.texture_name = self.file_location().split('/')[-1].split('.')[:-1][0]
        texture_location = '/'.join(self.file_location().split('/')[:-1])

        self.modifield_image2 = f'{texture_location}/.{self.texture_name}_Color.png'

        # NORMAL MAP
        if self.ui.normal_map_checkbox.isChecked():
            # Load the texture image in grayscale
            texture = cv2.imread(self.modifield_image2, cv2.IMREAD_GRAYSCALE)

            # Calculate gradients using the Sobel operator
            gradient_x = cv2.Sobel(texture, cv2.CV_64F, 1, 0, ksize=3)
            gradient_y = cv2.Sobel(texture, cv2.CV_64F, 0, 1, ksize=3)

            # Calculate the normal map from gradients
            normal_map = np.zeros((texture.shape[0], texture.shape[1], 3), dtype=np.uint8)
            for y in range(texture.shape[0]):
                for x in range(texture.shape[1]):
                    nx = self.normal_size_value * gradient_x[y, x] / 255.0
                    ny = self.normal_size_value * gradient_y[y, x] / 255.0
                    nz = 1.0 - self.normal_size_value * np.sqrt(nx**2 + ny**2)

                    normal = np.array([nx, ny, nz])
                    normal /= np.linalg.norm(normal)

                    r = int(255 * (0.5 + 0.5 * normal[0]))
                    g = int(255 * (0.5 + 0.5 * normal[1]))
                    b = int(255 * (0.5 + 0.5 * normal[2]))

                    normal_map[y, x] = [r, g, b]
            
            self.xxx(normal_map, 'Normal')
        
        # ROUGHNESS MAP
        if self.ui.roughness_map_checkbox.isChecked():
            # ROUGNESS
            # Load the texture image in grayscale
            texture = cv2.imread(self.modifield_image2, cv2.IMREAD_GRAYSCALE)

            # Calculate gradients using the Sobel operator
            gradient_x = cv2.Sobel(texture, cv2.CV_64F, 1, 0, ksize=3)
            gradient_y = cv2.Sobel(texture, cv2.CV_64F, 0, 1, ksize=3)

            # Calculate roughness map from gradients
            roughness_map = np.zeros_like(texture, dtype=np.uint8)
            for y in range(texture.shape[0]):
                for x in range(texture.shape[1]):
                    gradient_magnitude = np.sqrt(gradient_x[y, x]**2 + gradient_y[y, x]**2)
                    roughness = self.normal_size_value * gradient_magnitude / 255.0

                    # Ensure roughness values are in the valid range [0, 1]
                    roughness = np.clip(roughness, 0, 1)

                    # Map roughness value to 0-255 range
                    roughness_value = int(roughness * 255)
                    roughness_map[y, x] = roughness_value

            self.xxx(roughness_map, 'Roughness')
        
        if self.ui.specular_map_checkbox.isChecked():
            # SPECULAR
            # Load the texture image in grayscale
            texture = cv2.imread(self.modifield_image2, cv2.IMREAD_GRAYSCALE)

            # Normalize the texture to the range [0, 1]
            texture_normalized = texture / 255.0

            # Apply specular strength
            specular_map = (texture_normalized ** self.normal_size_value) * 255.0

            # return specular_map.astype(np.uint8)
            self.xxx(specular_map.astype(np.uint8), 'Specular')

        if self.ui.Transparent_map_checkbox.isChecked():
            # Remove Background
            self.remove_background()

            # Get texture path name
            self.texture_name = self.file_path.split('/')[-1].split('.')[:-1][0]
            texture_location = '/'.join(self.file_path.split('/')[:-1])

            # Add to added list
            if f'{texture_location}/.{self.texture_name}_Transparent.png' not in preview_list:
                preview_list.append(f'{texture_location}/.{self.texture_name}_Transparent.png')
            
            # Add to preview
            pixmap = QPixmap(preview_list[0])
            self.ui.preview_1.setPixmap(pixmap)

        self.done()

def on_about_to_quit():
    # Delete preview
    for i in range(len(preview_list)):
        print('Deleting',preview_list[i])
        try:
            os.remove(preview_list[i])
        except FileNotFoundError:
            pass


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.setWindowTitle('Texture Generator')
    window.setFixedHeight(800)
    window.setFixedWidth(1200)
    window.show()

    app.aboutToQuit.connect(on_about_to_quit)

    app.exec()
      