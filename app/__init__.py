from flask import Flask

def crateApp():

    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'g4df45h54d5fh64d5h4fg5hg45gf4hh4fg45h45f4gdfg4d5fg4d5s4f'

    #Blueprint routes Main
    from .blueprints.Main import main
    app.register_blueprint(main)
    

    return app