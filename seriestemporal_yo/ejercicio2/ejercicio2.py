from scipy import interpolate
import numpy as np 

class seriesejercicio():
    tiempo = []
    columnas = []
    rutadelarchivo = ''

    def leerdatos(self,rutadelarchivo):
        fichero = open(rutadelarchivo, 'r')
        datos = []

        for linea in fichero:
            columnas = linea.strip().split(';')
            datos.append(columnas)

        datos.remove(datos[0])

        fichero.close()
        del(fichero)

        print('tiempo y columnas han sido guardados correctamente')
        
        columnatiempo = [fila[0] for fila in datos]
        self.tiempo = [float(i) for i in columnatiempo]

        numero_de_columnas = len(datos[0])
        self.columnas = [[] for _ in range(numero_de_columnas)]

        for fila in datos:
            for indice, valor in enumerate(fila):
                self.columnas[indice].append(valor) 


        return datos
    



miserie = seriesejercicio()
datos = miserie.leerdatos('oscilador.csv')       
print(type(datos))





