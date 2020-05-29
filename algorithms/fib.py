def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n - 2)


def fib_opt(n, cache={}):
    if n < 2:
        return n
    elif n in cache:
        return cache[n]
    else:
        cache[n] = fib_opt(n - 1, cache) + fib_opt(n - 2, cache)
        return cache[n]


print(fib_opt(996))
