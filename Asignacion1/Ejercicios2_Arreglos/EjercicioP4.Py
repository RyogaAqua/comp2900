#Busca un valor en el arreglo
arreglo = [17, 19, 30, 42, 90]

elemento = 30

if elemento in arreglo:
    posicion = arreglo.index(elemento)
    print(f"El elemento {elemento} se encuentra en la posición {posicion}.")
else:
    print(f"El elemento {elemento} no se encuentra en el arreglo.")