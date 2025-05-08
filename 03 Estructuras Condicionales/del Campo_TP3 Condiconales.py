#1) Escribir un programa que solicite la edad del usuario. 
# Si el usuario es mayor de 18 años, deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”. 

edad= int(input("Por favor, Ingrese su edad..."))
if edad >= 18:
    print ("es mayor de edad")


#2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá mostrar por 
# pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el "mensaje “Desaprobado”. 

nota=int(input("ingrese su nota para sabe si se encuentra aprobado : "))
if nota>=6:
    print("Aprobado")
else:
        print("Desaprobado")


#3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un número par, imprimir 
# por en pantalla el mensaje "Ha ingresado un número par"; en caso #contrario, imprimir por pantalla "Por favor,
# ingrese un número par". 
# Nota: investigar el uso del #operador de módulo (%) en Python para evaluar si un número es # par o impar. 

print("COMPROBAR NROS PARES")
numero=int(input("ingrese un número : "))
if numero % 2 ==0:
    print("Ha ingresado un número par")
else:
        print("Por favor, ingrese un número par")


#4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las siguientes categorías pertenece: 
#● Niño/a: menor de 12 años. 
#● Adolescente: mayor o igual que 12 años y menor que 18 años. 
#● Adulto/a joven: mayor o igual que 18 años y menor que 30 años. 
#● Adulto/a: mayor o igual que 30 años.

edad=int(input("ingrese un su edad : "))
if edad  < 12:
    print("Pertenece a la categoria Niños")
elif edad >=12 and edad <=18:
        print("Pertenece a la categoria Adolescente")
elif edad >=18 and edad <30:
        print("Pertenece a la categoria Adulto/a joven")
else:
        print("Pertenece a la categoria Adulto/a ")


#5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres (incluyendo 8 y 14). 
# Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en pantalla el mensaje "Ha ingresado 
# una contraseña correcta"; en caso contrario, imprimir por pantalla "Por favor, ingrese una contraseña de entre 
# 8 y 14 caracteres".
# Nota: investigue el uso de la función len() en Python para evaluar la cantidad de
# elementos que tiene un iterable tal como una lista o un string. 

#USO FUNCION LEN()
#  texto = "Hola"
#  longitud = len(texto)
#  print(longitud)  # mostrara a la Salida: 4

password=(input("Ingrese su contraseña (entre 8 y 14 caracteres): "))
longitud =len(password)
if longitud >=8 and longitud <=14:
    print("Ha ingresado una contraseña correcta")
else:
        print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")
        
        
#6) El paquete statistics de python contiene funciones que permiten tomar una lista de números y calcular la moda, 
# la mediana y la media de dichos números. Un ejemplo de su uso es el siguiente: 
from statistics import mode, median, mean  
mi_lista = [1,2,5,5,3]  
mean(mi_lista) 
#En la documentación oficial se puede encontrar más información sobre este paquete: 
#https://docs.python.org/es/3.8/library/statistics.html.  
#La moda (mode), la mediana (median) y la media (mean) son parámetros estadísticos que se pueden utilizar para predecir 
# la forma de una distribución normal a partir del siguiente criterio: 
#● Sesgo positivo o a la derecha: cuando la media es mayor que la mediana y, a su vez, la mediana es mayor que la moda. 
#● Sesgo negativo o a la izquierda: cuando la media es menor que la mediana y, a su vez, la mediana es menor que la moda. 
#● Sin sesgo: cuando la media, la mediana y la moda son iguales. 
#Teniendo en cuenta lo antes mencionado, escribir un programa que tome la lista numeros_aleatorios, calcule su moda,
# su mediana y su media y las compare para determinar si hay sesgo positivo, negativo o no hay sesgo. Imprimir el
# resultado por pantalla. 
#  Definir la lista numeros_aleatorios de la siguiente forma: 
#  import random 
#  numeros_aleatorios = [random.randint(1, 100) for i in range(50)] 
# Nota: el bloque de código anterior crea una lista con 50 números entre 1 y 100 elegidos de forma aleatoria. 

import random
from statistics import mode, median, mean

# Crear la lista de números aleatorios
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

# Calcular la moda, la mediana y la media
moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

# Imprimir los resultados de cada estadistica
print(f"Moda: {moda}")
print(f"Mediana: {mediana}")
print(f"Media: {media}")

# Determinar cada sesgo
# Sesgo positivo o a la derecha: cuando la media es mayor que la mediana y, a su vez, la mediana es mayor que la moda. 
if (media > mediana) and (mediana > moda):
    print("Sesgo positivo (o a la derecha).")
    
    #Sesgo negativo o a la izquierda: cuando la media es menor que la mediana y, a su vez, la mediana es menor que la moda. 
elif (media < mediana) and (mediana < moda):
    print("Sesgo negativo (o a la izquierda).")
else:  # Sin sesgo: cuando la media, la mediana y la moda son iguales.
    print("Sin sesgo.")




#7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado termina con vocal, añadir un signo 
# de exclamación al final e imprimir el string resultante por pantalla; en caso contrario, dejar el string tal cual lo 
# ingresó el usuario e imprimirlo por pantalla. 

# Solicita al usuario ingresar una frase
frase=str(input(“ingrese una plabafra o frase ”))

# Obtiene la longitud de la frase
longitud=len(frase)

# Informa  la longitud de la frase ingresada
print (" *** la frase tiene una longitud de" , longitud, "caracteres ***")
# Obtiene el último carácter de la frase y lo muestro 
ultimo_caracter = frase[-1]
print("el último caracter de la frase es: ", ultimo_caracter)

# Verifica si el último carácter es una vocal (minúscula o mayúscula)
# Si termina con 'vocal', agrega un asterisco al final y lo imprime
if frase[-1] == "a" or frase[-1]=="A": 
    frase= frase+"*"
    print(frase)
elif  frase[-1] == "e" or frase[-1]=="E": 
     frase= frase+"*"
     print(frase)
elif  frase[-1] == "i" or frase[-1]=="I": 
     frase= frase+"*"
     print(frase)
elif  frase[-1] == "o" or frase[-1]=="O": 
     frase= frase+"*"
     print(frase)
elif  frase[-1] == "u" or frase[-1]=="U": 
     frase= frase+"*"
     print(frase)
else:
    # Si la frase no termina con una vocal, se imprime un mensaje indicando que no se hace cambio
    print("su frase no termina en vocal por lo tanto queda igual: ",frase)


#8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 dependiendo de la opción que desee: 
    #1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO. 
    #2. Si quiere su nombre en minúsculas. Por ejemplo: pedro. 
    #3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro. 
#El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el usuario e imprimir el resultado
# por pantalla. Nota: investigue uso de las funciones upper(), lower() y title() de Python para convertir entre mayúsculas y minúsculas. 

# Solicita al usuario ingresar una frase
nombre=str(input(“Por favor ingrese su nombre: ”))

# Muestra las opciones disponibles al usuario
print (" A continuación seleccione una opcion")
print (" 1. Si quiere su nombre en mayúsculas.")
print (" 2. Si quiere su nombre en minúsculas.")
print (" 3. Si quiere su nombre con la primera.")

# Solicita la opción que desea el usuario
opcion=int(input(""))

# Verifica la opción seleccionada por el usuario y realiza la acción correspondiente 
if opcion == 1: 
    nombre_mayusculas = nombre.upper()   # Convierte el nombre a MAYUSCULAS 
    print(nombre_mayusculas)  

elif  opcion == 2:
    nombre_minusculas = nombre.lower()   # Convierte el nombre a minusculas 
    print(nombre_minusculas)  

elif  opcion == 3:
    nombre_versalitas = nombre.title()    # Convierte el nombre a letra Capital o Versalita
    print(nombre_versalitas)  

else:
       # Si el usuario no selecciona una opción válida
    print("No selecciono una opcion valida ! ")


#9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la magnitud en una de las siguientes
# categorías según la escala de Richter e imprima el resultado por pantalla: 

#● Menor que 3: "Muy leve" (imperceptible). 
#● Mayor o igual que 3  y menor que 4: "Leve" (ligeramente perceptible). 
#● Mayor o igual que 4  y menor que 5: "Moderado" (sentido por personas, pero generalmente no causa daños). 
#● Mayor o igual que 5  y menor que 6: "Fuerte" (puede causar daños en estructuras débiles). 
#● Mayor o igual que 6  y menor que 7: "Muy Fuerte" (puede causar daños significativos). 
#● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala). 

# Solicita al usuario ingresar una frase
valor=float (input(“Por favor ingrese la magnitud del sismo (escala de Richter): ”))

# Redondea el valor y lo convierte a entero
# magnitud = round(valor)

# Solicita al usuario ingresar una frase
magnitud=int(valor)


# Verifica la opción seleccionada por el usuario y realiza la acción correspondiente 
if magnitud  < 3: 
   print( "Sismo Muy leve (imperceptible)")

elif  magnitud >= 3 and magnitud <4:
    print( "Sismo Muy Leve (ligeramente perceptible)") 

elif  magnitud >= 4 and magnitud <5:
    print( "Sismo Moderado (sentido por personas, pero generalmente no causa daños)") 
elif  magnitud >= 5 and magnitud <6:
    print( "Sismo Fuerte (puede causar daños en estructuras débiles)") 
elif  magnitud >= 6 and magnitud <7:
    print( "Sismo Muy Fuerte (puede causar daños significativos)") 
else:
    print("Sismo  Extremo (puede causar graves daños a gran escala)")


#10) Utilizando la información aportada en la siguiente tabla sobre las estaciones del año
#Periodo del año          Estación en el hemisferio norte            Estación en el hemisferio sur 

#Desde el 21 de diciembre hasta el 20 de marzo (incluidos)      #Invierno    #Verano 
#Desde el 21 de marzo hasta el 20 de junio (incluidos)          #Primavera   #Otoño 
#Desde el 21 de junio hasta el 20 de septiembre (incluidos)     #Verano     #Invierno
#Desde el 21 de septiembre hasta el 20 de diciembre (incluidos)  #Otoño     #Primavera 

#Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes del año es y qué día es.
# El programa deberá utilizar esa información para imprimir por pantalla si el usuario se encuentra en otoño, invierno,
# primavera o verano.

hemisferio=str(input("Indica en que hemisferio te encuentras:; presiona  N= Norte o S=Sur  "))

hemisferio = hemisferio.upper() #convierte a mayusculas letra mes

mes=int(input("Cual es el mes del año? (de 1 a 12) "))
dia=int(input("Cual es el día del mes (de 1 a 31) "))

if hemisferio == "N":   # Hemisferio Norte
        if (mes == 12 and dia >= 21) or (mes == 3 and dia <= 20) or (mes > 12 and mes < 3):
            print( "Invierno")
        elif (mes == 3 and dia >= 21) or (mes == 6 and dia <= 20) or (mes > 3 and mes < 6):
            print("Primavera")
        elif (mes == 6 and dia >= 21) or (mes == 9 and dia <= 20) or (mes > 6 and mes < 9):
            print( "Verano")
        elif (mes == 9 and dia >= 21) or (mes == 12 and dia <= 20) or (mes > 9 and mes < 12):
            print( "Otoño")
            
elif hemisferio == "S":  # Hemisferio Sur
    
            if (mes == 12 and dia >= 21) or (mes == 3 and dia <= 20) or (mes > 12 and mes < 3):
                print("Verano")
            elif (mes == 3 and dia >= 21) or (mes == 6 and dia <= 20) or (mes > 3 and mes < 6):
                print( "Otoño")
            elif (mes == 6 and dia >= 21) or (mes == 9 and dia <= 20) or (mes > 6 and mes < 9):
                print( "Invierno")
            elif (mes == 9 and dia >= 21) or (mes == 12 and dia <= 20) or (mes > 9 and mes < 12):
                print( "Primavera")
else:
        print("Hemisferio no válido")
        