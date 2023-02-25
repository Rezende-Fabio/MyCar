from flask import Blueprint, render_template
from flask_login import login_required
from .. import DB
from ..models.Models import *

carro = Blueprint("carro", __name__)

@carro.route("/carro/lista")
def listaCarro():
    return render_template("carro/lista.html")


@carro.route("/carro/cadastro")
def cadCarro():
    return render_template("carro/cadastro.html")