from flask import Flask, render_template, redirect, url_for
from passlib.hash import pbkdf2_sha256
from wtforms_fields import *
from models import *

app = Flask(__name__)
app.secret_key = 'Idontfuckingcare'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI']='postgres://ytdbqumpjfscjt:4b4e292afc9f625ba372a26ce5dde8b7020df316e91a4f81faea27a93accbb3e@ec2-54-147-54-83.compute-1.amazonaws.com:5432/dnbg4eods0163'

db = SQLAlchemy(app)

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
        return redirect(url_for('login'))

    return render_template("index.html", form=reg_form)

@app.route("/login", methods=['GET', 'POST'])
def login():

    login_form = LoginForm()

    if login_form.validate_on_submit():
        return "Logged in!"

    return render_template("login.html", form=login_form)    

if __name__ == "__main__":
    app.run(debug=True)