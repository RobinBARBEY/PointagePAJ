import datetime

from view import View
import model
from model import Database

"""Fonctions qui controlent les flux de donnees, les traitements et verifications a effectuer"""

def valider_pointage(current_view, nom_prenom: str):
    # print(nom_prenom)
    exists = model.query(f"SELECT EXISTS(SELECT Id_Jeune FROM Jeune "
                         f"WHERE CONCAT(Nom_jeune, ' ', Prénom_jeune) = '{nom_prenom}')", False)
    print(Database.pointages)
    print(nom_prenom)
    if exists[0][0] == 1 and nom_prenom not in Database.pointages:
        enregistrement_pointage(nom_prenom)
    else:
        Database.error_msg = "Nom hors base de donnée ou déjà pointé aujourd'hui"
        View.show_error_popup()
    current_view.ui.comboBoxEntreePointage.setCurrentText("")


# TODO Rename this here and in `valider_pointage`
def enregistrement_pointage(nom_prenom):
    Id = model.query_one(f"SELECT Id_Jeune FROM Jeune "
                         f"WHERE CONCAT(Nom_jeune, ' ', Prénom_jeune) = '{nom_prenom}'", False)

    model.insert('Pointage', '(Id_Jeune, Animateur, PeriodeScolaire)',
                 f"('{Id[0]}', '{Database.animateur}', {Database.periode_scolaire})")
    model.commit_to_database()

    Database.pointages.append(nom_prenom)

    Database.error_msg = "Pointage validé"
    View.show_error_popup(False)


def valider_inscription(current_view, infos: dict):
    # valider les infos avant de les passer dans une query TODO
    if not infos:
        return

    nom_jeune: str = infos.get('Nom_jeune')
    nom_jeune = nom_jeune.upper()
    nom_jeune = nom_jeune.rstrip().lstrip()

    prenom_jeune: str = infos.get('Prénom_jeune')
    prenom_jeune = prenom_jeune.lstrip().rstrip()
    prenom_jeune = prenom_jeune[0].upper() + prenom_jeune[1:].lower()

    genre = infos.get('Genre')

    date_as_tuple = infos.get('Date_de_naissance')
    date_naissance = datetime.date(date_as_tuple[0], date_as_tuple[1], date_as_tuple[2])

    etab_scolaire = infos.get('Nom_Etablissement')
    regime_social = infos.get('Régime_social')
    num_parent = infos.get('Numéro_parent')
    nom_parent = infos.get('Nom_parent')
    prenom_parent = infos.get('Prénom_parent')
    commune: dict = model.query_one(
        f"SELECT Id_Ville FROM Ville WHERE Nom_de_la_ville = '{infos.get('Nom_de_la_ville')}'")
    # print("commune:", commune, type(commune))
    id_commune = commune.get('Id_Ville')
    # print("id commune:", id_commune)

    if parent_not_in_db(num_parent):
        model.insert('Tuteur_Parent', '(Numéro_parent, Nom_parent, Prénom_parent)',
                     f"('{num_parent}', '{nom_parent}', '{prenom_parent}')")
        model.commit_to_database()

    model.insert('Jeune', '(Nom_jeune, Prénom_jeune, Date_de_naissance, Genre,'
                          ' Nom_Etablissement, Régime_social, Numéro_parent, Id_Ville)',
                 f"('{nom_jeune}', '{prenom_jeune}', '{date_naissance}',"
                 f" '{genre}', '{etab_scolaire}', '{regime_social}', '{num_parent}', '{id_commune}')")
    model.commit_to_database()

    Database.error_msg = "L'inscription est validée"
    View.show_error_popup(False)

    valider_pointage(current_view, f"{nom_jeune} {prenom_jeune}")


def parent_not_in_db(num_id: int) -> bool:
    is_in_DB = model.query(f"SELECT EXISTS(SELECT Numéro_parent FROM Tuteur_Parent WHERE Numéro_parent = '{num_id}')",
                           False)

    # print(is_in_DB[0][0])
    return is_in_DB[0][0] == 0


def select_jeune_modif(current_view: View, nom_prenom: str):
    # print(nom_prenom)
    exists = model.query_one(f"SELECT EXISTS(SELECT Id_Jeune FROM Jeune "
                             f"WHERE CONCAT(Nom_jeune, ' ', Prénom_jeune) = '{nom_prenom}')", False)
    # print(exists)
    if exists[0] == 1:
        Id = model.query_one(f"SELECT Id_Jeune FROM Jeune WHERE CONCAT(Nom_jeune, ' ', Prénom_jeune) = '{nom_prenom}'",
                             False)
        infos = model.query(f"SELECT * FROM Jeune WHERE Id_Jeune = {Id[0]}")
        # print(infos[0])
        current_view.update_modif(infos[0])


def appliquer_modif(infos: dict):
    if not infos:
        return
    additional_infos: dict = model.query_one(f"SELECT Id_Jeune, Numéro_parent FROM Jeune "
                                             f"WHERE CONCAT(Nom_jeune, Prénom_jeune) = "
                                             f"'{infos.get('Nom_jeune') + infos.get('Prénom_jeune')}'")
    date_as_tuple = infos.get('Date_de_naissance')
    date_naissance = datetime.date(date_as_tuple[0], date_as_tuple[1], date_as_tuple[2])
    id_jeune = additional_infos.get('Id_Jeune')
    old_num = additional_infos.get('Numéro_parent')
    new_num = int(infos.get('Numéro_parent'))
    # print(type(old_Num), type(new_num), "numbers", old_Num == new_num)

    if not old_num == new_num and parent_not_in_db(new_num):
        model.insert('Tuteur_Parent', '(Numéro_parent, Nom_parent, Prénom_parent)',
                     f"({new_num}, '{infos.get('Nom_parent')}', '{infos.get('Prénom_parent')}')")
        model.commit_to_database()

        model.query(f"UPDATE Jeune SET Numéro_parent = {new_num} WHERE Id_Jeune = '{id_jeune}'", False, False)
        model.commit_to_database()

        model.query(f"DELETE FROM Tuteur_Parent WHERE Numéro_parent = {old_num}",
                    False, False)
        model.commit_to_database()

    model.query(f"UPDATE Jeune SET Nom_jeune = '{infos.get('Nom_jeune')}', "
                f"Prénom_jeune = '{infos.get('Prénom_jeune')}', Date_de_naissance = '{date_naissance}',"
                f"Genre = '{infos.get('Genre')}', Nom_Etablissement = '{infos.get('Nom_Etablissement')}', "
                f"Régime_social = '{infos.get('Régime_social')}', Numéro_parent = {new_num}, "
                f"Id_Ville = {infos.get('Id_Ville')} WHERE Id_Jeune = '{id_jeune}'", False, False)
    model.commit_to_database()


def calculTotal(current_view: View, dates, filtres):
    date_debut = datetime.date(*dates[0])
    date_fin = datetime.date(*dates[1])
    # print("Calcul du:", date_debut, "au:", date_fin)
    # print("Et filtres:", filtres)
    total = model.query_one("SELECT COUNT(*) FROM Pointage "
                            f"WHERE DATE(Date_Heure_pointage) BETWEEN DATE('{date_debut}') AND DATE('{date_fin}')", False)
    # print("Total:", total)
    current_view.show_total(total[0])
