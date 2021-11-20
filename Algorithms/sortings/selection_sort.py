from typing import List


def selection_sort(arr: List[int]) -> None:
    """Implement selection sort"""
    for index in range(len(arr)):
        smallest_index = index
        for sub_index in range(index + 1, len(arr)):
            if arr[sub_index] < arr[smallest_index]:
                smallest_index = sub_index
        arr[index], arr[smallest_index] = arr[smallest_index], arr[index]


if __name__ == '__main__':
    arr = [8, 5, 2, 9, 5, 6, 3]
    selection_sort(arr)
    print(arr)

    arr = [8, 5, 2, 9, 5, 6, 3]
    selection_sort(arr)
    print(arr)

    arr = [8, 5, 2, 9, 5, 6, 3]
    selection_sort(arr)
    print(arr)
