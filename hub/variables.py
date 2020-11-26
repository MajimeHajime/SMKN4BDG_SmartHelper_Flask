import plotly
import plotly.express as px
import plotly.graph_objs as go
import pandas as pd
import numpy as np
import json
import pickle
from hub.PredictionModel import run_prediction
from datetime import date, timedelta, datetime

try:
    lastRun = pickle.load(open("day.pickle", "rb"))
except (OSError, IOError) as e:
    lastRun = date.today()
    pickle.dump(lastRun, open("day.pickle", "wb"))

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

if date.today() > lastRun :
    bar = create_plot()
    pickle.dump(bar, open("bar.pickle", "wb"))
else:
    try:
        bar = pickle.load(open("bar.pickle", "rb"))
    except (OSError, IOError) as e:
        bar = create_plot()
        pickle.dump(bar, open("bar.pickle", "wb"))
    pass
