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

  Now lets make another function that we can use to return yet another promise. this is where some of the `then chaining` starts to really come in handy. We're going to have to refactor our code, only where we're calling `time machine`

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

# HTTP

  HTTP is a `network protocol`, a set of rules that govern the way web clients, like a browser, communicate with web servers over the internet.

  Developers need to know what HTTP Methods are and how they are used to perform CRUD `(Create, Read, Update, Delete)` operations on server resources and what HTTP status codes are and what they are used for

  `HTTP Methods` provide a common language, or nomenclature that the client can use to let the server know what operation it wants to perform.

  When a client needs to ask a server for info it should do a `GET` request specifying a URL that points to the resource.

  A `POST` request is used to ask the server to add or create new resources.

  The method used by the client to ask the server to make changes to a specific resource is `PUT`

  To remove or delete data from the server the client should send a `DELETE` request.

  `HTTP Status Codes` are used to indicate if a request has been successful or not and why.

# Axios

  `axios` is a javascript library used to send HTTP requests to servers. It is not necessary to do this, but it makes things much easier. All server requests are asynchronous, `axios` uses Promises. Once you get the basic pattern down `axios` is incredibly easy to use.

  This needs added into the head of the HTML document to use axios

  `<script src="https://unpkg.com/axios/dist/axios.min.js"></script>`

    axios.get(url)

  axios.get will return a Promis to us. This tells us that it is busy getting the data and will return in a moment. As with all promises, we will use `.then` and `.catch` to deal with the data.

    axios.get('http://serverlocation.com/data')
      .then( response => {
        // deal with the response data in here
      })
      .catch( err => {
        // deal with the error in here
      })

  Lets see it all in action

  First we will build our component creator function

    function buttonCreator(buttonTitle){
      let newButton = document.createElement('button');
      newButton.textContent - buttonTitle;
      newButton.classList.add('button');

      return newButton;
    }

    axios.get('http://fakeserver.com/data')
      .then( response => {
        // remember response is an object, response.data is an array
        response.data.forEach( item => {
          let button = buttonCreator(item);
          parend.appendChild(button);
        })
      })
      .catch(error => {
        console.leg("Error: ", err);
      })
