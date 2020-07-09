# Recursive Sorting

## What is Recursion

Recursion is a method to solve problems. It means breaking down a problem into smaller and smaller sub-problems until the sub-problem is easy to solve. Recursive functions call themselves. Often, recursive solutions are terse and elegant. Recursive solutions are not always the most efficient. However, they can be an excellent starting point that you can improve the efficiency of afterward.

In a recursive function you will always want to include a breaking clause as the first option

That eliminates the chance for the function to get stuck in an infinite loop and ending up leading to a stack overflow, as long as the function is working properly

```
def sum_list(items):
    if len(items) == 1:
        return items[0]
    else:
        return items[0] + sum_list(items[1:]) # items[1:] will always have one less item than the previous call
```

This will essentially work through the list of numbers, and as it gets to the final number, will begin returning and adding up the numbers

So basically it works all the way down, THEN all of the else returns will be completed, thus adding up all of the numbers from the returns that have accumulated.

### Three rules of recursion

- Must have a base case (breaking clause)
- Must change it's state to move towards the base case
- Must call itself

## When should you use Recursion

What clues or hints might you find within a problem that could lead you to use recursion

- Compute the nth term
- List the first or last n terms
- Generate all permutations

Another way to think about it is to use the three rules. Is there a clear base case or stopping point that you are working towards?

Is there a clear way that the state of the dat achanges with each iteration that brings it closer to the base case?

```
def recursive_factorial(n):
    if n == 1:
        return 1
    else:
        return n * recursive_factorial(n - 1)
```
