"""
Dado un arreglo de números enteros ordenado de forma ascendente,
determina si existen dos números distintos cuya suma sea igual a un valor objetivo target.

Retorna True si existen, False en caso contrario.
"""

data = [1, 2, 4, 6, 8, 9]


def suma_target(lista, target):
    if len(lista) < 2:
        return False
    i = 0
    j = 1
    while (lista[i] + lista[j]) != target:
        j += 1
        if j >= len(lista) and i < len(lista) - 1:
            i += 1
            j = i + 1
        if j == len(lista):
            return False
    if lista[i] != lista[j]:
        return True
    else:
        return False


def two_pointers(lista, target):
    if len(lista) < 2:
        return False

    i = 0
    j = len(lista) - 1

    while i < j:
        suma = lista[i] + lista[j]

        if suma == target:
            return True
        elif suma < target:
            i += 1
        else:
            j -= 1

    return False


valor = 22
# resultado = suma_target(data, valor)
resultado = two_pointers(data, valor)
print(f"Hay dos numeros distintos que sumados dan {valor}" if resultado else "Falso")
