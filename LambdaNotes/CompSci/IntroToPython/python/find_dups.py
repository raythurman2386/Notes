# Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

# Find all the elements that appear twice in this array.

# Could you do it without extra space and in O(n) runtime?

# Input:
# [4,3,2,7,8,2,3,1]
# Output:
# [2,3]

def find_dups(arr):
    # Runtime is too long
    # dups = list(set([num for num in arr if arr.count(num) > 1]))
    # print(dups)
    seen = {}
    dups = []
    for num in arr:
        if num in seen:
            dups.append(num)
        else:
            seen[num] = 1

    return dups


print(find_dups([4, 3, 2, 7, 8, 2, 3, 1]))
