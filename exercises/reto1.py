"""
Recursion Challenge

Have the function RecursionChallenge (num) take the num parameter being passed and return the factorial of it. For example: if num = 4, then
your program should return (4 * 3 * 2 * 1) = 24. For the test cases, the range will be between 1 and 18 and the input will always be an integer.

Once your function is working, take the final output string and intersperse it character-by-character with your
ChallengeToken.

Your ChallengeToken: hbs2oim9c1la


Examples

Input: 4

Output: 24
Final Output: 2h4bs2oim9c1a

Input: 8

Output: 40320
Final Output: 4h0b3s220oim9c1a

"""

from itertools import zip_longest


def factorial(numero):
    if numero <= 1:
        return 1

    resultado = numero * (factorial(numero - 1))

    return resultado


def RecursionChallenge2(num):
    numero = str(factorial(num))
    token = "hbs2oim9c1la"
    salida = ""

    i = 0
    j = 0

    while i < len(numero) and j < len(token):
        salida += numero[i] + token[j]

        i += 1
        j += 1

    if i == len(numero):
        salida += token[j:]

    if j == len(token):
        salida += numero[i:]

    return salida


r1 = RecursionChallenge2(8)
print(r1)


# Version final
def RecursionChallenge(num):
    token = "hbs2oim9c1la"

    resultado = 1
    while num > 1:
        resultado *= num
        num -= 1

    valor = str(resultado)
    cadena = zip_longest(valor, token, fillvalue="")

    return "".join(a + b for a, b in cadena)


if __name__ == "__main__":

    r2 = RecursionChallenge(8)
    print(r2)
