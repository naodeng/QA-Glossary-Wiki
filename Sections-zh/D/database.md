# 数据库 (Database)
[数据库](#数据库)

### 相关术语：
- **SQL**

### 参见：
- [维基百科](https://en.wikipedia.org/wiki/Database)

---

## 关于数据库的问题？

#### 基础与重要性

- **什么是数据库？**
**数据库 (Database)** 是以电子方式存储和访问的结构化数据集合。它作为数据的存储库，可以使用专用软件进行查询和操作。在**测试自动化**的上下文中，数据库通常用于存储**测试数据**、结果和配置，以便进行高效的检索和分析。
数据库可以是**集中式**或**分布式**的，可以部署在本地或云端。它们对于跨测试运行持久化状态、支持数据驱动测试策略以及为验证应用程序行为提供“真理来源”至关重要。
对于测试自动化工程师，与数据库的交互通常包括：
    - 使用连接字符串或 API 建立连接。
    - 执行查询以获取或操作数据。
    - 利用事务确保数据完整性。
    - 实施清理程序以维持一致的测试环境。

SQL 查询示例：
```sql
SELECT * FROM Users WHERE IsActive = 1;
```

Python 连接示例：
```python
import pymysql.cursors

# 连接到数据库
connection = pymysql.connect(host='localhost',
                             user='user',
                             password='passwd',
                             db='db',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        # 执行查询
        sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
        cursor.execute(sql, ('webmaster@python.org',))
        result = cursor.fetchone()
        print(result)
finally:
    connection.close()
```

- **为什么数据库在软件开发中很重要？**
数据库是应用的核心，用于高效存储、检索和管理数据。在**测试自动化**中，其关键作用包括：
    - **测试数据管理**：为自动化测试提供各种数据集，实现系统化管理。
    - **结果存储**：存储历史测试结果用于分析、趋势检查和报告生成。
    - **环境配置**：存储不同测试环境的配置。
    - **Mock 与存根 (Stubs)**：模拟外部系统，提供受控数据集。
    - **性能测试**：数据库往往是负载和压力测试的对象，以确保其能处理并发和大数据量。
    - **CI/CD 集成**：通过自动化测试确保代码更改不破坏现有功能。

- **数据库有哪些不同类型？**
    - **关系型数据库 (Relational)**：使用 SQL，以行/表结构存储。如 MySQL, PostgreSQL, Oracle。
    - **NoSQL 数据库**：非结构化，不要求固定模式。包括：
        - **键值存储 (Key-Value)**：如 Redis, DynamoDB。
        - **文档存储 (Document)**：如 MongoDB, Couchbase。
        - **列族存储 (Column Stores)**：如 Cassandra, HBase。
        - **图数据库 (Graph)**：如 Neo4j。
    - **内存数据库**：数据保存在 RAM 中，低延迟。如 SAP HANA。
    - **对象导向数据库**。
    - **时序数据库 (Time Series)**：针对带时间戳的数据优化，如 InfluxDB。
    - **NewSQL**：结合 NoSQL 的可扩展性和 RDBMS 的 ACID 保证。

- **关系型数据库与非关系型数据库的区别？**
    - **关系型 (SQL)**：表格化、预定义模式、ACID 兼容，适合复杂查询。
    - **非关系型 (NoSQL)**：格式多样、模式灵活、高扩展性，适合大规模非结构化数据，通常提供最终一致性。
    - **核心区别**：SQL 向上扩展（增加硬件能力），NoSQL 向外扩展（增加服务器数量）。

#### 数据库管理系统 (DBMS)

- **什么是 DBMS？**
**数据库管理系统 (DBMS)** 是用于创建、管理和与数据库交互的软件套件。它是用户与数据库之间的中介，负责**数据存储、检索、更新和管理**。
关键功能：
    - **并发控制**：多用户同时操作。
    - **数据完整性与安全**。
    - **备份与恢复**。
对于测试工程师，熟悉 DBMS 有助于测试数据设置、结果验证和识别性能瓶颈。

- **流行的 DBMS 软件有哪些？**
    - **Oracle Database**：功能丰富，面向企业。
    - **MySQL**：开源关系型，广泛用于 Web 开发。
    - **Microsoft SQL Server**。
    - **PostgreSQL**：开源、对象关系型，强调扩展性。
    - **SQLite**：嵌入式、轻量级数据库引擎。
    - **MongoDB**：文档型 NoSQL 领军者。
    - **Redis**：内存数据结构存储。

- **DBMS 与数据库的区别？**
    - **数据库**：存放实际数据的容器。
    - **DBMS**：管理和分析数据的软件工具。

#### SQL 与 NoSQL

- **SQL 为什么重要？**
**SQL (Structured Query Language)** 是用于管理和操作关系型数据库的标准语言。它实现了 **CRUD (创建、读取、更新、删除)** 操作。
优势：通用性、高效性、精确性、标准化。

- **NoSQL 及其与 SQL 的区别？**
NoSQL 旨在处理多种数据模型（键值、文档、列族、图）。
    - **模式灵活性**：NoSQL 通常无模式 (Schema-less)。
    - **一致性模型**：SQL 遵循 ACID，NoSQL 往往追求高可用。

- **常用 SQL 命令**：
    - `SELECT`：检索。
    - `INSERT INTO`：添加。
    - `UPDATE`：修改。
    - `DELETE`：删除。
    - `CREATE/ALTER/DROP TABLE`：结构管理。
    - `JOIN`：多表联查。

#### 数据库设计与规范化

- **什么是数据库规范化 (Normalization)？**
规范化是减少冗余和提高数据完整性的过程。主要通过**范式 (Normal Forms)** 来实现：
    - **1NF**：单元格原子性，记录唯一。
    - **2NF**：消除部分依赖。
    - **3NF**：消除传递依赖。
目的：消除更新异常、节省存储、提高查询性能（由于索引更优）。

- **挑战与对策**：
    - **可扩展性**：采用分片 (Sharding)。
    - **性能**：索引优化、查询优化、必要时反规范化。
    - **安全**：访问控制、加密。

#### 数据库安全

- **安全性为什么重要？**
保护敏感信息免受未经授权的访问、盗取或损坏。在测试中，这意味着保障**测试数据**的完整性。
常见威胁：
    - **SQL 注入 (SQL Injection)**。
    - **内部威胁**。
    - **恶意软件与 DDoS 攻击**。

- **什么是 SQL 注入？如何预防？**
攻击者通过在查询中插入恶意代码来操纵数据库。
**对策**：
    - **参数化查询 (Prepared Statements)**。
    - **存储过程**。
    - **ORM 框架**。
    - **输入验证与转义**。

- **加密的作用**：
    - **静态加密 (At-rest)**：保护磁盘数据。
    - **传输加密 (In-transit)**：防止监听。
    - **透明数据加密 (TDE)**。
