def evaluaEdad1(edad):
    if edad<20:
        return 'eres muy joven'
    elif edad<40:
        return 'eres joven'
    elif edad<65:
        return 'eres maduro'
    elif edad<100:
        return 'cuidate'



def evaluaEdad2(edad):

    if edad<0:
        raise TypeError('no se permiten edades negativas')
    if edad<20:
        return 'eres muy joven'
    elif edad<40:
        return 'eres joven'
    elif edad<65:
        return 'eres maduro'
    elif edad<100:
        return 'cuidate'
    


import math

def calcularaiz(num1):
    #cuando el nuero que ingresemos sea negativo entra aca y probocamos un except
    if num1<0:
        raise ValueError('el numero no puede ser negativo')
    
    else:
        return math.sqrt(num1)

op1 = (int(input('introduce un numero: '))) 
#como el error sale al ejecutarse op1 lo capturamos con Try
try:   
    print(calcularaiz(op1))
#y damos el except y le damos un nombre alternativo con as
except ValueError as ErrorDeNumeroNegativo:
    print(ErrorDeNumeroNegativo)

print('programa terminado')

