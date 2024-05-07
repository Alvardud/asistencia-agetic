from flask import Flask, render_template, Blueprint

from routes.asistencia_bp import palabras_bp

app = Flask(__name__)
app.config.from_object('config')
app.config['JSON_AS_ASCII'] = False

#Registramos blueprint de API
api = Blueprint('API', __name__, url_prefix='/api')

#registramos sub grupos en api
api.register_blueprint(palabras_bp, url_prefix='/asistencia')

#registramos api a app
app.register_blueprint(api)


@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.debug = True
    app.run()
