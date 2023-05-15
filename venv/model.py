import mysql.connector
from dataclasses import dataclass
from dotenv import load_dotenv
import os

load_dotenv()

"""Fonctions utilisees pour communiquer avec la base de donnes et l'initialiser"""


@dataclass
class Database:
    animateur: str
    periode_scolaire: bool
    error_msg: str
    pointages: list
    password: str = os.getenv("POINTAGE_PASSWD")

    """connecteur vers la base de donnee, les mdp etc sont stockees dans 
    des variables environnement pour ne pas les ecrires en clair dans le code"""
    db = mysql.connector.connect(
        host=os.getenv("POINTAGE_HOST"),
        user=os.getenv("POINTAGE_USER"),
        passwd=os.getenv("POINTAGE_PASSWD"),
        database=os.getenv("POINTAGE_DATABASE"),
    )


def liste_pointages_jour() -> list:
    """
    Outil pour connaitre la liste des jeunes pointes aujourd'hui, utile pour verifier qu'un jeune ne se pointe
    pas 2 fois

    :return: Liste des jeunes pointes le jour courant
    """
    pointes_jour_id = query("SELECT Id_Jeune FROM Pointage WHERE DATE(Date_Heure_pointage) = CURRENT_DATE", False)

    liste_pointages: list = []
    for x in pointes_jour_id:
        nom_prenom = query(f"SELECT CONCAT(Nom_jeune, ' ', Prénom_jeune) FROM Jeune WHERE Id_Jeune = '{x[0]}'", False)

        liste_pointages.append(nom_prenom[0][0])
    return liste_pointages


def setup_database(anim: str, password: str):
    """

    :param anim: Nom de l'animateur qui ouvre l'appli
    :param password: mot de passe de la base de donnees
    """
    Database.animateur = anim
    Database.password = password


def commit_to_database():
    """
    Commit les requetes a la base de donnees, affichera un pop-up si le commit echoue, avec le message d'erreur
    """
    try:
        Database.db.commit()
    except Exception as error:
        Database.error_msg = error
        view.show_error_popup()


def query_one(str_query: str, as_dict=True):
    """
    Outil pour faire une requete d'une seule donnee

    :param str_query: La query a ecrire en SQL
    :param as_dict: Les donnees seront recuperees sous forme de dictionnaire par defaut
    :return: Le resultat de la requete dans un dictionnaire avec key = nom de la colonne et value = donnee
    """
    with Database.db.cursor(buffered=True, dictionary=as_dict) as cursor:
        cursor.execute(str_query)
        result = cursor.fetchone()
    return result


def query(str_query: str, as_dict: bool = True) -> object:
    """
    Outil pour faire une requete de plusieurs donnees

    :param str_query: La query a ecrire en SQL
    :param as_dict: Les donnees seront recuperees sous forme de dictionnaire par defaut (true)
    :return: L'ensemble des donnes, dans une liste de tuples si as_dict est false
    """
    with Database.db.cursor(buffered=True, dictionary=as_dict) as cursor:
        cursor.execute(str_query)
        return cursor.fetchall()


def insert(table: str, columns: str, values: str):
    """
    Outil d'insertion dans une table

    :param values : Donnees a inserer
    :param columns : Nom de la colonne
    :param table : Nom de la table
    """
    with Database.db.cursor() as cursor:
        cursor.execute(f"INSERT INTO {table}{columns} VALUES {values}")
        commit_to_database()


def create_tables():
    """
    Outil de creation des tables de la base de donnees
    """
    with Database.db.cursor() as cursor:
        cursor.execute("""create table if not exists Ville
(
    Id_Ville        int auto_increment
        primary key,
    Nom_de_la_ville varchar(50)          not null,
    Code_postal     int                  not null,
    Dans_la_CMB     tinyint(1) default 0 not null
);
""")

        # Create table Tuteur_Parent if not exist
        cursor.execute("""create table if not exists Tuteur_Parent
                                    (
                                        Numéro_parent int         not null
                                            primary key,
                                        Nom_parent    varchar(50) not null,
                                        Prénom_parent varchar(50) not null
                                    );""")

        # Create table Jeune if not exist
        cursor.execute("""create table if not exists Jeune(Id_Jeune bigint auto_increment primary key,
        Nom_jeune         varchar(50)                             not null,
        Prénom_jeune      varchar(50)                             not null,
        Date_de_naissance date                                    not null,
        Genre             enum ('Garçon', 'Fille', 'Non-Binaire') not null,
        Nom_Etablissement varchar(50) default 'Aucun'             not null,
        Portable          int                                     null,
        Mail              varchar(50)                             null,
        Régime_social     enum ('CAF', 'MSA', 'Autre')            not null,
        Numéro_parent     int                                     not null,
        Id_Ville          int                                     not null,
        Inscription       date        default curdate()           not null,
        constraint Jeune_ibfk_1
            foreign key (Numéro_parent) references Tuteur_Parent (Numéro_parent),
        constraint foreign_key_name
            foreign key (Id_Ville) references Ville (Id_Ville)
    );""")
        cursor.execute("create index if not exists Numéro_parent on Jeune (Numéro_parent);")

        # Create table Pointage if not exist
        cursor.execute("""create table if not exists Pointage
                        (
                            Date_Heure_pointage datetime   default current_timestamp() not null
                                primary key,
                            Id_Jeune            bigint                                 not null,
                            Animateur           varchar(50)                            not null,
                            PeriodeScolaire     tinyint(1) default 1                   not null,
                            constraint Pointage_ibfk_1
                                foreign key (Id_Jeune) references Jeune (Id_Jeune)
                        );""")
        cursor.execute("""create index if not exists Id_Jeune
                        on Pointage (Id_Jeune);""")


def get_liste_jeunes() -> dict:
    """
    Retourne la liste complete des noms de jeunes inscrits dans un dictionnaire
    """
    return query("SELECT Nom_jeune, Prénom_jeune FROM Jeune", True)


def get_liste_communes() -> list:
    """

    :return: La liste des villes dans la table Ville
    """
    return query("SELECT Nom_de_la_ville FROM Ville")


def infos_valides(infos: dict) -> bool:
    """
    Outil de validation des donnees pour enregistrer un jeune

    :param infos: Les donnees a verifier, avec key = colonne et value = donnee
    :return: Vrai si les infos ne contiennent pas de valeur interdite, s'il n'y a pas de champ vide etc
    """
    if not infos:
        return False
    for key, value in infos.items():
        if not value:
            Database.error_msg = f"{key} vide, veuillez remplir ce champ"
            return False
    if 9 > len(infos.get('Numéro_parent')) < 10:
        Database.error_msg = "Numéro de téléphone invalide"
        return False

    return True
