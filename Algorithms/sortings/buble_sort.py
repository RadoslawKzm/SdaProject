from typing import List


def bubble_sort(arr: List[int]) -> None:
    """Implement bubble sort"""
    end = len(arr) - 1
    while end > 0:
        for index in range(end):
            if arr[index] > arr[index + 1]:
                arr[index], arr[index + 1] = arr[index + 1], arr[index]
        end -= 1


if __name__ == '__main__':
    arr = [8, 5, 2, 9, 5, 6, 3]
    bubble_sort(arr)
    print(arr)
