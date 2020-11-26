from flask import Flask, render_template, url_for, flash, redirect
from hub.PredictionModel import run_prediction
from datetime import date, timedelta, datetime
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '51c11bd0792105993631f9e22095b5f8'
db = SQLAlchemy(app)

from hub import routes
