from random import randint

def generaNumeroAleatorio(minimo,maximo):

    try: 
        if minimo > maximo:
            aux = minimo
            minimo = maximo
            maximo = aux

        return randint(minimo, maximo)
    except TypeError:
        print("debes escribir numeros")
        return -1
    

numero_buscado = generaNumeroAleatorio(1,100)

print(numero_buscado)

encontrado = False  
    
while not encontrado:
        numero_usuario = int(input("introduce el numero buscado: "))

        if numero_usuario > numero_buscado:
            print("el numero que buscas es menor")
        elif numero_usuario < numero_buscado:
            print("el numero que buscas es mayor")
        else:
            encontrado = True
            print("has acertado")
