class Conjunto:
    resultado = None
    base = None
    def __init__(self, matrix1, matrix2):
        self.matrix1 = matrix1
        self.matrix2 = matrix2
        self.verMatrices()

    def verMatrices(self):
        self.arreglo1 = []
        faux = self.matrix1.listaFilas.primero
        for f in range(self.matrix1.listaFilas.cuenta):
            caux = faux.primero
            fila = []
            for c in range(faux.cuenta):
                fila.append({'dato': caux.dato, 'x': caux.x, 'y': caux.y})
                caux = caux.siguiente
            self.arreglo1.append(fila)
            faux = faux.siguiente

        self.arreglo2 = []
        faux2 = self.matrix2.listaFilas.primero
        for f in range(self.matrix2.listaFilas.cuenta):
            caux = faux2.primero
            fila = []
            for c in range(faux2.cuenta):
                fila.append({'dato': caux.dato, 'x': caux.x, 'y': caux.y})
                caux = caux.siguiente
            self.arreglo2.append(fila)
            faux2 = faux2.siguiente
        
        self.determinarDimensiones()

    def determinarDimensiones(self):
        unoRowMayor = False
        if (len(self.arreglo1) - len(self.arreglo2)) >= 0:
            unoRowMayor = True

        unoColMayor = False
        if (len(self.arreglo1[0]) - len(self.arreglo2[0])) >= 0:
            unoColMayor = True

        nmatrix = []
        if unoRowMayor:
            for x in range(len(self.arreglo1)):
                nmatrix.append([])
        else:
            for x in range(len(self.arreglo2)):
                nmatrix.append([])
        f = 0
        for fila in nmatrix:
            if unoColMayor:
                for celda in (self.arreglo1[f]):
                    fila.append({})
            else:
                for celda in (self.arreglo2[f]):
                    fila.append({})
            f+=1

        self.base = nmatrix

    def union(self):
        nmatrix = self.base
        y = 0
        for fila in self.arreglo1:
            x = 0
            for celda in fila:
                nmatrix[y][x] = celda
                x+=1
            y+=1
        
        j = 0
        for fila in self.arreglo2:
            i = 0
            for celda in fila:
                if 'dato' in nmatrix[j][i]:
                    if celda['dato'] == '-' and nmatrix[j][i]['dato'] == '*':
                        nmatrix[j][i]['dato'] = '*'
                    elif celda['dato'] == '-' and nmatrix[j][i]['dato'] == '-':
                        nmatrix[j][i]['dato'] = '-'
                    elif celda['dato'] == '*' and nmatrix[j][i]['dato'] == '*':
                        nmatrix[j][i]['dato'] = '*' 
                    elif celda['dato'] == '*' and nmatrix[j][i]['dato'] == '-':
                        nmatrix[j][i]['dato'] = '*' 
                else:
                    nmatrix[j][i] = celda
                i+=1
            j+=1
        self.resultado = nmatrix

    def interseccion(self):
        nmatrix = self.base
        y = 0
        for fila in self.arreglo1:
            x = 0
            for celda in fila:
                nmatrix[y][x] = celda
                x+=1
            y+=1
        
        j = 0
        for fila in self.arreglo2:
            i = 0
            for celda in fila:
                if 'dato' in nmatrix[j][i]:
                    if celda['dato'] == '-' and nmatrix[j][i]['dato'] == '*':
                        nmatrix[j][i]['dato'] = '-'
                    elif celda['dato'] == '-' and nmatrix[j][i]['dato'] == '-':
                        nmatrix[j][i]['dato'] = '-'
                    elif celda['dato'] == '*' and nmatrix[j][i]['dato'] == '*':
                        nmatrix[j][i]['dato'] = '*' 
                    elif celda['dato'] == '*' and nmatrix[j][i]['dato'] == '-':
                        nmatrix[j][i]['dato'] = '-' 
                else:
                    nmatrix[j][i] = {'dato': '-', 'x': celda['x'], 'y': celda['y']}
                i+=1
            j+=1
        self.resultado = nmatrix

    def diferencia(self):
        nmatrix = self.base
        y = 0
        for fila in self.arreglo1:
            x = 0
            for celda in fila:
                nmatrix[y][x] = celda
                x+=1
            y+=1
        
        j = 0
        for fila in self.arreglo2:
            i = 0
            for celda in fila:
                if 'dato' in nmatrix[j][i]:
                    if celda['dato'] == '-' and nmatrix[j][i]['dato'] == '*':
                        nmatrix[j][i]['dato'] = '*'
                    elif celda['dato'] == '-' and nmatrix[j][i]['dato'] == '-':
                        nmatrix[j][i]['dato'] = '-'
                    elif celda['dato'] == '*' and nmatrix[j][i]['dato'] == '*':
                        nmatrix[j][i]['dato'] = '-' 
                    elif celda['dato'] == '*' and nmatrix[j][i]['dato'] == '-':
                        nmatrix[j][i]['dato'] = '-' 
                else:
                    nmatrix[j][i] = {'dato': '-', 'x': celda['x'], 'y': celda['y']}
                i+=1
            j+=1
        self.resultado = nmatrix

    def diferenciaSimetrica(self):
        nmatrix = self.base
        y = 0
        for fila in self.arreglo1:
            x = 0
            for celda in fila:
                nmatrix[y][x] = celda
                x+=1
            y+=1
        
        j = 0
        for fila in self.arreglo2:
            i = 0
            for celda in fila:
                if 'dato' in nmatrix[j][i]:
                    if celda['dato'] == '-' and nmatrix[j][i]['dato'] == '*':
                        nmatrix[j][i]['dato'] = '*'
                    elif celda['dato'] == '-' and nmatrix[j][i]['dato'] == '-':
                        nmatrix[j][i]['dato'] = '-'
                    elif celda['dato'] == '*' and nmatrix[j][i]['dato'] == '*':
                        nmatrix[j][i]['dato'] = '-' 
                    elif celda['dato'] == '*' and nmatrix[j][i]['dato'] == '-':
                        nmatrix[j][i]['dato'] = '*' 
                else:
                    nmatrix[j][i] = celda
                i+=1
            j+=1
        self.resultado = nmatrix

        
                
