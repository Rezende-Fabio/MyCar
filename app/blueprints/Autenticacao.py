from flask import Blueprint, request, render_template, redirect
from flask_login import login_user, login_required, current_user, logout_user
from .. import DB
from ..models.Models import *

autenticacao = Blueprint('autenticacao', __name__)

@autenticacao.route('/login', methods=['POST'])
def login():
    if request.method == "POST":
        user = request.form["usuario"]
        senha = request.form["senha"]
        user = User.query.filter_by(email=user, password=senha).first()
        login_user(user)
        
        return render_template("base.html", user=user)


@autenticacao.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")
