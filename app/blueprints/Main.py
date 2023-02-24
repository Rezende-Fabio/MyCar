from flask import Blueprint, render_template
from flask_login import login_required
from .. import DB
from ..models.Models import *

main = Blueprint("main", __name__)

@main.route("/")
@main.route("/index")
def index():
    return render_template("index.html")

@main.route('/teste')
@login_required
def loginTeste():
    return render_template("teste2.html")