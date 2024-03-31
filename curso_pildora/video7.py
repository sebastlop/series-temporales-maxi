## como crear una lista

milista=['andres','maximiliano','abdala','alvarez']
print(milista[-2])

##porcion de lista

print(milista[0:3])#los primeros 3 elementos

##sin omites el 0 pyton interpreta que es el cero

print(milista[:3])

print(milista[1:3])

print(milista[2:])#le decimos que agarre desde 2 hasta los ultimos

#funcion append

milista.append('siliva')#lo agrega al ultimo

print(milista)

#funcion insert

milista.insert(1,'silvia')

print(milista)

#funcion extend

milista.extend(['silvia','mabel','aramayo'])

print(milista)

#funcion index

print(milista.index('andres'))

print(milista.index('silvia'))

#comprobar si un elemento se encuentra en una lista

print('silvia' in milista)

#funcion para eliminar elementos remove

milista.remove('abdala')

print(milista)

#eliminar el utlimo elemento de una lista

milista.pop()

print(milista)

#sumar listas

milista2 = [1,2,3,4,5,6,7,8,9]#queremos unirla a milista

milista3 = milista + milista2 #el operado suma funciona 
                              # concatenador

print(milista3)

# ahora el operador repetidor

milista3*3

print(milista3*3)