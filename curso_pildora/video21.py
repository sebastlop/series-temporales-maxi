 #errores excepciones

def suma(num1,num2):
    return num1 + num2

def resta(num1,num2):
    return num1 - num2

def multiplica(num1,num2):
    return num1 * num2

def divide(num1,num2):

    try:
        return num1 / num2
   
    except ZeroDivisionError:
        print('no se puede dividir entre 0')
        return 'operacion erronea'

op1 = (int(input('introduce el primer numero: ')))


op2 = (int(input('introduce el segundo numero: ')))

operacion = input('introduce la operacion a realizar (suma,resta,multiplica,divide); ')

if operacion == "suma":
    print(suma(op1,op2))

elif operacion == "resta":
    print(resta(op1,op2))


elif operacion == "multiplica":
    print(multiplica(op1,op2))


elif operacion == "divide":
    print(divide(op1,op2))

else:
    print('operacion no contemplada')

print('operacion ejecutada, continuacion de ejecucion del programa')

#hacemos de cuenta que aca abajo hay mas de cientos de lineas de codigo
