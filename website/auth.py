from flask import Blueprint, render_template, request, flash, redirect, url_for, render_template_string
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db, mail
from flask_login import login_user, login_required, current_user, logout_user
from flask_mail import Message
from .reset_password_email_content import reset_password_email_html_content


auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again', category='error')
        else:
            flash('User does not exist', category='error')
    return render_template('login.html', user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('views.home'))

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        username = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        check_email = User.query.filter_by(email=email).first()
        check_user = User.query.filter_by(username=username).first()
        if check_email:
            flash('Email already in use', category='error')
        elif check_user:
            flash('Username already in use', category='error')
        elif email[len(email)-7::] != '@bu.edu':
            flash('Must be a Boston University email', category='error')
        elif password1 != password2:
            flash('Both passwords must match', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters', category='error')
        else:
            new_user = User(email=email, username=username, password=generate_password_hash(password1, method='pbkdf2'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account created!', category='success')
            return redirect(url_for('views.home'))
    return render_template('sign_up.html', user=current_user)

@auth.route('/forgot', methods=['POST', 'GET'])
def forgot():
    if request.method == 'POST':
        email = request.form.get('email')
        user = User.query.filter_by(email=email).first()
        if user:
            send_mail(user)
            flash('Verification code has been sent to your email', category='success')
        else:
            flash('No user found with that email', category='error')
    return render_template('forgot.html', user=current_user)

def send_mail(user):
    reset_password_url = url_for("auth.change_password", token=User.generate_token(user.email, user.password), user_id=user.id, _external=True)
    email_body = render_template_string(reset_password_email_html_content, reset_password_url=reset_password_url)
    message = Message(subject="Reset your password", recipients=[user.email], html=email_body)
    mail.send(message)

@auth.route('/change-password/<token>/<int:user_id>', methods=['POST', 'GET'])
def change_password(token, user_id):
    if request.method == 'POST':
        user = User.validate_reset_password_token(token, user_id)
        if not user:
            flash('Password change error', category='error')
            return redirect(url_for('auth.login'))
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        if password1 != password2:
            flash('Passwords must match', category='error')
        else:
            user.password = generate_password_hash(password1, method='pbkdf2')
            db.session.commit()
            flash('Password successfully changed!', category='success')
            return redirect(url_for('auth.login'))
    return render_template('change_password.html', user=current_user)