import math 

i = 1

while i <= 4 :
    print('ejecucion ' + str(i))
    i += 1
print('termino la ejecucion ') 

edad = int(input('introduce la edad: '))

while edad < 0:
    print('has introducido una edad negativa')
    edad = int(input('introduce la edad por favor: '))

print('gracias por colaborar. puedes pasar')
print('edad del aspirante '+str(edad))

print('programa de calculo de raiz cuadrada: ')

numero = int(input('introdude un numero: '))

intentos = 0

while numero < 0:
    print('no se puede hallar la raiz de un numero negativo')
    if(intentos == 2):
        print('has consumido demasidos intento. el proframa ha finalizado')
        break
    numero = int(input('introdude un numero: '))
    
    if numero < 0:
        intentos += 1
if intentos < 2:
    solucion = math.sqrt(numero)        
    print('la raiz cuadrada de '+ str(numero)+ ' es '+ str(solucion))


