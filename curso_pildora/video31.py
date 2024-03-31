class persona():

    def __init__(self, nombre, edad, lugar_residencia):
        self.nombre = nombre
        self.edad = edad
        self.lugar_residencia = lugar_residencia
    
    def descripcion(self):
        print('nombre: ', self.nombre, 'edad: ', self.edad, 'lugar de residencia: ', self.lugar_residencia)

class empleado(persona):

    def __init__(self, salario, antigüedad, nombre_empleado, edad_empleado, residencia_empleado):
        super().__init__(nombre_empleado, edad_empleado, residencia_empleado)
        self.salario = salario
        self.antigüedad = antigüedad        

    def descripcion(self):
        super().descripcion()
        print('salario: ', self.salario, 'antigüedad: ', self.antigüedad)    


antonio = persona('antonio', 55, 'españa')
antonio.descripcion()

antonio = empleado(1500, 15, 'manuel', 55, 'colombia')
antonio.descripcion()

manuel = persona('manuel' , 55, 'colombia')

print(isinstance(manuel, empleado))