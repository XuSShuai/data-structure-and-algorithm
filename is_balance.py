# 判断一棵二叉树是否是平衡二叉树


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class ReturnInfo:
    def __init__(self, is_balance: bool, height: int):
        self.is_balance = is_balance
        self.height = height


def is_balance_tree(head):
    if head is None:
        return ReturnInfo(True, 0)

    left_info = is_balance_tree(head.left)
    if not left_info.is_balance:
        return ReturnInfo(False, 0)
    right_info = is_balance_tree(head.right)
    if not right_info.is_balance:
        return ReturnInfo(False, 0)
    if abs(left_info.height - right_info.height) > 1:
        return ReturnInfo(False, 0)
    else:
        return ReturnInfo(True, max([left_info.height, right_info.height]) + 1)


def is_balance_driver(head):
    return is_balance_tree(head).is_balance


if __name__ == "__main__":
    tree = Node(1)
    tree.left = Node(2)
    tree.left.left = Node(3)
    tree.right = Node(4)

    print(is_balance_driver(tree))

    tree1 = Node(1)
    tree1.left = Node(2)
    tree1.left.left = Node(3)

    print(is_balance_driver(tree1))