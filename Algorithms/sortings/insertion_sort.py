from typing import List


def insertion_sort(arr: List[int]) -> None:
    """Implement insertion sort"""
    start = 1
    for index in range(1, len(arr)):
        for sub_index in reversed(range(0, start)):
            if arr[sub_index] > arr[index]:
                arr[index], arr[sub_index] = arr[sub_index], arr[index]
                index -=1
                continue
            break
        start += 1


if __name__ == '__main__':
    arr = [8, 5, 2, 9, 5, 6, 3]
    insertion_sort(arr)
    print(arr)
