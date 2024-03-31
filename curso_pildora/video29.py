class vehiculos():

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


#ahora creamos una clase moto que herede todo de vehiculo
         
class Moto(vehiculos):
    pass

mimoto = Moto('Honda', 'cbr')

mimoto.estado()