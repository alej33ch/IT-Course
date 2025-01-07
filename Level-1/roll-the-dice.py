import random

#
# Lista de números para contar las frecuencias
numbers = [random.randint(1, 100) for _ in range(20)]

# Crear un diccionario para contar las frecuencias
frequency = {}
for num in numbers:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

# Imprimir las frecuencias
for num, count in frequency.items():
    print(f"El número {num} se repite {count} veces")