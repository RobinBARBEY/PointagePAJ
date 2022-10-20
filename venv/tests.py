# import lots of packages
import random
from datetime import datetime

import mysql.connector

#imports des modules homemade
import inserts
import totaux
import date_functions
import model
from view import View
from gui_elements import *

import sys

from PySide2 import QtCore
from PySide2.QtGui import (QColor)
from PySide2.QtWidgets import *
from PySide6.QtUiTools import loadUiType

generated_class, base_class = loadUiType("gui_elements/main.ui")
# the values will be:
#  (<class '__main__.Ui_ThemeWidgetForm'>, <class 'PySide6.QtWidgets.QWidget'>)

widget = base_class()
form = generated_class()
form.setupUi(widget)
# form.a_widget_member.a_method_of_member()
widget.show()

# import gui_elements
# # ==> MAIN WINDOW
# from gui_elements.ui_main import Ui_MainWindow
# # ==> SPLASH SCREEN
# from gui_elements.ui_splash_screen import Ui_SplashScreen


# os.system('sudo -S systemctl start mysqld')
# os.system('sudo -S systemctl enable mysqld')
# from mysql.connector import CMySQLConnection, MySQLConnection


db = mysql.connector.connect(
    host="localhost",
    user="admin",
    passwd="adminPass",
    database="DBPointageUnelles",
)

my_cursor = db.cursor()


# test_table_query = "CREATE TABLE IF NOT EXISTS test_jeunes (id int PRIMARY KEY AUTO_INCREMENT, random int)"
# my_cursor.execute(test_table_query)
# db.commit()
#
# for i in range(0, int(input("Entrez le nombre d'ajouts: "))):
#     a: int = random.randint(0, i)
#     print("a= " + str(a))
#     test_add_data = f"INSERT INTO test_jeunes (id, random) VALUES (DEFAULT, {a})"
#     my_cursor.execute(test_add_data)
#
# db.commit()

def init_tuteur() -> str:
    return """
    CREATE TABLE IF NOT EXISTS Tuteur_Parent(
       Numéro_parent INT,
       Nom_parent VARCHAR(50) NOT NULL,
       Prénom_parent VARCHAR(50) NOT NULL,
       PRIMARY KEY(Numéro_parent)
    );"""


def init_ville() -> str:
    return """ CREATE TABLE IF NOT EXISTS Ville(
           Id_Ville INT AUTO_INCREMENT,
           Nom_de_la_ville VARCHAR(50) NOT NULL,
           Code_postal INT NOT NULL ,
           Dans_la_CMB BOOLEAN NOT NULL DEFAULT False,
           PRIMARY KEY(Id_Ville)
        );"""


def init_jeune() -> str:
    return """CREATE TABLE IF NOT EXISTS Jeune(
           Id_Jeune BIGINT AUTO_INCREMENT,
           Nom VARCHAR(50) NOT NULL,
           Prénom VARCHAR(50) NOT NULL,
           Régime_social ENUM('CAF', 'MSA', 'Autre') NOT NULL,
           Date_de_naissance DATE NOT NULL,
           Portable INT,
           Inscription DATE NOT NULL,
           Mail VARCHAR(50),
           Numéro_parent INT NOT NULL,
           Nom_Etablissement VARCHAR(50) NOT NULL,
           Id_Ville INT NOT NULL,
           PRIMARY KEY(Id_Jeune),
           UNIQUE(Portable),
           FOREIGN KEY(Numéro_parent) REFERENCES Tuteur_Parent(Numéro_parent),
           FOREIGN KEY(Id_Ville) REFERENCES Ville(Id_Ville)
        );
        """


def init_pointage() -> str:
    return """CREATE TABLE IF NOT EXISTS Pointage(
        Date_Heure_pointage DATETIME,
        Id_Jeune BIGINT NOT NULL,
        PRIMARY KEY(Date_Heure_pointage),
        FOREIGN KEY(Id_Jeune) REFERENCES Jeune(Id_Jeune)
        );"""


my_cursor.execute(init_tuteur())
db.commit()

my_cursor.execute(init_ville())
db.commit()

my_cursor.execute(init_jeune())
db.commit()

my_cursor.execute(init_pointage())
db.commit()

# i = random.randint(0, 9999)
# randomizer = random.randint(600000000, 799999999)
# inserts.insert_parent(randomizer, "Nom" + str(randomizer), "Prénom" + str(randomizer))

# inserts.insert_villes('none')
#
# last_num = int(str(randomizer)[-1:]) inserts.insert_jeune("Nom" + str(randomizer), "Prenom" + str(randomizer),
# 'CAF', "2004010" + str(last_num), randomizer, datetime.now().strftime('%Y%m%d'), randomizer, 5030)
#
# print(datetime.now().date())
# print(datetime.now())
# date_point: str = datetime.now().strftime('%Y%m%d%H%M%S')
# print(date_point)

# pointage_jeune1 = f"INSERT INTO Pointage(Date_Heure_pointage, Id_Jeune) VALUES ({date_point}, -2215705374427814992)"
# my_cursor.execute(pointage_jeune1)
# db.commit()

# my_cursor.execute("SELECT Date_Heure_pointage FROM Pointage")
# dates_extraite = my_cursor.fetchall()
# for x in dates_extraite:
#     print("x = ", x)
# print(type(date_functions.get_dates(dates_extraite)))
# print(date_functions.get_dates(dates_extraite))
# print(type(date_functions.get_times(dates_extraite)))
# print(date_functions.get_times(dates_extraite))
# #
# # print("End of main")
#
# totaux.total_jour(datetime.now().strftime('%Y-%m-%d'))
# totaux.total_hebdo(datetime.now().strftime('%Y-%m-%d'))
# totaux.total_hebdo('2022-03-3')

# my_cursor.execute("SELECT Nom_jeune, Prénom_jeune FROM Jeune")
# dates_extraite = my_cursor.fetchall()
# print(dates_extraite)
# print(type(dates_extraite))

# print(model.get_liste_jeunes())
# test_view = view()
# print(test_view.liste_jeunes)

