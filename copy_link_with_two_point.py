# 复制含有随机指针节点的链表
# [题目] 一种特殊的链表节点类描述如下：
# public class Node {
#   public int value;
#   public Node next;
#   public Node rand;
#   public Node(int data) {
#       this.value = data;
#   }
# }
#
# Node类中的value是节点值， next指针和正常单链表中next指针的意义一样，都指向下一个节点，
# rand指针是Node类中新增的指针， 这个指针可能指向链表中的任意一个节点， 也可能指向null。
# 给定一个由Node节点类型组成的无环单链表的头节点head， 请实现一个函数完成这个链表中所有
# 结构的复制， 并返回复制的新链表的头节点。
# 进阶：
# 不使用额外的数据结构， 只用有限几个变量， 且在时间复杂度为 O(N)内完成原问题要实现的函数。


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.random = None


def copy_deep(head):
    new2old = dict()
    cur = head
    while cur:
        new2old[cur] = Node(cur.value)
        cur = cur.next
    cur = head
    while cur:
        new2old[cur].next = cur.next
        new2old[cur].random = cur.random
        cur = cur.next
    return new2old[head]


def print_link(head):
    cur = head
    print("next link: ", end=" ")
    while cur:
        print(cur.value, end=" ")
        cur = cur.next
    print("\nrandom link")
    cur = head
    while cur:
        print(str(cur.value) + " " + str(" " if cur.random is None else cur.random.value))
        cur = cur.next

if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)

    head.random = head.next.next.next.next.next  # 1 -> 6
    head.next.random = head.next.next.next.next.next  # 2 -> 6
    head.next.next.random = head.next.next.next.next  # 3 -> 5
    head.next.next.next.random = head.next.next  # 4 -> 3
    head.next.next.next.next.random = None  # 5 -> null
    head.next.next.next.next.next.random = head.next.next.next  # 6 -> 4

    print_link(head)
    print()

    new_head = copy_deep(head)
    print_link(new_head)

    print()
    print_link(head)
