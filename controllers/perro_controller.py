from flask import render_template, make_response
from flask_restful import Resource
from flask_login import login_required
from models.perro import Perros
from models.cuidador import Cuidadores

class PerroController(Resource):
    @login_required
    def get(self):
        perros = Perros.query.all()
        return make_response(render_template("perro.html", perros=perros))

class LassieController(Resource):
    @login_required   
    def get(self):
         count = Perros.query.filter_by(nombre='Lassie').count()
         return make_response(render_template("lassie.html", count=count))

class PerrosDeMario(Resource): 
    @login_required   
    def get(self):
         cuidador = Cuidadores.query.filter_by(nombre='Mario').first()
         if cuidador:
             perros = Perros.query.filter_by(id_cuidador=cuidador.id).all() 
             return make_response(render_template("perrosdemario.html", perros=perros))
         else:
             return "No se encontró ningún cuidador llamado Mario."
         
    