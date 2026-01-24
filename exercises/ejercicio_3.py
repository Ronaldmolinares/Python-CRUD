"""
Ejercicio 4: Sliding Window (Strings)

Dada una cadena s, encuentra la longitud de la subcadena más larga sin caracteres repetidos.

Ejemplo 1
    s = "abcabcbb"
    resultado → 3   ("abc")

Ejemplo 2
    s = "bbbbb"
    resultado → 1   ("b")

Ejemplo 3
    s = "pwwkew"
    resultado → 3   ("wke")
"""

s = "abcabcbb"


def sliding(cadena):
    if len(cadena) == 0:
        return 0

    max_long = 0
    izq = 0
    set_cadena = set()

    for der in range(len(cadena)):
        while cadena[der] in set_cadena:
            set_cadena.discard(cadena[izq])
            izq += 1

        set_cadena.add(cadena[der])
        print(set_cadena)
        max_long = max(max_long, der - izq + 1)

    return max_long


result = sliding(s)
print(result)
