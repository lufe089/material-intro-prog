# Haga un programa que imprima el recorrido de una matriz en forma de culebra.
# Ejemplo
# Dada la siguiente matriz:

# 1 [[1, 2, 3, 4, 5],
# 2 [6, 7, 8, 9, 10],
# 3 [11, 12, 13, 14, 15],
# 4 [16, 17, 18, 19, 20],
# 5 [21, 22, 23, 24, 25]]

# Su programa debe imprimir:
# 1 2 3 4 5 10 9 8 7 6 11 12 13 14 15 20 19 18 17 16 21 22 23 24 25

def main():
    matriz = [[1, 2, 3, 4, 5],[6, 7, 8, 9, 10],[11, 12, 13, 14, 15],[16, 17, 18, 19, 20],[21, 22, 23, 24, 25], [26, 27, 28, 29, 30]]
    #m[0] = [1, 2, 3, 4, 5]
    #m[4] = [21, 22, 23, 24, 25]
    recorrerMatriz(matriz)

def recorrerMatriz(m):
    cantidadFilas = len(m)
    for i in range(0,cantidadFilas):
        numeroFila = i + 1
        if numeroFila % 2 == 0:
            recorrerAtras(m[i])
        else:
            recorrerAdelante(m[i])

def recorrerAdelante(l):
    cantidadColumnas = len(l)
    for j in range (0, cantidadColumnas):
        print(f"{l[j]} ")

def recorrerAtras(l): #5
    cantidadColumnas = len(l) - 1
    while cantidadColumnas >= 0:
        print(f"{l[cantidadColumnas]}")
        cantidadColumnas -= 1

main()