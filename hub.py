from flask import Flask, render_template, url_for
from PredictionModel import run_prediction
from datetime import date, timedelta
import plotly
import plotly.express as px
import plotly.graph_objs as go
import pandas as pd
import numpy as np
import json
import pickle


app = Flask(__name__)

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


@app.route('/')
def front():
    return render_template(
        'frontpage.html'
        )

@app.route('/stats')
def stats():
    df = pd.read_csv('testfile.csv')
    t_stat = int(df.loc[df['date'] == str(date.today() - timedelta(days=1)), 'total'])
    y_stat = int(df.loc[df['date'] == str(date.today() - timedelta(days=2)), 'total'])
    p_stat = int(df.loc[df['date'] == str(date.today() + timedelta(days=7)), 'y_fut'])
    c_stat = t_stat - y_stat 

    bar = create_plot()
    return render_template(
        'stats.html',
        plot=bar,
        today=t_stat,
        predict=p_stat,
        change=c_stat
        )

def create_plot():
    df = pd.read_csv('testfile.csv')
    fig = px.line(df, x="date", y="predicted", color=px.Constant("Prediction"))
    fig.add_bar(x=df["date"], y=df["total"], name="Total Cases")
    fig.add_trace(go.Scatter(x=df["date"], y=df['y_fut'], name="Future Prediction", mode='lines+markers'))
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