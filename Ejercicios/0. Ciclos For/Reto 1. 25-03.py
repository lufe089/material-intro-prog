#Los números primos son números que únicamente son divisibles por 1 y por si mismos, por ejemplo:
#* 7 -> Solo es divisible por 7 y por 1.
#Los primeros números primos son: 2,3,5,7,11,13,17,19,23,29,37.....

#Le han solicitado crear un programa donde el usuario digita un número de 1 a 100 y se imprimen todos los números primos hasta ese número. Para ello le solicitan:

#- Cree una función que calcule si un número es primo o no. Debe enviar como entrada el número y devolver un valor boolean (false o true)
#- Cree una función que realice el ciclo de todos los números e invoque la función anterior para saber si debe imprimir el número o no.
#- Cree un procedimiento (main) donde se solicite al usuario el número límite y se invoque la función 2 para imprimir los primos. 

def main():
    numeroUsuario = eval(input(" Dígite un número entre 1 y 100: "))
    while numeroUsuario > 100 or numeroUsuario < 1:
        numeroUsuario = eval(input(" Dígite un número entre 1 y 100: "))
    recorrer(numeroUsuario)
    
    
def recorrer(limite):
    for i in range(2, limite + 1):
        validacionPrimo = primos(i)
        if validacionPrimo == True:
           print(f"El número {i} es primo")

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

main()