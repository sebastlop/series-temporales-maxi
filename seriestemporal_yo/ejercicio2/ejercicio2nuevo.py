from scipy import interpolate
import numpy as np 

class seriesejercicio():
    tiempo = []
    columnas = []
    rutadelarchivo = ''

    def leerdatos(self,rutadelarchivo):
        #apertura de datos
        fichero = open(rutadelarchivo, 'r')
        #volcado de datos
        datos = np.array(fichero)
        #cierre
        fichero.close()
        #borrar
        del fichero       

        #tratamiento de datos

        self.tiempo  =  datos[:,1]


        return datos
    



miserie = seriesejercicio()
datos = miserie.leerdatos('oscilador.csv')       
print(type(datos))
print(datos.size)





