from DesignPatterns.strategy.sorting_algo_interface import SortingStrategyABC


def sort(*, sort_type: str, obj_to_sort: list[int]) -> list[int]:
    """Implement sorting algrithms: bubble, insertion, selection, random"""

    SortingStrategyABC.subclasses_as_dict().get(sort_type).inplace_sort(obj_to_sort=obj_to_sort)
    return obj_to_sort


if __name__ == '__main__':
    dupa = sort(sort_type="bubble", obj_to_sort=[5, 2, 9, 6, 5, 1, 8, 0, 2, 4, 5])
