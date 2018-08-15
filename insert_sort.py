import numpy as np
import operator


def insertion_sort(arr):
    length = len(arr)
    for i in range(1, length):
        for j in range(i - 1, -1, -1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            else:
                break
    return arr


def correct_method(arr):
    return sorted(arr)


def generate_cases():
    for i in range(10000):
        arr = list(np.random.randint(1, 100, 10))
        res_1 = insertion_sort(arr)
        res_2 = correct_method(arr)

        if not operator.eq(res_2, res_1):
            print(arr)
            print(res_1)
            print(res_2)
            print("error")
            break


generate_cases()