# 输入：
#   参数1,正数数组costs
#   参数2,正数数组profits
#   参数3,正数k
#   参数4,正数m
# costs[i]表示i号项目的花费
# profits[i]表示i号项目的利润
# k表示你不能并行,只能串行的最多做k个项目
# m表示你初始的资金
# 说明: 你每做完一个项目,马上获得的收益,可以支持你去做下一个项目。
# 输出: 你最后获得的最大钱数。


class MaxHeap:
    def __init__(self):
        self.object_heap = []
        self.index = -1

    def push(self, obj):
        self.object_heap.append(obj)
        self.index += 1
        cur = self.index
        root_index = int((cur - 1) / 2)
        while self.object_heap[root_index].get_profits() < \
                self.object_heap[cur].get_profits():
            self.object_heap[root_index], self.object_heap[cur] = \
                self.object_heap[cur], self.object_heap[root_index]
            cur = root_index
            root_index = int((cur - 1)/2)

    def heapify(self):
        cur = 0
        left = 2 * cur + 1
        while left < self.index:
            largest = left + 1 if left + 1 < self.index and \
                                  self.object_heap[left + 1].get_profits() > \
                              self.object_heap[left].get_profits() else left
            largest = cur if self.object_heap[cur].get_profits() > \
                             self.object_heap[largest].get_profits() else largest
            if largest == cur:
                break
            self.object_heap[largest], self.object_heap[cur] = \
                self.object_heap[cur], self.object_heap[largest]
            cur = largest
            left = 2 * cur + 1

    def pop(self):
        if self.index == -1:
            return None
        if self.index == 0:
            re = self.object_heap.pop()
        else:
            re = self.object_heap[0]
            self.object_heap[0] = self.object_heap.pop()
            self.heapify()
        self.index -= 1
        return re


class MinHeap:
    def __init__(self):
        self.object_heap = []
        self.index = -1

    def push(self, obj):
        self.object_heap.append(obj)
        self.index += 1
        cur = self.index
        root_index = int((cur - 1) / 2)
        while self.object_heap[root_index].get_cost() > \
                self.object_heap[cur].get_cost():
            self.object_heap[root_index], self.object_heap[cur] = \
                self.object_heap[cur], self.object_heap[root_index]
            cur = root_index
            root_index = int((cur - 1)/2)

    def heapify(self):
        cur, left = 0, 1
        while left < self.index:
            smallest = left + 1 if left + 1 < self.index and \
                                   self.object_heap[left + 1].get_cost() < \
                                   self.object_heap[left].get_cost() else left
            smallest = cur if self.object_heap[cur].get_cost() < \
                             self.object_heap[smallest].get_cost() else smallest
            if smallest == cur:
                break
            self.object_heap[smallest], self.object_heap[cur] = \
                self.object_heap[cur], self.object_heap[smallest]
            cur = smallest
            left = 2 * cur + 1

    def pop(self):
        if self.index == -1:
            return None
        if self.index == 0:
            re = self.object_heap.pop()
        else:
            re = self.object_heap[0]
            self.object_heap[0] = self.object_heap.pop()
            self.heapify()
        self.index -= 1
        return re

    def peek(self):
        if self.index != -1:
            return self.object_heap[0].get_cost()
        else:
            return None


class Project:
    def __init__(self, id, cost, profits):
        self.id = id
        self.cost = cost
        self.profits = profits

    def get_cost(self):
        return self.cost

    def get_profits(self):
        return self.profits

    def __str__(self):
        return "id:" + str(self.id) + "\tcost:" + str(self.cost) \
               + "\tprofits:" + str(self.profits)


def max_profits(cost, profits, w, k):
    project_list = []
    for i in range(len(cost)):
        project_list.append(Project(i+1, cost[i], profits[i]))
    print("projects: ")
    for i in range(len(project_list)):
        print(project_list[i])
    print("-" * 50)

    cost_heap = MinHeap()
    for pro in project_list:
        cost_heap.push(pro)
    profits_heap = MaxHeap()
    count = 0
    while count < k:
        while cost_heap.index != -1 and cost_heap.peek() <= w:
            profits_heap.push(cost_heap.pop())
        if profits_heap.index == -1:
            return w
        w += profits_heap.pop().get_profits()
        count += 1
    return w


if __name__ == "__main__":
    cost = [5, 10, 6, 20, 16]
    profits = [3, 2, 4, 9, 4]
    print(max_profits(cost, profits, 7, 5))
    print(max_profits(cost, profits, 7, 4))
