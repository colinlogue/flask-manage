from flask import Flask
from flask_manage.core import register_modules




def create_app():
    app = Flask(__name__)
    register_modules(app)
    return app