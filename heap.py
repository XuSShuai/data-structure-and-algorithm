from heapq import *


def heap_sort(arr):
    h = []
    for item in arr:
        heappush(h, item)

    return [heappop(h) for i in range(len(h))]