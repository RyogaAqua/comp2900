#Convierte de Farenheit a Celsius
def conversion(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

fahrenheit = 190
celsius = round(conversion(fahrenheit))

print(f"Los {fahrenheit}* en Fahrenheit son {celsius}* en Celsius.")
