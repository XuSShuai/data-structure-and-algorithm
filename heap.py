from heapq import *


def heap_sort(arr):
    h = []
    for item in arr:
        heappush(h, item)

    return [heappop(h) for i in range(len(h))]

if __name__ == "__main__":
    arr = [5, 3, 5, 6, 9, 2, 8, 4, 7, 2]
    print(heap_sort(arr))


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


