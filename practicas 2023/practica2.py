def encontrar_mayor_menor(numeros):
    # Convierte la cadena de números en una lista de enteros
    numeros = [int(num) for num in numeros.split()]
    
    # Si la lista está vacía, devuelve None para mayor y menor
    if not numeros:
        return None, None
    
    # Inicializa las variables mayor y menor con el primer número
    mayor = menor = numeros[0]
    
    # Itera a través de la lista de números
    for num in numeros:
        # Actualiza el valor de 'mayor' si encontramos un número mayor
        if num > mayor:
            mayor = num
        # Actualiza el valor de 'menor' si encontramos un número menor
        if num < menor:
            menor = num
    
    # Devuelve el valor mayor y menor encontrados
    return mayor, menor

# Solicita al usuario ingresar una serie de números
entrada = input("Ingresa una serie de números separados por espacios: ")

# Llama a la función para encontrar el número mayor y menor
mayor, menor = encontrar_mayor_menor(entrada)

# Verifica si hay resultados y muestra el número mayor y menor
if mayor is not None and menor is not None:
    print(f"El número mayor es: {mayor}")
    print(f"El número menor es: {menor}")
else:
    print("No se ingresaron números.")
