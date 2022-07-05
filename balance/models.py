"""
Un movimiento debe tener:
1. Fecha
2. Concepto
3. Tipo (I=ingreso, G=gasto)
4. Cantidad
"""

import csv
from datetime import datetime

from . import FICHERO

class Movimiento:
    def __init__(self, fecha, concepto, tipo, cantidad):
        self.fecha = fecha
        self.concepto = concepto
        self.tipo = tipo
        self.cantidad = cantidad


class ListaMovimientos:
    def __init__(self):
        self.movimientos = []

    def leer_archivo(self):
        with open(FICHERO, "r",encoding="UTF-8") as fichero:
            reader = csv.DictReader(fichero)
            for linea in reader:
                #self.lista_movimientos.append(linea) no nos vale
                mov = Movimiento (
                    linea["fecha"], linea["concepto"],
                    linea["tipo"], linea["cantidad"]
                    )
                self.movimientos.append(mov)



