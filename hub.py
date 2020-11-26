from flask import Flask, render_template, url_for, flash, redirect
from PredictionModel import run_prediction
from datetime import date, timedelta
from forms import RegistrationForm, LoginForm
import plotly
import plotly.express as px
import plotly.graph_objs as go
import pandas as pd
import numpy as np
import json
import pickle


app = Flask(__name__)
app.config['SECRET_KEY'] = '51c11bd0792105993631f9e22095b5f8'

posts = [
    {
        'author': 'Arudo',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'WHWHW',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]

try:
    lastRun = pickle.load(open("day.pickle", "rb"))
except (OSError, IOError) as e:
    lastRun = date.today()
    pickle.dump(lastRun, open("day.pickle", "wb"))
lastRun = lastRun

if date.today() > lastRun :
    run_prediction()
    flastRun = date.today()
    pickle.dump(flastRun, open("day.pickle", "wb"))
else:
    pass

df = pd.read_csv('testfile.csv')
t_stat = int(df.loc[df['SN'] == df['total'].notna()[::-1].idxmax() + 1, 'total'])
y_stat = int(df.loc[df['SN'] == df['total'].notna()[::-1].idxmax(), 'total'])
yoy_stat = int(df.loc[df['SN'] == df['total'].notna()[::-1].idxmax() - 1, 'total'])
p_stat = int(df.loc[df['SN'] == df['total'].notna()[::-1].idxmax() + 7, 'y_fut'])
c_stat = t_stat - y_stat 
c1_stat = y_stat - yoy_stat
news = c_stat - c1_stat
news2 = p_stat - t_stat


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
    bar = create_plot()
    return render_template(
        'stats.html',
        plot=bar,
        today=f'{t_stat:,}',
        predict=f'{p_stat:,}',
        change=f'{c_stat:,}',
        compare=f'{c1_stat:,}',
        news=news,
        news2=news2,
        title='Stats'
        )

def create_plot():
    df = pd.read_csv('testfile.csv')
    fig = go.Figure(layout_title_text=" ")
    fig.add_trace(go.Scatter(x=df["date"], y=df['predicted'], name="Past Prediction", line = dict(color='#2AA965', width=2)))
    fig.add_bar(x=df["date"], y=df["total"], name="Total Cases")
    fig.add_trace(go.Scatter(x=df["date"], y=df['y_fut'], name="Future Prediction", line = dict(color='#CC252C', width=2, dash='dot')))
    fig.update_traces(marker_color='#cbcbcb')
    fig.layout.update(
        showlegend=False,
        yaxis_title=" ",
        xaxis_title=" ", 
        title_font_family="SF Pro Display Semibold",
        title_font_color="#1f1f1f",
        legend_title_font_color="green",
        font_family="SF Pro Display Semibold",
        font_color="#1f1f1f",
        margin=dict(l=20, r=20, t=23, b=20),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='#E1E1E1'
        )
    data = fig
    graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON

if __name__ == '__main__':
    app.run(debug=True)

#  ++=========================================++
#  || KKSI AI - SMKN 4 Bandung - Smart Helper ||
#  ||-----------------------------------------||
#  ||   Pembina:                              ||
#  ||       Ibu Tyas                          ||
#  ||   Anggota(Berdasarkan Alphabet):        ||
#  ||       Aldo Fakhry                       ||
#  ||       Firdaus Haqiqi                    ||
#  ||       Muhammad Azmi                     ||
#  ||-----------------------------------------||
#  ||   Terimakasih Pada:                     ||
#  ||       # Sentdex                         ||
#  ||       # Pandas Documentation            ||
#  ||       # Diwas Padley                    ||
#  ||       # Stack Overflow                  ||
#  ||       # Our World In Data               ||
#  ++=========================================++