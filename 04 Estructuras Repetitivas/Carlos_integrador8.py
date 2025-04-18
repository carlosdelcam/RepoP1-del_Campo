import random

# Generar un número aleatorio entre 0 y 255
numero_aleatorio = random.randint(0, 255)

cant_intentos = 0    # Inicializa el contador de  intentos
binario = ""        #inicializa cadena vacia para concatenar el binariio
decimal = numero_aleatorio

#convertir el nro decimal a binario
while decimal >0:
    resto = decimal % 2
    decimal = decimal //2
    binario = str(resto)+binario
    
#print("el binario es: " , binario)

# Bucle para que el usuario intente adivinar el número
while True:
    # Solicitar al usuario que ingrese un número
    intento = int(input(f"Adivina el número decimal que corresponde al binario  {binario} "))
    print("      AYUDA!!!  Se encuentra entre 0 y 255")
    
    # Contabilizar el intento
    cant_intentos += 1
    
    # Verificar si el intento es correcto
    if intento == numero_aleatorio:
        print(f"¡Felicidades! el numero binario: {binario} = {numero_aleatorio} en decimal; lo adivinaste en {cant_intentos} intentos.")
        break  # Salir del bucle cuando se acierta el número
    elif intento < numero_aleatorio:
        print("El número es mayor. Intenta de nuevo.")
    else:
        print("El número es menor. Intenta de nuevo.")