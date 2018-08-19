# 判断一个链表是否为回文结构
# 题目: 给定一个链表的头节点head， 请判断该链表是否为回
# 文结构。 例如： 1->2->1， 返回true。 1->2->2->1， 返回true。
# 15->6->15， 返回true。 1->2->3， 返回false。
# 如果链表长度为N， 时间复杂度达到O(N)， 额外空间复杂度达到O(1)。
import queue


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Link:
    def __init__(self):
        self.head = None

    def append(self, value):
        new = Node(value)
        p = self.head
        if p is None:
            self.head = new
        else:
            while p.next:
                p = p.next
            p.next = new

    def print_link(self):
        p = self.head
        while p:
            print(p.data, end=" ")
            p = p.next
        print()


def is_palindrome_list_n(link):
    # n extra space

    stack = queue.LifoQueue(-1)
    p = link.head
    while p:
        stack.put(p.data)
        p = p.next

    p = link.head
    while not stack.empty():
        e = stack.get()
        d = p.data
        if e != d:
            return False
        p = p.next
    return True


def is_palindrome_list_n_2(link):
    # n/2 extra space
    slow = link.head
    fast = link.head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    stack = queue.LifoQueue(-1)
    slow = slow.next
    while slow:
        stack.put(slow.data)
        slow = slow.next
    p = link.head
    while not stack.empty():
        if stack.get() != p.data:
            return False
        p = p.next
    return True


def is_palindrome_list_1(link):
    # O(1) extra space
    slow = link.head
    fast = link.head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    fast = slow.next
    slow.next = None
    slow = None
    cur = fast
    while cur:
        fast = cur.next
        cur.next = slow
        slow = cur
        cur = fast
    cur = link.head
    while slow and cur:
        if slow.data != cur.data:
            return False
        slow = slow.next
        cur = cur.next
    return True

if __name__ == "__main__":
    # link = Link()
    # link.append(1)
    # link.append(2)
    # link.print_link()
    # print(is_palindrome_list_n(link))
    # link.append(2)
    # link.append(1)
    # link.print_link()
    # print(is_palindrome_list_n(link))
    # link.append(2)
    # link.append(2)
    # link.append(1)
    # link.print_link()
    # print(is_palindrome_list_n(link))

    # link = Link()
    # link.append(1)
    # link.print_link()
    # print(is_palindrome_list_n_2(link))
    # link.append(2)
    # link.print_link()
    # print(is_palindrome_list_n_2(link))
    # link.append(2)
    # link.append(1)
    # link.print_link()
    # print(is_palindrome_list_n_2(link))
    # link.append(2)
    # link.append(2)
    # link.append(1)
    # link.print_link()
    # print(is_palindrome_list_n_2(link))

    link = Link()
    link.append(1)
    link.print_link()
    print(is_palindrome_list_1(link))
    link.append(2)
    link.print_link()
    print(is_palindrome_list_1(link))
    link.append(2)
    link.append(1)
    link.print_link()
    print(is_palindrome_list_1(link))
    link.append(2)
    link.append(2)
    link.append(1)
    link.print_link()
    print(is_palindrome_list_1(link))