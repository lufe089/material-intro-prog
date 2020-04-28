# Escriba un programa en Python que permita crear una lista de n elementos y que, a continuación, pida el valor de un elemento y elimine ese elemento de la lista. Es necesario que elimine todos los elementos de la lista que tengan el mismo valor.

# (numeroUsuario in lista) No se encuentre
# remove

def main():
    listaAleatoria = [2,5,4,2,3,9,5,1,2,3,4]
    numero = 5
    listafinal = eliminarDatos(listaAleatoria, numero)
    print(listafinal)

def eliminarDatos(lista, numeroUsuario):
    if not (numeroUsuario in lista):
        return lista
    else:
        lista.remove(numeroUsuario)
        return eliminarDatos(lista, numeroUsuario)

main()