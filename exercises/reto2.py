"""
String Challenge

Have the function
StringChallenge (sen) take the sen
parameter being passed and return the
longest word in the string. If there are

two or more words that are the same

length, return the first word from the
string with that length. Ignore
punctuation and assume sen will not be
empty. Words may also contain numbers,
for example "Hello world123 567"

Once your function is working, take
the final output string and intersperse
it character-by-character with your
ChallengeToken.

Your ChallengeToken: hbs2oim9c1a

Examples

Input: "fun&! ! time"
Output: time

Final Output: thibmse2oim9c1a

Input: "I love dogs"
Output: love
inal Output: lhobvse2oim9c1a
"""

from itertools import zip_longest


def StringChallenge(sen):
    token = "hbs2oim9c1la"
    cadena = sen.split(" ")
    mayor = 0
    palabra = ""

    for c in cadena:
        if c.isalnum():  # Comprueba si un caracter es alfanumerico
            if len(c) > mayor:
                mayor = len(c)
                palabra = c

    resultado = zip_longest(palabra, token, fillvalue="")

    return "".join(a + b for a, b in resultado)


r1 = StringChallenge("fun&!! time")
r2 = StringChallenge("I love dogs")
print(r1 + "\n" + r2)
