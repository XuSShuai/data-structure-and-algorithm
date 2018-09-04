# 设计可以变更的缓存结构（LRU）
# 【题目】
# 设计一种缓存结构， 该结构在构造时确定大小， 假设大小为K， 并有两个功能：
# set(key,value)： 将记录(key,value)插入该结构。
# get(key)： 返回key对应的value值。
# 【要求】
# 1． set和get方法的时间复杂度为O(1)。
# 2． 某个key的set或get操作一旦发生， 认为这个key的记录成了最经常使用的。
# 3． 当缓存的大小超过K时， 移除最不经常使用的记录， 即set或get最久远的。
# 【举例】
# 假设缓存结构的实例是cache， 大小为3， 并依次发生如下行为：
# 1． cache.set("A",1)。 最经常使用的记录为("A",1)。
# 2． cache.set("B",2)。 最经常使用的记录为("B",2)， ("A",1)变为最不经常的。
# 3． cache.set("C",3)。 最经常使用的记录为("C",2)， ("A",1)还是最不经常的。
# 4． cache.get("A")。   最经常使用的记录为("A",1)， ("B",2)变为最不经常的。
# 5． cache.set("D",4)。 大小超过了3， 所以移除此时最不经常使用的记录("B",2)，
# 加入记录 ("D",4)， 并且为最经常使用的记录， 然后("C",2)变为最不经常使用的
# 记录


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.last = None
        self.next = None


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_node(self, new_node):
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.last = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def move_node_to_tail(self, node):
        if self.tail == node:
            return
        if node == self.head:
            self.head = self.head.next
            self.head.last = None
        else:
            node.next.last = node.last
            node.last.next = node.next
        self.tail.next = node
        node.last = self.tail
        self.tail = node
        node.next = None

    def remove_head(self):
        cur = self.head
        self.head = self.head.next
        self.head.last = None
        return cur.key

    def print_by_priority(self):
        cur = self.tail
        while cur:
            print("(" + str(cur.key) + "," + str(cur.value) + ")", end=" ")
            cur = cur.last
        print()


class MyCache:
    def __init__(self, size):
        self.size = size
        self.double_linked_list = DoubleLinkedList()
        self.key_map_node = dict()

    def set(self, key, value):
        if key in self.key_map_node.keys():
            node = self.key_map_node[key]
            node.value = value
        else:
            node = Node(key, value)
            self.key_map_node[key] = node
            self.double_linked_list.add_node(node)
        self.double_linked_list.move_node_to_tail(node)
        if len(self.key_map_node) == self.size + 1:
            pop_key = self.double_linked_list.remove_head()
            self.key_map_node.pop(pop_key)

    def get(self, key):
        if not key in self.key_map_node.keys():
            return None
        node = self.key_map_node[key]
        self.double_linked_list.move_node_to_tail(node)
        return node.value

if __name__ == "__main__":
    cache = MyCache(3)
    cache.set("A", 1)
    cache.set("B", 2)
    cache.set("C", 3)
    cache.double_linked_list.print_by_priority()
    cache.get("A")
    cache.double_linked_list.print_by_priority()
    cache.get("B")
    cache.double_linked_list.print_by_priority()
    cache.get("A")
    cache.double_linked_list.print_by_priority()
    cache.set("D", 4)
    cache.double_linked_list.print_by_priority()
    print(cache.get("A"))
    print(cache.get("C"))