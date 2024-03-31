class coche():
    #propiedades --> atributos
    largochasis = 250
    anchochasis = 120
    ruedas = 4
    enmarcha = False #en principio esten por defecto detenidos
    #comportamiento --> metodos
    def arrncar(self):
        self.enmarcha = True

    def estado(self):
        if (self.enmarcha):
            return 'el coche esta en marcha'
        else:
            return 'el coche esta parado'        

        

micoche = coche() #instanziamos

print('el largo del coche es: ',micoche.largochasis)
print('el coche tiene: ',micoche.ruedas,'ruedas')

#micoche.arrncar()

print(micoche.estado())

micoche.ruedas = 2

print(micoche.ruedas)
