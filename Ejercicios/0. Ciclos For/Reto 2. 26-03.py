# NUMEROS ABUNDANTES

# Un número abundante es un número N tal que la suma de los números primos menores o iguales a el, cumpliendo todos la condición de que tengan al menos un digito "1" entre sus cifras, es mayor que 2N. Por ejemplo 17 es un número abundante ya que 11 + 13 + 17 = 41, donde 41 > 17*2 y además todos los números primos incluidos en la suma son en efecto primos menores o iguales a 41 y además tienen al menos un digito "1" entre sus cifras.

# A. Realice una función que reciba como parametro un número n y retorne True si ese número tiene al menos un digito "1" entre sus cifras o False en caso contrario.

# B. Realice la función sumaPrimos que dado un número n, retorna la suma de los números primos menores o iguales a n. Recuerde que en el anterior reto usted realizó una función muy parecida a esta :).

# C. Realice la función numeroAbundante que toma como parámetro un número natural n y retorna True si es un número abundante y False de lo contrario.

def main():
    for i in range(100):
        sumaTotal = sumaPrimos(i)
        numeroAbundante(i, sumaTotal)

def identificarUnos(k):
    numeroS = str(k)
    resultado = "1" in numeroS  # "1" in "25" = False  -> "1" in "31" = False
    return resultado

def sumaPrimos(n):
    acumuladorPrimos = 0
    for i in range(2, n+1):
        validarPrimo = primos(i)
        if validarPrimo == True:
            validarUno = identificarUnos(i)
            if validarUno == True:
                acumuladorPrimos += i
    return acumuladorPrimos

def primos(numero):  
    contadorDivisores = 0
    resultado = False
    for j in range(1, numero + 1):
        operacion = numero%j # División Exacta
        if operacion == 0:
            contadorDivisores += 1
    if contadorDivisores == 2:
        resultado = True
    return resultado

def numeroAbundante(n, sumaPrimos):
    if sumaPrimos > 2*n:
        print(f" El número {n} es un numero abundante")
    else:
        print(f" El número {n} no es un numero abundante")

main()