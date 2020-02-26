# GraphQL Introduction

<a href="https://www.howtographql.com/basics/0-introduction/">Resource</a>

GraphQL is a new API standard that provides a more efficient, powerful and flexible alternative to REST.

> APIs have become ubiquitous components of software infrastructures. In short, an API defines how a client can load data from a server

At its core, GraphQL enables `declarative data fetching` where a client can specify exactly what data it needs from an API.

Instead of multiple endpoints that return fixed data structures, a GraphQL server only exposes a single endpoint and responds with precisely the data a client asked for.

## GraphQL - A Query Language for APIs

Most applications today have the need to fetch data from a server where that data is stored in a database. It's the responsibility of the API to provide an interface to the stored data that fits an applications needs

GraphQL is often confused with being a database technology. This is a misconception, GraphQL is a query language for API's - not databases

### A more efficient REST alternative

REST has been a popular way to expose data from a server. When the concept of REST was developed, client applications were relatively simple and the development pace wasn't nearly where it is today.

Three factors have been challenging the way APIs are designed:
1. Increased mobile usage creates need for efficient data loading
> Increased mobile usage, low-powered devices and sloppy networks were the initial reasons why Facebook developed GraphQL. It minimizes the amount of data that needs to be transferred over the network and vastly improves applications

2. Variety of different frontend frameworks and platforms
> With GraphQL each client can access the data it needs

3. Fast development & expectation for rapid feature development
> Continuous deployment has become a standard for many companies, rapid iterations and frequent product updates are indispensable. With REST APIs the way data is exposed by the server often needs to be modified to account for specific requirements and design changes on the client side
