class coche():
    #propiedades --> atributos
    #metodo constructor
    def __init__(self):
        self.__largochasis = 250
        self.__anchochasis = 120
        self.__ruedas = 4
        self.__enmarcha = False #en principio esten por defecto detenidos
    #comportamiento --> metodos
    def arrancar(self,arrancamos):
       
        self.enmarcha = arrancamos

        if (self.__enmarcha):
            return 'el coche esta en marcha'
        else:
            return 'el coche esta parado'  
    def estado(self):
        print('el coche tiene: ',self.__ruedas,'ruedas','un ancho de: ',self.__anchochasis,'y un largo de: ', self.__largochasis)      

        

micoche = coche() #instanziamos

print(micoche.arrancar(True))

print(micoche.estado())

print('--------a continuacion creamos el segundo objeto------------')

micoche2 = coche() #segunda instancia

print(micoche2.arrancar(False))

micoche2.ruedas = 2

print(micoche2.estado())

