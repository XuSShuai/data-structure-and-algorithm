#  返回数组内每一个元素左右最邻近的最大值(单调栈最原始的作用)


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)


def get_neighbor_max(arr):
    stack = Stack()
    left_max = [0] * len(arr)
    right_max = [0] * len(arr)
    for i in range(len(arr)):
        while not stack.empty() and arr[i] > arr[stack.peek()]:
            cur = stack.pop()
            right_max[cur] = arr[i]
            left_max[cur] = "#" if stack.empty() is True else arr[stack.peek()]
        stack.push(i)

    while not stack.empty():
        cur = stack.pop()
        right_max[cur] = "#"
        left_max[cur] = "#" if stack.empty() is True else arr[stack.peek()]

    print(arr)
    for i in zip(arr, left_max, right_max):
        print(i[0], i[1], i[2])

if __name__ == "__main__":
    arr = [7, 11, 2, 4, 3, 12, 9, 3]
    get_neighbor_max(arr)

    # doesn't works when arr contains one element more than one times, as following
    arr = [7, 11, 2, 4, 3, 3, 12, 9, 3]
    get_neighbor_max(arr)
