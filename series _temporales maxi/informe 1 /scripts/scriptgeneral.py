
import numpy as np
import os
import csv, datetime
#from scipy.interpolate import interp1d
#from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# voy al direcotrio desde donde voy a trabajar
os.chdir('/home/ludeu/Escritorio/MachineLearning/Data/proyecto/power-consumption')

#creo mi path
archivo = os.path.join("..", "power-consumption","powerconsumption.csv")

#leo el archivo y guardon en data
with open(archivo,"r") as fp:
    reader = csv.reader(fp, delimiter=",")
    data = []
    for row in reader:
        data.append(row)

data = data[1:]

#creo un diccionario para manipular mejor mi archivo

data_dicc = {'TIME': [],
             'TEMP': [],
             'HUM': [],
             'VEL_VIENTO': [],
             'DIFU_GENERAL': [],
             'DIFU': [],
             'CONSUM_ZONA1': [],
             'CONSUM_ZONA2': [],
             'CONSUM_ZONA3': []
             }

cont_menos_datos = 0

for fila in data:
    if len(fila) > 8:
        data_dicc['TIME'].append(datetime.datetime.strptime(fila[0],'%m/%d/%Y %H:%M'))
        data_dicc['TEMP'].append(float(fila[1]))
        data_dicc['HUM'].append(float(fila[2]))
        data_dicc['VEL_VIENTO'].append(float(fila[3]))
        data_dicc['DIFU_GENERAL'].append(float(fila[4]))
        data_dicc['DIFU'].append(float(fila[5]))
        data_dicc['CONSUM_ZONA1'].append(float(fila[6]))
        data_dicc['CONSUM_ZONA2'].append(float(fila[7]))
        data_dicc['CONSUM_ZONA3'].append(float(fila[8]))
    else:
        cont_menos_datos += 1 

# como vemos por cont_menos_datos no hay casillas vacias

#convierto los datos en un array y el tiempo en otro

claves = [clave for clave in data_dicc if clave != 'TIME']

arrays_columnas = [np.array(data_dicc[clave]) for clave in claves]

datos = np.column_stack(arrays_columnas)
time = data_dicc['TIME']

datos[1,:]
datos.shape