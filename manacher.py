# manacher 算法


def manacher_string(string):
    string = list(string)
    res = [""] * (2 * len(string) + 1)
    for i in range(len(res)):
        res[i] = string[int(i/2)] if i % 2 != 0 else "#"
    return res


def manacher(string):
    string = manacher_string(string)
    C, R = -1, -1
    res_arr = [0] * len(string)
    max_value = 0
    for i in range(len(string)):
        res_arr[i] = 1 if i >= R else min([R - i + 1, res_arr[2 * C - i]])
        while i + res_arr[i] < len(string) and i - res_arr[i] > -1:
            if string[i + res_arr[i]] == string[i - res_arr[i]]:
                res_arr[i] += 1
            else:
                 break
        if i + res_arr[i] > R:
            R = i + res_arr[i]
            C = i

        max_value = max([max_value, res_arr[i]])
    return max_value - 1

if __name__ == "__main__":
    string = "tfasdtftdsaktt"
    print(manacher(string))
    string = "asdfghjkl"
    print(manacher(string))
    string = "srddfaddafdTdfdsffsdt"
    print(manacher(string))