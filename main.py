# main.py
# Servidor Flask para generar un menú recursivo dinámico
from flask import Flask, render_template

app = Flask(__name__)

# Estructura de navegación para ITM Minatitlán
nav_structure = {
    'Inicio': {},
    'Oferta Académica': {
        'Modalidad Presencial': {
            'Licenciatura en Administración': {},
            'Ingeniería Ambiental': {},
            'Ingeniería Electromecánica': {},
            'Ingeniería Electrónica': {},
            'Ingeniería Industrial': {},
            'Ingeniería Química': {},
            'Ingeniería en Gestión Empresarial': {},
            'Ingeniería en Sistemas Computacionales': {},
            'Ingeniería en Inteligencia Artificial': {},
            'Ingeniería en Desarrollo de Software': {}
        },
        'Modalidad a Distancia': {
            'Ingeniería Industrial': {}
        },
        'Posgrado': {
            'Maestría en Ingeniería Electrónica': {}
        },
        'Idiomas': {}
    },
    'Contacto': {}
}

@app.route('/')
def home():
    # Loguea en consola la estructura para verificarla
    print('Nav structure:', nav_structure)
    return render_template(
        'menu.html',
        nav=nav_structure,
        page_title='ITM Minatitlán Navigator'
    )

if __name__ == '__main__':
    # Ejecuta en modo debug para recarga automática
    app.run(debug=True)
