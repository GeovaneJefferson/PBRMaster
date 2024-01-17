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
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QSpinBox, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1200, 800)
        MainWindow.setMinimumSize(QSize(1200, 800))
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        self.actionPBR = QAction(MainWindow)
        self.actionPBR.setObjectName(u"actionPBR")
        self.actionStylized = QAction(MainWindow)
        self.actionStylized.setObjectName(u"actionStylized")
        self.actionPixel = QAction(MainWindow)
        self.actionPixel.setObjectName(u"actionPixel")
        self.actionOpen_Texture = QAction(MainWindow)
        self.actionOpen_Texture.setObjectName(u"actionOpen_Texture")
        self.actionSave_New_Textures = QAction(MainWindow)
        self.actionSave_New_Textures.setObjectName(u"actionSave_New_Textures")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.drag_and_drop_image = QLabel(self.centralwidget)
        self.drag_and_drop_image.setObjectName(u"drag_and_drop_image")

        self.verticalLayout.addWidget(self.drag_and_drop_image)

        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        font = QFont()
        font.setBold(True)
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


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.line_12 = QFrame(self.centralwidget)
        self.line_12.setObjectName(u"line_12")
        self.line_12.setFrameShape(QFrame.VLine)
        self.line_12.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line_12)

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

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.line_3 = QFrame(self.centralwidget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.gridLayout_5.addWidget(self.line_3, 2, 1, 1, 1)

        self.line_10 = QFrame(self.centralwidget)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setFrameShape(QFrame.HLine)
        self.line_10.setFrameShadow(QFrame.Sunken)

        self.gridLayout_5.addWidget(self.line_10, 6, 0, 1, 1)

        self.line_11 = QFrame(self.centralwidget)
        self.line_11.setObjectName(u"line_11")
        self.line_11.setFrameShape(QFrame.HLine)
        self.line_11.setFrameShadow(QFrame.Sunken)

        self.gridLayout_5.addWidget(self.line_11, 6, 1, 1, 1)

        self.pixel_size_spinbox = QSpinBox(self.centralwidget)
        self.pixel_size_spinbox.setObjectName(u"pixel_size_spinbox")

        self.gridLayout_5.addWidget(self.pixel_size_spinbox, 1, 1, 1, 1, Qt.AlignLeft)

        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_5.addWidget(self.label_10, 1, 0, 1, 1)

        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_5.addWidget(self.label_7, 3, 0, 1, 1)

        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout_5.addWidget(self.line_2, 2, 0, 1, 1)

        self.line_5 = QFrame(self.centralwidget)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.gridLayout_5.addWidget(self.line_5, 0, 1, 1, 1)

        self.line_4 = QFrame(self.centralwidget)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.gridLayout_5.addWidget(self.line_4, 0, 0, 1, 1)

        self.label_11 = QLabel(self.centralwidget)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_5.addWidget(self.label_11, 4, 0, 1, 1)

        self.transparent_comboBox = QComboBox(self.centralwidget)
        self.transparent_comboBox.addItem("")
        self.transparent_comboBox.addItem("")
        self.transparent_comboBox.setObjectName(u"transparent_comboBox")
        self.transparent_comboBox.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_5.addWidget(self.transparent_comboBox, 3, 1, 1, 1, Qt.AlignLeft)

        self.transparent_size_spinbox = QSpinBox(self.centralwidget)
        self.transparent_size_spinbox.setObjectName(u"transparent_size_spinbox")

        self.gridLayout_5.addWidget(self.transparent_size_spinbox, 4, 1, 1, 1, Qt.AlignLeft)


        self.verticalLayout_4.addLayout(self.gridLayout_5)

        self.update_btn = QPushButton(self.centralwidget)
        self.update_btn.setObjectName(u"update_btn")
        self.update_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_4.addWidget(self.update_btn)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)


        self.horizontalLayout_2.addLayout(self.verticalLayout_4)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 1200, 24))
        self.menuFilters = QMenu(self.menuBar)
        self.menuFilters.setObjectName(u"menuFilters")
        self.menuFile = QMenu(self.menuBar)
        self.menuFile.setObjectName(u"menuFile")
        MainWindow.setMenuBar(self.menuBar)

        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuFilters.menuAction())
        self.menuFilters.addAction(self.actionPBR)
        self.menuFilters.addAction(self.actionStylized)
        self.menuFilters.addAction(self.actionPixel)
        self.menuFile.addAction(self.actionOpen_Texture)
        self.menuFile.addAction(self.actionSave_New_Textures)

        self.retranslateUi(MainWindow)

        self.transparent_comboBox.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionPBR.setText(QCoreApplication.translate("MainWindow", u"PBR", None))
        self.actionStylized.setText(QCoreApplication.translate("MainWindow", u"Stylized", None))
        self.actionPixel.setText(QCoreApplication.translate("MainWindow", u"Pixel", None))
        self.actionOpen_Texture.setText(QCoreApplication.translate("MainWindow", u"Open Texture", None))
        self.actionSave_New_Textures.setText(QCoreApplication.translate("MainWindow", u"Save New Textures", None))
        self.drag_and_drop_image.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Maps", None))
        self.normal_map_checkbox.setText(QCoreApplication.translate("MainWindow", u"Normal", None))
        self.roughness_map_checkbox.setText(QCoreApplication.translate("MainWindow", u"Roughness", None))
        self.specular_map_checkbox.setText(QCoreApplication.translate("MainWindow", u"Specular", None))
        self.ao_map_checkbox.setText(QCoreApplication.translate("MainWindow", u"Ambient Occlusion", None))
        self.Transparent_map_checkbox.setText(QCoreApplication.translate("MainWindow", u"Transparent", None))
        self.selected_image_label.setText("")
        self.preview_1.setText("")
        self.preview_2.setText("")
        self.preview_3.setText("")
        self.preview_4.setText("")
        self.preview_5.setText("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Pixel Size", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Background Color", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Range", None))
        self.transparent_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"White", None))
        self.transparent_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Black", None))

        self.update_btn.setText(QCoreApplication.translate("MainWindow", u"Update Settings", None))
        self.menuFilters.setTitle(QCoreApplication.translate("MainWindow", u"Generate", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi

