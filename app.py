from flask import Flask
from routes.Inscription import inscrire_bp
from routes.Connecter import connecter_bp
import database

def creat_app():
    app = Flask(__name__)
    app.secret_key = "med_ffffff_1234"
    app.config.update(
    SESSION_COOKIE_SAMESITE="Lax",  
    SESSION_COOKIE_SECURE=False   
    )


    app.register_blueprint(inscrire_bp)
    app.register_blueprint(connecter_bp)

    return app