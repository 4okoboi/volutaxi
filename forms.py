from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, RadioField, DateField, TimeField, Field
from wtforms.validators import DataRequired, InputRequired, Optional


class AdminLoginForm(FlaskForm):
    username = StringField('Логин', validators=[DataRequired()], id='username')
    password = PasswordField('Пароль', validators=[DataRequired()], id='password')
    submit = SubmitField('Войти')


class UserLoginForm(FlaskForm):
    username = StringField('Логин', validators=[DataRequired()], id='username')
    password = PasswordField('Пароль', validators=[DataRequired()], id='password')
    submit = SubmitField('Войти')


class UserRegForm(FlaskForm):
    username = StringField('Логин', validators=[DataRequired()], id='username')
    password = StringField('Пароль', validators=[DataRequired()], id='password')
    name = StringField('Имя', validators=[DataRequired()], id='name')
    lastname = StringField('Фамилия', validators=[DataRequired()], id='lastname')
    patronymic = StringField('Отчество', validators=[DataRequired()], id='patronymic')
    date_of_birth = StringField('Дата рождения в формате ДД.ММ.ГГГГ', validators=[DataRequired()], id='date_of_birth')
    phone_number = StringField('Номер телефона', validators=[DataRequired()], id='phone_number')
    submit = SubmitField('Зарегистрироваться')


class TripDriverAddForm(FlaskForm):
    deadline_date = StringField('Дедлайн число', validators=[DataRequired()], id='deadline_date')
    deadline_time = StringField('Дедлайн время', validators=[DataRequired()], id='deadline_time')
    from_place = StringField('Откуда', validators=[DataRequired()], id='from_place')
    to_place = StringField('Куда', validators=[DataRequired()], id='to_place')
    places = StringField('Количество мест', validators=[DataRequired()], id='places')
    submit = SubmitField('Создать')

# class UserSettingsForm(FlaskForm):
#     name = StringField('Измените имя', validators=[DataRequired()], id='changed_name')
#     number = StringField('Измените номер', validators=[DataRequired()], id='changed_number')
#     submit = SubmitField('Изменить')


# 'active': 'true',
#                 'date': form.deadline_date.data,
#                 'driver': session['name'],
#                 'driverId': session['userId'],
#                 'from': form.from_place.data,
#                 'number': session['number'],
#                 'places': form.places.data,
#                 'time': form.deadline_time.data,
#                 'to': form.to_place.data
