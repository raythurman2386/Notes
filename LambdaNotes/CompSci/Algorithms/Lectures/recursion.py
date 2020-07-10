import time
from random import shuffle

arr = [num for num in range(1, 51)]
shuffle(arr)


def partition(array):
    # break the array into left, pivot, right
    left = []
    pivot = array[0]
    right = []

    # Partition the array
    for num in array[1:]:
        if num <= pivot:
            left.append(num)
        else:
            right.append(num)

    return left, pivot, right


def quicksort(array):
    # base case
    if len(array) <= 1:
        return array
    # Partition the data
    left, pivot, right = partition(array)
    # make usre an array of size one
    return quicksort(left) + [pivot] + quicksort(right)


print(quicksort(arr))
