from flask import Flask


"""
Para ejecutar la app Flask necesitamos un servidor web.
Flask proporciona uno para desarrollo, pero necesitamos
un par de variables de entorno.

-Linux/Mac
    export FLASK_APP=hello (hello es el nombre del archivo sin extensión)
    export FLASK_APP=develoment (puede ser también "production")

-Windows
    set FLASK_APP=hello
    set FLASK_ENV=develoment    
"""
app = Flask(__name__)


@app.route("/")
def hola():
    return "Hola, soy Flask, ¿y tú?"


@app.route("/adiós")
def otra():
    return "Hasta luego!!"
