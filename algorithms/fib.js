// Initialize an empty array of length n. Use reduce to add values to the array, using the sum of the last two values, except for the first two

const fib = n => (
  [...Array(n)].reduce((acc, val, i) => (
    acc.concat(i > 1 ? acc[i - 2] : i)
  ), [])
)

console.log(fib(50))