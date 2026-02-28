# SQL

<!-- TOC START -->
- [相关术语：](#相关术语：)
  - [另请参阅：](#另请参阅：)
- [有关 SQL 的问题吗？](#有关-sql-的问题吗？)
  - [基础知识和重要性](#基础知识和重要性)
    - [什么是 SQL，为什么它很重要？](#什么是-sql，为什么它很重要？)
    - [SQL 命令有哪些不同类型？](#sql-命令有哪些不同类型？)
    - [SQL 和 NoSQL 有什么区别？](#sql-和-nosql-有什么区别？)
    - [SQL 中的关系数据库是什么？](#sql-中的关系数据库是什么？)
    - [简单的 SQL 查询有哪些基本操作？](#简单的-sql-查询有哪些基本操作？)
  - [SQL 语法和查询](#sql-语法和查询)
    - [SQL 创建表的语法是什么？](#sql-创建表的语法是什么？)
    - [如何在 SQL 中向表中插入数据？](#如何在-sql-中向表中插入数据？)
    - [如何在 SQL 中更新表中的数据？](#如何在-sql-中更新表中的数据？)
    - [SQL 中 SELECT 语句的用途是什么？](#sql-中-select-语句的用途是什么？)
    - [如何在 SQL 中删除表中的数据？](#如何在-sql-中删除表中的数据？)
    - [SQL 中的 WHERE 和 HAVING 子句有什么区别？](#sql-中的-where-和-having-子句有什么区别？)
  - [高级 SQL 概念](#高级-sql-概念)
    - [什么是 SQL 连接以及 SQL 中的连接有哪些不同类型？](#什么是-sql-连接以及-sql-中的连接有哪些不同类型？)
    - [什么是 SQL 视图以及如何使用它们？](#什么是-sql-视图以及如何使用它们？)
    - [什么是 SQL 索引以及它们为何如此重要？](#什么是-sql-索引以及它们为何如此重要？)
    - [什么是 SQL 触发器以及如何使用它们？](#什么是-sql-触发器以及如何使用它们？)
    - [什么是 SQL 注入以及如何防止它？](#什么是-sql-注入以及如何防止它？)
  - [用于测试的 SQL](#用于测试的-sql)
    - [SQL如何用于软件测试？](#sql如何用于软件测试？)
    - [如何使用 SQL 查询来验证数据？](#如何使用-sql-查询来验证数据？)
    - [SQL在后端测试中的作用是什么？](#sql在后端测试中的作用是什么？)
    - [如何使用SQL来测试数据库连接？](#如何使用sql来测试数据库连接？)
    - [软件测试中常用的 SQL 查询有哪些？](#软件测试中常用的-sql-查询有哪些？)
<!-- TOC END -->

SQL

（结构化查询语言）是一种标准化编程语言，专门用于管理和操作关系型数据库

数据库

。

SQL

用于执行查询数据、更新数据、插入数据、删除数据等任务

数据库

。它还涉及创建和修改模式（

数据库

结构）并控制对数据的访问。

SQL

为关系提供一致的接口

数据库

管理系统 (RDBMS)，并受到大多数现代 RDBMS 平台的支持，例如 MySQL、PostgreSQL、

SQL

服务器、Oracle 等等。通过

SQL

，用户可以定义、检索和操作数据

数据库

高效且有效。

## 相关术语：

- [Database](../D/database.md)

### 另请参阅：

- [Wikipedia](https://en.wikipedia.org/wiki/SQL)

## 有关 SQL 的问题吗？

### 基础知识和重要性

#### 什么是 SQL，为什么它很重要？

[SQL](../S/sql.md)，或**结构化查询语言**，是一种标准化编程语言，用于管理和操作关系[databases](../D/database.md)。它很重要，因为它提供了一种系统的方法来创建、检索、更新和删除 [databases](../D/database.md) 中的数据，这是大多数软件应用程序不可或缺的一部分。
  在**软件[test automation](../T/test-automation.md)**的背景下，[SQL](../S/sql.md)在验证数据的状态和完整性方面发挥着至关重要的作用，这直接影响被测应用程序的可靠性。 [Test automation](../T/test-automation.md) 工程师使用[SQL](../S/sql.md) 来：

- 验证数据操作操作（例如插入、更新和删除）是否已正确执行。
  - 设置和拆除测试数据，确保测试在已知状态下运行。
  - 验证涉及数据检索和操作的业务逻辑，确保应用程序按预期运行。
  - 执行后端测试以确保应用程序与数据库正确交互，包括事务和并发的处理。
  - 检查数据完整性和约束，以确保数据库在不同的测试场景中保持有效状态。
  [SQL](../S/sql.md) 是[test automation](../T/test-automation.md) 工程师的一项关键技能，因为它使他们能够绕过用户界面直接与[database](../D/database.md) 交互。这允许对与[database](../D/database.md)交互的应用程序层进行更彻底的测试，并创建更复杂的[test scenarios](../T/test-scenario.md)，通过UI复制可能会很困难或耗时。

- 验证数据操作操作（例如插入、更新和删除）是否已正确执行。
  - 设置和拆除测试数据，确保测试在已知状态下运行。
  - 验证涉及数据检索和操作的业务逻辑，确保应用程序按预期运行。
  - 执行后端测试以确保应用程序与数据库正确交互，包括事务和并发的处理。
  - 检查数据完整性和约束，以确保数据库在不同的测试场景中保持有效状态。

#### SQL 命令有哪些不同类型？

[SQL](../S/sql.md) 命令可大致分为四种类型：

1. **数据定义语言 (DDL)**：这些命令定义[database](../D/database.md) 的结构并操作[database](../D/database.md) 对象，例如表、索引和视图。
    - `CREATE` ：创建新的数据库对象。
    - `ALTER` ：修改现有数据库对象。
    - `DROP` ：删除数据库对象。
    - `TRUNCATE` ：从表中删除所有记录，包括为记录分配的所有空间。
    - `CREATE` ：创建新的数据库对象。
    - `ALTER` ：修改现有数据库对象。
    - `DROP` ：删除数据库对象。
    - `TRUNCATE` ：从表中删除所有记录，包括为记录分配的所有空间。
  2. **数据操作语言 (DML)**：这些命令处理 [database](../D/database.md) 中存在的数据的操作。
    - `INSERT` ：将新数据添加到表中。
    - `UPDATE` ：修改表中的现有数据。
    - `DELETE` ：从表中删除数据。
    - `INSERT` ：将新数据添加到表中。
    - `UPDATE` ：修改表中的现有数据。
    - `DELETE` ：从表中删除数据。
  3. **数据控制语言（DCL）**：这些命令与[database](../D/database.md)系统的权限、权限和其他控制相关。
    - `GRANT` ：授予用户对数据库的访问权限。
    - `REVOKE` ：撤回使用 GRANT 命令授予的用户访问权限。
    - `GRANT` ：授予用户对数据库的访问权限。
    - `REVOKE` ：撤回使用 GRANT 命令授予的用户访问权限。
  4. **事务控制语言(TCL)**：这些命令处理[database](../D/database.md) 内的事务操作。
    - `COMMIT` ：将所有事务保存到数据库。
    - `ROLLBACK` ：将数据库恢复到上次提交的状态。
    - `SAVEPOINT` ：在事务中设置保存点。
    - `SET TRANSACTION` ：在事务上放置名称。
    - `COMMIT` ：将所有事务保存到数据库。
    - `ROLLBACK` ：将数据库恢复到上次提交的状态。
    - `SAVEPOINT` ：在事务中设置保存点。
    - `SET TRANSACTION` ：在事务上放置名称。
  了解这些命令对于[database](../D/database.md) 操作和管理至关重要，这在[test automation](../T/test-automation.md) 中通常是必要的，以确保应用程序与[database](../D/database.md) 正确交互。

1. **数据定义语言 (DDL)**：这些命令定义[database](../D/database.md) 的结构并操作[database](../D/database.md) 对象，例如表、索引和视图。
    - `CREATE` ：创建新的数据库对象。
    - `ALTER` ：修改现有数据库对象。
    - `DROP` ：删除数据库对象。
    - `TRUNCATE` ：从表中删除所有记录，包括为记录分配的所有空间。
    - `CREATE` ：创建新的数据库对象。
    - `ALTER` ：修改现有数据库对象。
    - `DROP` ：删除数据库对象。
    - `TRUNCATE` ：从表中删除所有记录，包括为记录分配的所有空间。
  2. **数据操作语言 (DML)**：这些命令处理 [database](../D/database.md) 中存在的数据的操作。
    - `INSERT` ：将新数据添加到表中。
    - `UPDATE` ：修改表中的现有数据。
    - `DELETE` ：从表中删除数据。
    - `INSERT` ：将新数据添加到表中。
    - `UPDATE` ：修改表中的现有数据。
    - `DELETE` ：从表中删除数据。
  3. **数据控制语言（DCL）**：这些命令与[database](../D/database.md)系统的权利、权限和其他控制相关。
    - `GRANT` ：授予用户对数据库的访问权限。
    - `REVOKE` ：撤回使用 GRANT 命令授予的用户访问权限。
    - `GRANT` ：授予用户对数据库的访问权限。
    - `REVOKE` ：撤消使用 GRANT 命令授予的用户访问权限。
  4. **事务控制语言(TCL)**：这些命令处理[database](../D/database.md) 内的事务操作。
    - `COMMIT` ：将所有事务保存到数据库。
    - `ROLLBACK` ：将数据库恢复到上次提交的状态。
    - `SAVEPOINT` ：在事务中设置保存点。
    - `SET TRANSACTION` ：在事务上放置名称。
    - `COMMIT` ：将所有事务保存到数据库。
    - `ROLLBACK` ：将数据库恢复到上次提交的状态。
    - `SAVEPOINT` ：在事务中设置保存点。
    - `SET TRANSACTION` ：在事务上放置名称。

#### SQL 和 NoSQL 有什么区别？

[SQL](../S/sql.md)（结构化查询语言）[databases](../D/database.md)，也称为**关系[databases](../D/database.md)**，使用行和列将数据存储在具有预定义架构的表中。它们在 **ACID 事务**（原子性、一致性、隔离性、持久性）方面表现出色，并通过 **JOIN 操作**支持复杂查询。
  NoSQL（不仅仅是[SQL](../S/sql.md)）[databases](../D/database.md) 专为分布式数据存储而设计，并考虑到**水平扩展**。它们不需要固定模式，可以存储非结构化数据，例如文档、键值对、宽列存储或图形。通常选择 NoSQL [databases](../D/database.md) 是因为它们能够通过**灵活的数据模型**处理**大量数据**和**高流量负载**。
  主要区别是：

- **模式灵活性**：NoSQL 数据库允许灵活的动态模式，而 SQL 数据库需要预定义模式。
  - **扩展**：NoSQL 数据库通常设计为通过在多个服务器之间分布数据来扩展，而 SQL 数据库则通过增加现有硬件的功能来扩展。
  - **数据模型**：SQL 数据库是基于表的，而 NoSQL 数据库可以是面向文档的、键值对、宽列存储或图形数据库。
  - **事务**：SQL 数据库支持复杂事务并且符合 ACID，使其适合需要可靠性和一致性的应用程序。 NoSQL 数据库可以提供最终一致性并优先考虑可用性和分区容错性（遵循 CAP 定理）。
  - **查询语言** ：SQL数据库使用SQL语言进行查询，对于复杂查询来说功能强大。 NoSQL 数据库具有多种查询语言，这些语言通常不太复杂，并且可能不支持 JOIN 操作或多记录 ACID 事务。
  - **模式灵活性**：NoSQL 数据库允许灵活的动态模式，而 SQL 数据库需要预定义模式。
  - **扩展**：NoSQL 数据库通常设计为通过在多个服务器之间分布数据来扩展，而 SQL 数据库则通过增加现有硬件的功能来扩展。
  - **数据模型**：SQL 数据库是基于表的，而 NoSQL 数据库可以是面向文档的、键值对、宽列存储或图形数据库。
  - **事务**：SQL 数据库支持复杂事务并且符合 ACID，使其适合需要可靠性和一致性的应用程序。 NoSQL 数据库可以提供最终一致性并优先考虑可用性和分区容错性（遵循 CAP 定理）。
  - **查询语言** ：SQL数据库使用SQL语言进行查询，对于复杂查询来说功能强大。 NoSQL 数据库具有多种查询语言，这些语言通常不太复杂，并且可能不支持 JOIN 操作或多记录 ACID 事务。

#### SQL 中的关系数据库是什么？

**关系[database](../D/database.md)** 是组织为一组正式描述的表的数据项的集合，可以通过各种方式访问​​或重新组装其中的数据，而无需重新组织[database](../D/database.md) 表。关系模型意味着逻辑数据结构（数据表、视图和索引）与物理存储结构分开。该模型基于**一阶谓词逻辑**，其核心思想是将[database](../D/database.md)描述为有限谓词变量集上的谓词集合，描述对可能值和值组合的约束。
  关系[database](../D/database.md) 的关键元素是**表**（或关系），其中数据存储在行和列中。每个表都有一个唯一的主键，用于标识行。表可以通过**外键**相互关联，外键是引用另一个表中主键的字段。
  关系[databases](../D/database.md) 使用**结构化查询语言 ([SQL](../S/sql.md))** 来定义和操作数据。这是非常强大的，因为它允许轻松访问数据，并且还用于使用约束（例如 UNIQUE、NOT NULL、CHECK、FOREIGN KEY）维护 [database](../D/database.md) 的完整性。
  在 [test automation](../T/test-automation.md) 上下文中，关系 [databases](../D/database.md) 通常是应用程序的后端，理解它们的结构对于验证应用程序是否正确存储和检索数据至关重要。 [Test automation](../T/test-automation.md) 工程师可以编写[SQL](../S/sql.md) 查询来提取数据并使用它来验证应用程序行为或设置测试前提条件。

#### 简单的 SQL 查询有哪些基本操作？

简单的 [SQL](../S/sql.md) 查询执行的基本操作包括：

- **选择**
    数据与
    `SELECT`：

    ```
    SELECT column1, column2 FROM table_name;
    ```

- **过滤**
    数据使用
    `WHERE`：

    ```
    SELECT * FROM table_name WHERE condition;
    ```

- **排序**
    结果与
    `ORDER BY`：

    ```
    SELECT * FROM table_name ORDER BY column ASC|DESC;
    ```

- **限制**
    结果使用
    `LIMIT`：

    ```
    SELECT * FROM table_name LIMIT number;
    ```

- **分组**
    数据与
    `GROUP BY`
    对于聚合函数：

    ```
    SELECT COUNT(column1), column2 FROM table_name GROUP BY column2;
    ```

- **结合**
    多个表中的列使用
    `JOIN`：

    ```
    SELECT * FROM table1 INNER JOIN table2 ON table1.column_name = table2.column_name;
    ```

- **计算**
    具有内置函数的值，例如
    `SUM()`
    ,
    `AVG()`
    ,
    `MIN()`
    ,
    `MAX()`：

    ```
    SELECT AVG(column1) FROM table_name;
    ```

- **别名**
    列或表的可读性
    `AS`：

    ```
    SELECT column1 AS alias_name FROM table_name;
    ```

- **插入**
    新数据与
    `INSERT INTO`：

    ```
    INSERT INTO table_name (column1, column2) VALUES (value1, value2);
    ```

- **更新**
    现有数据与
    `UPDATE`：

    ```
    UPDATE table_name SET column1 = value1 WHERE condition;
    ```

- **删除**
    数据与
    `DELETE`：

    ```
    DELETE FROM table_name WHERE condition;
    ```这些操作是与 [database](../D/database.md) 内的数据进行交互和操作的基础。

- **选择**
    数据与
    `SELECT`：

    ```
    SELECT column1, column2 FROM table_name;
    ```

- **过滤**
    数据使用
    `WHERE`：

    ```
    SELECT * FROM table_name WHERE condition;
    ```

- **排序**
    结果与
    `ORDER BY`：

    ```
    SELECT * FROM table_name ORDER BY column ASC|DESC;
    ```

- **限制**
    结果使用
    `LIMIT`：

    ```
    SELECT * FROM table_name LIMIT number;
    ```

- **分组**
    数据与
    `GROUP BY`
    对于聚合函数：

    ```
    SELECT COUNT(column1), column2 FROM table_name GROUP BY column2;
    ```

- **结合**
    多个表中的列使用
    `JOIN`：

    ```
    SELECT * FROM table1 INNER JOIN table2 ON table1.column_name = table2.column_name;
    ```

- **计算**
    具有内置函数的值，例如
    `SUM()`
    ,
    `AVG()`
    ,
    `MIN()`
    ,
    `MAX()`：

    ```
    SELECT AVG(column1) FROM table_name;
    ```

- **别名**
    列或表的可读性
    `AS`：

    ```
    SELECT column1 AS alias_name FROM table_name;
    ```

- **插入**
    新数据与
    `INSERT INTO`：

    ```
    INSERT INTO table_name (column1, column2) VALUES (value1, value2);
    ```

- **更新**
    现有数据与
    `UPDATE`：

    ```
    UPDATE table_name SET column1 = value1 WHERE condition;
    ```

- **删除**
    数据与
    `DELETE`：

    ```
    DELETE FROM table_name WHERE condition;
    ```

### SQL 语法和查询

#### SQL 创建表的语法是什么？

要在 [SQL](../S/sql.md) 中创建表，请使用 `CREATE TABLE` 语句，后跟表名和列列表，括号内包含各自的数据类型和约束。每个列定义均以逗号分隔。这是基本语法：

  ```
  CREATE TABLE table_name (
      column1 datatype constraint,
      column2 datatype constraint,
      column3 datatype constraint,
      ...
  );
  ```例如，创建一个名为`users`的表，该表包含`id`、`name`和`email`三列，其中`id`是一个自增整数，作为主键，`name`是一个最大长度为50个字符的可变字符串，`email`是一个可变字符串最大长度为 100 个字符，[SQL](../S/sql.md) 语句将是：

  ```
  CREATE TABLE users (
      id INT AUTO_INCREMENT PRIMARY KEY,
      name VARCHAR(50),
      email VARCHAR(100)
  );
  ```请记住为表定义**主键**，它唯一标识每条记录。如果需要，您还可以指定其他约束，例如 `NOT NULL`、`UNIQUE`、`CHECK`、`FOREIGN KEY` 等，以强制数据完整性。

#### 如何在 SQL 中向表中插入数据？

要将数据插入[SQL](../S/sql.md) 中的表中，请使用`INSERT INTO` 语句。指定表，然后定义要插入的列和值。如果要为表中的所有列插入值，则可以省略列名称，而仅按照与表架构中的列相同的顺序提供值。
  以下是向表中插入数据的基本语法：

  ```
  INSERT INTO table_name (column1, column2, column3, ...)
  VALUES (value1, value2, value3, ...);
  ```例如，如果您有一个名为 `users` 的表，其中包含 `id`、`name` 和 `email` 列，则可以像这样插入新行：

  ```
  INSERT INTO users (id, name, email)
  VALUES (1, 'John Doe', 'john.doe@example.com');
  ```如果您一次插入多行，请用逗号分隔每组值：

  ```
  INSERT INTO users (id, name, email)
  VALUES
  (1, 'John Doe', 'john.doe@example.com'),
  (2, 'Jane Smith', 'jane.smith@example.com');
  ```请记住对字符串值使用单引号并转义任何特殊字符以防止 [SQL](../S/sql.md) 注入攻击。对于数值，不需要引号。使用动态数据时始终验证和清理输入，以防止恶意 [SQL](../S/sql.md) 注入。

#### 如何在 SQL 中更新表中的数据？

要更新[SQL](../S/sql.md) 表中的数据，请使用`UPDATE` 语句。指定表并为一列或多列设置新值，通常使用 `WHERE` 子句来定位特定行。这是基本语法：

  ```
  UPDATE table_name
  SET column1 = value1, column2 = value2, ...
  WHERE condition;
  ```**示例**：假设您有一个 `users` 表，并且您想要更新 `id` 为 10 的用户的电子邮件。

  ```
  UPDATE users
  SET email = 'newemail@example.com'
  WHERE id = 10;
  ```**最佳实践**：

- 始终使用
    `WHERE`
    子句以避免无意中更新所有行。

- 测试你的
    `WHERE`
    条款与
    `SELECT`
    首先声明以确保您定位到正确的行。

- 如果您的数据库支持事务，请使用事务，以便在出现错误时回滚更改。
  - 对于复杂的条件，考虑使用子查询
    `WHERE`
    条款。

- 当根据不同条件更新多行时，可以使用
    `CASE`
    内的声明
    `SET`
    条款。
  **注意**：在[test automation](../T/test-automation.md) 中，确保您的[test data](../T/test-data.md) 已​​备份或可以在运行更新查询之前轻松恢复，因为它们会修改数据状态。

- 始终使用
    `WHERE`
    子句以避免无意中更新所有行。

- 测试你的
    `WHERE`
    条款与
    `SELECT`
    首先声明以确保您定位到正确的行。

- 如果您的数据库支持事务，请使用事务，以便在出现错误时回滚更改。
  - 对于复杂的条件，考虑使用子查询
    `WHERE`
    条款。

- 当根据不同条件更新多行时，可以使用
    `CASE`
    内的声明
    `SET`
    条款。

#### SQL 中 SELECT 语句的用途是什么？

[SQL](../S/sql.md) 中的`SELECT` 语句用于从[database](../D/database.md) 中的一个或多个表**检索数据**。它允许您指定要获取的确切列，以及选择行的任何条件。 `SELECT` 语句对于[test automation](../T/test-automation.md) 工程师**验证数据状态**、确保被测应用程序正确操作数据至关重要。
  以下是 `SELECT` 语句的基本示例：

  ```
  SELECT column1, column2 FROM table_name WHERE condition;
  ```在[test automation](../T/test-automation.md) 中，您可以使用`SELECT` 来：

- 验证新记录的插入。
  - 检查现有记录的更新。
  - 确认删除记录。
  - 通过检查数据是否满足某些条件来验证业务逻辑。
  - 提取数据用作自动化测试用例的输入。
  例如，在插入一条记录的 [test case](../T/test-case.md) 之后，您可以使用：

  ```
  SELECT * FROM users WHERE username = 'testuser';
  ```此查询检查“testuser”是否已成功添加到`users` 表中。 `SELECT`语句用途广泛，可以与其他[SQL](../S/sql.md)子句和函数组合来执行复杂的数据验证，使其成为后端测试不可或缺的工具。

- 验证新记录的插入。
  - 检查现有记录的更新。
  - 确认删除记录。
  - 通过检查数据是否满足某些条件来验证业务逻辑。
  - 提取数据用作自动化测试用例的输入。

#### 如何在 SQL 中删除表中的数据？

要从 [SQL](../S/sql.md) 中的表**删除数据，请使用 `DELETE` 语句。使用`WHERE` 子句指定表以及应删除行的条件。如果没有 `WHERE` 子句，所有行都将被删除。
  这是基本语法：

  ```
  DELETE FROM table_name WHERE condition;
  ```例如，要删除 `id` 为 `10` 的记录：

  ```
  DELETE FROM Employees WHERE id = 10;
  ```**警告**：省略`WHERE`子句将删除表中的所有记录，如果没有备份，则无法撤消。
  对于[test automation](../T/test-automation.md)，您可以在测试运行后删除[test data](../T/test-data.md)：

  ```
  DELETE FROM Test_Results WHERE test_date < '2023-01-01';
  ```请务必在批量删除操作之前备份数据，并考虑 `BEGIN TRANSACTION`、`COMMIT` 和 `ROLLBACK` 等事务控制语句以确保安全。

#### SQL 中的 WHERE 和 HAVING 子句有什么区别？

[SQL](../S/sql.md) 中的`WHERE` 和`HAVING` 子句都用于过滤记录，但它们具有不同的用途并在查询处理的不同阶段操作。

- **WHERE** ：该子句用于过滤记录
    **之前**
    进行任何分组。它适用于表的各个行。你用
    `WHERE`
    指定要包含在结果集中的行必须满足的条件。

  ```
  SELECT column1, column2
  FROM table
  WHERE condition;
  ```

- **HAVING** ：该子句用于过滤行组
    **之后**
    的
    `GROUP BY`
    条款已被应用。当您想要将条件应用于组函数时，通常会使用它，例如
    `SUM()`
    ,
    `AVG()`
    ,
    `MAX()`
    等

  ```
  SELECT column1, SUM(column2)
  FROM table
  GROUP BY column1
  HAVING condition;
  ```本质上，如果您需要根据各个列值过滤行，请使用`WHERE`。如果需要过滤聚合函数的结果，请使用`HAVING`。请记住，`HAVING` 仅当 `GROUP BY` 存在时才能使用，而 `WHERE` 可以在没有 `GROUP BY` 的情况下使用。

- **WHERE** ：该子句用于过滤记录
    **之前**
    进行任何分组。它适用于表的各个行。你用
    `WHERE`
    指定要包含在结果集中的行必须满足的条件。

- **HAVING** ：该子句用于过滤行组
    **之后**
    的
    `GROUP BY`
    条款已被应用。当您想要将条件应用于组函数时，通常会使用它，例如
    `SUM()`
    ,
    `AVG()`
    ,
    `MAX()`
    等

### 高级 SQL 概念

#### 什么是 SQL 连接以及 SQL 中的连接有哪些不同类型？

[SQL](../S/sql.md) 连接用于根据两个或多个表之间的相关列来组合来自两个或多个表的行。连接有多种类型：

- **INNER JOIN** ：返回两个表中具有匹配值的记录。

  ```
  SELECT * FROM table1
  INNER JOIN table2
  ON table1.common_field = table2.common_field;
  ```

- **LEFT (OUTER) JOIN** ：返回左表中的所有记录以及右表中的匹配记录。如果没有匹配，则右侧结果为 NULL。

  ```
  SELECT * FROM table1
  LEFT JOIN table2
  ON table1.common_field = table2.common_field;
  ```

- **RIGHT (OUTER) JOIN** ：返回右表中的所有记录以及左表中的匹配记录。如果没有匹配，则结果左侧为 NULL。

  ```
  SELECT * FROM table1
  RIGHT JOIN table2
  ON table1.common_field = table2.common_field;
  ```

- **FULL (OUTER) JOIN** ：当左表或右表中有匹配项时返回所有记录。如果没有匹配，则不匹配的一侧的结果为 NULL。

  ```
  SELECT * FROM table1
  FULL OUTER JOIN table2
  ON table1.common_field = table2.common_field;
  ```

- **CROSS JOIN** ：返回两个表中行的所有可能组合。这种连接不需要连接条件，并且可以产生大量行。

  ```
  SELECT * FROM table1
  CROSS JOIN table2;
  ```

- **SELF JOIN** ：常规联接，但表与自身联接。

  ```
  SELECT * FROM table1 T1
  INNER JOIN table1 T2
  ON T1.common_field = T2.common_field;
  ```理解和利用这些连接对于在 [software testing](../S/software-testing.md) 期间查询复杂数据集和验证数据关系至关重要。

- **INNER JOIN** ：返回两个表中具有匹配值的记录。
  - **LEFT (OUTER) JOIN** ：返回左表中的所有记录以及右表中的匹配记录。如果没有匹配，则右侧结果为 NULL。
  - **RIGHT (OUTER) JOIN** ：返回右表中的所有记录以及左表中的匹配记录。如果没有匹配，则结果左侧为 NULL。
  - **FULL (OUTER) JOIN** ：当左表或右表中有匹配项时返回所有记录。如果没有匹配，则不匹配的一侧的结果为 NULL。
  - **CROSS JOIN** ：返回两个表中行的所有可能组合。这种连接不需要连接条件，并且可以产生大量行。
  - **SELF JOIN** ：常规联接，但表与自身联接。

#### 什么是 SQL 视图以及如何使用它们？

[SQL](../S/sql.md) 视图是代表一个或多个表中的数据子集的虚拟表。它们是使用 `CREATE VIEW` 语句创建的，可以使用联接、过滤器和聚合封装复杂的查询，以简化数据访问。
  视图用于：

- **限制对数据的访问**：通过提供特定的数据视图，可以对某些用户隐藏敏感信息。
  - **简化复杂查询**：视图可以存储复杂性并呈现简单的界面，而不是每次都编写冗长的 SQL 查询。
  - **增强可读性**：可以对视图进行描述性命名以传达它们所代表的数据，使 SQL 代码更易于理解。
  - **维护遗留代码**：如果基础表结构发生变化，视图可以提供一致的界面，而无需修改现有查询或应用程序。
  这是创建视图的示例：

  ```
  CREATE VIEW EmployeeSummary AS
  SELECT EmployeeID, FirstName, LastName, Department
  FROM Employees
  WHERE IsActive = 1;
  ```要查询视图，您可以使用 `SELECT` 语句，就像使用常规表一样：

  ```
  SELECT * FROM EmployeeSummary;
  ```请记住，视图并不物理存储数据；而是存储数据。它们每次查询时都会从基础表中获取数据。对基表中数据的更改会立即反映在视图中。但是，某些视图是可更新的，并且可用于修改基表中的数据，但受到某些约束。

- **限制对数据的访问**：通过提供特定的数据视图，可以对某些用户隐藏敏感信息。
  - **简化复杂查询**：视图可以存储复杂性并呈现简单的界面，而不是每次都编写冗长的 SQL 查询。
  - **增强可读性**：可以对视图进行描述性命名以传达它们所代表的数据，使 SQL 代码更易于理解。
  - **维护遗留代码**：如果基础表结构发生变化，视图可以提供一致的界面，而无需修改现有查询或应用程序。

#### 什么是 SQL 索引以及它们为何如此重要？

[SQL](../S/sql.md) 索引是[database](../D/database.md) 搜索引擎可用来加速数据检索的特殊查找表。简而言之，[SQL](../S/sql.md) 中的索引用于**快速定位和访问[database](../D/database.md) 表中的数据**。索引对于提高 **SELECT** 查询的性能特别重要，并且当您具有过滤排序数据的 **WHERE** 子句时也很有用。
  索引是在表的一列或多列上创建的。创建索引时，它会对指定列的值进行排序并将它们存储在数据结构中，通常是 B 树或哈希表。这意味着当执行查询时，[database](../D/database.md) 可以使用索引快速查找数据，而不是扫描整个表，这可能非常耗时，尤其是对于大型表。
  对于[test automation](../T/test-automation.md) 工程师来说，理解索引至关重要，因为：

- 他们可以显着地
    **减少时间**
    需要运行涉及数据验证或比较的测试。

- 它们有助于识别可以通过适当的索引来缓解的性能问题，从而确保应用程序能够良好地扩展。
  - 它们对于在测试中编写高效的 SQL 查询至关重要，这可以
    **减少负载**
    并最大限度地减少超时或测试执行缓慢的风险。
  但是，需要注意的是，虽然索引可以提高读取性能，但它们也可能**减慢写入操作**（INSERT、UPDATE、DELETE），因为只要修改索​​引列中的数据，就必须更新索引。因此，必须仔细考虑确定对哪些列建立索引，尤其是在频繁更新的[database](../D/database.md) 中。

- 他们可以显着地
    **减少时间**
    需要运行涉及数据验证或比较的测试。

- 它们有助于识别可以通过适当的索引来缓解的性能问题，从而确保应用程序能够良好地扩展。
  - 它们对于在测试中编写高效的 SQL 查询至关重要，这可以
    **减少负载**
    并最大限度地减少超时或测试执行缓慢的风险。

#### 什么是 SQL 触发器以及如何使用它们？

[SQL](../S/sql.md) 触发器是特殊类型的存储过程，当[database](../D/database.md) 中发生指定事件时自动执行或触发，例如表上的`INSERT`、`UPDATE` 或`DELETE` 操作。它们用于强制执行业务规则、维护数据完整性以及管理 [database](../D/database.md) 状态的更改，而无需手动干预。
  触发器可以定义为在触发事件之前或之后执行。例如：

- **BEFORE 触发器** ：在插入、更新或删除数据行之前执行任务。
  - **AFTER触发器** ：数据修改完成后执行。
  下面是一个触发器的简单示例，用于在表中更新记录后记录审核条目：

  ```
  CREATE TRIGGER AuditLogUpdate
  AFTER UPDATE ON Employees
  FOR EACH ROW
  BEGIN
     INSERT INTO AuditLog (ChangeType, TableName, ChangedBy, ChangeDate)
     VALUES ('UPDATE', 'Employees', CURRENT_USER(), NOW());
  END;
  ```在[test automation](../T/test-automation.md) 中，触发器可用于：

- **验证业务逻辑**：确保测试用例期间触发器强制执行业务规则。
  - **数据验证**：检查触发器是否通过防止无效数据操作来维护数据完整性。
  - **[Performance testing](../P/performance-testing.md)** ：评估触发器对数据库性能的影响。
  - **[Regression testing](../R/regression-testing.md)** ：确认新更改不会破坏现有触发器。
  应谨慎使用触发器，因为它们会带来复杂性并影响性能。 [Test automation](../T/test-automation.md) 工程师必须确保触发器按预期工作并且不会引入意外的副作用。

- **BEFORE 触发器** ：在插入、更新或删除数据行之前执行任务。
  - **AFTER触发器** ：数据修改完成后执行。
  - **验证业务逻辑**：确保测试用例期间触发器强制执行业务规则。
  - **数据验证**：检查触发器是否通过防止无效数据操作来维护数据完整性。
  - **[Performance testing](../P/performance-testing.md)** ：评估触发器对数据库性能的影响。
  - **[Regression testing](../R/regression-testing.md)** ：确认新更改不会破坏现有触发器。

#### 什么是 SQL 注入以及如何防止它？

[SQL](../S/sql.md) 注入是一种安全漏洞，攻击者可以通过应用程序的输入数据注入恶意[SQL](../S/sql.md) 代码来操纵[SQL](../S/sql.md) 查询。这可能会导致未经授权访问或操纵[database](../D/database.md) 数据。
  为了防止 [SQL](../S/sql.md) 注入：

- **使用准备好的语句（参数化查询）**：它们强制代码和数据之间的明确分离。例如，在 Java 中，您可以使用 `PreparedStatement` 对象。

    ```
    String query = "SELECT * FROM users WHERE username = ? AND password = ?";
    PreparedStatement ps = connection.prepareStatement(query);
    ps.setString(1, username);
    ps.setString(2, password);
    ```

- **使用存储过程**：它们封装[SQL](../S/sql.md)语句并将所有输入视为数据而不是可执行代码。
  - **验证输入**：严格验证用户输入的类型、长度、格式和范围。使用正则表达式或验证库。
  - **转义用户输入**：如果必须在 [SQL](../S/sql.md) 查询中包含用户输入，请确保转义特殊字符。但是，这不如准备好的语句安全，应尽可能避免。
  - **使用 ORM 库**：像 Hibernate 或实体框架这样的对象关系映射 (ORM) 库可以抽象 [SQL](../S/sql.md) 查询并使用它们自己的方法来防止注入。
  - **实施最小权限**：限制[database](../D/database.md)用户权限，以便在发生注入时将潜在损害降至最低。
  - **保持软件更新**：确保您的 [database](../D/database.md) 管理系统 (DBMS) 和任何相关软件均已安装最新的安全补丁。
  - **使用 Web 应用程序防火墙**：它们可以帮助检测和阻止 [SQL](../S/sql.md) 注入攻击。
  - **[Security Testing](../S/security-testing.md)**：使用 SQLMap 等工具或执行 [penetration testing](../P/penetration-testing.md) 定期测试您的应用程序是否存在 [SQL](../S/sql.md) 注入漏洞。
  - **使用准备好的语句（参数化查询）**：它们强制代码和数据之间的明确分离。例如，在 Java 中，您可以使用 `PreparedStatement` 对象。

    ```
    String query = "SELECT * FROM users WHERE username = ? AND password = ?";
    PreparedStatement ps = connection.prepareStatement(query);
    ps.setString(1, username);
    ps.setString(2, password);
    ```

- **使用存储过程**：它们封装[SQL](../S/sql.md)语句并将所有输入视为数据而不是可执行代码。
  - **验证输入**：严格验证用户输入的类型、长度、格式和范围。使用正则表达式或验证库。
  - **转义用户输入**：如果必须在 [SQL](../S/sql.md) 查询中包含用户输入，请确保转义特殊字符。但是，这不如准备好的语句安全，应尽可能避免。
  - **使用 ORM 库**：像 Hibernate 或实体框架这样的对象关系映射 (ORM) 库可以抽象 [SQL](../S/sql.md) 查询并使用它们自己的方法来防止注入。
  - **实施最小权限**：限制[database](../D/database.md)用户权限，以便在发生注入时将潜在损害降至最低。
  - **保持软件更新**：确保您的 [database](../D/database.md) 管理系统 (DBMS) 和任何相关软件均已安装最新的安全补丁。
  - **使用 Web 应用程序防火墙**：它们可以帮助检测和阻止 [SQL](../S/sql.md) 注入攻击。
  - **[Security Testing](../S/security-testing.md)**：使用 SQLMap 等工具或执行 [penetration testing](../P/penetration-testing.md) 定期测试您的应用程序是否存在 [SQL](../S/sql.md) 注入漏洞。

### 用于测试的 SQL

#### SQL如何用于软件测试？

[SQL](../S/sql.md) 是**软件[test automation](../T/test-automation.md)** 的组成部分，用于验证关系[databases](../D/database.md) 内数据的状态和完整性。它使测试人员能够：

- **验证结果**
    通过执行测试用例
    `SELECT`
    查询以检查数据操作是否会产生预期结果。

- **设置和拆除[test data](../T/test-data.md)**
    使用
    `INSERT`
    ,
    `UPDATE`
    , 和
    `DELETE`
    命令，确保测试在受控环境中运行。

- **测试 [database](../D/database.md) 函数、存储过程和触发器**
    通过调用它们并评估它们对数据的影响。

- **验证业务逻辑**
    通过运行涉及的复杂查询在数据库级别实现
    `JOIN`
    s、子查询和聚合函数。

- **检查约束和索引**
    确保它们按预期运行，这对于数据完整性和性能至关重要。

- **模拟用户交易**
    通过使用事务来测试事务完整性和并发性
    `BEGIN`
    ,
    `COMMIT`
    , 和
    `ROLLBACK`
    。

- **评估表现**
    查询和数据库操作，识别潜在的瓶颈或优化。
  自动[test scripts](../T/test-script.md) 通常包括[SQL](../S/sql.md) 查询来执行这些任务，并将结果与​​预期结果进行比较，以确定测试通过或失败状态。因此，[SQL](../S/sql.md) 在[test automation](../T/test-automation.md) 中的角色对于后端测试至关重要，确保应用程序与[database](../D/database.md) 层一起正确运行。

- **验证结果**
    通过执行测试用例
    `SELECT`
    查询以检查数据操作是否会产生预期结果。

- **设置和拆除[test data](../T/test-data.md)**
    使用
    `INSERT`
    ,
    `UPDATE`
    , 和
    `DELETE`
    命令，确保测试在受控环境中运行。

- **测试 [database](../D/database.md) 函数、存储过程和触发器**
    通过调用它们并评估它们对数据的影响。

- **验证业务逻辑**
    通过运行涉及的复杂查询在数据库级别实现
    `JOIN`
    s、子查询和聚合函数。

- **检查约束和索引**
    确保它们按预期运行，这对于数据完整性和性能至关重要。

- **模拟用户交易**
    通过使用事务来测试事务完整性和并发性
    `BEGIN`
    ,
    `COMMIT`
    , 和
    `ROLLBACK`
    。

- **评估表现**
    查询和数据库操作，识别潜在的瓶颈或优化。

#### 如何使用 SQL 查询来验证数据？

[SQL](../S/sql.md) 作为软件[test automation](../T/test-automation.md) 的一部分，查询对于**验证数据**很有帮助。通过执行特定的查询，测试人员可以验证数据操作操作（例如插入、更新和删除）是否已正确执行。
  对于**数据完整性检查**，可使用`SELECT` 语句来检索数据并确保其与[expected results](../E/expected-result.md) 匹配。例如，在自动 [test case](../T/test-case.md) 插入一条记录后，查询可以确认数据是否存在：

  ```
  SELECT * FROM users WHERE username = 'testuser';
  ```**聚合函数**，如 `COUNT`、`SUM`、`AVG`、`MIN` 和 `MAX` 对于验证计算和摘要很有用：

  ```
  SELECT COUNT(*) FROM orders WHERE order_date = '2023-01-01';
  ```**联接**可以验证表之间的关系，确保外键和链接数据一致：

  ```
  SELECT * FROM orders
  JOIN customers ON orders.customer_id = customers.id
  WHERE customers.email = 'example@test.com';
  ```**子查询**和**设置操作**，如 `IN`、`EXISTS`、`UNION` 和 `EXCEPT` 可以验证复杂的条件和数据集：

  ```
  SELECT id FROM products WHERE price > (SELECT AVG(price) FROM products);
  ```对于**一致性检查**，`TRANSACTION` 控制和 `ROLLBACK` 可用于验证事务行为而不影响实际数据：

  ```
  BEGIN TRANSACTION;
  UPDATE account_balance SET balance = balance - 100 WHERE account_id = 1;
  SELECT balance FROM account_balance WHERE account_id = 1;
  ROLLBACK;
  ```自动化测试可以执行这些查询并将结果与​​预期结果进行比较，标记任何差异以供进一步调查。此方法可确保[database](../D/database.md) 按预期运行，从而保持数据质量和应用程序可靠性。

#### SQL在后端测试中的作用是什么？

在后端测试中，[SQL](../S/sql.md) 在**验证**和**操作**[database](../D/database.md) 中的数据方面发挥着至关重要的作用。 [Test automation](../T/test-automation.md) 工程师使用 [SQL](../S/sql.md) 来：

- **验证数据完整性**
    通过执行查询来检查数据是否在各种操作后正确存储、更新或删除。

- **设置和拆除[test data](../T/test-data.md)**
    通过插入、更新或删除数据来为测试创建必要的先决条件或在测试完成后进行清理。

- **测试[database](../D/database.md)功能**
    、存储过程和触发器，以确保它们在操作数据时按预期工作。

- **检查业务逻辑**
    在数据库级别实现，例如作为存储过程一部分的复杂查询或计算。

- **执行数据驱动测试**
    通过从数据库检索数据集作为自动化测试的输入。

- **评估表现**
    通过执行预期返回大型数据集或特别复杂的查询，以确保它们在可接受的时间范围内运行。
  [SQL](../S/sql.md) 查询集成到[test scripts](../T/test-script.md) 或测试工具中以自动执行这些检查。例如，在应修改数据的 Web 服务调用之后，可能会运行后续 [SQL](../S/sql.md) 查询来确认更改：

  ```
  SELECT * FROM Orders WHERE OrderID = 1234;
  ```此查询将检查订单`1234` 操作后是否具有预期值。通过自动化此类[SQL](../S/sql.md) 检查，测试人员可以有效地验证后端进程并确保应用程序中[database](../D/database.md) 操作的可靠性。

- **验证数据完整性**
    通过执行查询来检查数据是否在各种操作后正确存储、更新或删除。

- **设置和拆除[test data](../T/test-data.md)**
    通过插入、更新或删除数据来为测试创建必要的先决条件或在测试完成后进行清理。

- **测试[database](../D/database.md)功能**
    、存储过程和触发器，以确保它们在操作数据时按预期工作。

- **检查业务逻辑**
    在数据库级别实现，例如作为存储过程一部分的复杂查询或计算。

- **执行数据驱动测试**
    通过从数据库检索数据集作为自动化测试的输入。

- **评估表现**
    通过执行预期返回大型数据集或特别复杂的查询，以确保它们在可接受的时间范围内运行。

#### 如何使用SQL来测试数据库连接？

[SQL](../S/sql.md) 通过执行简单查询来验证连接的完整性和响应能力，有助于测试 [database](../D/database.md) 连接。要测试 [database](../D/database.md) 连接，通常执行以下步骤：

1. **建立连接**
    使用适当的连接字符串和凭据连接到数据库。

2. **执行一个简单的查询**
    以确保连接处于活动状态。一个常见的选择是
    `SELECT`
    语句，从单个表中检索数据而不影响数据。

  ```
  SELECT 1;
  ```

1. **检查查询结果**
    。如果查询返回预期结果（例如数字1），则认为连接成功。

2. **执行清理**
    通过关闭连接来避免资源泄漏。
  在[automated testing](../A/automated-testing.md) 框架中，这些步骤封装在[test case](../T/test-case.md) 中，并使用断言来验证连接。例如，您可以断言查询返回值为 1 的单行。
  此外，您还可以测试连接处理更复杂操作（例如事务、联接或特定应用程序查询）的能力，以确保 [database](../D/database.md) 在模拟实际应用程序使用的条件下正确响应。
  将这些基于 [SQL](../S/sql.md) 的连接测试合并到 [test suite](../T/test-suite.md) 中可确保在开发周期的早期识别 [database](../D/database.md) 连接的任何问题，从而降低生产中断或性能问题的风险。

1. **建立连接**
    使用适当的连接字符串和凭据连接到数据库。

2. **执行一个简单的查询**
    以确保连接处于活动状态。一个常见的选择是
    `SELECT`
    语句，从单个表中检索数据而不影响数据。

1. **检查查询结果**
    。如果查询返回预期结果（例如数字1），则认为连接成功。

2. **执行清理**
    通过关闭连接来避免资源泄漏。

#### 软件测试中常用的 SQL 查询有哪些？

在[software testing](../S/software-testing.md) 中，[SQL](../S/sql.md) 查询对于验证[database](../D/database.md) 中数据的完整性和准确性至关重要。以下是一些常用的 [SQL](../S/sql.md) 查询：

- **SELECT** 和 **assertions** 来验证数据：
    使用结果来断言预期的活跃用户数。

    ```
    SELECT COUNT(*) FROM users WHERE active = 1;
    ```

- **JOIN** 查询来验证关系：
    确认订单已正确链接到客户。

    ```
    SELECT * FROM orders INNER JOIN customers ON orders.customer_id = customers.id;
    ```

- **数据[setup](../S/setup.md)** 用于测试先决条件：
    在[test execution](../T/test-execution.md)之前创建必要的数据。

    ```
    INSERT INTO products (name, price) VALUES ('Test Product', 9.99);
    ```

- 测试后**数据清理**：
    删除过时的数据以维护[test environment](../T/test-environment.md)。

    ```
    DELETE FROM temporary_data WHERE created_at < CURRENT_TIMESTAMP - INTERVAL '1 hour';
    ```

- **检查约束**和**业务规则**：
    确保没有重复的用户名，这可能违反唯一性约束。

    ```
    SELECT username FROM users GROUP BY username HAVING COUNT(*) > 1;
    ```

- 用于复杂验证的**子查询**：
    识别从未订购过的产品。

    ```
    SELECT name FROM products WHERE id NOT IN (SELECT product_id FROM order_details);
    ```

- **事务**来测试原子操作：
    验证余额转移是原子的且一致的。

    ```
    BEGIN TRANSACTION;
    UPDATE account_balance SET balance = balance - 100 WHERE account_id = 1;
    UPDATE account_balance SET balance = balance + 100 WHERE account_id = 2;
    COMMIT;
    ```这些查询可以集成到自动化[test scripts](../T/test-script.md) 中，以验证[database](../D/database.md) 的各个方面，作为综合测试策略的一部分。

- **SELECT** 和 **assertions** 来验证数据：
    使用结果来断言预期的活跃用户数。

    ```
    SELECT COUNT(*) FROM users WHERE active = 1;
    ```

- **JOIN** 查询来验证关系：
    确认订单已正确链接到客户。

    ```
    SELECT * FROM orders INNER JOIN customers ON orders.customer_id = customers.id;
    ```

- **数据[setup](../S/setup.md)** 用于测试先决条件：
    在[test execution](../T/test-execution.md)之前创建必要的数据。

    ```
    INSERT INTO products (name, price) VALUES ('Test Product', 9.99);
    ```

- 测试后**数据清理**：
    删除过时的数据以维护[test environment](../T/test-environment.md)。

    ```
    DELETE FROM temporary_data WHERE created_at < CURRENT_TIMESTAMP - INTERVAL '1 hour';
    ```

- **检查约束**和**业务规则**：
    确保没有重复的用户名，这可能违反唯一性约束。

    ```
    SELECT username FROM users GROUP BY username HAVING COUNT(*) > 1;
    ```

- 用于复杂验证的**子查询**：
    识别从未订购过的产品。

    ```
    SELECT name FROM products WHERE id NOT IN (SELECT product_id FROM order_details);
    ```

- **事务**来测试原子操作：
    验证余额转移是原子的且一致的。

    ```
    BEGIN TRANSACTION;
    UPDATE account_balance SET balance = balance - 100 WHERE account_id = 1;
    UPDATE account_balance SET balance = balance + 100 WHERE account_id = 2;
    COMMIT;
    ```
