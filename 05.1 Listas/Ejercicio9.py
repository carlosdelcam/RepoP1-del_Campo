#9)	Dada la lista “compras”, cuyos elementos representan los productos comprados por diferentes clientes: 

compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]  
#a) Agregar "jugo" a la lista del tercer cliente usando append. 
compras[2].append("jugo")  #agrega “jugo” a la lista del 3er clinte (índice 2)
#b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente. 
compras[1][1]= "tallarines"     
#c) Eliminar "pan" de la lista del primer cliente.  
compras[0].remove("pan")
#d) Imprimir la lista resultante por pantalla 
print(compras)

[['leche'], ['arroz', 'tallarines', 'salsa'], ['agua', 'jugo']]
