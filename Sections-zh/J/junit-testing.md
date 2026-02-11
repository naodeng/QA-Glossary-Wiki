# JUnit 测试 (JUnit Testing)
[JUnit Testing](#junit-testing)

## 关于 JUnit 测试的常见问题

#### 基础与重要性
- **什么是 JUnit 测试？**
  JUnit 是一款针对 Java 语言的**单元测试 (Unit Testing)** 框架，旨在通过提供注解 (Annotations) 和断言 (Assertions) 来简化**测试用例 (Test Cases)** 的创建。它是开发人员独立于应用其余部分**验证每个软件单元**的核心工具。
  一个基础的 JUnit 测试用例使用 `@Test` 注解标识测试方法。例如：
  ```java
  import static org.junit.Assert.*;
  import org.junit.Test;

  public class ExampleTest {
      @Test
      public void testMethod() {
          int expected = 2;
          int actual = Math.addExact(1, 1);
          assertEquals("数值应当相等", expected, actual);
      }
  }
  ```
  为了处理**设置 (Setup)** 和**清理 (Cleanup)** 操作，JUnit 分别提供了 `@Before` 和 `@After`（JUnit 4）或 `@BeforeEach` 和 `@AfterEach`（JUnit 5）注解。此外，它还支持**异常测试**、**参数化测试**和**测试套件**。JUnit 可与 Maven、Gradle 等构建工具无缝集成。

- **为什么 JUnit 测试在软件开发中很重要？**
  - **确保回归安全**：自动化测试能快速识别代码更改引发的非预期副作用。
  - **促进持续集成 (CI)**：JUnit 是 CI/CD 流水的基石，实现自动化的构建与验证。
  - **推动测试驱动开发 (TDD)**：倡导先写测试再写代码，确保开发始终围绕需求。
  - **作为活文档**：展示系统的预期行为，方便代码维护。
  - **重构信心**：全面的测试套件让开发人员能大胆重构代码而不用担心破坏现有功能。
  - **质量指标**：通过**代码覆盖率 (Code Coverage)** 等指标评估软件质量。

- **JUnit 测试的关键特性有哪些？**
  - **基于注解的配置**：`@Test`, `@Before`, `@After`, `@BeforeClass`, `@AfterClass` 等。
  - **测试运行器 (Test Runners)**：执行测试并反馈结果。
  - **测试夹具 (Fixtures)**：确保测试环境的一致性。
  - **测试套件 (Test Suites)**：逻辑分组多个测试类。
  - **参数化测试**：使用不同输入多次运行同一测试。
  - **假设 (Assumptions)**：根据条件决定是否执行测试（`Assume`）。
  - **超时 (Timeouts)**：为测试指定运行时间上限。
  - **IDE 集成**：顶级 Java IDE（IntelliJ, Eclipse）的原生支持。

- **JUnit 如何提高代码质量？**
  它强制执行一种**纪律严明的方法**来编写和维护代码。它鼓励开发人员编写**可测试的、模块化的、低耦合**的代码，这通常会带来更好的软件设计和对 **SOLID 原则**的遵循。通过快速反馈机制，Bug 能在早期被发现并修复。

#### JUnit 测试用例 (JUnit Test Cases)
- **如何编写基础的 JUnit 测试用例？**
  1. **导入**：`import static org.junit.Assert.*; import org.junit.Test;`
  2. **定义类**：普通 Java 类即可。
  3. **注解方法**：使用 `@Test`。
  4. **编写逻辑并断言**：使用 `assertEquals`, `assertTrue` 等验证结果。

- **有哪些不同类型的断言 (Assertions)？**
  - `assertEquals(expected, actual)`：检查值相等。
  - `assertTrue(condition)`：断言为真。
  - `assertNull(object)`：断言为空。
  - `assertSame(expected, actual)`：断言引用同一个对象。
  - `assertArrayEquals(expectedArray, actualArray)`：断言数组相等。
  - `assertThrows(exceptionType, executable)`：断言抛出特定异常。

- **如何使用 setup() 和 teardown() 方法？**
  用于准备和清理环境。使用 `@BeforeEach` (JUnit 5) 或 `@Before` (JUnit 4) 在每个测试前运行；使用 `@AfterEach` 或 `@After` 在每个测试后运行。这确保了测试之间的**隔离性**。

- **如何测试异常？**
  在 JUnit 5 中推荐使用 `assertThrows`：
  ```java
  @Test
  void testException() {
      assertThrows(NumberFormatException.class, () -> Integer.parseInt("One"));
  }
  ```

#### 高级概念 (Advanced Concepts)
- **什么是参数化测试 (Parameterized Testing)？**
  允许以不同的参数多次运行同一测试，减少代码重复。JUnit 5 使用 `@ParameterizedTest` 配合 `@ValueSource`, `@CsvSource` 或 `@MethodSource` 实现。

- **什么是测试套件 (Test Suites)？**
  测试套件是测试用例或其他套件的集合，用于批量运行。这在组织大规模项目或区分冒烟测试、回归测试时非常有用（使用 `@Suite` 注解）。

- **如何从命令行运行 JUnit？**
  对于 JUnit 5，可以使用控制台启动器 `junit-platform-console-standalone.jar`，或者在 Maven/Gradle 项目中使用 `mvn test` 或 `./gradlew test`。

- **什么是 Mocking 以及如何在 JUnit 中使用？**
  Mocking 是一种通过模拟对象替代真实依赖来隔离被测单元的技术。常用框架是 **Mockito**。
  ```java
  @ExtendWith(MockitoExtension.class)
  public class MyTest {
      @Mock
      private Dependency dependency;

      @Test
      void test() {
          when(dependency.call()).thenReturn("Mocked");
          // ... 验证逻辑
      }
  }
  ```

#### 最佳实践 (Best Practices)
- **编写优质 JUnit 测试的建议**：
  - **命名清晰**：如 `shouldReturnTrueWhenConditionMet()`。
  - **单一职责**：每个方法只测试一个方面。
  - **AAA 模式**：Arrange (安排环境), Act (执行动作), Assert (断言结果)。
  - **独立性**：测试顺序不应影响结果。
  - **保持快速**：避免耗时的 I/O 操作，使用 Mock 替代。
  - **利用参数化测试**：覆盖边界值。
  - **保持代码 Review 标准**：像对待生产代码一样对待测试代码。

- **如何确保测试有效？**
  - 面向**行为**，而不是实现（允许重构不改测试）。
  - 测试**边界条件**和异常路径。
  - 维持合理的**代码覆盖率**，但追求“有意义的测试”而非单纯提高覆盖率数字。
  - 避免在测试中加入逻辑（如循环或条件判断），保持其简单直观。

- **性能优化建议**：
  - 并行执行测试。
  - 使用**内存在数据库**（如 H2）进行持久层测试。
  - 使用 `@TestInstance(Lifecycle.PER_CLASS)` 共享昂贵的初始化过程。
  - 及时清理资源。
