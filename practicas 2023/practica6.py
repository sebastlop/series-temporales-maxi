"""
pintar una escalera con *

*
**
***
****
*****

pintar un cuadrado con *

* * * * * *
*         *
*         *
*         *
* * * * * *

"""

altura = 10

for fila in range(altura):
    for columna in range(fila + 1):
        print("* ",end="")
    print()

lado = 5

for fila in range(lado):
    for columna in range(lado):
        if fila == 0 or fila == lado -1 or columna == 0 or columna == lado - 1:
            print("* ", end="")
        else:
            print("  ", end="")
    print()

