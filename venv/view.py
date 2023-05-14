import typing
from typing import List, Any

import datetime
import model
import gui_elements
from gui_elements.ui_main import Ui_MainWindow
from PySide6 import QtCore
from PySide6.QtGui import (QColor)
from PySide6.QtWidgets import *

"""Fonctions d'affichage et de recuperation des entrees de l'interface utilisateur"""
class View:

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
        """
        Outil pour mettre les infos entrees sur le jeune dans la page d'inscription dans un dictionnaire

        :return: Un dictionnaire contenant les infos sur le jeune
        """
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
            View.show_error_popup()
            return
        return infos

    def get_champs_modification(self) -> dict:
        """
        Outil pour mettre les infos entrees sur le jeune dans la page de modif dans un dictionnaire

        :return: Un dictionnaire contenant toutes les infos sur le jeune
        """
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
            View.show_error_popup()
            return
        return infos

    def update_modif(self, infos: dict):
        """
        Outil pour remplir les cases de la page de modification des infos des jeunes

        :param infos: Le dictionnaire contenant les infos sur le jeune
        :return: Rempli les cases du formulaire
        """
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

        num_parent = infos.get('Numéro_parent')
        self.ui.lineEditModifNumTuteur.setText(f"{num_parent:010}")
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
        """
        Methode d'affichage d'une fenetre d'erreur "pop_up"

        :param critical: Si l'erreur est critique, un pop-up d'erreur critique sera affiche (vrai par defaut)
        """
        msg = QMessageBox()
        msg.setWindowTitle("Information")
        msg.setText(model.Database.error_msg)
        if critical:
            msg.setWindowTitle("Erreur")
            msg.setIcon(QMessageBox.Critical)
        x = msg.exec()

    def show_total(self, total):
        """
        Change le texte de textBrowserTotal

        :param total: Le nombre a afficher
        """
        self.ui.textBrowserTotal.setText(f"Le total pour la periode est de: {total} jeunes pointés")

    def get_total_dates(self):
        debut = self.ui.dateEditDebut.date().getDate()
        fin = self.ui.dateEditFin.date().getDate()
        return debut, fin

    def get_total_filtres(self) -> dict:
        lun = self.ui.checkBoxLundi.isChecked()
        mar = self.ui.checkBoxMardi.isChecked()
        mer = self.ui.checkBoxMercredi.isChecked()
        jeu = self.ui.checkBoxJeudi.isChecked()
        ven = self.ui.checkBoxVendredi.isChecked()
        sam = self.ui.checkBoxSamedi.isChecked()
        is_periode_scol = self.ui.checkBoxPeriodeVac.isChecked()
        filtres = {'lundi': lun,
                   'mardi': mar,
                   'mercredi': mer,
                   'jeudi': jeu,
                   'vendredi': ven,
                   'samedi': sam,
                   'periode_scol': is_periode_scol}
        return filtres
