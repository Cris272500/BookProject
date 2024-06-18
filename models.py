# en este archivo vamosa crear nuestros modelos o TABLAS
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Usuario(db.Model):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    password_hash = db.Column(db.String(100), nullable=False)
    correo = db.Column(db.String(40), nullable=False, unique=True)

    # funcion para imprimir un registro de este modelo
    def __repr__(self):
        return f"Username: {self.username}"
    

    # metodos de flask-login
    @property
    def is_authenticated(self):
        return True 
    
    @property
    def is_active(self):
        return True 
    
    @property
    def is_anonymous(self):
        return False
    
    def get_id(self):
        return str(self.id)