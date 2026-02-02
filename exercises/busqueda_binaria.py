import random


def busqueda_binaria(lista, objetivo):
    bajo = 0
    alto = len(lista) - 1

    while bajo <= alto:
        medio = (bajo + alto) // 2
        valor_medio = lista[medio]

        if valor_medio == objetivo:
            return medio
        elif valor_medio < objetivo:
            bajo = medio + 1
        else:
            alto = medio - 1

    return -1


if __name__ == "__main__":
    data = [random.randint(0, 100) for _ in range(20)]
    print("Lista desordenada:", data)
    data.sort()
    print("Lista ordenada:", data)

    objetivo = int(input("Ingrese el número a buscar: "))

    resultado = busqueda_binaria(data, objetivo)
    print(
        f"El elemento {objetivo} se encuentra en el índice: {resultado}"
        if resultado != -1
        else f"El elemento {objetivo} no se encuentra en la lista."
    )
