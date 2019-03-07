High Order Functions

Abstraction
Abstractions hide details and give us the ability to talk about problems at a higher level.

    repeat()
    sum()
    range()
    forEach()
    map()
    filter()
    reduce()
    some()

Functions that operate on other functions, either by taking them as args or by returning them, are called higher-order-functions.

Higher order functions allow us to abstract over actions, not just values.

repeat() acts similar to a for loop, it describes the kind of loop then provides a body, but the body will be written as a function value.

sum() adds two numbers like expected.

range() will work with a range of numbers, and can do things such as sum(range(1,10));

some() takes a test function and tells you whether that function returns true for any of the elements in the array.

Standard Array Methods

    forEach() is a built in Array method that provides something similar to a for/of loop for arrays.

    map() transforms an array by applying a function to all of its elements and building a new array from the returned values. The new array will have the same length as the input array, but its content will have been mapped to a new form by the function.
        function map(array, transform){
            let mapped = [];
            for(let element of array){
                mapped.push(transform(element));
            }
            return mapped;
        }

    filter() rather than deleting elements from the existing array, builds up a new array with only the elements that pass the test that is givin.
        function filter(array, test){
            let passed = [];
            for(let element of array){
                if(test(element)){
                    passed.push(element);
                }
            }
            return passed;
        }

    reduce() builds a value by repeatedly taking a single element from the array and combining it with the current value. When summing numbers, you'd start with the number zero and, for each element, add that to the sum.
        function reduce(array, combine, start){
            let current = start;
            for(let element of array){
                current = combine(current, element);
            }
            return current;
        }
        console.log([1,2,3,4].reduce((a,b) => a+b));
    the parameters for reduce include, the array, a combining function and a start value. If your array contains at least one value, the start argument can be left off.

Arrays provide a number of useful high order methods. You can use forEach to loop over the elements in an array. The filter method returns a new array containing only the elements that pass the predicate function. Transforming an array by putting each element through a function is done with map. You can use reduce to combing all the elements in an array into a single value. The some method tests whether any element matches a given predicate function. And findIndex finds the position of the first element that matches a predicate.
