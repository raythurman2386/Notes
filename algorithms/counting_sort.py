def counting_sort(arr):
    str = ""
    for i in range(len(arr)//2):
        arr[i][1] = "-"

    for i in range(len(arr)):
        arr[i][0] = int(arr[i][0])

    a = sorted(arr, key=lambda x: x[0])

    for i in range(len(a)):
        str += a[i][1] + " "

    print(str)

def count(arr):
    cnt = len(arr)
    m = int(max(arr, key=lambda x: int(x[0]))[0])
    index = 0
    lst = [[] for i in range(m + 1)]
    for item in arr:
        index2 = int(item[0])
        value = item[1]
        if index < (cnt/2):
            value = "-"
        lst[index2].append(value)
        index += 1

    print((" ".join(map(" ".join, lst))).strip())

counting_sort([["1", "e"], ["2", "a"], ["1", "b"], ["3", "a"], ["4", "f"],["1", "f"], ["2", "a"], ["1", "e"], ["1", "b"], ["1", "c"]])

count([["1", "e"], ["2", "a"], ["1", "b"], ["3", "a"], ["4", "f"], ["1", "f"], ["2", "a"], ["1", "e"], ["1", "b"], ["1", "c"]])

count([["0", "a"], ["1", "b"], ["0", "c"], ["1", "d"]])