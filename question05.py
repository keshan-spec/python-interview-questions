"""
Given a string s consisting of small English letters,
find and return the first instance of a non-repeating character in it. 
If there is no such character, return '_'.

For s = "abacabad", the output should be
firstNotRepeatingCharacter(s) = 'c'.

There are 2 non-repeating characters in the string: 'c' and 'd'. Return c since it appears in the string first.
"""

s = "abacabad"
s2 = "ngrhhqbhnsipkcoqjyviikvxbxyphsnjpdxkhtadltsuxbfbrkof"


def firstNotRepeatingCharacter(string):
    for c in string:
        if string.index(c) == string.rindex(c):
            return c
    return '_'


print(f"First non repeating char : {firstNotRepeatingCharacter(s)}")
print(f"First non repeating char : {firstNotRepeatingCharacter(s2)}")
