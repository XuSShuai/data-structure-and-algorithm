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


print("input array: ")  # 1,4,2,3,5
arr = list(map(int, stdin.readline().strip().split(",")))
print(merge_sort(arr, 0, len(arr) - 1))
