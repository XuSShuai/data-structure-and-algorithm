import numpy as np
import operator


def bubble_sort(arr):
    length = len(arr)
    for end in range(length - 1, 0, -1):
        for i in range(end):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return arr


def correct_method(arr):
    return sorted(arr)


def generate_cases():
    for i in range(10000):
        arr = list(np.random.randint(1, 100, 10))
        res_1 = bubble_sort(arr)
        res_2 = correct_method(arr)

        if not operator.eq(res_2, res_1):
            print("fuck")
            break


generate_cases()

