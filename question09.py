"""
find longest sub array that add upto a given sum in an array of integers
"""


# Sliding window tchnique
# TIME COMPLEXITY : O(n)
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
    return lsa

# Brute force technique
# TIME COMPLEXITY : O(n^2)
def find_longest_subarr_bf(arr,s):
    lsa = [-1]
    for r in range(len(arr)):
        es = 0 
        for j in range(len(arr)):
            es += arr[j]
            if es == s and (len(lsa) == 1 or j - r > lsa[1] - lsa[0]):
                lsa = [r+1,j+1]
                break
    return lsa

a = [5,5,1,2,3,45,6]
s = 10
print(find_longest_subarr(a,s))
print(find_longest_subarr_bf(a,s)) 
