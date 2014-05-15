from app import model

__author__ = 'Marcin'

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
app.config.from_envvar('GEOREPORT_SETTINGS', silent=True)
db = SQLAlchemy(app)

