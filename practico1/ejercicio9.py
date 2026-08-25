class Rectangulo:
    """
    Representa un rectángulo.

    Atributos:
    ancho (float): El ancho del rectángulo.
    alto (float): El alto del rectángulo.

    Métodos:
    calcular_area(): Devuelve el área del rectángulo.
    calcular_perimetro(): Devuelve el perímetro del rectángulo.
    """

    def __init__(self, ancho, alto):
        """
        Inicializa una nueva instancia de Rectangulo.

        Parámetros:
        ancho (float): El ancho del rectángulo.
        alto (float): El alto del rectángulo.
        """
        self.ancho = ancho
        self.alto = alto

    def calcular_area(self):
        """Devuelve el área del rectángulo."""
        return self.ancho * self.alto

    def calcular_perimetro(self):
        """Devuelve el perímetro del rectángulo."""
        return 2 * self.ancho + 2 * self.alto


# creamos una instancia de Rectangulo
rectangulo1 = Rectangulo(4, 6)

print(f"Área: {rectangulo1.calcular_area()}")
print(f"Perímetro: {rectangulo1.calcular_perimetro()}")