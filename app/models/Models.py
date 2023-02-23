from .. import DB
from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash

class User(UserMixin, DB.Model):
    id = DB.Column(DB.Integer, primary_key=True)
    email = DB.Column(DB.String(100), unique=True)
    password = DB.Column(DB.String(100))
    name = DB.Column(DB.String(1000))

    def __init__(self, email, nome, pssd):
        self.email = email
        self.name = nome
        self.password = pssd
    
        
