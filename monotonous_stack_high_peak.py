#  数组[2, 3, 6, 4, 3]表示首尾相连的山峰高度，两个山峰之间如果没有
#  更高的山峰则记为一对儿可以相互看到的山峰，相邻的两座山峰之间必能相互看到。
#  求，对于给定的数组arr，有多少对山峰是可以相互看到的


class Node:
    def __init__(self, value):
        self.value = value
        self.time = 1


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, obj):
        self.stack.append(obj)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)


def get_next_index(cur_index, size):
    return 0 if cur_index == size - 1 else cur_index + 1


def comb(num):
    return (num * (num - 1)) / 2


def get_peak_pair(arr):
    max_index = arr.index(max(arr))
    index = get_next_index(max_index, len(arr))
    max_stack = Stack()
    max_stack.push(Node(max_index))
    res = 0
    while index != max_index:
        while not max_stack.empty() and arr[index] > arr[max_stack.peek().value]:
            cur = max_stack.pop()
            res += comb(cur.time) + 2 * cur.time
        if not max_stack.empty() and arr[index] == arr[max_stack.peek().value]:
            max_stack.peek().time += 1
        else:
            max_stack.push(Node(index))
        index = get_next_index(index, len(arr))

    while not max_stack.empty():
        if max_stack.size() > 2:
            cur = max_stack.pop()
            res += comb(cur.time) + 2 * cur.time
        else:
            sec = max_stack.pop()
            fir = max_stack.pop()
            if fir.time == 1:
                res += comb(sec.time) + sec.time + comb(fir.time)
            else:
                res += comb(sec.time) + 2 * sec.time + comb(fir.time)

    return int(res)

if __name__ == "__main__":
    arr = [12, 2, 4, 5, 3, 11, 23]
    print(get_peak_pair(arr))