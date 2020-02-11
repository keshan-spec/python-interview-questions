'''
A cryptarithm is a mathematical puzzle for which the goal is to find the correspondence between letters and digits
,such that the given arithmetic equation consisting of letters holds true when the letters are converted to digits.

If crypt, when it is decoded by replacing all of the letters in the cryptarithm with digits using the mapping in solution,
becomes a valid arithmetic equation containing no numbers with leading zeroes, the answer is true.
If it does not become a valid arithmetic solution, the answer is false.

Note that number 0 doesn't contain leading zeroes (while for example 00 or 0123 do).

Example

For crypt = ["SEND", "MORE", "MONEY"] and

solution = [['O', '0'],
            ['M', '1'],
            ['Y', '2'],
            ['E', '5'],
            ['N', '6'],
            ['D', '7'],
            ['R', '8'],
            ['S', '9']]
the output should be
isCryptSolution(crypt, solution) = true.

When you decrypt "SEND", "MORE", and "MONEY" using the mapping given in crypt,
you get 9567 + 1085 = 10652 which is correct and a valid arithmetic equation.

For crypt = ["TEN", "TWO", "ONE"] and

solution = [['O', '1'],
            ['T', '0'],
            ['W', '9'],
            ['E', '5'],
            ['N', '4']]
the output should be
isCryptSolution(crypt, solution) = false.

Even though 054 + 091 = 145, 054 and 091 both contain leading zeroes, meaning that this is not a valid solution.
'''

c = ["SEND", "MORE", "MONEY"]
sol = [['O', '0'], ['M', '1'], ['Y', '2'], ['E', '5'], ['N', '6'], ['D', '7'], ['R', '8'], ['S', '9']]


def isCryptSolution(crypt, solution):
    num = []
    for x, word in enumerate(crypt):
        num.append([])
        [num[x].append(i[1]) if c in i else 0 for c in word for i in solution]
        if num[x][0] == '0' and len(num[x]) > 1:
            return False
        num[x] = "".join(num[x])
    return not any(x != "0" and x.startswith("0") for x in num) and int(num[0]) + int(num[1]) == int(num[2])


def isCrypt(crypt, solution):
    dic = {ord(c): d for c, d in solution}
    *v, = map(lambda x: x.translate(dic), crypt)
    return not any(x != "0" and x.startswith("0") for x in v) and int(v[0]) + int(v[1]) == int(v[2])


print(isCryptSolution(c, sol))
