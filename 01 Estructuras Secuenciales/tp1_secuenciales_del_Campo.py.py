# 1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.  
print ("Hola Mundo!")

#2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando el nombre ingresado. Por ejemplo: si el usuario 
# ingresa “Marcos”, el programa debe imprimir  #por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) 
# para realizar la impresión por pantalla. 
nombre = input("Ingresa tu nombre: ")      # Solicita el nombre al usuario
print(f"Hola {nombre}!")                   # Imprime el saludo usando el nombre ingresado, empleando f-strings para formateo de cadenas

#3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e imprima por pantalla una oración con los datos 
# ingresados. Por ejemplo: si el usuario ingresa “Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 
# 30 años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar #la impresión por pantalla.

nombre = input("Me dirias tu nombre: ")      # Solicita los datos al usuario
apellido = input(" tu Apellido: ") 
edad =int (input(" tu edad: ") )
lugar = input(" y tu lugar de residencia: ") 
print(f"soy {nombre} {apellido}, tengo {edad} años y resido en {lugar} ")   # Imprime concatenando las variabes y el texto


#4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y su perímetro. 
radio = float(input("Introduce el radio del círculo: "))    # Solicita ingresar el tamaño del radio del circ
pi = 3.1415926
área = pi*radio  # area= pi.radio
perim = 2*pi*(radio)
print(f"El area del circulo es : {área:.2f}   y ")
print(f"El perímetro del circulo es : {perim:.2f}")   

#5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a  cuántas horas equivale. 
#5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a  cuántas horas equivale. 
segundos = int(input("Introduce la cantidad de segundos  "))    # Solicita ingresar lo ssegundos
 #  Calcular cuántas horas equivalenen  sabemos que en 1hs hay 3600seg
equivale_hs = float(segundos/3600)       
print(f"Los {segundos} equivalen a { equivale_hs:.2f}  hora")


#otra forma de resolver   
# Solicitar al usuario la cantidad de segundos
segundos = int(input("Introduce la cantidad de segundos: "))

# Calcular cuántas horas equivalen
horas = segundos // 3600           # División entera para obtener las horas completas
segundos_restantes = segundos % 3600  # Resto de segundos después de contar las horas
# Imprimir el resultado
print(f"Los {segundos} segundos equivalen a {horas} horas y {segundos_restantes} segundos.")


#6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de multiplicar de dicho número.  
# Pedir al usuario un número
numero = int(input("Introduce un número: "))  # se solicita al usuario un número
# Imprimir la tabla de multiplicar sin usar estructura de bucle
print(f"Tabla de multiplicar del {numero}:")
print(f"{numero} x 1 = {numero * 1}")
print(f"{numero} x 2 = {numero * 2}")
print(f"{numero} x 3 = {numero * 3}")
print(f"{numero} x 4 = {numero * 4}")
print(f"{numero} x 5 = {numero * 5}")
print(f"{numero} x 6 = {numero * 6}")
print(f"{numero} x 7 = {numero * 7}")
print(f"{numero} x 8 = {numero * 8}")
print(f"{numero} x 9 = {numero * 9}")
print(f"{numero} x 10 = {numero * 10}")

#7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos. 
# Pedir al usuario dos números enteros distintos de 0
num1 = int(input("Introduce el primer número entero (distinto de 0): "))
num2 = int(input("Introduce el segundo número entero (distinto de 0): "))

    # calculo de las operaciones
suma = num1 + num2
resta = num1 - num2
multiplica = num1 * num2
division = num1/num2

print(f"La suma de {num1} y {num2} es: {suma}")
print(f"La resta de {num1} y {num2} es: {resta}")
print(f"La multiplicación de {num1} y {num2} es: {multiplica}")
print(f"La división de {num1} y {num2} es: {division}")
#8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice  de masa corporal.  imc= 𝑝𝑒𝑠𝑜 𝑒𝑛 𝑘𝑔/((altura en m)**2)

# se solicitan al usuario su altura y peso 
altura = float(input("Ingrese por favor su altura en metros: ")) 
peso = float(input("Ingrese su peso en KG: ")) 

imc=peso / (altura**2)    # Calcula el índice de masa corporal (IMC)

# Mostrar el resultado
print(f"Según sus datos ingresados, su IMC es: {imc:.2f}")

#9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia:  # T𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐹𝑎ℎ𝑟𝑒𝑛ℎ𝑒𝑖𝑡 = (9/5 x( 𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐶𝑒𝑙𝑠𝑖𝑢𝑠)) + 32

temp_celsius = float(input("Ingrese la temperatura en grados Celsius: ")) 
temp_farenheit = (9 / 5) * temp_celsius + 32
print(f"Los {temp_celsius} grados Celsius, equivalen a {temp_farenheit:.2f} grados Fahrenheit")

# 10) Crear un programa que pida al usuario  3 números e imprima por pantalla el promedio de dichos números. 

# Se piden al usuario 3 números enteros
num1 = int(input("Introduce un numero entero: ")) 
num2 = int(input("Introduce un segundo numero entero: ")) 
num3= int(input("Introduce un tercer numero entero: ")) 

# Calcular el promedio
promedio= (num1+num2+num3)/3    # No es necesario convertir a float ya que la división devuelve un float
# Imprimir el promedio con dos decimales
print(f"El promedio de los 3 números es: {promedio:.2f}")  
