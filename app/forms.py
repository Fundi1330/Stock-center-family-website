from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, SelectField, FileField
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
    name = StringField('Назва', validators=[DataRequired()])
    descreption = StringField('Опис', validators=[DataRequired()])
    price = StringField('Ціна', validators=[DataRequired()])
    size = StringField('Розмір', validators=[DataRequired()])
    matherial = StringField('Матеріал', validators=[DataRequired()])
    type = SelectField('Тип одягу', validators=[DataRequired()], choices=[('Жіночий', 'Жіночий'), ('Чоловічий', 'Чоловічий'), ('Дівчачий', 'Дівчачий'), ('Хлопчачий', 'Хлопчачий')])
    quantity = IntegerField('Кількість')
    in_stock = SelectField('В наявності', validators=[DataRequired()], choices=[('Так', 'Так'), ('Ні', 'Ні')])
    image = FileField('Зображення', validators=[DataRequired()])

    submit = SubmitField('Add good')
