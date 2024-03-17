from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SECRET_KEY'] = 'c7fbc86d44bc46d8862d7836'
db = SQLAlchemy(app)
bcrypt = Bcrypt()

from . import models

from . import routes
