import numpy as np


def get_max(arr, L, R):
    if L == R:
        return arr[L]
    mid = (L + R) // 2
    left_max = get_max(arr, L, mid)
    right_max = get_max(arr, mid + 1, R)
    return left_max if left_max > right_max else right_max

if __name__ == "__main__":
    arr = list(np.random.randint(1, 100, 10))
    print(arr)
    print(get_max(arr, 0, len(arr)-1))
    arr = list(np.random.randint(1, 100, 11))
    print(arr)
    print(get_max(arr, 0, len(arr)-1))
