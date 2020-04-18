# Ecuaciones simples
# Tenemos tres enteros diferentes x, y y z, los cuales satisfacen las siguientes condiciones:
    # ● x + y + z = A
    # ● xyz = B
    # ● x^2 + y^2 + z^2 =C
    
# Escriba un programa que halle los valores de x, y y z, para valores A, B y C dados por el usuario. Si dichos valores no existen su programa debe imprimir que no existe una solución que satisfaga las condiciones

def main():
    a = eval(input("Digite el valor de A: "))
    b = eval(input("Digite el valor de B: "))
    c = eval(input("Digite el valor de C: "))
    evaluar(a,b,c)

def evaluar(A, B, C):
    cumple = False
    xExitoso = 0
    yExitoso = 0
    zExitoso = 0
    for x in range(-100, 101):
        for y in range(-100, 101):
            for z in range(-100, 101):
                ecuacion1 = primeraEcuacion(x, y, z, A)
                if ecuacion1 == True:
                    ecuacion2 = segundaEcuacion(x, y, z, B)
                    if ecuacion2 == True:
                        ecuacion3 = segundaEcuacion(x, y, z, C)
                        if ecuacion3 == True:
                            cumple = True
                            xExitoso = x
                            yExitoso = y
                            zExitoso = z
    imprimirResultado(xExitoso,yExitoso,zExitoso,cumple)


def primeraEcuacion(x, y, z, A):
    resultado = False
    operacion = x + y + z
    if operacion == A:
        resultado = True
    return resultado

def segundaEcuacion(x, y, z, B):
    resultado = False
    operacion = x * y * z
    if operacion == B:
        resultado = True
    return resultado

def terceraEcuacion(x, y, z, C):
    resultado = False
    operacion = x**2 + y**2 + z**2
    if operacion == C:
        resultado = True
    return resultado

def imprimirResultado(x,y,z,cumple):
    if cumple == True:
        print(f"Los valores de x, y y z que cumples con las ecuaciones son {x} , {y}, {z}")
    else:
        print(f"No hay valores que satisfagan las 3 ecuaciones")

main()