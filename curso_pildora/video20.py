def devuelve_ciudades(*ciudades):
    for elemento in ciudades:
        yield elemento

ciudades_devueltas = devuelve_ciudades('madrid','barcelona','bilbao','valencia') 

print(next(ciudades_devueltas))
print(next(ciudades_devueltas))


#deseamos acceder a los subelementos por ejemplo en madrid serian sus letras

def devuelve_ciudades(*ciudades):
    for elemento in ciudades:
        for subelemento in elemento:
            yield subelemento

ciudades_devueltas = devuelve_ciudades('madrid','barcelona','bilbao','valencia') 

print(next(ciudades_devueltas))
print(next(ciudades_devueltas))

#como usar yield from

def devuelve_ciudades(*ciudades):
    for elemento in ciudades:
         yield from elemento

ciudades_devueltas = devuelve_ciudades('madrid','barcelona','bilbao','valencia') 

print(next(ciudades_devueltas))
print(next(ciudades_devueltas))

