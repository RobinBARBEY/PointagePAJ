import datetime
import sys

from view import view
import controller
import model
from model import database

from PySide2 import QtCore
from PySide2.QtGui import QColor
from PySide2.QtWidgets import *

import gui_elements
# ==> MAIN WINDOW
from gui_elements.ui_main import Ui_MainWindow
# ==> SPLASH SCREEN
from gui_elements.ui_splash_screen import Ui_SplashScreen
from gui_elements.ui_login import Ui_Dialog

# ==> GLOBALS
counter = 0
NOM_LOGICIEL = "Pointage du PAJ des Unelles"
VERSION = "Version 1.0.0"


# MAIN APPLICATION
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self, None)
        model.create_tables()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle(f"{NOM_LOGICIEL} - {VERSION}")
        self.ui.dateEditAfficahgeDate.setDate(datetime.date.today())
        self.ui.dateEditDebut.setDate(datetime.date.today())
        self.ui.dateEditFin.setDate(datetime.date.today())

        # Creation de la vue pour modification des sorties sur l'UI
        self.view = view(self.ui)

        self.ui.stackedWidgetPages.setCurrentWidget(self.ui.PagePointage)

        # Stacked widget connection using Menu buttons
        self.ui.PB_Pointage.clicked.connect(lambda: self.ui.stackedWidgetPages.setCurrentWidget(self.ui.PagePointage))
        self.ui.PB_Inscription.clicked.connect(lambda: self.ui.stackedWidgetPages.setCurrentWidget(
            self.ui.PageInscription))
        self.ui.PB_Modif.clicked.connect(lambda: open_protected_page(self.ui.PageModification))
        self.ui.PB_Totaux.clicked.connect(lambda: open_protected_page(self.ui.PageTotaux))
        self.ui.PB_Extraction.clicked.connect(
            lambda: open_protected_page(self.ui.PageExtraction))

        # Validation des pointages lors d'un click sur valider dans la page pointage
        self.ui.pushButtonValiderPointage.clicked.connect(
            lambda: controller.valider_pointage(self.view, self.ui.comboBoxEntreePointage.currentText()))

        # Enregistrement de l'inscription lors d'un click sur valider inscription
        self.ui.pushButtonValiderInscr.clicked.connect(
            lambda: controller.valider_inscription(self.view, self.view.get_champs_inscription()))

        self.ui.pushButtonModifSelJeune.clicked.connect(
            lambda: controller.select_jeune_modif(self.view, self.ui.comboBoxModifSelJeune.currentText())
        )

        self.ui.pushButtonModifAppliquer.clicked.connect(
            lambda: controller.appliquer_modif(self.view.get_champs_modification()))

        self.ui.pushButtonCalculerTotal.clicked.connect(
            lambda: controller.calculTotal(self.view, self.view.get_total_dates(), self.view.get_total_filtres())
        )

        def open_protected_page(page):
            if not show_login():
                return
            match page:
                case self.ui.PageModification:
                    self.ui.stackedWidgetPages.setCurrentWidget(self.ui.PageModification)
                case self.ui.PageTotaux:
                    self.ui.stackedWidgetPages.setCurrentWidget(self.ui.PageTotaux)
                case self.ui.PageExtraction:
                    self.ui.stackedWidgetPages.setCurrentWidget(self.ui.PageExtraction)


# LOGIN AFTER SPLASH SCREEN
def show_login() -> bool:
    dialog = QDialog()
    qui = Ui_Dialog()
    qui.setupUi(dialog)
    dialog.setWindowTitle("Login")
    dialog.show()
    resp = dialog.exec_()

    database.animateur = qui.lineEditAnim.text()
    database.periode_scolaire = qui.checkBoxPeriodeScol.isChecked()
    database.pointages = model.liste_pointages_jour()
    if database.password != qui.lineEditMdp.text():
        return False
    elif resp == QDialog.rejected:
        return False
    return True


# SPLASH SCREEN
class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self, None)
        self.main = MainWindow()
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)

        # UI ==> INTERFACE CODES
        ########################################################################

        # REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # DROP SHADOW EFFECT
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.dropShadowFrame.setGraphicsEffect(self.shadow)

        # QTIMER ==> START
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        # TIMER IN MILLISECONDS
        self.timer.start(35)

        # Change Texts
        QtCore.QTimer.singleShot(1500, lambda: self.ui.label_description_2.setText("<strong>LOADING</strong> DATABASE"))
        QtCore.QTimer.singleShot(3000,
                                 lambda: self.ui.label_description_2.setText("<strong>LOADING</strong> USER INTERFACE"))

        # SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        # ==> END ##

    # ==> APP FUNCTIONS
    ########################################################################
    def progress(self):
        global counter
        logged = False
        self.ui.progressBar.setValue(counter)
        if counter > 100:
            self.timer.stop()
            tries = 0
            while not logged and tries < 3:
                tries += 1
                logged = show_login()
            if not logged:
                error_dialog = QErrorMessage()
                error_dialog.showMessage('Mauvais mot de passe à 3 reprises')
                error_dialog.setWindowTitle("Mdp erroné")
                error_dialog.exec_()
                self.close()
                return
            self.main.show()
            self.close()
        counter += 2


if __name__ == "__main__":
    app = QApplication()
    window = SplashScreen()
    sys.exit(app.exec_())
