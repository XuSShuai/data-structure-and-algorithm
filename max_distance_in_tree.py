# 二叉树中， 一个节点可以往上走和往下走， 那么从节点A总能走到节点B。
# 节点A走到节点B的距离为： A走到B最短路径上的节点个数。
# 求一棵二叉树上的最远距离
import networkx as nx
import matplotlib.pyplot as plt


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class ReturnInfo:
    def __init__(self, max_distance, tree_height):
        self.max_distance = max_distance
        self.tree_height = tree_height


def process(head):
    if head is None:
        return ReturnInfo(0, 0)
    left_info = process(head.left)
    right_info = process(head.right)

    max_distance = max([max([left_info.max_distance, right_info.max_distance]),
                        left_info.tree_height + right_info.tree_height + 1])
    return ReturnInfo(max_distance, max([left_info.tree_height, right_info.tree_height]) + 1)


def get_max_distance(head):
    return process(head).max_distance


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
    head = Node(3)
    head.left = Node(2)
    head.left.left = Node(1)
    head.right = Node(4)
    head.right.right = Node(5)
    # draw(head)
    print(get_max_distance(head))

    head = Node(1)
    head.left = Node(2)
    head.right = Node(3)
    head.left.left = Node(4)
    head.left.right = Node(5)
    head.left.left.left = Node(6)
    head.left.right.right = Node(7)
    # draw(head)
    print(get_max_distance(head))