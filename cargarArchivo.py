import xml.etree.ElementTree as ET
from datos.fila import Fila
from datos.listaFilas import ListaFilas
from datos.listaMatrices import listaMatrices

class CargarArchivo:
    def __init__(self, ruta):
        self.ruta = ruta
        self.extraerContenido()

    def extraerContenido(self):
        doc = ET.parse(self.ruta)
        raiz = doc.getroot()
        if raiz.tag == 'matrices':
            self.matrices = listaMatrices()
            for matriz in raiz:
                if matriz.tag == 'matriz':
                    nombre = ''
                    columnas = 0
                    nfilas = 0
                    imagen = ''
                    for etiqueta in matriz:
                        if etiqueta.tag == 'nombre':
                            nombre = etiqueta.text
                        elif etiqueta.tag == 'filas':
                            nfilas = int(etiqueta.text)
                        elif etiqueta.tag == 'columnas':
                            columnas = int(etiqueta.text)
                        elif etiqueta.tag == 'imagen':
                            imagen = etiqueta.text
                    filas = []
                    f = ''
                    for x in range(len(imagen)):
                        if imagen[x] in ('-', '*'):
                            f = f + imagen[x]
                        elif imagen[x] in ('\n'):
                            if f != '':
                                filas.append(f)
                                f = ''
                    listaFilas = ListaFilas()
                    f = 1
                    for l in filas:
                        fila = Fila()
                        c = 1
                        for x in range(len(l)):
                            fila.agregarFinal(l[x], c, f)
                            c +=1
                        listaFilas.agregarFila(fila)
                        f += 1
                    #listaFilas.recorrer()
                    self.matrices.agregarMatriz(nombre, nfilas, columnas, listaFilas)
                    

