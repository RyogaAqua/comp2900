#Escoge el valor maximo
def maximo(numero1, numero2):
    if numero1 > numero2:
        return numero1
    else:
        return numero2

resultado = maximo(96, 94)
print("El valor máximo entre los números es:", resultado)