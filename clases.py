import os   # es el modulon que se importa para poder eliminar el archivo de la computadora

class Pelicula:
    def __init__(self, nombre):
        self.__nombre = nombre #atributo privado

   #crear método __str__ 

   #Métodos de acceso para el atributo privado: mostrar el atributo "nombre" y modificarlo
   # recordar que hay dos metodos (decoradores o funciones)

    @property       #decorador que permite que un método sea accedido como un atributo 
    def nombre(self): 
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre 

class CatalogoPelicula:
    
    def __init__(self, nombre):
        self.nombre = nombre
        self.ruta_archivo = f'{self.nombre}.txt'

    def agregar_pelicula(self, pelicula):
        with open(self.ruta_archivo, 'a') as archivo:
            archivo.write(f'{pelicula.nombre}\n')

    def listar_peliculas(self):
        # abrir el archivo con with 
        # imprimir lo que hay en el archivo ( arhivo.read() )
        #print()
        pass

    def eliminar_catalogo(self):
        os.remove(self.ruta_archivo)
        print(f'Catálogo eliminado: {self.ruta_archivo}')