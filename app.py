from flask import Flask, render_template, redirect, url_for, flash
from flask_login import LoginManager, login_user, current_user, login_required, logout_user
from wtforms_fields import *
from models import *
from flask_socketio import SocketIO, send, emit

app = Flask(__name__)
app.secret_key = 'Idontfuckingcare'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI']='postgres://ytdbqumpjfscjt:4b4e292afc9f625ba372a26ce5dde8b7020df316e91a4f81faea27a93accbb3e@ec2-54-147-54-83.compute-1.amazonaws.com:5432/dnbg4eods0163'
socketio = SocketIO(app)
db = SQLAlchemy(app)

login = LoginManager()
login.init_app(app)

@login.user_loader
def load_user(id):

    return User.query.get(int(id))


@app.route("/", methods=['GET', 'POST'])
def index():
    
    reg_form = RegistrationForm()

    if reg_form.validate_on_submit():
        username = reg_form.username.data
        password = reg_form.password.data
        
        hashed_pswd = pbkdf2_sha256.hash(password)

        user = User(username=username, password=hashed_pswd)
        db.session.add(user)
        db.session.commit()

        flash('Registered successfully. Please Login.', 'success')
        return redirect(url_for('login'))

    return render_template("index.html", form=reg_form)

@app.route("/login", methods=['GET', 'POST'])
def login():

    login_form = LoginForm()

    if login_form.validate_on_submit():
        user_object = User.query.filter_by(username=login_form.username.data).first()
        login_user(user_object)
        return redirect(url_for('chat'))

    return render_template("login.html", form=login_form)    
@app.route("/chat", methods=['GET', 'POST'])

def chat():
    #if not current_user.is_authenticated:
    #    flash('Please login', 'danger')
    #    return redirect(url_for('login'))
    return render_template('chat.html', username=current_user.username)

@app.route("/logout", methods=['GET'])
def logout():

    logout_user()
    flash('You have logged out successfully', 'success')
    return redirect(url_for('login'))


@socketio.on('message')
def message(data):

    print(f"\n\n{data}\n\n")
    
    send(data)

    #emit('some-event', 'this is a custom event message')

if __name__ == "__main__":
    socketio.run(app, debug=True)
   