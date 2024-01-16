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
big_preview_size = 350
small_preview_size = 200
hover_preview_size = 650
version_number = 'V.0.3'


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Drag And Drop
        self.ui.drag_and_drop_image.setAlignment(Qt.AlignCenter)
        self.ui.drag_and_drop_image.setText('\n\n Drop Texture Here \n\n')
        self.ui.drag_and_drop_image.setStyleSheet('''
            QLabel{
                border: 4px dashed #aaa
            }
        ''')

        self.texture_name = ''
        self.texture_location = ''
        self.already_handled_space = False

        # Version label
        # self.ui.version_label.setText(version_number)
        
        # Enable buttons
        self.ui.normal_map_checkbox.setChecked(True)
        self.ui.specular_map_checkbox.setChecked(True)
        self.ui.roughness_map_checkbox.setChecked(True)
        self.ui.ao_map_checkbox.setChecked(True)
        self.ui.Transparent_map_checkbox.setEnabled(False)

        # Connection
        # self.ui.load_texture_btn.clicked.connect(self.load_image)
        # self.ui.normal_btn.clicked.connect(self.apply_normal)
        # self.ui.stylized_btn.clicked.connect(self.apply_stylization)
        # self.ui.pixel_btn.clicked.connect(self.apply_pixelization)
        # self.ui.toon_btn.clicked.connect(self.apply_toon)
        self.ui.update_btn.clicked.connect(self.update_preview)
        # self.ui.save_btn.clicked.connect(self.save_textures)

        # CONNECTIONS
        # File
        self.ui.actionOpen_Texture.triggered.connect(self.load_image)
        self.ui.actionSave_New_Textures.triggered.connect(self.save_textures)

        # Generate
        self.ui.actionPBR.triggered.connect(self.apply_normal)
        self.ui.actionStylized.triggered.connect(self.apply_stylization)
        self.ui.actionPixel.triggered.connect(self.apply_pixelization)
   
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
        self.transparent_range = self.ui.transparent_size_spinbox.value()
        self.transparent_color = self.ui.transparent_comboBox.currentText()

        # Hide
        self.ui.sigma_s_spinbox.setEnabled(False)
        self.ui.sigma_r_spinbox.setEnabled(False)
        self.ui.pixel_size_spinbox.setEnabled(False)
        self.ui.transparent_comboBox.setEnabled(False)
        self.ui.transparent_size_spinbox.setEnabled(False)
        self.ui.normal_size_spinbox.setEnabled(False)
        self.ui.normal_mode.setEnabled(False)

        # self.ui.toon_btn.hide()
        self.ui.Transparent_map_checkbox.hide()
        
        # Disable
        # # self.ui.save_btn.setEnabled(False)

    def reset_ui(self):
        # Reset all settings
        self.modifield_image = ''
        self.file_path = ''

        self.ui.preview_1.setPixmap(QPixmap())
        self.ui.preview_2.setPixmap(QPixmap())
        self.ui.preview_3.setPixmap(QPixmap())
        self.ui.preview_4.setPixmap(QPixmap())
        self.ui.preview_5.setPixmap(QPixmap())
        
        # Delete first 5 previous textures
        refresh()

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
            self.reset_ui()

            event.setDropAction(Qt.CopyAction)
            # Get file path
            file_path = event.mimeData().urls()[0].toLocalFile()

            # Texture informations
            self.file_path = file_path
            
            # Get texture path name
            self.texture_name = str(self.file_location().split('/')[-1].split('.')[:-1][0])
            self.texture_location = '/'.join(self.file_location().split('/')[:-1])
    
            
            if self.file_path:
                image_reader = QImageReader(self.file_path)
                image_reader.setAutoTransform(True)

                self.loaded_image = QImage(image_reader.read())

                if not self.loaded_image.isNull():
                    pixmap = QPixmap.fromImage(self.loaded_image)
                    self.ui.selected_image_label.setPixmap(
                        pixmap.scaledToWidth(
                        big_preview_size, Qt.SmoothTransformation))
                else:
                    self.ui.selected_image_label.setText("Failed to load image.")

            event.accept()
        else:
            event.ignore()
    
    def load_image(self):
        self.reset_ui()

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

        if self.file_path:
            # Load image with 16-bit color depth
            # img_16bit = cv2.imread(self.file_path, cv2.IMREAD_UNCHANGED)

            # Convert to QImage for display
            # height, width, channel = img_16bit.shape
            # bytes_per_line = channel * width
            # q_image = QImage(img_16bit.data, width, height, bytes_per_line, QImage.Format_RGB16)
            
            image_reader = QImageReader(self.file_path)
            image_reader.setAutoTransform(True)

            self.loaded_image = QImage(image_reader.read())

            if not self.loaded_image.isNull():
                pixmap = QPixmap.fromImage(self.loaded_image)
                self.ui.selected_image_label.setPixmap(
                    pixmap.scaledToWidth(
                    big_preview_size, Qt.SmoothTransformation))
            else:
                self.ui.selected_image_label.setText("Failed to load image.")
    
    def file_location(self):
        # Get texture path name
        self.texture_name = self.file_path.split('/')[-1].split('.')[:-1][0]
        self.texture_location = '/'.join(self.file_path.split('/')[:-1])
        
        # # Handle spaces
        # if not self.already_handled_space:
        #     if ' ' in self.texture_location:
        #         self.texture_location = self.texture_location.replace(' ', r'\ ')
        #         # self.texture_location = self.texture_location.replace(' ', '\\ ')
        #         # self.texture_location = '"' + self.texture_location + '"'

        #         self.already_handled_space = True

        return f'{self.texture_location}/.{self.texture_name}'
    
    def loading(self):
        self.setCursor(Qt.WaitCursor)
    
    def done(self):
        self.unsetCursor()

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
        # elif self.choosed_style == 'toon':
        #     self.update_toon()
        #     self.apply_toon()
             
        self.done() 


    def apply_stylization(self):
        self.loading()
     
        self.choosed_style = 'style'
        self.modifield_image = self.file_path

        self.ui.preview_1.setPixmap(QPixmap())
        
        # Enable buttons
        # self.ui.save_btn.setEnabled(True)
       
        # Hide
        self.ui.sigma_s_spinbox.setEnabled(True)
        self.ui.sigma_r_spinbox.setEnabled(True)
        self.ui.pixel_size_spinbox.setEnabled(False)
        self.ui.transparent_comboBox.setEnabled(False)
        self.ui.transparent_size_spinbox.setEnabled(False)
        self.ui.normal_size_spinbox.setEnabled(True)
        self.ui.normal_mode.setEnabled(True)
        
        # Read the input image
        img = cv2.imread(self.modifield_image)

        # Convert BGR image to RGB
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        # Apply cv2.stylization with user-defined values
        stylized_image = cv2.stylization(img_rgb,
                                        sigma_s=self.sigma_s_value,
                                        sigma_r=self.sigma_r_value)

        cv2.imwrite(
            f'{self.file_location()}_color.png',
            cv2.cvtColor(stylized_image,
            cv2.COLOR_RGB2BGR))
        
        # Add to added list
        if f'{self.file_location()}_color.png' not in preview_list:
            preview_list.append(f'{self.file_location()}_color.png')

        # Preview 1
        pixmap = QPixmap.fromImage(QImage(f'{self.file_location()}_color.png'))
        self.ui.preview_1.setPixmap(pixmap.scaledToWidth(big_preview_size))

        # Unlock stylized settings
        # self.ui.stylized_settings.setEnabled(True)
        
        self.generate_maps()

        self.done()
    
    def apply_pixelization(self):
        self.choosed_style = 'pixel'

        # Enable buttons
        # self.ui.save_btn.setEnabled(True)
        
        # # Hide
        self.ui.sigma_s_spinbox.setEnabled(False)
        self.ui.sigma_r_spinbox.setEnabled(False)
        self.ui.pixel_size_spinbox.setEnabled(True)
        self.ui.transparent_comboBox.setEnabled(False)
        self.ui.transparent_size_spinbox.setEnabled(False)
        self.ui.normal_size_spinbox.setEnabled(True)
        self.ui.normal_mode.setEnabled(True)
        
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
            pixelated_image.save(f'{self.file_location()}_color.png')
            self.modifield_image = f'{self.file_location()}_color.png'

            # Add to added list
            if f'{self.file_location()}_color.png' not in preview_list:
                preview_list.append(f'{self.file_location()}_color.png')

            # Convert PIL Image to QImage
            q_image = QImage(pixelated_image.tobytes(), pixelated_image.width, pixelated_image.height, pixelated_image.width * 3, QImage.Format_RGB888)
            
            # Preview 1
            pixmap = QPixmap.fromImage(q_image)
            
            # Save informations
            self.saved_pixel_image = pixmap.scaledToWidth(self.ui.selected_image_label.width())
           
            # Add to label
            self.ui.preview_1.setPixmap(pixmap.scaledToWidth(big_preview_size))
            
            self.generate_maps()

    # def apply_toon(self):
    #     self.choosed_style = 'toon'

    #     # Hide
    #     self.ui.sigma_s_spinbox.setEnabled(False)
    #     self.ui.sigma_r_spinbox.setEnabled(False)
    #     self.ui.pixel_size_spinbox.setEnabled(False)
    #     self.ui.transparent_comboBox.setEnabled(False)
    #     self.ui.transparent_size_spinbox.setEnabled(False)
    #     self.ui.normal_size_spinbox.setEnabled(True)
    #     self.ui.normal_mode.setEnabled(False)
        
    #     # Read the input image
    #     img = cv2.imread(self.file_path)

    #     # Convert the image to grayscale
    #     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    #     # Apply bilateral filter to smooth the image while preserving edges
    #     smooth = cv2.bilateralFilter(gray, self.toon_size_value, 300, 75)

    #     # Apply edge detection using adaptive thresholding
    #     edges = cv2.adaptiveThreshold(smooth, 255,
    #                                 cv2.ADAPTIVE_THRESH_MEAN_C,
    #                                 cv2.THRESH_BINARY, 9, 9)

    #     # Combine the edges with the original image using bitwise_and
    #     cartoon = cv2.bitwise_and(img, img, mask=edges)

    #     # Save the result
    #     cv2.imwrite(
    #         f'{self.file_location()}_color.png',
    #         cv2.cvtColor(cartoon,
    #         cv2.COLOR_RGB2BGR))
        
    #     # Add to added list
    #     if f'{self.file_location()}_color.png' not in preview_list:
    #         preview_list.append(f'{self.file_location()}_color.png')

    #     # Preview 1
    #     pixmap = QPixmap.fromImage(QImage(f'{self.file_location()}_color.png'))
    #     self.ui.preview_1.setPixmap(pixmap.scaledToWidth(big_preview_size))
        
    #     self.generate_maps()
    
    def apply_normal(self):
        self.choosed_style = 'normal'
        # self.modifield_image = self.file_path

        # Hide
        self.ui.sigma_s_spinbox.setEnabled(False)
        self.ui.sigma_r_spinbox.setEnabled(False)
        self.ui.pixel_size_spinbox.setEnabled(False)
        self.ui.transparent_comboBox.setEnabled(False)
        self.ui.transparent_size_spinbox.setEnabled(False)
        self.ui.normal_size_spinbox.setEnabled(True)
        self.ui.normal_mode.setEnabled(True)
        
        # Add to added list
        if f'{self.file_location()}_color.png' not in preview_list:
            preview_list.append(f'{self.file_location()}_color.png')
        
        pil_image = Image.fromqpixmap(self.loaded_image)
        pil_image.save(f'{self.file_location()}_color.png')

        # Preview 1
        pixmap = QPixmap.fromImage(QImage(f'{self.file_location()}_color.png'))
        self.ui.preview_1.setPixmap(pixmap.scaledToWidth(big_preview_size))

        self.generate_maps()
 

    # UPDATES
    def update_pixelization(self):
        try:
            self.pixel_size_value = self.ui.pixel_size_spinbox.value()
        except ValueError:
            pass
    
    def update_normal(self):
        try:
            self.normal_size_value = self.ui.normal_size_spinbox.value()
        except ValueError:
            pass
    
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
    
    def update_toon(self):
        try:
            self.toon_size_value = self.ui.toon_size_spinbox.value()
        except ValueError:
            pass
     
    def generate_maps(self):
        self.loading()

        # self.ui.save_btn.setEnabled(True)
        
        # Get texture path name
        self.texture_name = self.file_location().split('/')[-1].split('.')[:-1][0]
        self.texture_location = '/'.join(self.file_location().split('/')[:-1])
        
        # # Handle spaces
        # if not self.already_handled_space:
        #     if ' ' in self.texture_location:
        #         # self.texture_location = self.texture_location.replace(' ', r'\ ')
        #         # self.texture_location = self.texture_location.replace(' ', '\\ ')
        #         # self.texture_location = self.texture_location.replace(' ', '\ ')
        #         # self.texture_location = '"' + self.texture_location + '"'

        #         self.already_handled_space = True

        self.new_color_generated_image = f'{self.texture_location}/.{self.texture_name}_color.png'
        
        # NORMAL MAP
        if self.ui.normal_map_checkbox.isChecked():
            # Load the texture image in grayscale
            texture = cv2.imread(self.new_color_generated_image, cv2.IMREAD_GRAYSCALE)

            # Calculate gradients using the Sobel operator
            gradient_x = cv2.Sobel(texture, cv2.CV_64F, 1, 0, ksize=3)
            gradient_y = cv2.Sobel(texture, cv2.CV_64F, 0, 1, ksize=3)

            # Calculate the normal map from gradients with scaling
            normal_map = np.zeros((texture.shape[0], texture.shape[1], 3), dtype=np.uint8)
            for y in range(texture.shape[0]):
                for x in range(texture.shape[1]):
                    if self.ui.normal_mode.currentText() == 'NormalGL':
                        # DX
                        nx = -self.normal_size_value * gradient_x[y, x] / 255.0  # Invert the sign
                        ny = -self.normal_size_value * gradient_y[y, x] / 255.0  # Invert the sign
                        nz = 1 + self.normal_size_value * np.sqrt(nx**2 + ny**2)  # Invert the sign
                    else:    
                        # GL
                        nx = self.normal_size_value * gradient_x[y, x] / 255.0  # Invert the sign
                        ny = self.normal_size_value * gradient_y[y, x] / 255.0  # Invert the sign
                        nz = 1 - self.normal_size_value * np.sqrt(nx**2 + ny**2)  # Invert the sign

                    normal = np.array([nx, ny, nz])
                    normal /= np.linalg.norm(normal)

                    r = int(255 * (0.5 + 0.5 * normal[0]))
                    g = int(255 * (0.5 + 0.5 * normal[1]))
                    b = int(255 * (0.5 + 0.5 * normal[2]))

                    normal_map[y, x] = [r, g, b]

            self.show_preview(normal_map, 'normal')
        else:
            self.ui.preview_2.setPixmap(QPixmap())

        # ROUGHNESS MAP
        if self.ui.roughness_map_checkbox.isChecked():
            # Calculate gradients using the Sobel operator
            gradient_x = cv2.Sobel(texture, cv2.CV_64F, 1, 0, ksize=3)
            gradient_y = cv2.Sobel(texture, cv2.CV_64F, 0, 1, ksize=3)

            # Calculate roughness map from gradients
            roughness_map = np.zeros_like(texture, dtype=np.uint8)
            for y in range(texture.shape[0]):
                for x in range(texture.shape[1]):
                    gradient_magnitude = np.sqrt(gradient_x[y, x]**2 + gradient_y[y, x]**2)

                    # Adjust the scaling factor for roughness
                    roughness = 0.5 * gradient_magnitude / 255.0  # Adjust the factor as needed

                    # # Ensure roughness values are in the valid range [0, 1]
                    # roughness = np.clip(roughness, 0, 1)

                    # # Map roughness value to 0-255 range
                    # roughness_value = int(roughness * 255)
                    # roughness_map[y, x] = roughness_value

                    # Apply gamma correction to brighten the roughness map
                    gamma = 4  # Adjust the gamma value as needed
                    roughness = np.power(roughness, 1/gamma)

                    # Ensure roughness values are in the valid range [0, 1]
                    roughness = np.clip(roughness, 0, 1)

                    # Map roughness value to 0-255 range
                    roughness_value = int(roughness * 255)
                    roughness_map[y, x] = roughness_value

            self.show_preview(roughness_map, 'roughness')
        else:
            self.ui.preview_3.setPixmap(QPixmap())

        if self.ui.specular_map_checkbox.isChecked():
            # SPECULAR
            # Load the texture image in grayscale
            texture = cv2.imread(self.new_color_generated_image, cv2.IMREAD_GRAYSCALE)

            # Normalize the texture to the range [0, 1]
            texture_normalized = texture / 255.0

            # Apply specular strength
            # specular_map = (texture_normalized ** self.normal_size_value) * 255.0
            specular_map = (texture_normalized ** 1) * 255.0

            # return specular_map.astype(np.uint8)
            self.show_preview(specular_map.astype(np.uint8), 'specular')
        else:
            self.ui.preview_4.setPixmap(QPixmap())

        # AMBIENT OCCLUSION
        if self.ui.ao_map_checkbox.isChecked():
            # Read the texture image
            texture = cv2.imread(self.new_color_generated_image, cv2.IMREAD_GRAYSCALE)

            # Normalize the texture to the range [0, 1]
            texture = texture.astype(np.float32) / 255.0

            # Calculate the gradient of the texture
            gradient_x = cv2.Sobel(texture, cv2.CV_64F, 1, 0, ksize=3)
            gradient_y = cv2.Sobel(texture, cv2.CV_64F, 0, 1, ksize=3)

            # Calculate the magnitude of the gradient
            gradient_magnitude = np.sqrt(gradient_x**2 + gradient_y**2)

            # Apply a Gaussian blur to the gradient magnitude
            # blurred_gradient = cv2.GaussianBlur(gradient_magnitude, (5, 5), 0)

            # Invert the blurred gradient to create the ambient occlusion map
            ao_map = 1 - gradient_magnitude * 1

            # Clip values to the range [0, 1]
            ao_map = np.clip(ao_map, 0, 1)
            
            # Increase contrast in the dark parts
            ao_map = np.power(ao_map, 2)

            # Clip values to the range [0, 1]
            ao_map = np.clip(ao_map, 0, 1)

            self.show_preview((ao_map * 255).astype(np.uint8), 'ambient_occlusion')
        else:
            # Clean preview
            self.ui.preview_5.setPixmap(QPixmap())
            
        if self.ui.Transparent_map_checkbox.isChecked():
            # Remove Background
            self.remove_background()

            # Get texture path name
            self.texture_name = self.file_path.split('/')[-1].split('.')[:-1][0]
            self.texture_location = '/'.join(self.file_path.split('/')[:-1])

            # Add to added list
            if f'{self.texture_location}/.{self.texture_name}_Transparent.png' not in preview_list:
                preview_list.append(f'{self.texture_location}/.{self.texture_name}_Transparent.png')
            
            # Add to preview
            pixmap = QPixmap(preview_list[0])
            self.ui.preview_1.setPixmap(pixmap)

        self.done()
    
    def show_preview(self, coordinates, type):
        img = Image.fromarray(coordinates)

        current_image = f'{self.texture_location}/.{self.texture_name}_{type}.png'
        
        scaledHTML=f'width:"5%" height="{hover_preview_size}"'
        # Hover preview
        self.ui.preview_1.setToolTip(
            f"<img src={self.new_color_generated_image} {scaledHTML}/>")
        
        try:
            # Normal
            if type == 'normal':
                # Save texture as hidden file
                img.save(f'{self.texture_location}/.{self.texture_name}_{type}.png')

                # Add to added list
                if f'{self.texture_location}/.{self.texture_name}_{type}.png' not in preview_list:
                    preview_list.append(f'{self.texture_location}/.{self.texture_name}_{type}.png')
                
                # Add to preview
                # pixmap = QPixmap(preview_list[1])
                pixmap = QPixmap(current_image)
                self.ui.preview_2.setPixmap(pixmap.scaledToWidth(small_preview_size))
                
                # Hover preview
                self.ui.preview_2.setToolTip(
                    f"<img src={current_image} {scaledHTML}/>")
                
            # Roughness
            elif type == 'roughness':
                img.save(f'{self.texture_location}/.{self.texture_name}_{type}.png')

                # Add to added list
                if f'{self.texture_location}/.{self.texture_name}_{type}.png' not in preview_list:
                    preview_list.append(f'{self.texture_location}/.{self.texture_name}_{type}.png')
                
                # Add to preview
                # pixmap = QPixmap(preview_list[2])
                pixmap = QPixmap(current_image)
                self.ui.preview_3.setPixmap(pixmap.scaledToWidth(small_preview_size))
                
                # Hover preview
                self.ui.preview_3.setToolTip(
                    f"<img src={current_image} {scaledHTML}/>")
                
            # Specular
            elif type == 'specular':
                img.save(f'{self.texture_location}/.{self.texture_name}_{type}.png')

                # Add to added list
                if f'{self.texture_location}/.{self.texture_name}_{type}.png' not in preview_list:
                    preview_list.append(f'{self.texture_location}/.{self.texture_name}_{type}.png')
                
                # Add to preview
                # pixmap = QPixmap(preview_list[3])
                pixmap = QPixmap(current_image)
                self.ui.preview_4.setPixmap(pixmap.scaledToWidth(small_preview_size))
                
                # Hover preview
                self.ui.preview_4.setToolTip(
                    f"<img src={current_image} {scaledHTML}/>")
                
            # Ambient Occlusion
            elif type == 'ambient_occlusion':
                img.save(f'{self.texture_location}/.{self.texture_name}_{type}.png')
                
                # Add to added list
                if f'{self.texture_location}/.{self.texture_name}_{type}.png' not in preview_list:
                    preview_list.append(f'{self.texture_location}/.{self.texture_name}_{type}.png')

                # Add to preview
                pixmap = QPixmap(current_image)
                self.ui.preview_5.setPixmap(pixmap.scaledToWidth(small_preview_size))
                
                # Hover preview
                self.ui.preview_5.setToolTip(
                    f"<img src={current_image} {scaledHTML}/>")
                
            # # Transparent
            # elif type == 'Transparent':
            #     img.save(f'{self.texture_location}/.{self.texture_name}_{type}.png')

            #     # Add to added list
            #     if f'{self.texture_location}/.{self.texture_name}_{type}.png' not in preview_list:
            #         preview_list.append(f'{self.texture_location}/.{self.texture_name}_{type}.png')
        except Exception as e:
            print(e)
            pass

    # Save
    def save_textures(self):
        # Check if the file exists before renaming
        if os.path.exists(f'{self.texture_location}/.{self.texture_name}_color.png'):
            os.rename(f'{self.texture_location}/.{self.texture_name}_color.png', f'{self.texture_location}/{self.texture_name}_color.png')
        
        if self.ui.normal_map_checkbox.isChecked():
            # Check if the file exists before renaming
            if os.path.exists(f'{self.texture_location}/.{self.texture_name}_normal.png'):
                os.rename(
                f'{self.texture_location}/.{self.texture_name}_normal.png', 
                f'{self.texture_location}/{self.texture_name}_normal.png')
        
        if self.ui.roughness_map_checkbox.isChecked():
            # Check if the file exists before renaming
            if os.path.exists(f'{self.texture_location}/.{self.texture_name}_roughness.png'):
                os.rename(
                f'{self.texture_location}/.{self.texture_name}_roughness.png', 
                f'{self.texture_location}/{self.texture_name}_roughness.png')
       
        if self.ui.specular_map_checkbox.isChecked():
            # Check if the file exists before renaming
            if os.path.exists(f'{self.texture_location}/.{self.texture_name}_specular.png'):
                os.rename(
                f'{self.texture_location}/.{self.texture_name}_specular.png', 
                f'{self.texture_location}/{self.texture_name}_specular.png')
            
        if self.ui.ao_map_checkbox.isChecked():
            # Check if the file exists before renaming
            if os.path.exists(f'{self.texture_location}/.{self.texture_name}_ambient_occlusion.png'):
                os.rename(
                    f'{self.texture_location}/.{self.texture_name}_ambient_occlusion.png', 
                    f'{self.texture_location}/{self.texture_name}_ambient_occlusion.png')

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
    
    def add_to_list(self, type):
        # Get texture path name
        self.texture_name = str(self.file_location().split('/')[-1].split('.')[:-1][0])
        self.texture_location = '/'.join(self.file_location().split('/')[:-1])

        # Add to added list
        if f'{self.texture_location}/.{self.texture_name}_{type}.png' not in preview_list:
            preview_list.append(f'{self.texture_location}/.{self.texture_name}_{type}.png')
            
 
def on_about_to_quit():
    # Delete preview
    for i in range(len(preview_list)):
        try:
            print('Deleting', preview_list[i])
            os.remove(preview_list[i])
        except FileNotFoundError:
            pass

def refresh():
    # Delete preview
    for i in range(len(preview_list)):
        try:
            os.remove(preview_list[i])
        except Exception as e:
            print(e)
            pass


if __name__ == "__main__": 
    app = QApplication([])
    window = MainWindow()
    window.setWindowTitle('PBRMaster')
    window.showMaximized()
    window.show()

    app.aboutToQuit.connect(on_about_to_quit)

    app.exec()
      