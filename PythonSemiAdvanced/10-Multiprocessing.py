from multiprocessing import Pool
from functools import reduce
from typing import List


def map_example(*, lst: List[int], return_dict: dict) -> int:
    print(f"Starting map_example")
    retval = len(list(map(lambda x: x ** 2, lst)))
    return_dict["filter_comp"] = retval
    print(f"done calculating map_example {retval}")
    return retval


def map_comp(*, lst: List[int], return_dict: dict) -> int:
    print(f"Starting map_comp")
    retval = len([x ** 2 for x in lst])
    return_dict["filter_comp"] = retval
    print(f"done calculating map_comp {retval}")
    return retval


def filter_example(*, lst: List[int], return_dict: dict) -> int:
    print(f"Starting filter_example")
    retval = len(list(filter(lambda x: x % 2, lst)))
    return_dict["filter_comp"] = retval
    print(f"done calculating filter_example {retval}")
    return retval


def filter_comp(*, lst: List[int], return_dict: dict) -> int:
    print(f"Starting filter_comp")
    retval = len([x for x in lst if x % 2 != 0])
    return_dict["filter_comp"] = retval
    print(f"done calculating filter_comp {retval}")
    return retval


def reduce_example(*, lst: List[int], return_dict: dict) -> int:
    print(f"Starting reduce_example")
    retval = reduce(lambda x, y: x + y, lst)
    return_dict["reduce_example"] = retval
    print(f"done calculating reduce_example {retval}")
    return retval


def reduce_comp(*, lst: List[int], return_dict: dict) -> int:
    print(f"Starting reduce_comp")
    retval = sum(lst)
    return_dict["reduce_comp"] = retval
    print(f"done calculating reduce_comp {retval}")
    return retval


if __name__ == '__main__':
    HOW_MUCH: int = 1_000_000
    items: list = list(range(HOW_MUCH))
    # jobs: list = []
    # return_dict: dict = {}
    # for func in [map_example, map_comp, filter_example, filter_comp, reduce_example, reduce_comp]:
    #     p = multiprocessing.Process(target=func, kwargs={"lst": items, "return_dict": return_dict})
    #     jobs.append(p)
    # queue = multiprocessing.Queue()
    # for p in jobs:
    #     p.start()

    # result = [queue.get() for p in jobs]
    # print(result)
    #
    # for p in jobs:
    #     p.join()
    # print(result)

    # with Pool() as pool:
    #     # results_list = pool.starmap(, [(width, height, figures, position) for position in play_fields])
    #     results_list = pool.starmap(map_example, {"lst": items})

    # print("pass")


