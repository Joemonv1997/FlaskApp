from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
class Register(FlaskForm):
    user=StringField(label="Username")
    email=StringField(label="Email Address")
    passw=PasswordField(label="Passwords")
    submit=SubmitField(label="Create Account")

class Login(FlaskForm):
    email=StringField(label="Email Address")
    passw=PasswordField(label="Passwords")
    submit=SubmitField(label="Create Account")