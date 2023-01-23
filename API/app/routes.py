

import json
from flask import render_template, request, redirect, jsonify
import pandas as pd
import numpy as np
import mysql.connector as mysqlpy
from app import app

file = open(r"C:\VS_Progs\Projets\brief\23-01-23_Le_stagiaire_est_enfin_parti__le_CHU_de_Caen_veut_une_API\sql.json", "r")
int = json.load(file)
db = mysqlpy.connect(**int) 
cursor = db.cursor()   
dbOK = db.is_connected()

@app.route('/employe', methods=["GET"])
def get_db():
    cursor.execute(f"Select * from employe ;")
    result_db = cursor.fetchall()
    return result_db


@app.route('/materiel', methods=["GET"])
def get_db1():
    cursor.execute(f"Select * from materiel ;")
    result_db = cursor.fetchall()
    return result_db




@app.route('/employe', methods=["POST"])
def add():
    record = request.get_json()
    try:
        
        cursor.execute(f"""INSERT INTO employe(nom, prénom, age, profession) VALUES('{record["nom"]}', '{record["prénom"]}', '{record["age"]}', '{record["profession"]}');""")
        db.commit()
        result_db = get_db()
        return result_db

    except Exception as e:
        return {"erreur" : e}

@app.route('/materiel', methods=["POST"])
def add1():
    record = request.get_json()
    try:
        
        cursor.execute(f"""INSERT INTO materiel(nom_du_produit, dimensions, etat) VALUES('{record["nom_du_produit"]}', '{record["dimensions"]}', '{record["etat"]}');""")
        db.commit()
        result_db = get_db1()
        return result_db

    except Exception as e:
        return {"erreur" : e}



@app.route('/employe', methods=["PUT"])
def modif():
    try:
        record = request.get_json()
        query=f"""UPDATE employe SET nom='{record['nom']}', prénom='{record['prénom']}', age='{record['age']}', profession='{record['profession']}' WHERE id='{record['id']}' ;"""
        cursor.execute(query)
        db.commit()
        result_db = get_db()
        return result_db

    except Exception as e:
        return {"erreur" : e}

@app.route('/materiel', methods=["PUT"])
def modif1():
    try:
        record = request.get_json()
        query=f"""UPDATE materiel SET nom_du_produit='{record['nom_du_produit']}', dimensions='{record['dimensions']}', etat='{record['etat']}' WHERE id='{record['id']}' ;"""
        cursor.execute(query)
        db.commit()
        result_db = get_db1()
        return result_db

    except Exception as e:
        return {"erreur" : e}


@app.route('/employe', methods=["DELETE"])
def delete():
    record = request.get_json()

    try:
        query=f"""DELETE FROM employe WHERE id='{record['id']}' ;"""
        cursor.execute(query)
        db.commit()
        result_db = get_db()
        return result_db

    except Exception as e:
        return {"erreur" : e}

@app.route('/materiel', methods=["DELETE"])
def delete1():
    record = request.get_json()

    try:
        query=f"""DELETE FROM materiel WHERE id='{record['id']}' ;"""
        cursor.execute(query)
        db.commit()
        result_db = get_db()
        return result_db

    except Exception as e:
        return {"erreur" : e}
