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
    hcaballito =''
    def caballito(self):
        self.hcaballito = 'voy haciendo el caballito'
    def estado(self):
         print('marca: ', self.marca, '\nmodelo: ',self.modelo, '\nen marcha: ', self.enmarcha, '\nacelerando: ', self.acelera, '\nfrenando: ', self.frena, '\n',self.hcaballito)
 
class furgoneta(vehiculos):
    def carga(self,cargar):
        self.cargado = cargar
        if(self.cargado):
            return 'la furgoneta esta cargada'
        else:
            return 'la furgoneta no esta cargada'

class velectricos():
    def __init__(self):
        self.autonomia = 100
    def cargarenergia(self):
        self.cargando = True

class bicicletaelectrica(velectricos,vehiculos):
    pass

mibici = bicicletaelectrica('orbea','hc123')

