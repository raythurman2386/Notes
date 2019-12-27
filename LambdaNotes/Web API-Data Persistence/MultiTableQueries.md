# Multiple-Table Queries

## Explain the role of a foreign key

Foreign keys are a foundational concept in understanding table relationships, designing a multi table schema, and writing join statements.

Foreign keys are a type of table field used for creating links between tables. Like primary keys, they are most often integers that identify data. 

However, whereas a primary key is used to id rows in a table, foreign keys are used to connect a record in one table to a record in a second table

## Learn to query data from multiple tables

Now that we understand the basics of querying data from a single table, let's move on to selecting data from multiple tables using JOIN operations

We can use a `JOIN` to combine query data from multiple tables using a single `SELECT`

There are different types of joins

- inner joins
- outer joins
- left joins
- right joins
- cross joins 
- non-equality joins
- self joins

Using `joins` requires that the two tables of interest contain at least one field with shared information

For example, if a departments table has in id field and an employee table had a department_id field, and the values that exist in the id column of the departments table live in the department_id field of the employee table, we can use those fields to join both tables like so:

    select * from employees
    join departments on employees.department_id = departments.id

This query will return the data from both tables for every instance where the ON condition is true. 

If there are employees with no value for the department id or where the value stored in teh field does not correspond, then that record will NOT be returned.

We can shorten the condition by giving the table names and alias

    select d.id, d.name, e.id, e.first_name, e.last_name, e.salary
    from employees as e
    join departments as d
      on e.department_id = d.id
    order by d.name, e.last_named

And the syntax for using Knex

    db('employees as e')
      .join('departments as d', 'e.department_id', 'd.id')
      .select('d.id', 'd.name', 'e.first_name', 'e.last_name', 'e.salary')

## Learn to write Database access methods

Developers should get in the habit of keeping code modular.

This particular approach will help keep endpoints clean, allow for easier testing, and generally practice modular coding.

Best practices dictate that all database logic exists in separate, modular methods.

These files containing database access helpers are often called `models`

To handle CRUD operations for a single resource, we would want to create a `model` containing the following methods:

    function find() {
      return db('users');
    }

    function findById(id) {
      return db('users').where({ id }).first();
    }

    function add(user) {
      db('users').insert(user)
        .then(ids => {
          return findById(ids[0])
        })
    }

    function update(changes, id) {}

    function remove(id) {}

Each of these functions would use knex logic to perform the necessary database operation

Once complete you export, then import to use the helpers in our endpoints

    const User = require('./user-model.js');

    router.get('/', (req, res) {
      User.find()
        .then(users => {
          res.json(users)
        }).catch(err => {
          return res.status(400).json(err)
        })
    })

There should be no knex code in the endpoints themselves