# Le piden hacer un contador de 10 hasta 0 en caso que el mundo se vaya a acabar. No puede utilizar ciclos.

# Cuando contador = 0
# Restar 1 al contador actual.


def main():
    inicioFin = 10 
    contadorFinMundo(inicioFin)

def contadorFinMundo(inicioFin):
    if inicioFin == 0:
        print(0)
    else:
        print(inicioFin)
        return contadorFinMundo(inicioFin-1)

main()