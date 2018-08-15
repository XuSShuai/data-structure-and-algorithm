#
# 在一个数组中，每一个数左边比当前数小的数累加起来，叫做这个数组的小和，求一个数组的小和
#
# 例子：
# [1,3,4,2,5]
# 1左边比1小的数， 没有
# 3左边比3小的数， 1
# 4左边比4小的数， 1、 3
# 2左边比2小的数， 1
# 5左边比5小的数， 1、 3、 4、 2
# 所以小和为1+1+3+1+1+3+4+2=16

from sys import stdin


def merge_sort(arr, L, R):
    if L == R:
        return 0
    mid = (L + R) // 2
    return merge_sort(arr, L, mid) + merge_sort(arr, mid + 1, R) + merge(arr, L, mid, R)


def merge(arr, L, mid, R):
    p = L
    q = mid + 1
    auxiliary = []
    res = 0
    while p <= mid and q <= R:
        if arr[p] < arr[q]:
            res += arr[p] * (R - q + 1)
            auxiliary.append(arr[p])
            p += 1
        else:
            auxiliary.append(arr[q])
            q += 1

    if p > mid:
        auxiliary.extend(arr[q:R+1])
    if q > R:
        auxiliary.extend(arr[p:mid+1])

    for i in range(len(auxiliary)):
        arr[L + i] = auxiliary[i]

    return res


print("input array: ")
arr = list(map(int, stdin.readline().strip().split(",")))
print(merge_sort(arr, 0, len(arr) - 1))
