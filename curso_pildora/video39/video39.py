import pickle

lista_nombres = ['pedro','ana', 'maria','isabel']

#crear fichero externo acceso de escritura binario

fichero_binario = open('lista_nombres','wb')

#volcado de la lista al fichero

pickle.dump(lista_nombres, fichero_binario)

fichero_binario.close()

del(fichero_binario) 