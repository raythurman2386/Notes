# Tkit Example
def my_hash_func(str, list_size):
    bytes_rep = str.encode()

    sum = 0
    for byte in bytes_rep:
        sum += byte

    print(sum % list_size)
    return sum % list_size


# my_list = [None] * 8

# my_list[my_hash_func("aqua", len(my_list))] = "#00FFFF"
# print(my_list[my_hash_func("aqua", len(my_list))])
# my_list[my_hash_func("beige", len(my_list))] = "#F5F5DC"
# print(my_list[my_hash_func("beige", len(my_list))])
# my_list[my_hash_func("chartreuse", len(my_list))] = "#7FFF00"
# print(my_list[my_hash_func("chartreuse", len(my_list))])
# my_list[my_hash_func("deepskyblue", len(my_list))] = "#00BFFF"
# print(my_list[my_hash_func("deepskyblue", len(my_list))])
# my_list[my_hash_func("forestgreen", len(my_list))] = "#228B22"
# print(my_list[my_hash_func("forestgreen", len(my_list))])


# print(my_list)

# Lecture Begin
words = ['apple', 'book', 'cat', 'dog', 'egypt', 'france']


def lecture_hash(str, limit):
    # take all chars in str and convert to num
    str_utf = str.encode()
    sum = 0

    for char in str_utf:
        sum += char
        sum &= 0xffffffff  # limit to 32 bits

    return sum % limit


# ** Always try to make your hash table a power of 2 **
hash_table = [None] * 8

# Add items to the hash_table using the lecture_hash function
index = lecture_hash('Hello', len(hash_table))
hash_table[index] = "Value for Hello"

index = lecture_hash('World', len(hash_table))
hash_table[index] = "Value for World"

print(hash_table[lecture_hash('Hello', len(hash_table))])
