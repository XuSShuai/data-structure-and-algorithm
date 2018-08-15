import numpy as np
import operator
import copy


def quick_sort(arr, l, r):
    if l < r:
        start, end = partition(arr, l, r)
        quick_sort(arr, l, start - 1)
        quick_sort(arr, end + 1, r)


def partition(arr, l, r):
    less = l - 1
    more = r
    cur = l
    while cur < more:
        if arr[cur] < arr[r]:
            arr[less + 1], arr[cur] = arr[cur], arr[less + 1]
            less += 1
            cur += 1
        elif arr[cur] > arr[r]:
            arr[cur], arr[more - 1] = arr[more - 1], arr[cur]
            more -= 1
        else:
            cur += 1
    arr[r], arr[more] = arr[more], arr[r]
    return less + 1, more


def correct_method(arr):
    return sorted(arr)


def generate_cases():
    for i in range(10000):
        arr = list(np.random.randint(1, 100, 10))
        res_1 = copy.deepcopy(arr)
        quick_sort(res_1, 0, len(res_1) - 1)
        res_2 = correct_method(arr)

        if not operator.eq(res_2, res_1):
            print(arr)
            print(res_1)
            print(res_2)
            print("error")
            break


generate_cases()