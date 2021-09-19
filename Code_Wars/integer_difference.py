def int_diff(lst, n):
    output = []
    for i in range(len(lst)):
        item = lst[i]
        lst2 = lst[i + 1:]
        if (n + item) in lst2:
            output.append((item, n + item))
    return len(output)


if __name__ == '__main__':
    # print(int_diff([1, 1, 5, 6, 9, 16, 27], 4))
    print(int_diff([1, 1, 3, 3], 2), 4)