from tkinter import *
from tkinter import ttk, Entry
from tkinter.filedialog import askopenfilename
from cargarArchivo import CargarArchivo
from transformada import Transformada
from conjuntos import Conjunto

class Main():
    opcion = 0
    matriz = None
    opImagen = 0
    opFrame1 = None
    opFrame2 = None

    matrix1 = None
    matrix2 = None

    def __init__(self):
        self.desplegarInterfaz()

    def desplegarInterfaz(self):
        self.raiz = Tk()
        self.raiz.state('zoomed')

        self.ancho = self.raiz.winfo_screenwidth()
        self.alto = self.raiz.winfo_screenheight()

        miFrame = Frame(self.raiz, width=self.ancho, height=150, bg='gray')
        miFrame.place(x=0,y=0)

        titulo = Label(miFrame, text='Operador de Imagenes', font=('Century Gothic', 36), bg='gray')
        titulo.place(x=self.obtenerPocisionCentrada(titulo))

        opcion1 = Button(miFrame, text='Cargar Archivo', width=50, height=3, cursor='hand2', command=self.cargarArchivoFrame)
        opcion1.place(x=10, y=80)
        opcion2 = Button(miFrame, text='Operaciones', width=50, height=3, cursor='hand2', command=self.mostrarOperacionesFrame)
        opcion2.place(x=390, y=80)
        opcion3 = Button(miFrame, text='Reportes', width=50, height=3, cursor='hand2')
        opcion3.place(x=775, y=80)
        opcion4 = Button(miFrame, text='Ayuda', width=50, height=3, cursor='hand2')
        opcion4.place(x=1160, y=80)
        self.raiz.title('Editor de matrices')
        self.raiz.mainloop()


    def obtenerPocisionCentrada(self, elemento):
        self.raiz.update()
        return (self.ancho/2) - (elemento.winfo_reqwidth()/2)

    def cargarArchivoFrame(self):
        self.opcion = 1
        self.cargarFrame = Frame(self.raiz, width=self.ancho, height=650, bg='red')
        self.cargarFrame.place(y=150)
        try:
            ruta = askopenfilename(initialdir='/', title='Seleccionar archivo', filetypes=(("xml files","*.xml"),("xml files","*.xml")))
            cargar = CargarArchivo(ruta)
            self.matrices = cargar.matrices
        except:
            self.opcion = 0
            nombre = Label(self.cargarFrame, 'Ha ocurrido un error!', font=('Arial', 24))
            nombre.place(x=self.obtenerPocisionCentrada(nombre), y=60)

    def mostrarOperacionesFrame(self):
        if self.opcion == 0:
            return
        self.opcion = 2
        self.cargarFrame.pack_forget()
        self.operacionesFrame = Frame(self.raiz, width=self.ancho, height=650, bg='yellow')
        self.operacionesFrame.place(y=150)
        
        unaMatrizBoton = Button(self.operacionesFrame, text='Operaciones Sobre Una Imagen', width=105, height=3, cursor='hand2', command=self.mostrarUnaImagenOperaciones)
        unaMatrizBoton.place(x=5, y=2)

        dosMatricesBoton = Button(self.operacionesFrame, text='Operaciones Sobre Dos Imagenes', width=105, height=3, cursor='hand2', command=self.desplegarDosImagenes)
        dosMatricesBoton.place(x=(self.ancho/2)+10, y=2)

    
    def mostrarUnaImagenOperaciones(self):
        if self.opFrame2 != None:
            self.opFrame2.place_forget()
        self.opFrame1 = Frame(self.operacionesFrame, width=self.ancho, height=650, bg='blue')
        self.opFrame1.place(y=60)
        sidebar = Frame(self.opFrame1, width=300, height=600, bg='green')
        sidebar.place(x=0,y=0)

        Label(self.opFrame1, text='Matriz Actual:', font=('Century Gothic', 20), bg='blue').place(x=350, y=20)
        aux = self.matrices.primero
        nombres = ['Elegir matriz']
        for matrix in range(self.matrices.cuenta):
            nombres.append(aux.nombre)
            aux = aux.siguiente
        combo = ttk.Combobox(self.opFrame1, values=nombres, state='readonly')
        combo.current(0)
        combo.place(x=550, y=30)

        Button(self.opFrame1, text='Ver Matriz', width=10, height=1, cursor='hand2', command=lambda: self.verMatriz(combo.get())).place(x=700, y=30)
        
        Button(sidebar, text='Rotacion Horizontal', width=35, height=2, cursor='hand2', command=self.rotacionHorizontal).place(x=15, y=20)
        Button(sidebar, text='Rotacion Vertical', width=35, height=2, cursor='hand2', command=self.rotacionVertical).place(x=15, y=70)
        Button(sidebar, text='Transpuesta', width=35, height=2, cursor='hand2', command=self.transpuesta).place(x=15, y=120)
        Button(sidebar, text='Limpiar Zona', width=35, height=2, cursor='hand2', command=self.limpiarZona).place(x=15, y=170)
        Button(sidebar, text='Agregar Linea Horizontal', width=35, height=2, cursor='hand2', command=self.agregarHorizontal).place(x=15, y=220)
        Button(sidebar, text='Agregar Linea Vertical', width=35, height=2, cursor='hand2', command=self.agregarVertical).place(x=15, y=270)
        Button(sidebar, text='Agregar Rectangulo', width=35, height=2, cursor='hand2', command=self.agregarRectangulo).place(x=15, y=320)
        Button(sidebar, text='Agregar Triangulo Rectangulo', width=35, height=2, cursor='hand2', command=self.agregarTriangulo).place(x=15, y=370)


    def verMatriz(self, nombreMatriz):
        if nombreMatriz == 'Elegir matriz':
            return
        aux = self.matrices.primero
        for x in range(self.matrices.cuenta):
            if aux.nombre == nombreMatriz:
                self.matriz = aux
            aux = aux.siguiente
        Label(self.opFrame1, text='Original', font=('Arial', 16), bg='blue').place(x=550, y=70)
        Label(self.opFrame1, text='Resultado', font=('Arial', 16), bg='blue').place(x=1200, y=70)
        matrixFrame = Frame(self.opFrame1, width=510, height=410, bg='white')
        matrixFrame.place(x=350, y=100)
        #Button(matrixFrame, text='h', width=100, height=80)

        faux = self.matriz.listaFilas.primero
        for f in range(self.matriz.listaFilas.cuenta):
            caux = faux.primero
            for c in range(faux.cuenta):
                if caux.dato == '*':
                    b = Button(matrixFrame, text='*', width=int(65/self.matriz.columnas), height=int(25/self.matriz.filas))
                    b.place(x=(c*b.winfo_reqwidth()), y=(f*b.winfo_reqheight()))
                else:
                    b = Button(matrixFrame, text=' ', width=int(65/self.matriz.columnas), height=int(25/self.matriz.filas))
                    b.place(x=(c*b.winfo_reqwidth()), y=(f*b.winfo_reqheight()))
                caux = caux.siguiente
            faux = faux.siguiente
        
        self.resultadoFrame = Frame(self.opFrame1, width=510, height=410, bg='red')
        self.resultadoFrame.place(x=1000, y=100)

    def limpiarFrame(self):
        if self.opImagen == 4:
            self.limpZonaFrame.place_forget()
        elif self.opImagen == 5:
            self.horizontalFrame.place_forget()
            print('horizontal forget')
        elif self.opImagen == 6:
            self.verticalFrame.place_forget()
        elif self.opImagen == 7:
            self.rectanguloFrame.place_forget()
        elif self.opImagen == 8:
            self.trianguloFrame.place_forget()

    def rotacionHorizontal(self):
        if self.matriz == None:
            return
        self.limpiarFrame()
        self.opImagen = 1
        tran = Transformada(self.matriz)
        tran.rotacionHorizontal()
        self.desplegarResultado(tran.resultado)
    
    def rotacionVertical(self):
        if self.matriz == None:
            return
        self.limpiarFrame()
        self.opImagen = 2
        tran = Transformada(self.matriz)
        tran.rotacionVertical()
        self.desplegarResultado(tran.resultado)

    def transpuesta(self):
        if self.matriz == None:
            return
        self.limpiarFrame()
        self.opImagen = 3
        tran = Transformada(self.matriz)
        tran.transpuesta()
        self.desplegarResultado(tran.resultado)

    def limpiarZona(self):
        if self.matriz == None:
            return
        self.limpiarFrame()
        self.opImagen = 4

        self.limpZonaFrame = Frame(self.opFrame1, width=600, height=50, bg='orange')
        self.limpZonaFrame.place(x=900, y=0)
        Label(self.limpZonaFrame, text='x1:').place(x=20, y=20)
        x1 = Entry(self.limpZonaFrame, width=5)
        x1.place(x=50, y=20)
        Label(self.limpZonaFrame, text='y1:').place(x=90, y=20)
        y1 = Entry(self.limpZonaFrame, width=5)
        y1.place(x=120, y=20)
        Label(self.limpZonaFrame, text='x2:').place(x=220, y=20)
        x2 = Entry(self.limpZonaFrame, width=5)
        x2.place(x=250, y=20)
        Label(self.limpZonaFrame, text='y2:').place(x=290, y=20)
        y2 = Entry(self.limpZonaFrame, width=5)
        y2.place(x=320, y=20)
        Button(self.limpZonaFrame, text='Calcular', width=10, height=1, command=lambda: self.opLimpiar(x1,y1,x2,y2)).place(x=360, y=15)

    def opLimpiar(self, x1, y1, x2, y2):
        if self.matriz == None:
            return
        coordenadas = {'x1': x1.get(), 'y1': y1.get(), 'x2': x2.get(), 'y2': y2.get()}
        tran = Transformada(self.matriz)
        tran.limpiarZona(coordenadas)
        self.desplegarResultado(tran.resultado)

    def agregarHorizontal(self):
        if self.matriz == None:
            return
        self.limpiarFrame()
        self.opImagen = 5

        self.horizontalFrame = Frame(self.opFrame1, width=600, height=50, bg='orange')
        self.horizontalFrame.place(x=900, y=0)
        Label(self.horizontalFrame, text='Fila:').place(x=20, y=20)
        fila = Entry(self.horizontalFrame, width=5)
        fila.place(x=70, y=20)
        Label(self.horizontalFrame, text='x1:').place(x=110, y=20)
        x1 = Entry(self.horizontalFrame, width=5)
        x1.place(x=140, y=20)
        Label(self.horizontalFrame, text='x2:').place(x=180, y=20)
        x2 = Entry(self.horizontalFrame, width=5)
        x2.place(x=210, y=20)
        Button(self.horizontalFrame, text='Calcular', width=10, height=1, command=lambda: self.horizonrtalOp(fila,x1,x2)).place(x=360, y=15)
    
    def horizonrtalOp(self, fila, x1, x2):
        datos = {'fila': fila.get(), 'x1': x1.get(), 'x2': x2.get()}
        tran = Transformada(self.matriz)
        tran.agregarHorizontal(datos)
        self.desplegarResultado(tran.resultado)

    def agregarVertical(self):
        if self.matriz == None:
            return
        self.limpiarFrame()
        self.opImagen = 6

        self.verticalFrame = Frame(self.opFrame1, width=600, height=50, bg='orange')
        self.verticalFrame.place(x=900, y=0)
        Label(self.verticalFrame, text='Columna:').place(x=10, y=20)
        columna = Entry(self.verticalFrame, width=5)
        columna.place(x=70, y=20)
        Label(self.verticalFrame, text='y1:').place(x=110, y=20)
        y1 = Entry(self.verticalFrame, width=5)
        y1.place(x=140, y=20)
        Label(self.verticalFrame, text='y2:').place(x=180, y=20)
        y2 = Entry(self.verticalFrame, width=5)
        y2.place(x=210, y=20)
        Button(self.verticalFrame, text='Calcular', width=10, height=1, command=lambda: self.verticalOp(columna,y1,y2)).place(x=360, y=15)

    def verticalOp(self, columna, y1, y2):
        datos = {'columna': columna.get(), 'y1': y1.get(), 'y2': y2.get()}
        tran = Transformada(self.matriz)
        tran.agregarVertical(datos)
        self.desplegarResultado(tran.resultado)

    def agregarRectangulo(self):
        if self.matriz == None:
            return
        self.limpiarFrame()
        self.opImagen = 7

        self.rectanguloFrame = Frame(self.opFrame1, width=600, height=50, bg='orange')
        self.rectanguloFrame.place(x=900, y=0)
        Label(self.rectanguloFrame, text='x:').place(x=20, y=20)
        x = Entry(self.rectanguloFrame, width=5)
        x.place(x=50, y=20)
        Label(self.rectanguloFrame, text='y:').place(x=90, y=20)
        y = Entry(self.rectanguloFrame, width=5)
        y.place(x=120, y=20)
        Label(self.rectanguloFrame, text='Filas:').place(x=200, y=20)
        filas = Entry(self.rectanguloFrame, width=5)
        filas.place(x=240, y=20)
        Label(self.rectanguloFrame, text='Columnas:').place(x=280, y=20)
        columnas = Entry(self.rectanguloFrame, width=5)
        columnas.place(x=350, y=20)
        Button(self.rectanguloFrame, text='Calcular', width=10, height=1, command=lambda: self.rectanguloOp(x,y,filas,columnas)).place(x=400, y=15)   

    def rectanguloOp(self, x, y, filas, columnas):
        datos = {'x': int(x.get()), 'y': int(y.get()), 'filas': int(filas.get()), 'columnas': int(columnas.get())}
        tran = Transformada(self.matriz)
        tran.agregarRectangulo(datos)
        self.desplegarResultado(tran.resultado)

    def agregarTriangulo(self):
        if self.matriz == None:
            return
        self.limpiarFrame()
        self.opImagen = 8

        self.trianguloFrame = Frame(self.opFrame1, width=600, height=50, bg='orange')
        self.trianguloFrame.place(x=900, y=0)
        Label(self.trianguloFrame, text='x:').place(x=20, y=20)
        x = Entry(self.trianguloFrame, width=5)
        x.place(x=50, y=20)
        Label(self.trianguloFrame, text='y:').place(x=90, y=20)
        y = Entry(self.trianguloFrame, width=5)
        y.place(x=120, y=20)
        Label(self.trianguloFrame, text='Filas:').place(x=200, y=20)
        filas = Entry(self.trianguloFrame, width=5)
        filas.place(x=240, y=20)
        Label(self.trianguloFrame, text='Columnas:').place(x=280, y=20)
        columnas = Entry(self.trianguloFrame, width=5)
        columnas.place(x=350, y=20)
        Button(self.trianguloFrame, text='Calcular', width=10, height=1, command=lambda: self.trianguloOp(x,y,filas,columnas)).place(x=400, y=15)   

    def trianguloOp(self, x, y, filas, columnas):
        datos = {'x': int(x.get()), 'y': int(y.get()), 'filas': int(filas.get()), 'columnas': int(columnas.get())}
        tran = Transformada(self.matriz)
        tran.agregarTriangulo(datos)
        #self.desplegarResultado(tran.resultado)

    def desplegarResultado(self, resultado):
        f=0
        for fila in resultado:
            c=0
            for celda in fila:
                if celda['dato'] == '*':
                    b = Button(self.resultadoFrame, text='*', width=int(65/self.matriz.columnas), height=int(25/self.matriz.filas))
                    b.place(x=(c*b.winfo_reqwidth()), y=(f*b.winfo_reqheight()))
                else:
                    b = Button(self.resultadoFrame, text=' ', width=int(65/self.matriz.columnas), height=int(25/self.matriz.filas))
                    b.place(x=(c*b.winfo_reqwidth()), y=(f*b.winfo_reqheight()))
                c+=1
            f+=1

    def desplegarDosImagenes(self):
        if self.opFrame1 != None:
            self.opFrame1.place_forget()
        
        self.opFrame2 = Frame(self.operacionesFrame, width=self.ancho, height=650, bg='pink')
        self.opFrame2.place(y=60)

        nombres = ['Elegir matriz']
        aux = self.matrices.primero
        for matrix in range(self.matrices.cuenta):
            nombres.append(aux.nombre)
            aux = aux.siguiente

        Label(self.opFrame2, text='Matriz 1:', font=('Century Gothic', 15), bg='pink').place(x=20, y=20)
        combo1 = ttk.Combobox(self.opFrame2, values=nombres, state='readonly', width=10)
        combo1.current(0)
        combo1.place(x=120, y=25)
        Button(self.opFrame2, text='Ver Matriz', width=10, height=1, cursor='hand2', command=lambda: self.imprimirMatriz(combo1.get(), True)).place(x=220, y=20)
        
        self.matrizUnoFrame = Frame(self.opFrame2, width=380, height=410, bg='white')
        self.matrizUnoFrame.place(x=20, y=100)

        Button(self.opFrame2, text='Unión', width=15, height=2, cursor='hand2', command=self.union).place(x=450, y=150)
        Button(self.opFrame2, text='Intersección', width=15, height=2, cursor='hand2', command=self.interseccion).place(x=450, y=200)
        Button(self.opFrame2, text='Diferencia', width=15, height=2, cursor='hand2', command=self.diferencia).place(x=450, y=250)
        Button(self.opFrame2, text='Diferencia Simetrica', width=15, height=2, cursor='hand2', command=self.diferenciaSimetrica).place(x=450, y=300)

        Label(self.opFrame2, text='Matriz 2:', font=('Century Gothic', 15), bg='pink').place(x=600, y=20)
        combo2 = ttk.Combobox(self.opFrame2, values=nombres, state='readonly', width=10)
        combo2.current(0)
        combo2.place(x=700, y=25)
        Button(self.opFrame2, text='Ver Matriz', width=10, height=1, cursor='hand2', command=lambda: self.imprimirMatriz(combo2.get(), False)).place(x=800, y=20)

        self.matrizDosFrame = Frame(self.opFrame2, width=380, height=410, bg='white')
        self.matrizDosFrame.place(x=600, y=100)

        Label(self.opFrame2, text='=', font=('Century Gothic', 65), bg='pink').place(x=1000, y=200)

        Label(self.opFrame2, text='Resultado', font=('Century Gothic', 15), bg='pink').place(x=1250, y=50)
        self.respuestaFrame = Frame(self.opFrame2, width=380, height=410, bg='white')
        self.respuestaFrame.place(x=1100, y=100)

    def imprimirMatriz(self, nombreMatriz, esUno):
        if nombreMatriz == 'Elegir matriz':
            return
        aux = self.matrices.primero
        for x in range(self.matrices.cuenta):
            if aux.nombre == nombreMatriz:
                if esUno:
                    self.matrix1 = aux
                else:
                    self.matrix2 = aux
            aux = aux.siguiente

        if esUno:
            faux = self.matrix1.listaFilas.primero
            for f in range(self.matrix1.listaFilas.cuenta):
                caux = faux.primero
                for c in range(faux.cuenta):
                    if caux.dato == '*':
                        b = Button(self.matrizUnoFrame, text='*', width=int(45/self.matrix1.columnas), height=int(20/self.matrix1.filas))
                        b.place(x=(c*b.winfo_reqwidth()), y=(f*b.winfo_reqheight()))
                    else:
                        b = Button(self.matrizUnoFrame, text=' ', width=int(45/self.matrix1.columnas), height=int(20/self.matrix1.filas))
                        b.place(x=(c*b.winfo_reqwidth()), y=(f*b.winfo_reqheight()))
                    caux = caux.siguiente
                faux = faux.siguiente
        else:
            faux = self.matrix2.listaFilas.primero
            for f in range(self.matrix2.listaFilas.cuenta):
                caux = faux.primero
                for c in range(faux.cuenta):
                    if caux.dato == '*':
                        b = Button(self.matrizDosFrame, text='*', width=int(45/self.matrix2.columnas), height=int(20/self.matrix2.filas))
                        b.place(x=(c*b.winfo_reqwidth()), y=(f*b.winfo_reqheight()))
                    else:
                        b = Button(self.matrizDosFrame, text=' ', width=int(45/self.matrix2.columnas), height=int(20/self.matrix2.filas))
                        b.place(x=(c*b.winfo_reqwidth()), y=(f*b.winfo_reqheight()))
                    caux = caux.siguiente
                faux = faux.siguiente

    def union(self):
        if self.matrix1 == None or self.matrix2 == None:
            return
        res = Conjunto(self.matrix1, self.matrix2)
        res.union()
        self.imprimirConjResultado(res.resultado)
    
    def interseccion(self):
        if self.matrix1 == None or self.matrix2 == None:
            return
        res = Conjunto(self.matrix1, self.matrix2)
        res.interseccion()
        self.imprimirConjResultado(res.resultado)

    def diferencia(self):
        if self.matrix1 == None or self.matrix2 == None:
            return
        res = Conjunto(self.matrix1, self.matrix2)
        res.diferencia()
        self.imprimirConjResultado(res.resultado)

    def diferenciaSimetrica(self):
        if self.matrix1 == None or self.matrix2 == None:
            return
        res = Conjunto(self.matrix1, self.matrix2)
        res.diferenciaSimetrica()
        self.imprimirConjResultado(res.resultado)

    def imprimirConjResultado(self, resultado):
        f=0
        for fila in resultado:
            c=0
            for celda in fila:
                if celda['dato'] == '*':
                    b = Button(self.respuestaFrame, text='*', width=int(45/len(resultado[0])), height=int(20/len(resultado)))
                    b.place(x=(c*b.winfo_reqwidth()), y=(f*b.winfo_reqheight()))
                else:
                    b = Button(self.respuestaFrame, text=' ', width=int(45/len(resultado[0])), height=int(20/len(resultado)))
                    b.place(x=(c*b.winfo_reqwidth()), y=(f*b.winfo_reqheight()))
                c+=1
            f+=1

m = Main()