# Ejercicio 1

def area_rectangulo(b,h):
    area = b * h
    return area

print(area_rectangulo(10,7))


# Ejercicio 2

pi = 3.14159

def area_circulo(r):
    circulo = pi * r **2
    return circulo

print(area_circulo(5))


# Ejercicio 3 

def relacion(num1,num2):
    if (num1 > num2):
        return 1
    elif (num1 < num2):
        return -1
    else:
        return 0

print(relacion(1,2))     


# Ejercicio 4

def intermedio(num1, num2):
    intermedio = (num1 + num2) / 2
    return intermedio

print(intermedio(10,24))    