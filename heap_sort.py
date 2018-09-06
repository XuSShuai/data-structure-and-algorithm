import numpy as np
import operator
import copy


def heap_insert(arr, index):
    root_index = int((index - 1)/2)
    while arr[index] > arr[root_index]:
        arr[index], arr[root_index] = arr[root_index], arr[index]
        index = root_index
        root_index = int((index - 1) / 2)


def heapify(arr, index, heap_size):
    left = 2 * index + 1
    while left < heap_size:
        largest = left + 1 if left + 1 < heap_size and arr[left + 1] > arr[left] else left
        largest = index if arr[index] > arr[largest] else largest
        if largest == index:
            break
        arr[largest], arr[index] = arr[index], arr[largest]
        index = largest
        left = 2 * index + 1


def heap_sort(arr):
    for i in range(len(arr)):
        heap_insert(arr, i)
    heap_size = len(arr)
    for i in range(len(arr) - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heap_size -= 1
        heapify(arr, 0, heap_size)


def correct_method(arr):
    return sorted(arr)


def generate_cases():
    for i in range(10000):
        arr = list(np.random.randint(1, 100, 10))
        res_1 = copy.deepcopy(arr)
        heap_sort(res_1)
        res_2 = correct_method(arr)

        if not operator.eq(res_2, res_1):
            print(arr)
            print(res_1)
            print(res_2)
            print("error")
            break

if __name__ == "__main__":
    generate_cases()

    arr = [2, 4, 5, 3, 9, 8, 11, 4, 12]
    heap_sort(arr)
    print(arr)
