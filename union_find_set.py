# 并查集结构
#   判断两个节点是否属于同一个集合
#   对两个节点所属的集合进行合并
import queue


class UnionFindSet:
    def __init__(self, data_set):
        self.data = data_set
        self.father_map = dict()
        self.size_map = dict()
        for x in data_set:
            self.father_map[x] = x
            self.size_map[x] = 1

    def __find_head(self, node):
        que = queue.Queue(-1)
        while self.father_map.get(node) != node:
            que.put(node)
            node = self.father_map.get(node)
        while not que.empty():
            self.father_map[que.get()] = node
        return node

    def is_same_set(self, a, b):
        return self.__find_head(a) == self.__find_head(b)

    def union(self, a, b):
        a_head = self.__find_head(a)
        b_head = self.__find_head(b)
        if a_head != b_head:
            a_size = self.size_map[a_head]
            b_size = self.size_map[b_head]
            if a_size < b_size:
                self.father_map[a_head] = b_head
                self.size_map[b_head] += a_size
            else:
                self.father_map[b_head] = a_head
                self.size_map[a_head] += b_size


if __name__ == "__main__":
    data_set = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    ufs = UnionFindSet(data_set)
    print("ufs.is_same_set(1, 10):", ufs.is_same_set(1, 10))

    ufs.union(1, 2)
    ufs.union(3, 4)
    ufs.union(4, 5)
    print("ufs.is_same_set(3, 5):", ufs.is_same_set(3, 5))
    ufs.union(2, 3)

    # 2 -> 1 -> 3 <- 4
    #           ^
    #           5

    print("ufs.father_map[2]:", ufs.father_map[2])
    print("ufs.father_map[1]:", ufs.father_map[1])
    print("ufs.is_same_set(1, 5):", ufs.is_same_set(1, 5))
    print("-" * 50)

    ufs.union(9, 8)
    ufs.union(8, 7)
    ufs.union(6, 7)

    # 7 -> 9 <- 8
    #      ^
    #      6

    print("ufs.is_same_set(2, 8):", ufs.is_same_set(2, 8))
    print("-" * 50)

    ufs.union(2, 8)
    print("ufs.is_same_set(2, 8):", ufs.is_same_set(2, 8))
    print("ufs.father_map[9]:", ufs.father_map[9])
    print("ufs.father_map[2]:", ufs.father_map[2])
