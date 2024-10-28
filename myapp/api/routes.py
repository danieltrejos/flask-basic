from flask import Blueprint

# Blueprint para la api del sitio web
api_bp = Blueprint('api', __name__,url_prefix='/api')

# Rutas del api

@api_bp.route('/getdata')
def getdata():
    # Simulación de un llamado a una API externa
    # Aquí debería ir el código para hacer el llamado a la API externa
    return {'message': 'Data retrieved successfully'}