# NUnit
[NUnit](#nunit) [NUnit](/wiki/nunit) [单元测试 (unit testing)](/wiki/unit-testing) [测试执行 (test executions)](/wiki/test-execution)

### 相关术语：
- JUnit 测试 (JUnit Testing)
- 测试框架 (Test Framework)
[JUnit Testing](/glossary/junit-testing) [Test Framework](/glossary/test-framework)

### 参见：
- [官方网站](https://nunit.org/)
- [维基百科](https://en.wikipedia.org/wiki/NUnit)

## 关于 NUnit 的常见问题

#### 基础与重要性
- **什么是 NUnit？**
  NUnit 是一个针对 .NET 语言的开源**单元测试框架**，旨在为编写和运行测试提供灵活且用户友好的工具。它是 .NET 基金会的一部分，因其能够创建简单及复杂的**测试用例**而被广泛使用。
  **核心用法：**
  - **特性标记 (Attributes)**：使用 `[Test]` 标记测试方法，`[TestFixture]` 标记测试类，`[SetUp]` 和 `[TearDown]` 分别标记在每项测试前后运行的方法。
  - **断言 (Assertions)**：提供丰富的断言集（如 `Assert.AreEqual`, `Assert.IsTrue`）来验证测试结果。
  - **异常处理**：支持使用 `Assert.Throws` 验证预期异常。
  - **参数化测试**：通过 `[TestCase]` 和 `[TestCaseSource]` 支持数据驱动测试。
  - **工具集成**：与 **Selenium** 等工具无缝协作，支持**端到端测试 (E2E)** 场景。

- **为什么 NUnit 在软件测试中很重要？**
  它是 **.NET 测试生态**中的核心工具，通过提供高效框架支持**测试驱动开发 (TDD)**。
  - **CI/CD 集成**：方便集成到持续集成系统，实现自动化构建和测试，尽早发现缺陷。
  - **并行执行**：支持并行运行测试，显著缩短测试套件执行时间。
  - **可扩展性**：支持通过插件自定义功能。
  - **一致性**：在团队开发中维护统一的测试结构和约定。

- **NUnit 的关键特性有哪些？**
  - 基于特性的测试配置。
  - 测试用例与测试套件的组织管理。
  - 全面的断言模型（含约束模型/Constraint Model）。
  - 参数化与并行执行支持。
  - 强大的过滤与分类 (`[Category]`) 功能。
  - 生成详细的 XML 格式测试报告。
  - 跨平台支持（.NET Core, Mono 等）。

- **NUnit 与其他框架（如 MSTest, xUnit）的比较？**
  - **MSTest**：微软官方工具，集成度高但灵活性稍逊，断言库相对较弱。
  - **xUnit**：被视为 NUnit 的继任者，采用更现代的方法（如用构造函数代替 SetUp），对异步测试支持更好。
  - **NUnit**：在易用性与现代测试方法间取得了平衡，灵活且属性丰富，拥有强大的数据驱动测试支持。

#### 安装与配置
- **如何安装 NUnit？**
  - 使用 **NuGet 管理器**：在 VS 中搜索安装 `NUnit`。
  - **Package Manager Console**：运行 `Install-Package NUnit -Version 3.x.x`。
  - **.NET CLI**：运行 `dotnet add package NUnit`。
  - **注意**：若要在 VS 测试浏览器中运行，还需安装 `NUnit3TestAdapter`。

- **系统要求**：支持 .NET Framework 2.0+（推荐 4.5+）、.NET Core 1.1+（含 .NET 5/6）、Mono 4.6+。支持 Windows, macOS 和 Linux。

#### 使用与实施
- **如何编写基础测试用例？**
  1. 使用 `[TestFixture]` 装饰测试类。
  2. 使用 `[Test]` 装饰测试方法。
  3. 按照 **Arrange-Act-Assert (AAA)** 模式编写逻辑。
  ```csharp
  [TestFixture]
  public class CalculatorTests {
      [Test]
      public void Add_TwoNumbers_ReturnsSum() {
          var calc = new Calculator();
          int result = calc.Add(5, 7);
          Assert.AreEqual(12, result);
      }
  }
  ```

- **断言类型**：涵盖等值、身份（同一对象）、布尔、空值、比较（大于/小于）、字符串匹配（正则/包含）、集合（子集/成员）以及异常断言。

- **测试分组与过滤**：使用 `[Category("Urgent")]` 进行逻辑分组。运行命令如 `--where "cat == Urgent"` 可仅执行特定组。

- **SetUp 与 TearDown 的作用**：
  - `[SetUp]`：每个测试前运行，用于初始化环境（如创建对象实例）。
  - `[TearDown]`：每个测试后运行，用于清理资源（如关闭数据库连接）。

#### 高级概念
- **异常处理**：使用 `Assert.Throws<T>(() => { ... })` 验证。若要求不抛异常，使用 `Assert.DoesNotThrow`。注意：`ExpectedException` 属性已过时。
- **参数化与数据驱动**：
  - `[TestCase(1, 2, 3)]`：直接在属性中定义多组数据。
  - `[TestCaseSource(nameof(SourceData))]`：从外部 `IEnumerable` 获取复杂测试数据。
  - 分离测试逻辑与数据，提高测试覆盖率和维护性。

- **Selenium 集成**：
  在 `[SetUp]` 中初始化驱动（如 `ChromeDriver`），在 `[Test]` 中调用 Selenium API 操作浏览器并断言结果，最后在 `[TearDown]` 中执行 `driver.Quit()` 释放资源。
