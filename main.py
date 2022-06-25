

"""
Dado una matriz, con valores de entre 0 o 1.

Objetivo:
Los valores con 1 que esten en el borde de la matriz, deben de ser eliminado
ademas que si esta, tiene una relacion o una pareja de otro 1, de relacion
vertical o horizontal, tambien esta debe de ser eliminado pues esta conlleva una relacion
con el borde.
Al final como resultado debemos de mostrar solo los valor (1) que no tengan ninguna relacion
con el borde ni por medio de otra pareja

Ejemplo:
    Entrada:
        [1, 1, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 1],
        [0, 1, 0, 1, 1, 0],
        [1, 0, 1, 0, 1, 0],
        [1, 0, 0, 0, 0, 0],
        [1, 0, 1, 1, 1, 1],
    Salida:
        [0, 0, 0, 0, 0, 0]
        [0, 0, 0, 0, 0, 0]
        [0, 1, 0, 1, 1, 0]
        [0, 0, 1, 0, 1, 0]
        [0, 0, 0, 0, 0, 0]
        [0, 0, 0, 0, 0, 0]
"""



matriz = [
[1,1,0,1,0,0],
[0,0,0,0,0,1],
[0,1,0,1,1,0],
[1,0,1,0,1,0],
[1,0,0,0,0,0],
[1,0,1,1,1,1],
]
def separarIslas(matriz):
    # los limites
    numColum = len(matriz[1])
    numRow = len(matriz)
    def filtro(ro,co):
        if(ro>=numRow or ro<0 or co >= numColum or co<0): return False
        else:
            if(matriz[ro][co]==1):verAlrededor(ro,co)
    def verAlrededor(row,colm):
        # desactivamos los uno de la matriz
        matriz[row][colm] = 0
        # registrar sus alrededores
        filtro(row-1,colm) # arriba
        filtro(row+1,colm) # abajo
        filtro(row,colm+1) # izquierda
        filtro(row,colm-1) # derecha

    for row in range(0,numRow):
        for colm in range(0,numColum):
            # encontrar todas las posiciones que estan en el borde
            if(row== 0 or colm == 0 or row== numRow-1 or colm == numRow-1 or row== numColum-1or colm == numColum-1):
                # las posiciones que tiene uno como valor
                if(matriz[row][colm] == 1):
                    verAlrededor(row,colm)
    return matriz
# mostrar la matriz
for value in separarIslas(matriz):
    print(value)
