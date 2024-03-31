import pickle


class vehiculo():

    def __init__(self, marca, modelo):

        self.marca = marca
        self.modelo = modelo
        self.enmarcha = False
        self.acelera = False
        self.frena = False
    
    def arracar(self):
        self.enmarcha = True

    def acelera(self):
        self.acelera = True
    
    def frena(self):
        self.frena = True
    
    def estado(self):
         print('marca: ', self.marca, '\nmodelo: ',self.modelo, '\nen marcha: ', self.enmarcha, '\nacelerando: ', self.acelera, '\nfrenando: ', self.frena)

#guardo la informacion en un fichero binario
coche1 = vehiculo('mazda', 'mx5')

coche2 = vehiculo('seat', 'leon')

coche3 = vehiculo('renault', 'megane')

coches = [coche1, coche2, coche3]

fichero = open('loscoches','wb')

pickle.dump(coches, fichero)

fichero.close()

del(fichero)

#rescato la informacion de un fichero binario

fichero = open('loscoches','rb')

miscoches = pickle.load(fichero)

fichero.close()

#para recorrer la informacion dentro de la variable

for c in miscoches:
    print(c)