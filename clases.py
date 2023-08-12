import os   # es el modulon que se importa para poder eliminar el archivo de la computadora

class Pelicula:
    def __init__(self, nombre):
        self.__nombre = nombre #atributo privado



   #crear método __str__ 


   #crear métodos de acceso para el atributo privado: mostrar el atributo "nombre" y modificarlo
   # recordar que hay dos metodos (decoradores o funciones)
        




class CatalogoPelicula:
    def __init__(self, nombre):
        self.nombre = nombre
        self.ruta_archivo = self.nombre,".txt"  #no va a ser pasado por parametro sino que lo creo a partir del nombre


    def agregar_pelicula(self, pelicula):  
        with open(self.ruta_archivo, 'a') as archivo:   # 'a' para indicar que quiero abrir el archivo
            archivo.write(pelicula.nombre, '\n')

    def listar_peliculas(self):
        # abrir el archivo con with
        # imprimir lo que hay en el archivo (archivo.read())
        pass

    def eliminar_peliculas(self):    
        os.remove(self.ruta_archivo)
        print("El archivo: ", self.ruta_archivo, "fue eliminado")
        


