import jwt
from flask import flash, redirect, render_template, request, url_for
from flask_login import current_user, login_user, logout_user, login_required
from app import app, db, login_manager, bcrypt
from app.forms import (RegisterForm, LoginForm, AddGroupForm, AddBillForm, UserRequestResetPasswordForm,
    UserResetPasswordForm)

from app.models.id import Group_ID, Amount, Description
from app.models.User import User




@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('login'))
    form = RegisterForm()
    if request.method == 'POST' and form.validate_on_submit():
        encrypted_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(email=form.email.data, password=encrypted_password)
        db.session.add(user)
        db.session.commit()
        flash('Sėkmingai prisiregistravote! Galite prisijungti', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('login'))
    form = LoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            flash('Sėkmingai prisijungėte!', 'success')
            return redirect(url_for('login'))
        else:
            flash('Prisijungti nepavyko. Patikrinkite el. paštą ir slaptažodį', 'danger')
    return render_template('login.html', form=form)


@app.route("/request-reset-password", methods=['GET', 'POST'])
def request_reset_password():
    if current_user.is_authenticated:
        return redirect(url_for('login'))
    form = UserRequestResetPasswordForm()
    if request.method == 'POST' and form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()


@app.route("/reset-password", methods=['GET', 'POST'])
def reset_password():
    if current_user.is_authenticated:
        return redirect(url_for('login'))
    token = request.args.get('token', '', type=str)
    try:
        payload = jwt.decode(token, app.config['SECRET_KEY'], algorithms="HS256")
        user = User.query.get(payload['user_id'])
        form = UserResetPasswordForm()
        if user and request.method == 'POST' and form.validate_on_submit():
            encrypted_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
            user.password = encrypted_password
            db.session.add(user)
            db.session.commit()
            flash('Slaptažodis atstatytas sėkmingai! Galite prisijungti', 'success')
            return redirect(url_for('login'))
        return render_template('reset_password.html', form=form, token=token)
    except jwt.InvalidSignatureError:
        flash('Klaida arba pasibaigusi nuoroda', 'danger')
        return redirect(url_for('login'))
    except jwt.ExpiredSignatureError:
        flash('Klaida arba pasibaigusi nuoroda', 'danger')
        return redirect(url_for('login'))


@app.route("/logout", methods=['GET', 'POST'])
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/groups')
def about():
    return render_template('groups.html')


@app.route('/bills')
def services():
    return render_template('bills.html')



@app.errorhandler(401)
def unauthorized(error):
    return render_template('unauthorized.html'), 401


@app.errorhandler(404)
def not_found(error):
    return render_template('not_found.html'), 404


@app.errorhandler(500)
def server_error(error):
    return render_template('server_error.html'), 500
