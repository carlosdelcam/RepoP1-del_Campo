"""
3)	Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por pantalla. Pista: para crear una lista vacía debes colocar los corchetes sin nada en su interior. 
"""
lista = []    # crea lista vacia
for elemento in range (0,3):     # para repetir 3 veces (índices 0, 1, 2).
    print(f"ingrese el {elemento+1} elemento de la lista")
    elemento=input((": "))
    lista.append(elemento)
print(lista)              # imprime lista,

ingrese el 1 elemento de la lista
: casa
ingrese el 2 elemento de la lista
: barrio
ingrese el 3 elemento de la lista
: ciudad
['casa', 'barrio', 'ciudad']

