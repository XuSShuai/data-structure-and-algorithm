import numpy as np
import operator
import copy


def merge_sort(arr, L, R):
    if R == L:
        return

    mid = (R + L) // 2
    merge_sort(arr, L, mid)
    merge_sort(arr, mid + 1, R)
    merge(arr, L, mid, R)


def merge(arr, L, mid, R):
    auxiliary = list()
    p = L
    q = mid + 1
    while p <= mid and q <= R:
        if arr[p] < arr[q]:
            auxiliary.append(arr[p])
            p += 1
        else:
            auxiliary.append(arr[q])
            q += 1
    if p > mid:
        auxiliary.extend(arr[q:R + 1])
    if q > R:
        auxiliary.extend(arr[p:mid + 1])

    for i in range(len(auxiliary)):
        arr[L + i] = auxiliary[i]


def correct_method(arr):
    return sorted(arr)


def generate_cases():
    for i in range(10000):
        arr = list(np.random.randint(1, 100, 10))
        res_1 = copy.deepcopy(arr)
        merge_sort(res_1, 0, len(arr) - 1)
        res_2 = correct_method(arr)

        if not operator.eq(res_2, res_1):
            print(arr)
            print(res_1)
            print(res_2)
            print("fuck")
            break


generate_cases()
