from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QColorDialog, QColor, QGraphicsScene, QGraphicsView
from PySide6.QtGui import QPainter, QBrush, QPen
from PySide6.QtCore import Qt

class ColorPicker(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.color_view = QGraphicsView(self)
        self.color_scene = QGraphicsScene(self)
        self.color_view.setScene(self.color_scene)
        self.color_view.setRenderHint(QPainter.Antialiasing)

        self.color_button = QPushButton('Pick a Color', self)
        self.color_button.clicked.connect(self.show_custom_color_dialog)

        layout.addWidget(self.color_view)
        layout.addWidget(self.color_button)

        self.setLayout(layout)
        self.setWindowTitle('Custom Color Picker')
        self.show()

    def show_custom_color_dialog(self):
        color = self.get_custom_color()

        if color.isValid():
            # The user selected a valid color
            self.set_selected_color(color)

    def get_custom_color(self):
        # Open a custom color picker dialog
        color_dialog = QColorDialog(self)
        color_dialog.setOption(QColorDialog.DontUseNativeDialog)  # Avoid native dialog
        color_dialog.exec_()

        return color_dialog.selectedColor()

    def set_selected_color(self, color):
        # Set the selected color to the scene background
        self.color_scene.setSceneRect(0, 0, 50, 50)
        self.color_scene.clear()
        self.color_scene.addRect(0, 0, 50, 50, QPen(Qt.NoPen), QBrush(color))
        # You can use the selected color for further processing or set it to a widget, etc.

if __name__ == '__main__':
    app = QApplication([])
    window = ColorPicker()
    app.exec_()
