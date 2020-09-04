from flask import Flask, render_template
from wtforms_fields import *


app = Flask(__name__)
app.secret_key = 'Idontfuckingcare'
@app.route("/", methods=['GET', 'POST'])
def index():
    
    reg_form = RegistrationForm()

    if reg_form.validate_on_submit():
        return "Great success"

    return render_template("index.html", form=reg_form)


if __name__ == "__main__":
    app.run(debug=True)