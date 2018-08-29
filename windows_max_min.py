# 窗口内最大值减去最小值小于等于num的子数组的数量
# 双端队列用来解决在窗口中的最大值问题
from collections import deque
import numpy as np


def comparator(arr, num):
    res = 0
    for start in range(len(arr)):
        for end in range(start, len(arr)):
            if judge(arr, start, end, num):
                res += 1
    return res


def judge(arr, start, end, num):
    max_v, min_v = max(arr[start:end+1]), min(arr[start:end+1])
    return max_v - min_v <= num


def window_max_min(arr, num):
    max_log = deque([])
    min_log = deque([])
    L, R, res = 0, 0, 0
    while L < len(arr):
        while R < len(arr):
            while len(max_log) != 0 and arr[max_log[len(max_log) - 1]] <= arr[R]:
                max_log.pop()
            max_log.append(R)
            while len(min_log) != 0 and arr[min_log[len(min_log) - 1]] >= arr[R]:
                min_log.pop()
            min_log.append(R)
            if arr[max_log[0]] - arr[min_log[0]] > num:
                break
            R += 1
        res += R - L  # why not R - L + 1
        if min_log[0] == L:
            min_log.popleft()
        if max_log[0] == L:
            max_log.popleft()
        L += 1
    return res

if __name__ == "__main__":
    for i in range(1000):
        arr = list(np.random.randint(1, 10000, 100))
        num = int(np.random.randint(1, 100, 1))
        res1 = comparator(arr, num)
        res2 = window_max_min(arr, num)
        if res1 != res2:
            print(res1, res2, "false")
