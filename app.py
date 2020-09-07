from flask import Flask, render_template
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

        user_object = User.query.filter_by(username=username).first()
        if user_object:
            return "someone else has taken this username!"

        user = User(username=username, password=password)
        db.session.add(user)
        db.session.commit()
        return "Inserted into DB!"

    return render_template("index.html", form=reg_form)


if __name__ == "__main__":
    app.run(debug=True)