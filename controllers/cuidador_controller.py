from flask import render_template, make_response
from flask_restful import Resource
from flask_login import login_required
from models.cuidador import Cuidadores

class CuidadorController(Resource):

    @login_required
    def get(self):
        cuidadores = Cuidadores.query.all()
        return make_response(render_template("cuidador.html", cuidadores=cuidadores))
