#concatenacion de operadores de comparacion
#en condicional if

edad = -7

if 0 < edad < 100:
    print('la edad es correcta')
else:
    print('edad incorrecta')


salario_presidente = int(input('introducir salario presidente: '))
print('salario presidente: '+ str(salario_presidente))

salario_director = int(input('introducir salario director: '))
print('salario presidente: '+ str(salario_presidente))

salario_administrativo = int(input('introducir salario administrativo: '))
print('salario presidente: '+ str(salario_presidente))

salario_jefe_area= int(input('introducir jefe area: '))
print('salario presidente: '+ str(salario_presidente))

if salario_administrativo<salario_jefe_area<salario_director<salario_presidente:
    print('todo funciona correctamente')
else:
    print('algo falla en esta empresa')