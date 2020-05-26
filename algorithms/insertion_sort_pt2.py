def insertionSort2(arr):
    a = arr
    for i in range(1, len(arr)):
        index = next(iter(j for j in range(i) if a[j] > a[i]), i)
        a[index+1:i+1], a[index] = a[index:i], a[i]
        print(*a)


insertionSort2([1, 4, 3, 5, 6, 2])
