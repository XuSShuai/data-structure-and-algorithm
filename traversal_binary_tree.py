import queue


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def pre_order_recursive(head):
    if not head:
        return
    print(head.data, end=" ")
    pre_order_recursive(head.left)
    pre_order_recursive(head.right)


def in_order_recursive(head):
    if not head:
        return
    in_order_recursive(head.left)
    print(head.data, end=" ")
    in_order_recursive(head.right)


def post_order_recursive(head):
    if not head:
        return
    post_order_recursive(head.left)
    post_order_recursive(head.right)
    print(head.data, end=" ")


def pre_order(head):
    # root -> left -> right
    if head:
        stack = queue.LifoQueue(-1)
        stack.put(head)
        while not stack.empty():
            head = stack.get()
            print(head.data, end=" ")
            if head.right:
                stack.put(head.right)
            if head.left:
                stack.put(head.left)
    print()


def in_order(head):
    # left -> root -> right
    if head:
        stack = queue.LifoQueue(-1)
        while head or not stack.empty():
            if head:
                stack.put(head)
                head = head.left
            else:
                head = stack.get()
                print(head.data, end=" ")
                head = head.right
        print()


def post_order(head):
    # left -> right -> root
    if head:
        stack = queue.LifoQueue(-1)
        auxiliary_stack = queue.LifoQueue(-1)
        stack.put(head)
        while not stack.empty():
            head = stack.get()
            auxiliary_stack.put(head.data)
            if head.left:
                stack.put(head.left)
            if head.right:
                stack.put(head.right)
        while not auxiliary_stack.empty():
            print(auxiliary_stack.get(), end=" ")
        print(" ")


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

    print("=" * 50)
    pre_order_recursive(head)
    print()
    in_order_recursive(head)
    print()
    post_order_recursive(head)
    print()

    print("=" * 50)
    pre_order(head)
    in_order(head)
    post_order(head)