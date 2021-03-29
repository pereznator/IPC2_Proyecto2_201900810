from matriz import Matriz

class listaMatrices():
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.cuenta = 0

    def vacia(self):
        return self.primero == None
    
    def agregarMatriz(self, nombre, filas, columnas, listaFilas):
        if self.vacia():
            self.primero = self.ultimo = Matriz(nombre, filas, columnas, listaFilas)
        else:
            aux = self.ultimo
            self.ultimo = aux.siguiente = Matriz(nombre, filas, columnas, listaFilas)

    def recorrer(self):
        aux = self.primero
        while aux:
            print(aux.nombre)
            aux = aux.siguiente
