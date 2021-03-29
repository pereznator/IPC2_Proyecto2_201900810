from cargarArchivo import CargarArchivo

class Main():
    def __init__(self):
        self.imprimirMenu()

    def imprimirMenu(self):
        while True:
            print('''
Seleccione una de las siguientes opciones
    1. Cargar Acrchivo XML
    2. Salir
            ''')

            p = input()
            if p == '1':
                archivo = CargarArchivo()
            elif p == '2':
                print('adios')
                break
            else:
                print('Escriba una opcion disponible')

m = Main()