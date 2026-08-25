notas = {"Ana": 8.5, "Juan": 6.0, "María": 9.5}
suma = 0
for nota in notas:
    suma = notas[nota] + suma
promedio = suma / len(notas)
print("El promedio de las notas es:", promedio)