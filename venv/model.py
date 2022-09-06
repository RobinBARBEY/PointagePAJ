import mariadb
from dataclasses import dataclass
from dotenv import load_dotenv
import os

load_dotenv()


@dataclass
class database:
    animateur: str
    periode_scolaire: bool
    error_msg: str
    pointages: list
    password: str = os.getenv("POINTAGE_PASSWD")

    db = mariadb.connect(
        host=os.getenv("POINTAGE_HOST"),
        user=os.getenv("POINTAGE_USER"),
        passwd=os.getenv("POINTAGE_PASSWD"),
        database=os.getenv("POINTAGE_DATABASE"),
    )


def liste_pointages_jour() -> list:
    pointes_jour_id = query("SELECT Id_Jeune FROM Pointage WHERE DATE(Date_Heure_pointage) = CURRENT_DATE", False)

    liste_pointages: list = []
    for x in pointes_jour_id:
        nom_prenom = query(f"SELECT CONCAT(Nom_jeune, ' ', Prénom_jeune) FROM Jeune WHERE Id_Jeune = '{x[0]}'", False)

        liste_pointages.append(nom_prenom[0][0])
    return liste_pointages


def setup_database(anim: str, password: str):
    database.animateur = anim
    database.password = password


def commit_to_database():
    try:
        database.db.commit()
    except Exception as error:
        database.error_msg = error
        view.show_error_popup()


def query_one(str_query: str, as_dict=True):
    with database.db.cursor(buffered=True, dictionary=as_dict) as cursor:
        cursor.execute(str_query)
        result = cursor.fetchone()
    return result


def query(str_query: str, as_dict=True, fetch=True):
    with database.db.cursor(buffered=True, dictionary=as_dict) as cursor:
        cursor.execute(str_query)
        if fetch:
            return cursor.fetchall()


def insert(table: str, columns: str, values: str):
    with database.db.cursor() as cursor:
        cursor.execute(f"INSERT INTO {table}{columns} VALUES {values}")
        commit_to_database()


def create_tables():
    with database.db.cursor() as cursor:
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
    return query("SELECT Nom_jeune, Prénom_jeune FROM Jeune", True)


def get_liste_communes() -> list:
    return query("SELECT Nom_de_la_ville FROM Ville")


def infos_valides(infos: dict) -> bool:
    if not infos:
        return False
    for key, value in infos.items():
        if not value:
            database.error_msg = f"{key} vide, veuillez remplir ce champ"
            return False
    if 9 > len(infos.get('Numéro_parent')) < 10:
        database.error_msg = "Numéro de téléphone invalide"
        return False

    return True
