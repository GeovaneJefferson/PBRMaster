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
        MainWindow.resize(900, 600)
        MainWindow.setMaximumSize(QSize(900, 600))
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

        self.specular_map_checkbox = QCheckBox(self.centralwidget)
        self.specular_map_checkbox.setObjectName(u"specular_map_checkbox")

        self.verticalLayout_3.addWidget(self.specular_map_checkbox)

        self.roughness_map_checkbox = QCheckBox(self.centralwidget)
        self.roughness_map_checkbox.setObjectName(u"roughness_map_checkbox")

        self.verticalLayout_3.addWidget(self.roughness_map_checkbox)

        self.Transparent_map_checkbox = QCheckBox(self.centralwidget)
        self.Transparent_map_checkbox.setObjectName(u"Transparent_map_checkbox")

        self.verticalLayout_3.addWidget(self.Transparent_map_checkbox)


        self.verticalLayout.addLayout(self.verticalLayout_3)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.verticalLayout.addWidget(self.label_4, 0, Qt.AlignHCenter)

        self.stylized_settings = QWidget(self.centralwidget)
        self.stylized_settings.setObjectName(u"stylized_settings")
        self.stylized_settings.setMinimumSize(QSize(0, 70))
        self.verticalLayoutWidget_3 = QWidget(self.stylized_settings)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(0, 0, 177, 64))
        self.layout_s = QVBoxLayout(self.verticalLayoutWidget_3)
        self.layout_s.setObjectName(u"layout_s")
        self.layout_s.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_9 = QLabel(self.verticalLayoutWidget_3)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_8.addWidget(self.label_9)

        self.sigma_s_spinbox = QSpinBox(self.verticalLayoutWidget_3)
        self.sigma_s_spinbox.setObjectName(u"sigma_s_spinbox")

        self.horizontalLayout_8.addWidget(self.sigma_s_spinbox, 0, Qt.AlignLeft)


        self.layout_s.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_5 = QLabel(self.verticalLayoutWidget_3)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_9.addWidget(self.label_5)

        self.sigma_r_spinbox = QSpinBox(self.verticalLayoutWidget_3)
        self.sigma_r_spinbox.setObjectName(u"sigma_r_spinbox")

        self.horizontalLayout_9.addWidget(self.sigma_r_spinbox, 0, Qt.AlignLeft)


        self.layout_s.addLayout(self.horizontalLayout_9)


        self.verticalLayout.addWidget(self.stylized_settings)

        self.pixel_settings = QWidget(self.centralwidget)
        self.pixel_settings.setObjectName(u"pixel_settings")
        self.gridLayout_3 = QGridLayout(self.pixel_settings)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(0)
        self.gridLayout_3.setVerticalSpacing(9)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.pixel_size_spinbox = QSpinBox(self.pixel_settings)
        self.pixel_size_spinbox.setObjectName(u"pixel_size_spinbox")

        self.gridLayout_3.addWidget(self.pixel_size_spinbox, 0, 1, 1, 1, Qt.AlignLeft)

        self.label_10 = QLabel(self.pixel_settings)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_3.addWidget(self.label_10, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.pixel_settings)

        self.transparent_settings = QWidget(self.centralwidget)
        self.transparent_settings.setObjectName(u"transparent_settings")
        self.gridLayout_6 = QGridLayout(self.transparent_settings)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_7 = QLabel(self.transparent_settings)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_5.addWidget(self.label_7, 0, 0, 1, 1)

        self.transparent_comboBox = QComboBox(self.transparent_settings)
        self.transparent_comboBox.addItem("")
        self.transparent_comboBox.addItem("")
        self.transparent_comboBox.setObjectName(u"transparent_comboBox")
        self.transparent_comboBox.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_5.addWidget(self.transparent_comboBox, 0, 1, 1, 1, Qt.AlignLeft)

        self.label_11 = QLabel(self.transparent_settings)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_5.addWidget(self.label_11, 1, 0, 1, 1)

        self.transparent_size_spinbox = QSpinBox(self.transparent_settings)
        self.transparent_size_spinbox.setObjectName(u"transparent_size_spinbox")

        self.gridLayout_5.addWidget(self.transparent_size_spinbox, 1, 1, 1, 1, Qt.AlignLeft)


        self.gridLayout_6.addLayout(self.gridLayout_5, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.transparent_settings)

        self.normal_settings = QWidget(self.centralwidget)
        self.normal_settings.setObjectName(u"normal_settings")
        self.normal_settings.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_3 = QHBoxLayout(self.normal_settings)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_12 = QLabel(self.normal_settings)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_3.addWidget(self.label_12, 0, Qt.AlignLeft|Qt.AlignTop)

        self.normal_size_spinbox = QSpinBox(self.normal_settings)
        self.normal_size_spinbox.setObjectName(u"normal_size_spinbox")

        self.horizontalLayout_3.addWidget(self.normal_size_spinbox, 0, Qt.AlignLeft|Qt.AlignTop)


        self.verticalLayout.addWidget(self.normal_settings, 0, Qt.AlignTop)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.toon_settings = QWidget(self.centralwidget)
        self.toon_settings.setObjectName(u"toon_settings")
        self.toon_settings.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_5 = QHBoxLayout(self.toon_settings)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_3 = QLabel(self.toon_settings)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_4.addWidget(self.label_3, 0, Qt.AlignLeft|Qt.AlignTop)

        self.toon_size_spinbox = QSpinBox(self.toon_settings)
        self.toon_size_spinbox.setObjectName(u"toon_size_spinbox")

        self.horizontalLayout_4.addWidget(self.toon_size_spinbox, 0, Qt.AlignLeft|Qt.AlignTop)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)


        self.verticalLayout.addWidget(self.toon_settings)

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

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer)


        self.verticalLayout_2.addLayout(self.horizontalLayout_7)

        self.verticalLayout_2.setStretch(0, 1)

        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.horizontalLayout.setStretch(2, 1)

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
        self.specular_map_checkbox.setText(QCoreApplication.translate("MainWindow", u"Specular", None))
        self.roughness_map_checkbox.setText(QCoreApplication.translate("MainWindow", u"Roughness", None))
        self.Transparent_map_checkbox.setText(QCoreApplication.translate("MainWindow", u"Transparent", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Sigma_s", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Sigma_r", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Pixel Size", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Background Color", None))
        self.transparent_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"White", None))
        self.transparent_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Black", None))

        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Range", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Strength", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Strength", None))
        self.update_btn.setText(QCoreApplication.translate("MainWindow", u"Update Settings", None))
        self.save_btn.setText(QCoreApplication.translate("MainWindow", u"Save Textures", None))
        self.selected_image_label.setText("")
        self.preview_1.setText("")
        self.preview_2.setText("")
        self.preview_3.setText("")
        self.preview_4.setText("")
        self.version_label.setText(QCoreApplication.translate("MainWindow", u"Version", None))
    # retranslateUi

