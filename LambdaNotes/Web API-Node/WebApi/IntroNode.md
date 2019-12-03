# Introduction to Node and Express

## What is an API

API stands for Application Programming Interface

> An API is server sofware that publishes a set of endpoints that clients can use to manage resources.

An API isn't the same as a remote server, rather <strong>it is the part of the server that receives requests and sends responses.</strong>

To summarize, when a company offers an API to their customers, it just means that they've built a set of dedicated URLs that return pure data responses

Meaning the responses won't contain the kind of presentational overhead that you would expect in a GUI like a website.

## What is Node.js

Node.js is a runtime environment(a program that runs other programs), a platform used to execute JS apps outside of the browser

This opens up a new world of possibilities for JS developers, we can now use JS to write command line utilities, native programs that run on different OS, networking software, web services, web apps and more

Traditionally JS was only used in web browsers, but in 2009 Node.js was unveiled and with it the developer tool kit expanded greatly. Node gave devs the chance to use JS to write software that up to that point, could only be written using C, C++, Java, Python, Ruby, C# and the like.

### Some Advantages of Node

- JS on the server: same language and paradigm for both client and server
- Single Threaded: removes complexity involved in handling multiple threads
- Asynchronous: can take full advantage of the processor it's running on
- Npm repository: access the largest ecosystem of useful libraries in the form of NPM modules

### Disadvantages

- JS on the server, lose the ability to use the right tool for the job
- Single threaded: can't take advantage of servers with multiple cores/processors.
- Asynchronous: it is harder to learn for devs who have only worked with languages that default to synchronous operations that block the execution thread
- NPM repository: too many packages that do the same thing makes it harder to choose one and, in some cases, may introduce vulnerabilities into our code.

To write a simple server with pure Node.js

    const http = require('http');

    const hostname = '127.0.0.1';
    const port = 5000;

    // Creates our server
    const server = http.createServer((req, res) => {
      // http status code returned to client
      res.statusCode = 200;
      // inform client that we'll be returning text
      res.setHeader('Content-Type', 'text/plain');
      // end the request and send a response
      res.end('Hello World from node);
    })

    server.listen(port, hostname, () => {
      console.log(`Server running at http://${hostname}:${port}/`)
    })

## Explain Express and its core features

Express is a web app framework that sits on top of the Node we server. It's like React, for the backend

Node's built in HTTP module provides a powerful way to build web applications and services, but it requires a lot of code for common tasks.

Express is a light and unopinionated framework that sits on top of node and makes it easier to create web apps and services. Sending HTML file or images is now a one line task with the sendFile helper method in Express

### What can we do with Express?

- build web apps
- build RESTful web services with JSON
- serve static content
- power real-time apps using technologies like web sockets or WebRTC

### Main Features of Express

#### Middleware

Middleware functions can get the request and response objects, operate on them and trigger some action

#### Routing

Routing is a way to select which request handler function is executed, it does so based on the URL visiten and the HTTP method used

Lets write our first web server with express

    const express = require('express');

    const server = express();

    server.get('/', (req, res) => {
      res.send('Hello from Express');
    });

    server.listen(5000, () => {
      console.log('Server running on http://localhost:5000')
    });

## Create an API that can respond to GET requests

- The first step is to define a new route handler to respond to GET requestss at the /hobbits endpoint
- Next, we define the return data that our endpoint will send back to the client. We do this inside the newly defined route handler function
- Now we can return the hobbits array. We could use .send(hobbits) like we did for the string on the / endpoint, but this time we'll learn about two other useful methods we find in the res object

We should provide as much useful information as possible to the clients using our API. One such piece of information is the HTTP status code that reflects the outcome of the operation the client is trying to perform.

In this case the client is trying to get a list of a particular resource.

Sending back a 200 OK status code communicates to the client that the operation was successful

The .status() method of the response object can be used to send any valid HTTP status code

We are also chaining the .json() method of the res object to clearly communicate to both the client making the request and to the next dev working with this code, that we intend to send the data in JSON format

      server.get('/hobbits', (req, res) => {
        const hobbits = [
        {
          id: 1,
          name: 'Sam Gamgee',
        },
        {
          id: 2,
          name: 'Frodo'
        }
      ]
        // Route handler code here
        res.status(200).json(hobbits)
      })

# Postman/Insomnia

Testing API's is different from testing websites or web applications. To test the latter, a web browser is sufficient, but for APIs, we need to be able to make POST/PUT/PATCH/DELETE requests and even modify the request headers.

Postman and other tools allow full control when making requests. We can easily change the HTTP Method used, add JSON data to the body, add form data, add headers, examine the response, and more
