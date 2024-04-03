import numpy as np
import matplotlib.pyplot as plt

# Constantes
k = 8.99e9  # Constante electrostática en N m^2/C^2
q = 1e-9     # Magnitud de la carga en C
d = 1        # Distancia entre las cargas en metros

# Función para calcular el campo eléctrico en un punto (x, y) debido al dipolo
def dipole_field(x, y):
    dx = x
    dy = y
    
    r1 = np.sqrt(dx**2 + dy**2)
    r2 = np.sqrt(dx**2 + (dy - d)**2)
    
    Ex = k * q * (dx / r1**3 - dx / r2**3)
    Ey = k * q * (dy / r1**3 - (dy - d) / r2**3)
    
    return Ex, Ey

# Crea un rango de valores para x y y con mayor densidad
x = np.linspace(-2, 2, 40)
y = np.linspace(-2, 2, 40)

# Crea líneas de corriente siguiendo el campo eléctrico con más puntos
start_points = np.array([[-1.5, 0.5], [-1, -1], [1, 1], [1.5, -0.5]])
num_points = 200
delta_t = 0.05
streamlines = []

for start_point in start_points:
    x, y = start_point
    streamline = [[x, y]]
    for _ in range(num_points):
        Ex, Ey = dipole_field(x, y)
        x += Ex * delta_t
        y += Ey * delta_t
        streamline.append([x, y])
    streamlines.append(np.array(streamline))

# Grafica las líneas de corriente
plt.figure(figsize=(6, 6))
for streamline in streamlines:
    plt.plot(streamline[:, 0], streamline[:, 1], color='red', linewidth=1)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Líneas de Corriente de un Dipolo Eléctrico')
plt.grid(True)
plt.show()

