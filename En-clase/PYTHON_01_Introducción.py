#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Gustavo Moya
#
# Created:     23/08/2022
# Copyright:   (c) Gustavo Moya 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    x = "Hola"
    print(x)

    y = "Cómo estás?"
    print(y)

    # comentario de una línea
    # otro comentario de una línea

    '''
    comentario
    de
    varias
    líneas
    '''
    numero = 2
    cadena = "hola mundo"
    diccionario = { "nombre": "Gustavo", "apellido": "Moya" }
    lista = [ "manzanas", "peras", "naranjas" ]
    tupla = ( "azul", "verde", "amarillo" )

    PI = 3.14
    GRAVEDAD = 9.8

    nombre = input("Ingrese su nombre")

    edad = input("Ingrese su edad")

    # Puedo imprimir sus valores de la siguiente manera
    print(f'El nombre del usuario es {nombre}')
    print(f'La edad es {edad}')

if __name__ == '__main__':
    main()
