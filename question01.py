"""
given an unordered list of numbers and a sum
if a  pair that adds upto the sum exists return true else false

ex; [1,2,3,9] => 8 // False
ex; [1,2,4,4] => 8 // True

"""


def hasSum(dataSet, sum):
    # a list for adding the compliments of the sum and the data
    comps = []
    # loop through the data
    for data in dataSet:
        # if the data is found in the compliments return True
        if data in comps:
            return True
        # else, add the compliment of the current value and the sum
        comps.append(sum-data)
        # print(f'Adding compliments : {comps}')  # comment if not needed
    return False


ex1 = [1, 2, 3, 9]
ex2 = [1, 2, 4, 4]
sumVal = 8
print(hasSum(ex1, sumVal))
print(hasSum(ex2, sumVal))
