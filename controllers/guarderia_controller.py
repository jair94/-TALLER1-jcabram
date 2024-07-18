from flask import render_template, make_response
from flask_restful import Resource
from flask_login import login_required
from models.guarderia import Guarderias

class GuarderiaController(Resource):
    @login_required
    def get(self):
        guarderias = Guarderias.query.all()
        return make_response(render_template("guarderia.html", guarderias=guarderias))
    