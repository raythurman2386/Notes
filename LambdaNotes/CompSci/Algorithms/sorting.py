# Binary search
def binary_search(my_list, search_item):
    low = 0
    high = len(my_list) - 1

    while low <= high:
        middle = (low + high) // 2
        guess = my_list[middle]

        if guess == search_item:
            return middle

        if guess > search_item:
            high = middle - 1
        else:
            low = middle + 1

    return None


test_list = [2, 4, 7, 8, 9, 10, 12, 34, 45]

print('*** Binary Search ***')
print(binary_search(test_list, 7))
print(binary_search(test_list, 34))

# Selection Sort

my_numbers = [5, 9, 3, 6, 2, 1, 7, 8, 4]


def selection_sort(items):
    # Outer Loop
    for i in range(0, len(items) - 1):
        cur_index = i
        smallest_index = cur_index
        for j in range(cur_index + 1, len(items)):
            if items[j] < items[smallest_index]:
                smallest_index = j

        items[smallest_index], items[cur_index] = items[cur_index], items[smallest_index]

    return items


print('\n*** Selection Sort ***')
print(selection_sort(my_numbers))

"""
Write a recursive search function that receives as input an array of integers and a target integer value
This function should return True if the target element exists in the array, and False otherwise.
"""


def recursive_search(arr, target):
    # if the first index is the target return True
    if arr[0] == target:
        return True
    elif len(arr) == 1 and not arr[0] == target:
        return False
    # Otherwise, Splice from the first index on
    else:
        # send the spliced list into the function again with the target
        return recursive_search(arr[1:], target)


print("\n*** Recursive Search ***")
print(recursive_search([1, 2, 3, 4, 5], 4))
print(recursive_search([1, 2, 3, 4, 5], 7))


"""
Write a recursive function that takes in a string and returns the string reversed
"""


def reverse_string(str):
    # If the string is empty, return the base case
    if len(str) == 0:
        return str
    # otherwise, return the recursive call with the string spliced at the first index
    else:
        # add the first index of the string to the end
        return reverse_string(str[1:]) + str[0]


print("\n*** Reversed String ***")
print(reverse_string("Lambda"))
print(reverse_string("Raymond"))


"""
Write a recursive function that checks if a string is a palindrome
"""


def palindrome(str):
    # If the string is 1 or 0 in length return True
    if len(str) <= 1:
        return True
    # Otherwise compare the first and last elements
    if str[0] == str[-1]:
        # If they are the same, strip those characters and run again
        return palindrome(str[1:-1])

    return False


print("\n*** Is Palindrome ***")
print(palindrome("radar"))
print(palindrome("banana"))
