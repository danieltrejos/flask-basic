from flask import Flask

from .site.routes import site_bp
from .api.routes import api_bp


# Funcion para crear la app inciada por run.py aqui se deben cargar las configuracions
def create_app():
    # Instancia del objeto Flask
    app = Flask(__name__)

    # Registro de blueprints
    app.register_blueprint(site_bp)
    app.register_blueprint(api_bp)

    return app