from flask import Flask, redirect, url_for, render_template, request, jsonify
from datetime import datetime

app = Flask(__name__)

# Context processors
@app.context_processor
def date_now():
    return {
        'now': datetime.utcnow()
    }

# Endpoints
@app.route('/')
def index():
    edad=18
    personas=['Juan', 'Pedro', 'Lucas']
    return render_template('index.html', 
                            edad=edad,
                            data1='value1',
                            data2='value2',
                            lista=['uno', 'dos','tres'],
                            personas=personas)

@app.route('/contacto')
@app.route('/contacto/<redireccion>')
def contact(redireccion=None):
    if redireccion is not None:
        return redirect(url_for('lenguajes'))
    return render_template('contact.html')

@app.route('/informacion')
@app.route('/informacion/<string:nombre>')
@app.route('/informacion/<string:nombre>/<apellidos>')
def information(nombre=None, apellidos=None):
    texto = ""
    if nombre != None:
        texto = f"Bienvenido {nombre}"
    elif apellidos!=None:
        texto = f"Bienvenido {nombre} {apellidos}"
    else:
        texto = f"Bienvenido!"
    return render_template('information.html', texto=texto)


@app.route('/lenguajes-de-programacion')
def lenguajes():
    return "<h1>Languages page</h1>"


if __name__ == '__main__':
    app.run(debug=True)
