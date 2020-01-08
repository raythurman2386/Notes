# Data Modeling 
## Learn to explain data normalization

The relational database model is different from the object model we use in our JS code. 
In JS we can add arrays or nested objects to our entities.
A client can have multiple address embedded as an array. But that same relationship in a relational model could result in data repetition and other anomalies.

`Normalization` is the process of designing or refactoring database tables for maximum consistency and minimum redundancy.

With objects, we're used to denormalized data, stored with ease of use and speed in mind. Non-normalized tables are considered ineffective in relational databases.

### Normalization Guidlines
- Each record has a primary key
- No fields are repeated.
- All fields relate directly to the key data
- Each field entry contains a single data point
- There are no redundant entries

DENORMALIZED DATA
<br/>

<code>
<b>farm_name</b>  | <b>animal1</b>  | <b>animal2</b>  | <b>animal3</b>
<br/>
Beech Ranch | pigs  | chickens  | goats
</code>

<br/>
***
<br />

<code>
<b>farm_id</b>  | <b>farm_name</b>  | <b>animals</b>  | <b>ann_revenue</b>
<br/>
1 | Beech Ranch | pigs, chickens, goats | 65000
</code>

While we have now eliminated the first two issues, we now have multiple entries in one field separated by commas.

This isn't good either as its another example of denormalization.

There is no array data type in a relational database so each field must contain only one data point.

## Learn to explain different table relationships

When modeling the data for our systems we'll start noticing the relationships that exist between our entities.
Those relationships need to be added to our resulting model

There are three types of relationships
- One to one
- one to many
- many to many

Determining how data is related can provide a set of guidelines for table representation and guides the use of foreign keys to connect said tables.

### One to One Relationships

Imagine we are storing the financial projections for a series of farms

We may wish to attach fields into two categories: information related to the farm directly, and info related to financial projections

We would say that `farms` and `projections` have a one-to-one relationship. 

This is to say that every farm has exactly one projection and every project corresponds to exactly one farm

This can be represented in two tables: `farms` and `projections`

<code>
| id | farm_name |<br/>
|----|------------|<br/>
| 01 | Beech Ranch |<br/>
| 02 | Morton Farms |
</code>

<hr>
<br/>

<code>
| id | farm_id | revenue |<br/>
|----|----------|------|<br/>
| 01 |---- 1 ---|  65000  |<br/>
| 02 |---- 2 ---|  105000  |
</code>

The `farm_id` is the foregn key that links `farms` and `projections` together

#### Notes about one-to-one relationships

- foreign key should always have a unique constraint to prevent duplicate entries.
- The F key can be in either table, for ex we may have had a projection_id in the farms table instead
- You can represent one-to-one data in a single table without creating anomolies.

### One to Many Relationships
Now imagine we are storing the full-time ranchers employed at each farm. In this case, each rancher would only work at one farm, however each farm may have multiple ranchers

This is called a one-to-many relationship

This is the most common type of relationship between entities.

Manage this type of relationship by adding a foregn key on the many table of the relationship that points to the primary key on the "one" table.

Take the farms and ranchers tables.

In this case, the foreign key `farm_id` should not be unique

### Many to Many Relationships

If we want to track animals on a farm as well, we must explore the many-to-many relationship.

A farm has multiple animals, and multiple of each type

To model this relationship we need to introduce an intermediary table that holds foregn keys that reference the primary key on the related tables.

We now have a farms, animals, and farm_animals table

While each foregn key on the intermediary table is not unique, the combinations of keys should be unique.

## Learn to create table relationships using Knex

The Knex query builder library also allows us to create multi-table schemas include foreign keys. 

However there are a few extra things to keep in mind when designing a multi table schema, such as using the correct order when creating tables, dropping tables, seeding data and removing data

We have to consider the way that `delete` and `updates` through our API will impact related data

### Foreign Key setup

In Knex, foregn key restrictions don't automatically work. Whenever using foreign keys in your schema, add the following to your `knexfile`

```
development: {
  client: 'sqlite3',
  useNullAsDefault: true,
  connection: {
    filename: './data/database.db3',
  },
  // Needed when using foreign keys
  pool: {
    afterCreate: (conn, done) => {
      // runs after a connection is made to the sqlite engine
      conn.run('PRAGMA foreign_keys = ON', done);
    },
  },
},
```

### Migrations

Lets look at how we might track our `farms` and `ranchers` using knex in our `up` and `down` functions

```
exports.up = function(knex, Promis) {
  return knex.schema
    .createTable('farms', tbl => {
      tbl.increments();
      tbl.string('farm_name', 128)
        .notNullable();
    })
    // we can chain together createTable
    .createTable('ranchers', tbl => {
      tbl.increments();
      tbl.string('rancher_name', 128);
      tbl.integer('farm_id')
        .unsigned()
        .notNullable()
        .references('id')
        // This table must exist already
        .inTable('farms')
    })
}
```

Note that the foreign key can only be created after the reference table

In the down, you must always drop a table with a foreign key before dropping the table it references

```
exports.down = function(knex, Promise) {
  return knex.schema
    .dropTableIfExists('ranchers')
    .dropTableIfExists('farms')
}
```

In the case of many-to-many, the syntax for the intermediary table is identical minus one step to make sure each combo of foreign keys is unique

```
.createTable('farm_animals', tbl => {
  tbl.integer('farm_id')
    .unsigned()
    .notNullable()
    .references('id')
    // this table must exist already
    .inTable('farms')
  tbl.integer('animal_id')
    .unsigned()
    .notNullable()
    .references('id')
    // this table must exist already
    .inTable('animals')

  // the combination of the two keys becomes our primary key
  // will enforce unique combinations of ids
  tbl.primary(['farm_id', 'animal_id']);
});

```

### Seeds

Order is also a concern when seeding. We want to create seeds in the same order we created our tables.

In our example, make sure to write the 01-farms seed file then the 02-ranchers seed file

Since we want to truncate 02-rancers before 01-farms. A library called `knex-cleaner` provides an easy solution

Run `knex seed:make 00-cleanup` and `npm install knex-cleaner`

```
const cleaner = require('knex-cleaner`);

exports.seed = funciton(knex) {
  return cleaner.clean(knex, {
    mode: 'truncate',
    ignoreTables: ['knex_migrations', 'knex_migrations_lock']
  });
};
```

This removes all tables (excluding the two that track migrations) in the correct order before any seed files run.

### Cascading

If a user attempt to delete a record that is referenced by another record such as attempting to delete, by default, the database will block the action.

The same thing can happen when updating a record when a foreign key reference

With cascade, deleting a record also deletes all referencing records, we can set that up in our schema

```
.createTable('ranchers', tbl => {
  tbl.increments();
  tbl.string('rancher_name', 128);
  tbl.integer('farm_id')
    .unsigned()
    .notNullable()
    .references('id')
    .intable('farms')
    .onUpdate('CASCADE')
    .onDelete('CASCADE')
})
```