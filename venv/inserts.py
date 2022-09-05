"""Fonctions pour insérer dans la Base de données
"""
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="admin",
    passwd="adminPass",
    database="DBPointageUnelles",
)

my_cursor = db.cursor()


def insert_parent(Numero: int, Nom: str, Prenom: str):
    """
    Insertion du Numéro, Nom et Prénom dans la table parent

    :param Numero: int
    :param Prenom: str
    :param Nom: str
    :exception TypeError : print errors if types can't be passed to the SQL query
    """
    try:
        query = "INSERT INTO Tuteur_Parent " \
                f"VALUES ({Numero}, '{Nom}', '{Prenom}')"
        my_cursor.execute(query)
        db.commit()
        print(f"Insertion parent {Nom} {Prenom} effectuée")
    except Exception as error:
        print(f'Parent non inséré, erreur: {error} dans insert_parent()')


def insert_villes(path: str):

    try:
        query = f"LOAD DATA INFILE 'laposte_hexasmal.csv'INTO TABLE Ville " \
                f"FIELDS TERMINATED BY ',' ENCLOSED BY '' LINES TERMINATED BY '\n' " \
                f"IGNORE 1 ROWS (ligne_5, libelle_d_acheminement, coordonnees_gps)"
        my_cursor.execute(query)
        db.commit()
        print(f"Insertion ville {Nom} effectuée")
    except Exception as error:
        raise error


def insert_jeune(Nom: str, Prenom: str, Date_naissance, Genre, Nom_Etab: str,
                 Portable: int, Num_Portable: int, Mail, Reg_soc, Num_parent, Id_V: int):
    """

    :param Nom:
    :param Prenom:
    :param Date_naissance:
    :param Genre:
    :param Nom_Etab:
    :param Portable:
    :param Num_Portable:
    :param Mail:
    :param Reg_soc:
    :param Num_parent:
    :param Id_V:
    """
    try:
        query = f"insert into Jeune (Nom_jeune, Prénom_jeune, Date_de_naissance,"\
                " Genre, Régime_social, Numéro_parent, Id_Ville) "\
                f"values ({Nom}, {Prenom}, {Date_naissance}, {Genre}, {Nom_Etab},"\
                 f"{Portable}, {Num_Portable}, {Mail}, {Reg_soc}, {Num_parent}, {Id_V});"
        my_cursor.execute(query)
        db.commit()
        print(f"Insertion jeune {Nom} {Prenom} effectuée")
    except Exception as error:
        print(f'Jeune non inséré, erreur: {error} dans insert_jeune()')


def pointage(Id: int):
    try:
        query = f"INSERT INTO Pointage VALUES (CURRENT_DATE, {Id});"
        my_cursor.execute(query)
        db.commit()
    except Exception as error:
        print(f"Pointage non enregistré, erreur: {error}")
