# Algorithms

## Algorithm Complexity

- Space complexity - How much memory does it require
- Time complexity - How much time does it take to complete

## Common algorithms

- Search algorithms

- Sorting algorithms

- Computational algorithms

- Collection algorithms

## Big-O Notation

- Classifies performance as the input size grows
- O indicates thhe `order of operation:` time scale to perform an operation

### Common Big-O Terms

O(1) - Constant Time - Looking up a single element in an array
O(log n) - Logarithmic - Finding item in sorted array with binary search
O(n) - Linear Time - Searching an unsorted array for specific value
O(n log n) - Log-Linear - Complex sorting algos like heap and merge sort
O(n2) - Quadratic - Simple sorting algos such as bubble, selection, and insertion

## Data Structures

Used to organize data so it can be processed.

- Arrays
  Collection of elements identified by an index or a key
  1 dimensional

  Calculate itme index: O(1)
  Insert or delete: O(n)
  Insert or delete at end: O(1)

- Linked lists
  Collection of data elements called nodes
  Contain reference to the next node in list
  Hold whatever data the app needs

  Benefit:
  Elements easily inserted and removed
  Underlying memory doesnt need to be reorganized
  Can't do constant time random access
  Item lookup is linear in time complexity (O(n))

- Stacks and Queues
  Stack: collection of elements that support push and pop operations
  the last item pushed is the first one popped
  last on first off

  - Expression processing
  - Backtracking: browser back stack for example (back button)

  Queue: collection that supposts adding and removing
  first item added is the first item out

  - Order processing, that way first order that comes through is the first processed
  - Messaging, make sure that each message is sent in the correct order

- Trees
- Hash Tables
  Data structue that matches keys to values, similar to a dict

  - key-to-value mappings are unique
  - hash tables are typically very fast

  - for small datasets, arrays are usually more efficient, or a linked list
  - hash tables don't order entries in a predictable way

## Recursion

Recursion is when a function calls itself

```
def function():
  <!-- do something -->
  function()
```

recursive functions must have a breaking condition,
otherwise you will create an infinite loop and will eventually crash

Each time the function is called, the old arguments are saved

This is called the "call stack"

```
def countdown(x):
  if x == 0:
    print("done!)
  else:
    print(x, "..")
    countdown(x - 1)

countdown(4)
```

## Sorting

### The Bubble Sort

- very simple to understand and implement
- Performance: O(n2)

  - pretty poor performance overall
  - for loops inside of for loops are usually n2 (quadratic)

- Other sorting algorithms are generally much better
- Not considered to be a practical solution

### The Merge Sort

- Divide and conquer algorithm
- Breaks a dataset into individual pieces and merges them
- uses recursion to operate on datasets
- performs well on large datasets
- In general has a performace of O(n log n) time complexity (log linear)

### The Quick Sort

- Divide and conquer just like merge sort
- also uses recursion for sorting
- Generally performs better than merge sort, O(n log n)
- operates in place on the data
- Worst case is O(n2) when data is mostly sorted already

## Searching

- unordered searching can become inneficient
- unordered is considered a linear search

- ordered searching can be done with a binary search
- ordered is much more performant than unordered

- isSorted is a linear search as well
