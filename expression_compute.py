# 给定一个字符串str， str表示一个公式， 公式里可能有整数、 加减乘除符号和
# 左右括号， 返回公式的计算结果。
# 【举例】
# str="48*((70-65)-43)+8*1"， 返回-1816。
# str="3+1*4"， 返回7。 str="3+(1*4)"， 返回7。
# 【说明】
# 1． 可以认为给定的字符串一定是正确的公式， 即不需要对str做公式有效性检查。
# 2． 如果是负数， 就需要用括号括起来， 比如"4*(-3)"。 但如果负数作为公式的开头或括号部分的开头，
#     则可以没有括号， 比如"-3*4"和"(-3*4)"都是合法的。
# 3． 不用考虑计算过程中会发生溢出的情况
from collections import deque


def expression_compute(string):
    return in_bracket(string, 0)[0]


def in_bracket(string, i):
    double_end_queue = deque([])
    num = 0
    while i < len(string) and string[i] != ")":
        if ord("0") <= ord(string[i]) <= ord("9"):
            num = num * 10 + int(string[i])
            i += 1
        elif string[i] != "(":  # + - * / and end of the num
            add_num(double_end_queue, num)
            double_end_queue.append(string[i])
            i += 1
            num = 0
        else:  # "("
            num, i = in_bracket(string, i + 1)
    add_num(double_end_queue, num)
    return get_num(double_end_queue), i + 1


def add_num(double_end_queue, num):
    if double_end_queue.__len__() != 0:
        op_item = double_end_queue.pop()
        if op_item == "+" or op_item == "-":
            double_end_queue.append(op_item)
        else:
            another_num = double_end_queue.pop()
            num = another_num * num if op_item == "*" else another_num // num
    double_end_queue.append(num)


def get_num(double_end_queue):
    add = True
    res = 0
    while len(double_end_queue) != 0:
        item = double_end_queue.popleft()
        if item == "+":
            add = True
        elif item == "-":
            add = False
        else:
            res = res + item if add else res - item
    return res

if __name__ == "__main__":
    exp = "48*((70-65)-43)+8*1"  # -1816
    print(expression_compute(exp))
    exp = "4*(6+78)+53-9/2+45*8"  # 745
    print(expression_compute(exp))
    exp = "10-5*3"
    print(expression_compute(exp))
    exp = "-3*4"
    print(expression_compute(exp))
    exp = "3+1*4"
    print(expression_compute(exp))
