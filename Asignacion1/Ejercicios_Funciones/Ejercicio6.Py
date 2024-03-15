#Manda el texto ingresado de forma invertida
def invertir_cadena(cadena):
    cadena_invertida = ""
    for caracter in cadena:
        cadena_invertida = caracter + cadena_invertida
    return cadena_invertida

cadena = "Don't be Afraid..."
cadena_invertida = invertir_cadena(cadena)
print(cadena_invertida)