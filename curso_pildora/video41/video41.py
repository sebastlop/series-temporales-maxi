import pickle

class persona():
    def __init__(self, nombre, genero, edad):
        self.nombre = nombre
        self.genero = genero
        self.edad = edad
        print('se ha craeado una persona nueva con el nombre de: ', self.nombre)


    def __str__(self):
        return '{} {} {}'.format(self.nombre, self.genero, self.edad)    
#el metodo __str__ es un metodo especial de python que convierte la informacion en cadenas de strings
#.format se utiliza para fomatear candenas de texto  
#formatear significa dar estructura

#ejemplo de format

nombre = 'maxi'
edad = 30 

saludo = 'hola me llamo {} y tengo {} años.'.format(nombre,edad)
print(saludo)

##seguimos


#queremos ir creando personas y que se vayan almacenando en un futuro en el fichero
#externo
#que se guarden en una lista

class listapersonas():

    personas = []

    def __init__(self):#constructor 

        listadepersonas = open('ficheroexterno','ab+')
        listadepersonas.seek(0)

        try:
            self.personas = pickle.load(listadepersonas)
            print('se cargaron {} personas del fichero externo'.format(len(self.personas)))
        except:
            print('el fichero esta vacio')
        finally:
            listadepersonas.close()
            del(listadepersonas)

    
    

    def agregarpersona(self, p):
        self.personas.append(p)

    def mostrarpersonas(self):
        for p in self.personas:
            print(p)
    def guardarpersonasenficheroexterno(self):
        listapersonas=open('ficheroexterno','wb') 
        pickle.dump(self.personas, listapersonas)   
        del(listapersonas)

    def mostrarinfoficheroexterno(self):
        print('la informacion del fichero externo es la siguiente: ') 
        for p in self.personas:
            print(p)   

milista = listapersonas()

p = persona('gisel','femenino',29)
milista.agregarpersona(p)

p = persona('antonio','masculino',39)
milista.agregarpersona(p)

p = persona('ana','femenino',19)
milista.agregarpersona(p)

milista.mostrarpersonas()

milista.guardarpersonasenficheroexterno()

milista.mostrarinfoficheroexterno()

#este script se puede volver ultilizar para guardar datos
#de forma atemporal