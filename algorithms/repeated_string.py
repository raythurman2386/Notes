# HackerRank Repeated String algorithm
def repeated_string(str, n):
    substring = ""
    while len(substring) < n:
        substring += str

    substring = substring[0:n] # Ensure the string is n letters long

    num_a = 0
    for char in substring:
        if char == "a":
            num_a += 1

    return num_a


print(repeated_string("aba", 10))