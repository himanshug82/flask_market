# save this as app.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SECRET_KEY'] = '1fc41cf3e00487b11312c925'
db = SQLAlchemy(app)

from market import routes
from market import models
