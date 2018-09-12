def kmp(string1, string2):
    string1 = list(string1)
    string2 = list(string2)
    p = 0
    q = 0
    next = get_next(string2)
    while p < len(string1) and q < len(string2):
        if string1[p] == string2[q]:
            p += 1
            q += 1
        elif next[q] == -1:  # q at the first of string2
            p += 1
        else:
            q = next[q]
    return p - q if q == len(string2) else -1


def get_next(string):
    next = [0] * len(string)
    next[0] = -1
    next[1] = 0
    i = 2
    back = 0
    while i < len(string):
        if string[i - 1] == string[back]:
            next[i] = back + 1
            back = next[i]
            i += 1
        elif back <= 0:
            next[i] = 0
            i += 1
        else:
            back = next[back]
    return next


if __name__ == "__main__":
    string1 = "abcedabcttabcdrtd"

    string2 = "abacabat"
    print(string1.find(string2))
    print(kmp(string1, string2))

    string2 = "abcd"
    print(string1.find(string2))
    print(kmp(string1, string2))


    string1 = "周杰伦"
    string2 = "今天是周杰伦的演唱会"

    print(kmp(string2, string1))