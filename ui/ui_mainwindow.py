# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QSpinBox,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1200, 800)
        MainWindow.setMinimumSize(QSize(1200, 800))
        MainWindow.setMaximumSize(QSize(1200, 800))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        font = QFont()
        font.setBold(True)
        self.label_8.setFont(font)

        self.verticalLayout.addWidget(self.label_8, 0, Qt.AlignHCenter)

        self.drag_and_drop_image = QLabel(self.centralwidget)
        self.drag_and_drop_image.setObjectName(u"drag_and_drop_image")

        self.verticalLayout.addWidget(self.drag_and_drop_image)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2, 0, Qt.AlignHCenter)

        self.load_texture_btn = QPushButton(self.centralwidget)
        self.load_texture_btn.setObjectName(u"load_texture_btn")
        self.load_texture_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout.addWidget(self.load_texture_btn)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.stylized_btn = QPushButton(self.centralwidget)
        self.stylized_btn.setObjectName(u"stylized_btn")
        self.stylized_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.stylized_btn, 0, 1, 1, 1)

        self.normal_btn = QPushButton(self.centralwidget)
        self.normal_btn.setObjectName(u"normal_btn")
        font1 = QFont()
        font1.setBold(False)
        self.normal_btn.setFont(font1)
        self.normal_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.normal_btn, 0, 0, 1, 1)

        self.pixel_btn = QPushButton(self.centralwidget)
        self.pixel_btn.setObjectName(u"pixel_btn")
        self.pixel_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.pixel_btn, 1, 0, 1, 1)

        self.toon_btn = QPushButton(self.centralwidget)
        self.toon_btn.setObjectName(u"toon_btn")
        self.toon_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.toon_btn, 1, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)

        self.verticalLayout.addWidget(self.label_6, 0, Qt.AlignHCenter)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.normal_map_checkbox = QCheckBox(self.centralwidget)
        self.normal_map_checkbox.setObjectName(u"normal_map_checkbox")

        self.verticalLayout_3.addWidget(self.normal_map_checkbox)

        self.roughness_map_checkbox = QCheckBox(self.centralwidget)
        self.roughness_map_checkbox.setObjectName(u"roughness_map_checkbox")

        self.verticalLayout_3.addWidget(self.roughness_map_checkbox)

        self.specular_map_checkbox = QCheckBox(self.centralwidget)
        self.specular_map_checkbox.setObjectName(u"specular_map_checkbox")

        self.verticalLayout_3.addWidget(self.specular_map_checkbox)

        self.ao_map_checkbox = QCheckBox(self.centralwidget)
        self.ao_map_checkbox.setObjectName(u"ao_map_checkbox")

        self.verticalLayout_3.addWidget(self.ao_map_checkbox)

        self.Transparent_map_checkbox = QCheckBox(self.centralwidget)
        self.Transparent_map_checkbox.setObjectName(u"Transparent_map_checkbox")

        self.verticalLayout_3.addWidget(self.Transparent_map_checkbox)


        self.verticalLayout.addLayout(self.verticalLayout_3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.update_btn = QPushButton(self.centralwidget)
        self.update_btn.setObjectName(u"update_btn")
        self.update_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout.addWidget(self.update_btn)

        self.save_btn = QPushButton(self.centralwidget)
        self.save_btn.setObjectName(u"save_btn")
        self.save_btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon(QIcon.fromTheme(u"document-save"))
        self.save_btn.setIcon(icon)

        self.verticalLayout.addWidget(self.save_btn)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.line_12 = QFrame(self.centralwidget)
        self.line_12.setObjectName(u"line_12")
        self.line_12.setFrameShape(QFrame.VLine)
        self.line_12.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line_12)

        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.normal_size_spinbox = QSpinBox(self.centralwidget)
        self.normal_size_spinbox.setObjectName(u"normal_size_spinbox")

        self.gridLayout_5.addWidget(self.normal_size_spinbox, 10, 1, 1, 1, Qt.AlignLeft)

        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_5.addWidget(self.label_9, 2, 0, 1, 1)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.gridLayout_5.addWidget(self.label_4, 0, 0, 1, 1)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_5.addWidget(self.label_3, 12, 0, 1, 1)

        self.line_5 = QFrame(self.centralwidget)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.gridLayout_5.addWidget(self.line_5, 1, 1, 1, 1)

        self.label_12 = QLabel(self.centralwidget)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_5.addWidget(self.label_12, 10, 0, 1, 1)

        self.sigma_s_spinbox = QSpinBox(self.centralwidget)
        self.sigma_s_spinbox.setObjectName(u"sigma_s_spinbox")

        self.gridLayout_5.addWidget(self.sigma_s_spinbox, 2, 1, 1, 1, Qt.AlignLeft)

        self.sigma_r_spinbox = QSpinBox(self.centralwidget)
        self.sigma_r_spinbox.setObjectName(u"sigma_r_spinbox")

        self.gridLayout_5.addWidget(self.sigma_r_spinbox, 3, 1, 1, 1, Qt.AlignLeft)

        self.transparent_size_spinbox = QSpinBox(self.centralwidget)
        self.transparent_size_spinbox.setObjectName(u"transparent_size_spinbox")

        self.gridLayout_5.addWidget(self.transparent_size_spinbox, 8, 1, 1, 1, Qt.AlignLeft)

        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_5.addWidget(self.label_7, 7, 0, 1, 1)

        self.pixel_size_spinbox = QSpinBox(self.centralwidget)
        self.pixel_size_spinbox.setObjectName(u"pixel_size_spinbox")

        self.gridLayout_5.addWidget(self.pixel_size_spinbox, 5, 1, 1, 1, Qt.AlignLeft)

        self.line_9 = QFrame(self.centralwidget)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setFrameShape(QFrame.HLine)
        self.line_9.setFrameShadow(QFrame.Sunken)

        self.gridLayout_5.addWidget(self.line_9, 9, 1, 1, 1)

        self.line_7 = QFrame(self.centralwidget)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.HLine)
        self.line_7.setFrameShadow(QFrame.Sunken)

        self.gridLayout_5.addWidget(self.line_7, 4, 1, 1, 1)

        self.line_8 = QFrame(self.centralwidget)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShape(QFrame.HLine)
        self.line_8.setFrameShadow(QFrame.Sunken)

        self.gridLayout_5.addWidget(self.line_8, 9, 0, 1, 1)

        self.line_6 = QFrame(self.centralwidget)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.gridLayout_5.addWidget(self.line_6, 4, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_2, 13, 0, 1, 1)

        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_5.addWidget(self.label_10, 5, 0, 1, 1)

        self.toon_size_spinbox = QSpinBox(self.centralwidget)
        self.toon_size_spinbox.setObjectName(u"toon_size_spinbox")

        self.gridLayout_5.addWidget(self.toon_size_spinbox, 12, 1, 1, 1, Qt.AlignLeft)

        self.line_4 = QFrame(self.centralwidget)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.gridLayout_5.addWidget(self.line_4, 1, 0, 1, 1)

        self.transparent_comboBox = QComboBox(self.centralwidget)
        self.transparent_comboBox.addItem("")
        self.transparent_comboBox.addItem("")
        self.transparent_comboBox.setObjectName(u"transparent_comboBox")
        self.transparent_comboBox.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_5.addWidget(self.transparent_comboBox, 7, 1, 1, 1, Qt.AlignLeft)

        self.line_3 = QFrame(self.centralwidget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.gridLayout_5.addWidget(self.line_3, 6, 1, 1, 1)

        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout_5.addWidget(self.line_2, 6, 0, 1, 1)

        self.label_11 = QLabel(self.centralwidget)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_5.addWidget(self.label_11, 8, 0, 1, 1)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_5.addWidget(self.label_5, 3, 0, 1, 1)

        self.line_10 = QFrame(self.centralwidget)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setFrameShape(QFrame.HLine)
        self.line_10.setFrameShadow(QFrame.Sunken)

        self.gridLayout_5.addWidget(self.line_10, 11, 0, 1, 1)

        self.line_11 = QFrame(self.centralwidget)
        self.line_11.setObjectName(u"line_11")
        self.line_11.setFrameShape(QFrame.HLine)
        self.line_11.setFrameShadow(QFrame.Sunken)

        self.gridLayout_5.addWidget(self.line_11, 11, 1, 1, 1)


        self.horizontalLayout.addLayout(self.gridLayout_5)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line, 0, Qt.AlignHCenter)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.selected_image_label = QLabel(self.centralwidget)
        self.selected_image_label.setObjectName(u"selected_image_label")

        self.horizontalLayout_10.addWidget(self.selected_image_label, 0, Qt.AlignRight)

        self.preview_1 = QLabel(self.centralwidget)
        self.preview_1.setObjectName(u"preview_1")
        self.preview_1.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_10.addWidget(self.preview_1, 0, Qt.AlignLeft)


        self.verticalLayout_2.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(-1, 9, -1, 34)
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_2)

        self.preview_2 = QLabel(self.centralwidget)
        self.preview_2.setObjectName(u"preview_2")

        self.horizontalLayout_7.addWidget(self.preview_2)

        self.preview_3 = QLabel(self.centralwidget)
        self.preview_3.setObjectName(u"preview_3")

        self.horizontalLayout_7.addWidget(self.preview_3)

        self.preview_4 = QLabel(self.centralwidget)
        self.preview_4.setObjectName(u"preview_4")

        self.horizontalLayout_7.addWidget(self.preview_4)

        self.preview_5 = QLabel(self.centralwidget)
        self.preview_5.setObjectName(u"preview_5")

        self.horizontalLayout_7.addWidget(self.preview_5)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer)


        self.verticalLayout_2.addLayout(self.horizontalLayout_7)

        self.verticalLayout_2.setStretch(0, 1)

        self.horizontalLayout.addLayout(self.verticalLayout_2)


        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        self.version_label = QLabel(self.centralwidget)
        self.version_label.setObjectName(u"version_label")

        self.horizontalLayout_2.addWidget(self.version_label, 0, Qt.AlignBottom)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.transparent_comboBox.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Set Texture", None))
        self.drag_and_drop_image.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"or", None))
        self.load_texture_btn.setText(QCoreApplication.translate("MainWindow", u"Find Texture", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
        self.stylized_btn.setText(QCoreApplication.translate("MainWindow", u"Stylized", None))
#if QT_CONFIG(whatsthis)
        self.normal_btn.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.normal_btn.setText(QCoreApplication.translate("MainWindow", u"Normal", None))
        self.pixel_btn.setText(QCoreApplication.translate("MainWindow", u"Pixel", None))
        self.toon_btn.setText(QCoreApplication.translate("MainWindow", u"Toon", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Maps", None))
        self.normal_map_checkbox.setText(QCoreApplication.translate("MainWindow", u"Normal", None))
        self.roughness_map_checkbox.setText(QCoreApplication.translate("MainWindow", u"Roughness", None))
        self.specular_map_checkbox.setText(QCoreApplication.translate("MainWindow", u"Specular", None))
        self.ao_map_checkbox.setText(QCoreApplication.translate("MainWindow", u"Ambient Occlusion", None))
        self.Transparent_map_checkbox.setText(QCoreApplication.translate("MainWindow", u"Transparent", None))
        self.update_btn.setText(QCoreApplication.translate("MainWindow", u"Update Settings", None))
        self.save_btn.setText(QCoreApplication.translate("MainWindow", u"Save Textures", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Sigma_s", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Toon Strength", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Texture Strength", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Background Color", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Pixel Size", None))
        self.transparent_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"White", None))
        self.transparent_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Black", None))

        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Range", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Sigma_r", None))
        self.selected_image_label.setText("")
        self.preview_1.setText("")
        self.preview_2.setText("")
        self.preview_3.setText("")
        self.preview_4.setText("")
        self.preview_5.setText("")
        self.version_label.setText(QCoreApplication.translate("MainWindow", u"Version", None))
    # retranslateUi

