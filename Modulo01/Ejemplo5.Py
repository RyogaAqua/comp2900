def buscar_elemento( arreglo, elemento):
    return elemento in arreglo

# Prueba
arreglo = {1, 2, 3, 4, 5}

assert buscar_elemento(arreglo, 3), "El elemento fue encontrado donde deberia estar."
assert buscar_elemento(arreglo, 6), "El elemento no fue encontrado donde deberia estar"