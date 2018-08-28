# 分组:O(1), 每五个相连的数为一组
# 组内排序 O(1) -> O(N)， 对组内的5个数进行排序
# 每一个组的中位数，构成新的数组(中位数或者上中位数)， 长度为N/5
# 利用bfprt算法找到长度为N/5的数组的中位数num
# 利用num对原数组做partition，小于num的左边， 大于num的右边， 等于的中间，返回
# 等于区域的下标区域start， end， 如果start，end包括第k小的数， 返回；否则，在
# 一边区域中继续bfprt算法
import copy
import numpy as np


def get_top_k_by_bfprt(arr, k):
    arr_copy = copy.deepcopy(arr)
    return bfprt(arr_copy, 0, len(arr_copy) - 1, k - 1)


def bfprt(arr, l, r, k):
    if l == r:
        return arr[l]
    pivot = get_median_of_median(arr, l, r)
    start, end = partition(arr, l, r, pivot)
    if start <= k <= end:
        return arr[k]
    elif start > k:
        return bfprt(arr, l, start - 1, k)
    else:
        return bfprt(arr, end + 1, r, k)


def get_median_of_median(arr, l, r):
    length = (r - l + 1) // 5
    offset = 0 if (r - l + 1) % 5 == 0 else 1
    median = []
    for i in range(length + offset):
        end = min([l + i * 5 + 4, r])
        tmp = get_median_from_5(arr, l + i * 5, end)
        median.append(tmp)
    return bfprt(median, 0, len(median) - 1, (len(median)) // 2)


def get_median_from_5(arr, l, r):
    sort_arr = sorted(arr[l:r + 1])
    return sort_arr[len(sort_arr) // 2]


def partition(arr, l, r, pivot):
    less = l - 1
    more = r + 1
    cur = l
    while cur < more:
        if arr[cur] < pivot:
            arr[cur], arr[less + 1] = arr[less + 1], arr[cur]
            less += 1
            cur += 1
        elif arr[cur] > pivot:
            arr[cur], arr[more - 1] = arr[more - 1], arr[cur]
            more -= 1
        else:
            cur += 1
    return less + 1, more - 1


def quick_sort(arr, l, r):
    if l < r:
        start, end = partition_2(arr, l, r)
        quick_sort(arr, l, start - 1)
        quick_sort(arr, end + 1, r)


def partition_2(arr, l, r):
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

if __name__ == "__main__":
    for i in range(1000):
        arr = list(np.random.randint(1, 10000, 100))
        k = int(np.random.randint(1, 101, 1))
        res1 = get_top_k_by_bfprt(arr, k)
        arr_copy = copy.deepcopy(arr)
        quick_sort(arr_copy, 0, len(arr) - 1)
        if res1 != arr_copy[k - 1]:
            print(arr)
            print("quick sort: ", arr_copy)
            print("false", i, k, res1, arr_copy[k - 1])
            break

    arr = [5, 3, 533, 2, 4, 54, 332, 42, 22]
    print(get_top_k_by_bfprt(arr, 5))
