# 使用递归函数求出一棵二叉树的最大值和最小值


import sys


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class ReturnInfo:
    def __init__(self, min, max):
        self.min = min
        self.max = max


def get_max_min(head):
    if head is None:
        return ReturnInfo(sys.maxsize, -sys.maxsize)
    right_info = get_max_min(head.right)
    left_info = get_max_min(head.left)

    return ReturnInfo(min([min([left_info.min, right_info.min]), head.data]),
                      max([max([left_info.max, right_info.max]), head.data]))


if __name__ == "__main__":
    head = Node(4)
    head.left = Node(12)
    head.right = Node(6)
    head.left.left = Node(11)
    head.left.right = Node(1)
    head.right.right = Node(3)

    print("max: ", get_max_min(head).max)
    print("min: ", get_max_min(head).min)
