from flask import Flask

from flask_sqlalchemy import SQLAlchemy 

from os import getenv

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = ('mysql+pymysql://' + getenv('MY_SQL_USER') + ':' + getenv('MY_SQL_PASSWORD') + '@' + getenv('MY_SQL_URL') + '/' + getenv('MY_SQL_DB'))
app.config['SECRET_KEY'] = getenv('SECRET_KEY')

db = SQLAlchemy(app)



from application import routes
