from flask import Flask
from flask_sqlalchemy import SQLAlchemy

DB = SQLAlchemy()

def crateApp():

    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'g4df45h54d5fh64d5h4fg5hg45gf4hh4fg45h45f4gdfg4d5fg4d5s4f'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

    DB.init_app(app)

    #Blueprint routes Main
    from .blueprints.Main import main
    app.register_blueprint(main)
    

    return app