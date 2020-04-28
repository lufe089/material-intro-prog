# Realice una función recursiva que permita calcular el MCD (máximo común divisor) de dos números enteros positivos utilizando el Algoritmo de Euclides: 
# Algoritmo de Euclides: Dados dos números enteros positivos m y n, tal que m > n, para encontrar su máximo común divisor (es decir, el mayor entero positivo que divide a ambos): 
# • Dividir m por n para obtener el resto r (0 ≤ r < n) 
# • Si r = 0, el MCD es n 
# • Si no, el máximo común divisor es MCD (n,r)

def main():
    print("Bienvenido a la calculadora del MCD por el método de Euclides")
    print("Recuerde que debe digitar 2 enteros positivos y que el primero debe ser mayor al segundo")
    datosCorrectos = False 
    while datosCorrectos == False:
        m = eval(input("Digite el primer número: "))
        n = eval(input("Digite el segundo número: "))
        datosCorrectos = evaluarCondiciones(m, n)
    mcd = MCD(m ,n)
    print(f"El MCD de {m} y {n} es {mcd}")
    
def evaluarCondiciones(m, n):
    resultado = False
    if (m > n) and (m > 0) and (n > 0):
        resultado = True
    else:
        print("Las condiciones de los números no son correctas")
    return resultado

def MCD(m, n):
    residuo = m % n
    if residuo == 0:
        return n
    else:
        return MCD(n, residuo)

main()