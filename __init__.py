from flask import Flask
from config import Config
from views import views
from auth import auth
from os import path
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager



app=Flask(__name__)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
# login_manager.login_view = 'auth.login'

app.config.from_object(Config)

app.register_blueprint(views, url_prefix='/')
app.register_blueprint(auth, url_prefix='/')

def create_database(app):
    if not path.exists(app.config['SQLALCHEMY_DATABASE_URI']):
        db.create_all()
        print('Database created')

create_database(app)
