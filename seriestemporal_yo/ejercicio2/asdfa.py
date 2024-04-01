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
handswing2.hacerGraficas(funcion_sinusoidal,tiempoAcotado,columnasAcotado)


#periodo
pi = np.pi
periodo = 2*pi/(b)
print('el periodo es: ',periodo)