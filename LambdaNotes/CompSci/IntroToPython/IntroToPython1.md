# Introduction to Python

<a href="https://github.com/LambdaSchool/CS-Wiki/wiki/Javascript-Python-cheatsheet">Python Cheat Sheet</a>

### What is a Program

A program is a sequence of instructions that specifies how to perform a computation.

The computation could be anything. It could require you to get the length of one side of a triangle, to look for every instance of a certain character or letter and replace it, or to transform a color image into a black and white image

Regardless of the language, every programming language is made up of a few basic instructions

- Input = Receiving data from a keyboard, file, network or another device
- Output = Presenting data on a screen, saving to a file, sending over a network
- Arithmetic and Logic = Add, subtract, multiply, divide
- Conditionals = Running code given certain conditions
- Repetition - Executing repeatedly but with slight modifications

<a href="https://github.com/LambdaSchool/CS-Wiki/wiki/Installing-Python-3-and-pipenv">Install Python</a>

### Python Basics

`print('Hello World!')`

Arithmetic Operators

```
+ addition
- subtraction
* multiplication
/ division
// floor division
** exponentiation
% modulous
```

Variables in Python

```
greeting = "Good Afternoon"
x = 23
pi = 3.1415
```

Python cannot perform mathematical operations on strings, even if the strings look like numbers

Although, you can use the `+` to concatenate strings
And `*` to duplicate a string

### Composition

In programming, when we talk about taking small pieces and building larger functionality we are describing composition.

Almost anywere you can put a value, you can put an expression(which evaluates to a value)

### Creating new functions in Python

```
def print_lyrics():
    print("Oh yeah, I'll tell you something")
    print("I think you'll understand")
    print("Then I'll say that something")
    print("I wanna hold your hand")
```

`def` is a keyword in Python that shows that this is a function definition

The PEP-8 convention is to always indent by 4 spaces in python

### Why functions

There are several reasons to use functions which i'll define below

- By creating a function, you can group similar statements that are part of the same process. this makes code easier to read

- Functions make your program smaller by eliminating repetition in your code

- By grouping statements into functions and reusing the function throughout the program it removes repetitiveness in your application

- A well-designed function can often be useful in other programs

```
for i in range(4):
    print('Hello!')

if x < 0:
    print("x is negative")
else:
    print("x is positive")

if x == y:
    print('x and y are equal')
elif x > y:
    print('x is greater than y')
else:
    print('y is greater than x')
```

### Short circuit evaluation

```
def is_five(n):
    # If n is 0 the and will return immediately
    # avoiding the division by 0 error
    return n != 0 and 5 / n == 1
```

```
def right_justify(s):
    return ((70 - len(s)) * ' ') + s
```

## Lists

Like a string a `list` is a sequence of values.

just like an array in JavaScript

```
[2, 4, 5, 6.2, 7, ['hello', 'world']]
```

to access elements in a list in Python you must use bracket notation

arr[0]

lists, just like arrays are 0 index based.

## Dictionaries

A `dictionary` is like a list but more general. Dictionaries must contain `key/value` pairs and they can containn almost any type

A dictionary is an Object from JavaScript

Unlike JavaScript the only way to access the items on a dictionary is through bracket notation

dict["name"]

```
for key, values in dict:
    print(f`{key}:{value}`)
```

Curly braces represent an empty dictionary, to add items you can use bracket notation as well

person = {}

person["name"] = "Ray"
person["age"] = 30
person["hobbies"] = ["computers", "gym"]

## Tuples

A `Tuple` is a sequence of values. The values can be any type and they are indexed by integers. They are a lot like lists.

> The major important difference is that tuples are immutable while lists are mutable

```
my_tuple = ('f', 'g', 'h')
```

t = tuple('lambda')

## Sets

Python provides another built-in type, called a set, that behaves like a collection of dictionary keys with no values mapped to those keys.
In a set you cannot change items, you can only add items.

Importantly you can also not duplicate items

my_first_set = { 'tree', 'building', 'sky' }

#### Decisions Decisions

When deciding with collection type to use, it’s important to think about your needs for interacting with the data beforehand.

If the order of your data matters, then use a List.

If you want to store an immutable (unchangeable) list of data, then use a Tuple.

If you need to associate values with keys so you can look up data efficiently, then you should use a Dictionary.

If you just need to know if you already have a particular piece of data, order doesn’t matter, and you need not keep duplicates, then use a Set.
