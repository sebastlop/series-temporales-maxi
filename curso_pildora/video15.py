for i in ['pildoras', 'informaticas',3]:

    print('hola',end = "   ")

for i in "andresmaximilianoabdala":
    print('hola',end = "---")

# busca un @
correo = input('ingrese su email:')

email = False
for i in correo:
    print(i,end='')

    if (i=="@"):

        email = True
if email == True:
    print('email es correcto') 
else:
    print('el email no es correcto')       


    correo = input('ingrese su email:')


#busca un punto y un @
correo = input('ingrese su email:')
contador = 0
email = False
for i in correo:
    print(i,end='')

    if (i=="@" or i=='.'):
        contador+=1

        email = True
if contador == 2:
    print('email es correcto') 
else:
    print('el email no es correcto')   

 #tipo range

for i in range(5):  
    print('hola') 

ber = range(5)
print(type(ber))