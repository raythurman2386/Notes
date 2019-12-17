# Introduction to Relational Databases

<a href="https://www.w3resource.com/sql/tutorials.php">W3 Resource SQL Tutorial</a>

## Explain what a Relational Database is

> A database is a collection of data organized for easy retrieval and manipulation.

Digital databases have been around since the 1960's. Relational databases, those which store "related" data, are the oldest and most common type of database in use today.

### Data Persistence

A database is often necessary because our application or code requires `data persistence`. This term refers to data that is infrequently accessed and not likely to be modified.

A familiar example of non-persistent data would be JS objects and arrays, which reset each time the code runs

### Relational Databases

A collection of `rows` is called a table. Each row represents a single record in the table and is made up of one or more `columns`.

- Tables
  - Tables organize data in rows and columns.
  - Each row on a table represents one distinct record
  - Each column represents a field or attribute that is common to all records
  - Fields should have a descriptive name and a data type appropriate for the data
  - Tables usually have more rows than columns
  - Tables have primary keys that uniquely identify each row
  - Foreign keys represent the relationships with other tables.

## Explain SQL and it's advantages

SQL is a standard language, which means that it almost certainly be supported, no matter how your database is managed. That said, be aware the SQL language can vary depending on database management tools.

As a query language, SQL is optimized for the sole purpose of querying data.

The syntax for SQL is English-like and requires fewer symbols than programming languages like C, Java, and JavaScript.

- Data Definition Language (DDL) Used to modify database objects. EX: `CREATE TABLE`, `ALTER TABLE`, `DROP TABLE`

- Data Manipulation Language (DML) Used to manipulate stored data. EX: `INSERT`, `UPDATE`, `DELETE`

- Data Query Language (DQL) Used to ask questions about the data stored EX: `SELECT`

- Data Control Language (DCL) Used to manage database security EX: `GRANT`, `REVOKE`

- Transaction Control Commands Used for managing groups of statement that must execute as a unit or not at all `COMMIT`, `ROLLBACK`

## Learn to Query, Insert, and Modify data in SQL

Four critical SQL commands are SELECT, INSERT, UPDATE, and DELETE. This command allow for basic querying, inserting, and modifying of data. They are also necessary for performing CRUD operations on the database level

#### The basic syntax for a SELECT statement:

    select <selection> from <table name>;

#### To see all the fields on a table we can use a \* as the selection

    select * from employees;

#### To pick fields we want to see, we list them separated by commas

    select first_name, last_name, salary from employees;

The return of that statement would show all the records from the listed fields.

We can extend the capabilities of the SELECT command using `clauses` for things like filtering, sorting, pagination, and more

#### To insert new data into a table, we'll use the `INSERT` command.

    insert into <table name> (<selection>) values (<values>)

#### Using this formula we can specify which values will be inserted into which fields

    insert into Customers (Country, CustomerName, ContactName, Address, City, PostalCode) values ('USA', 'Lambda School`, `Austen Allred`, `1 Lambda Court`, `Provo`, `84601`);

#### Modifying a database consists of updating and removing records.

    update <table name> set <field> = <value> where <condition>;

    delete from <table name> where <condition>;

### Filtering results using WHERE clause

When querying a database, by default, the result will be every entry in the given table. However, often, we are looking for a specific record or a set of records that meets certain criteria

    select City, CustomerName, ContactName
    from Customers
    where City = `Berlin`

We can also chain together where clauses usion OR and AND to limit our results further.

    select City, CustomerName, ContactName
    from Customers
    where Country = 'France' and City = 'Paris'

and this one includes records that match either criteria

    select City, CustomerName, ContactName
    from Customers
    where Country = 'France' or City = 'Paris'

To select a single record, we can use a WHERE statement with a uniquely identifying field

    select * from Customers
    where CustomerId=3;

Other comparison operators also work in WHERE conditions

    select * from employees where salary >= 50000

### Ordering results using the ORDER BY clause

Query results are shown in the same order the data was inserted. To control how the data is sorted, we can use the `ORDER BY` clause

    select * from employees order by salary desc, last_name

We can pass a list of field names to `order by` and optionally choose `asc` or `desc` for the sort direction.

The default sort direction is ascending.

Some SQL engines also support using field abbreviations when sorting

    select name, salary, department from employees order by 3, 2 desc;

In this case, the results are sorted by department in ascending order first and then by salary in desc order.

The numbers refer to the position of the fields in the selection portion of the query, so 1 would be `name`, 2 `salary`, and so on

NOTE: `where` clause should come after the `from clause`. The `order by` always goes last

    select * from employees where salary > 50000 order by last_name

### Limiting results using the LIMIT clause

When we wish to see only a limited number of records, we use a `LIMIT` clause

    select * from products
    limit 10

`Limit` clauses are often used in conjunction with `ORDER BY`

    select * from products
    order by price desc
    limit 5

### Inserting data with INSERT

An insert statement adds a new record in the database.

    insert into Customers (Country, CustomerName, ContactName, Address, City, PostalCode) values ('USA', 'Lambda School', 'Austen Allred', '1 Lambda Court', 'Provo', '84601')

The id's and timestamps may be auto generated and do not need to be included.

### Modifying data with UPDATE

When modifying a record, we identify a single record or a set of records to update using a `WHERE` clause

    update Customers
    set City = 'Silicon Valley', Country = 'USA'
    where CustomerName = 'Lambda School';

Technically the `where` clause is not required but leaving it off would result in every table receiving the update.

When removing records, we need only identify which records to remove

    delete from Customers
    where CustomerName = 'Lambda School';

Once again, the WHERE clause is not required, but leaving it off would remove every record in the table, so it’s very important.

## Learn to write queries using knex.js

While raw SQL is a critical baseline skill, Node developers generally use an ORM or query builder to write database commands in a backend codebase. Both ORMs and query builders are JS libraries that allow us to interface with the database using a JS version of the SQL language

    select * from users;

Becomes

    db.select('*').from('users');

Query builders are lightweight and easy to get off the ground, whereas ORMs use an object-oriented model and can provide more heavy lifting within their rigid structure.

Within this sprint we will use a query builder called <a href='https://knexjs.org/'>knex.js</a>

### Knex Setup

To use Knex in a repo, we'll need to add two libraries

    npm i knex sqlite3

    const knex = require('knex');

    const config = {
      client: 'sqlite3',
      connection: {
        filename: './data/posts.db3
      },
      useNullAsDefault: true
    };

    module.exports = knex(config);

To use the query builder elsewhere in our code, we need to call knex and pass in a config object. We'll be discussing knex config more in a future module, but for now all we need the `client`, `connection`, and `useNullAsDefault`.

GOTCHA The file path to the database should be with respect to the root of the repo, not the config file itself.

Once Knex is configured we can import the above config file anywhere in our code to access the database

    const db = require("../data/db-config.js");

### SELECT using Knex

    db.select('*').from('users');

OR

    db('users');

Using this we could write a GET endpoint

    router.get('/api/users', (req, res) => {
      db('users')
      .then(users => {
        res.json(users);
      })
      .catch (err => {
        res.status(500).json({ message: 'Failed to get users' });
      });
    });

NOTE: All Knex queries return promises

Knex also allows the use of a where clause

    db('users').where({ id: 1 });

This method will resolve to an array containing a single entry like so:

    [{ id: 1, name: 'Bill' }]

Using this we could write a get point for a specific user

    server.get('api/users/:id', (req, res) => {
      const { id } = req.params;

      db('users').where({ id })
      .then(users => {
        // we must check the length to find our if our user exists
        if (users.length) {
          res.json(users);
        } else {
          res.status(404).json({ message: 'Could not find user with given id.' })
      })
      .catch (err => {
        res.status(500).json({ message: 'Failed to get user' });
      });
    });

### INSERT using Knex

In Knex, the equivalent of INSERT INTO users (name, age) VALUES ('Eva', 32) is:

    db('users').insert({ name: 'Eva', age: 32 });

The insert method in Knex will resolve to an array containing the newly created id for that user like so:

    [3]

### UPDATE using Knex

In knex, the equivalent of UPDATE users SET name='Ava', age=33 WHERE id=3; is:

    db('users').where({ id: 3 })
    .update({name: 'Ava', age: 33 });

Note that the where method comes before update, unlike in SQL.

Update will resolve to a count of rows updated.

### DELETE using Knex

In Knex, the equivalent of DELETE FROM users WHERE age=33; is:

    db('users').where({ age: 33}).del();

Once again, the where must come before the del. This method will resolve to a count of records removed.
