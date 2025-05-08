"""

4)	Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”, respectivamente.  Imprimir la lista resultante por pantalla. ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el indexing con números negativos! 
"""

animales = ["perro", "gato", "conejo", "pez"]  
animales = ["perro", "gato", "conejo", "pez"]
print(animales)
animales[1]="loro" # reemplaza ultimo elemento por "loro"
animales[-1]="oso" # reemplaza ultimo elemento por "oso"
print(animales)

#Muestra en pantalla
# ['perro', 'gato', 'conejo', 'pez']
# ['perro', 'loro', 'conejo', 'oso']
