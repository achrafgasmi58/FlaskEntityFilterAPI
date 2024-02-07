from flask import Flask
from flask_cors import CORS
from .config import Config
from .models import db
from .routes import bp

def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(Config)
    db.init_app(app)

    with app.app_context():
        db.create_all()

    app.register_blueprint(bp)

    return app
