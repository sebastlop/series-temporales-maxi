class coche():

    def desplazamiento(self):
        print('me desplazo utilizando 4 ruedas')

class moto():

    def desplazamiento(self):
        print('me desplazo utilizando 2 ruedas')

class camion():

    def desplazamiento(self):
        print('me desplazo utilizando 6 ruedas')

mivehiculo = moto()
mivehiculo.desplazamiento()

mivehiculo2 = coche()
mivehiculo2.desplazamiento()

mivehiculo3 = camion()
mivehiculo3.desplazamiento()

#podemos usar la magia del polimorfismo

def desplazamientovehiculo(vehiculo):
    vehiculo.desplazamiento()

#con esto generalizo el metodo para los tipos de vehiculos
mivehiculo = moto()
desplazamientovehiculo(mivehiculo)