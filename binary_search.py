# not recursion
def binary_search(array, key):
    start, end = 0, len(array) - 1
    while start <= end:
        mid = (end - start) // 2 + start
        if array[mid] == key:
            return mid
        elif key < array[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return -1


# recursion
def binary_search_recursion(array, key, start, end):
    if start > end:
        return -1
    mid = (end - start) // 2 + start
    if array[mid] == key:
        return mid
    elif key < array[mid]:
        return binary_search_recursion(array, key, start, mid - 1)
    else:
        return binary_search_recursion(array, key, mid + 1, end)
    return -1

if __name__ == "__main__":
    array = [3,5,11,17,21,23,28,30,32,50,64,78,81,95,101]
    print(binary_search(array, 28))
    print(binary_search(array, 31))

    print(binary_search_recursion(array, 28, 0, len(array) - 1))
    print(binary_search_recursion(array, 31, 0, len(array) - 1))
