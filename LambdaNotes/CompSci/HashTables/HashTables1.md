# Hash Tables

Hash tables are arguably the single most important data structure known to developers. Used to implement everything from objects in JavaScript and dictionaries in Python to Memcached over a distributed computer network, hash tables are beloved by programmers for providing key/value storage with constant big-O time complexity for insertion, deletion and search.

## Implement a hashing function

Imagine you are a designer, and you want a quick way of remembering all the hex codes for your favorite colors. If you had the colors (like "aqua", "beige", and "chartreuse") in an unsorted collection, you would have to start from the beginning and look through each item whenever you needed to look up a color. This searching process would take linear time (0(n)). If you had the colors sorted alphabetically, you could do a binary search, and that would take logarithmic time (0(log n)).

The binary search method is pretty fast, but what if there was a way to do the same search in constant time

In python a list of your colors would look like this:

```
[("aqua", "#00FFFF"), ("beige", "#F5F5DC"), ("chartreus", "#7FFF00")]
```

as we said earlier, if this list of tuples was sorted alphabetically by the color name, we could use binary search to get the hex color value of a color in logarithmic time (o(log n)).

### Hash Functions

A hash function is a function where the input is any data, and the output is a number

So in our case we would want a hash function where I could input "aqua" and receive a number like 4 as the output.

The requirements for a hash function are:

- A hash function must be consistent. Every time it receives the same input, it must return the same output. If it's not deterministic, it is not a hash function
- Different input data should return different numbers. For example, if the input "aqua" returns 4, then the input "beige" should not return 4.
- A hash function must return numbers that are within a specific range.

When you combine a hash function with an array, you get a data structure called a hash table. In python, hash tables are called dictionaries

### A Naive Hashing Function

```
bytes_representation = "hello".encode()

for byte in bytes_representation:
    print(byte)
```

```
def my_hashing_func(str):
    bytes_representation = str.encode()

    sum = 0
    for byte in bytes_representation:
        sum += byte

    return sum
```

This hashing function still has a limmitaion. We need our hashing function to return integers within a specific range. Remember the purpose of our hashing function is to map our input data to an index value on a list.

Constant time does not mean that it happens instantaneously. It still takes time to run the computations, of course. Constant time means that the computation takes the same amount of time regardless of the size of the hash table. If your hash table has one element, it takes the same amount of time to search for an item as it would if your hash table had one trillion elements. The same is true for insertions and deletions.
