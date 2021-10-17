import time
from functools import reduce
from typing import List
import numpy as np


def time_measure(func):
    def wrapper(*args, **kwargs):
        tstart = time.time()
        retval = func(*args, **kwargs)
        print(f"{time.time() - tstart:0.4f}s")
        return retval

    return wrapper


@time_measure
def map_example(*, lst: List[int]) -> List[int]:
    return list(map(lambda x: x ** 2, lst))


@time_measure
def map_comp(*, lst: List[int]) -> List[int]:
    return [x ** 2 for x in lst]


@time_measure
def array_example(*, arr):
    return np.square(arr)


@time_measure
def filter_example(*, lst: List[int]) -> List[int]:
    return list(filter(lambda x: x % 2, lst))


@time_measure
def filter_comp(*, lst: List[int]) -> List[int]:
    return [x for x in lst if x % 2 != 0]


@time_measure
def reduce_example(*, lst: List[int]) -> int:
    return reduce(lambda x, y: x + y, lst)


@time_measure
def reduce_comp(*, lst: List[int]) -> int:
    return sum(lst)


if __name__ == '__main__':
    HOW_MUCH = 10_000_000
    items = list(range(HOW_MUCH))
    # arr = np.arange(HOW_MUCH)
    lst = [[1, 2, 3], [1, 5, 7], [1, 2, 3]]
    # comprehension_example(lst=items)
    # map_example(lst=items)
    # array_example(arr=arr)
    # filter_example(lst=items)
    # filter_comp(lst=items)
    # reduce_example(lst=items)
    # reduce_comp(lst=items)
