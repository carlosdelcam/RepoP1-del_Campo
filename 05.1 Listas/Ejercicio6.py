"""
6)	Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por pantalla los dos primeros. 
"""
#genera lista nros desde 10 hasta 30 inclusive, de 5 en 5
nueva_lista=list(range(10,31,5))   
print("lista origen: ",nueva_lista)
	
# Mostrar los dos primeros elementos
print(nueva_lista[:2]) #usa slicing para tomar los dos primeros elementos de la lista.

#en pantalla se muestra
# lista origen: [10, 15, 20, 25, 30]
# [10, 15]
