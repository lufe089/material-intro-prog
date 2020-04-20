# NÚMEROS LEJANOS N
# Dos números son llamados "números lejanos n", si cumplen las siguientes condiciones:
# 	1. Ambos números son primos.
# 	2. La diferencia(en valor absoluto) entre ellos es n. (Para sacar el valor absoluto se debe revisar si el número es negativo
#      y si si es negativo, se le debe cambiar el signo a positivo multiplicándolo por -1)

# Algunos ejemplos:
# 	- 7 y 13 son "números lejanos 6", ya que ambos son primos y ademas la diferencia entre ellos es exactamente 6.
# 	- 7 y 10 no son números lejanos ya que 10 no es primo(no importa la diferencia entre ellos).
# 	- 5 y 7 no son "números lejanos 6", ya que la diferencia entre ellos es 2. Así pues, estos dos números si pueden ser llamados "números lejanos 2", ya que de esta forma se cumplen las dos condiciones descritas anteriormente.

# El problema es el siguiente:

# Realice una programa que calcule todos los "números lejanos n" que se encuentran en un rango dado. 
# El valor de n(la lejanía), el rango inferior y el rango superior son parámetros de la función que realice.
# Debe realizarlo en mínimo 2 funciones/procedimientos aparte del main

# Por ejemplo, si mi rango inferior es 1, mi rango superior es 100, y mi valor de lejanía es 2, 
# se me está indicando que debo encontrar todas las parejas de "números lejanos 2" entre 1 y 100. En este caso mi programa debería imprimir:

# (3, 5)
# (5, 7)
# (11, 13)
# (17, 19)
# (29, 31)
# (41, 43)
# (59, 61)
# (71, 73)
