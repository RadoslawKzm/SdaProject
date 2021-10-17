import multiprocessing
from functools import reduce
from typing import List

HOW_MUCH = 10_000_000
items = list(range(HOW_MUCH))


def map_example(*, lst: List[int]) -> int:
    print(f"Starting map_example")
    return len(list(map(lambda x: x ** 2, lst)))


def map_comp(*, lst: List[int]) -> int:
    print(f"Starting map_comp")
    return len([x ** 2 for x in lst])


def filter_example(*, lst: List[int]) -> int:
    print(f"Starting filter_example")
    return len(list(filter(lambda x: x % 2, lst)))


def filter_comp(*, lst: List[int]) -> int:
    print(f"Starting filter_comp")
    return len([x for x in lst if x % 2 != 0])


def reduce_example(*, lst: List[int]) -> int:
    print(f"Starting reduce_example")
    return reduce(lambda x, y: x + y, lst)


def reduce_comp(*, lst: List[int]) -> int:
    print(f"Starting reduce_comp")
    return sum(lst)


def worker(num):
    """thread worker function"""
    print
    'Worker:', num
    return


if __name__ == '__main__':
    jobs = []
    for i in range(5):
        p = multiprocessing.Process(target=worker, args=(i,))
        jobs.append(p)
        p.start()
