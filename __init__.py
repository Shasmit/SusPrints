from os import path
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

from views import views
from auth import auth
from admin import admin


app.register_blueprint(views, url_prefix="/")
app.register_blueprint(auth, url_prefix="/")
app.register_blueprint(admin, url_prefix="/")

# from models import user


def create_database(app):
    if not path.exists(app.config["SQLALCHEMY_DATABASE_URI"]):
        db.create_all()

        print("create_database")


create_database(app)