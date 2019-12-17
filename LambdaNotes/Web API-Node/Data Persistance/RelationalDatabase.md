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
