# SQL


<!-- TOC START -->
- [Related Terms:](#related-terms)
  - [See also:](#see-also)
- [Questions about SQL ?](#questions-about-sql)
  - [Basics and Importance](#basics-and-importance)
    - [What is SQL and why is it important?](#what-is-sql-and-why-is-it-important)
    - [What are the different types of SQL commands?](#what-are-the-different-types-of-sql-commands)
    - [What is the difference between SQL and NoSQL?](#what-is-the-difference-between-sql-and-nosql)
    - [What is a relational database in SQL?](#what-is-a-relational-database-in-sql)
    - [What are the basic operations that a simple SQL query does?](#what-are-the-basic-operations-that-a-simple-sql-query-does)
  - [SQL Syntax and Queries](#sql-syntax-and-queries)
    - [What is the syntax for creating a table in SQL?](#what-is-the-syntax-for-creating-a-table-in-sql)
    - [How do you insert data into a table in SQL?](#how-do-you-insert-data-into-a-table-in-sql)
    - [How do you update data in a table in SQL?](#how-do-you-update-data-in-a-table-in-sql)
    - [What is the purpose of the SELECT statement in SQL?](#what-is-the-purpose-of-the-select-statement-in-sql)
    - [How do you delete data from a table in SQL?](#how-do-you-delete-data-from-a-table-in-sql)
    - [What is the difference between the WHERE and HAVING clauses in SQL?](#what-is-the-difference-between-the-where-and-having-clauses-in-sql)
  - [Advanced SQL Concepts](#advanced-sql-concepts)
    - [What are SQL Joins and what are the different types of Joins in SQL?](#what-are-sql-joins-and-what-are-the-different-types-of-joins-in-sql)
    - [What are SQL Views and how are they used?](#what-are-sql-views-and-how-are-they-used)
    - [What are SQL Indexes and why are they important?](#what-are-sql-indexes-and-why-are-they-important)
    - [What are SQL Triggers and how are they used?](#what-are-sql-triggers-and-how-are-they-used)
    - [What is SQL Injection and how can it be prevented?](#what-is-sql-injection-and-how-can-it-be-prevented)
  - [SQL for Testing](#sql-for-testing)
    - [How is SQL used in software testing?](#how-is-sql-used-in-software-testing)
    - [How can SQL queries be used to validate data?](#how-can-sql-queries-be-used-to-validate-data)
    - [What is the role of SQL in backend testing?](#what-is-the-role-of-sql-in-backend-testing)
    - [How can SQL be used to test database connections?](#how-can-sql-be-used-to-test-database-connections)
    - [What are some common SQL queries used in software testing?](#what-are-some-common-sql-queries-used-in-software-testing)
<!-- TOC END -->

SQL

(Structured Query Language) is a standardized programming language specifically designed for managing and manipulating relational

databases

.

SQL

is used to perform tasks such as querying data, updating data, inserting data, and deleting data from a

database

. It also involves creating and modifying schemas (

database

structures) and controlling access to data.

SQL

provides a consistent interface to relational

database

management systems (RDBMS) and is supported by most modern RDBMS platforms like MySQL, PostgreSQL,

SQL

Server, Oracle, and many others. Through

SQL

, users can define, retrieve, and manipulate data within the

database

efficiently and effectively.

## Related Terms:

- [Database](../D/database.md)

### See also:

- [Wikipedia](https://en.wikipedia.org/wiki/SQL)

## Questions about SQL ?

### Basics and Importance

#### What is SQL and why is it important?

  [SQL](../S/sql.md), or **Structured Query Language**, is a standardized programming language used for managing and manipulating relational [databases](../D/database.md). It is important because it provides a systematic way to create, retrieve, update, and delete data from [databases](../D/database.md), which are integral to most software applications.
  In the context of **software [test automation](../T/test-automation.md)**, [SQL](../S/sql.md) plays a crucial role in validating the state and integrity of data, which directly impacts the reliability of the application under test. [Test automation](../T/test-automation.md) engineers use [SQL](../S/sql.md) to:

  - Verify that data manipulation operations, such as inserts, updates, and deletions, have been performed correctly.
  - Set up and tear down test data, ensuring tests run in a known state.
  - Validate business logic that involves data retrieval and manipulation, ensuring the application behaves as expected.
  - Perform backend testing to ensure that the application interacts with the database correctly, including handling of transactions and concurrency.
  - Check data integrity and constraints to ensure that the database maintains a valid state throughout different test scenarios.
  [SQL](../S/sql.md) is a critical skill for [test automation](../T/test-automation.md) engineers as it enables them to interact directly with the [database](../D/database.md), bypassing the user interface. This allows for more thorough testing of the application layers that interact with the [database](../D/database.md), and for the creation of more complex [test scenarios](../T/test-scenario.md) that might be difficult or time-consuming to replicate through the UI.

  - Verify that data manipulation operations, such as inserts, updates, and deletions, have been performed correctly.
  - Set up and tear down test data, ensuring tests run in a known state.
  - Validate business logic that involves data retrieval and manipulation, ensuring the application behaves as expected.
  - Perform backend testing to ensure that the application interacts with the database correctly, including handling of transactions and concurrency.
  - Check data integrity and constraints to ensure that the database maintains a valid state throughout different test scenarios.

#### What are the different types of SQL commands?

  [SQL](../S/sql.md) commands can be broadly categorized into four types:

  1. **Data Definition Language (DDL)**: These commands define the structure of the [database](../D/database.md) and manipulate [database](../D/database.md) objects such as tables, indexes, and views.
    - `CREATE` : Creates new database objects.
    - `ALTER` : Modifies existing database objects.
    - `DROP` : Deletes database objects.
    - `TRUNCATE` : Removes all records from a table, including all spaces allocated for the records.
    - `CREATE` : Creates new database objects.
    - `ALTER` : Modifies existing database objects.
    - `DROP` : Deletes database objects.
    - `TRUNCATE` : Removes all records from a table, including all spaces allocated for the records.
  2. **Data Manipulation Language (DML)**: These commands deal with the manipulation of data present in the [database](../D/database.md).
    - `INSERT` : Adds new data to a table.
    - `UPDATE` : Modifies existing data within a table.
    - `DELETE` : Removes data from a table.
    - `INSERT` : Adds new data to a table.
    - `UPDATE` : Modifies existing data within a table.
    - `DELETE` : Removes data from a table.
  3. **Data Control Language (DCL)**: These commands are related to the rights, permissions, and other controls of the [database](../D/database.md) system.
    - `GRANT` : Gives user's access privileges to the database.
    - `REVOKE` : Withdraws user's access privileges given by using the GRANT command.
    - `GRANT` : Gives user's access privileges to the database.
    - `REVOKE` : Withdraws user's access privileges given by using the GRANT command.
  4. **Transaction Control Language (TCL)**: These commands deal with the transaction operations within the [database](../D/database.md).
    - `COMMIT` : Saves all the transactions to the database.
    - `ROLLBACK` : Restores the database to the last committed state.
    - `SAVEPOINT` : Sets a savepoint within a transaction.
    - `SET TRANSACTION` : Places a name on a transaction.
    - `COMMIT` : Saves all the transactions to the database.
    - `ROLLBACK` : Restores the database to the last committed state.
    - `SAVEPOINT` : Sets a savepoint within a transaction.
    - `SET TRANSACTION` : Places a name on a transaction.
  Understanding these commands is crucial for [database](../D/database.md) manipulation and management, which is often necessary in [test automation](../T/test-automation.md) to ensure the application interacts correctly with the [database](../D/database.md).

  1. **Data Definition Language (DDL)**: These commands define the structure of the [database](../D/database.md) and manipulate [database](../D/database.md) objects such as tables, indexes, and views.
    - `CREATE` : Creates new database objects.
    - `ALTER` : Modifies existing database objects.
    - `DROP` : Deletes database objects.
    - `TRUNCATE` : Removes all records from a table, including all spaces allocated for the records.
    - `CREATE` : Creates new database objects.
    - `ALTER` : Modifies existing database objects.
    - `DROP` : Deletes database objects.
    - `TRUNCATE` : Removes all records from a table, including all spaces allocated for the records.
  2. **Data Manipulation Language (DML)**: These commands deal with the manipulation of data present in the [database](../D/database.md).
    - `INSERT` : Adds new data to a table.
    - `UPDATE` : Modifies existing data within a table.
    - `DELETE` : Removes data from a table.
    - `INSERT` : Adds new data to a table.
    - `UPDATE` : Modifies existing data within a table.
    - `DELETE` : Removes data from a table.
  3. **Data Control Language (DCL)**: These commands are related to the rights, permissions, and other controls of the [database](../D/database.md) system.
    - `GRANT` : Gives user's access privileges to the database.
    - `REVOKE` : Withdraws user's access privileges given by using the GRANT command.
    - `GRANT` : Gives user's access privileges to the database.
    - `REVOKE` : Withdraws user's access privileges given by using the GRANT command.
  4. **Transaction Control Language (TCL)**: These commands deal with the transaction operations within the [database](../D/database.md).
    - `COMMIT` : Saves all the transactions to the database.
    - `ROLLBACK` : Restores the database to the last committed state.
    - `SAVEPOINT` : Sets a savepoint within a transaction.
    - `SET TRANSACTION` : Places a name on a transaction.
    - `COMMIT` : Saves all the transactions to the database.
    - `ROLLBACK` : Restores the database to the last committed state.
    - `SAVEPOINT` : Sets a savepoint within a transaction.
    - `SET TRANSACTION` : Places a name on a transaction.

#### What is the difference between SQL and NoSQL?

  [SQL](../S/sql.md) (Structured Query Language) [databases](../D/database.md), also known as **relational [databases](../D/database.md)**, store data in tables with predefined schemas, using rows and columns. They excel in **ACID transactions** (Atomicity, Consistency, Isolation, Durability) and support complex queries with **JOIN operations**.
  NoSQL (Not Only [SQL](../S/sql.md)) [databases](../D/database.md) are designed for distributed data stores with **horizontal scaling** in mind. They do not require a fixed schema and can store unstructured data like documents, key-value pairs, wide-column stores, or graphs. NoSQL [databases](../D/database.md) are often chosen for their ability to handle **large volumes of data** and **high traffic loads** with **flexible data models**.
  The key differences are:

  - **Schema flexibility** : NoSQL databases allow for a flexible, dynamic schema, while SQL databases require a predefined schema.
  - **Scaling** : NoSQL databases are typically designed to scale out by distributing data across multiple servers, whereas SQL databases scale up by increasing the power of the existing hardware.
  - **Data model** : SQL databases are table-based, while NoSQL databases can be document-oriented, key-value pairs, wide-column stores, or graph databases.
  - **Transactions** : SQL databases support complex transactions and are ACID-compliant, making them suitable for applications that require reliability and consistency. NoSQL databases may offer eventual consistency and prioritize availability and partition tolerance (following the CAP theorem).
  - **Query language** : SQL databases use the SQL language for queries, which is powerful for complex queries. NoSQL databases have varied query languages that are typically less complex and may not support JOIN operations or multi-record ACID transactions.
  - **Schema flexibility** : NoSQL databases allow for a flexible, dynamic schema, while SQL databases require a predefined schema.
  - **Scaling** : NoSQL databases are typically designed to scale out by distributing data across multiple servers, whereas SQL databases scale up by increasing the power of the existing hardware.
  - **Data model** : SQL databases are table-based, while NoSQL databases can be document-oriented, key-value pairs, wide-column stores, or graph databases.
  - **Transactions** : SQL databases support complex transactions and are ACID-compliant, making them suitable for applications that require reliability and consistency. NoSQL databases may offer eventual consistency and prioritize availability and partition tolerance (following the CAP theorem).
  - **Query language** : SQL databases use the SQL language for queries, which is powerful for complex queries. NoSQL databases have varied query languages that are typically less complex and may not support JOIN operations or multi-record ACID transactions.

#### What is a relational database in SQL?

  A **relational [database](../D/database.md)** is a collection of data items organized as a set of formally described tables from which data can be accessed or reassembled in various ways without having to reorganize the [database](../D/database.md) tables. The relational model means that the logical data structures—the data tables, views, and indexes—are separate from the physical storage structures. This model is based on **first-order predicate logic** and its core idea is to describe a [database](../D/database.md) as a collection of predicates over a finite set of predicate variables, describing constraints on the possible values and combinations of values.
  The key element of the relational [database](../D/database.md) is the **table** (or relation), where data is stored in rows and columns. Each table has a unique primary key, which identifies the rows. Tables can relate to each other through **foreign keys**, which are fields that reference a primary key in another table.
  Relational [databases](../D/database.md) use **Structured Query Language ([SQL](../S/sql.md))** for defining and manipulating data. This is powerful because it allows for data to be easily accessed and it is also used to maintain the integrity of the [database](../D/database.md) using constraints (e.g., UNIQUE, NOT NULL, CHECK, FOREIGN KEY).
  In the context of [test automation](../T/test-automation.md), relational [databases](../D/database.md) are often the backend of an application, and understanding their structure is crucial for validating that the application is storing and retrieving data correctly. [Test automation](../T/test-automation.md) engineers can write [SQL](../S/sql.md) queries to extract data and use it to verify application behavior or to set up test preconditions.

#### What are the basic operations that a simple SQL query does?

  Basic operations performed by a simple [SQL](../S/sql.md) query include:

  - **Selecting**
    data with
    `SELECT` :

    ```
    SELECT column1, column2 FROM table_name;
    ```

  - **Filtering**
    data using
    `WHERE` :

    ```
    SELECT * FROM table_name WHERE condition;
    ```

  - **Sorting**
    results with
    `ORDER BY` :

    ```
    SELECT * FROM table_name ORDER BY column ASC|DESC;
    ```

  - **Limiting**
    results using
    `LIMIT` :

    ```
    SELECT * FROM table_name LIMIT number;
    ```

  - **Grouping**
    data with
    `GROUP BY`
    for aggregate functions:

    ```
    SELECT COUNT(column1), column2 FROM table_name GROUP BY column2;
    ```

  - **Combining**
    columns from multiple tables using
    `JOIN` :

    ```
    SELECT * FROM table1 INNER JOIN table2 ON table1.column_name = table2.column_name;
    ```

  - **Calculating**
    values with built-in functions like
    `SUM()`
    ,
    `AVG()`
    ,
    `MIN()`
    ,
    `MAX()` :

    ```
    SELECT AVG(column1) FROM table_name;
    ```

  - **Aliasing**
    columns or tables for readability with
    `AS` :

    ```
    SELECT column1 AS alias_name FROM table_name;
    ```

  - **Inserting**
    new data with
    `INSERT INTO` :

    ```
    INSERT INTO table_name (column1, column2) VALUES (value1, value2);
    ```

  - **Updating**
    existing data with
    `UPDATE` :

    ```
    UPDATE table_name SET column1 = value1 WHERE condition;
    ```

  - **Deleting**
    data with
    `DELETE` :

    ```
    DELETE FROM table_name WHERE condition;
    ```
  These operations are foundational for interacting with and manipulating data within a [database](../D/database.md).

  - **Selecting**
    data with
    `SELECT` :

    ```
    SELECT column1, column2 FROM table_name;
    ```

  - **Filtering**
    data using
    `WHERE` :

    ```
    SELECT * FROM table_name WHERE condition;
    ```

  - **Sorting**
    results with
    `ORDER BY` :

    ```
    SELECT * FROM table_name ORDER BY column ASC|DESC;
    ```

  - **Limiting**
    results using
    `LIMIT` :

    ```
    SELECT * FROM table_name LIMIT number;
    ```

  - **Grouping**
    data with
    `GROUP BY`
    for aggregate functions:

    ```
    SELECT COUNT(column1), column2 FROM table_name GROUP BY column2;
    ```

  - **Combining**
    columns from multiple tables using
    `JOIN` :

    ```
    SELECT * FROM table1 INNER JOIN table2 ON table1.column_name = table2.column_name;
    ```

  - **Calculating**
    values with built-in functions like
    `SUM()`
    ,
    `AVG()`
    ,
    `MIN()`
    ,
    `MAX()` :

    ```
    SELECT AVG(column1) FROM table_name;
    ```

  - **Aliasing**
    columns or tables for readability with
    `AS` :

    ```
    SELECT column1 AS alias_name FROM table_name;
    ```

  - **Inserting**
    new data with
    `INSERT INTO` :

    ```
    INSERT INTO table_name (column1, column2) VALUES (value1, value2);
    ```

  - **Updating**
    existing data with
    `UPDATE` :

    ```
    UPDATE table_name SET column1 = value1 WHERE condition;
    ```

  - **Deleting**
    data with
    `DELETE` :

    ```
    DELETE FROM table_name WHERE condition;
    ```

### SQL Syntax and Queries

#### What is the syntax for creating a table in SQL?

  To create a table in [SQL](../S/sql.md), use the `CREATE TABLE` statement followed by the table name and a list of columns with their respective data types and constraints within parentheses. Each column definition is separated by a comma. Here's the basic syntax:

  ```
  CREATE TABLE table_name (
      column1 datatype constraint,
      column2 datatype constraint,
      column3 datatype constraint,
      ...
  );
  ```
  For example, to create a table named `users` with three columns—`id`, `name`, and `email`—where `id` is an integer that auto-increments and serves as the primary key, `name` is a variable character string with a maximum length of 50 characters, and `email` is a variable character string with a maximum length of 100 characters, the [SQL](../S/sql.md) statement would be:

  ```
  CREATE TABLE users (
      id INT AUTO_INCREMENT PRIMARY KEY,
      name VARCHAR(50),
      email VARCHAR(100)
  );
  ```
  Remember to define the **primary key** for the table, which uniquely identifies each record. If needed, you can also specify other constraints like `NOT NULL`, `UNIQUE`, `CHECK`, `FOREIGN KEY`, etc., to enforce data integrity.

#### How do you insert data into a table in SQL?

  To insert data into a table in [SQL](../S/sql.md), use the `INSERT INTO` statement. Specify the table and then define the columns and values you want to insert. If you're inserting values for all columns in the table, you can omit the column names and only provide the values in the same order as the columns in the table schema.
  Here's the basic syntax for inserting data into a table:

  ```
  INSERT INTO table_name (column1, column2, column3, ...)
  VALUES (value1, value2, value3, ...);
  ```
  For example, if you have a table named `users` with columns `id`, `name`, and `email`, you can insert a new row like this:

  ```
  INSERT INTO users (id, name, email)
  VALUES (1, 'John Doe', 'john.doe@example.com');
  ```
  If you're inserting multiple rows at once, separate each set of values with a comma:

  ```
  INSERT INTO users (id, name, email)
  VALUES
  (1, 'John Doe', 'john.doe@example.com'),
  (2, 'Jane Smith', 'jane.smith@example.com');
  ```
  Remember to use single quotes for string values and to escape any special characters to prevent [SQL](../S/sql.md) injection attacks. For numerical values, quotes are not necessary. Always validate and sanitize input when using dynamic data to protect against malicious [SQL](../S/sql.md) injection.

#### How do you update data in a table in SQL?

  To update data in a [SQL](../S/sql.md) table, use the `UPDATE` statement. Specify the table and set the new values for one or more columns, often using a `WHERE` clause to target specific rows. Here's the basic syntax:

  ```
  UPDATE table_name
  SET column1 = value1, column2 = value2, ...
  WHERE condition;
  ```
  **Example**: Imagine you have a `users` table and you want to update the email of a user with the `id` of 10.

  ```
  UPDATE users
  SET email = 'newemail@example.com'
  WHERE id = 10;
  ```
  **Best Practices**:

  - Always use a
    `WHERE`
    clause to avoid updating all rows unintentionally.

  - Test your
    `WHERE`
    clause with a
    `SELECT`
    statement first to ensure you're targeting the right rows.

  - Use transactions if your database supports them, to roll back changes in case of errors.
  - For complex conditions, consider using subqueries within the
    `WHERE`
    clause.

  - When updating multiple rows based on different conditions, you can use a
    `CASE`
    statement within the
    `SET`
    clause.
  **Note**: In [test automation](../T/test-automation.md), ensure your [test data](../T/test-data.md) is backed up or can be easily restored before running update queries, as they modify the data state.

  - Always use a
    `WHERE`
    clause to avoid updating all rows unintentionally.

  - Test your
    `WHERE`
    clause with a
    `SELECT`
    statement first to ensure you're targeting the right rows.

  - Use transactions if your database supports them, to roll back changes in case of errors.
  - For complex conditions, consider using subqueries within the
    `WHERE`
    clause.

  - When updating multiple rows based on different conditions, you can use a
    `CASE`
    statement within the
    `SET`
    clause.

#### What is the purpose of the SELECT statement in SQL?

  The `SELECT` statement in [SQL](../S/sql.md) is used to **retrieve data** from one or more tables in a [database](../D/database.md). It allows you to specify the exact columns you want to fetch, along with any conditions for selecting rows. The `SELECT` statement is fundamental for [test automation](../T/test-automation.md) engineers to **validate the state of the data**, ensuring that the application under test is manipulating the data correctly.
  Here's a basic example of a `SELECT` statement:

  ```
  SELECT column1, column2 FROM table_name WHERE condition;
  ```
  In [test automation](../T/test-automation.md), you might use `SELECT` to:

  - Verify the insertion of a new record.
  - Check updates to existing records.
  - Confirm the deletion of records.
  - Validate business logic by checking if the data meets certain conditions.
  - Extract data to be used as input for automated test cases.
  For instance, after a [test case](../T/test-case.md) that inserts a record, you might use:

  ```
  SELECT * FROM users WHERE username = 'testuser';
  ```
  This query checks if 'testuser' was successfully added to the `users` table. The `SELECT` statement is versatile and can be combined with other [SQL](../S/sql.md) clauses and functions to perform complex data validations, making it an indispensable tool for backend testing.

  - Verify the insertion of a new record.
  - Check updates to existing records.
  - Confirm the deletion of records.
  - Validate business logic by checking if the data meets certain conditions.
  - Extract data to be used as input for automated test cases.

#### How do you delete data from a table in SQL?

  To **delete data from a table** in [SQL](../S/sql.md), use the `DELETE` statement. Specify the table and the condition for which rows should be deleted using the `WHERE` clause. Without a `WHERE` clause, all rows will be removed.
  Here's the basic syntax:

  ```
  DELETE FROM table_name WHERE condition;
  ```
  For example, to delete a record where the `id` is `10`:

  ```
  DELETE FROM Employees WHERE id = 10;
  ```
  **Caution**: Omitting the `WHERE` clause will delete all records in the table, which can't be undone without a backup.
  For [test automation](../T/test-automation.md), you might delete [test data](../T/test-data.md) after a test run:

  ```
  DELETE FROM Test_Results WHERE test_date < '2023-01-01';
  ```
  Always back up data before mass delete operations, and consider transaction control statements like `BEGIN TRANSACTION`, `COMMIT`, and `ROLLBACK` for safety.

#### What is the difference between the WHERE and HAVING clauses in SQL?

  The `WHERE` and `HAVING` clauses in [SQL](../S/sql.md) are both used to filter records, but they serve different purposes and operate at different stages of the query processing.

  - **WHERE** : This clause is used to filter records
    **before**
    any groupings are made. It applies to individual rows of a table. You use
    `WHERE`
    to specify the conditions that must be met for the rows to be included in the result set.

  ```
  SELECT column1, column2
  FROM table
  WHERE condition;
  ```

  - **HAVING** : This clause is used to filter groups of rows
    **after**
    the
    `GROUP BY`
    clause has been applied. It's typically used when you want to apply a condition to a group function like
    `SUM()`
    ,
    `AVG()`
    ,
    `MAX()`
    , etc.

  ```
  SELECT column1, SUM(column2)
  FROM table
  GROUP BY column1
  HAVING condition;
  ```
  In essence, if you need to filter rows based on individual column values, use `WHERE`. If you need to filter on the result of an aggregate function, use `HAVING`. Remember that `HAVING` can only be used when `GROUP BY` is present, whereas `WHERE` can be used without it.

  - **WHERE** : This clause is used to filter records
    **before**
    any groupings are made. It applies to individual rows of a table. You use
    `WHERE`
    to specify the conditions that must be met for the rows to be included in the result set.

  - **HAVING** : This clause is used to filter groups of rows
    **after**
    the
    `GROUP BY`
    clause has been applied. It's typically used when you want to apply a condition to a group function like
    `SUM()`
    ,
    `AVG()`
    ,
    `MAX()`
    , etc.

### Advanced SQL Concepts

#### What are SQL Joins and what are the different types of Joins in SQL?

  [SQL](../S/sql.md) joins are used to combine rows from two or more tables, based on a related column between them. There are several types of joins:

  - **INNER JOIN** : Returns records that have matching values in both tables.

  ```
  SELECT * FROM table1
  INNER JOIN table2
  ON table1.common_field = table2.common_field;
  ```

  - **LEFT (OUTER) JOIN** : Returns all records from the left table, and the matched records from the right table. If there is no match, the result is NULL on the right side.

  ```
  SELECT * FROM table1
  LEFT JOIN table2
  ON table1.common_field = table2.common_field;
  ```

  - **RIGHT (OUTER) JOIN** : Returns all records from the right table, and the matched records from the left table. If there is no match, the result is NULL on the left side.

  ```
  SELECT * FROM table1
  RIGHT JOIN table2
  ON table1.common_field = table2.common_field;
  ```

  - **FULL (OUTER) JOIN** : Returns all records when there is a match in either left or right table. If there is no match, the result is NULL for the unmatched side.

  ```
  SELECT * FROM table1
  FULL OUTER JOIN table2
  ON table1.common_field = table2.common_field;
  ```

  - **CROSS JOIN** : Returns all possible combinations of rows from both tables. This join does not require a condition to join and can produce a large number of rows.

  ```
  SELECT * FROM table1
  CROSS JOIN table2;
  ```

  - **SELF JOIN** : A regular join, but the table is joined with itself.

  ```
  SELECT * FROM table1 T1
  INNER JOIN table1 T2
  ON T1.common_field = T2.common_field;
  ```
  Understanding and utilizing these joins is crucial for querying complex data sets and validating data relationships during [software testing](../S/software-testing.md).

  - **INNER JOIN** : Returns records that have matching values in both tables.
  - **LEFT (OUTER) JOIN** : Returns all records from the left table, and the matched records from the right table. If there is no match, the result is NULL on the right side.
  - **RIGHT (OUTER) JOIN** : Returns all records from the right table, and the matched records from the left table. If there is no match, the result is NULL on the left side.
  - **FULL (OUTER) JOIN** : Returns all records when there is a match in either left or right table. If there is no match, the result is NULL for the unmatched side.
  - **CROSS JOIN** : Returns all possible combinations of rows from both tables. This join does not require a condition to join and can produce a large number of rows.
  - **SELF JOIN** : A regular join, but the table is joined with itself.

#### What are SQL Views and how are they used?

  [SQL](../S/sql.md) Views are virtual tables representing a subset of data from one or more tables. They are created using the `CREATE VIEW` statement and can encapsulate complex queries with joins, filters, and aggregations to simplify data access.
  Views are used to:

  - **Restrict access to data** : By providing a specific view of the data, sensitive information can be hidden from certain users.
  - **Simplify complex queries** : Instead of writing lengthy SQL queries each time, a view can store the complexity and present a simple interface.
  - **Enhance readability** : Views can be named descriptively to convey the data they represent, making SQL code easier to understand.
  - **Maintain legacy code** : If underlying table structures change, views can provide a consistent interface without modifying existing queries or applications.
  Here's an example of creating a view:

  ```
  CREATE VIEW EmployeeSummary AS
  SELECT EmployeeID, FirstName, LastName, Department
  FROM Employees
  WHERE IsActive = 1;
  ```
  To query the view, you use the `SELECT` statement just as you would with a regular table:

  ```
  SELECT * FROM EmployeeSummary;
  ```
  Remember, views do not store data physically; they fetch data from the underlying tables each time they are queried. Changes to the data in the base tables are immediately reflected in the views. However, some views are updatable and can be used to modify data in the base tables, subject to certain constraints.

  - **Restrict access to data** : By providing a specific view of the data, sensitive information can be hidden from certain users.
  - **Simplify complex queries** : Instead of writing lengthy SQL queries each time, a view can store the complexity and present a simple interface.
  - **Enhance readability** : Views can be named descriptively to convey the data they represent, making SQL code easier to understand.
  - **Maintain legacy code** : If underlying table structures change, views can provide a consistent interface without modifying existing queries or applications.

#### What are SQL Indexes and why are they important?

  [SQL](../S/sql.md) indexes are special lookup tables that the [database](../D/database.md) search engine can use to speed up data retrieval. Simply put, an index in [SQL](../S/sql.md) is used to **quickly locate and access the data** in a [database](../D/database.md) table. Indexes are particularly important for improving the performance of **SELECT** queries and are also beneficial when you have **WHERE** clauses that filter sorted data.
  An index is created on one or more columns of a table. When an index is created, it sorts the values of the specified columns and stores them in a data structure, typically a B-tree or a hash table. This means that when a query is executed, the [database](../D/database.md) can use the index to find data quickly instead of scanning the entire table, which can be time-consuming especially with large tables.
  For [test automation](../T/test-automation.md) engineers, understanding indexes is crucial because:

  - They can significantly
    **reduce the time**
    it takes to run tests that involve data verification or comparison.

  - They help in identifying performance issues that could be mitigated by proper indexing, ensuring that the application scales well.
  - They are essential for writing efficient SQL queries in tests, which can
    **reduce the load**
    on the database and minimize the risk of timeouts or slow test execution.
  However, it's important to note that while indexes can improve read performance, they can also **slow down write operations** (INSERT, UPDATE, DELETE) because the index has to be updated whenever the data in the indexed columns is modified. Therefore, careful consideration must be given to determine which columns to index, especially in a frequently updated [database](../D/database.md).

  - They can significantly
    **reduce the time**
    it takes to run tests that involve data verification or comparison.

  - They help in identifying performance issues that could be mitigated by proper indexing, ensuring that the application scales well.
  - They are essential for writing efficient SQL queries in tests, which can
    **reduce the load**
    on the database and minimize the risk of timeouts or slow test execution.

#### What are SQL Triggers and how are they used?

  [SQL](../S/sql.md) Triggers are special types of stored procedures that automatically execute or fire when a specified event occurs in the [database](../D/database.md), such as `INSERT`, `UPDATE`, or `DELETE` operations on a table. They are used to enforce business rules, maintain data integrity, and manage changes in [database](../D/database.md) state without manual intervention.
  Triggers can be defined to execute before or after the triggering event. For example:

  - **BEFORE triggers** : Perform a task before a data row is inserted, updated, or deleted.
  - **AFTER triggers** : Execute after the data modification is completed.
  Here's a simple example of a trigger that logs an audit entry after a record is updated in a table:

  ```
  CREATE TRIGGER AuditLogUpdate
  AFTER UPDATE ON Employees
  FOR EACH ROW
  BEGIN
     INSERT INTO AuditLog (ChangeType, TableName, ChangedBy, ChangeDate)
     VALUES ('UPDATE', 'Employees', CURRENT_USER(), NOW());
  END;
  ```
  In [test automation](../T/test-automation.md), triggers can be used to:

  - **Verify business logic** : Ensure that business rules are enforced by the trigger during test cases.
  - **Data validation** : Check if the trigger maintains data integrity by preventing invalid data operations.
  - **[Performance testing](../P/performance-testing.md)** : Assess the impact of triggers on database performance.
  - **[Regression testing](../R/regression-testing.md)** : Confirm that new changes do not break existing triggers.
  Triggers should be used judiciously as they can introduce complexity and affect performance. [Test automation](../T/test-automation.md) engineers must ensure that triggers work as expected and do not introduce unintended side effects.

  - **BEFORE triggers** : Perform a task before a data row is inserted, updated, or deleted.
  - **AFTER triggers** : Execute after the data modification is completed.
  - **Verify business logic** : Ensure that business rules are enforced by the trigger during test cases.
  - **Data validation** : Check if the trigger maintains data integrity by preventing invalid data operations.
  - **[Performance testing](../P/performance-testing.md)** : Assess the impact of triggers on database performance.
  - **[Regression testing](../R/regression-testing.md)** : Confirm that new changes do not break existing triggers.

#### What is SQL Injection and how can it be prevented?

  [SQL](../S/sql.md) Injection is a type of security vulnerability where an attacker can manipulate a [SQL](../S/sql.md) query by injecting malicious [SQL](../S/sql.md) code through an application's input data. This can result in unauthorized access to or manipulation of [database](../D/database.md) data.
  To prevent [SQL](../S/sql.md) Injection:

  - **Use Prepared Statements (Parameterized Queries)**: They enforce a clear separation between the code and the data. For example, in Java, you can use `PreparedStatement` objects.

    ```
    String query = "SELECT * FROM users WHERE username = ? AND password = ?";
    PreparedStatement ps = connection.prepareStatement(query);
    ps.setString(1, username);
    ps.setString(2, password);
    ```

  - **Employ Stored Procedures**: They encapsulate the [SQL](../S/sql.md) statements and treat all input as data rather than executable code.
  - **Validate Input**: Rigorously validate user inputs for type, length, format, and range. Use regular expressions or validation libraries.
  - **Escape User Input**: If you must include user input within [SQL](../S/sql.md) queries, make sure to escape special characters. However, this is less secure than prepared statements and should be avoided when possible.
  - **Use ORM Libraries**: Object-Relational Mapping (ORM) libraries like Hibernate or Entity Framework can abstract [SQL](../S/sql.md) queries and use their own methods to prevent injection.
  - **Implement Least Privilege**: Restrict [database](../D/database.md) user permissions so that if an injection occurs, the potential damage is minimized.
  - **Keep Software Updated**: Ensure that your [database](../D/database.md) management system (DBMS) and any related software are up-to-date with the latest security patches.
  - **Use Web Application Firewalls**: They can help to detect and block [SQL](../S/sql.md) Injection attacks.
  - **[Security Testing](../S/security-testing.md)**: Regularly test your application for [SQL](../S/sql.md) Injection vulnerabilities using tools like SQLMap or by performing [penetration testing](../P/penetration-testing.md).
  - **Use Prepared Statements (Parameterized Queries)**: They enforce a clear separation between the code and the data. For example, in Java, you can use `PreparedStatement` objects.

    ```
    String query = "SELECT * FROM users WHERE username = ? AND password = ?";
    PreparedStatement ps = connection.prepareStatement(query);
    ps.setString(1, username);
    ps.setString(2, password);
    ```

  - **Employ Stored Procedures**: They encapsulate the [SQL](../S/sql.md) statements and treat all input as data rather than executable code.
  - **Validate Input**: Rigorously validate user inputs for type, length, format, and range. Use regular expressions or validation libraries.
  - **Escape User Input**: If you must include user input within [SQL](../S/sql.md) queries, make sure to escape special characters. However, this is less secure than prepared statements and should be avoided when possible.
  - **Use ORM Libraries**: Object-Relational Mapping (ORM) libraries like Hibernate or Entity Framework can abstract [SQL](../S/sql.md) queries and use their own methods to prevent injection.
  - **Implement Least Privilege**: Restrict [database](../D/database.md) user permissions so that if an injection occurs, the potential damage is minimized.
  - **Keep Software Updated**: Ensure that your [database](../D/database.md) management system (DBMS) and any related software are up-to-date with the latest security patches.
  - **Use Web Application Firewalls**: They can help to detect and block [SQL](../S/sql.md) Injection attacks.
  - **[Security Testing](../S/security-testing.md)**: Regularly test your application for [SQL](../S/sql.md) Injection vulnerabilities using tools like SQLMap or by performing [penetration testing](../P/penetration-testing.md).

### SQL for Testing

#### How is SQL used in software testing?

  [SQL](../S/sql.md) is integral to **software [test automation](../T/test-automation.md)** for validating the state and integrity of data within relational [databases](../D/database.md). It enables testers to:

  - **Verify outcomes**
    of test cases by executing
    `SELECT`
    queries to check if data manipulations lead to expected results.

  - **Set up and tear down [test data](../T/test-data.md)**
    using
    `INSERT`
    ,
    `UPDATE`
    , and
    `DELETE`
    commands, ensuring tests run in a controlled environment.

  - **Test [database](../D/database.md) functions, stored procedures, and triggers**
    by invoking them and assessing their effects on the data.

  - **Validate business logic**
    implemented at the database level by running complex queries involving
    `JOIN`
    s, subqueries, and aggregate functions.

  - **Check constraints and indexes**
    to ensure they are functioning as intended, which is crucial for data integrity and performance.

  - **Simulate user transactions**
    to test transactional integrity and concurrency by using transactions with
    `BEGIN`
    ,
    `COMMIT`
    , and
    `ROLLBACK`
    .

  - **Assess performance**
    of queries and database operations, identifying potential bottlenecks or optimizations.
  Automated [test scripts](../T/test-script.md) often include [SQL](../S/sql.md) queries to perform these tasks, and results are compared against expected outcomes to determine test pass or fail status. [SQL](../S/sql.md)'s role in [test automation](../T/test-automation.md) is therefore pivotal for backend testing, ensuring the application behaves correctly in conjunction with the [database](../D/database.md) layer.

  - **Verify outcomes**
    of test cases by executing
    `SELECT`
    queries to check if data manipulations lead to expected results.

  - **Set up and tear down [test data](../T/test-data.md)**
    using
    `INSERT`
    ,
    `UPDATE`
    , and
    `DELETE`
    commands, ensuring tests run in a controlled environment.

  - **Test [database](../D/database.md) functions, stored procedures, and triggers**
    by invoking them and assessing their effects on the data.

  - **Validate business logic**
    implemented at the database level by running complex queries involving
    `JOIN`
    s, subqueries, and aggregate functions.

  - **Check constraints and indexes**
    to ensure they are functioning as intended, which is crucial for data integrity and performance.

  - **Simulate user transactions**
    to test transactional integrity and concurrency by using transactions with
    `BEGIN`
    ,
    `COMMIT`
    , and
    `ROLLBACK`
    .

  - **Assess performance**
    of queries and database operations, identifying potential bottlenecks or optimizations.

#### How can SQL queries be used to validate data?

  [SQL](../S/sql.md) queries can be instrumental in **validating data** as part of software [test automation](../T/test-automation.md). By executing specific queries, testers can verify that data manipulation operations, such as inserts, updates, and deletions, have been performed correctly.
  For **data integrity checks**, a `SELECT` statement can be used to retrieve data and ensure it matches [expected results](../E/expected-result.md). For example, after an automated [test case](../T/test-case.md) inserts a record, a query can confirm the data is present:

  ```
  SELECT * FROM users WHERE username = 'testuser';
  ```
  **Aggregate functions** like `COUNT`, `SUM`, `AVG`, `MIN`, and `MAX` are useful for validating calculations and summaries:

  ```
  SELECT COUNT(*) FROM orders WHERE order_date = '2023-01-01';
  ```
  **Joins** can validate relationships between tables, ensuring foreign keys and linked data are consistent:

  ```
  SELECT * FROM orders
  JOIN customers ON orders.customer_id = customers.id
  WHERE customers.email = 'example@test.com';
  ```
  **Subqueries** and **set operations** like `IN`, `EXISTS`, `UNION`, and `EXCEPT` can validate complex conditions and data sets:

  ```
  SELECT id FROM products WHERE price > (SELECT AVG(price) FROM products);
  ```
  For **consistency checks**, `TRANSACTION` control with `ROLLBACK` can be used to verify transactional behavior without affecting the actual data:

  ```
  BEGIN TRANSACTION;
  UPDATE account_balance SET balance = balance - 100 WHERE account_id = 1;
  SELECT balance FROM account_balance WHERE account_id = 1;
  ROLLBACK;
  ```
  Automated tests can execute these queries and compare the results against expected outcomes, flagging any discrepancies for further investigation. This approach ensures that the [database](../D/database.md) behaves as intended, maintaining data quality and application reliability.

#### What is the role of SQL in backend testing?

  In backend testing, [SQL](../S/sql.md) plays a crucial role in **validating** and **manipulating** data within the [database](../D/database.md). [Test automation](../T/test-automation.md) engineers use [SQL](../S/sql.md) to:

  - **Verify data integrity**
    by executing queries that check if data is stored, updated, or deleted correctly after various operations.

  - **Set up and tear down [test data](../T/test-data.md)**
    by inserting, updating, or removing data to create the necessary preconditions for tests or to clean up after tests are completed.

  - **Test [database](../D/database.md) functions**
    , stored procedures, and triggers to ensure they work as expected when they manipulate data.

  - **Check business logic**
    that is implemented at the database level, such as complex queries or calculations that are part of stored procedures.

  - **Perform data-driven testing**
    by retrieving data sets from the database to be used as inputs for automated tests.

  - **Assess performance**
    by executing queries that are expected to return large data sets or that are particularly complex, to ensure they run within acceptable time frames.
  [SQL](../S/sql.md) queries are integrated into [test scripts](../T/test-script.md) or test harnesses to automate these checks. For example, after a web service call that should modify data, a subsequent [SQL](../S/sql.md) query might be run to confirm the change:

  ```
  SELECT * FROM Orders WHERE OrderID = 1234;
  ```
  This query would check if order `1234` has the expected values after the operation. By automating such [SQL](../S/sql.md) checks, testers can efficiently validate backend processes and ensure the reliability of the [database](../D/database.md) operations within the application.

  - **Verify data integrity**
    by executing queries that check if data is stored, updated, or deleted correctly after various operations.

  - **Set up and tear down [test data](../T/test-data.md)**
    by inserting, updating, or removing data to create the necessary preconditions for tests or to clean up after tests are completed.

  - **Test [database](../D/database.md) functions**
    , stored procedures, and triggers to ensure they work as expected when they manipulate data.

  - **Check business logic**
    that is implemented at the database level, such as complex queries or calculations that are part of stored procedures.

  - **Perform data-driven testing**
    by retrieving data sets from the database to be used as inputs for automated tests.

  - **Assess performance**
    by executing queries that are expected to return large data sets or that are particularly complex, to ensure they run within acceptable time frames.

#### How can SQL be used to test database connections?

  [SQL](../S/sql.md) can be instrumental in testing [database](../D/database.md) connections by executing simple queries to verify the connection's integrity and responsiveness. To test a [database](../D/database.md) connection, you typically perform the following steps:

  1. **Establish a connection**
    to the database using the appropriate connection string and credentials.

  2. **Execute a simple query**
    to ensure the connection is active. A common choice is the
    `SELECT`
    statement, which retrieves data from a single table without affecting the data.

  ```
  SELECT 1;
  ```

  1. **Check the query's result**
    . If the query returns the expected result (e.g., the number 1), the connection is considered successful.

  2. **Perform a cleanup**
    by closing the connection to avoid resource leaks.
  In [automated testing](../A/automated-testing.md) frameworks, these steps are encapsulated in a [test case](../T/test-case.md), and assertions are used to validate the connection. For instance, you might assert that the query returns a single row with the value 1.
  Additionally, you can test the connection's ability to handle more complex operations such as transactions, joins, or specific application queries to ensure the [database](../D/database.md) responds correctly under conditions that mimic the actual application use.
  Incorporating these [SQL](../S/sql.md)-based connection tests into your [test suite](../T/test-suite.md) ensures that any issues with [database](../D/database.md) connectivity are identified early in the development cycle, reducing the risk of production outages or performance issues.

  1. **Establish a connection**
    to the database using the appropriate connection string and credentials.

  2. **Execute a simple query**
    to ensure the connection is active. A common choice is the
    `SELECT`
    statement, which retrieves data from a single table without affecting the data.

  1. **Check the query's result**
    . If the query returns the expected result (e.g., the number 1), the connection is considered successful.

  2. **Perform a cleanup**
    by closing the connection to avoid resource leaks.

#### What are some common SQL queries used in software testing?

  In [software testing](../S/software-testing.md), [SQL](../S/sql.md) queries are essential for verifying the integrity and accuracy of data within a [database](../D/database.md). Here are some common [SQL](../S/sql.md) queries used:

  - **SELECT** with **assertions** to validate data:
    Use the result to assert the expected number of active users.

    ```
    SELECT COUNT(*) FROM users WHERE active = 1;
    ```

  - **JOIN** queries to validate relationships:
    Confirm that orders are correctly linked to customers.

    ```
    SELECT * FROM orders INNER JOIN customers ON orders.customer_id = customers.id;
    ```

  - **Data [setup](../S/setup.md)** for test preconditions:
    Create necessary data before [test execution](../T/test-execution.md).

    ```
    INSERT INTO products (name, price) VALUES ('Test Product', 9.99);
    ```

  - **Data cleanup** after tests:
    Remove obsolete data to maintain [test environment](../T/test-environment.md).

    ```
    DELETE FROM temporary_data WHERE created_at < CURRENT_TIMESTAMP - INTERVAL '1 hour';
    ```

  - **Checking constraints** and **business rules**:
    Ensure there are no duplicate usernames, which may violate a uniqueness constraint.

    ```
    SELECT username FROM users GROUP BY username HAVING COUNT(*) > 1;
    ```

  - **Subqueries** for complex validations:
    Identify products that have never been ordered.

    ```
    SELECT name FROM products WHERE id NOT IN (SELECT product_id FROM order_details);
    ```

  - **Transactions** to test atomic operations:
    Verify that balance transfers are atomic and consistent.

    ```
    BEGIN TRANSACTION;
    UPDATE account_balance SET balance = balance - 100 WHERE account_id = 1;
    UPDATE account_balance SET balance = balance + 100 WHERE account_id = 2;
    COMMIT;
    ```
  These queries can be integrated into automated [test scripts](../T/test-script.md) to validate various aspects of the [database](../D/database.md) as part of a comprehensive testing strategy.

  - **SELECT** with **assertions** to validate data:
    Use the result to assert the expected number of active users.

    ```
    SELECT COUNT(*) FROM users WHERE active = 1;
    ```

  - **JOIN** queries to validate relationships:
    Confirm that orders are correctly linked to customers.

    ```
    SELECT * FROM orders INNER JOIN customers ON orders.customer_id = customers.id;
    ```

  - **Data [setup](../S/setup.md)** for test preconditions:
    Create necessary data before [test execution](../T/test-execution.md).

    ```
    INSERT INTO products (name, price) VALUES ('Test Product', 9.99);
    ```

  - **Data cleanup** after tests:
    Remove obsolete data to maintain [test environment](../T/test-environment.md).

    ```
    DELETE FROM temporary_data WHERE created_at < CURRENT_TIMESTAMP - INTERVAL '1 hour';
    ```

  - **Checking constraints** and **business rules**:
    Ensure there are no duplicate usernames, which may violate a uniqueness constraint.

    ```
    SELECT username FROM users GROUP BY username HAVING COUNT(*) > 1;
    ```

  - **Subqueries** for complex validations:
    Identify products that have never been ordered.

    ```
    SELECT name FROM products WHERE id NOT IN (SELECT product_id FROM order_details);
    ```

  - **Transactions** to test atomic operations:
    Verify that balance transfers are atomic and consistent.

    ```
    BEGIN TRANSACTION;
    UPDATE account_balance SET balance = balance - 100 WHERE account_id = 1;
    UPDATE account_balance SET balance = balance + 100 WHERE account_id = 2;
    COMMIT;
    ```
