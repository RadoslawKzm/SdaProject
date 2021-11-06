from functools import lru_cache

@lru_cache(5000)
def fibonacci(n, lst=None):
    if not isinstance(lst, list):
        lst = [0, 1]
    # if n in [0, 1]:
    #     return n
    try:
        fib1 = lst[n-1]
    except IndexError:
        fib1 = fibonacci(n - 1, lst)
        lst.append(fib1)
    try:
        fib2 = lst[n-2]
    except IndexError:
        fib2 = fibonacci(n - 2, lst)
        lst.append(fib2)
    return fib1 + fib2


print(fibonacci(5000))
# print(fibonacci(70))
