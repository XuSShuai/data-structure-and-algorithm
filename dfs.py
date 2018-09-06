# 深度优先遍历，利用栈实现
# 从源节点开始依次按照深度进栈，然后弹出；
# 每次弹出一个节点，把该节点下一个没有进过栈的邻居节点放入栈，直到栈为空


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        return self.stack.pop()

    def is_empty(self):
        return len(self.stack) == 0


def dfs(graph, node):
    stack = Stack()
    visited = set()
    stack.push(node)
    visited.add(node)
    print(node, end=" ")
    while not stack.is_empty():
        cur = stack.pop()
        for i in range(len(graph)):
            if graph[cur - 1][i] == 1 and i + 1 not in visited:
                stack.push(cur)
                stack.push(i + 1)
                visited.add(i + 1)
                print(i + 1, end=" ")
                break

if __name__ == "__main__":
    graph = [[0, 1, 1, 1, 0, 0],
             [1, 0, 1, 0, 1, 0],
             [1, 1, 0, 0, 1, 1],
             [1, 0, 0, 0, 0, 0],
             [0, 1, 1, 0, 0, 1],
             [0, 0, 1, 0, 1, 0]]
    dfs(graph, 1)