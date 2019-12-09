# Express Middleware

Express is a minimalist framework. It doesn't provide everything out of the box, but using middleware we can add extra functionality to our application.

Middleware provide a way to extend the features provided by the Express Framework.

## **_ Explain what middleware is and different types _**

We can use Express Middleware to add features to Express. It is the biggest part of Express, most of the code we write, including route handlers, is middleware under the hood.

We can think of middleware as array of functions that get executed in the order they are introduced into the server code.

Express middleware is compatible with `connect middleware`. Connect is a web application framework for Node.js that only provides the middleware layer.

Since `Connect` has been around for longer, it has a rich ecosystem of modules and we can take advantage of that.

<strong>Built-in middleware</strong> is included with Express, but not added to the app automatically. Like the other types, we need to opt-in to using it in our app.

We saw an example of built in middleware when we added support for parsing JSON content

      server.use(express.json());

<strong>Third-party middleware</strong> are npm modules that we can install then import into our app using `require()`

some popular middleware modules are:

- <a href="https://www.npmjs.com/package/morgan">morgan</a>
- <a href="https://www.npmjs.com/package/cors">cors</a>
- <a href="https://www.npmjs.com/package/helmet">helmet</a>

<strong>Custom middleware</strong> are functions we write to perform certain tasks. We'll learn more about how to write them in the next section

    server.use((req, res) => {
      res.status(404).send("Ain't nobody got time for that!");
    })

Using this catch all as if it were middleware requires <strong>adding this status after each route handler</strong>, so that if the preceding middleware or route handlers do not respond to the request, then this will become our catch-all

#### Dig Deeper

- <a href="https://www.npmjs.com/package/cors">Cors middleware</a>
- <a href="https://www.npmjs.com/package/helmet">Helmet middleware</a>
- <a href="https://www.npmjs.com/package/morgan">Morgan Middleware</a>

## **_ Learn to write custom middleware _**

Writing `custom middleware` is a two-step process:

Writ a function that will receive three or four arguments. Add it to the `middleware queue`.

Lets write middleware that logs information about every request that comes into our server.

      const logger = (req, res, next) => {
        console.log(
          `[${new Date().toISOString()}] ${req.method} to ${req.usrl} from ${req.get('Origin')}`
        );

        next();
      }

      server.use(logger);

We can see that a middleware function takes three parameters, the request and response objects, and a third parameter that is a `function that points to the next middleware` in the queue.

Any middleware in the queue can modify both the req, and res objects but it's not required.

Calling `next()` signals to Express that the middleware has finished, and it should call the next middleware function.

Make sure to always call `next()` or use one of the methods that send a response back like `res.send()` or `res.json()`

## **_ Learn to Write error handling middleware _**

<a href="https://nemethgergely.com/error-handling-express-async-await/">Error handling middleware</a>

When our app encounters an error in the middle of executing middleware, we can choose to hand over control to error handling middleware by calling `next()` with one arg.

This type of middleware takes four args: error, req, res, and next.

We pass the first arg when calling `next(new Error('Error message here'))

Error handling middleware can be placed anywhere in the stack, but it makes the most sense to place it at the end. If the intention is for middleware to handle errors that may occur elsewhere in the queue the it needs to run after the rest of middleware has run.

      server.get('/download', (req, res, next) => {
        const filePath = path.join(__dirname, 'index.html');
        res.sendFile(filePath, err => {
          if(err) {
            next(err);
          } else {
            console.log('File sent successfully');
          }
        })
      })

No let's add error-handling middleware to the server

      server.use((err, req, res, next) => {
        console.log(err);

        res
          .status(500)
          .json({ message: 'There was an error'});
      })

This middleware will only get called if any other middleware or route handler that comes before it has called next() with an argument like the /download endpoint above

// Completed Code should look like

    const express = require('express');
    const path = require('path');

    const server = express();

    server.get('/download', (req, res, next) => {
      const filePath = path.join(__dirname, 'index.html');
      res.sendFile(filePath, err => {
        // if there is an error the callback function will get an error as it's first argument
        if (err) {
          // we could handle the error here or pass it down to error-handling middleware like so:
          next(err); // call the next error-handling middleware in the queue
        } else {
          console.log('File sent successfully');
        }
      });
    });

    server.use((err, req, res, next) => {
      console.error(err);

      res
        .status(500)
        .json({ message: 'There was an error performing the required operation' });
    });

    server.listen(5000);
