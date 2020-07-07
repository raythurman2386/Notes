# Iterative Sorting

### What is a linear search

Suppose I am thinking of a number between 1 and 1000. The object of the game is for you to guess the nuimber I am thinking of with as few guesses as possible. Every time you make a guess, I will tell you if you're too high, low, or correct.

What strategyt for guessing would you choose?

Linear search would be looking at each number to see if it was the correct number

As you could imagine, that would take awhile

### What is a Binary Search

The best strategy would be to eliminate half of the numbers with each guess. We do that by guessing the middle number each time.

If it is to low or high, that will eliminate half of the numbers.

### Logarithms

This situation where I'm halving the number of possibilities each time, mathematically is considered a logarithm.

Logarithms and exponents are related to eachother in the same way that multiplication and division are related.

They have an inverse relationship.

## Sorting

Sorting is a common thing that we encounter in our everyday lives. When we need to sort something each of us chooses a strategy without even thinking about it.

### Selection Sort

Out of place selection sort

Let's talk about an actual example. Imagine for a moment that you have a shelf of books and you would like your books to be sorted on the shelf alphabetically by the title.

The most natural wayis to scan the books from left to right, looking for the book with the lowest alphabetical title

Once found we will move it to the other side of the bookshelf and look for the next book.

In place selection sort

But what if your bookshelf is too short to do that?

Then you would scan, find the book and place it in the first spot essentially swapping the books places.

### Insertion Sort

Insertion sort is an efficient algorithm for sorting _small amounts_ of data.

Insertion sort runs in `O(n)` time in it's best case(already sorted), and `O(n^2)` in it's worst and average cases.

If the collection is already sorted, the insertion sort algorithm will still have to go through each item in the collection to make sure it is in the correct position.

### Bubble Sort

Bubble sort is one of the simplest sorting algorithms. It is also very inneficient.

Bubble sort can be described in the following terms:

- compare the first and second item of a collection. If the first is bigger, swap the items
- move to the next item, then the thhhird and so on
- do this till the end of the list
- repeat the steps decrementing the 'end of the list' by 1 each time
