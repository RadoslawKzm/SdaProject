import bisect
from typing import List

inpt: List[int] = list(range(64))


def bisect_fider(*, num: int, collection: List[int]) -> bool:
    index = bisect.bisect_left(collection, num)
    if index > len(collection) - 1:
        print(f"{num = } outside of scope")
        return False
    if num < collection[index]:
        print(f"{num = } outside of scope")
        return False
    return True


def is_number_inside(*, num: int, collection: List[int]) -> bool:
    """implement binary search"""
    low_index = 0
    high_index = len(collection) - 1
    if not collection[low_index] <= num <= collection[high_index]:
        print(f"{num = } outside of scope")
        return False
    index = len(collection) // 2
    while True:
        if num == collection[index]:
            return True
        if num < collection[index]:
            high_index = index
            index = len(collection[low_index:high_index]) // 2 + low_index
            continue
        if num > collection[index]:
            low_index = index
            index = len(collection[low_index:high_index]) // 2 + low_index


if __name__ == '__main__':
    # print(is_number_inside(num=5, collection=inpt))
    # print(is_number_inside(num=-1, collection=inpt))
    # print(is_number_inside(num=80, collection=inpt))
    bisect_fider(num=-1, collection=inpt)
    bisect_fider(num=100, collection=inpt)
    bisect_fider(num=5, collection=inpt)
