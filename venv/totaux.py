"""Fonctions pour calcul des totaux :
-Journalier: total_jour
-Hebdomadaire: total_hebdo
-Mensuel: total_mois
-Annuel: total_an
"""
import mysql

db = mysql.connector.connect(
    host="localhost",
    user="admin",
    passwd="adminPass",
    database="DBPointageUnelles",
)

my_cursor = db.cursor()


def total_jour(date_jour: str) -> int:
    """Retourne le total de pointages du jour en entrée"""
    print(date_jour)
    query = "SELECT COUNT(*) FROM Pointage "\
            f"WHERE DATE(Date_Heure_pointage) = DATE('{date_jour}');"
    my_cursor.execute(query)
    total: int = int(my_cursor.fetchone()[0])
    print("total jour " + date_jour.format('YYYY-MM-DD') + ": " + str(total))
    return total


def total_hebdo(date_debut_semaine: str) -> int:
    query = "SELECT COUNT(*) FROM Pointage "\
            f"WHERE WEEK(Date_Heure_pointage) = WEEK('{date_debut_semaine}');"
    my_cursor.execute(query)
    total: int = int(my_cursor.fetchone()[0])
    print("total mois " + date_debut_semaine + ": " + str(total))
    return total
