# from db_repository.db_connection import cred
from flask import Flask, render_template, redirect, request, url_for, flash, make_response, session
from forms import *
from db_repository.db import db_auth, database
from math import ceil
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hacktaxi_secret_key'
ADMIN_FLAG = False
USER_FLAG = False
DRIVER_FLAG = False
LOGIN = {'id': '',
         'name': '',
         'login': '',
         'number': ''}


@app.route('/')
@app.route('/main')
def main():
    data = dict(database.child('Roads').get().val())
    keys = list(dict(data).keys())
    amount = len(keys)
    row_amount = ceil(len(keys) / 4)
    return render_template('index.html', session=session, data=data, keys=keys, row_amount=row_amount, amount=amount)


@app.route('/admin_page')
def admin_page():
    if ADMIN_FLAG:
        return "Admin Page"
    else:
        return redirect('/admin_auth')


@app.route('/admin_auth', methods=['GET', 'POST'])
def admin_auth():
    form = AdminLoginForm()
    if form.validate_on_submit():
        global ADMIN_FLAG
        ADMIN_FLAG = True
        return redirect('/admin_page')
    return render_template('admin_auth.html', title='Авторизация админа', form=form)


@app.route('/auth', methods=['GET', 'POST'])
def auth():
    form = UserLoginForm()
    if form.validate_on_submit():
        login = form.username.data
        passwd = form.password.data
        try:
            user = db_auth.sign_in_with_email_and_password(login + "@gmail.com", passwd)
            data = dict(database.child('Users').child(user['localId']).get().val())
            session['username'] = data[list(data.keys())[0]]['username']
            session['name'] = data[list(data.keys())[0]]['name']
            session['number'] = data[list(data.keys())[0]]['number']
            session['userId'] = user['localId']
            print(session['username'], session['name'], session['number'], session['userId'])
        except Exception as _ex:
            print(type(_ex))
            return render_template('auth.html', title='Авторизация', form=form, error='Вы ввели неверные данные')
        return redirect('/')
    return render_template('auth.html', title='Авторизация', form=form)


@app.route('/user_reg', methods=['GET', 'POST'])
def user_reg():
    try:
        if "userId" in session:
            return redirect('/')
        else:
            pass
    except Exception as _ex:
        pass

    form = UserRegForm()
    if form.validate_on_submit():
        login = form.username.data
        passwd = form.password.data
        b_day = form.date_of_birth.data
        name = form.name.data
        number = form.phone_number.data
        patronymic = form.patronymic.data
        second_name = form.lastname.data
        username = form.username.data
        try:
            session['username'] = username
            user = db_auth.create_user_with_email_and_password(login + "@gmail.com", passwd)
            session['userId'] = user['localId']
            session['name'] = name
            session['number'] = number
            user_info = {"b_day": b_day, "name": name, "number": number, "patronymic": patronymic,
                         "secondName": second_name, "userId": user['localId'], "username": username}
            result = database.child("Users").child(user['localId']).push(user_info)
            print(result, session['username'], session['userId'])
        except Exception as _ex:
            print(_ex)
            return render_template('user_reg.html', title='Регистрация пользователя', form=form)
        return redirect('/')
    return render_template('user_reg.html', title='Регистрация пользователя', form=form)


@app.route('/account')
def account():
    data = dict(database.child('Roads').get().val())
    keys = list(dict(data).keys())
    keys_user = []
    print(keys)
    for i in keys:
        if data[i]['driverId'] == session['userId']:
            keys_user.append(i)
    row_amount = ceil(len(keys_user) / 4)
    amount = len(keys_user)
    return render_template('index.html', session=session, data=data, keys=keys_user, row_amount=row_amount,
                           amount=amount)


@app.route('/add_trip', methods=['GET', 'POST'])
def add_trip():
    form = TripDriverAddForm()
    if form.validate_on_submit():
        # print(session['username'], session['userId'], session['number'])
        print(session.keys())
        road_info = {'active': 'true', 'date': str(form.deadline_date.data), 'driver': session['name'],
                     'driverId': session['userId'], 'from': form.from_place.data,
                     'number': session['number'],
                     'places': form.places.data, 'time': str(form.deadline_time.data), 'to': form.to_place.data}
        result = database.child('Roads').push(road_info)
        print(result)
    return render_template('trip_add_driver.html', title='Регистрация пользователя', form=form)
#
# @app.route('/user_settings'):
# def user_settings():
#     pass


@app.route('/about')
def about():
    return 'Страница о нас'


if __name__ == "__main__":
    app.run(debug=True, port=2000)
