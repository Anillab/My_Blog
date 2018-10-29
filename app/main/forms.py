from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,PasswordField
from wtforms.validators import DataRequired,Length,Email,EqualTo
class RegistrationForm(FlaskForm):
    username=StringField('Username',validators=[DataRequired()])
    email=StringField('Email Address',validators=[DataRequired(),Email()])
    password=PasswordField('New Password',validators=[DataRequired(),EqualTo('Confirm',message='Passwords must match')])
    confirm=PasswordField('Repeat Password')
    submit=SubmitField('submit')

class LoginForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired(),Length(min=2,max=20)])
    email = StringField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')
