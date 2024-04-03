import pickle

fichero = open('lista_nombres','rb')

#leer la info en binario
lista = pickle.load(fichero)

print(lista)
