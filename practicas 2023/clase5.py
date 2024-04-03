class particulas:
    '''Clase para mejorar un sistema de particulas'''
    def __init__(self, num_particulas=2, **kwargs): #Este es el constructor de la clase. la palabra clave self refiere a todas las variables y metodos que son propios de la clase
        assert num_particulas > 0, 'el primer argumento es el numero de particulas y debe ser entero mayor a 0'
        self.n = num_particulas
        self.espacio_fase = []

    def crea_espacio_fase(self): #este es un metodo
        '''metodo para construir las listas de posiciones y momentos todas con 0'''
        for i in range(self.n):
            self.espacio_fase.append([[0,0,0],[0,0,0]]) #a todas las particulas las pongo en el origen

    def provee_espacio_fase(self,*args):
        '''metodo para cargar un espacio de fase desde afuera'''
        self.espacio_fase = args[0]

sistema1 = particulas(3) #creo un objeto llamado sistema1 de la clase particulas con n=3
print(sistema1)
print(sistema1.espacio_fase, '<--- vacia') #imprimo la lista espacio_fase
sistema1.crea_espacio_fase() #ejecuto el metodo para crear espacio de fase
print(sistema1.espacio_fase, '<--- creamos el espacio de fase de 3 particulas en el origen con velocidad 0')
       
