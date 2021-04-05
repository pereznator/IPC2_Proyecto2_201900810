from graphviz import Digraph
import os

class Grafico:
    arreglo = []
    def __init__(self, matriz, esArreglo, nombre = None, operacion = None):
        self.matriz = matriz
        self.nombre = ''
        if esArreglo:
            aux = nombre + operacion
            self.nombre = ''
            for x in range(len(aux)):
                if aux[x] != ' ':
                    self.nombre = self.nombre + aux[x]
            self.arreglo = self.matriz
            self.getEstructura()
        else:
            aux = self.matriz.nombre
            self.nombre = ''
            for x in range(len(aux)):
                if aux[x] != ' ':
                    self.nombre = self.nombre + aux[x]
            self.arreglo = matriz
            self.descomponer()

    def descomponer(self):
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
        self.getEstructura()

    def getEstructura(self):
        estructura = ''
        y = 1
        for fila in self.arreglo:
            x = 1
            if y == 1:
                estructura = estructura + '<TR>'
                for c in range(0, len(self.arreglo[0])+1):
                    if c == 0:
                        estructura = estructura + '<TD> </TD>'
                    else:
                        estructura = estructura + '<TD>'+str(c)+'</TD>'
                estructura = estructura + '</TR>'

            for celda in fila:
                if x == 1:
                    estructura = estructura + '<TR><TD>'+str(y)+'</TD>'
                if celda['dato'] == '*':
                    estructura = estructura + '<TD> * </TD>'
                else:
                    estructura = estructura + '<TD>  </TD>'
                x+=1
            estructura = estructura + '</TR>'
            y+=1

        self.hacerGrafico(estructura)



    def hacerGrafico(self, estructura):
        d = Digraph('structs', comment=self.nombre, node_attr={'shape': 'plaintext'}, format='png')
        d.node('tabla', '''<
            <TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0">
                '''+estructura+'''
            </TABLE>
        >''')
        #d.view()
        d.render('imagenes/'+self.nombre)
        self.ruta = os.path.abspath('imagenes/'+self.nombre+'.png')
        self.diagram = d
