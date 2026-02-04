"""
String Challenge

Have the function
StringChallenge (str) take the str
parameter being passed and return a
compressed version of the string using
the Run-length encoding algorithm. This
algorithm works by taking the
occurrence of each repeating character
and outputting that number along with a
single character of the repeating
sequence. For example: "wwwggopp"
would return 3w2g1o2p. The string will
not contain any numbers, punctuation, or
symbols.

Once your function is working, take
the final output string and intersperse
it character-by-character with your
ChallengeToken.

Your ChallengeToken: hbs2oim9c1a

Examples
Input: "aabbcde"
    Output: 2a2b1c1d1e
    Final Output: 2hab2sb21oci1md91ce1a

Input: "wwwbbbw"
    Output: 3w3b1w
    Final Output: 3hwb3sb21owin9c1a
"""

from itertools import zip_longest

# def StringChallenge1(stri):
#     if not stri.isalpha():
#         raise ValueError(
#             "The string will not contain any numbers, punctuation, or symbols."
#         )

#     token = "hbs2oim9c1a"
#     dic = {}
#     contador = 1

#     for c in stri:
#         if c not in dic:
#             dic[c] = contador
#         else:
#             dic[c] += contador

#     casteo = "".join(map(str, dic.values()))
#     cadena = zip(casteo, dic.keys())
#     valores = "".join(a + b for a, b in cadena)

#     resultado = zip_longest(valores, token, fillvalue="")

#     return "".join(a + b for a, b in resultado)


def StringChallenge(stri):
    token = "hbs2oim9c1a"
    contador = 1
    cadena = ""

    for c in range(1, len(stri)):
        if stri[c - 1] == stri[c]:
            contador += 1
        else:
            cadena += str(contador) + stri[c - 1]
            contador = 1

    cadena += str(contador) + stri[c]

    resultado = zip_longest(cadena, token, fillvalue="")
    return "".join(a + b for a, b in resultado)


r = StringChallenge("aabbcde")
r2 = StringChallenge("wwwbbbw")
print(r + "\n" + r2)
