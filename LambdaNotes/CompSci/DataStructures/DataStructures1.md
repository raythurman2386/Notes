# Data Structures 1
> Learn to define what runtime complexity is, differentiate between various classifications and categorize the performance of an algorithm using Big O notation.

## What is an algorithm

An algorithm is a set of instructions for accomplishing a task. Because of this broad definition, we could call every piece of code an algorithm.

### How do we measure how "good" an algorithm is

After coming up with a first pass solution to a problem, we need to measure how "good" our solution is. Will it stand up to the test of millions of users? Is it fast enough that our users will be blown away by how quickly they get their results? Or will torturously slow speeds cause lag that drives them all away?

> _Note: It is common for your first solution to work with a few items or users, but break as you add more. Making sure solutions scale is something that all developers must remain vigilant about._

## What is Big O Notation

We need a way to talk about efficiency (number of operations in the worst case) in a more general sense.

Big O notation is a way of describing the rate of change in the execution speed of an algorithm when the data size increases. It is teh agreed-upon terminology we use to describe how long an algorithm takes to run. It is a way of comparing different algorithm's efficiencies.

The specific terms of Big O notation describe how fast the runtime grows (relative to the size of the input) with a focus on when the input gets extremely large.

Why do we focus on the growth of runtime versus exact runtime? The exact runtime is dependent on the specific computer that is running the algorithm, so we cannot compare efficiencies that way. By focusing on the general growth, we can avoid the differences in exact runtime between machines and environments.

We also talk about runtime relative to the input size because we need to express our speed in terms of something. So we show the speed of the algorithm in terms of the input size. That way, we can see how the speed reacts as the input size grows.

We don't care about speed when the input size is small. The differences in speed are likely to be minimal when the input is small. When the input gets enormous, that is where we can see teh differences in efficiency between different algorithms.

### Common Big O run times

|    Classification       |    What it means    |   Examples       |
| ----------------------- | ------------------- | ---------------- |
|                         | Runtime space used  | def foo(inp)     |
| Constant O(1)           | is unaffected by the|    x = 5         |
|         Ideal           | size of the input   |                  |
| ----------------------- | ------------------- | ---------------- |
|                         | As input grows the  | def foo(i)       |
| Logarithmic O(log n)    | runtime will grow at|   x = len(i)     |
|      Pretty Good        | slight slower pace  |   while i>0:     |
| ----------------------- | ------------------- | ---------------- |
|                         | As size grows, the  | def foo(inp)     |
| Linear O(n)             | runtime will grow   |    for i in inp: |
|      Acceptable         | at the same rate    |       print(i)   |
| ----------------------- | ------------------- | ---------------- |
|                         | As input grows, the |                  |
| Linearithmic O(n log n) | space used will grow|   mergesort      |
|    Usable/Not Ideal     | slightly faster rate|                  |
| ----------------------- | ------------------- | ---------------- |
|                         | As input grows, the |                  |
| Polynomial O(n^c)       | space used will grow|    2 for loops   |
|    No Way Scalable      | at a faster rate    |                  |
| ----------------------- | ------------------- | ---------------- |
|                         | As input grows, the |                  |
| Exponential O(c^n)      | space used will grow|                  |
|   Pretty Inefficient    | much faster rate    |                  |
| ----------------------- | ------------------- | ---------------- |
|                         | As input grows, the |                  |
| Factorial O(n!)         | space used will grow|                  |
|     EXTREMELY SLOW      | astronomically      |                  |

Again `n` represents teh size of the data, and on the chart above, N represents the number of operations. This visualization should help illustrate why `O(1)` or `O(log n)` is the most desirable.

> _Note: Big O only matters for large data sets. An `O(n^3)` solution is adequate, as long as you can guarantee that your datasets will always be small._

#### A few examples

- Constant Time `O(1)`

```
def print_one(items):
    print(items[0])
```

Why is this constant? Because no matter how large or small the input is, the number of computations within the function is the same.

- Linear Time `O(n)`

```
def print_all(items):
    for item in items:
        print(item)
```

Why is this classified as linear time? Because of the speed of the algorithms increases at the same rate as the input size. If `items` has tem items, then the function will print ten times. If it has 10,000 items, then the function will print 10,000 times.

- Quadratic Time `O(n^2)`

```
def print_pairs(items):
    for item_one in items:
        for item_two in items:
            print(item_one, item_two)
```

Why is this quadratic time? The clue is the nested for loops. These nested for loops mean that for each item in items (the outer loop), we iterate through every item in items(inner loop). For an input size of `n`, we have to print `n*n` times or `n^2` times.


### What about constants?

```
def do_a_bunch_of_stuff(items):
    last_idx = len(items) - 1
    print(items[last_idx])

    middle_idx = len(items) / 2
    idx = 0
    while idx < middle_idx:
        print(items[idx])
        idx = idx + 1

    for num in range(2000):
        print(num)
```

`print(items[last_idx])` is constant time because it doesn't change as the input changes. So, that portion of the function is `O(1)`.

The while loop that prints up to the middle index is 1/2 of whatever the input size is; we can say that portion of the function is `O(n/2)`.

The final portion will run 2000 times, no matter the size of the input.

So putting it all together, we could say that the efficiency is `O(1 + n/2 + 2000)`.
However, we don't say this. We just describe this function as having linear time `O(n)` because we drop all of the constants. Why do we cut all of the constants? Because as the input size gets huge, adding 2000 or dividing by 2 has minimal effect on the performance of the algorithm.

### Most Significant Term

```
def do_different_things(items):
    for item in items:
        print(item)

    for item_one in items:
        for item_two in items:
            print(item_one, item_two)
```

We could describe this function as `O(n + n^2)`; however, we only need to keep the essential term, which is `n^2`, so this would be `O(n^2)`. Why can we do this? Because as the input size gets larger and larger, the sell significant terms have less of an effect, and only the most significant term is important

### Big O represents the worst case

```
def search_for_thing(items, thing):
    for item in items:
        if item == thing:
            return True

    return False

```

What would the result be if it just so happens that the thing we are looking for in items is the very first item in the list? The function would only have to look at one item in items before returning. In this case, it would be `constant` time. But, when we are talking about the complexity of a function, we usually assume the worst case. What would the worst case be? It would be if it were the last item in items. In that case we would have to look through all the items, and that complexity would be `linear`.


### Do constants ever matter?

Complexity analysis with Big O notation is a valuable tool, and you should get in the habit of thinking about the efficiency of the algorithms you write and use in your code. However, just because two algorithms have the same Big O notation doesn't mean they are equal.

Imagine you have a script that takes 1 hour to run. By improving the function, you can divide that runtime by six, and now it only takes 10 minutes to run. With Big O notation, O(n) and O(n/6) can both be written as O(n), but that doesn’t mean it isn’t worth optimizing the script to save 50 minutes every time the script runs.

That being said, there is a term you should become familiar with: `premature optimization (xkcd: Optimization)`. Sometimes, you can sacrifice readability or spend too much time on something to improve its efficiency. Depending on the situation, it could be that having a finished product to iterate on is more important than maximally efficient code. It is your job as a developer to know when spending time making your code more efficient is necessary. You will always be making calculated tradeoffs between runtime, memory, development time, readability, and maintainability. It takes time to develop the wisdom to strike the right balance depending on the scenario.

```
def foo(n):
    i = 1
    while i < n:
        print(i)
        i *= 2
```

We can use the process of elimination to narrow down which runtime classification makes sense for this algorithm. The number of times the loop runs seems to vary based on the value of n, so this is NOT O(1).

We can also see from the above examples that the number of times the loop runs is increasing slower than the size of the input is increasing. n must be doubled before the loop will run one more time. We can eliminate classifications such as O(n log n), O(n^c), O(c^n), and O(n!).

The only two options left at this point are logarithmic and linear. Since the two rates of growth (input, the number of operations) are not the same, this function must run in logarithmic time!