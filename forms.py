from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, validators, FormField
from wtforms.validators import DataRequired, Email

class LoginForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])

class EmaiPasswordForm(FlaskForm):
    email = StringField('Emai', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
