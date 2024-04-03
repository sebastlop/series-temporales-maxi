def suma_digitos(numero):
    suma = 0
    while numero > 0:
        digito = numero % 10  # Obtiene el último dígito
        suma += digito  # Agrega el dígito a la suma
        numero //= 10  # Elimina el último dígito del número
        print(suma,numero)
    return suma

entrada = int(input("Ingresa un número entero positivo: "))
if entrada >= 0:
    resultado = suma_digitos(entrada)
    print(f"La suma de los dígitos de {entrada} es: {resultado}")
else:
    print("Ingresa un número entero positivo.")
