from tkinter import *

raiz = Tk()


raiz.title('ventana de prueba')

raiz.resizable(1,1)

raiz.iconbitmap('toad.icns')

#raiz.geometry('650x350')
#la raiz siempre se va a adapatar al tampaño de si frames
raiz.config(bg='blue')

miframe = Frame()
miframe.config(bg='red')
miframe.config(width='650', height='350' )


miframe.pack(side = 'right', anchor = 'se')



#esta sentencia debe estar al ultimo
raiz.mainloop() #una ventana para que pueda estar en ejecucion tiene que estar en un bucle infinito
