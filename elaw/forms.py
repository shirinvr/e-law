from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from elaw.models import *
# from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms import SelectField

# class LoginForm(FlaskForm):
#     username = StringField('Username',validators=[DataRequired(), Email()])
#     password = PasswordField('Password', validators=[DataRequired()])
#     submit = SubmitField('Login') 


# class BoatForm(FlaskForm):
#     boat_owner = StringField('Name',validators=[DataRequired()])
#     boat_name = StringField('Boat',validators=[DataRequired()])
#     boat_no = StringField('Boat Number', validators=[DataRequired()])
#     image = FileField('Upload Photo', validators=[FileAllowed(['jpg', 'png','jpeg'])])
#     type = StringField('Type', validators=[DataRequired()])
#     nor = StringField('Rooms', validators=[DataRequired()])
#     price = StringField('Amount', validators=[DataRequired()])
#     contact = StringField('Contact', validators=[DataRequired()])
#     email = StringField('Email', validators=[DataRequired()])
#     password = PasswordField('Password', validators=[DataRequired()])
#     submit = SubmitField('Submit')