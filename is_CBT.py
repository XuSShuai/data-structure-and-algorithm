# 判断一棵树是不是完全二叉树CBT
import queue


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def is_complete_binary_tree(head):
    if head:
        que = queue.Queue(-1)
        que.put(head)
        all_leaf = False
        while not que.empty():
            head = que.get()
            left = head.left
            right = head.right
            # ____ right return False
            # left right all_leaf = False
            # left _____ all_leaf = True
            # ____ _____ all_leaf = True
            if (right and left is None) or (all_leaf and (left or right)):
                return False
            if left:
                que.put(left)
            if right:
                que.put(right)
            else:
                all_leaf = True
        return True


if __name__ == "__main__":
    head = Node(1)
    head.left = Node(2)
    head.right = Node(3)
    head.left.left = Node(4)
    head.left.right = Node(5)

    print(is_complete_binary_tree(head))

    head.right.right = Node(6)

    print(is_complete_binary_tree(head))