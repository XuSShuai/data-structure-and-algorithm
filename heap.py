import heapq
import numpy as np


def heap_sort(arr):
    h = []
    for item in arr:
        heapq.heappush(h, item)

    return [heapq.heappop(h) for i in range(len(h))]


class Project:
    def __init__(self, cost: int, profits: int):
        self.cost = cost
        self.profits = profits

    def __str__(self):
        return str(self.cost) + "\t" + str(self.profits)

    def __lt__(self, other):
        return self.profits - other.profits


class MaxHeap(object):
    def __init__(self, x):
        self.heap = [-e for e in x]
        heapq.heapify(self.heap)

    def push(self, value):
        heapq.heappush(self.heap, -value)

    def pop(self):
        return -heapq.heappop(self.heap)

if __name__ == "__main__":
    arr = np.arange(10)
    np.random.shuffle(arr)
    arr = list(arr)
    print(arr)
    heapq.heapify(arr)
    print(arr)
    print("-"*50)

    arr = [5, 3, 5, 6, 9, 2, 8, 4, 7, 2]
    print(heap_sort(arr))
    print("-"*50)

    heap_project = []
    cost = [10, 2, 11, 9, 14, 5, 3]
    profits = [3, 10, 4, 2, 5, 10, 4]
    for i, project in enumerate(zip(cost, profits)):
        heap_project.append(Project(project[0], project[1]))
    for i in range(len(cost)):
        print(heap_project[i])
    print()

    res = heap_sort(heap_project)
    for i in range(len(cost)):
        print(res[i])
    # why not work?



# 堆的基本操作
# heap = []             :创建了一个空堆
# heappush(heap,item)   :往堆中插入一条新的值
# item = heappop(heap)  :从堆中弹出最小值
# item = heap[0]        :查看堆中最小值，不弹出
# heapify(x)            :以线性时间讲一个列表转化为堆
# nlargest(n,iterbale,key=None)
# 从堆中找出做大的N个数，key的作用和sorted()方法里面的key类似，用列表元素的某个属性和函数作为关键字。
# nsmallest(n, iterable, key=None)
# 找到堆中最小的N个数用法同上


