# Database Schema Design

## Use SQLite Studio on existing DB

To manage digital databases we use specialized software called DataBase Management Systems. These systems typically run on servers and are managed by DataBase Administrators.

### What is SQLite

SQLite is the DBMS we primarily use at Lambda. As the name suggests, it is a more lightweight system and thus easier to get set up than some others.

SQLite allows us to store databases as single files. Many of the challenges and guided projects in Lambda have a .db3 extension.

SQLite is not a database, but rather a database management system.

## Learn to explain what is a database schema

A database schema is the shape of our database. It defines what tables we'll have, which columns should exist within the tables and any restrictions on each column.

A well-designed database schema keeps the data well organized and can help ensure high-quality data.

One requirement every table should specify is a <strong>primary key</strong>.

A primary key is a way to identify each entry in the database uniquely.

It is most often represented as a auto incrementing integer called `id`

## Learn to create and use knex migrations

Knex provides a schema builder, which allows us to write code to design our database schema. However, beyond thinking about columns and constraints, we must also consider updates.

When a schema needs to be updated, a developer must feel confident that the changes go into effect everywhere.

This means schema updates on the developers local machine, on any testing or staging versions, on the prod database and then on any other devs local machines.

A database migration describes changes made to the structure of a database. 

Migrations include things like adding new objects, adding new tables, and modifying existing objects or tables.

### Knex CLI

To use migrations(and to make knex setup easier) we need to use knex cli. 

To start, add the knex and sqlite3 libraries to the repo

`npm install knex sqlite3`

Next you will create your knex config object

`npx knex init`

This command will generate a file called `knexfile.js`. It will be auto populated with three config objects, based on environments.

    module.exports = {
      development: {
        client: 'sqlite3',
        connection: {
          filename: './data/DATABASE_FILE_NAME.db3',
        },
        // Necessary with sqlite3
        useNullAsDefault: true,
        // generates migration files in specified dir
        migrations: {
          directory: './data/migrations'
        },
        seeds: {
          directory: './data/seeds'
        }
      }
    }

Now whenerever we configure our database, we may use the following syntax instead of hardcoding in a config object

    const knex = require('knex');
    const config = require('../knexfile.js');

    const db = knex(config.development);

    module.exports = db;

### Knex Migrations 

Once our knexfile is set up, we can begin creating migrations. 

we can generate a new migration with:

    npx knex migrate:make [migration-name]

If we needed to create an accounts table

    npx knex migrate:make create-accounts

<strong>DO NOT EDIT MIGRATION FILENAMES</strong>

The migration file should have an up and down function.

Within the up function we write the ended database changes.

Within the down function, we write the code to undo the up functions

    exports.up = function(knex, Promise) {
      return knex.schema.createTable('accounts', tbl => {
        tbl.increments();
        tbl.text('name', 128).unique().notNullable();
        tbl.decimal('budget').notNullable();
      })
    }

    exports.down = function(knex, Promise) {
      return knex.schema.dropTableIfExists('accounts');
    }

At this point, the table is not yet created. To run this, and any other migrations run:

    npx knex migrate:latest

If the database file does not exist, this command will auto-generate one.

#### Changes and Rollbacks

If later down the road we realize you need to update your schema, you shouldn't edit the migration file. 

Instead you will want to create a new migration with:

    npx knex migrate:make accounts-schema-update

Once we've written our updates into this file we save and close with:

    npx knex migrate:latest

If we migrate our database and then quickly realize something isn't right, we can edit the migration file. However, first, we need to rollback our last migration with:

    npx knex migrate:rollback

## Knex Seeds

To create a seed run:

    npx knex seed:make 001-seedName

Numbering is a good idea because Knex doesn't attach a timestamp to the name like migrate does.

    npx knex seed:make 001-accounts

A file will appear in the designated folder

    exports.seed = function(knex, Promise) {
      // truncate will reset the primary key each time
      return knex('accounts').truncate()
        .then(() => {
          return knex('accounts').insert([
            { name: 'Stephenson', budget: 10000 },
            { name: 'Gordon & Gale', budget: 40400},
          ])
        })
    }

You will then run your seeds by running:

    npx knex seed:run
