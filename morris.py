#  空间复杂度为O(1)， 时间复杂度为O(N)的二叉树遍历方式
#  流程：
#  当前节点记为cur
#    1) 如果cur没有左孩子，cur向右移动，cur=cur.right
#    2) 如果cur有左孩子，找到左子树上最右的节点mostright
#         1) 如果mostright的右指针为空，则mostright指向cur，然后cur向左移动
#         2) 如果mostright的右指针指向cur，则mostright指向null，cur向右移动
#
# 递归和非递归的二叉树遍历算法都需要log(h)的额外空间复杂度，morris需要的是O(1)的空间复杂度


import networkx as nx
import matplotlib.pyplot as plt


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def morris(head):
    if head is None:
        return
    cur = head
    while cur:
        most_right = cur.left
        if most_right:
            while most_right.right and most_right.right != cur:
                most_right = most_right.right
            if most_right.right is None:   # first visit
                print(cur.value, end=" ")
                most_right.right = cur
                cur = cur.left
            else:   # second visit
                print(cur.value, end=" ")
                most_right.right = None
                cur = cur.right
        else:
            # only visit once
            print(cur.value, end=" ")
            cur = cur.right
    print()


def order(head):
    if head is None:
        return
    print(head.value, end=" ")
    order(head.left)
    print(head.value, end=" ")
    order(head.right)
    print(head.value, end=" ")


def morris_pre_order(head):
    if not head:
        return
    cur = head
    while cur:
        most_right = cur.left
        if most_right:
            while most_right.right and most_right.right != cur:
                most_right = most_right.right
            if most_right.right is None:  # first visit
                most_right.right = cur
                print(cur.value, end=" ")
                cur = cur.left
            else:  # second visit
                most_right.right = None
                cur = cur.right
        else:
            print(cur.value, end=" ")
            cur = cur.right
    print()


def morris_in_order(head):
    if not head:
        return
    cur = head
    while cur:
        most_right = cur.left
        if most_right:
            while most_right.right and most_right.right != cur:
                most_right = most_right.right
            if most_right.right is None:  # first visit
                most_right.right = cur
                cur = cur.left
            else:  # second visit
                print(cur.value, end=" ")
                most_right.right = None
                cur = cur.right
        else:
            print(cur.value, end=" ")
            cur = cur.right
    print()


def morris_post_order(head):
    if not head:
        return
    cur = head
    while cur:
        most_right = cur.left
        if most_right:
            while most_right.right and most_right.right != cur:
                most_right = most_right.right
            if most_right.right is None:
                most_right.right = cur
                cur = cur.left
            else:  # second visit
                most_right.right = None
                print_right_most_link(cur.left)
                cur = cur.right
        else:
            cur = cur.right
    print_right_most_link(head)
    print()


def print_right_most_link(pointer):
    end = reverse(pointer)
    cur = end
    while cur:
        print(cur.value, end=" ")
        cur = cur.right
    reverse(end)


def reverse(head):
    pre = None
    lat = head
    while lat.right:
        lat = lat.right
        head.right = pre
        pre = head
        head = lat
    head.right = pre
    return head


def create_graph(G, node, pos={}, x=0, y=0, layer=1):
    pos[node.value] = (x, y)
    if node.left:
        G.add_edge(node.value, node.left.value)
        l_x, l_y = x - 1 / 2 ** layer, y - 1
        l_layer = layer + 1
        create_graph(G, node.left, x=l_x, y=l_y, pos=pos, layer=l_layer)
    if node.right:
        G.add_edge(node.value, node.right.value)
        r_x, r_y = x + 1 / 2 ** layer, y - 1
        r_layer = layer + 1
        create_graph(G, node.right, x=r_x, y=r_y, pos=pos, layer=r_layer)
    return G, pos


def draw(node):
    graph = nx.DiGraph()
    graph, pos = create_graph(graph, node)
    fig, ax = plt.subplots(figsize=(8, 10))  # 比例可以根据树的深度适当调节
    nx.draw_networkx(graph, pos, ax=ax, node_size=300)
    plt.show()

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

    # draw(head)

    print("morris order:")
    morris(head)
    print("recursive order:")
    order(head)
    print()
    print("pre order by morris:")
    morris_pre_order(head)
    print("in order by morris:")
    morris_in_order(head)
    print("post order by morris:")
    morris_post_order(head)
    print("in order by morris:")
    morris_in_order(head)
