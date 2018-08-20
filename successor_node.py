# 在二叉树中找到一个节点的后继节点


class Node:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None


def get_successor_node(node):
    if node:
        if node.right:
            node = node.right
            while node.left:
                node = node.left
            return node
        else:  # node.right = None
            parent = node.parent
            while parent and parent.left != node:
                node = parent
                parent = parent.parent
            return parent
    return None


def in_order_traversal(head):
    if head is None:
        return
    in_order_traversal(head.left)
    print(head.data, end=" ")
    in_order_traversal(head.right)


if __name__ == "__main__":
    head = Node(6)
    head.parent = None
    head.left = Node(3)
    head.left.parent = head
    head.right = Node(9)
    head.right.parent = head
    head.left.left = Node(1)
    head.left.right = Node(4)
    head.left.left.parent = head.left
    head.left.right.parent = head.left
    head.left.left.right = Node(2)
    head.left.left.right.parent = head.left.left
    head.left.right.right = Node(5)
    head.left.right.right.parent = head.left.right
    head.right.left = Node(8)
    head.right.left.parent = head.right
    head.right.right = Node(10)
    head.right.right.parent = head.right
    head.right.left.left = Node(7)
    head.right.left.left.parent = head.right.left

    print("in order traversal: ")
    in_order_traversal(head)
    print()

    print("successor node of 5: ", get_successor_node(head.left.right.right).data)
    print("successor node of 6: ", get_successor_node(head).data)
    print("successor node of 10:", get_successor_node(head.right.right))
    print("successor node of 1: ", get_successor_node(head.left.left).data)