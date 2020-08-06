# What is Computer Science

- Computer science is fundamentally problem solving
- We can think of problem solving as the process of taking some input, and generate some output.
- We need a way to represent inputs, such that we can store and work with information in a standard way.

## Binary

- A computer, at the lowest level stores data in binary, a numeral system in which there are just two digits, 0 and 1
- When we first learned to cound, we might have used one finger to represent one thing. That system is called unary. When we learned to write numbers with the digits 0 through 9, we learned to use decimal.

To represent 3

```
4 2 1
0 1 1
```

To represent 8

```
8 4 2 1
1 0 0 0
```

- Binary makes sense for computers because we power them with electricity, which can be either on or off, so each bit only needs to be on or off. In a computer, there are millions or billions of switches called transistors that can store electricity and represent a bit by being "on" or "off".

- With enough bits, computers can count to any number

- 8 bits make up one byte

Represent the number 50

```
128 64  32  16  8  4  2  1
 0   0   1   1  0  0  1  0
```

represent the number 13

```
0 0 0 0 1 0 1 1
```

## Representing Data

- To represent letters, all we need to do is decide how numbers map to letters. Some humans, many years ago, collectively decided on a standard mapping called `ASCII`. The letter "A", for example, is the number 65, and "B" is 66, and so on.

- This mapping includes punctuation and other symbols. Other characters, like letters with accent marks, and emoji, are part of a standard called `Unicode` that use more bits than ASCII to accomodate all these characters.

## Algorithms

- Step by step instructions for solving a problem
