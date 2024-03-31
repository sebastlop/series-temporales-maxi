for letra in 'python':

    if letra == 'h':
        continue
    print('viendo la letra: '+ letra)


#como saltar lineas de codigo en algunas iteraciones con continue
nombre = 'pildoras informaticas' 

print(len(nombre)) # al espacio blanco se lo cuenta  como cáracter

contador =  0

for i in nombre:
    
    if i==' ':
        continue
    contador += 1
print(contador)    

#usar la instruccion pass
#se utiliza en casos muy concretos

#bucle infinito
#while True:
#   pass

class miclase:
    pass # para implementar mas tarde

email = input('introduce tu email: ')

for i in email:
    if i =='@':
        arroba = True
        break
else:#este else forma parte del bulce for y no del if 
    arroba = False 
print(arroba) 