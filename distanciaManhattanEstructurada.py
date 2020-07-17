"""
Programa que calcula la distancia manhattan de dos puntos
"""

# Entrada del algoritmo
x1 = float(input("Introduce el valor de X1: "))
y1 = float(input("Introduce el valor de Y1: "))
x2 = float(input("Introduce el valor de X2: "))
y2 = float(input("Introduce el valor de Y2: "))

# Proceso 
distanciaManhattan = (abs(x2 - x1) + abs(y2 - y1))

# Salida
print("La distancia manhattan entre los dos puntos es: ", distanciaManhattan)
