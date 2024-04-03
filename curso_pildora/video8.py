mitupla = ('andres','maximiliano',13,10,101,12,12,12,12,)

#acceder a un elemento

print(mitupla[2])

#converitr una tupla en una lista

milista = list(mitupla)

print(mitupla)
print(milista)

#convertir una lista en una tupla

mitupla2 = tuple(milista)
print(mitupla)

#elementos en una tupla

print('andres' in mitupla)

#metodo count para contar

print(mitupla.count(12))

#metodo len para saber cuantos elementos tengo

print(len(mitupla))

#tuplas unitarias

mitupla = ('ju,')# si o si con la coma, si no cuenta cada letra

print(len(mitupla))
print(mitupla)

# sin nada tambien es una tupla

mitupla = 'asn',12,123,123,123,2  #empaquetado de tupla
print(mitupla)

#desempaquetado de una tupla
mitupla = 'andres', 'abdala', 13, 10, 1993
nombre, apellido, dia, mes, año = mitupla
print(nombre)
print(apellido)

 