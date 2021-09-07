from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validations import InputRequiered, Email


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[InputRequiered(), Email()])
    password = PasswordField('Password', validators=[InputRequiered()])
    submit = SubmitField('Login')
