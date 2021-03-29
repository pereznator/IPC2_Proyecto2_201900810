import xml.etree.ElementTree as ET

class CargarArchivo():
    def __init__(self):
        print('Ingrese la ruta del archivo')
        self.ruta = input()
        self.extraerContenido()

    def extraerContenido(self):
        doc = ET.parse(self.ruta)
        raiz = doc.getroot()
        print(raiz.tag)
        if raiz.tag == 'matrices':
            for matriz in raiz:
                if matriz.tag == 'matriz':
                    nombre = ''
                    columnas = 0
                    filas = 0
                    imagen = ''
                    for etiqueta in matriz:
                        if etiqueta.tag == 'nombre':
                            nombre = etiqueta.text
                        elif etiqueta.tag == 'filas':
                            filas = int(etiqueta.text)
                        elif etiqueta.tag == 'columnas':
                            columnas = int(etiqueta.text)
                        elif etiqueta.tag == 'imagen':
                            imagen = etiqueta.text
                    print(nombre, columnas, filas, imagen)

