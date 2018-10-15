class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


def node_number(head):
    if head:
        return complete_tree_node_number(head, 1, get_most_left_level(head, 1))


def complete_tree_node_number(head, level, tree_height):
    if level == tree_height:
        return 1
    if get_most_left_level(head.right, level + 1) == tree_height:
        return 1 + 2 ** (tree_height - level) - 1 + complete_tree_node_number(head.right, level + 1, tree_height)
    else:
        return 2 ** (tree_height - level - 1) - 1 + 1 + complete_tree_node_number(head.left, level + 1, tree_height)


def get_most_left_level(head, level):
    """
    返回位于level层的节点head的最左侧子节点的层数
    """
    while head:
        head = head.left
        level += 1
    return level - 1


if __name__ == "__main__":
    head = Node(1)
    head.left = Node(2)
    head.right = Node(3)
    head.left.left = Node(4)
    head.left.right = Node(5)
    head.right.left = Node(6)
    head.right.right = Node(7)
    head.left.left.left = Node(8)
    head.left.left.right = Node(9)

    print("node number of complete is: ", node_number(head))

    head.left.right.left = Node(10)

    print("node number of complete is: ", node_number(head))


