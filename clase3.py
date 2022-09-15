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


# Ejercicio 5 

def recortar(num,inf,sup):
    if (num > sup):
        return sup
    elif (num < inf):
        return inf
    else:
        return num  

print(recortar(5,2,10))  


# Ejercicio 6

lista = [1,2,3,4,5,6,7,8,9,10]

listImp = []
listPar = []
def separar(dato):
    for num in dato:
        if num %2 == 0:
            listPar.append(num)
        else:
            listImp.append(num)   

separar(lista)
print(f'Lista de pares: {listPar}')
print(f'Lista de pares: {listImp}')