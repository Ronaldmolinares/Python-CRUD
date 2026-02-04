"""
String Challenge

Have the function

StringChallenge (str) take the str
parameter being passed and modify it
using the following algorithm. Replace
every letter in the string with the letter
following it in the alphabet (ie. c
becomes d, z becomes a). Then
capitalize every vowel in this new string
(a, e, i, o, u) and finally return this
modified string.

Once your function is working, take
the final output string and intersperse

    it character-by-character with your
    ChallengeToken.

    Your ChallengeToken: hbs2oim9c1a

Examples

    Input: "hello*3"
    Output: Ifmmp*3
    Final Output: Ihfbmsm2po*i3m9c1a

    Input: "fun times!"
    Output: gvO Ujnft!
    Final Output: ghvbOs 2Uojinmf9tc!1a
"""

from itertools import zip_longest


def StringChallenge(str):
    dic = {
        "a": "b",
        "b": "c",
        "c": "d",
        "d": "e",
        "e": "f",
        "f": "g",
        "g": "h",
        "h": "i",
        "i": "j",
        "j": "k",
        "k": "l",
        "l": "m",
        "m": "n",
        "n": "o",
        # "ñ": "o",
        "o": "p",
        "p": "q",
        "q": "r",
        "r": "s",
        "s": "t",
        "t": "u",
        "u": "v",
        "v": "w",
        "w": "x",
        "x": "y",
        "y": "z",
        "z": "a",
    }
    cadena = ""
    token = "hbs2oim9c1a"
    vocales = "aeiou"

    for c in str:
        if c in dic.keys():
            if dic[c] in vocales:
                cadena += dic[c].upper()
            else:
                cadena += dic[c]
        else:
            cadena += c

    resultado = zip_longest(cadena, token, fillvalue="")

    return "".join(a + b for a, b in resultado)


r1 = StringChallenge("hello*3")
r2 = StringChallenge("fun times!")
print(r1 + "\n" + r2)
