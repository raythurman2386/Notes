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
