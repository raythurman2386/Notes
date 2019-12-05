# Server-Side Routing with Express

## Explain how routing works in an express application

Routing is one of the main features of Express. Using routing we can map incoming requests to the appropriate request handler based on the URL and HTTP Method used.

Routing makes building RESTful Web APIs a breeze. We can have a single URL per resource and execute different code based on the HTTP method used.

Building Web APIs to perform CRUD operations on resources is also very straight forward because there are HTTP methods that map directly to each operation.

#### Basic example of routing

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
