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


lista = [1, 3, 5, 7, 9, 11]
objetivo = 12

resultado = busqueda_binaria(lista, objetivo)
print(
    f"El elemento {objetivo} se encuentra en el índice: {resultado}"
    if resultado != -1
    else f"El elemento {objetivo} no se encuentra en la lista."
)
