from flask import Flask

from flask_sqlalchemy import SQLAlchemy 

from os import getenv

import pymysql

from flask_bcrypt import Bcrypt

from flask_login import LoginManager

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = ('mysql+pymysql://' + getenv('MY_SQL_USER') + ':' + getenv('MY_SQL_PASSWORD') + '@' + getenv('MY_SQL_URL') + '/' + getenv('MY_SQL_DB'))
app.config['SECRET_KEY'] = getenv('SECRET_KEY')

db = SQLAlchemy(app)

bcrypt = Bcrypt(app)

login_manager = LoginManager(app)

login_manager.login_view = 'login'

from application import routes
