#Encuentra el indice del primer valor de la lista
def encontrar_indice(lista, elemento):
    for i in range(len(lista)):
        if lista[i] == elemento:
            return i
    return -1

lista = [1, 2, 3, 4, 5, 6, 7]
elemento = 3
indice = encontrar_indice(lista, elemento)
if indice != -1:
    print("El elemento buscado se encuentra en el índice", indice)
else:
    print("El elemento buscado no se encuentra en la lista.")