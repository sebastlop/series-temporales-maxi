from io import open

archivo_texto = open('archivo.txt', 'r')
#por defecto el puntero se ubica en la primera posicion del archivo
#en python podemos desplazar el cursor

#metodo seek(5)el puntero en la posicion 5


archivo_texto.seek(len(archivo_texto.read())/2)
print(archivo_texto.read())


 