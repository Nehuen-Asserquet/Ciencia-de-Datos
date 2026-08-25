PI = 3.14159

def calcular_area_circulo(radio):
    """
    Calcula el área de un círculo dado su radio.

    Parámetros:
    radio (float): El radio del círculo.

    Retorna:
    float: El área del círculo.
    """
    area = PI * (radio ** 2)
    return area

radio_texto = input("Ingresá el radio del círculo: ")
radio_numero = float(radio_texto)

area = calcular_area_circulo(radio_numero)

print(f"El área del círculo con radio {radio_numero} es {area}")