class Persona:
    def __init__(self, nombre, edad): #estos son atributos
        self.nombre = nombre
        self.edad = edad

    def saludar(self): #este es un metodo 
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")

# Crear una instancia de la clase Persona
persona1 = Persona("Juan", 30)

# Llamar al método saludar usando self
persona1.saludar()
