#Muestra el promedio entre los numeros ingresados.
def promedio(lista_numeros):
    suma = 0
    cantidad = 0
    for numero in lista_numeros:
        suma += numero
        cantidad += 1
    if cantidad == 0:  # Manejo de la división por cero
        return 0
    else:
        return suma / cantidad

resultado = promedio([585, 1120, 15000, 245340])
print("El promedio es:", resultado)