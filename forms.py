from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length

class LoginForm(FlaskForm):
    # LOG IN FIELDS 
    username = StringField("Username", validators=
                [DataRequired(), Length(min=20, max=120)])
    password = PasswordField("Password", validators=
                [DataRequired(), Length(min=3, max=120)])
    button = SubmitField("LOG IN")

class RegisterForm(FlaskForm):
    firstname = StringField("Firstname", validators=
                [DataRequired(), Length(min=20, max=120)])
    secondname = PasswordField("Secondname", validators=
                [Length(min=3, max=120)])
    lastname = PasswordField("Lastname", validators=
                [DataRequired(), Length(min=3, max=120)])
    
    button = SubmitField("ADD TEACHER")

