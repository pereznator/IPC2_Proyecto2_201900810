class ListaFilas():
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.cuenta = 0

    def vacia(self):
        return self.primero == None
    
    def agregarFila(self, fila):
        if self.vacia():
            self.primero = self.ultimo = fila
        else:
            aux = self.ultimo
            self.ultimo = aux.siguiente = fila
        self.cuenta += 1

    def recorrer(self):
        aux = self.primero
        for x in range(self.cuenta):
            celda = aux.primero
            for i in range(aux.cuenta):
                print(celda.dato, celda.x, celda.y)
                celda = celda.siguiente
            print('===========')
            aux = aux.siguiente
