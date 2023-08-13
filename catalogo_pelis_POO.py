
from clases import *

opcion = None

nombre_catalogo = input("Ingrese el nombre del catálogo: \n")
catalogo = CatalogoPelicula(nombre_catalogo)  # con este paso creo mi objeto / instancia


while opcion != 4:
    try:
        print("\nOpciones: ")
        print("1. Agregar película")
        print("2. Listar película")
        print("3. Eliminar catálogo de películas")
        print("4. SALIR\n")
        
        opcion = int(input("Escriba una opción del menú (del 1 al 4): "))

        if opcion == 1:
            nombre_pelicula = input("Escriba el nombre de la película: ")
            pelicula = Pelicula(nombre_pelicula)
            catalogo.agregar_pelicula(pelicula)
            
        elif opcion == 2:
            catalogo.listar_peliculas()

        
        elif opcion == 3:
            catalogo.eliminar_catalogo()

    except Exception as e:
        print("\n¡Ocurrio un error!\n", e, "\n")
        opcion = None

else: 
    print("Programa finalizado")    



