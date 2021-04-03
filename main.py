from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from cargarArchivo import CargarArchivo

class Main():
    opcion = 0
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

        dosMatricesBoton = Button(self.operacionesFrame, text='Operaciones Sobre Dos Imagenes', width=105, height=3, cursor='hand2')
        dosMatricesBoton.place(x=(self.ancho/2)+10, y=2)

    
    def mostrarUnaImagenOperaciones(self):
        self.opFrame1 = Frame(self.operacionesFrame, width=self.ancho, height=650, bg='blue').place(y=60)
        sidebar = Frame(self.opFrame1, width=300, height=600, bg='green').place(y=210)

        Button(sidebar, text='Rotacion Horizontal', width=35, height=2, cursor='hand2').place(x=15, y=280)
        Button(sidebar, text='Rotacion Vertical', width=35, height=2, cursor='hand2').place(x=15, y=330)
        Button(sidebar, text='Transpuesta', width=35, height=2, cursor='hand2').place(x=15, y=380)
        Button(sidebar, text='Limpiar Zona', width=35, height=2, cursor='hand2').place(x=15, y=430)
        Button(sidebar, text='Agregar Linea Horizontal', width=35, height=2, cursor='hand2').place(x=15, y=480)
        Button(sidebar, text='Agregar Linea Vertical', width=35, height=2, cursor='hand2').place(x=15, y=530)
        Button(sidebar, text='Agregar Rectangulo', width=35, height=2, cursor='hand2').place(x=15, y=580)
        Button(sidebar, text='Agregar Triangulo Rectangulo', width=35, height=2, cursor='hand2').place(x=15, y=630)

        Label(self.opFrame1, text='Matriz Actual:', font=('Century Gothic', 20), bg='blue').place(x=350, y=220)
        aux = self.matrices.primero
        nombres = ['Elegir matriz']
        for matrix in range(self.matrices.cuenta):
            nombres.append(aux.nombre)
            aux = aux.siguiente
        combo = ttk.Combobox(self.opFrame1, values=nombres, state='readonly')
        combo.current(0)
        combo.place(x=550, y=230)

        Button(self.opFrame1, text='Ver Matriz', width=10, height=1, cursor='hand2', command=lambda: self.verMatriz(combo.get())).place(x=700, y=230)

    def verMatriz(self, nombreMatriz):
        if nombreMatriz == 'Elegir matriz':
            return
        aux = self.matrices.primero
        matriz = ''
        for x in range(self.matrices.cuenta):
            if aux.nombre == nombreMatriz:
                matriz = aux
            aux = aux.siguiente
        Label(self.opFrame1, text='Original', font=('Arial', 16), bg='blue').place(x=550, y=270)
        Label(self.opFrame1, text='Resultado', font=('Arial', 16), bg='blue').place(x=1200, y=270)
        matrixFrame = Frame(self.opFrame1, width=500, height=400, bg='white').place(x=350, y=310)
        Button(matrixFrame, text='h', width=100, height=80)

        faux = matriz.listaFilas.primero
        for f in range(matriz.listaFilas.cuenta):
            caux = faux.primero
            for c in range(faux.cuenta):
                if caux.dato == '*':
                    b = Button(matrixFrame, text='*', width=int(65/matriz.columnas), height=int(25/matriz.filas))
                    b.place(x=350+(c*b.winfo_reqwidth()), y=310+(f*b.winfo_reqheight()))
                else:
                    b = Button(matrixFrame, text=' ', width=int(65/matriz.columnas), height=int(25/matriz.filas))
                    b.place(x=350+(c*b.winfo_reqwidth()), y=310+(f*b.winfo_reqheight()))
                caux = caux.siguiente
            faux = faux.siguiente
        resultadoFrame = Frame(self.opFrame1, width=500, height=400, bg='red').place(x=1000, y=310)

    def rotacionHorizontal(self):
        pass
    def rotacionVertical(self):
        pass
    def transpuesta(self):
        pass
    def limpiarZona(self):
        pass
    def agregarHorizontal(self):
        pass
    def agregarVertical(self):
        pass
    def agregarRectangulo(self):
        pass
    def agregarTriangulo(self):
        pass

m = Main()