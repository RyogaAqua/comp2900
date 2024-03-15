#Borra un valor en el arreglo
arreglo = [4, 21, 33, 47, 58]

elemento = 4

if elemento in arreglo:
    arreglo.remove(elemento)
    print(f"El elemento {elemento} ha sido borrado del arreglo.")
    print("Arreglo despues de la eliminacion:", arreglo)
else:
    print(f"El elemento {elemento} no está en el arreglo.")