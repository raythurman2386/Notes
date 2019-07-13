# Asynchronous code
  Asynchronous `(async)` code is what makes it possible for a Javasript engine to do 2 things at the same time.
  We can use async code to allow the browser to keep executing code while something else is happening - usually a call to an external API for data
  When we use this technique, we create a helper object, called a `Promise`, to inform the browser that the second, async task has finished.

    setTimeout( () => {
      console.log('Hello!');
    }, 1000);

    console.log('Over Here!');

  Even if you have never seen setTimeout before, you probably realized that it will wait a moment to run.

  Async code is everywhere in JS and an important concept to begin to understand

# Promises
  A Promise is a proxy for a value not necessarily known when the promise is created. It allows you to associate handlers with an asynchronous action's eventual success or failure. This lets asynchronous methods return values like synchronous methods: instead of immediately returning the final value, the async method returns a promise to supply the value at some point in the future.

  A Promise is simply an object with a few properties

  When we want to run some async code, we create a new Promise, and use that Promise to inform the Javascript engine that the async function has finished.

  When we instantiate a new Promise with the `new` keyword, we pass in a callback function that receives a `resolve` function and a `reject` function.

  If the async function finishes and was successful, we call the `resolve()` function. If it was unsuccessful, we call the `reject()` function.

  When a Promise is resolved or rejected we use the Promise object's methods `.then()` or `.catch()` to tell the Javascript engine what to do next.

# .then() & .catch()
  `.then()` and `.catch` are both methods on the Promise object that receive a callback function as an argument

  When our async function finishes running, that callback function is executed.

    let time = 0;
    const timeMachine = () => {
      return new Promise((resolve, reject) => {
        setTimeout(() => {
          resolve((time += 1000));
        }, 1000);
      });
    }

  Notice that we have wrapped our `setTimeout` function in a `new Promise` and we're resolving the addition of the `time += 1000` and passing that resolved result. This allows us to do what we call `promise chaining` when we invoke our `timeMachine` function

    timeMachine()
      .then(newTime => {
        console.log(newTime);
      })

    timeMachine()
      .then(newTime => {
        const myTime = newTime / 1000;
        return `${myTime} seconds have passed`;
      })
      .then(newString => {
        console.log(newString);
      })

  Now lets make another function that we can use to return yet another promise. this is where some of the `then chaining` starts to really come in hady. We're going to have to refactor our code, only where we're calling `time machine`

    const parseTime = ms => {
      return new Promise((resolve, reject) => {
        const timeString = time / 1000;
        resolve(`{timeString} seconds have passed`);
      });
    }

  Now we have offloaded some of our `then` block into a function that resolves a promise. We can now use it like above, but this time, when we call our `timeMachine` function we'll pass this `parseTime` function as and argument to our first `then` block

    timeMachine()
      .then(parseTime)
      .then(timePassed => {
        console.log(timePassed);
      })