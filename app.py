from flask import Flask, request, render_template, redirect, flash
# importar nuestros modelos
from models import Usuario, db
from config import Config
from flask_session import Session
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.exc import IntegrityError
# importar modulo para que el usuario haga login
from flask_login import LoginManager, login_user, logout_user, login_required, current_user

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

# configuraciones para el login
login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return Usuario.query.get(int(user_id))


@app.route('/')
@login_required
def index():
    return render_template('index.html')
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

        # generar hash_password
        hash = generate_password_hash(password)
        # creamos un nuevo usuario
        try:
            # si el usuario es nuevo
            usuario_nuevo = Usuario(username=username, correo=correo, password_hash=hash)
            db.session.add(usuario_nuevo)
            db.session.commit()
        except IntegrityError as e:
            # si el usuario ya existe
            db.session.rollback()
            flash("El usuario ya existe, verifique de nuevo",'warning' )
            return redirect('/register')

        flash('Usuario registrado', 'success')
        return redirect('/')
    else:
        return render_template('register.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        # validaciones
        # si los campos estan vacios
        if not email or not password:
            flash("Campos vacios", "danger")
            return redirect("/login")
        
        # si el usuario no existe
        # el que esta a la izquierda del igual es el campo de mi modelo Usuario
        usuario = Usuario.query.filter_by(correo=email).first()

        if usuario is None:
            flash("El usuario no existe", "warning")
            return redirect("/login")
        
        # si las passwords coinciden
        if not check_password_hash(usuario.password_hash, password):
            flash("Las passwords no coinciden", "warning")
            return redirect("/login")
        
        # logear al usuario
        login_user(usuario)
        flash("Inicio de sesion exitoso", "success")
        return redirect("/")
    else:
        return render_template("login.html")

@app.route("/logout")
def logout():
    logout_user()
    flash("Has cerrado sesion", "primary")
    return redirect("/")

if __name__ == '__main__':
    app.run(debug=True) 