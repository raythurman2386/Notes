# https://www.hackerrank.com/challenges/encryption/problem
import math


def encryption(s):
    c = math.ceil(math.sqrt(len(s)))
    return ' '.join(map(lambda x: s[x::c], range(c)))

# def encryption(str):
#     rows_arr = []
#     string = str
#     string_length = len(string)
#     rows = math.floor(math.sqrt(string_length))
#     cols = math.ceil(math.sqrt(string_length))
#     print(string_length, ': string length,',rows, ': rows,', cols, ': cols')

#     while string_length > 0:
#         row = []
#         for letter in range(0, cols):
#             row.append(string[letter])
#             print(row)
#             string = string.strip(string[letter])
#             print(string)
#         rows_arr.append(row)

#     print(rows_arr)

    # create an array to hold the 'rows'
    # loop over string to create the array for each row
    # push row into the array
    # join each internal array
    # add a space between each array
    # return the complete joined string with proper spacing


print(encryption("haveaniceday"))
# expected output == 'hae and via ecy'
