"""
String Challenge

Have the function
StringChallenge (num) take the num

parameter being passed and return the
number of hours and minutes the

parameter converts to (ie. if num = 63
then the output should be 1:3). Separate
the number of hours and minutes with a
colon.

Once your function is working, take
the final output string and intersperse
it character-by-character with your
ChallengeToken.

Your ChallengeToken: hbs2oim9c1a

Examples

Input: 126
    Output: 2:6
    Final Output: 2h:b6s2oim9c1a

Input: 45
    Output: 0:45
    Final Output: 0h:b4s52oim9c1a
"""

from itertools import zip_longest


def StringChallenge(num):
    # horas = str(num // 60)
    # minutos = str(num % 60)

    # resultado = horas + ":" + minutos

    resultado = f"{num // 60}:{num % 60}"

    token = "hbs2oim9c1a"

    cadena = zip_longest(resultado, token, fillvalue="")

    return "".join(a + b for a, b in cadena)


r = StringChallenge(126)
print(r)
