# Server-Side Routing with Express

- <a href="https://www.webdevdrops.com/en/http-primer-for-frontend-developers-f091a2070637/">HTTP Primer</a>

## **_ Explain how routing works in an express application _**

Routing is one of the main features of Express. Using routing we can map incoming requests to the appropriate request handler based on the URL and HTTP Method used.

Routing makes building RESTful Web APIs a breeze. We can have a single URL per resource and execute different code based on the HTTP method used.

Building Web APIs to perform CRUD operations on resources is also very straight forward because there are HTTP methods that map directly to each operation.

### Basic example of routing

    server.get('/about', (req, res) => {
      res.status(200).send('<h1>About Us</h1>')
    })

    server.get('/contact', (req, res) => {
      res.status(200).send('<h1>Contact Us</h1>')
    })

Two things to note:

- We are using the same HTTP Method on both endpoints, but express looks at the URL and executes the corresponding request handler.

- We can return a string with Valid HTTP

Now we will write endpoints that execute different request handlers on the same URL by changing the HTTP method used

#### Dig Deeper

- <a href="https://expressjs.com/en/4x/api.html#res">Express Res Object</a>
- <a href="https://expressjs.com/en/4x/api.html#req">Express Req Object</a>
- <a href="https://expressjs.com/en/guide/routing.html">Express Routing Guide</a>

## **_ Learn to Read data from the query string, req body, and route params _**

Most Web APIs require data from clients. This data can come in different ways

- as route params
- as key/value pairs inside the query string
- as the request body

Let's revisit our DELETE endpoint

    server.delete('/hobbits', (req, res) => {
      res.status(204);
    });

How does the client let the API know which hobbit should be deleted or updated?
One way, through `route parameters`.

We define route params by adding it to the URL with a colon in front of it, Express will add it to the `.params` property part of the req object

    server.delete('/hobbits/:id', (req, res) => {
      const { id } = req.params;

      res.status(200).json({
        url: `/hobbits/&{id}`,
        operation: `DELETE for hobbit with id ${id}`
      })
    })

This route handler will execute every `DELETE` for a URL that begins with `/hobbits/` followed by any value

<strong>
The value for a route param will always be a string, even if the value passed is numeric.
</strong>

### Using the Query String

The query string is another strategy using the URL to pass information from clients to the server.

It is structured as a set of key/value pairs, where each pair takes the form of `key=value`, and pairs are separated by a `&`

Let's add sorting capabilities to our api using the query string.

      server.get('/hobbits', (req, res) => {
        const sortField = req.query.sortby || 'id';
        const hobbits = [
          {
            id: 1,
            name: "Samwise Gamgee"
          },
          {
            id: 2,
            name: "Frodo Baggins",
          }
        ];

        // Apply the sorting
        const response = hobbits.sort(
          (a, b) => (a[sortField] < b[sortField] ? -1 : 1 >)
        );

        res.status(200).json(response);
      });

<strong>Names of query string params are case sensitive!</strong>

### Reading data from the req.body

To read data from the request body, we need to do two things:

- Add the line: `server.use(express.json())`; after the express app has been created.
- Read the data from the body property that Express adds to the req object. Express takes all the information that the client added to the body and makes it available as a nice JS object

## **_ Learn to explain the basics of REST architecture _**

<a href="https://www.ics.uci.edu/~fielding/pubs/dissertation/rest_arch_style.htm">Original REST Documentation</a>

REpresentational State Transfer, or REST is a set of principles, introduced in 1999 by Roy Fielding, that define a way to design distributed software.

When Designing a RESTful API, keep the following principles in mind:

- everything is a resource
- each resource is accessible via a unique URI
- resources can have multiple representations
- communication happens over a stateless protocol (HTTP)
- resource management happens via HTTP Methods

Rest API's have six constraints

- client-server architecture
- stateless architecture: each req should stand on its own
- cacheable: improves network performance

  - GET, PUT, and DELETE should be idempotent(same command executed multiple times)
  - POST is not idempotent
  - Caching is a way to store and retrieve data so that future requests can be fulfilled faster

- Layered system: component A might or might not communicate with component B
- Code on demand

  - API return the resource and code to act on it
  - Client only needs to know how to execute the code
  - Makes API more flexible, upgradable, and extendible
  - Most web apps send JS code along with data

- Uniform interfaces
  - Each resource should be accesible through a single url
  - We should be able to manage the resources through these representations
  - Every interaction with the resource should happen through the URL identifier we gave it
  - Self-descriptive messages
  - HATEOAS (Hyepermedia As The Engine Of Application State)

By applying REST architecture to our API's we can make them scalable and simpler to maintain and extend

## **_ Learn to use Express Routers to organize API code _**

Express Routers are a way to split an application into sub-applications to make it more modular and easier to maintain and reason about

An Express `Router` behaves like a mini Express application. It can have it's own `Routing` and `Middleware`, but it needs to exist inside of an Express application

    // inside /api/apiRoutes.js <- this can be place anywhere and called anything
    const express = require('express');

    // if the other routers are not nested inside /api then the paths would change
    const userRoutes = require('./users/userRoutes');
    const productRoutes = require('./products/productRoutes');
    const clientRoutes = require('./clients/clientRoutes');

    // notice the Uppercase R
    const router = express.Router();

    // this file will only be used when the route begins with "/api"
    // so we can remove that from the URLs, so "/api/users" becomes simply "/users"
    router.use('/users', userRoutes);
    router.use('/products', productRoutes);
    router.use('/clients', clientRoutes);

    // .. and any other endpoint related to the user's resource

    // after the route has been fully configured, then we export it so it can be required where needed
    // standard convention dictates that this is the last line on the file
    module.exports = router;
