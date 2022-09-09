# Ejercicio 1

while True:
    num = int(input('ingrese numero'))
    if (num %2 != 0):
        print('El numero que ingreso es impar') 
        break
    else:
        print('El numero que ingreso es par, volve a ingresar')


# Ejercicio 2

num1 = int(input('ingrese primer numero'))
num2 = int(input('ingrese segundo numero'))

print('Ingrese una de las siguientes operaciones: \n1. Sumar \n2. Restar\n3. Multiplicar')
while True:
    operacion = input('Ingrese la operacion a realizar').lower()
    if (operacion == 'sumar'):
        sumar = num1 + num2
        print(f'La suma es: {sumar}')
        break
    elif (operacion == 'restar'):
        restar = num1 - num2
        print(f'La resta es: {restar}')   
        break
    elif (operacion == 'multiplicar'):
        multiplicar = num1 * num2 
        print(f'La multiplicacion es: {multiplicar}')    
        break
    else:
        print('La opcion ingresada es incorrecta, intente nuevamente')   


# Ejercicio 3

while True:

    user = input('Ingrese un mail valido: ')
    
    if '@' in user:
        print(f'El mail es valido: {user}')
        break
    else:
        print('mail no valido, intente nuevamente')    

#  Ejercicio 4

lista = ['elemento1', 'elemento2', 'elemento3', 'elemento4']
contar = 0

for i in lista:
    contar = contar + 1
    print(contar)

print('La cantidad total es: ', len(lista))

    
#  Ejercicio 5

numeros = [2,5,10,5]
total = 0

for i in numeros:
    total += i

print(f'La suma total es: {total}')


#  Ejercicio 6

promedio = total / len(numeros)
print(promedio)


#  Ejercicio 7

mayor = numeros[0]

for i in numeros:
    if i > mayor:
        mayor = i
print(f'El numero mayor es: {mayor}')


#  Ejercicio 8

menor = numeros[0]

for i in numeros:
    if i < menor:
        menor = i
print(f'El numero mayor es: {menor}')
        
    
  

