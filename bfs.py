# 广度优先遍历，利用队列实现
# 从源节点开始依次按照广度进队列，然后弹出；
# 每次弹出一个节点，把该节点所有没有进过队列的邻居节点放入队列，直到队列为空


class Queue:
    def __init__(self):
        self.queue = []

    def add(self, value):
        self.queue.insert(0, value)

    def poll(self):
        return self.queue.pop()

    def is_empty(self):
        return len(self.queue) == 0


def bfs(graph, node):
    queue = Queue()
    visited = set()
    queue.add(node)
    visited.add(node)
    while not queue.is_empty():
        cur = queue.poll()
        print(cur, end=" ")
        for i in range(len(graph)):
            if graph[cur - 1][i] == 1 and i + 1 not in visited:
                queue.add(i + 1)
                visited.add(i + 1)

if __name__ == "__main__":
    graph = [[0, 1, 1, 1, 0, 0],
             [1, 0, 1, 0, 1, 0],
             [1, 1, 0, 0, 1, 1],
             [1, 0, 0, 0, 0, 0],
             [0, 1, 1, 0, 0, 1],
             [0, 0, 1, 0, 1, 0]]
    bfs(graph, 3)