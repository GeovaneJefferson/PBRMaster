# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'stylized.ui'
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

class Ui_Stylized_Window(object):
    def setupUi(self, Stylized_Window):
        if not Stylized_Window.objectName():
            Stylized_Window.setObjectName(u"Stylized_Window")
        Stylized_Window.resize(400, 300)
        self.gridLayout = QGridLayout(Stylized_Window)
        self.gridLayout.setObjectName(u"gridLayout")
        self.normal_mode = QComboBox(Stylized_Window)
        self.normal_mode.addItem("")
        self.normal_mode.addItem("")
        self.normal_mode.setObjectName(u"normal_mode")

        self.gridLayout.addWidget(self.normal_mode, 3, 1, 1, 1, Qt.AlignRight)

        self.label_2 = QLabel(Stylized_Window)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 4, 0, 1, 1)

        self.sigma_r_spinbox = QSpinBox(Stylized_Window)
        self.sigma_r_spinbox.setObjectName(u"sigma_r_spinbox")

        self.gridLayout.addWidget(self.sigma_r_spinbox, 1, 1, 1, 1, Qt.AlignRight)

        self.sigma_s_spinbox = QSpinBox(Stylized_Window)
        self.sigma_s_spinbox.setObjectName(u"sigma_s_spinbox")

        self.gridLayout.addWidget(self.sigma_s_spinbox, 0, 1, 1, 1, Qt.AlignRight)

        self.label = QLabel(Stylized_Window)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setBold(True)
        self.label.setFont(font)

        self.gridLayout.addWidget(self.label, 5, 0, 1, 1)

        self.Stylized_Preview_Label = QLabel(Stylized_Window)
        self.Stylized_Preview_Label.setObjectName(u"Stylized_Preview_Label")

        self.gridLayout.addWidget(self.Stylized_Preview_Label, 6, 0, 1, 1)

        self.label_9 = QLabel(Stylized_Window)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout.addWidget(self.label_9, 0, 0, 1, 1)

        self.label_5 = QLabel(Stylized_Window)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1)

        self.stylized_generate_btn = QPushButton(Stylized_Window)
        self.stylized_generate_btn.setObjectName(u"stylized_generate_btn")
        self.stylized_generate_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.stylized_generate_btn, 7, 1, 1, 1, Qt.AlignRight|Qt.AlignBottom)

        self.label_3 = QLabel(Stylized_Window)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.normal_size_spinbox = QSpinBox(Stylized_Window)
        self.normal_size_spinbox.setObjectName(u"normal_size_spinbox")

        self.gridLayout.addWidget(self.normal_size_spinbox, 2, 1, 1, 1, Qt.AlignRight)


        self.retranslateUi(Stylized_Window)

        QMetaObject.connectSlotsByName(Stylized_Window)
    # setupUi

    def retranslateUi(self, Stylized_Window):
        Stylized_Window.setWindowTitle(QCoreApplication.translate("Stylized_Window", u"Form", None))
        self.normal_mode.setItemText(0, QCoreApplication.translate("Stylized_Window", u"NormalDX", None))
        self.normal_mode.setItemText(1, QCoreApplication.translate("Stylized_Window", u"NormalGL", None))

        self.label_2.setText(QCoreApplication.translate("Stylized_Window", u"Mode", None))
        self.label.setText(QCoreApplication.translate("Stylized_Window", u"Preview:", None))
        self.Stylized_Preview_Label.setText("")
        self.label_9.setText(QCoreApplication.translate("Stylized_Window", u"Sigma_s", None))
        self.label_5.setText(QCoreApplication.translate("Stylized_Window", u"Sigma_r", None))
        self.stylized_generate_btn.setText(QCoreApplication.translate("Stylized_Window", u"Generate", None))
        self.label_3.setText(QCoreApplication.translate("Stylized_Window", u"Normal Map strength", None))
    # retranslateUi

