# Debido al aumento en la obesidad en los niños una empresa contra los dulces llamada SInoMelaSeMeLasInvento S.A. quiere poner una ley para que los niños no puedan salir a pedir dulces en Halloween.
# Los defensores de los dulces desean demostrarle a la empresa SInoMelaSeMeLasInvento S.A. que los niños no comen tantos dulces como ellos creen y que son los padres los que terminan aprovechando la recolección; mientras que ellos controlan lo que le dan a sus hijos. Para ello, ud debe crear un programa que pregunte la información siguiente información a N familias:
# Cantidad de hijos, cantidad de dulces recogidos, cantidad de dulces que cada niño comió, cantidad de dulces que se regalaron.
# A partir de esa información, ud debe completar la lista con:
# Porcentaje de dulces consumidos por niños, porcentaje de dulces consumidos por invitados y porcentaje de dulces consumidos por los padres.

# Cuando termine de solicitar la información, ud tendrá una matriz con todos los datos necesarios para hacer un estudio y así no permitir que la empresa SInoMelaSeMeLasInvento S.A. prohiba Halloween. Para ello ud mostrará los siguientes datos:

# Cantidad de familias con un porcentaje mayor de 50% de consumo de dulces por parte de los niños
# Cantidad de familias con un porcentaje mayor de 50% de consumo de dulces por parte de los invitados
# Cantidad de familias con un porcentaje mayor de 50% de consumo de dulces por parte de los padres
# Cantidad de dulces totales
# Cantidad de dulces comidos por niños en total
# Cantidad de dulces comidos por invitados en total
# Cantidad de dulces comidos por adultos en total
# Promedio de dulces comidos por niños y por adultos en total en cada familia.
# Porcentaje de dulces comidos por niños en total
# Porcentaje de dulces comidos por adultos en total
# Debe agregar todos los datos calculados a un diccionario.

# Construya una función que reciba como parámetros (entradas) un diccionario, un variable correspondiente a la llave y una variable correspondiente al valor. Esta función debe agregar dentro del diccionario la nueva llave valor y devolver el diccionario modificado.
# Construya una función que tome el diccionario e imprima la información del estudio
# Recuerde mantener la responsabilidad de las funciones. (Una función solo debe realizar una acción específica.)

# Familias= [[cantidadHijos, cantidadDulces, (sumatoria dulces niños), cantidadDulcesRegalados, cantidadDulcesPadres, porcentajeDulcesNiños, porcentajeDulcesInvitados, porcentajeDulcesAdultos], [...]]

def main():
    cantidadFamilias = eval(input("Digite la cantidad de familias del estudio: "))
    familias = solicitarDatosFamilia(cantidadFamilias)
    calculosEstudio(familias)

def solicitarDatosFamilia(cantidadFamilias): #10
    matrizFamilias = []
    for i in range(0, cantidadFamilias):
        familia = []
        cantidadHijos = eval(input("Cantidad de hijos en la familia: "))
        cantidadDulces = eval(input("Cantidad de dulces recogidos: "))
        cantidadDNiños = cantidadDulcesNiños(cantidadHijos, cantidadDulces) #5
        cantidadDRegalados = cantidadDulcesRegalados(cantidadDulces, cantidadDNiños)
        cantidadDPadres = cantidadDulces - cantidadDNiños - cantidadDRegalados
        porcentajeDulcesNiños = cantidadDNiños / cantidadDulces
        porcentajeDulcesRegalados = cantidadDRegalados / cantidadDulces
        porcentajeDulcesPadres = cantidadDPadres / cantidadDulces
        familia.append(cantidadHijos)
        familia.append(cantidadDulces)
        familia.append(cantidadDNiños)
        familia.append(cantidadDRegalados)
        familia.append(cantidadDPadres)
        familia.append(porcentajeDulcesNiños)
        familia.append(porcentajeDulcesRegalados)
        familia.append(porcentajeDulcesPadres)
        matrizFamilias.append(familia)
    return matrizFamilias

def cantidadDulcesNiños(cantidadHijos, cantidadDulces):
    dulcesNiños = 0
    for i in range(0, cantidadHijos):
        bandera = False
        while bandera == False:
            dulcesNiñoActual = eval(input("Cantidad de dulces que se comió el niño: "))
            dulcesNiños += dulcesNiñoActual
            if dulcesNiños <= cantidadDulces:
                bandera = True
            else:
                dulcesNiños -= dulcesNiñoActual
    return dulcesNiños

def cantidadDulcesRegalados(cantidadDulces, cantidadDulcesNiños):
    dulcesRestantes = cantidadDulces - cantidadDulcesNiños
    dulcesRegalados = 0
    if dulcesRestantes > 0:
        bandera = False
        while bandera == False:
            dulcesRegalados = eval(input("Cantidad de dulces que se regalaron: "))
            if dulcesRegalados <= dulcesRestantes:
                bandera = True
    return dulcesRegalados

def calculosEstudio(familias):
    cantidadFamilias = len(familias)
    cantidadFamiliasNiñosMayor50 = 0
    cantidadFamiliasInvitadosMayor50 = 0
    cantidadFamiliasPadresMayor50 = 0
    cantidadDulcesTotales = 0
    cantidadDulcesNiños = 0
    cantidadDulcesInvitados = 0
    cantidadDulcesAdultos = 0
    diccionarioDatos = {}
    for i in range(0, cantidadFamilias):
        if familias[i][5] > 0.5: # Cantidad de familias con un porcentaje mayor de 50% de consumo de dulces por parte de los niños
            cantidadFamiliasNiñosMayor50 += 1

        if familias[i][6] > 0.5: # Cantidad de familias con un porcentaje mayor de 50% de consumo de dulces por parte de los invitados
            cantidadFamiliasInvitadosMayor50 += 1

        if familias[i][7] > 0.5: # Cantidad de familias con un porcentaje mayor de 50% de consumo de dulces por parte de los padres
            cantidadFamiliasPadresMayor50 += 1
        
        cantidadDulcesTotales += familias[i][1] # Cantidad de dulces totales
        cantidadDulcesNiños += familias[i][2] # Cantidad de dulces totales de niños
        cantidadDulcesInvitados += familias[i][3] # Cantidad de dulces totales de invitados
        cantidadDulcesAdultos += familias[i][4] # Cantidad de dulces totales de padres
    
    promedioNiñosPadres = (cantidadDulcesNiños + cantidadDulcesAdultos) / cantidadFamilias
    porcentajeDulcesNiños = (cantidadDulcesNiños/cantidadDulcesTotales) * 100
    porcentajeDulcesAdultos = (cantidadDulcesAdultos/cantidadDulcesTotales) * 100

    diccionarioDatos = llenarDiccionario(diccionarioDatos, "cantidadFamiliasNiñosMayor50", cantidadFamiliasNiñosMayor50)
    diccionarioDatos = llenarDiccionario(diccionarioDatos, "cantidadFamiliasInvitadosMayor50", cantidadFamiliasInvitadosMayor50)
    diccionarioDatos = llenarDiccionario(diccionarioDatos, "cantidadFamiliasPadresMayor50", cantidadFamiliasPadresMayor50)
    diccionarioDatos = llenarDiccionario(diccionarioDatos, "cantidadDulcesTotales", cantidadDulcesTotales)
    diccionarioDatos = llenarDiccionario(diccionarioDatos, "cantidadDulcesNiños", cantidadDulcesNiños)
    diccionarioDatos = llenarDiccionario(diccionarioDatos, "cantidadDulcesInvitados", cantidadDulcesInvitados)
    diccionarioDatos = llenarDiccionario(diccionarioDatos, "cantidadDulcesPadres", cantidadFamiliasNiñosMayor50)
    diccionarioDatos = llenarDiccionario(diccionarioDatos, "promedioNiñosPadres", promedioNiñosPadres)
    diccionarioDatos = llenarDiccionario(diccionarioDatos, "porcentajeDulcesNiños", porcentajeDulcesNiños)
    diccionarioDatos = llenarDiccionario(diccionarioDatos, "porcentajeDulcesAdultos", porcentajeDulcesAdultos)

def llenarDiccionario(diccionario, llave, valor):
    diccionario[llave] = valor
    return diccionario

main()