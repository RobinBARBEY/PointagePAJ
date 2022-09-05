# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'splash_screenEQHhSi.ui'
##
## Created by: Qt User Interface Compiler version 5.15.5
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *  # type: ignore
from PySide2.QtGui import *  # type: ignore
from PySide2.QtWidgets import *  # type: ignore


class Ui_SplashScreen(object):
    def setupUi(self, SplashScreen):
        if not SplashScreen.objectName():
            SplashScreen.setObjectName(u"SplashScreen")
        SplashScreen.resize(680, 400)
        SplashScreen.setStyleSheet(u"QFrame {\n"
"                                background-color: #005369;\n"
"                                color: rgb(123, 157, 0);\n"
"                                border-radius: 10px;\n"
"                                }")
        self.centralwidget = QWidget(SplashScreen)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.dropShadowFrame = QFrame(self.centralwidget)
        self.dropShadowFrame.setObjectName(u"dropShadowFrame")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dropShadowFrame.sizePolicy().hasHeightForWidth())
        self.dropShadowFrame.setSizePolicy(sizePolicy)
        self.dropShadowFrame.setStyleSheet(u"QFrame {\n"
"                                background-color: #005369;\n"
"                                color: rgb(123, 157, 0);\n"
"                                border-radius: 10px;\n"
"                                }\n"
"                            ")
        self.dropShadowFrame.setFrameShape(QFrame.StyledPanel)
        self.dropShadowFrame.setFrameShadow(QFrame.Raised)
        self.label_title = QLabel(self.dropShadowFrame)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setGeometry(QRect(0, 70, 661, 81))
        font = QFont()
        font.setFamily(u"Noto Sans Arabic UI")
        font.setPointSize(40)
        font.setBold(False)
        font.setWeight(50)
        self.label_title.setFont(font)
        self.label_title.setStyleSheet(u"color: rgb(152, 192, 0);")
        self.label_title.setTextFormat(Qt.AutoText)
        self.label_title.setScaledContents(False)
        self.label_title.setAlignment(Qt.AlignCenter)
        self.label_description = QLabel(self.dropShadowFrame)
        self.label_description.setObjectName(u"label_description")
        self.label_description.setGeometry(QRect(0, 150, 661, 31))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(14)
        self.label_description.setFont(font1)
        self.label_description.setStyleSheet(u"color: rgb(123, 157, 0);")
        self.label_description.setAlignment(Qt.AlignCenter)
        self.progressBar = QProgressBar(self.dropShadowFrame)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(50, 240, 561, 23))
        self.progressBar.setStyleSheet(u"QProgressBar {\n"
"\n"
"                                    background-color:rgb(151, 151, 155);\n"
"                                    color: rgb(200, 200, 200);\n"
"                                    border-style: none;\n"
"                                    border-radius: 10px;\n"
"                                    text-align: center;\n"
"                                    }\n"
"                                    QProgressBar::chunk{\n"
"                                    border-radius: 10px;\n"
"                                    background-color: qlineargradient(spread:pad, x1:0, y1:0.511364, x2:1, y2:0.523,\n"
"                                    stop:0 rgba(123, 157, 0, 1), stop:1 rgba(152, 192, 0, 1));\n"
"                                    }\n"
"                                ")
        self.progressBar.setValue(24)
        self.label_description_2 = QLabel(self.dropShadowFrame)
        self.label_description_2.setObjectName(u"label_description_2")
        self.label_description_2.setGeometry(QRect(0, 260, 661, 31))
        font2 = QFont()
        font2.setFamily(u"Noto Sans")
        font2.setPointSize(10)
        self.label_description_2.setFont(font2)
        self.label_description_2.setStyleSheet(u"color: rgb(123, 157, 0);")
        self.label_description_2.setAlignment(Qt.AlignCenter)
        self.label_credits = QLabel(self.dropShadowFrame)
        self.label_credits.setObjectName(u"label_credits")
        self.label_credits.setGeometry(QRect(490, 350, 158, 18))
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(5)
        sizePolicy1.setHeightForWidth(self.label_credits.sizePolicy().hasHeightForWidth())
        self.label_credits.setSizePolicy(sizePolicy1)
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setPointSize(10)
        self.label_credits.setFont(font3)
        self.label_credits.setStyleSheet(u"color: rgb(123, 157, 0);")
        self.label_credits.setScaledContents(False)
        self.label_credits.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.dropShadowFrame)

        SplashScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(SplashScreen)

        QMetaObject.connectSlotsByName(SplashScreen)
    # setupUi

    def retranslateUi(self, SplashScreen):
        SplashScreen.setWindowTitle(QCoreApplication.translate("SplashScreen", u"MainWindow", None))
        self.label_title.setText(QCoreApplication.translate("SplashScreen", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">POINT</span> ACCUEIL JEUNES </p></body></html>", None))
        self.label_description.setText(QCoreApplication.translate("SplashScreen", u"<html><head/><body><p>POINTAGES</p></body></html>", None))
        self.label_description_2.setText(QCoreApplication.translate("SplashScreen", u"<html><head/><body><p>Loading...</p></body></html>", None))
        self.label_credits.setText(QCoreApplication.translate("SplashScreen", u"<html><head/><body><p><span style=\"\n"
"                                    font-weight:600;\">Created by</span>: BARBEY Robin</p></body></html>\n"
"                                ", None))
    # retranslateUi

