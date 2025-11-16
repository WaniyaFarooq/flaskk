from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class RegistrationForm(FlaskForm):
    name = StringField("Name", validators =[DataRequired()])
    email = StringField("Email" , validators = [Email(), DataRequired()])
    password = PasswordField("Password",validators=[DataRequired(),Length(min=9,max=16)])
    submit = SubmitField("Register")

