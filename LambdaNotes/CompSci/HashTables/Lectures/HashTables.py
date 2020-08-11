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
# hash_table = [None] * 8

# Add items to the hash_table using the lecture_hash function
# index = lecture_hash('Hello', len(hash_table))
# hash_table[index] = "Value for Hello"

# index = lecture_hash('World', len(hash_table))
# hash_table[index] = "Value for World"

# print(hash_table[lecture_hash('Hello', len(hash_table))])


# Start of lecture 2

class HashTableEntry:
    """
    Linked List hash table key/value pair
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


hash_table = [None] * 8   # 8 slots, all initiailized to None


def my_hash(s):
    # take every character in the string, and convert character to number
    # Convert each character into UTF-8 numbers
    string_utf = s.encode()

    total = 0
    for char in string_utf:
        total += char
        total &= 0xffffffff  # limit total to 32 bits
    return total


def hash_index(key):
    hash_num = my_hash(key)
    return hash_num % len(hash_table)


def put(key, val):
    # hash the key and get an index
    i = hash_index(key)
    # find the start of the linked list using the index
    # Search through linked list
    # IF the key already exists in the linked list
    # Replace the value
    # Else
    # Add new HashTable Entry to the head of linked list


def get(key):
    # hash the key and get an index
    i = hash_index(key)
    # Get the linked list AT the computed index
    # Search through the linked list for the key
    #   Compare keys until you find the right one
    # If it exists, return the value
    # else, return None


def delete(key):
    # hash the key and get an index
    i = hash_index(key)
    # Search through the linked list for the matching key
    # Delete that node
    # Return value of deleted node (or None)


def resize():
    # Make a new array thats DOUBLE the current size
    # Go through each linked list in the array
    # GO through each item and re-hash it
    # Insert the items into their new locations
    pass


def shrink():
    # Same as resize, but reduce array by HALF
    pass


put("Hello", "Hello Value")
put("World", "World Value")

print(hash_table)

put("foo", "Foo Value")

print(hash_table)

value = get("foo")
print(value)

print(hash_index("Hello"))
print(hash_index("foo"))
