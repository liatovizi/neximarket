from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import psycopg2
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:****@localhost/market'
app.config['SECRET_KEY'] ='0x00000223826CFD80'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
conn = psycopg2.connect(host='localhost', dbname='market', user='postgres', password='*****', port=5432)
cur = conn.cursor()
#
login_manager = LoginManager(app)
login_manager.login_view = "login_page"
login_manager.login_message_category = "info"

from market import routers