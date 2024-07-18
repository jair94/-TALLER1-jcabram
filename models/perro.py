from db import db
"""from flask import render_template, make_response
from flask_restful import Resource
from app import Perro
from db import db

class PerroController(Resource):
    def get(self):
        perro = Perro.query.all()
        return make_response(render_template("perro.html", perro=perro))
        """
class Perros(db.Model):
    id = db.Column(db.Integer,primary_key= True)
    nombre = db.Column(db.String(255),nullable = False)
    raza = db.Column(db.String(255),nullable = False)
    edad = db.Column(db.Integer, nullable = False)
    peso = db.Column(db.Float, nullable = False)

    id_cuidador = db.Column(db.Integer,db.ForeignKey("cuidadores.id"),nullable = False)
    id_guarderia = db.Column(db.Integer,db.ForeignKey("guarderias.id"),nullable = False)
