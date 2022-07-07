from flask import render_template, request

from balance import app
from . models import ListaMovimientos, Movimiento


@app.route("/")
def home():
    movimientos = ListaMovimientos()
    movimientos.leer_archivo()
    return render_template("inicio.html", movs=movimientos.movimientos)

@app.route("/nuevo", methods=["GET", "POST"])
def nuevo():
    if request.method == "GET":
        return render_template("nuevo.html")
    else:
        datos = request.form
        nuevo_movimiento = Movimiento(datos)
        if len(nuevo_movimiento.errores) > 0:
            return f"Error en el nuevo movimiento. {nuevo_movimiento.errores}"
        return f"He recibido los datos: {nuevo_movimiento}"

@app.route("/modificar")
def modificar():
    return "Actualizar movimiento"

@app.route("/borrar")
def borrar():
    return "Borrar movimiento"