nombreusuario = input('introduce tu nombre de usuario: ')

print('el nombre es: ', nombreusuario.capitalize())


edad = input('ingrese la edad: ')

while(edad.isdigit()==False):
    
    print('por favor introduce un valor numerico: ')
    edad = input('ingrese la edad: ')

if (int(edad)<18):

    print('no puede pasar')

else:

    print('puede pasar')

