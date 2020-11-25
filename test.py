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

'''
today = date.today()
todayish = today - timedelta(days=1)
yesterday = today - timedelta(days=2)
tomorrow = today + timedelta(days=1)
outaded = bool(0)
case = 0
casePast = 0
casePred = 0
change = 0

try:
    lastRun = pickle.load(open("day.pickle", "rb"))
except (OSError, IOError) as e:
    lastRun = today
    pickle.dump(lastRun, open("day.pickle", "wb"))
lastRun = lastRun

print(lastRun)
'''

df = pd.read_csv('testfile.csv')
today = date.today() - timedelta(days=1)
stats = int(df.loc[df['date'] == str(date.today() - timedelta(days=1)), 'total'])
print(stats)
