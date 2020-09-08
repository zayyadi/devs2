from flask_wtf import FlaskForm
from passlib.hash import pbkdf2_sha256
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, EqualTo, ValidationError
from models import User 


def invalid_credentials(form, field):
    """username and password checker"""

    username_entered = form.username.data
    password_entered = field.data

    user_object = User.query.filter_by(username=username_entered).first()
    if user_object is None:
        raise ValidationError("Username or password incorrect")
    elif not pbkdf2_sha256.verify(password_entered, user_object.password):
        raise ValidationError("Username or password incorrect")

class RegistrationForm(FlaskForm):

    username = StringField('username_label', 
        validators=[InputRequired(message="username required"),
        Length(min=4, max=25, message='Username must be between 4 to 25 characters')])
    
    password = PasswordField('password_label', validators=[InputRequired(message="Password required"),
        Length(min=4, max=25, message='Password must be between 4 to 25 characters')])
    confirm_pswrd = PasswordField('confirm_pswrd_label', validators=[InputRequired(message="username required"),
        EqualTo('password', message="Password must match")])
    submit_button = SubmitField('Create')

    def validate_username(self, username):
        user_object = User.query.filter_by(username=username.data).first()
        if user_object:
            raise ValidationError("Username already exist!")

class LoginForm(FlaskForm):
    """Login form"""

    username = StringField('username_label', validators=[InputRequired(message="Username Required")])
    password = PasswordField('password_label', validators=[InputRequired(message="Password required"), invalid_credentials])

    submit_button = SubmitField('Login')        