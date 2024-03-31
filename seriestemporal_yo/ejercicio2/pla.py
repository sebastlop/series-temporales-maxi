handswing2 = seriesejercicio()
datos = handswing2.leerdatos('handswing2.csv')       


def funcion_sinusoidal(x, a, b, c, d):
    return a * np.sin(b * x + c) + d
x = handswing2.tiempo 
y = funcion_sinusoidal(x,a,b,c,d)


numeroGraficas = len(handswing2.titulos) - 1
# Crear subgráficas
fig, axs = plt.subplots(numeroGraficas)

# Trazar cada gráfica en su subgráfica correspondiente
for i in range(numeroGraficas):
    parametros = handswing2.ajustarFuncion(funcion_sinusoidal,handswing2.columnas[0:,i])
    a ,b , c, d = parametros 
    axs[i].plot(x, y)
    axs[i].set_title(handswing2.titulos[i+1])

# Ajustar los márgenes
plt.tight_layout()

# Mostrar la gráfica
plt.show()
plt.savefig('grafico handswing2.png')

#periodo

pi = np.pi
periodo = 2*pi/b
print('el periodo es: ',periodo)