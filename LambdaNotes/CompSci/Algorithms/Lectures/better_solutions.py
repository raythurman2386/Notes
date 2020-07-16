from time import time
from functools import lru_cache

# Cacheing
"""
Dynamic Programming - instead of repeating the same steps and getting the same results,
"cache" the results instead

Also called memoization

memo-cache - keys are your input to the function
    - values are what the fn returns

import functools
@functools.lru_cache
"""


@lru_cache
def fib(n):
    if n < 2:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


print("\n***** Reg Fib *****")
start = time()
print(fib(20))
print(f"\nResult calculated in {time() - start:.5f} seconds")


def mem_fib(n, cache={}):
    if n == 0:
        cache[0] = 0
        return 0
    elif n == 1:
        cache[1] = 1
        return 1
    elif n in cache:
        return cache[n]
    else:
        cache[n] = mem_fib(n - 1, cache) + mem_fib(n - 2, cache)
        return cache[n]


print("\n***** Cache Fib *****")
start = time()
print(mem_fib(20))
print(f"\nResult calculated in {time() - start:.5f} seconds")


# Tabulation example of fibonacci
def tab_fib(n):
    fib_arr = [0 for _ in range(0, n + 1)]
    fib_arr[0] = 0
    fib_arr[1] = 1

    for i in range(2, n + 1):
        fib_arr[i] = fib_arr[i - 1] + fib_arr[i - 2]

    return fib_arr[n]


print("\n***** Tab Fib *****")
start = time()
print(tab_fib(20))
print(f"\nResult calculated in {time() - start:.5f} seconds")
