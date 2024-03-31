from io import open 

#si no exite open lo crea
archivo_texto=open('archivo.txt','w')
frase = 'estupendo dia para estudiar python \n el miercoles'
archivo_texto.write(frase)
archivo_texto.close() 

#modo leer
archivo_texto = open('archivo.txt','r')
texto = archivo_texto.read()
archivo_texto.close()
print(texto)

#leer lineas
archivo_texto = open('archivo.txt','r')
lineas_texto = archivo_texto.readlines()
archivo_texto.close()
print(lineas_texto)

#modo agregar
archivo_texto = open('archivo.txt','a')
archivo_texto.write("\n siempre es una buena ocasión para estudiar python")
archivo_texto.close()


