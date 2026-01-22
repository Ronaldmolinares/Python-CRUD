"""
Dada una cadena s, determina si es un palíndromo.
Un palíndromo se lee igual de izquierda a derecha que de derecha a izquierda.

Restricciones:
- Ignora mayúsculas y minúsculas
- Ignora espacios
- No uses estructuras auxiliares (listas nuevas, reverse, etc.)
"""


def two_Pointers_Strings(cadena):
    if len(cadena.strip()) <= 1:
        return True

    lista = []
    for c in cadena:
        if c != " ":
            lista.append(c)

    i = 0
    j = len(lista) - 1

    while lista[i].lower() == lista[j].lower():
        i += 1
        j -= 1

        if i >= j:
            return True

    return False


def palindroma(cadena):
    if len(cadena.strip()) <= 1:
        return True

    i = 0
    j = len(cadena) - 1

    while i < j:
        if cadena[i] == " ":
            i += 1
            continue
        if cadena[j] == " ":
            j -= 1
            continue
        if cadena[i].lower() != cadena[j].lower():
            return False
        i += 1
        j -= 1
    return True


text = "   ANITA LAVA LA tina"
# r = two_Pointers_Strings(text)
r = palindroma(text)
print(f"La cadena: '{text.strip()}' es palindroma" if r else "Falso")
