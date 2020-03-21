def ejemploFactorial(num):
    if num == 0:
        return 1
    else:
        return num * ejemploFactorial(num-1)

def ejemploFactorialMensajes(num):
    if num == 0:
        print("Entre al caso base")
        print ("Voy a retornar", 1)
        return 1
    else:
        print ("Entre al caso general")
        print("Num vale ", num, " Voy a a llamar a la funcion con ", num-1)
        resultado = num * ejemploFactorial(num-1)
        print ("Voy a retornar de resultado ", resultado)
        return resultado

def calcularPotenciaIterativo(base,exponente):
    potencia =1
    while exponente > 0:
        potencia = base * potencia
        exponente -= 1
    return potencia

def calcularPotenciaRecursivo(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * calcularPotenciaRecursivo(base, exponente-1)


def calcularPotenciaRecursivoMensajes(base, exponente):
    if exponente == 0:
        print ("Caso base")
        return 1
    else:
        print ("Caso general")
        print ("Exponente actual ", exponente)
        print("Exponente a llamar a la funcion ", exponente-1)
        resultado = base * calcularPotenciaRecursivo(base, exponente-1)
        print ("Resultado ", resultado)
        return resultado

def contarMultiplosTresRecursivo(numActual):
    if numActual == 3:
        return 1
    else:
        if numActual % 3 == 0:
            return 1 + contarMultiplosTresRecursivo(numActual-1)
        else:
            return 0 + contarMultiplosTresRecursivo(numActual-1)

def contarMultiplosTresRecursivoMensajes(numActual):
    if numActual == 3:
        print("Ingrese al caso base ")
        return 1
    else:
        if numActual % 3 == 0:
            print("El numActual es", numActual, "y es múltiplo")
            resultado = 1 + contarMultiplosTresRecursivoMensajes(numActual-1)
            print ("El resultado es ", resultado)
        else:
            print("El numActual es", numActual, "y no es múltiplo")
            resultado = 0 + contarMultiplosTresRecursivoMensajes(numActual - 1)
            print("El resultado es ", resultado)
        return resultado

def sumarMultiplosDeTres(numActual):
    if numActual == 0:
        return 0
    else:
        if numActual % 3 == 0:
            return numActual + sumarMultiplosDeTres(numActual-1)
        else:
            return sumarMultiplosDeTres(numActual-1)

def sumarMultiplosDeTresMensajes(numActual):
    if numActual == 0:
        print("Caso base ")
        return 0
    else:
        print ("Caso general")
        print("num Actual vale ", numActual)
        if numActual % 3 == 0:
            print ("Es múltiplo. Suma y hace la llamada recursiva")
            resultado = numActual + sumarMultiplosDeTresMensajes(numActual-1)
            print ("El resultado es ", resultado)
            return resultado
        else:
            print ("No es múltiplo, solo hace la llamada recursiva")
            resultado = sumarMultiplosDeTresMensajes(numActual-1)
            print("El resultado es ", resultado)
            return resultado


"""Aqui se puede preguntar a los estudiantes que pasa si la condicion de parada no se hace con num<=9 sino con numero <10. 
Rta python arroja un error pq se llega a un nivel máximo de recursión. Qué pasa si el número de la condición de parada es <= 10. Por ejemplo si se prueba con 100. Rta
La suma de los numeros da mal, pq debería dar 1."""
def sumarDigitosNum(num):
    if num <= 9:
        return num
    else:
        residuo = sumarDigitosNum(num%10)
        return residuo + sumarDigitosNum(num//10)


"""Aqui se puede preguntar a lo esudiantes que pasa si se cambia el orden entre el llamado del print y la llamada a la conversión del número binario"
La respuesta es que el numero binario sale invertido. La otra cosa que se puede preguntar es que pasa si se agrega una condición de parada como 
num == 2. La respuesta es que cuando se hace la conversión al binario, el número binario queda incompleto pq hace falta una llamada recursiva. """
def convertirBinario(num):
    if num == 1:
        print(1) # El mumero no es divisible exactamente
    elif num == 0:
        print(0)
    else:
        modulo =  num % 2
        convertirBinario(num // 2)
        print(modulo)



### Funciones para probar las funcionalidades recursivas

def probarSumarDigitos():
    sumaTotal=sumarDigitosNum(85)
    print("La suma de los digitos es ", sumaTotal)

def probarPotencia():
    base = int(input("Ingrese la base "))
    exponente = int(input("Ingrese el exponente "))
    resultado = calcularPotenciaRecursivoMensajes(base,exponente)
    resultadoIterativo = calcularPotenciaIterativo(base,exponente)
    print("El resultado recursivo ", resultado)
    print("El resultado iterativo ", resultadoIterativo)

def probarFactorial():
    resultado = ejemploFactorialMensajes(0)
    print("El factorial de cero es ", resultado)

    print (" UN CASO MAS GRANDE")
    resultado = ejemploFactorialMensajes(4)
    print("El factorial de 4 es ", resultado)

def probarSumarMultiplosDeTres():
    num = int(input("Ingrese el intervalo superior "))
    sumaMultiplos = sumarMultiplosDeTresMensajes(num)
    print("La sumatoria de los números múltiplos de tres de 0 hasta ", num, " es:", sumaMultiplos)

def probarContarMultiplosDeTres():
    num = int(input("Ingrese el intervalo superior "))
    contadorMultiplos = contarMultiplosTresRecursivoMensajes(num)
    print("La cantidad de numeros multiplos de tres es ", contadorMultiplos)

convertirBinario(85)