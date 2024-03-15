#Rota los elementos en el arreglo
arreglo = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

arreglo_rotado = [arreglo[-1]] + arreglo[:-1]

print("Arreglo con los elementos rotados:", arreglo_rotado)