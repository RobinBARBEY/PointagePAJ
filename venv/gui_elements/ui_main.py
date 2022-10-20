# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainPyQDMA.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QCheckBox, QComboBox,
    QDateEdit, QFormLayout, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QTableView, QTextBrowser, QVBoxLayout,
    QWidget)
import rc_icons

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1145, 766)
        MainWindow.setStyleSheet(u"/*Copyright (c) DevSec Studio. All rights reserved.\n"
"\n"
"MIT License\n"
"\n"
"Permission is hereby granted, free of charge, to any person obtaining a copy\n"
"of this software and associated documentation files (the \"Software\"), to deal\n"
"in the Software without restriction, including without limitation the rights\n"
"to use, copy, modify, merge, publish, distribute, sublicense, and/or sell\n"
"copies of the Software, and to permit persons to whom the Software is\n"
"furnished to do so, subject to the following conditions:\n"
"\n"
"The above copyright notice and this permission notice shall be included in all\n"
"copies or substantial portions of the Software.\n"
"\n"
"THE SOFTWARE IS PROVIDED *AS IS*, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR\n"
"IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,\n"
"FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE\n"
"AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER\n"
"LIABILITY, WHETHER IN AN ACT"
                        "ION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,\n"
"OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.\n"
"*/\n"
"\n"
"/*-----QWidget-----*/\n"
"QWidget\n"
"{\n"
"		background-color: #005369;\n"
"        color: rgb(152, 192, 0);\n"
"		border-radius: 16px;\n"
"}\n"
"\n"
"QFrame\n"
"{\n"
"		background-color: #005369;\n"
"        color: rgb(152, 192, 0);\n"
"		border: 1px solid rgb(154, 192, 0);\n"
"		border-color: rgb(123, 157, 0);\n"
"		border-radius: 16px;\n"
"		padding: 2px;\n"
"}\n"
"\n"
"/*-----QLabel-----*/\n"
"QLabel\n"
"{\n"
"	background-color: transparent;\n"
"	color: #98c000;\n"
"	font-size: 18px;\n"
"	border: 0px;\n"
"	padding: 2px;\n"
"}\n"
"\n"
"\n"
"/*-----QPushButton-----*/\n"
"QPushButton\n"
"{\n"
"	background-color: rgb(7, 66, 83);\n"
"	color: rgb(152, 192, 0);\n"
"	font-size: 16px;\n"
"	font-weight: bold;\n"
"	border: 1px solid rgb(119, 149, 0);\n"
"	border-radius: 8px;\n"
"	padding: 7px;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"	background-"
                        "color: rgb(16, 163, 206) ;\n"
"	border: 3px solid rgb(128, 156, 15);\n"
"}\n"
"\n"
"/*-----QComboBox-----*/\n"
"QComboBox\n"
"{\n"
"	background-color: rgb(215, 248, 255);\n"
"	color: rgb(0, 0, 0);\n"
"	font-size: 18px;\n"
"	font-weight: bold;\n"
"	border-radius: 10px;\n"
"	padding: 6px;\n"
"}\n"
"\n"
"QComboBox::drop-down{\n"
"	width: 30px;\n"
"	border: 0px;\n"
"	padding-right: 0px;\n"
"}\n"
"\n"
"QComboBox::down-arrow{\n"
"	image: url(:/Icons/icons8-drop-down-50.png);\n"
"	height: 20px;\n"
"	width: 20px;\n"
"}\n"
"\n"
"QComboBox:on{\n"
"	 border: 1px solid rgb(152, 192, 0);\n"
"}\n"
"\n"
"\n"
"QComboBox QListView{\n"
"	font: 14px;\n"
"	border: 1px solid rgb(152, 192, 0);\n"
"	padding: 5px;\n"
"	background-color: rgb(7, 66, 83);\n"
"	outline: 0px;\n"
"}\n"
"\n"
"QComboBox QListView:item{\n"
"	font-size: 14px;\n"
"	padding-left: 10px;\n"
"	background-color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QComboBox QListView:item:hover{\n"
"	background-color: rgb(7, 66, 83);\n"
"	color: rgb(60, 181, 181);\n"
"	border: 1px solid rg"
                        "b(152, 192, 0);\n"
"	font-size: 14px;\n"
"}\n"
"\n"
"\n"
"/*-----QCheckBox-----*/\n"
"QCheckBox\n"
"{\n"
"	background-color: transparent;\n"
"	color: #fff;\n"
"	font-size: 18px;\n"
"	font-weight: bold;\n"
"	border: none;\n"
"	border-radius: 5px;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QCheckBox-----*/\n"
"QCheckBox::indicator\n"
"{\n"
"    color: #b1b1b1;\n"
"    background-color: #323232;\n"
"    border: 1px solid darkgray;\n"
"    width: 12px;\n"
"    height: 12px;\n"
"\n"
"}\n"
"\n"
"\n"
"QCheckBox::indicator:checked\n"
"{\n"
"    image:url(\"./ressources/check.png\");\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.511, x2:1, y2:0.511, stop:0 rgba(0, 172, 149, 255),stop:0.995192 rgba(54, 197, 177, 255));;\n"
"    border: 1px solid #607cff;\n"
"\n"
"}\n"
"\n"
"\n"
"QCheckBox::indicator:unchecked:hover\n"
"{\n"
"    border: 1px solid #98c000;\n"
"\n"
"}\n"
"\n"
"\n"
"QCheckBox::disabled\n"
"{\n"
"	color: #656565;\n"
"\n"
"}\n"
"\n"
"\n"
"QCheckBox::indicator:disabled\n"
"{\n"
"	background-color: #65656"
                        "5;\n"
"	color: #656565;\n"
"    border: 1px solid #656565;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QLineEdit-----*/\n"
"QLineEdit\n"
"{\n"
"	background-color: rgb(215, 248, 255);\n"
"	color: rgb(0, 0, 0);\n"
"	font-size: 18px;\n"
"	font-weight: bold;\n"
"	border-radius: 10px;\n"
"	padding: 6px;\n"
"\n"
"}\n"
"\n"
"/*-----QLineEdit-----*/\n"
"QDateEdit\n"
"{\n"
"	background-color: rgb(215, 248, 255);\n"
"	color: rgb(0, 0, 0);\n"
"	font-size: 18px;\n"
"	font-weight: bold;\n"
"	border-radius: 10px;\n"
"	padding: 6px;\n"
"}\n"
"\n"
"QDateEdit::drop-down{\n"
"	width: 30px;\n"
"	border: 0px;\n"
"	padding-right: 0px;\n"
"}\n"
"\n"
"QDateEdit::down-arrow{\n"
"	image: url(:/Icons/icons8-drop-down-50.png);\n"
"	height: 20px;\n"
"	width: 20px;\n"
"}\n"
"\n"
"\n"
"/*-----QListView-----*/\n"
"QListView\n"
"{\n"
"	background-color: rgb(7, 66, 83);\n"
"	color: rgb(152, 192, 19)rgb(152, 192, 0);\n"
"	font-size: 14px;\n"
"	font-weight: bold;\n"
"	border: 1px solid #191919;\n"
"	border-radius: 10px;\n"
"\n"
"\n"
"}\n"
"\n"
"\n"
"QListV"
                        "iew::item\n"
"{\n"
"	color: #31cecb;\n"
"	background-color:rgb(7, 66, 83);\n"
"	border: 1px solid rgb(152, 192, 0);\n"
"	padding: 5px;\n"
"	border-radius: 10px;\n"
"	padding-left : 10px;\n"
"	height: 42px;\n"
"\n"
"}\n"
"\n"
"QListView::item:selected\n"
"{\n"
"	background-color: rgb(7, 66, 83);\n"
"\n"
"}\n"
"\n"
"\n"
"QListView::item:!selected\n"
"{\n"
"	color:white;\n"
"	background-color: transparent;\n"
"	border: none;\n"
"	padding-left : 10px;\n"
"\n"
"}\n"
"\n"
"\n"
"QListView::item:!selected:hover\n"
"{\n"
"	color: #bbbcba;\n"
"	background-color: #454e5e;\n"
"	border: none;\n"
"	padding-left : 10px;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QTreeView-----*/\n"
"QTreeView \n"
"{\n"
"	background-color: #232939;\n"
"	show-decoration-selected: 0;\n"
"	color: #c2c8d7;\n"
"\n"
"}\n"
"\n"
"\n"
"QTreeView::item \n"
"{\n"
"	border-top-color: transparent;\n"
"	border-bottom-color: transparent;\n"
"\n"
"}\n"
"\n"
"\n"
"QTreeView::item:hover \n"
"{\n"
"	background-color: #606060;\n"
"	color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QTr"
                        "eeView::item:selected \n"
"{\n"
"	background-color: #0ab19a;\n"
"	color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QTreeView::item:selected:active\n"
"{\n"
"	background-color: #0ab19a;\n"
"	color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QTreeView::branch:has-children:!has-siblings:closed,\n"
"QTreeView::branch:closed:has-children:has-siblings \n"
"{\n"
"	image: url(://tree-closed.png);\n"
"\n"
"}\n"
"\n"
"QTreeView::branch:open:has-children:!has-siblings,\n"
"QTreeView::branch:open:has-children:has-siblings  \n"
"{\n"
"	image: url(://tree-open.png);\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QTableView & QTableWidget-----*/\n"
"QTableView\n"
"{\n"
"    background-color: #232939;\n"
"	border: 1px solid gray;\n"
"    color: #f0f0f0;\n"
"    gridline-color: #232939;\n"
"    outline : 0;\n"
"\n"
"}\n"
"\n"
"\n"
"QTableView::disabled\n"
"{\n"
"    background-color: #242526;\n"
"    border: 1px solid #32414B;\n"
"    color: #656565;\n"
"    gridline-color: #656565;\n"
"    outline : 0;\n"
"\n"
"}\n"
"\n"
"\n"
"QTableView::item:hover \n"
"{\n"
"  "
                        "  background-color: #606060;\n"
"    color: #f0f0f0;\n"
"\n"
"}\n"
"\n"
"\n"
"QTableView::item:selected \n"
"{\n"
"	background-color: #0ab19a;\n"
"    color: #F0F0F0;\n"
"\n"
"}\n"
"\n"
"\n"
"QTableView::item:selected:disabled\n"
"{\n"
"    background-color: #1a1b1c;\n"
"    border: 2px solid #525251;\n"
"    color: #656565;\n"
"\n"
"}\n"
"\n"
"\n"
"QTableCornerButton::section\n"
"{\n"
"	background-color: #343a49;\n"
"    color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section\n"
"{\n"
"	color: #fff;\n"
"	border-top: 0px;\n"
"	border-bottom: 1px solid gray;\n"
"	border-right: 1px solid gray;\n"
"	background-color: #343a49;\n"
"    margin-top:1px;\n"
"	margin-bottom:1px;\n"
"	padding: 5px;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section:disabled\n"
"{\n"
"    background-color: #525251;\n"
"    color: #656565;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section:checked\n"
"{\n"
"    color: #fff;\n"
"    background-color: #0ab19a;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section:checked:disabled\n"
"{\n"
"    color: #656"
                        "565;\n"
"    background-color: #525251;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section::vertical::first,\n"
"QHeaderView::section::vertical::only-one\n"
"{\n"
"    border-top: 1px solid #353635;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section::vertical\n"
"{\n"
"    border-top: 1px solid #353635;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section::horizontal::first,\n"
"QHeaderView::section::horizontal::only-one\n"
"{\n"
"    border-left: 1px solid #353635;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section::horizontal\n"
"{\n"
"    border-left: 1px solid #353635;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QScrollBar-----*/\n"
"QScrollBar:horizontal \n"
"{\n"
"    background-color: transparent;\n"
"    height: 8px;\n"
"    margin: 0px;\n"
"    padding: 0px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::handle:horizontal \n"
"{\n"
"    border: none;\n"
"	min-width: 100px;\n"
"    background-color: #56576c;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:horizontal, \n"
"QScrollBar::sub-line:horizontal,\n"
"QScrollBar::add-page:horizontal, \n"
"Q"
                        "ScrollBar::sub-page:horizontal \n"
"{\n"
"    width: 0px;\n"
"    background-color: transparent;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar:vertical \n"
"{\n"
"    background-color: transparent;\n"
"    width: 8px;\n"
"    margin: 0;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::handle:vertical \n"
"{\n"
"    border: none;\n"
"	min-height: 100px;\n"
"    background-color: #56576c;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:vertical, \n"
"QScrollBar::sub-line:vertical,\n"
"QScrollBar::add-page:vertical, \n"
"QScrollBar::sub-page:vertical \n"
"{\n"
"    height: 0px;\n"
"    background-color: transparent;\n"
"\n"
"}\n"
"")
        self.centralwidgetMain = QWidget(MainWindow)
        self.centralwidgetMain.setObjectName(u"centralwidgetMain")
        self.centralwidgetMain.setStyleSheet(u"")
        self.verticalLayout_16 = QVBoxLayout(self.centralwidgetMain)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.frameHeader = QFrame(self.centralwidgetMain)
        self.frameHeader.setObjectName(u"frameHeader")
        self.frameHeader.setStyleSheet(u"")
        self.frameHeader.setFrameShape(QFrame.StyledPanel)
        self.frameHeader.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frameHeader)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.labelBienvenue = QLabel(self.frameHeader)
        self.labelBienvenue.setObjectName(u"labelBienvenue")

        self.horizontalLayout_3.addWidget(self.labelBienvenue, 0, Qt.AlignHCenter)

        self.dateEditAfficahgeDate = QDateEdit(self.frameHeader)
        self.dateEditAfficahgeDate.setObjectName(u"dateEditAfficahgeDate")
        self.dateEditAfficahgeDate.setEnabled(False)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dateEditAfficahgeDate.sizePolicy().hasHeightForWidth())
        self.dateEditAfficahgeDate.setSizePolicy(sizePolicy)
        self.dateEditAfficahgeDate.setMinimumSize(QSize(140, 0))
        self.dateEditAfficahgeDate.setMaximumSize(QSize(90, 16777215))
        self.dateEditAfficahgeDate.setStyleSheet(u"background-color: rgb(0, 83, 105);\n"
"color: rgb(152, 192, 0);\n"
"border: 1px solid rgb(123, 157, 0);\n"
"border-radius: 10px;\n"
"padding: 5px;")
        self.dateEditAfficahgeDate.setWrapping(False)
        self.dateEditAfficahgeDate.setFrame(True)
        self.dateEditAfficahgeDate.setAlignment(Qt.AlignCenter)
        self.dateEditAfficahgeDate.setReadOnly(True)
        self.dateEditAfficahgeDate.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.dateEditAfficahgeDate.setKeyboardTracking(False)

        self.horizontalLayout_3.addWidget(self.dateEditAfficahgeDate)


        self.verticalLayout_16.addWidget(self.frameHeader)

        self.SideMenu = QWidget(self.centralwidgetMain)
        self.SideMenu.setObjectName(u"SideMenu")
        sizePolicy.setHeightForWidth(self.SideMenu.sizePolicy().hasHeightForWidth())
        self.SideMenu.setSizePolicy(sizePolicy)
        self.horizontalLayout_4 = QHBoxLayout(self.SideMenu)
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.MenuFrame = QFrame(self.SideMenu)
        self.MenuFrame.setObjectName(u"MenuFrame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(3)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.MenuFrame.sizePolicy().hasHeightForWidth())
        self.MenuFrame.setSizePolicy(sizePolicy1)
        self.MenuFrame.setMaximumSize(QSize(16777215, 16777215))
        self.MenuFrame.setStyleSheet(u"")
        self.MenuFrame.setFrameShape(QFrame.StyledPanel)
        self.MenuFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.MenuFrame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.PB_Pointage = QPushButton(self.MenuFrame)
        self.PB_Pointage.setObjectName(u"PB_Pointage")
        self.PB_Pointage.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.PB_Pointage.sizePolicy().hasHeightForWidth())
        self.PB_Pointage.setSizePolicy(sizePolicy2)

        self.verticalLayout_3.addWidget(self.PB_Pointage)

        self.PB_Inscription = QPushButton(self.MenuFrame)
        self.PB_Inscription.setObjectName(u"PB_Inscription")
        self.PB_Inscription.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.PB_Inscription.sizePolicy().hasHeightForWidth())
        self.PB_Inscription.setSizePolicy(sizePolicy2)
        self.PB_Inscription.setCheckable(False)
        self.PB_Inscription.setAutoDefault(False)
        self.PB_Inscription.setFlat(False)

        self.verticalLayout_3.addWidget(self.PB_Inscription)

        self.PB_Modif = QPushButton(self.MenuFrame)
        self.PB_Modif.setObjectName(u"PB_Modif")
        sizePolicy2.setHeightForWidth(self.PB_Modif.sizePolicy().hasHeightForWidth())
        self.PB_Modif.setSizePolicy(sizePolicy2)

        self.verticalLayout_3.addWidget(self.PB_Modif)

        self.PB_Totaux = QPushButton(self.MenuFrame)
        self.PB_Totaux.setObjectName(u"PB_Totaux")
        sizePolicy2.setHeightForWidth(self.PB_Totaux.sizePolicy().hasHeightForWidth())
        self.PB_Totaux.setSizePolicy(sizePolicy2)

        self.verticalLayout_3.addWidget(self.PB_Totaux)

        self.PB_Extraction = QPushButton(self.MenuFrame)
        self.PB_Extraction.setObjectName(u"PB_Extraction")
        sizePolicy2.setHeightForWidth(self.PB_Extraction.sizePolicy().hasHeightForWidth())
        self.PB_Extraction.setSizePolicy(sizePolicy2)

        self.verticalLayout_3.addWidget(self.PB_Extraction)

        self.PB_Inscription.raise_()
        self.PB_Modif.raise_()
        self.PB_Totaux.raise_()
        self.PB_Extraction.raise_()
        self.PB_Pointage.raise_()

        self.horizontalLayout_4.addWidget(self.MenuFrame)

        self.stackedWidgetPages = QStackedWidget(self.SideMenu)
        self.stackedWidgetPages.setObjectName(u"stackedWidgetPages")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(10)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.stackedWidgetPages.sizePolicy().hasHeightForWidth())
        self.stackedWidgetPages.setSizePolicy(sizePolicy3)
        self.stackedWidgetPages.setStyleSheet(u"")
        self.stackedWidgetPages.setFrameShape(QFrame.StyledPanel)
        self.stackedWidgetPages.setFrameShadow(QFrame.Raised)
        self.PagePointage = QWidget()
        self.PagePointage.setObjectName(u"PagePointage")
        self.verticalLayout_2 = QVBoxLayout(self.PagePointage)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_5 = QFrame(self.PagePointage)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_5)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_12 = QLabel(self.frame_5)
        self.label_12.setObjectName(u"label_12")

        self.verticalLayout_4.addWidget(self.label_12, 0, Qt.AlignHCenter)


        self.verticalLayout_2.addWidget(self.frame_5)

        self.verticalSpacerPointage = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacerPointage)

        self.frameEntreNom = QFrame(self.PagePointage)
        self.frameEntreNom.setObjectName(u"frameEntreNom")
        sizePolicy.setHeightForWidth(self.frameEntreNom.sizePolicy().hasHeightForWidth())
        self.frameEntreNom.setSizePolicy(sizePolicy)
        self.frameEntreNom.setFrameShape(QFrame.StyledPanel)
        self.frameEntreNom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frameEntreNom)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.labelEntreNom = QLabel(self.frameEntreNom)
        self.labelEntreNom.setObjectName(u"labelEntreNom")

        self.verticalLayout_15.addWidget(self.labelEntreNom)


        self.verticalLayout_2.addWidget(self.frameEntreNom, 0, Qt.AlignHCenter)

        self.comboBoxEntreePointage = QComboBox(self.PagePointage)
        self.comboBoxEntreePointage.setObjectName(u"comboBoxEntreePointage")
        sizePolicy.setHeightForWidth(self.comboBoxEntreePointage.sizePolicy().hasHeightForWidth())
        self.comboBoxEntreePointage.setSizePolicy(sizePolicy)
        self.comboBoxEntreePointage.setStyleSheet(u"")
        self.comboBoxEntreePointage.setEditable(True)
        self.comboBoxEntreePointage.setInsertPolicy(QComboBox.NoInsert)

        self.verticalLayout_2.addWidget(self.comboBoxEntreePointage)

        self.pushButtonValiderPointage = QPushButton(self.PagePointage)
        self.pushButtonValiderPointage.setObjectName(u"pushButtonValiderPointage")
        sizePolicy4 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.pushButtonValiderPointage.sizePolicy().hasHeightForWidth())
        self.pushButtonValiderPointage.setSizePolicy(sizePolicy4)

        self.verticalLayout_2.addWidget(self.pushButtonValiderPointage, 0, Qt.AlignHCenter)

        self.verticalSpacerPointage_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacerPointage_2)

        self.labelGuideInscript = QLabel(self.PagePointage)
        self.labelGuideInscript.setObjectName(u"labelGuideInscript")

        self.verticalLayout_2.addWidget(self.labelGuideInscript)

        self.stackedWidgetPages.addWidget(self.PagePointage)
        self.PageInscription = QWidget()
        self.PageInscription.setObjectName(u"PageInscription")
        self.verticalLayout = QVBoxLayout(self.PageInscription)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.PageNameInscritpion = QFrame(self.PageInscription)
        self.PageNameInscritpion.setObjectName(u"PageNameInscritpion")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.PageNameInscritpion.sizePolicy().hasHeightForWidth())
        self.PageNameInscritpion.setSizePolicy(sizePolicy5)
        self.PageNameInscritpion.setFrameShape(QFrame.StyledPanel)
        self.PageNameInscritpion.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.PageNameInscritpion)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.labelInscription = QLabel(self.PageNameInscritpion)
        self.labelInscription.setObjectName(u"labelInscription")

        self.horizontalLayout_5.addWidget(self.labelInscription)


        self.verticalLayout.addWidget(self.PageNameInscritpion, 0, Qt.AlignTop)

        self.frameInsc = QFrame(self.PageInscription)
        self.frameInsc.setObjectName(u"frameInsc")
        sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.frameInsc.sizePolicy().hasHeightForWidth())
        self.frameInsc.setSizePolicy(sizePolicy6)
        self.frameInsc.setFrameShape(QFrame.StyledPanel)
        self.frameInsc.setFrameShadow(QFrame.Raised)
        self.formLayout_2 = QFormLayout(self.frameInsc)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.LabelNomJeune = QLabel(self.frameInsc)
        self.LabelNomJeune.setObjectName(u"LabelNomJeune")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.LabelNomJeune)

        self.lineEditNomJeune = QLineEdit(self.frameInsc)
        self.lineEditNomJeune.setObjectName(u"lineEditNomJeune")
        sizePolicy5.setHeightForWidth(self.lineEditNomJeune.sizePolicy().hasHeightForWidth())
        self.lineEditNomJeune.setSizePolicy(sizePolicy5)

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.lineEditNomJeune)

        self.labelPrenomJeune = QLabel(self.frameInsc)
        self.labelPrenomJeune.setObjectName(u"labelPrenomJeune")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.labelPrenomJeune)

        self.lineEditPrenomJeune = QLineEdit(self.frameInsc)
        self.lineEditPrenomJeune.setObjectName(u"lineEditPrenomJeune")
        sizePolicy5.setHeightForWidth(self.lineEditPrenomJeune.sizePolicy().hasHeightForWidth())
        self.lineEditPrenomJeune.setSizePolicy(sizePolicy5)

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.lineEditPrenomJeune)

        self.LabelDateNais = QLabel(self.frameInsc)
        self.LabelDateNais.setObjectName(u"LabelDateNais")

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.LabelDateNais)

        self.dateEditNaissance = QDateEdit(self.frameInsc)
        self.dateEditNaissance.setObjectName(u"dateEditNaissance")
        sizePolicy.setHeightForWidth(self.dateEditNaissance.sizePolicy().hasHeightForWidth())
        self.dateEditNaissance.setSizePolicy(sizePolicy)
        self.dateEditNaissance.setWrapping(False)
        self.dateEditNaissance.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.dateEditNaissance.setCalendarPopup(False)

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.dateEditNaissance)

        self.labelGenre = QLabel(self.frameInsc)
        self.labelGenre.setObjectName(u"labelGenre")

        self.formLayout_2.setWidget(4, QFormLayout.LabelRole, self.labelGenre)

        self.comboBoxGenre = QComboBox(self.frameInsc)
        self.comboBoxGenre.addItem("")
        self.comboBoxGenre.addItem("")
        self.comboBoxGenre.addItem("")
        self.comboBoxGenre.setObjectName(u"comboBoxGenre")
        sizePolicy.setHeightForWidth(self.comboBoxGenre.sizePolicy().hasHeightForWidth())
        self.comboBoxGenre.setSizePolicy(sizePolicy)
        self.comboBoxGenre.setInsertPolicy(QComboBox.NoInsert)

        self.formLayout_2.setWidget(4, QFormLayout.FieldRole, self.comboBoxGenre)

        self.labelNomParent = QLabel(self.frameInsc)
        self.labelNomParent.setObjectName(u"labelNomParent")

        self.formLayout_2.setWidget(5, QFormLayout.LabelRole, self.labelNomParent)

        self.lineEditNomParent = QLineEdit(self.frameInsc)
        self.lineEditNomParent.setObjectName(u"lineEditNomParent")
        sizePolicy5.setHeightForWidth(self.lineEditNomParent.sizePolicy().hasHeightForWidth())
        self.lineEditNomParent.setSizePolicy(sizePolicy5)

        self.formLayout_2.setWidget(5, QFormLayout.FieldRole, self.lineEditNomParent)

        self.labelPrenomParent = QLabel(self.frameInsc)
        self.labelPrenomParent.setObjectName(u"labelPrenomParent")

        self.formLayout_2.setWidget(6, QFormLayout.LabelRole, self.labelPrenomParent)

        self.lineEditPrenomParent = QLineEdit(self.frameInsc)
        self.lineEditPrenomParent.setObjectName(u"lineEditPrenomParent")
        sizePolicy5.setHeightForWidth(self.lineEditPrenomParent.sizePolicy().hasHeightForWidth())
        self.lineEditPrenomParent.setSizePolicy(sizePolicy5)

        self.formLayout_2.setWidget(6, QFormLayout.FieldRole, self.lineEditPrenomParent)

        self.labelNumParent = QLabel(self.frameInsc)
        self.labelNumParent.setObjectName(u"labelNumParent")

        self.formLayout_2.setWidget(7, QFormLayout.LabelRole, self.labelNumParent)

        self.lineEditNumParent = QLineEdit(self.frameInsc)
        self.lineEditNumParent.setObjectName(u"lineEditNumParent")
        sizePolicy5.setHeightForWidth(self.lineEditNumParent.sizePolicy().hasHeightForWidth())
        self.lineEditNumParent.setSizePolicy(sizePolicy5)

        self.formLayout_2.setWidget(7, QFormLayout.FieldRole, self.lineEditNumParent)

        self.labelCommune = QLabel(self.frameInsc)
        self.labelCommune.setObjectName(u"labelCommune")

        self.formLayout_2.setWidget(8, QFormLayout.LabelRole, self.labelCommune)

        self.comboBoxCommune = QComboBox(self.frameInsc)
        self.comboBoxCommune.setObjectName(u"comboBoxCommune")
        sizePolicy5.setHeightForWidth(self.comboBoxCommune.sizePolicy().hasHeightForWidth())
        self.comboBoxCommune.setSizePolicy(sizePolicy5)
        self.comboBoxCommune.setEditable(True)
        self.comboBoxCommune.setInsertPolicy(QComboBox.NoInsert)
        self.comboBoxCommune.setFrame(True)
        self.comboBoxCommune.setModelColumn(0)

        self.formLayout_2.setWidget(8, QFormLayout.FieldRole, self.comboBoxCommune)

        self.labelEtabScol = QLabel(self.frameInsc)
        self.labelEtabScol.setObjectName(u"labelEtabScol")

        self.formLayout_2.setWidget(9, QFormLayout.LabelRole, self.labelEtabScol)

        self.comboBoxEtabScol = QComboBox(self.frameInsc)
        self.comboBoxEtabScol.addItem("")
        self.comboBoxEtabScol.addItem("")
        self.comboBoxEtabScol.addItem("")
        self.comboBoxEtabScol.addItem("")
        self.comboBoxEtabScol.addItem("")
        self.comboBoxEtabScol.addItem("")
        self.comboBoxEtabScol.addItem("")
        self.comboBoxEtabScol.addItem("")
        self.comboBoxEtabScol.addItem("")
        self.comboBoxEtabScol.addItem("")
        self.comboBoxEtabScol.addItem("")
        self.comboBoxEtabScol.addItem("")
        self.comboBoxEtabScol.addItem("")
        self.comboBoxEtabScol.addItem("")
        self.comboBoxEtabScol.setObjectName(u"comboBoxEtabScol")
        sizePolicy5.setHeightForWidth(self.comboBoxEtabScol.sizePolicy().hasHeightForWidth())
        self.comboBoxEtabScol.setSizePolicy(sizePolicy5)
        self.comboBoxEtabScol.setEditable(True)
        self.comboBoxEtabScol.setMaxVisibleItems(8)
        self.comboBoxEtabScol.setInsertPolicy(QComboBox.NoInsert)

        self.formLayout_2.setWidget(9, QFormLayout.FieldRole, self.comboBoxEtabScol)

        self.labelRegSoc = QLabel(self.frameInsc)
        self.labelRegSoc.setObjectName(u"labelRegSoc")

        self.formLayout_2.setWidget(10, QFormLayout.LabelRole, self.labelRegSoc)

        self.comboBoxRegSoc = QComboBox(self.frameInsc)
        self.comboBoxRegSoc.addItem("")
        self.comboBoxRegSoc.addItem("")
        self.comboBoxRegSoc.addItem("")
        self.comboBoxRegSoc.setObjectName(u"comboBoxRegSoc")
        sizePolicy.setHeightForWidth(self.comboBoxRegSoc.sizePolicy().hasHeightForWidth())
        self.comboBoxRegSoc.setSizePolicy(sizePolicy)
        self.comboBoxRegSoc.setInsertPolicy(QComboBox.NoInsert)

        self.formLayout_2.setWidget(10, QFormLayout.FieldRole, self.comboBoxRegSoc)


        self.verticalLayout.addWidget(self.frameInsc)

        self.frameBtnInscr = QFrame(self.PageInscription)
        self.frameBtnInscr.setObjectName(u"frameBtnInscr")
        self.frameBtnInscr.setMinimumSize(QSize(0, 0))
        self.frameBtnInscr.setFrameShape(QFrame.StyledPanel)
        self.frameBtnInscr.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frameBtnInscr)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.pushButtonValiderInscr = QPushButton(self.frameBtnInscr)
        self.pushButtonValiderInscr.setObjectName(u"pushButtonValiderInscr")

        self.horizontalLayout_6.addWidget(self.pushButtonValiderInscr)

        self.pushButtonAnnulerInsc = QPushButton(self.frameBtnInscr)
        self.pushButtonAnnulerInsc.setObjectName(u"pushButtonAnnulerInsc")

        self.horizontalLayout_6.addWidget(self.pushButtonAnnulerInsc)


        self.verticalLayout.addWidget(self.frameBtnInscr)

        self.stackedWidgetPages.addWidget(self.PageInscription)
        self.PageModification = QWidget()
        self.PageModification.setObjectName(u"PageModification")
        self.verticalLayout_17 = QVBoxLayout(self.PageModification)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.frameTitreModif = QFrame(self.PageModification)
        self.frameTitreModif.setObjectName(u"frameTitreModif")
        self.frameTitreModif.setMaximumSize(QSize(16777215, 50))
        self.frameTitreModif.setFrameShape(QFrame.StyledPanel)
        self.frameTitreModif.setFrameShadow(QFrame.Raised)
        self.frameTitreModif.setLineWidth(1)
        self.verticalLayout_18 = QVBoxLayout(self.frameTitreModif)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.labelTitreModif = QLabel(self.frameTitreModif)
        self.labelTitreModif.setObjectName(u"labelTitreModif")

        self.verticalLayout_18.addWidget(self.labelTitreModif, 0, Qt.AlignHCenter)


        self.verticalLayout_17.addWidget(self.frameTitreModif)

        self.frameSelJeune = QFrame(self.PageModification)
        self.frameSelJeune.setObjectName(u"frameSelJeune")
        self.frameSelJeune.setFrameShape(QFrame.StyledPanel)
        self.frameSelJeune.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frameSelJeune)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.labelSelJeune = QLabel(self.frameSelJeune)
        self.labelSelJeune.setObjectName(u"labelSelJeune")
        sizePolicy7 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.labelSelJeune.sizePolicy().hasHeightForWidth())
        self.labelSelJeune.setSizePolicy(sizePolicy7)

        self.horizontalLayout_7.addWidget(self.labelSelJeune)

        self.comboBoxModifSelJeune = QComboBox(self.frameSelJeune)
        self.comboBoxModifSelJeune.setObjectName(u"comboBoxModifSelJeune")
        sizePolicy8 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.comboBoxModifSelJeune.sizePolicy().hasHeightForWidth())
        self.comboBoxModifSelJeune.setSizePolicy(sizePolicy8)
        self.comboBoxModifSelJeune.setEditable(True)
        self.comboBoxModifSelJeune.setInsertPolicy(QComboBox.NoInsert)

        self.horizontalLayout_7.addWidget(self.comboBoxModifSelJeune)

        self.pushButtonModifSelJeune = QPushButton(self.frameSelJeune)
        self.pushButtonModifSelJeune.setObjectName(u"pushButtonModifSelJeune")
        sizePolicy9 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.pushButtonModifSelJeune.sizePolicy().hasHeightForWidth())
        self.pushButtonModifSelJeune.setSizePolicy(sizePolicy9)

        self.horizontalLayout_7.addWidget(self.pushButtonModifSelJeune)


        self.verticalLayout_17.addWidget(self.frameSelJeune)

        self.frameModifiaction = QFrame(self.PageModification)
        self.frameModifiaction.setObjectName(u"frameModifiaction")
        sizePolicy6.setHeightForWidth(self.frameModifiaction.sizePolicy().hasHeightForWidth())
        self.frameModifiaction.setSizePolicy(sizePolicy6)
        self.frameModifiaction.setFrameShape(QFrame.StyledPanel)
        self.frameModifiaction.setFrameShadow(QFrame.Raised)
        self.formLayout = QFormLayout(self.frameModifiaction)
        self.formLayout.setObjectName(u"formLayout")
        self.labelModifNom = QLabel(self.frameModifiaction)
        self.labelModifNom.setObjectName(u"labelModifNom")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.labelModifNom)

        self.labelModifPrenom = QLabel(self.frameModifiaction)
        self.labelModifPrenom.setObjectName(u"labelModifPrenom")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.labelModifPrenom)

        self.labelModifEtab = QLabel(self.frameModifiaction)
        self.labelModifEtab.setObjectName(u"labelModifEtab")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.labelModifEtab)

        self.labelModifDateNaiss = QLabel(self.frameModifiaction)
        self.labelModifDateNaiss.setObjectName(u"labelModifDateNaiss")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.labelModifDateNaiss)

        self.lineEditModifNom = QLineEdit(self.frameModifiaction)
        self.lineEditModifNom.setObjectName(u"lineEditModifNom")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEditModifNom)

        self.lineEditModifPrenom = QLineEdit(self.frameModifiaction)
        self.lineEditModifPrenom.setObjectName(u"lineEditModifPrenom")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lineEditModifPrenom)

        self.dateEditModifDateNaiss = QDateEdit(self.frameModifiaction)
        self.dateEditModifDateNaiss.setObjectName(u"dateEditModifDateNaiss")
        self.dateEditModifDateNaiss.setButtonSymbols(QAbstractSpinBox.NoButtons)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.dateEditModifDateNaiss)

        self.labelModifRegSoc = QLabel(self.frameModifiaction)
        self.labelModifRegSoc.setObjectName(u"labelModifRegSoc")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.labelModifRegSoc)

        self.comboBoxModifRegSoc = QComboBox(self.frameModifiaction)
        self.comboBoxModifRegSoc.addItem("")
        self.comboBoxModifRegSoc.addItem("")
        self.comboBoxModifRegSoc.addItem("")
        self.comboBoxModifRegSoc.setObjectName(u"comboBoxModifRegSoc")
        sizePolicy2.setHeightForWidth(self.comboBoxModifRegSoc.sizePolicy().hasHeightForWidth())
        self.comboBoxModifRegSoc.setSizePolicy(sizePolicy2)

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.comboBoxModifRegSoc)

        self.labelModifGenre = QLabel(self.frameModifiaction)
        self.labelModifGenre.setObjectName(u"labelModifGenre")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.labelModifGenre)

        self.comboBoxModifGenre = QComboBox(self.frameModifiaction)
        self.comboBoxModifGenre.addItem("")
        self.comboBoxModifGenre.addItem("")
        self.comboBoxModifGenre.addItem("")
        self.comboBoxModifGenre.setObjectName(u"comboBoxModifGenre")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.comboBoxModifGenre)

        self.labelModifNumTuteur = QLabel(self.frameModifiaction)
        self.labelModifNumTuteur.setObjectName(u"labelModifNumTuteur")

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.labelModifNumTuteur)

        self.lineEditModifNumTuteur = QLineEdit(self.frameModifiaction)
        self.lineEditModifNumTuteur.setObjectName(u"lineEditModifNumTuteur")

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.lineEditModifNumTuteur)

        self.labelModifComm = QLabel(self.frameModifiaction)
        self.labelModifComm.setObjectName(u"labelModifComm")

        self.formLayout.setWidget(9, QFormLayout.LabelRole, self.labelModifComm)

        self.comboBoxModifCom = QComboBox(self.frameModifiaction)
        self.comboBoxModifCom.setObjectName(u"comboBoxModifCom")
        sizePolicy10 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.comboBoxModifCom.sizePolicy().hasHeightForWidth())
        self.comboBoxModifCom.setSizePolicy(sizePolicy10)
        self.comboBoxModifCom.setEditable(True)

        self.formLayout.setWidget(9, QFormLayout.FieldRole, self.comboBoxModifCom)

        self.labelModifNomTuteur = QLabel(self.frameModifiaction)
        self.labelModifNomTuteur.setObjectName(u"labelModifNomTuteur")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.labelModifNomTuteur)

        self.labelModifPrenomTuteur = QLabel(self.frameModifiaction)
        self.labelModifPrenomTuteur.setObjectName(u"labelModifPrenomTuteur")

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.labelModifPrenomTuteur)

        self.lineEditModifNomTuteur = QLineEdit(self.frameModifiaction)
        self.lineEditModifNomTuteur.setObjectName(u"lineEditModifNomTuteur")

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.lineEditModifNomTuteur)

        self.lineEditModifPrenomTuteur = QLineEdit(self.frameModifiaction)
        self.lineEditModifPrenomTuteur.setObjectName(u"lineEditModifPrenomTuteur")

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.lineEditModifPrenomTuteur)

        self.comboBoxModifEtabScol = QComboBox(self.frameModifiaction)
        self.comboBoxModifEtabScol.addItem("")
        self.comboBoxModifEtabScol.addItem("")
        self.comboBoxModifEtabScol.addItem("")
        self.comboBoxModifEtabScol.addItem("")
        self.comboBoxModifEtabScol.addItem("")
        self.comboBoxModifEtabScol.addItem("")
        self.comboBoxModifEtabScol.addItem("")
        self.comboBoxModifEtabScol.addItem("")
        self.comboBoxModifEtabScol.addItem("")
        self.comboBoxModifEtabScol.addItem("")
        self.comboBoxModifEtabScol.addItem("")
        self.comboBoxModifEtabScol.addItem("")
        self.comboBoxModifEtabScol.addItem("")
        self.comboBoxModifEtabScol.addItem("")
        self.comboBoxModifEtabScol.setObjectName(u"comboBoxModifEtabScol")
        sizePolicy5.setHeightForWidth(self.comboBoxModifEtabScol.sizePolicy().hasHeightForWidth())
        self.comboBoxModifEtabScol.setSizePolicy(sizePolicy5)
        self.comboBoxModifEtabScol.setEditable(True)
        self.comboBoxModifEtabScol.setInsertPolicy(QComboBox.NoInsert)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.comboBoxModifEtabScol)


        self.verticalLayout_17.addWidget(self.frameModifiaction)

        self.pushButtonModifAppliquer = QPushButton(self.PageModification)
        self.pushButtonModifAppliquer.setObjectName(u"pushButtonModifAppliquer")

        self.verticalLayout_17.addWidget(self.pushButtonModifAppliquer)

        self.stackedWidgetPages.addWidget(self.PageModification)
        self.PageTotaux = QWidget()
        self.PageTotaux.setObjectName(u"PageTotaux")
        self.verticalLayout_13 = QVBoxLayout(self.PageTotaux)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.frameTitreTotal = QFrame(self.PageTotaux)
        self.frameTitreTotal.setObjectName(u"frameTitreTotal")
        self.frameTitreTotal.setMinimumSize(QSize(0, 0))
        self.frameTitreTotal.setMaximumSize(QSize(16777215, 50))
        self.frameTitreTotal.setFrameShape(QFrame.StyledPanel)
        self.frameTitreTotal.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frameTitreTotal)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.labelTitreTotal = QLabel(self.frameTitreTotal)
        self.labelTitreTotal.setObjectName(u"labelTitreTotal")

        self.horizontalLayout_2.addWidget(self.labelTitreTotal, 0, Qt.AlignHCenter)


        self.verticalLayout_13.addWidget(self.frameTitreTotal)

        self.widgetSelDates = QWidget(self.PageTotaux)
        self.widgetSelDates.setObjectName(u"widgetSelDates")
        sizePolicy.setHeightForWidth(self.widgetSelDates.sizePolicy().hasHeightForWidth())
        self.widgetSelDates.setSizePolicy(sizePolicy)
        self.widgetSelDates.setMinimumSize(QSize(0, 0))
        self.gridLayout = QGridLayout(self.widgetSelDates)
        self.gridLayout.setSpacing(10)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(6, 10, -1, 10)
        self.dateEditFin = QDateEdit(self.widgetSelDates)
        self.dateEditFin.setObjectName(u"dateEditFin")
        self.dateEditFin.setLocale(QLocale(QLocale.French, QLocale.France))
        self.dateEditFin.setCalendarPopup(True)
        self.dateEditFin.setDate(QDate(2022, 8, 19))

        self.gridLayout.addWidget(self.dateEditFin, 3, 1, 1, 1)

        self.dateEditDebut = QDateEdit(self.widgetSelDates)
        self.dateEditDebut.setObjectName(u"dateEditDebut")
        sizePolicy11 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy11.setHorizontalStretch(0)
        sizePolicy11.setVerticalStretch(0)
        sizePolicy11.setHeightForWidth(self.dateEditDebut.sizePolicy().hasHeightForWidth())
        self.dateEditDebut.setSizePolicy(sizePolicy11)
        self.dateEditDebut.setLocale(QLocale(QLocale.French, QLocale.France))
        self.dateEditDebut.setCalendarPopup(True)
        self.dateEditDebut.setDate(QDate(2022, 8, 19))

        self.gridLayout.addWidget(self.dateEditDebut, 3, 0, 1, 1)

        self.labelDateFin = QLabel(self.widgetSelDates)
        self.labelDateFin.setObjectName(u"labelDateFin")

        self.gridLayout.addWidget(self.labelDateFin, 1, 1, 1, 1)

        self.labelDateDebut = QLabel(self.widgetSelDates)
        self.labelDateDebut.setObjectName(u"labelDateDebut")

        self.gridLayout.addWidget(self.labelDateDebut, 1, 0, 1, 1)


        self.verticalLayout_13.addWidget(self.widgetSelDates, 0, Qt.AlignVCenter)

        self.pushButtonCalculerTotal = QPushButton(self.PageTotaux)
        self.pushButtonCalculerTotal.setObjectName(u"pushButtonCalculerTotal")

        self.verticalLayout_13.addWidget(self.pushButtonCalculerTotal)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_13.addItem(self.verticalSpacer)

        self.textBrowserTotal = QTextBrowser(self.PageTotaux)
        self.textBrowserTotal.setObjectName(u"textBrowserTotal")

        self.verticalLayout_13.addWidget(self.textBrowserTotal)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_13.addItem(self.verticalSpacer_2)

        self.labelCocheFiltres = QLabel(self.PageTotaux)
        self.labelCocheFiltres.setObjectName(u"labelCocheFiltres")
        sizePolicy.setHeightForWidth(self.labelCocheFiltres.sizePolicy().hasHeightForWidth())
        self.labelCocheFiltres.setSizePolicy(sizePolicy)

        self.verticalLayout_13.addWidget(self.labelCocheFiltres, 0, Qt.AlignBottom)

        self.widgetSelFiltres = QWidget(self.PageTotaux)
        self.widgetSelFiltres.setObjectName(u"widgetSelFiltres")
        sizePolicy.setHeightForWidth(self.widgetSelFiltres.sizePolicy().hasHeightForWidth())
        self.widgetSelFiltres.setSizePolicy(sizePolicy)
        self.widgetSelFiltres.setMinimumSize(QSize(0, 50))
        self.horizontalLayout = QHBoxLayout(self.widgetSelFiltres)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.checkBoxLundi = QCheckBox(self.widgetSelFiltres)
        self.checkBoxLundi.setObjectName(u"checkBoxLundi")
        sizePolicy.setHeightForWidth(self.checkBoxLundi.sizePolicy().hasHeightForWidth())
        self.checkBoxLundi.setSizePolicy(sizePolicy)
        self.checkBoxLundi.setChecked(True)

        self.horizontalLayout.addWidget(self.checkBoxLundi)

        self.checkBoxMardi = QCheckBox(self.widgetSelFiltres)
        self.checkBoxMardi.setObjectName(u"checkBoxMardi")
        sizePolicy.setHeightForWidth(self.checkBoxMardi.sizePolicy().hasHeightForWidth())
        self.checkBoxMardi.setSizePolicy(sizePolicy)
        self.checkBoxMardi.setChecked(True)

        self.horizontalLayout.addWidget(self.checkBoxMardi)

        self.checkBoxMercredi = QCheckBox(self.widgetSelFiltres)
        self.checkBoxMercredi.setObjectName(u"checkBoxMercredi")
        sizePolicy.setHeightForWidth(self.checkBoxMercredi.sizePolicy().hasHeightForWidth())
        self.checkBoxMercredi.setSizePolicy(sizePolicy)
        self.checkBoxMercredi.setChecked(True)

        self.horizontalLayout.addWidget(self.checkBoxMercredi)

        self.checkBoxJeudi = QCheckBox(self.widgetSelFiltres)
        self.checkBoxJeudi.setObjectName(u"checkBoxJeudi")
        sizePolicy.setHeightForWidth(self.checkBoxJeudi.sizePolicy().hasHeightForWidth())
        self.checkBoxJeudi.setSizePolicy(sizePolicy)
        self.checkBoxJeudi.setChecked(True)

        self.horizontalLayout.addWidget(self.checkBoxJeudi)

        self.checkBoxVendredi = QCheckBox(self.widgetSelFiltres)
        self.checkBoxVendredi.setObjectName(u"checkBoxVendredi")
        sizePolicy.setHeightForWidth(self.checkBoxVendredi.sizePolicy().hasHeightForWidth())
        self.checkBoxVendredi.setSizePolicy(sizePolicy)
        self.checkBoxVendredi.setChecked(True)

        self.horizontalLayout.addWidget(self.checkBoxVendredi)

        self.checkBoxSamedi = QCheckBox(self.widgetSelFiltres)
        self.checkBoxSamedi.setObjectName(u"checkBoxSamedi")
        sizePolicy.setHeightForWidth(self.checkBoxSamedi.sizePolicy().hasHeightForWidth())
        self.checkBoxSamedi.setSizePolicy(sizePolicy)
        self.checkBoxSamedi.setChecked(True)

        self.horizontalLayout.addWidget(self.checkBoxSamedi)

        self.checkBoxPeriodeVac = QCheckBox(self.widgetSelFiltres)
        self.checkBoxPeriodeVac.setObjectName(u"checkBoxPeriodeVac")
        sizePolicy.setHeightForWidth(self.checkBoxPeriodeVac.sizePolicy().hasHeightForWidth())
        self.checkBoxPeriodeVac.setSizePolicy(sizePolicy)
        self.checkBoxPeriodeVac.setChecked(True)

        self.horizontalLayout.addWidget(self.checkBoxPeriodeVac)


        self.verticalLayout_13.addWidget(self.widgetSelFiltres, 0, Qt.AlignTop)

        self.stackedWidgetPages.addWidget(self.PageTotaux)
        self.PageExtraction = QWidget()
        self.PageExtraction.setObjectName(u"PageExtraction")
        self.verticalLayout_5 = QVBoxLayout(self.PageExtraction)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frameExtraction = QFrame(self.PageExtraction)
        self.frameExtraction.setObjectName(u"frameExtraction")
        self.frameExtraction.setFrameShape(QFrame.StyledPanel)
        self.frameExtraction.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frameExtraction)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.labelExtraction = QLabel(self.frameExtraction)
        self.labelExtraction.setObjectName(u"labelExtraction")

        self.verticalLayout_6.addWidget(self.labelExtraction)


        self.verticalLayout_5.addWidget(self.frameExtraction)

        self.widgetExtraction = QWidget(self.PageExtraction)
        self.widgetExtraction.setObjectName(u"widgetExtraction")
        sizePolicy6.setHeightForWidth(self.widgetExtraction.sizePolicy().hasHeightForWidth())
        self.widgetExtraction.setSizePolicy(sizePolicy6)
        self.verticalLayout_7 = QVBoxLayout(self.widgetExtraction)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(50, -1, 50, -1)
        self.pushButtonInfosJeunes = QPushButton(self.widgetExtraction)
        self.pushButtonInfosJeunes.setObjectName(u"pushButtonInfosJeunes")

        self.verticalLayout_7.addWidget(self.pushButtonInfosJeunes)

        self.pushButtonDataPointage = QPushButton(self.widgetExtraction)
        self.pushButtonDataPointage.setObjectName(u"pushButtonDataPointage")

        self.verticalLayout_7.addWidget(self.pushButtonDataPointage)

        self.tableView = QTableView(self.widgetExtraction)
        self.tableView.setObjectName(u"tableView")

        self.verticalLayout_7.addWidget(self.tableView)


        self.verticalLayout_5.addWidget(self.widgetExtraction)

        self.stackedWidgetPages.addWidget(self.PageExtraction)

        self.horizontalLayout_4.addWidget(self.stackedWidgetPages)


        self.verticalLayout_16.addWidget(self.SideMenu)

        MainWindow.setCentralWidget(self.centralwidgetMain)
        QWidget.setTabOrder(self.PB_Pointage, self.PB_Inscription)
        QWidget.setTabOrder(self.PB_Inscription, self.PB_Modif)
        QWidget.setTabOrder(self.PB_Modif, self.PB_Totaux)
        QWidget.setTabOrder(self.PB_Totaux, self.PB_Extraction)
        QWidget.setTabOrder(self.PB_Extraction, self.comboBoxEntreePointage)
        QWidget.setTabOrder(self.comboBoxEntreePointage, self.pushButtonValiderPointage)

        self.retranslateUi(MainWindow)
        self.pushButtonAnnulerInsc.clicked.connect(self.lineEditNumParent.clear)
        self.pushButtonAnnulerInsc.clicked.connect(self.lineEditPrenomParent.clear)
        self.pushButtonAnnulerInsc.clicked.connect(self.lineEditNomParent.clear)
        self.pushButtonAnnulerInsc.clicked.connect(self.lineEditPrenomJeune.clear)
        self.pushButtonAnnulerInsc.clicked.connect(self.lineEditNomJeune.clear)
        self.pushButtonAnnulerInsc.clicked.connect(self.comboBoxEtabScol.clear)
        self.pushButtonAnnulerInsc.clicked.connect(self.comboBoxRegSoc.clear)
        self.pushButtonAnnulerInsc.clicked.connect(self.comboBoxCommune.clear)

        self.stackedWidgetPages.setCurrentIndex(1)
        self.comboBoxEtabScol.setCurrentIndex(0)
        self.comboBoxModifEtabScol.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.labelBienvenue.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">BIENVENUE AU PAJ</span></p></body></html>", None))
        self.PB_Pointage.setText(QCoreApplication.translate("MainWindow", u"Pointage", None))
        self.PB_Inscription.setText(QCoreApplication.translate("MainWindow", u"Inscription", None))
        self.PB_Modif.setText(QCoreApplication.translate("MainWindow", u"Modification", None))
        self.PB_Totaux.setText(QCoreApplication.translate("MainWindow", u"Totaux", None))
        self.PB_Extraction.setText(QCoreApplication.translate("MainWindow", u"Extraction", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:700;\">POINTAGE</span></p></body></html>", None))
        self.labelEntreNom.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Entre ton nom pour te pointer:</span></p></body></html>", None))
        self.comboBoxEntreePointage.setCurrentText("")
        self.pushButtonValiderPointage.setText(QCoreApplication.translate("MainWindow", u"Valider", None))
        self.labelGuideInscript.setText(QCoreApplication.translate("MainWindow", u"Pas encore inscrit? Clique sur \"Inscription\"", None))
        self.labelInscription.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">INSCRIPTION</span></p></body></html>", None))
        self.LabelNomJeune.setText(QCoreApplication.translate("MainWindow", u"Nom", None))
        self.lineEditNomJeune.setText("")
        self.labelPrenomJeune.setText(QCoreApplication.translate("MainWindow", u"Pr\u00e9nom", None))
        self.lineEditPrenomJeune.setText("")
        self.LabelDateNais.setText(QCoreApplication.translate("MainWindow", u"Date de naissance", None))
        self.labelGenre.setText(QCoreApplication.translate("MainWindow", u"Genre", None))
        self.comboBoxGenre.setItemText(0, QCoreApplication.translate("MainWindow", u"Fille", None))
        self.comboBoxGenre.setItemText(1, QCoreApplication.translate("MainWindow", u"Gar\u00e7on", None))
        self.comboBoxGenre.setItemText(2, QCoreApplication.translate("MainWindow", u"Non-binaire", None))

        self.labelNomParent.setText(QCoreApplication.translate("MainWindow", u"Nom Tuteur/Parent", None))
        self.lineEditNomParent.setText("")
        self.labelPrenomParent.setText(QCoreApplication.translate("MainWindow", u"Pr\u00e9nom Tuteur/Parent", None))
        self.lineEditPrenomParent.setText("")
        self.labelNumParent.setText(QCoreApplication.translate("MainWindow", u"Num\u00e9ro Tuteur/Parent", None))
        self.labelCommune.setText(QCoreApplication.translate("MainWindow", u"Commune de r\u00e9sidence", None))
        self.labelEtabScol.setText(QCoreApplication.translate("MainWindow", u"Etablissement scolaire", None))
        self.comboBoxEtabScol.setItemText(0, QCoreApplication.translate("MainWindow", u"Lyc\u00e9e Pesquet", None))
        self.comboBoxEtabScol.setItemText(1, QCoreApplication.translate("MainWindow", u"Autre", None))
        self.comboBoxEtabScol.setItemText(2, QCoreApplication.translate("MainWindow", u"Aucun", None))
        self.comboBoxEtabScol.setItemText(3, QCoreApplication.translate("MainWindow", u"Lyc\u00e9e Nature", None))
        self.comboBoxEtabScol.setItemText(4, QCoreApplication.translate("MainWindow", u"Lyc\u00e9e Lebrun", None))
        self.comboBoxEtabScol.setItemText(5, QCoreApplication.translate("MainWindow", u"Lyc\u00e9e JPII", None))
        self.comboBoxEtabScol.setItemText(6, QCoreApplication.translate("MainWindow", u"Coll\u00e8ge Pr\u00e9vert", None))
        self.comboBoxEtabScol.setItemText(7, QCoreApplication.translate("MainWindow", u"Coll\u00e8ge JPII", None))
        self.comboBoxEtabScol.setItemText(8, QCoreApplication.translate("MainWindow", u"Coll\u00e8ge de Cerisy la salle", None))
        self.comboBoxEtabScol.setItemText(9, QCoreApplication.translate("MainWindow", u"Coll\u00e8ge de Gavray", None))
        self.comboBoxEtabScol.setItemText(10, QCoreApplication.translate("MainWindow", u"Coll\u00e8ge de Montmartin sur mer", None))
        self.comboBoxEtabScol.setItemText(11, QCoreApplication.translate("MainWindow", u"Coll\u00e8ge de St-Sauveur Villages", None))
        self.comboBoxEtabScol.setItemText(12, QCoreApplication.translate("MainWindow", u"Coll\u00e8ge d'Agon-Coutainville", None))
        self.comboBoxEtabScol.setItemText(13, QCoreApplication.translate("MainWindow", u"MFR de St-Sauveur Lendelain", None))

        self.labelRegSoc.setText(QCoreApplication.translate("MainWindow", u"R\u00e9gime social", None))
        self.comboBoxRegSoc.setItemText(0, QCoreApplication.translate("MainWindow", u"CAF", None))
        self.comboBoxRegSoc.setItemText(1, QCoreApplication.translate("MainWindow", u"MSA", None))
        self.comboBoxRegSoc.setItemText(2, QCoreApplication.translate("MainWindow", u"AUTRE", None))

        self.pushButtonValiderInscr.setText(QCoreApplication.translate("MainWindow", u"Valider", None))
        self.pushButtonAnnulerInsc.setText(QCoreApplication.translate("MainWindow", u"Annuler", None))
        self.labelTitreModif.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">MODIFICATION</span></p></body></html>", None))
        self.labelSelJeune.setText(QCoreApplication.translate("MainWindow", u"Selectionner le nom du jeune", None))
        self.pushButtonModifSelJeune.setText(QCoreApplication.translate("MainWindow", u"Valider", None))
        self.labelModifNom.setText(QCoreApplication.translate("MainWindow", u"Nom", None))
        self.labelModifPrenom.setText(QCoreApplication.translate("MainWindow", u"Prenom", None))
        self.labelModifEtab.setText(QCoreApplication.translate("MainWindow", u"Etablissement scolaire", None))
        self.labelModifDateNaiss.setText(QCoreApplication.translate("MainWindow", u"Date de naissance", None))
        self.labelModifRegSoc.setText(QCoreApplication.translate("MainWindow", u"R\u00e9gime Social", None))
        self.comboBoxModifRegSoc.setItemText(0, QCoreApplication.translate("MainWindow", u"CAF", None))
        self.comboBoxModifRegSoc.setItemText(1, QCoreApplication.translate("MainWindow", u"MSA", None))
        self.comboBoxModifRegSoc.setItemText(2, QCoreApplication.translate("MainWindow", u"AUTRE", None))

        self.labelModifGenre.setText(QCoreApplication.translate("MainWindow", u"Genre", None))
        self.comboBoxModifGenre.setItemText(0, QCoreApplication.translate("MainWindow", u"Gar\u00e7on", None))
        self.comboBoxModifGenre.setItemText(1, QCoreApplication.translate("MainWindow", u"Fille", None))
        self.comboBoxModifGenre.setItemText(2, QCoreApplication.translate("MainWindow", u"Non-binaire", None))

        self.labelModifNumTuteur.setText(QCoreApplication.translate("MainWindow", u"Num\u00e9ro tuteur/parent", None))
        self.labelModifComm.setText(QCoreApplication.translate("MainWindow", u"Commune", None))
        self.labelModifNomTuteur.setText(QCoreApplication.translate("MainWindow", u"Nom tuteur/parent", None))
        self.labelModifPrenomTuteur.setText(QCoreApplication.translate("MainWindow", u"Prenom tuteur/parent", None))
        self.comboBoxModifEtabScol.setItemText(0, QCoreApplication.translate("MainWindow", u"Lyc\u00e9e Pesquet", None))
        self.comboBoxModifEtabScol.setItemText(1, QCoreApplication.translate("MainWindow", u"Autre", None))
        self.comboBoxModifEtabScol.setItemText(2, QCoreApplication.translate("MainWindow", u"Aucun", None))
        self.comboBoxModifEtabScol.setItemText(3, QCoreApplication.translate("MainWindow", u"Lyc\u00e9e Nature", None))
        self.comboBoxModifEtabScol.setItemText(4, QCoreApplication.translate("MainWindow", u"Lyc\u00e9e Lebrun", None))
        self.comboBoxModifEtabScol.setItemText(5, QCoreApplication.translate("MainWindow", u"Lyc\u00e9e JPII", None))
        self.comboBoxModifEtabScol.setItemText(6, QCoreApplication.translate("MainWindow", u"Coll\u00e8ge Pr\u00e9vert", None))
        self.comboBoxModifEtabScol.setItemText(7, QCoreApplication.translate("MainWindow", u"Coll\u00e8ge JPII", None))
        self.comboBoxModifEtabScol.setItemText(8, QCoreApplication.translate("MainWindow", u"Coll\u00e8ge de Cerisy la salle", None))
        self.comboBoxModifEtabScol.setItemText(9, QCoreApplication.translate("MainWindow", u"Coll\u00e8ge de Gavray", None))
        self.comboBoxModifEtabScol.setItemText(10, QCoreApplication.translate("MainWindow", u"Coll\u00e8ge de Montmartin sur mer", None))
        self.comboBoxModifEtabScol.setItemText(11, QCoreApplication.translate("MainWindow", u"Coll\u00e8ge de St-Sauveur Villages", None))
        self.comboBoxModifEtabScol.setItemText(12, QCoreApplication.translate("MainWindow", u"Coll\u00e8ge d'Agon-Coutainville", None))
        self.comboBoxModifEtabScol.setItemText(13, QCoreApplication.translate("MainWindow", u"MFR de St-Sauveur Lendelain", None))

        self.pushButtonModifAppliquer.setText(QCoreApplication.translate("MainWindow", u"Appliquer les modifications", None))
        self.labelTitreTotal.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">CALCUL TOTAL</span></p></body></html>", None))
        self.labelDateFin.setText(QCoreApplication.translate("MainWindow", u"Jusqu'au:", None))
        self.labelDateDebut.setText(QCoreApplication.translate("MainWindow", u"Depuis le:", None))
        self.pushButtonCalculerTotal.setText(QCoreApplication.translate("MainWindow", u"Calculer", None))
        self.labelCocheFiltres.setText(QCoreApplication.translate("MainWindow", u"D\u00e9ocher les cases pour selectionner les jours:", None))
        self.checkBoxLundi.setText(QCoreApplication.translate("MainWindow", u"Lun", None))
        self.checkBoxMardi.setText(QCoreApplication.translate("MainWindow", u"Mar", None))
        self.checkBoxMercredi.setText(QCoreApplication.translate("MainWindow", u"Mer", None))
        self.checkBoxJeudi.setText(QCoreApplication.translate("MainWindow", u"Jeu", None))
        self.checkBoxVendredi.setText(QCoreApplication.translate("MainWindow", u"Ven", None))
        self.checkBoxSamedi.setText(QCoreApplication.translate("MainWindow", u"Sam", None))
        self.checkBoxPeriodeVac.setText(QCoreApplication.translate("MainWindow", u"Inclure periodes de vacances", None))
        self.labelExtraction.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">EXTRACTION</span></p></body></html>", None))
        self.pushButtonInfosJeunes.setText(QCoreApplication.translate("MainWindow", u"Informations jeunes", None))
        self.pushButtonDataPointage.setText(QCoreApplication.translate("MainWindow", u"Donn\u00e9es de pointage", None))
    # retranslateUi

