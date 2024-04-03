print('verificacion de acceso')

edad_usuario=int(input('introduce la edad por favor:'))

if edad_usuario < 18:
    print('no puedes pasar')
elif edad_usuario > 100:
    print('edad incorrecta')
else:
    print('puedes pasar')
print('elprograma a finalizado')
#otra forma

print('notas')

nota_alumno = int(input('introduce tu nota: '))

if nota_alumno<5:
    print('insuficiente')

elif nota_alumno<6:
    print('suficiente')

elif nota_alumno<7:
    print('notable')

else:
    print('sobresaliente')




