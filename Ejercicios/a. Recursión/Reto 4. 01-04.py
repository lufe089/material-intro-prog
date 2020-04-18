# La serie de fibonnaci se obtiene de la siguiente manera: 

# El primer número de la serie es 1 
# El segundo número de la serie también es 1 
# El tercer número de la serie es la suma de los dos anteriores, es decir, 2 
# El cuarto número de la serie es la suma de los dos anteriores, es decir, 3 
# Y así sucesivamente.
# De esta manera, la serie luce de esta manera: 1, 1, 2, 3, 5, 8, 13, 21, 34, . . . 
# La definición matemática recursiva de esta formula es la siguiente:
#  F(0) = 1 F(1) = 1 F(n) = F(n - 1) + F(n - 2)
# Realice una función recursiva que calcule el n-ésimo número de fibonacci, donde n debe ser un parametro de la función que realice

def main():
    posicion = eval(input("Qué número de la serie fibonacci desea obtener (posición): "))
    resultado = fibonacciRecursivo(posicion)
    print(f"El resultado de la serie para la posición {posicion} es {resultado}")

def fibonacciRecursivo(n):
    if n < 2:
        return n
    else:
        return fibonacciRecursivo(n-1) + fibonacciRecursivo(n-2)

main()