import video34modulo

video34modulo.sumar(1,2)
video34modulo.restar(4,3)

from video34modulo import sumar # esto nos permite quitar el nombre del modulo
from video34modulo import restar
sumar(1,2)
restar(4,3)

import video34modulo as fm

fm.sumar(1,2)
fm.restar(4,3)
fm.multiplicar(2,2)