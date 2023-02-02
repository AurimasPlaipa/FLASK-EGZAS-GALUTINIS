from flask_login import current_user
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, DateField, TextAreaField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, EqualTo, Email, ValidationError
from wtforms_sqlalchemy.fields import QuerySelectField, QuerySelectMultipleField
from app.models.User import User




class RegisterForm(FlaskForm):
  FullName = StringField('Vardas Pavardė', [DataRequired()])
  email = StringField('El. paštas', [DataRequired(), Email()])
  password = PasswordField('Slaptažodis', [DataRequired()])
  repeat_password = PasswordField("Pakartokite slaptažodį", [EqualTo('password', "Slaptažodis turi sutapti.")])

  def check_email(self, email):
    user = User.query.filter_by(email=email.data).first()
    if user:
      raise ValidationError('Šis el. pašto adresas panaudotas. Pasirinkite kitą.')


class LoginForm(FlaskForm):
  email = StringField('El. paštas', [DataRequired(), Email()])
  password = PasswordField('Slaptažodis', [DataRequired()])
  remember = BooleanField('Prisiminti')

class AddGroupForm(FlaskForm):
  ID = StringField('Naujas ID', [DataRequired()])

class AddBillForm(FlaskForm):
  Amount = StringField('Nauja sąskaita', [DataRequired()])
  Description = StringField('Naujas priskyrimas', [DataRequired()])

class UserRequestResetPasswordForm(FlaskForm):
    email = StringField('El. paštas', [DataRequired(), Email()])


class UserResetPasswordForm(FlaskForm):
    password = PasswordField('Slaptažodis', [DataRequired()])
    confirm_password = PasswordField("Pakartokite slaptažodį", [EqualTo('password', "Slaptažodis turi sutapti.")])
