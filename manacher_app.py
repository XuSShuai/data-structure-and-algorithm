#  给定一个字符串，求一个最短的字符串加在该字符串之后
#  使得整体字符串为回文字符串


def manacher_string(string):
    res = [0] * (2 * len(string) + 1)
    for i in range(len(res)):
        res[i] = "#" if i % 2 == 0 else string[i//2]
    return res


def shortest_end(string):
    string = manacher_string(string)
    res_arr = [0] * len(string)
    R = -1
    C = -1
    max_contains_end = -1

    for i in range(len(string)):
        res_arr[i] = 1 if i >= R else min([R - i + 1, res_arr[2 * C - i]])
        while i + res_arr[i] < len(string) and i - res_arr[i] > -1:
            if string[i + res_arr[i]] == string[i - res_arr[i]]:
                res_arr[i] += 1
            else:
                break
        if R < i + res_arr[i]:
            R = i + res_arr[i]
            C = i
        if R == len(string):
            max_contains_end = res_arr[i]
            break

    print(max_contains_end)
    end_string = [""] * (len(string)//2 - (max_contains_end - 1))
    for i in range(len(end_string)):
        end_string[len(end_string) - i - 1] = string[2 * i + 1]
    return "".join(end_string)

if __name__ == "__main__":
    end = shortest_end("abcdc")
    print(end)
    end = shortest_end("qwerasdfdsa")
    print(end)