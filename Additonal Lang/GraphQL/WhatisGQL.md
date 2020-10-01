# What is GraphQL

GraphQL is a lnguage for querying databases from client-side applications. On the backend, GQL specifies to the API how to present the data to the client. GraphQL redefines developers' work with APIs offering more flexibility and spped to market; it improves client-server interactions by enabling the former to make precise data requests and obtain no more and no less, but exactly what is needed.

Initially created by Facebook in 2012, GraphQL was used internally for their mobile applications to reduce network usage by means of its specific data fetching capabilities.

## Core Concepts

### The Schema Definition Language

```
type Person {
name: String!
age: Int!
posts: [Post!]!
}

type Post {
title: String!
author: Person!
}
```

#### Basic Queries

```
{
  allPersons {
    name
    age
    posts {
      title
    }
  }
}
```

With args

```
{
  allPersons(last: 2) {
    name
  }
}
```

### Writing data with Mutations

```
mutation {
  createPerson(name: "Bob", age: 36) {
    name
    age
  }
}
```

### Realtime updates with Subscriptions

Another important requirement for many applications today is to have a realtime connection to the server in order to get immediately informed about important events. For this use case, GraphQL offers the concept of subscriptions.

When a client subscribes to an event it will initiate and hold a steady connection to the server. When that event then occurs, the server pushes the corresponding data to the client. Unlike queries and mutations htat follow a typical "request-response-cycle" subs represent a stream of data.

```
subscription {
  newPerson {
    name
    age
  }
}
```

### Defining a Schema

Generally a schema is simply a collection of GraphQL types, However when writing the schema for an API, there a special root types

```
type Query { ... }
type Mutation { ... }
type Subscription { ... }
```

```
type Query {
  allPersons(last: Int): [Person!]!
}

type Mutation {
  createPerson(name: String!, age: Int!): Person!
}

type Subscription {
  newPerson: Person!
}

type Person {
  name: String!
  age: Int!
  posts: [Post!]!
}

type Post {
  title: String!
  author: Person!
}
```
