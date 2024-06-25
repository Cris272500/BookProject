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

class Autor(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(200), nullable=False)
    biografia = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f"Nombre: {self.nombre}"

class Categoria(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(80), nullable=False, unique=True)

    def __repr__(self):
        return f"Categoria: {self.nombre}"


# tabla relacion, n-n / Categoria y Libro
categorias_libro = db.Table("categorias_libro", 
            db.Column('libro_id', db.Integer, db.ForeignKey('libro.id'), primary_key=True),
            db.Column('categoria_id', db.Integer, db.ForeignKey('categoria.id'), primary_key=True)
            )
            

class Libro(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    titulo = db.Column(db.String(150), nullable=False)
    descripcion = db.Column(db.Text, nullable=False)
    fecha_publicacion = db.Column(db.Date, nullable=False)
    # campo autor 1-n
    autor_id = db.Column(db.Integer, db.ForeignKey('autor.id'), nullable=False)
    # campo categoria n-n
    categorias = db.relationship('Categoria', secondary=categorias_libro,
                                 backref='libros', lazy="dynamic")
    user_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)