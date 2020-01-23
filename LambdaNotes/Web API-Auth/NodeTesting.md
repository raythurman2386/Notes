# Node Testing

## Learn to test Web API Endpoints

The tests we write for endpoints are called integration tests because they test how different parts of the system work together.

We'll use a npm module called `supertest` that makes it easier to write tests for Node.js HTTP servers.

We can use `supertest` to load an instance of our server, send requests to the different endpoints, and make assertions about the responses

```
const request = require('supertest`);
const server = require('./server.js');

describe('server.js', () => {
  describe('index route', () => {
    it('should return an OK status code from the index route', async () => {
      const expectedStatusCode = 200;

      const response = await request(server).get('/');

      expect(response.status).toEqual(expectedStatusCode);
    });

    it('should return a JSON object from the index route', async () => {
      const expectedBody = { api: 'running' };

      const response = await request(server).get('/');

      expect(response.body).toEqual(expectedBody);
    });

    it('should return a JSON object from the index route' async () => {
      const response = await request(server).get('/');

      expect(response.type).toEqual('application/json');
    })
  })
})
```

In this code, we consider three questions commonly tested for our endpoints:

- Does it return the correct status code for the input provided
- Does it return the data in the expected format
- Does the data returned, if any, have the right content

When testing your endpoints, start with those three tests and then move on to write tests that are unique for the system you're building.

The payroll endpoints for an accounting system, for example, require different tests than those for an accounts payable module.

There is no one size fit's all when it comes to testing.

```
const express = require('express');

const server = express();

server.get('/', (req, res) => {
  res.status(200).json({ api: 'running' })
})

module.exports = server;
```

Notice we are not starting the server, this is a common pattern, we separate the server implementation from the code that runs the server.

If we start listening for requests in this file, then every time a test runs, it will start a new instance of the API using the specified port and run into an "address (meaning the port number) in use" error.

## Lern to test Data Access Code

To test the data access, we'll write end to end tests. 

These types of tests run slower because they perform operations and run queries against an actual database that is similar to the one used in production.

To avoid polluting the development database, we'll use a separate database for testing. One advantage of using a dedicated testing database is that we can add and remove records without affecting the data in the development or staging databases.

### Using cross-env

Setting and using env variables is different for windows and POSIX Operating Systems. 

We can use `cross-env` an npm module that deals with the OS inconsistencies and provides a uniform way of setting env variables across all platforms.

```
"test": "cross-env DB_ENV=testing jest --watch"
```

```
// ./data/dbConfig.js
const knex = require('knex');

const config = require('../knexfile.js');

// if the environment variable is not set, default to 'development'
// this variable is only set when running the "test" npm script using npm run test
const dbEnv = process.env.DB_ENV || 'development';

// the value of dbEnv will be either 'development' or 'testing'
// we pass it within brackets to select the corresponding configuration
// from knexfile.js
module.exports = knex(config[dbEnv]);

```

### Write End to End Tests that Involve the Database

To test the data access code, execute teh data access and then verify that the database was updated correctly.

```
const db = require('../data/dbConfig.js');

const Hobbits = require('./hobbitsModel.js');

describe('hobbits model', () => {
  describe('insert()', () => {
    it('should insert the provided hobbits into the db', async () => {
      await Hobbits.insert({ name: 'gaffer' });
      await Hobbits.insert({ name: 'sam' });

      const hobbits = await db('hobbits');

      expect(hobbits).toHaveLength(2);
    })
  })
})
```

To make sure that the tables are cleared before running each test, add the following code before the test cases

```
beforeEach(async () => {
  await db('hobbits').truncate();
})
```

Implement code to make the tests pass.

```
async function insert(hobbit) {
  const [id] = await db('hobbits').insert(hobbit, 'id');

  return db('hobbits')
    .where({ id })
    .first();
}
```

This test only checks that there are two records added to the table, even if those records were there at the beginning

Lets add another test to make sure that the record is making it to the database and that the `.insert()` method returns the newly inserted hobbit.

```
it('should insert the provided hobbit into the db', async () => {
  let hobbit = await Hobbits.insert({ name: 'gaffer' });
  expect(hobbit.name).toBe('gaffer');

  hobbit = await Hobbits.insert({ name: 'sam' });
  expect(hobbit.name).toBe('sam');
})
```