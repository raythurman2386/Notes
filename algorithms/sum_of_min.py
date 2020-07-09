"""
Add up and print the sum of the all of the minimum elements of each inner array:
[[8, 4], [90, -1, 3], [9, 62], [-7, -1, -56, -6], [201], [76, 18]]

The expected output is given by:
4 + -1 + 9 + -56 + 201 + 18 = 175

You may use whatever programming language you'd like.
Verbalize your thought process as much as possible before writing any code. 
Run through the UPER problem solving framework while going through your thought process.
"""

# loop through each inner array
# Find the minimum number
# add the minimum to an accumulator
# return accumulator(total)


def sum_of_min(arr):
    print(sum([min(i) for i in arr]))
    # accumulator = 0
    # for array in arr:
    #     # find the min of the current array
    #     index = 0
    #     lowest = array[0]
    #     for num in array:
    #         if num < lowest:
    #             lowest = num

    #     accumulator += lowest

    #     # accumulator += min(array)

    # print(accumulator)


sum_of_min([[8, 4], [90, -1, 3], [9, 62], [-7, -1, -56, -6], [201], [76, 18]])
