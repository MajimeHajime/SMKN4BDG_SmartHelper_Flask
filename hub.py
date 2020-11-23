from flask import Flask, render_template, url_for
from PredictionModel import run_prediction
from datetime import date
import plotly
import plotly.express as px
import plotly.graph_objs as go
import pandas as pd
import numpy as np
import json
import pickle


app = Flask(__name__)

today = date.today()
outaded = bool(0)
try:
    lastRun = pickle.load(open("day.pickle", "rb"))
except (OSError, IOError) as e:
    lastRun = today
    pickle.dump(lastRun, open("day.pickle", "wb"))


@app.route('/')
def front():
    return render_template(
        'frontpage.html'
        )

@app.route('/stats')
def stats():
    check_day()
    if outaded:
        run_prediction()
    else:
        pass
    bar = create_plot()
    return render_template(
        'stats.html',
        plot=bar
        )

def check_day():
    if today == lastRun :
        outaded = bool(0)
        return outaded
    elif today > lastRun :
        outaded = bool(1)
        return outaded
    else:
        pass

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