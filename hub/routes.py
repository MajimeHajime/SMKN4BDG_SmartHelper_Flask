from flask import render_template, url_for, flash, redirect
from hub import app
from hub.forms import RegistrationForm, LoginForm
from hub.models import User, Post
import pickle
from hub.variables import t_stat, y_stat, yoy_stat, p_stat, c_stat, c1_stat, news, news2, posts

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
    form=LoginForm()
    if form.validate_on_submit():
        if form.validate_on_submit():
            if form.email.data == 'admin@blog.com' and form.password.data == 'password':
                flash('You have been logged in!', 'success')
                return redirect(url_for('front'))
            else:
                flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template(
        'login.html',
        title='Login',
        form=form
        )
@app.route('/register', methods=['GET', 'POST'])
def register():
    form=RegistrationForm()
    if form.validate_on_submit():
        flash(
            f'Account created for {form.username.data}!', 
            'success'
            )
        return redirect(
            url_for(
                'login'
                )
            )
    return render_template(
        'register.html',
        title='Register',
        form=form
        )

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

