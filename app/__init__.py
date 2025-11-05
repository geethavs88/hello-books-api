from flask import Flask
from .db import db, migrate
from .models import book
#from .routes.hello_world_routes import hello_world_bp
from .routes.book_routes import book_bp
import os

def create_app(config=None):
    app = Flask(__name__)
    app.register_blueprint(book_bp)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')
    if config:
        app.config.update(config)

    db.init_app(app)
    migrate.init_app(app, db)

    return app