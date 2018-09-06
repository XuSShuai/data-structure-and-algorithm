import numpy as np


def netherlands_flag(arr, num):
    less, more = -1, len(arr)
    cur = 0
    while cur < more:
        if arr[cur] < num:
            arr[less + 1], arr[cur] = arr[cur], arr[less + 1]
            less += 1
            cur += 1
        elif arr[cur] > num:
            arr[more - 1], arr[cur] = arr[cur], arr[more - 1]
            more -= 1
        else:
            cur += 1

    return less + 1, more - 1


def check():
    for i in range(10000):
        arr = list(np.random.randint(1, 100, 10))
        num = arr[np.squeeze(np.random.randint(1, 10, 1))]
        start, end = netherlands_flag(arr, num)

        for k in range(start):
            if arr[k] >= num:
                print("error")
                return
        for k in range(end + 1, len(arr)):
            if arr[k] <= num:
                print("error")
                return


check()



