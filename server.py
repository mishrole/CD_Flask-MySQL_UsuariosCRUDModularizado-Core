from users_app import app
# Importante importar para cargar las rutas
from users_app.controllers import usersController

if __name__ == '__main__':
    app.run( debug = True )