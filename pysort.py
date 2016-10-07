__author__ = 'ace139'
__email__ = 'soumyodey@live.com'
"""
This program is implementation of different sorting algorithms,
also could be imported as a module in other programs.
"""


def insertion_sort(arr):
    for p in range(1, len(arr)):
        key = arr[p]
        c = p - 1
        while c >= 0 and arr[c] > key:
            arr[c + 1] = arr[c]
            c -= 1
        arr[c + 1] = key
    return arr


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_arr = arr[:mid]
        right_arr = arr[mid:]

        merge_sort(left_arr)
        merge_sort(right_arr)

        i, j, z = 0, 0, 0

        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[z] = left_arr[i]
                i += 1
            else:
                arr[z] = right_arr[j]
                j += 1
            z += 1

        while i < len(left_arr):
            arr[z] = left_arr[i]
            i += 1
            z += 1

        while j < len(right_arr):
            arr[z] = right_arr[j]
            j += 1
            z += 1
    return arr


def bubble_sort(arr):
    l = len(arr)
    for i in range(l - 1):
        for j in range(l - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def driver(c, arr):
    option = {
        0: insertion_sort,
        1: bubble_sort,
        2: merge_sort
    }
    func = option.get(c)
    result = func(arr)
    for r in result:
        print(r, end=" ")


if __name__ == '__main__':
    print("Select any Sorting Algorithm")
    choices = {
        "0": "insertion sort",
        "1": "bubble sort",
        "2": "merge sort"
    }
    for k, v in sorted(choices.items()):
        print("%s : %s" % (k, v))
    ch = int(input("Enter your choice : "))
    var = input("Enter the array to perform sorting : ")
    array = list(map(int, var.split(" ")))
    driver(ch, array)
