# Sock Merchant     https://www.hackerrank.com/challenges/sock-merchant/problem

"""
John works at a clothing store. He has a large pile of socks that he must pair by color for sale. Given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are.

For example, there are n = 7 socks with colors ar = [1, 2, 1, 2, 1, 3, 2]. There is one pair of collor 1 and one of color 2. There are three odd socks left, one of each color. The number of pairs is 2.
"""

"""
Function Description

Must return an integer representing the number of matching pairs of socks that are available

Following params:
- n: number of socks in the pile
- ar: the colors of each sock
"""

def sock_merchant(n, ar):
    socks = {}
    pairs = 0

    for i in ar:
        if i not in socks:
            socks[i] = 1
        else:
            socks[i] += 1

    for k, v in socks.items():
        pairs += v // 2

    return pairs

print(sock_merchant(7, [1, 2, 1, 2, 1, 3, 2]))


from collections import Counter
def sockMerchant(n, ar):
    # total = 0
    # for values in Counter(ar).values():
    #     total += values//2
    # return total
    return sum([Counter(ar)[k] // 2 for k in Counter(ar)])


print(sockMerchant(7, [1, 2, 1, 2, 1, 3, 2]))
