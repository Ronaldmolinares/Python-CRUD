"""
Min Window Substring
Have the function MinWindowSubstring(strArr) take the array of strings stored in strArr,
which will contain only two strings, the first parameter being the string N and the second
parameter being a string K of some characters, and your goal is to determine the smallest
substring of N that contains all the characters in K. For example: if strArr is ["aaabaaddae", "aed"]
then the smallest substring of N that contains the characters a, e, and d is "dae" located at the end
of the string. So for this example your program should return the string dae.

Another example: if strArr is ["aabdccdbcacd", "aad"] then the smallest substring of N that contains
all of the characters in K is "aabd" which is located at the beginning of the string. Both parameters
will be strings ranging in length from 1 to 50 characters and all of K's characters will exist somewhere
in the string N. Both strings will only contains lowercase alphabetic characters.

Examples
    Input: ["ahffaksfajeeubsne", "jefaa"]
    Output: aksfaje

    Input: ["aaffhkksemckelloe", "fhea"]
    Output: affhkkse
"""


def MinWindowSubstring(strArr):

    N = strArr[0]
    K = strArr[1]

    map_k = {}
    map_n = {}

    for c in K:
        map_k[c] = 1 + map_k.get(c, 0)

    need = len(map_k)
    have = 0
    ansL = -1
    ansR = -1
    minLen = 50

    left = 0
    for right, c in enumerate(N):
        if c in map_k:
            map_n[c] = 1 + map_n.get(c, 0)
            if map_n[c] == map_k[c]:
                have += 1

        while have == need:
            newLen = right - left + 1
            if newLen < minLen:
                ansL = left
                ansR = right
                minLen = newLen

            if N[left] in map_k:
                map_n[N[left]] -= 1
                if map_n[N[left]] < map_k[N[left]]:
                    have -= 1

            left += 1

    return N[ansL : ansR + 1] if ansL != -1 else ""


# keep this function call here
print(MinWindowSubstring(input()))
