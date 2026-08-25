class Cuadrado(Rectangulo):
    """
    Representa un cuadrado. Hereda de Rectangulo,
    ya que un cuadrado es un rectángulo con ancho y alto iguales.

    Atributos:
    lado (float): El lado del cuadrado.
    """

    def __init__(self, lado):
        """
        Inicializa una nueva instancia de Cuadrado.

        Parámetros:
        lado (float): El lado del cuadrado.
        """
        super().__init__(lado, lado)


# creamos una instancia de Cuadrado
cuadrado1 = Cuadrado(5)

print(f"Área: {cuadrado1.calcular_area()}")
print(f"Perímetro: {cuadrado1.calcular_perimetro()}")