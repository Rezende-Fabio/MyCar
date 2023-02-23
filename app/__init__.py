from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os

DB = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    basedir = os.path.abspath(os.path.dirname(__file__))

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'Car.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    app.config["SECRET_KEY"] = 'pbkdf2:sha256:260000$9C1lotTLZookpgaC$cd1fb937818bee2ec8c5a8a1f8e7f3b40c49ddd452a63ca1bec553c2d03724da'
    
    from .blueprints.Autenticacao import autenticacao
    app.register_blueprint(autenticacao)
    
    from .blueprints.Main import main
    app.register_blueprint(main)
    
    DB.init_app(app)
    
    login_manager = LoginManager()
    login_manager.login_view = 'autenticacao.login'
    login_manager.init_app(app)
    
    from .models.Models import User
    
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app