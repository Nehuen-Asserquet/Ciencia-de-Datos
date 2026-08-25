def es_palindromo(cadena):
    """
    Esta función recibe una cadena y determina si es un palíndromo.

    Parámetros:
    cadena (str): El texto a evaluar.

    Retorna:
    bool: True si la cadena es un palíndromo, False si no lo es.
    """
    return cadena == cadena[::-1]

print(es_palindromo("neuquen"))
print(es_palindromo("hola"))