#1) Crea un programa en python que imprima en pantalla todos los números enteros desde 0 hasta 100 (incluyendo ambos extremos), 
# en orden creciente, mostrando un número por línea. 

for i in range(101):  # bucle desde 0 hasta 100
    print(i)          # Imprime los números del 0 al 100, uno por línea

##Recordar que el valor final de range no es inclusivo, por eso usamos 101). 


#2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de dígitos que contiene. 
# Solicitar un número entero al usuario
numero = int(input("Por favor ingresa un número entero: "))

# Si el número es negativo, lo convertimos a positivo
if numero < 0:
    numero = -(numero)

# Contar la cantidad de dígitos
cant_digitos = 1  # Inicializamos con 1 porque el número tiene al menos un dígito

while numero >= 10:
    numero = numero // 10  # Dividimos entero entre 10 para eliminar el último dígito
    cant_digitos = cant_digitos+1   # Incremento en 1 la cantidad de digitos

# Imprimir la cantidad de dígitos
print(f"El número tiene { cant_digitos } dígitos.")


#3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores dados por el usuario, excluyendo esos dos valores. 
# se piden dos valores al usuario
valor_inferior = int(input("Introduce el valor inferior: "))
valor_superior = int(input("Introduce el valor superior: "))

suma = 0   # Inicializa la variable que almacenará la suma en 0

# Comprobamos que valor inferior sea menor que valor superior
if valor_inferior < valor_superior:
    # Recorremos los números entre valor_inferior y valor_superior, excluyendo esos dos
    for i in range(valor_inferior + 1, valor_superior):
        suma =  suma + i       #podria hacerlo con (suma += i)
else:
    # Si el valor inferior no es menor que el superior, intercambiamos los valores (suma conmutativa)
    for i in range(valor_superior + 1, valor_inferior):
        suma =  suma + i 

# Imprimir el resultado de la suma
print(f"La suma de los números entre los dos valores es: {suma}")


# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.
# Inicializar la variable de suma
suma = 0
# Solicitar el primer número
numero = int(input("Introduce un número entero (0 para terminar): "))

# Continuar pidiendo números mientras el usuario no ingrese 0
while numero != 0:
    suma = suma + numero
    numero = int(input("Introduce un número entero (0 para terminar): "))

# Mostrar el total acumulado
print(f"El total acumulado es: {suma}")


#  5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el programa debe mostrar cuántos 
# intentos fueron necesarios para acertar el número. 

import random

# Generar un número aleatorio entre 0 y 9
numero_aleatorio = random.randint(0, 9)

# Inicializar los intentos
intentos = 0

# Bucle para que el usuario intente adivinar el número
while True:
    # Solicitar al usuario que ingrese un número
    intento = int(input("Adivina el número (entre 0 y 9): "))
    
    # Contabilizar el intento
    intentos += 1
    
    # Verificar si el intento es correcto
    if intento == numero_aleatorio:
        print(f"¡Felicidades! Has adivinado el número en {intentos} intentos.")
        break  # Salir del bucle cuando se acierta el número
    elif intento < numero_aleatorio:
        print("El número es mayor. Intenta de nuevo.")
    else:
        print("El número es menor. Intenta de nuevo.")



# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos entre 0 y 100, en orden decreciente. 

# Imprimir los números pares en orden decreciente
for i in range(100, -1, -2):        # rango(inicio, final(0), decremento)
    if i %2==0:
        print(i)
# Otra forma de Imprimir los números pares en orden decreciente de 2 en 2  sin condicional
for i in range(100, -1, -2):
    print(i)


#  7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un número entero positivo indicado por el usuario.

# Solicitar un número entero positivo
numero = int(input("Introduce un número entero positivo: "))

suma = 0  # Inicializar la suma en cero

# Comprobar si el número es positivo
if numero >= 0:
    # Sumar los números desde 0 hasta el número ingresado
    for i in range(1, numero + 1):
        suma = suma + i
        
else:
    # solicita un nuevo numero en caso de no ser positivo
    print("Por favor, introduce un número entero positivo.")
    
print(f"La suma de los números entre 0 y {numero} es: {suma}")



# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el programa debe indicar cuántos de estos 
# números son pares, cuántos son impares, cuántos son negativos y cuántos son positivos. (Nota: para probar el programa puedes usar 
# una cantidad menor, pero debe estar preparado para procesar 100 números con un solo cambio). 

# Inicializar cada contador en cero
pares = 0
impares = 0
negativos = 0
positivos = 0

# Solicitar al usuario 100 números
for i in range(100):    
    numero = int(input(f"Introduce el número {i + 1}: "))
    
    # identificar si el número es par o impar
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
    
    # Identificar si el número es negativo o positivo
    if numero < 0:
        negativos += 1
    elif numero > 0:
        positivos += 1

# Mostar los resultados
print(f"\nResultados:")
print(f"Cantidad de números pares: {pares}")
print(f"Cantidad de números impares: {impares}")
print(f"Cantidad de números negativos: {negativos}")
print(f"Cantidad de números positivos: {positivos}")


# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la media de esos valores. 
# (Nota: puedes probar el programa con una cantidad menor, pero debe poder procesar 100 números cambiando solo un valor). 

# Número total de entradas
total_numeros = 5

# Inicializar la variable de suma
suma = 0

# Solicitar al usuario 100 números1

for i in range(total_numeros):
    numero = int(input(f"Introduce el número {i + 1}: "))
    suma = suma + numero  # Acumula la suma de los números en cada iteracion

# Calcular la media
print("La suma de los numeros es: ", suma)

media = suma / total_numeros

# Mostrar el resultado
print(f"\n La media de los números ingresados es: {media}")   #\n hace salto de linea antes de mostrar media


# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

# Solicitar al usuario un número entero
numero = int(input("Introduce un número entero: "))

# Inicializar la variable para almacenar el número invertido
numero_invertido = 0

# Mientras el número sea mayor que 0
while numero > 0:
    # Obtener el último dígito del número
    ultimo_digito = numero % 10
    
    # Colocar el último dígito en la posición correcta en el número invertido
    numero_invertido = numero_invertido * 10 + ultimo_digito
    
    # Eliminar el último dígito del número original
    numero = numero // 10

# Mostrar el número invertido
print(f" \n 12345El número invertido es: {numero_invertido}")
