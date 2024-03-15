#Cuenta la cantidad de letras en un texto
def contar_apariciones_letra(cadena, letra):
    contador = 0
    for caracter in cadena:
        if caracter.lower() == letra.lower():
            contador += 1
    return contador

cadena = "Solo hay cuatro L en esta oracion, aqui esta la otra l."
letra = "l"
cantidad_apariciones = contar_apariciones_letra(cadena, letra)
print(cantidad_apariciones)