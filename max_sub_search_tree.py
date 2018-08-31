#  给定一棵二叉树的头节点head， 返回最大搜索二叉子树的大小
import sys
import networkx as nx
import matplotlib.pyplot as plt


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class ReturnInfo:
    def __init__(self, size: int, head: Node, max_v: int, min_v: int):
        self.size = size
        self.head = head
        self.max_v = max_v
        self.min_v = min_v


def get_max(head):
    if head is None:
        return ReturnInfo(0, None, -sys.maxsize, sys.maxsize)

    left_info = get_max(head.left)
    right_info = get_max(head.right)

    size = left_info.size if left_info.size > right_info.size else right_info.size
    if left_info.head == head.left and right_info.head == head.right \
            and left_info.max_v < head.value < right_info.min_v:
        size = left_info.size + right_info.size + 1

    new_head = left_info.head if left_info.size > right_info.size else right_info.head
    new_head = head if size == left_info.size + right_info.size + 1 else new_head

    return ReturnInfo(size,
                      new_head,
                      max([max([left_info.max_v, right_info.max_v]), head.value]),
                      min([min([left_info.min_v, right_info.min_v]), head.value]))


def get_max_sub_search_tree(head):
    return get_max(head).size


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
    fig, ax = plt.subplots(figsize=(8, 10))
    nx.draw_networkx(graph, pos, ax=ax, node_size=300)
    plt.show()


if __name__ == "__main__":
    head = Node(7)
    head.left = Node(9)
    head.right = Node(16)
    head.left.left = Node(10)
    head.left.right = Node(2)
    head.right.left = Node(15)
    head.right.right = Node(17)
    head.left.left.left = Node(8)
    head.left.left.right = Node(11)
    head.left.left.left.left = Node(6)

    # draw(head)

    print(get_max_sub_search_tree(head))

