"""
Add up and print the sum of the all of the minimum elements of each inner array:
[[8, 4], [90, -1, 3], [9, 62], [-7, -1, -56, -6], [201], [76, 18]]

The expected output is given by:
4 + -1 + 9 + -56 + 201 + 18 = 175

You may use whatever programming language you'd like.
Verbalize your thought process as much as possible before writing any code. 
Run through the UPER problem solving framework while going through your thought process.
"""


def sum_of_min(arr):
    # Final Implementation
    print(sum([min(i) for i in arr]))
    # loop through each inner array
    # Find the minimum number
    # add the minimum to an accumulator
    # return accumulator(total)

    # Initial implementation using min()
    # accumulator = 0
    # for array in arr:
    #     accumulator += min(array)

    # Basic Implementation not using min()
    # find the min of the current array
    # for array in arr:
    #     lowest = array[0]
    #     for num in array:
    #         if num < lowest:
    #             lowest = num
    #     accumulator += lowest

    # This print is for the initial using min and implementation not using min
    # print(accumulator)


# Recursive implementation
def sum_min(arr):
    if len(arr) == 1:
        return min(arr[0])
    else:
        return min(arr[0]) + sum_min(arr[1:])


sum_of_min([[8, 4], [90, -1, 3], [9, 62], [-7, -1, -56, -6], [201], [76, 18]])
print(sum_min([[8, 4], [90, -1, 3], [9, 62],
               [-7, -1, -56, -6], [201], [76, 18]]))
