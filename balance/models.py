"""
Un movimiento debe tener:
1. Fecha
2. Concepto
3. Tipo (I=ingreso, G=gasto)
4. Cantidad
"""

import csv
from datetime import date, datetime

from . import FICHERO

class Movimiento:
    def __init__(self, dicc_datos):
        self.errores = []
        try:
            self.fecha = date.fromisoformat(dicc_datos["fecha"])
        except ValueError:
            self.fecha = None
            self.errores.append("El formato de la fecha no es válido")  
        
        self.concepto = dicc_datos["concepto"]
        self.tipo = dicc_datos["tipo"]
        self.cantidad = dicc_datos["cantidad"]

    def __str__(self):
        return "fecha: {} concepto: {} tipo: {} cantidad: {}".format(
            self.fecha,
            self.concepto,
            self.tipo,
            self.cantidad
        )


class ListaMovimientos:
    def __init__(self):
        self.movimientos = []

    def leer_archivo(self):
        with open(FICHERO, "r",encoding="UTF-8") as fichero:
            reader = csv.DictReader(fichero)
            for linea in reader:
                #self.lista_movimientos.append(linea) no nos vale
                mov = Movimiento (linea)
                
                self.movimientos.append(mov)



