import numpy as np
import operator


def selection_sort(arr):
    length = len(arr)
    for i in range(length):
        min_index = i
        for j in range(i + 1, length):
            min_index = min_index if arr[min_index] < arr[j] else j
        arr[min_index], arr[i] = arr[i], arr[min_index]

    return arr


def correct_method(arr):
    return sorted(arr)


def generate_cases():
    for i in range(10000):
        arr = list(np.random.randint(1, 100, 10))
        res_1 = selection_sort(arr)
        res_2 = correct_method(arr)

        if not operator.eq(res_2, res_1):
            print(arr)
            print(res_1)
            print(res_2)
            print("error")
            break


generate_cases()
