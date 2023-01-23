"""Le service informatique du CHU de Caen est très satisfait de votre dernière mission,
 il souhaite maintenant que vous développiez pour lui un API en flask.
Vous devrez dans un premier temps créer les 2 tables MySQL suivantes via phpMyAdmin : "materiel" & "employe"
Ensuite vous les peuplerez à l'aide du script populateTables.py qui insérera les données contenues dans data.json.

In fine, votre API Rest qui vous permettra de réaliser un CRUD sur vos  "materiel" & "employe".

NB : Vous devriez normalement avoir 8 endpoints et vous pouvez vous inspirer des exercices faits la semaine du 16/01.
NB2 : Cliquez sur le lien github "document" ci-dessous pour récupérer les fichiers

Bon courage !!"""

import mysql.connector
import json
import pandas as pd


file = open(r"C:\VS_Progs\Projets\brief\23-01-23_Le_stagiaire_est_enfin_parti__le_CHU_de_Caen_veut_une_API\sql.json", "r")
ident = json.load(file)
db = mysql.connector.connect(**ident)
cursor = db.cursor()
cursor.execute("DELETE FROM employe")
db.commit()
cursor.execute("DELETE FROM materiel")
db.commit()

file = open(r"C:\VS_Progs\Projets\brief\23-01-23_Le_stagiaire_est_enfin_parti__le_CHU_de_Caen_veut_une_API\data.json", "r", encoding="utf-8")
data = json.load(file)




def insert_materiel(nom_du_produit, dimensions, etat):
    cursor.execute(f"""insert into materiel(nom_du_produit, dimensions, etat) VALUES("{nom_du_produit}", "{dimensions}", "{etat}");""")
    db.commit()

def insert_employe(nom, prénom, age, profession):
    cursor.execute(f"""insert into employe(nom, prénom, age, profession) VALUES("{nom}", "{prénom}", "{age}", "{profession}");""")
    db.commit()



for dict in data["materiel"]:
    for key, value in dict.items():
        insert_materiel(value[0], value[1], value[2])

for dict in data["employe"]:
    for key, value in dict.items():
        insert_employe(value[0], value[1], value[2], value[3])



if __name__ == "__main__":
    pass