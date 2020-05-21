if __name__ == '__main__':
    n = int(input('Please Supply a number: '))

    i = 1
    arr = []
    strArr = []
    results = ""

    while i <= n:
        arr.append(i)
        i += 1

    for num in arr:
       j = str(num)
       strArr.append(j)

    print("".join(strArr))