from random import shuffle

from Algorithms.sortings.insertion_sort import insertion_sort
from Algorithms.sortings.selection_sort import selection_sort
from Algorithms.sortings.buble_sort import bubble_sort


def sort(*, sort_type: str, obj_to_sort: list[int]) -> list[int]:
    """Implement sorting algrithms: bubble, insertion, selection, random"""
    dictio = {"bubble": bubble_sort, "insertion": insertion_sort, "selection": selection_sort, "random": shuffle}
    dictio[sort_type](obj_to_sort)
    return obj_to_sort


if __name__ == '__main__':
    sort(sort_type="random", obj_to_sort=[5, 2, 9, 6, 5, 1, 8, 0, 2, 4, 5])
