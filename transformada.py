class Transformada:
    resultado = []
    def __init__(self, matriz):
        self.matriz = matriz
        self.verMatriz()

    def verMatriz(self):
        self.arreglo = []
        faux = self.matriz.listaFilas.primero
        for f in range(self.matriz.listaFilas.cuenta):
            caux = faux.primero
            fila = []
            for c in range(faux.cuenta):
                fila.append({'dato': caux.dato, 'x': caux.x, 'y': caux.y})
                caux = caux.siguiente
            self.arreglo.append(fila)
            faux = faux.siguiente
    
    def rotacionHorizontal(self):
        nuevaMatriz = []
        for fila in self.arreglo:
            nuevaMatriz.append([])
        
        i = len(nuevaMatriz) - 1
        for fila in self.arreglo:
            nuevaMatriz[i] = fila
            i-=1
        self.resultado = nuevaMatriz

    def rotacionVertical(self):
        nuevaMatriz = []
        for fila in self.arreglo:
            arr = []
            for celda in fila:
                arr.append({})
            nuevaMatriz.append(arr)

        f = 0
        for fila in self.arreglo:
            l = len(fila) - 1
            for celda in fila:
                nuevaMatriz[f][l] = celda
                l-=1
            f+=1
        self.resultado = nuevaMatriz

    def transpuesta(self):
        columnas = []
        for c in range(len(self.arreglo[0])):
            columnas.append([])

        for f in self.arreglo:
            for c in f:
                columnas[c['x'] - 1].append(c)

        nuevaMatriz = []
        for fila in self.arreglo:
            nuevaMatriz.append([])

        f = 0
        for fila in columnas:
            nuevaMatriz[f] = fila
            f+=1
        self.resultado = nuevaMatriz

    def limpiarZona(self, coordenadas):
        for y in range(int(coordenadas['y1'])-1, int(coordenadas['y2'])):
            for x in range(int(coordenadas['x1'])-1, int(coordenadas['x2'])):
                self.arreglo[y][x]['dato'] = '-'

        self.resultado = self.arreglo

    def agregarHorizontal(self, datos):
        for dato in self.arreglo[int(datos['fila'])-1]:
            if int(datos['x1']) <= dato['x'] <= int(datos['x2']):
                dato['dato'] = '*'

        self.resultado = self.arreglo

    def agregarVertical(self, datos):
        f = 1
        for fila in self.arreglo:
            if int(datos['y1']) <= f <= int(datos['y2']):
                for celda in fila:
                    if celda['x'] == int(datos['columna']):
                        celda['dato'] = '*'
            f+=1
        self.resultado = self.arreglo

    def agregarRectangulo(self, datos):
        limy = datos['y'] + datos['filas']
        limx = datos['x'] + datos['columnas']
        celdas = []
        for y in range(datos['y'], limy):
            for x in range(datos['x'], limx):
                celdas.append({'x': x-1, 'y': y-1})
        
        for c in celdas:
            self.arreglo[c['y']][c['x']]['dato'] = '*'
        self.resultado = self.arreglo

    def agregarTriangulo(self, datos):
        limy = datos['y'] + datos['filas']
        limx = datos['x'] + datos['columnas']
        celdas = []
        for y in range(datos['y'], limy):
            for x in range(datos['x'], limx):
                celdas.append({'x': x-1, 'y': y-1})
        
        c = 1
        triangulo = []
        for x in range(datos['filas']):
            fila = []
            for m in range(c):
                fila.append({})
            triangulo.append(fila)
            c+=1

        self.resultado = self.arreglo
        