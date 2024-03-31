
#funcion tradicional

def generapares(limite):
    
    num = 1
    
    milista = []

    while num < limite:

        milista.append(num*2)

        num = num + 1

    return milista 

print(generapares(10))   

#generador

def generapares(limite):
    
    num = 1

    while num < limite:

        yield num*2 #construye un objeto iterable

        num = num + 1

devuelvepares = generapares(10)#objeto iterable

print(next(devuelvepares))
print('mas codigo')
print(next(devuelvepares))
print('mas codigo')
print(next(devuelvepares))



sum = 6+15+13+21+18+16+25+19+21+23+21+21+23+18+21+11+27+16+18+10
print(sum/60)