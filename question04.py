"""
In an integer array made up of values starting from 1 and the length of the array.
find the first pair of duplicates, example
    [0,15,2,10] wrong
    [1,2,3,4] right
    [1,2,3,2,4,3] -> 2 would be the first duplicate here

    return the index if the duplicate is found, else return -1
"""

import numpy as np
import time

x = np.array([5,2, 3, 4 , 2, 3 ])

# checks if the array is valid
# return : [True ,False ,....]
def array_valid(array):
    return [(False if 0 in array or i > len(array) else True) for i in array]


# main function that finds the first duplicate
# return : -1 if there is any error or no duplicates, index and data if the duplicate is found
def find_first_duplicate(array):
    now = time.time()
    if all(array_valid(array)):
        hash_map = []
        for index, data in enumerate(array):
            if data in hash_map:
                print(f"Took {time.time() - now}s")
                return f"Value : {data} has a duplicate in the Index : {index}"
            else:
                hash_map.append(data)

    print(f"Took {time.time() - now}s")
    return -1


# print(find_first_duplicate(x))


# without the hash_map
def firstDuplicate(a):
    if all(array_valid(a)):
        for i,_ in enumerate(a):
            if a[abs(a[i])-1] < 0:
                return f"First duplicate value: {abs(a[i])}"
            else:
                # make the value in that index negative
                # example: n becomes -n
                print(a[abs(a[i])-1], end=" ")
                a[abs(a[i]) - 1] = -a[abs(a[i])-1]
                print(a[abs(a[i])-1])
    return -1

print(firstDuplicate(x))
