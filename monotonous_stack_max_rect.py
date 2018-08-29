#  求最大子矩阵的大小
#  给定一个整形矩阵，其中的值只有0和1，求由值1构成的矩形区域中面积最大的矩形局域中1的个数
#  1 0 1 1
#  1 1 1 1
#  1 1 1 0
#  的返回值为6
#
# 使用从小到大的单调栈来找到一个数左右最邻近的最小值


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


def max_histogram(arr):
    # arr = height = [3, 2, 4, 5, 6]
    min_stack = Stack()
    max_area = 0
    for i in range(len(arr)):
        while not min_stack.empty() and arr[i] <= arr[min_stack.peek()]:
            cur = min_stack.pop()
            left = -1 if min_stack.empty() else min_stack.peek()
            max_area = max([max_area, arr[cur] * (i - left - 1)])
        min_stack.push(i)

    while not min_stack.empty():
        cur = min_stack.pop()
        left = -1 if min_stack.empty() is True else min_stack.peek()
        right = len(arr)
        max_area = max([max_area, arr[cur] * (right - left - 1)])
    return max_area


def max_rectangle(matrix):
    row = len(matrix)
    col = len(matrix[0])
    histogram = [0] * col
    max_area = 0
    for i in range(row):
        for j in range(col):
            histogram[j] = 0 if matrix[i][j] == 0 else histogram[j] + 1
        max_area = max([max_area, max_histogram(histogram)])
    return max_area


if __name__ == "__main__":
    arr = [4, 3, 2, 5, 6]
    print(max_histogram(arr))
    matrix = [[1, 0, 1, 1],
              [1, 1, 1, 1],
              [1, 1, 1, 0]]
    print(max_rectangle(matrix))
    matrix = [[1, 1, 0, 0, 0],
              [0, 1, 1, 1, 0],
              [0, 1, 1, 0, 0],
              [0, 0, 1, 1, 1]]
    print(max_rectangle(matrix))
