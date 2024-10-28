from flask import Blueprint

# Blueprint para el sitio web

site_bp = Blueprint('site',__name__, url_prefix= '/')

@site_bp.route('/')
def index():
    return '<h1>Servidor arriba, estas en el index del sitio web</h1>'
