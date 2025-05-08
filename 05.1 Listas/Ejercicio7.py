"""
7)	Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores cualesquiera. 
"""
autos = ["sedan", "polo", "suran", "gol"]
for i in range(1,3):  #recorre indice 1 y 2
    autos[i]=input("Ingrese un nuevo auto a cambiar: ")
print(autos)

Ingrese un nuevo auto a cambiar: citroen
Ingrese un nuevo auto a cambiar: ranger
['sedan', 'citroen', 'ranger', 'gol']
