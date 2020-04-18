# INVERIR NÚMERO

# La inversión de un número n se define como invertir de orden sus digitos. Por ejemplo, el número 1328727 invertido equivale al número 7278231.
# Realice una función RECURSIVA que invierta un número n cualquiera. Puede asumir que el número no tiene mas de 20 digitos, pero recuerde que su programa debe hacerlo de forma general(no para un número determinado de digitos). El número n debe ser un parametro de la función que realice.

def main():
    numero = eval(input("Digite un número: "))
    resultado = invertirNumero(numero)
    print(f"El número invertido es : {resultado}")

def invertirNumero(numero):
    if numero < 10:
      return numero
    else:
      x = numero % 10
      y = numero // 10
      return str(x) + str(invertirNumero(y))
    
main()