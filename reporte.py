import dominate
from dominate.tags import *
from datetime import date, datetime
import webbrowser
import os

class Reporte:
    def __init__(self):
        self.matrices = []
        self.operacionesSimples = []
        self.operacionesComplejas = []
        self.errores = []

    def introducirMatrices(self, matrices):
        maux = matrices.primero
        for m in range(matrices.cuenta):
            faux = maux.listaFilas.primero
            mobj = {'nombre': maux.nombre, 'llenos': 0, 'vacios': 0, 'fecha': str(date.today()), 'hora': str(datetime.now())}
            for f in range(maux.listaFilas.cuenta):
                caux = faux.primero
                for c in range(faux.cuenta):
                    if caux.dato == '*':
                        mobj['llenos'] += 1
                    else:
                        mobj['vacios'] += 1
                    caux = caux.siguiente
                faux = faux.siguiente
            self.matrices.append(mobj)
            maux = maux.siguiente


    def nuevaOperacionSimple(self, tipo, nombreMatriz):
        self.operacionesSimples.append({'tipo': tipo, 'nombre': nombreMatriz, 'fecha': str(date.today()), 'hora': str(datetime.now())})

    def nuevaOperacionCompleja(self, tipo, matriz1, matriz2):
        self.operacionesComplejas.append({'tipo': tipo, 'nombre1': matriz1, 'nombre2': matriz2, 'fecha': str(date.today()), 'hora': str(datetime.now())})

    def nuevoError(self, descripcion, tipo, nombre):
        self.errores.append({'descripcion': descripcion, 'tipo': tipo, 'nombre': nombre, 'fecha': str(date.today()), 'hora': str(datetime.now())})

    def generarReporte(self):
        doc = dominate.document(title = 'Reporte')
        with doc.head:
            link(rel="stylesheet", href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css", integrity="sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z", crossorigin="anonymous")

        with doc:
            with div( cls='container mt-5 mb-5'):
                h1('Reporte')
                hr()
                h3('Matrices')
                with table(cls = 'table'):
                    with thead(cls = 'thead-dark'):
                        with tr():
                            th('Fecha')
                            th('Hora')
                            th('Nombre')
                            th('Espacios Llenos')
                            th('Espacios Vacios')
                    with tbody():
                        for matriz in self.matrices:
                            with tr():
                                td(matriz['fecha'])
                                td(matriz['hora'])
                                td(matriz['nombre'])
                                td(matriz['llenos'])
                                td(matriz['vacios'])
                h3('Operaciones de Una Imagen')
                with table(cls = 'table'):
                    with thead(cls = 'thead-dark'):
                        with tr():
                            th('Fecha')
                            th('Hora')
                            th('Nombre')
                            th('Tipo de Operacion')
                    with tbody():
                        for operacion in self.operacionesSimples:
                            with tr():
                                td(operacion['fecha'])
                                td(operacion['hora'])
                                td(operacion['nombre'])
                                td(operacion['tipo'])
                h3('Operaciones de Dos Imagenes')
                with table(cls = 'table'):
                    with thead(cls = 'thead-dark'):
                        with tr():
                            th('Fecha')
                            th('Hora')
                            th('Nombre de Matriz 1')
                            th('Nombre de Matriz 2')
                            th('Tipo de Operacion')
                    with tbody():
                        for operacion in self.operacionesComplejas:
                            with tr():
                                td(operacion['fecha'])
                                td(operacion['hora'])
                                td(operacion['nombre1'])
                                td(operacion['nombre2'])
                                td(operacion['tipo'])
                h3('Errores')
                with table(cls = 'table'):
                    with thead(cls = 'thead-dark'):
                        with tr():
                            th('Fecha')
                            th('Hora')
                            th('Descripcion')
                            th('Tipo de Operacion')
                            th('Nombres')
                    with tbody():
                        for error in self.errores:
                            with tr():
                                td(error['fecha'])
                                td(error['hora'])
                                td(error['descripcion'])
                                td(error['tipo'])
                                td(error['nombre'])
        
        with open('reportes/reporte.html', 'wb') as file:
            b = doc.render().encode()
            file.write(b)
        webbrowser.open_new_tab(os.path.abspath('reportes/reporte.html'))
