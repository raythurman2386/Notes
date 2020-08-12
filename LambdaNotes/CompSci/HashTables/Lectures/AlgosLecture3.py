# Substitution Ciphers
# Or how to transform data from one thing to another

import math
encode_table = {
    'A': 'H',
    'B': 'Z',
    'C': 'Y',
    'D': 'W',
    'E': 'O',
    'F': 'R',
    'G': 'J',
    'H': 'D',
    'I': 'P',
    'J': 'T',
    'K': 'I',
    'L': 'G',
    'M': 'L',
    'N': 'C',
    'O': 'E',
    'P': 'X',
    'Q': 'K',
    'R': 'U',
    'S': 'N',
    'T': 'F',
    'U': 'A',
    'V': 'M',
    'W': 'B',
    'X': 'Q',
    'Y': 'V',
    'Z': 'S'
}

decode_table = {}

for key, value in encode_table.items():
    decode_table[value] = key


def encode(plain_text):
    cipher = ""

    for char in plain_text:
        if char.isspace():
            cipher += ' '
        else:
            cipher += encode_table[char.upper()]

    return cipher


def decode(cipher_text):
    plain_text = ''
    for char in cipher_text:
        if char.isspace():
            plain_text += ' '
        else:
            plain_text += decode_table[char.upper()]
    return plain_text


cipher = encode("Dictionaries are awesome")
print(cipher)

reversed_plain_text = decode(cipher)
print(reversed_plain_text)

# Records algorithm
records = [
    ("Alice", "Engineering"),
    ("Bob", "Sales"),
    ("Carol", "Sales"),
    ("Sarah", "Sales"),
    ("Pranjal", "Sales"),
    ("Dave", "Engineering"),
    ("Erin", "Engineering"),
    ("Frank", "Engineering"),
    ("Grace", "Marketing"),
    ("Charles", "Marketing"),
    ("Brian", "Marketing"),
    ("Jordan", "Marketing"),
]

# Proposed Dictionary
# Keys will be Departments
# values array of names, or list of names


def build_index(recs):
    index = {}

    for record in recs:
        name, dept = record

        # Check if department is already in index
        if dept in index:
            # if it is, add name to the list
            index[dept].append(name)
        else:
            # else create new key with list with the name in it
            index[dept] = [name]

    return index


department_index = build_index(records)

print(department_index)


# # print all the departments
# print(department_index.keys())
# # print everyone in Engineering:
# print(department_index['Engineering'])
# # print everyone in Sales:
# print(department_index['Sales'])

# # print everyone in Marketing:


# Given a string, can we figure out how many times each letter appears in it?

def letter_count(s):
    # Dict where keys are letters and values will be an incrementing counter
    d = {}
    for char in s:
        if char.isspace():
            continue

        if char not in d:
            d[char] = 1
        else:
            d[char] += 1

    return d


def double_letter(s):
    # store letters as keys and a counter as value
    # Find all letters,(or just the one letter) where value > 1
    # Dict where keys are letters and values will be an incrementing counter
    d = set()
    for char in s:
        if char.isspace():
            continue

        if char not in d:
            d.add(char)
        else:
            return char


print(double_letter("abecdef"))  # should be e

# print(letter_count("aaabbc"))
# print(letter_count("Hello!"))
# print(letter_count("The quick brown fox jumps over the lazy dogs"))


# Inverse square root is 1 / square root of number
# Relatively time consuming

def get_inverse_square(num):
    return 1 / math.sqrt(num)


# We need to constantly get the inverse square roots of numbers between 1 and 1000

# what should our lookup table look like?
# Keys will be numbers
# Values will be results of get_inverse_square


def build_lookup_table():
    lookup_table = {}
    for i in range(1, 1001):
        lookup_table[i] = get_inverse_square(i)
    return lookup_table


sqrt_lookup_table = build_lookup_table()

print(sqrt_lookup_table[3])
print(sqrt_lookup_table[982])
print(sqrt_lookup_table[234])
