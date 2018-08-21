#  判断一棵树是否是搜索二叉树BST
import queue
import sys


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def is_binary_search_tree(head):
    stack = queue.LifoQueue(-1)
    if head:
        pre_data = -sys.maxsize - 1
        while head or not stack.empty():
            if head:
                stack.put(head)
                head = head.left
            else:
                head = stack.get()
                if pre_data > head.data:
                    return False
                else:
                    pre_data = head.data
                head = head.right
        return True


if __name__ == "__main__":
    head = Node(5)
    head.left = Node(3)
    head.right = Node(8)
    head.left.left = Node(2)
    head.left.left.left = Node(1)
    head.left.right = Node(4)
    head.right.left = Node(7)
    head.right.left.left = Node(6)
    head.right.right = Node(10)
    head.right.right.left = Node(9)
    head.right.right.right = Node(11)

    print(is_binary_search_tree(head))

    head = Node(3)
    head.left = Node(2)
    head.left.left = Node(1)
    head.left.right = Node(4)
    print(is_binary_search_tree(head))