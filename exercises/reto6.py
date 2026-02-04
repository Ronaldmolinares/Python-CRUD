""" """


def StringChallenge(stri):
    """Palindromo sin importar caracteres No alfanumericos

    Args:
        stri (_type_): _description_

    Returns:
        _type_: _description_
    """

    stri_filter = filter(str.isalpha, stri)
    stri_modifi = "".join(stri_filter)

    i = 0
    j = len(stri_modifi) - 1

    while i < j:
        if stri_modifi[i].lower() == stri_modifi[j].lower():
            i += 1
            j -= 1
        else:
            return False

    return True


r = StringChallenge("Noel - sees Leon")
r2 = StringChallenge("A war at Tarawa!")
r3 = StringChallenge("Anne, I vote more cars race Rome-to-Vienna")
print(r)
print(r2)
print(r3)
