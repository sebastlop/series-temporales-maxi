
from scipy import interpolate
from scipy.optimize import curve_fit
import numpy as np 
import matplotlib.pyplot as plt

class seriesejercicio():
    tiempo = []
    columnas = []
    rutadelarchivo = ''
    titulos = []

    def leerdatos(self,rutadelarchivo):
        #apertura de datos
        fichero = open(rutadelarchivo, 'r')
        #volcado de datos
        self.titulos = fichero.readline().strip().split(';')
        fichero.seek(0)#me da los titulos en una lista
        datos = np.genfromtxt(fichero, delimiter=';')# me da lo demas en un array
        #cierre
        fichero.close()
        #borrar de la memorira
        del fichero       

        #tratamiento de datos
        self.tiempo = datos[1:,0]
        self.columnas = datos[1:,1:]

        return datos
    
    def interpolacionColumna(self,funcion,tiempo,columna,semillas):
        popt, pcov =curve_fit(funcion,tiempo,columna,semillas) 
        
        return popt
    
    def hacerGraficas(self,funcion,x,columnas,semillas,nombregrafica):
        # Crear subgráficas
        numeroGraficas = len(self.titulos) - 1
        fig, axs = plt.subplots(numeroGraficas)

        for i in range(numeroGraficas):
            axs[i].plot(x,columnas[0:,i])

            # Trazar cada gráfica en su subgráfica correspondiente

            parametros = self.interpolacionColumna(funcion,x,columnas[0:,i],semillas) 
            
            y = funcion(x, *parametros)
            axs[i].plot(x, y)
            axs[i].set_title(self.titulos[i+1])

        # Ajustar los márgenes
        plt.tight_layout()
    
        # Mostrar la gráfica
        plt.savefig('{}.png'.format(nombregrafica))
        plt.show()

#-------------------------------------------------------------------#
oscilador = seriesejercicio()
datos = oscilador.leerdatos('oscilador.csv')       

#acoto el rango de valores en donde la oscilación sea mas estable.
tiempo_mask= (oscilador.tiempo  > 5) & (oscilador.tiempo < 25) 

# aplico la mascara sobre el timepo y la fuerza total.
tiempoAcotado = oscilador.tiempo[tiempo_mask]
columnasAcotado =oscilador.columnas[tiempo_mask]

def funcion_sinusoidal(x, a, b, c, d):
    return a * np.sin(b * x + c) + d
#graficas
oscilador.hacerGraficas(funcion_sinusoidal,tiempoAcotado,columnasAcotado,(0.5,6,0.5,0.5),'oscilador')

#interpolacion con la ultima columna
popt = oscilador.interpolacionColumna(funcion_sinusoidal,tiempoAcotado,columnasAcotado[0:,3],(0.5,6,0.5,0.5))
w = popt[2]
#periodo
pi = np.pi
periodo = 2*pi/(w)
print('el periodo es: ',periodo)

#largo de la cinta
l = (9.8)/(w)**2
print('el largo de la cinta es: ', l)

#-------------------------------------------------------------------#

caminata = seriesejercicio()
datos = caminata.leerdatos('caminata-ejemplo.csv')       

#acoto el rango de valores en donde la oscilación sea mas estable.
tiempo_mask= (caminata.tiempo  > 5) & (caminata.tiempo < 25) 

# aplico la mascara sobre el timepo y la fuerza total.
tiempoAcotado = caminata.tiempo[tiempo_mask]
columnasAcotado =caminata.columnas[tiempo_mask]

def funcion_sinusoidal(x, a, b, c, d):
    return a * np.sin(b * x + c) + d
#graficas
caminata.hacerGraficas(funcion_sinusoidal,tiempoAcotado,columnasAcotado,(0.5,6,0.5,0.5),'caminata')

#interpolacion
popt = caminata.interpolacionColumna(funcion_sinusoidal,tiempoAcotado,columnasAcotado[0:,3],(0.5,6,0.5,0.5))
w = popt[2]
#periodo
pi = np.pi
periodo = 2*pi/(w)
print('el periodo es: ',periodo)

#-------------------------------------------------------------------#

frec_var = seriesejercicio()
datos = frec_var.leerdatos('frec-var.csv')       

#acoto el rango de valores en donde la oscilación sea mas estable.
tiempo_mask= (frec_var.tiempo  > 5) & (frec_var.tiempo < 25) 

# aplico la mascara sobre el timepo y la fuerza total.
tiempoAcotado = frec_var.tiempo[tiempo_mask]
columnasAcotado =frec_var.columnas[tiempo_mask]

def funcion_sinusoidal(x, a, b, c, d):
    return a * np.sin(b * x + c) + d
#graficas
frec_var.hacerGraficas(funcion_sinusoidal,tiempoAcotado,columnasAcotado,(0.5,6,0.5,0.5),'frec-var')

#interpolacion
popt = frec_var.interpolacionColumna(funcion_sinusoidal,tiempoAcotado,columnasAcotado[0:,3],(0.5,6,0.5,0.5))
w = popt[2]
#periodo
pi = np.pi
periodo = 2*pi/(w)
print('el periodo es: ',periodo)


#-------------------------------------------------------------------#

golpes_escritorio = seriesejercicio()
datos = golpes_escritorio.leerdatos('golpes-escritorio.csv')       

#acoto el rango de valores en donde la oscilación sea mas estable.
tiempo_mask= (golpes_escritorio.tiempo  > 5) & (golpes_escritorio.tiempo < 25) 

# aplico la mascara sobre el timepo y la fuerza total.
tiempoAcotado = golpes_escritorio.tiempo[tiempo_mask]
columnasAcotado =golpes_escritorio.columnas[tiempo_mask]

def funcion_sinusoidal(x, a, b, c, d):
    return a * np.sin(b * x + c) + d
#graficas
golpes_escritorio.hacerGraficas(funcion_sinusoidal,tiempoAcotado,columnasAcotado,(0.5,6,0.5,0.5),'golpes-escritorio')

#interpolacion
popt = golpes_escritorio.interpolacionColumna(funcion_sinusoidal,tiempoAcotado,columnasAcotado[0:,3],(0.5,6,0.5,0.5))
w = popt[2]
#periodo
pi = np.pi
periodo = 2*pi/(w)
print('el periodo es: ',periodo)

#-------------------------------------------------------------------#


handswing = seriesejercicio()
datos = handswing.leerdatos('handswing.csv')       

#acoto el rango de valores en donde la oscilación sea mas estable.
tiempo_mask= (handswing.tiempo  > 5) & (handswing.tiempo < 25) 

# aplico la mascara sobre el timepo y la fuerza total.
tiempoAcotado = handswing.tiempo[tiempo_mask]
columnasAcotado =handswing.columnas[tiempo_mask]

def funcion_sinusoidal(x, a, b, c, d):
    return a * np.sin(b * x + c) + d
#graficas
handswing.hacerGraficas(funcion_sinusoidal,tiempoAcotado,columnasAcotado,(0.5,6,0.5,0.5),'handswing')

#interpolacion
popt = handswing.interpolacionColumna(funcion_sinusoidal,tiempoAcotado,columnasAcotado[0:,3],(0.5,6,0.5,0.5))
w = popt[2]
#periodo
pi = np.pi
periodo = 2*pi/(w)
print('el periodo es: ',periodo)

#-------------------------------------------------------------------#


handswing2 = seriesejercicio()
datos = handswing2.leerdatos('handswing2.csv')       

#acoto el rango de valores en donde la oscilación sea mas estable.
tiempo_mask= (handswing2.tiempo  > 5) & (handswing2.tiempo < 25) 

# aplico la mascara sobre el timepo y la fuerza total.
tiempoAcotado = handswing2.tiempo[tiempo_mask]
columnasAcotado =handswing2.columnas[tiempo_mask]

def funcion_sinusoidal(x, a, b, c, d):
    return a * np.sin(b * x + c) + d 
#graficas
handswing2.hacerGraficas(funcion_sinusoidal,tiempoAcotado,columnasAcotado,(0.5,6,0.5,0.5),'handswing2')

#interpolacion
popt = handswing2.interpolacionColumna(funcion_sinusoidal,tiempoAcotado,columnasAcotado[0:,3],(0.5,6,0.5,0.5))
w = popt[2]
#periodo
pi = np.pi
periodo = 2*pi/(w)
print('el periodo es: ',periodo)

             

