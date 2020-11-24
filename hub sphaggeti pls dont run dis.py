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

# global outdated << somehow gak recognize sm function
today = date.today()
todayish = today - timedelta(days=1)
yesterday = today - timedelta(days=2)
tomorrow = today + timedelta(days=1)
outdated = bool(0)
case = 0
casePast = 0
casePred = 0
change = 0
# global lastRun << doesn't work fak

try:
    lastRun = pickle.load(open("day.pickle", "rb"))
except (OSError, IOError) as e:
    flastRun = today
    pickle.dump(lastRun, open("day.pickle", "wb"))
lastRun = lastRun

@app.route('/')
def front():
    return render_template(
        'frontpage.html'
        )

@app.route('/stats')
def stats():
    # FIX CODE BELOW
    #check_day() << python why u do dis to my variable
    #return outdated << temporary fix that doesnt work
    #if outdated: << 'not declared' why?
    #    run_prediction()
    #    outdated = bool(0)
    #else:
        #pass
    # FIXX THE UPPER CODE

    #TEMPORARY FIX
    if today > lastRun :
        run_prediction()
        flastRun = today
        pickle.dump(flastRun, open("day.pickle", "wb"))
    else:
        pass
    #UPPER CODE IS VERY BEEG AND NOT GOOD
    bar = create_plot()
    stats = [today_case()]
    return render_template(
        'stats.html',
        today=todayish,
        plot=bar,
        stat=stats
        )

def create_plot():
    global df 
    df = pd.read_csv('testfile.csv')
    fig = px.line(df, x="date", y="predicted", color=px.Constant("Prediction"))
    fig.add_bar(x=df["date"], y=df["total"], name="Total Cases")
    fig.add_trace(go.Scatter(x=df["date"], y=df['y_fut'], name="Future Prediction", mode='lines+markers'))
    data = fig
    graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON

def check_day():
    flastRun = lastRun
    if today == flastRun :
        outdated = bool(0)
        return outdated
    elif today > flastRun :
        outdated = bool(1) 
        flastRun = today
        pickle.dump(flastRun, open("day.pickle", "wb"))
        return outdated
    else:
        pass


def today_case():
    case = df.loc[df["date"] == todayish, "total"]
    casePast = df.loc[df["date"] == yesterday, "total"]
    casePred = df.loc[df["date"] == tomorrow, "y_fut"]
    change = case - casePred
    global stats
    stats = [case,casePred,casePast]
    return stats


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