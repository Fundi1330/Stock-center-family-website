from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo
from app.models import User
from flask import flash


"""Форми на сайті"""
class LoginForm(FlaskForm):
    username = StringField('Псевдонім', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField("Запам'ятати мене")
    submit = SubmitField('Ввійти')


class RegestrationForm(FlaskForm):
    username = StringField("Псевдонім", validators=[DataRequired()])
    email = StringField('Електронна адрессу', validators=[DataRequired(), Email()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    confirm_password = PasswordField('Підтвердити пароль', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Зареєструватися')
    
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            flash("Використовуйте інший Псевдонім")

    def validate_username(self, email):
        email = User.query.filter_by(email=email.data).first()
        if email is not None:
            flash('Використовуйте іншиу електронну адрессу')


class AddGoodForm(FlaskForm):
    name = StringField('Good name', validators=[DataRequired()])
    descreption = StringField('Good descreption', validators=[DataRequired()])
    price = StringField('Good price', validators=[DataRequired()])
    size = StringField('Size')
    matherial = StringField('Matherial')
    submit = SubmitField('Add good')
