# Busca el valor maximo en el arreglo
arreglo = [1890, 3994, 70000000, 1598888989, 3]

maximo_elemento = arreglo[0]

for elemento in arreglo:
    if elemento > maximo_elemento:
        maximo_elemento = elemento

print("El valor máximo en el arreglo es:", maximo_elemento)