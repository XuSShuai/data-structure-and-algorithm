#  介绍二叉树的序列化和反序列化
import queue


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def serialize_by_pre(head):
    if head is None:
        return "#_"
    res = str(head.data) + "_"
    res += serialize_by_pre(head.left)
    res += serialize_by_pre(head.right)
    return res


def re_serialize_by_pre_driver(str):
    que = queue.Queue(-1)
    str = str.split("_")
    for x in str:
        que.put(x)
    return re_serialize_by_pre(que)


def re_serialize_by_pre(que):
    item = que.get()
    if item == "#":
        return None
    else:
        head = Node(item)
        head.left = re_serialize_by_pre(que)
        head.right = re_serialize_by_pre(que)
        return head


def pre_order_traversal(head):
    if head is None:
        return
    print(head.data, end=" ")
    pre_order_traversal(head.left)
    pre_order_traversal(head.right)

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

    print("pre order traversal: ")
    pre_order_traversal(head)
    print()
    print("after serializing: ")
    serial_pre = serialize_by_pre(head)
    print(serial_pre)

    print("re-serializing: (pre order)")
    tree = re_serialize_by_pre_driver(serial_pre)
    pre_order_traversal(tree)


