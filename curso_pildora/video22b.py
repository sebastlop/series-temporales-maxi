def divide1(): 

    try:

        op1 = (float(input('introduce el primer numero: ')))
        op2 = (float(input('introduce el primer segundo: ')))
        print('la division es: '+str(op1/op2))
    except ValueError:
        print('el valor introducio es erroneo')
    except ZeroDivisionError:
        print('nose puede dividir por 0!')    
    
    print('calculos finalizados')

def divide2(): 

    try:

        op1 = (float(input('introduce el primer numero: ')))
        op2 = (float(input('introduce el primer segundo: ')))
        print('la division es: '+str(op1/op2))
    except:
        print('ha icurrido un error')    
    
    print('calculos finalizados')

def divide3(): 

    try:

        op1 = (float(input('introduce el primer numero: ')))
        op2 = (float(input('introduce el primer segundo: ')))
        print('la division es: '+str(op1/op2))

    finally:
        print('calculos finalizados')    

divide1()
divide2() 
divide3()