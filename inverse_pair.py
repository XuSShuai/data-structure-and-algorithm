# 逆序对问题:
# 在一个数组中， 左边的数如果比右边的数大， 则两个数构成一个逆序对， 请打印所有逆序对。
#
# 1,3,4,2,5,1
#
# 3, 2
# 4, 2
# 3, 1
# 4, 1
# 2, 1
# 5, 1
from sys import stdin
import numpy as np


def merge_sort(arr, L, R):
    if L == R:
        return 0
    mid = (L + R) // 2
    return merge_sort(arr, L, mid) + merge_sort(arr, mid + 1, R) + merge(arr, L, mid, R)


def merge(arr, L, mid, R):
    p = L
    q = mid + 1
    res = 0
    auxiliary = []
    while p <= mid and q <= R:
        if arr[p] > arr[q]:
            res += (mid - p + 1)
            auxiliary.append(arr[q])
            q += 1
        else:
            auxiliary.append(arr[p])
            p += 1

    if p > mid:
        auxiliary.extend(arr[q:R+1])
    if q > R:
        auxiliary.extend(arr[p:mid+1])

    for i in range(len(auxiliary)):
        arr[L + i] = auxiliary[i]

    return res


def correct_method(arr):
    res = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[i]:
                res += 1
    return res


def generate_cases():
    for i in range(10000):
        arr = list(np.random.randint(1, 100, 10))
        res_1 = correct_method(arr)
        res_2 = merge_sort(arr, 0, len(arr) - 1)

        if res_2 != res_1:
            print("error")


# print("input array: ")
# arr = list(map(int, stdin.readline().strip().split(",")))
# print(merge_sort(arr, 0, len(arr) - 1))

generate_cases()