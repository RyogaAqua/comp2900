#Cuenta la cantidad de vocales en una cadena
def contar_vocales(cadena):
    cadena = cadena.lower()
    contador_vocales = 0
    vocales = "aeiou"
    
    for caracter in cadena:
        if caracter in vocales:
            contador_vocales += 1
    return contador_vocales

cadena = "Hay una cierta cantidad de vocales."
print("La cantidad de vocales es:", contar_vocales(cadena))
