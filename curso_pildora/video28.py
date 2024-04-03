#encapsulacion de metodos

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
       
        self.__enmarcha = arrancamos
        
        if(self.__enmarcha):
            chequeo = self.__chequeo_interno()

        if (self.__enmarcha and chequeo):
            return 'el coche esta en marcha'
        elif(self.__enmarcha  and chequeo == False):
            return 'algo ha ido mal en el chequeo, no podemos arrancar'

        else:
            return 'el coche esta parado'  
    def estado(self):
        print('el coche tiene: ',self.__ruedas,'ruedas','un ancho de: ',self.__anchochasis,'y un largo de: ', self.__largochasis)      

    #encapsular al metodo asi no se puede acceder desde afuer y queda restringuido a un uso interno
    def __chequeo_interno(self):
        print('realizando chequeo interno')

        self.gasolina = 'o'
        self.aceite  = 'ok'
        self.puertas = 'cerradas'

        if (self.gasolina == 'ok' and self.aceite == 'ok' and self.puertas == 'cerradas'):
            return True
        else:
            return False
        

micoche = coche() #instanziamos

print(micoche.arrancar(True))

print(micoche.estado())

print(micoche.chequeo_interno())

print('--------a continuacion creamos el segundo objeto------------')

micoche2 = coche() #segunda instancia

print(micoche2.arrancar(False))

micoche2.ruedas = 2

print(micoche2.estado())
