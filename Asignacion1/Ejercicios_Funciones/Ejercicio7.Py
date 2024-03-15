#valida si una cadena es de numero entero
def es_numero_entero(cadena):
    if all(caracter.isdigit() for caracter in cadena) or \
       (cadena[0] == '-' and all(caracter.isdigit() for caracter in cadena[1:])):
        return True
    else:
        return False

cadena1 = "4788902"
cadena2 = "1.59"
print(es_numero_entero(cadena1))  # True
print(es_numero_entero(cadena2))  # False

#isdigit = devuelve verdadero si todos los caracteres son digitos o falso si 
# no lo son.
