def es_nro_par_o_impar(numero):
    """
    Esta función recibe un número y determina si es par o impar.
    
    Parámetros:
    numero (int): El número a evaluar.
    
    Retorna:
    str: "par" si el número es par, "impar" si el número es impar.
    """
    if numero % 2 == 0:
        return "par"
    else:
        return "impar"

print(es_nro_par_o_impar(4))  # Ejemplo de uso de la función
print(es_nro_par_o_impar(7))  # Ejemplo de uso de la función