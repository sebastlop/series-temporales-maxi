# diccionario con keys del tipo texto

midiccionario = {'alemania':'berlin','francia':'paris','reino unido':'londres','españa':'madrid','argentina':'buenos aires'}

print(midiccionario['francia'])#le doy la clave y me decuelve el valor
print(midiccionario['españa'])

print(midiccionario)#me imprime todo

#agredar elementos

midiccionario['italia']='lisboa'
print(midiccionario)

#quiero corregir o cabiar un valor

midiccionario['italia']='roma'
print(midiccionario) 

del midiccionario['reino unido']
print(midiccionario)

#puedo agregar numeros

midiccionario[23]='jordan'
print(midiccionario)

#uso una tupla como keys y le asigno valores

mitupla= 'españa', 'francia', 'alemania'
midiccionario={mitupla[0]:'maadrid',mitupla[1]:'francia', mitupla[2]:'berlin'}
print(midiccionario)

#asignar a una key una tupla de valores

midiccionario = {23:'jordan','nombre':'michael','equipo':'chicago','anillos':[1991,1992,1993,1996,1997,1998]}
print(midiccionario['equipo'])
print(midiccionario['anillos'])

#asignar a una key un diccionario

midiccionario = {23:'jordan','nombre':'michael','equipo':'chicago','anillos':{'temporadas':[1991,1992,1993,1996,1997,1998]}}
print(midiccionario['anillos']['temporadas'])
                 
#metodos

print(midiccionario.keys())
print(midiccionario.values())
print(len(midiccionario))