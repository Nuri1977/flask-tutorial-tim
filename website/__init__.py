from os import getenv
from flask import Flask
from .views import views
from .auth import auth
from .models import User, Note
from .extensions import db, setup_custom_json_encoder, migrate, jwt
from dotenv import load_dotenv
from flask_login import LoginManager
from dotenv import load_dotenv

import json
import os

def parse_json_filter(json_string):
    return json.loads(json_string)

def create_app():
    load_dotenv()
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
    app.jinja_env.filters['parse_json'] = parse_json_filter
    # Injecting customized json encoder for solving serialization issues with following types:
    #  * Decimal
    #  * Date
    #  * DateTime
    setup_custom_json_encoder()

    # Initialize Flask extensions here
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")


    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app
