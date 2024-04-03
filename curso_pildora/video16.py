valido = False

email = input('introduce tu email:')

for i in range(len(email)):
    if email[i]=='@':

        valido = True

if valido:
    print('email correcto')

else:
    print('email incorrecto')
    