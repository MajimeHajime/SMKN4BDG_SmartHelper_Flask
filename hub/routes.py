from flask import render_template, url_for, flash, redirect, request
from hub import app, db, bcrypt
from hub.forms import RegistrationForm, LoginForm
from hub.models import User, Post
import pickle
from hub.variables import t_stat, y_stat, yoy_stat, p_stat, c_stat, c1_stat, news, news2, posts
from flask_login import login_user, current_user, logout_user, login_required


@app.route('/')
def front():
    return render_template(
        'frontpage.html',
        posts=posts,
        today=f'{t_stat:,}',
        predict=f'{p_stat:,}',
        change=f'{c_stat:,}',
        compare=f'{c1_stat:,}',
        news=news,
        news2=news2,
        )

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('front'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('front'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/stats')
def stats():
    sbar = pickle.load(open("bar.pickle", "rb"))
    return render_template(
        'stats.html',
        plot=sbar,
        today=f'{t_stat:,}',
        predict=f'{p_stat:,}',
        change=f'{c_stat:,}',
        compare=f'{c1_stat:,}',
        news=news,
        news2=news2,
        title='Stats'
        )

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route("/account")
@login_required
def account():
    return render_template('account.html', title='Account')