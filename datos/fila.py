from celda import Celda

class Fila():
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.cuenta = 0

    def vacia(self):
        return self.primero == None

    def agregarFinal(self, dato, x, y):
        if self.vacia():
            self.primero = self.ultimo = Celda(dato, x, y)
        else:
            aux = self.ultimo
            self.ultimo = aux.siguiente = Celda(dato, x , y)
            self.ultimo.anterior = aux
        self.cuenta += 1

    def agregarInicio(self, dato, x, y):
        if self.vacia():
            self.primero = self.ultimo = Celda(dato, x, y)
        else:
            aux = Celda(dato, x, y)
            aux.siguiente = self.primero
            self.primero.anterior = aux
            self.primero = aux
        self.cuenta += 1


    def recorrerInicio(self):
        aux = self.primero
        while aux:
            print(aux.dato, aux.x, aux.y)
            aux = aux.siguiente

    def recorrerFin(self):
        aux = self.ultimo
        while aux:
            print(aux.dato, aux.x, aux.y)
            aux = aux.anterior