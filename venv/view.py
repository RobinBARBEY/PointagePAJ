import typing
from typing import List, Any

import datetime
import model
import gui_elements
from gui_elements.ui_main import Ui_MainWindow
from PySide2 import QtCore
from PySide2.QtGui import (QColor)
from PySide2.QtWidgets import *



class view:

    def __init__(self, ui):
        self.liste_jeunes: list[dict] = model.get_liste_jeunes()
        self.liste_communes = model.get_liste_communes()
        self.ui = ui
        # print("liste des jeunes:", self.liste_jeunes)
        # print("liste des communes:", self.liste_communes)
        for i in self.liste_jeunes:
            self.ui.comboBoxEntreePointage.addItem(f"{i.get('Nom_jeune')} {i.get('Prénom_jeune')}")
            self.ui.comboBoxModifSelJeune.addItem(f"{i.get('Nom_jeune')} {i.get('Prénom_jeune')}")
        for j in self.liste_communes:
            # print(j)
            self.ui.comboBoxCommune.addItem(f"{j.get('Nom_de_la_ville')}")
            self.ui.comboBoxModifCom.addItem(f"{j.get('Nom_de_la_ville')}")

        self.ui.comboBoxEntreePointage.setCurrentText("")
        self.ui.comboBoxModifSelJeune.setCurrentText("")

    def get_champs_inscription(self) -> dict:
        infos: dict = {'Nom_jeune': self.ui.lineEditNomJeune.text(),
                       'Prénom_jeune': self.ui.lineEditPrenomJeune.text(),
                       'Date_de_naissance': self.ui.dateEditNaissance.date().getDate(),
                       'Genre': self.ui.comboBoxGenre.currentText(),
                       'Nom_parent': self.ui.lineEditNomParent.text(),
                       'Prénom_parent': self.ui.lineEditPrenomParent.text(),
                       'Numéro_parent': self.ui.lineEditNumParent.text(),
                       'Nom_de_la_ville': self.ui.comboBoxCommune.currentText(),
                       'Nom_Etablissement': self.ui.comboBoxEtabScol.currentText(),
                       'Régime_social': self.ui.comboBoxRegSoc.currentText()
                       }

        # print(infos)
        if not model.infos_valides(infos):
            view.show_error_popup()
            return
        return infos

    def get_champs_modification(self) -> dict:
        Id_ville = model.query_one(f"SELECT Id_Ville FROM Ville "
                                   f"WHERE Nom_de_la_ville = '{self.ui.comboBoxModifCom.currentText()}'", False)[0]
        # print(Id_ville)

        infos: dict = {'Nom_jeune': self.ui.lineEditModifNom.text(),
                       'Prénom_jeune': self.ui.lineEditModifPrenom.text(),
                       'Date_de_naissance': self.ui.dateEditModifDateNaiss.date().getDate(),
                       'Genre': self.ui.comboBoxModifGenre.currentText(),
                       'Nom_parent': self.ui.lineEditModifNomTuteur.text(),
                       'Prénom_parent': self.ui.lineEditModifPrenomTuteur.text(),
                       'Numéro_parent': self.ui.lineEditModifNumTuteur.text(),
                       'Id_Ville': Id_ville,
                       'Nom_de_la_ville': self.ui.comboBoxModifCom.currentText(),
                       'Nom_Etablissement': self.ui.comboBoxModifEtabScol.currentText(),
                       'Régime_social': self.ui.comboBoxModifRegSoc.currentText()
                       }

        # print(infos)
        if not model.infos_valides(infos):
            view.show_error_popup()
            return
        return infos

    def update_modif(self, infos: dict):

        if not infos:
            show_error_popup("Infos vide")
            return

        self.ui.lineEditModifNom.setText(infos.get('Nom_jeune').upper().rstrip().lstrip())

        prenom_jeune: str = infos.get('Prénom_jeune').lstrip().rstrip()
        self.ui.lineEditModifPrenom.setText(prenom_jeune[0].upper() + prenom_jeune[1:].lower())

        date_naissance = QtCore.QDate(infos.get('Date_de_naissance'))
        self.ui.dateEditModifDateNaiss.setDate(date_naissance)

        # genre = infos[4]
        self.ui.comboBoxModifGenre.setCurrentText(infos.get('Genre'))

        # etab_scolaire = infos[5]
        self.ui.comboBoxModifEtabScol.setCurrentText(infos.get('Nom_Etablissement'))

        # regime_social = infos[8]
        self.ui.comboBoxModifRegSoc.setCurrentText(infos.get('Régime_social'))

        num_parent = str(infos.get('Numéro_parent'))
        self.ui.lineEditModifNumTuteur.setText(num_parent)
        infos_parent = model.query(f"SELECT Nom_parent, Prénom_parent FROM Tuteur_Parent "
                                   f"WHERE Numéro_parent = '{num_parent}'", False)

        # nom_parent = infos_parent[0][0]
        # print(infos_parent[0][0], infos_parent[0][1])
        self.ui.lineEditModifNomTuteur.setText(infos_parent[0][0])
        # prenom_parent = infos_parent[0][1]
        self.ui.lineEditModifPrenomTuteur.setText(infos_parent[0][1])

        commune = model.query_one(f"SELECT Nom_de_la_ville FROM Ville WHERE Id_Ville = '{infos.get('Id_Ville')}'")
        # print(commune, " -> Commune jeune modif, num:", infos.get('Id_Ville'))
        self.ui.comboBoxModifCom.setCurrentText(commune.get('Nom_de_la_ville'))

    @staticmethod
    def show_error_popup(critical=True):
        msg = QMessageBox()
        msg.setWindowTitle("Information")
        msg.setText(model.database.error_msg)
        if critical:
            msg.setWindowTitle("Erreur")
            msg.setIcon(QMessageBox.Critical)
        x = msg.exec_()

    def show_total(self, total):
        self.ui.textBrowserTotal.setText(f"Le total pour la periode est de: {total} jeunes pointés")

    def get_total_dates(self):
        debut = self.ui.dateEditDebut.date().getDate()
        fin = self.ui.dateEditFin.date().getDate()
        return debut, fin

    def get_total_filtres(self):
        lun = self.ui.checkBoxLundi.isChecked()
        mar = self.ui.checkBoxMardi.isChecked()
        mer = self.ui.checkBoxMercredi.isChecked()
        jeu = self.ui.checkBoxJeudi.isChecked()
        ven = self.ui.checkBoxVendredi.isChecked()
        sam = self.ui.checkBoxSamedi.isChecked()
        is_periode_scol = self.ui.checkBoxPeriodeVac.isChecked()
        return lun, mar, mer, jeu, ven, sam, is_periode_scol
