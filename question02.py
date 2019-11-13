"""
find the highest number in  any given unordered list
ex; [2,9,8,6,11,1] => 11
"""


def maximum(data):
    minimum = []
    maximum = data[0]
    for i in data:
        if i < maximum:
            minimum.append(i)
        elif i > maximum:
            minimum.append(maximum)
            maximum = i
    return maximum


ex1 = [1000, 2, 9, 8, 6, 11, 1, 100]
print(maximum(ex1))
