#Combina dos arreglos
def combinar_arreglos(arreglo1, arreglo2):

    arreglo_combinado = []
    
    for numero in arreglo1:
        arreglo_combinado.append(numero)

    for numero in arreglo2:
        arreglo_combinado.append(numero)

    return arreglo_combinado

arreglo1 = [1, 2, 3, 4, 5]
arreglo2 = [6, 7, 8, 9, 10]
