print('programas de beca 2024')

distancia_escuela = int(input('introduce la distancia a la escuela en km: ') )
print(distancia_escuela)

numero_hermano = int(input('numero de hermanos: '))
print(numero_hermano)

salario_familar = int(input('salario familiar: '))
print(salario_familar)

if distancia_escuela > 40 and numero_hermano > 2 and salario_familar <= 20000:

    print('tienes derecho a beca')

else:
    print('no tienes derecho a beca')


print('asignaturas optativas año 2024')
print('asignatura optativas: informatica grafica - pruebas de software - usabilidad y accesibiliad')

asignatura = (input('escribe la asignatura escogida: '))
asignatura = asignatura.lower()

if asignatura in ('informatica grafica','pruebas de software','usabilidad y accesibilidad'):

    print('asignatura elegida ' + asignatura)

else:
    print('la asignatira elegida no esta contemplada')


