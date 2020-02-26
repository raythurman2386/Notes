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

```print('Hello World!')```

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