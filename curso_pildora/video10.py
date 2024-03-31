print('programa de evaluacion de notas de alumnos')

nota_alumno = input('ingrese la nota del alumno: ')

def evaluacion(nota):
    valoracion  = 'aprobado'
    if nota < 6:
        valoracion = 'deaprobado'
    return valoracion    


print(evaluacion(int(nota_alumno)))


