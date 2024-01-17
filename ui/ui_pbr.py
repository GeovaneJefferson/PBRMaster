# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pbr.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QSpinBox,
    QWidget)

class Ui_PBR_Window(object):
    def setupUi(self, PBR_Window):
        if not PBR_Window.objectName():
            PBR_Window.setObjectName(u"PBR_Window")
        PBR_Window.resize(400, 300)
        PBR_Window.setMaximumSize(QSize(400, 300))
        self.gridLayout = QGridLayout(PBR_Window)
        self.gridLayout.setObjectName(u"gridLayout")
        self.PBR_Preview_Label = QLabel(PBR_Window)
        self.PBR_Preview_Label.setObjectName(u"PBR_Preview_Label")

        self.gridLayout.addWidget(self.PBR_Preview_Label, 4, 0, 1, 1)

        self.label = QLabel(PBR_Window)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.normal_mode = QComboBox(PBR_Window)
        self.normal_mode.addItem("")
        self.normal_mode.addItem("")
        self.normal_mode.setObjectName(u"normal_mode")

        self.gridLayout.addWidget(self.normal_mode, 1, 1, 1, 1, Qt.AlignRight)

        self.normal_size_spinbox = QSpinBox(PBR_Window)
        self.normal_size_spinbox.setObjectName(u"normal_size_spinbox")

        self.gridLayout.addWidget(self.normal_size_spinbox, 0, 1, 1, 1, Qt.AlignRight)

        self.pbr_generate_btn = QPushButton(PBR_Window)
        self.pbr_generate_btn.setObjectName(u"pbr_generate_btn")
        self.pbr_generate_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.pbr_generate_btn, 6, 1, 1, 1, Qt.AlignRight|Qt.AlignBottom)

        self.label_2 = QLabel(PBR_Window)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setBold(True)
        self.label_2.setFont(font)

        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)

        self.label_12 = QLabel(PBR_Window)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout.addWidget(self.label_12, 0, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 2, 0, 1, 1)


        self.retranslateUi(PBR_Window)

        QMetaObject.connectSlotsByName(PBR_Window)
    # setupUi

    def retranslateUi(self, PBR_Window):
        PBR_Window.setWindowTitle(QCoreApplication.translate("PBR_Window", u"Form", None))
        self.PBR_Preview_Label.setText("")
        self.label.setText(QCoreApplication.translate("PBR_Window", u"Mode", None))
        self.normal_mode.setItemText(0, QCoreApplication.translate("PBR_Window", u"NormalDX", None))
        self.normal_mode.setItemText(1, QCoreApplication.translate("PBR_Window", u"NormalGL", None))

        self.pbr_generate_btn.setText(QCoreApplication.translate("PBR_Window", u"Generate", None))
        self.label_2.setText(QCoreApplication.translate("PBR_Window", u"Preview:", None))
        self.label_12.setText(QCoreApplication.translate("PBR_Window", u"Normal Map", None))
    # retranslateUi

