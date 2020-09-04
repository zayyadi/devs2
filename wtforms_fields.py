from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, EqualTo

class RegistrationForm(FlaskForm):

    username = StringField('username_label', 
        validators=[InputRequired(message="username required"),
        Length(min=4, max=25, message='Username must be between 4 to 25 characters')])
    
    password = PasswordField('password_label', validators=[InputRequired(message="Password required"),
        Length(min=4, max=25, message='Password must be between 4 to 25 characters')])
    confirm_pswrd = PasswordField('confirm_pswrd_label', validators=[InputRequired(message="username required"),
        EqualTo('password', message="Password must match")])
    submit_button = SubmitField('Create')