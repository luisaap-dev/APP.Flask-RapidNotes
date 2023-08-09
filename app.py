from flask import Flask  # Importar la clase Flask del módulo flask
from controllers.controller import Controller  # Importar la clase Controller del módulo controllers.controller

app = Flask(__name__)  # Crear una instancia de la clase Flask y asignarla a la variable "app"
controller = Controller()  # Crear una instancia de la clase Controller y asignarla a la variable "controller"

@app.route('/', methods=['GET', 'POST'])
def index():
    return controller.index()

@app.route('/nota/<codigo>', methods=['GET'])
def nota(codigo):
    return controller.nota(codigo)

@app.route('/notas', methods=['GET'])
def lista_notas():
    return controller.lista_notas()

@app.errorhandler(404)
def pagina_no_encontrada(error):
    return controller.pagina_no_encontrada(error)

if __name__ == '__main__':
    app.run()
