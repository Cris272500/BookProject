from flask import Flask, request, render_template, redirect, flash
# importar nuestros modelos
from models import Usuario, db
from config import Config
from flask_session import Session
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# configuraciones extra
# conexion a base de datos
app.config.from_object(Config)

# configuraciones de las sesiones
app.config['SESSION_PERMANENT'] = False
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

# ejecutamos la base de datos
db.init_app(app)

empleados = [
    {
        "id": 1,
        "nombre": "Juan Pérez",
        "edad": 28,
        "departamento": "Ventas",
        "salario": 35000,
        "fecha_contratacion": "2019-04-21"
    },
    {
        "id": 2,
        "nombre": "María López",
        "edad": 34,
        "departamento": "Marketing",
        "salario": 42000,
        "fecha_contratacion": "2018-07-14"
    },
    {
        "id": 3,
        "nombre": "Carlos Sánchez",
        "edad": 45,
        "departamento": "Finanzas",
        "salario": 58000,
        "fecha_contratacion": "2012-01-12"
    },
    {
        "id": 4,
        "nombre": "Ana Torres",
        "edad": 30,
        "departamento": "Recursos Humanos",
        "salario": 39000,
        "fecha_contratacion": "2020-09-01"
    },
]

@app.route('/')
def index():
    nombre = "David"
    edad = 20
    precio = 100

    return render_template('index.html', nombre=nombre, edad=edad, precio=precio, empleados=empleados)
@app.route('/repaso/<nombre>')
def repaso(nombre):
    return f"Hola {nombre}"

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username') # es para recibir un input
        correo = request.form.get('email')
        password = request.form.get('password')

        # si los campos estan vacios
        if not username or not correo or not password:
            # mostramos una alerta de error
            flash("Campos vacios", 'danger')
            return redirect('/register')

        # creamos un nuevo usuario
        # si el usuario ya existe
        # generar hash_password
        hash = generate_password_hash(password)
        usuario_existente = Usuario.query.filter_by(username=username, correo=correo).first()

        if usuario_existente:
            flash("Ese usuario ya existe", 'warning ')
            return redirect('/')
        
        # si el usuario es nuevo
        usuario_nuevo = Usuario(username=username, correo=correo, password_hash=hash)

        db.session.add(usuario_nuevo)
        db.session.commit()

        flash('Usuario registrado', 'success')
        return redirect('/')
    else:
        return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True) 