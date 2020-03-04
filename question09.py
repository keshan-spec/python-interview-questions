"""
find longest sub array that add upto a given sum in an array of integers
# Sliding window tchnique
"""


def find_longest_subarr(arr,s):
    lsa = [-1]
    l = es = 0
    for r in range(len(arr)):
        es += arr[r]
        while l < r and es > s:
            es -= arr[l]
            l += 1
        if es == s and (len(lsa) == 1 or r - l > lsa[1] - lsa[0]):
            lsa = [l+1,r+1]
        r+=1
    return lsa

a = [5,5,1,2,3,45,6]
s = 10
res = find_longest_subarr(a,s)
print(res)
