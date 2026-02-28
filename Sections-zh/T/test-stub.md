# 测试存根

<!-- TOC START -->
- [关于测试存根的问题吗？](#关于测试存根的问题吗？)
  - [基础知识和重要性](#基础知识和重要性)
    - [什么是测试存根？](#什么是测试存根？)
    - [为什么测试存根在软件测试中很重要？](#为什么测试存根在软件测试中很重要？)
    - [测试存根与模拟对象有何不同？](#测试存根与模拟对象有何不同？)
    - [单元测试中测试存根的作用是什么？](#单元测试中测试存根的作用是什么？)
    - [使用测试存根有哪些优点和缺点？](#使用测试存根有哪些优点和缺点？)
    - [测试存根是如何实现的？](#测试存根是如何实现的？)
    - [测试存根的关键要素是什么？](#测试存根的关键要素是什么？)
    - [您能提供一个测试存根的示例吗？](#您能提供一个测试存根的示例吗？)
    - [测试存根如何用于模拟异常或错误情况？](#测试存根如何用于模拟异常或错误情况？)
    - [创建测试存根时有哪些最佳实践？](#创建测试存根时有哪些最佳实践？)
  - [与测试框架集成](#与测试框架集成)
    - [测试存根如何与流行的测试框架集成？](#测试存根如何与流行的测试框架集成？)
    - [如何在 JUnit 中创建测试存根？](#如何在-junit-中创建测试存根？)
    - [如何在 Mockito 中创建测试存根？](#如何在-mockito-中创建测试存根？)
    - [在不同的测试框架中使用测试存根有什么区别？](#在不同的测试框架中使用测试存根有什么区别？)
    - [测试存根如何与其他测试工具和技术结合使用？](#测试存根如何与其他测试工具和技术结合使用？)
<!-- TOC END -->

模拟不存在的组件的行为。

## 关于测试存根的问题吗？

### 基础知识和重要性

#### 什么是测试存根？

**[Test Stub](../T/test-stub.md)** 是测试期间使用的接口或类的最小实现，用于替换被测系统与之交互的真实组件。存根为测试期间进行的函数调用提供预定义的响应，而不执行它们所替换的组件的任何实际代码。
  实现 [Test Stub](../T/test-stub.md) 通常涉及创建符合所需接口的新类或对象。该存根将包括预期由被测系统调用的方法，这些方法将返回与[test case](../T/test-case.md)相关的固定值。

  ```
  public class PaymentServiceStub implements PaymentService {
      public boolean processPayment(double amount) {
          // Return a fixed response for testing purposes
          return true;
      }
  }
  ```存根对于模拟难以用真实组件生成的场景特别有用，例如网络故障或[database](../D/database.md) 错误。通过返回特定值或引发异常，它们可以模仿这些条件。
  创建[Test Stubs](../T/test-stub.md) 时，必须确保它们简单并专注于测试的需求。它们不应包含复杂的逻辑，而应易于理解和维护。与测试框架的集成通常很简单，因为存根可以在 [test cases](../T/test-case.md) 中直接实例化和使用，或者使用框架的依赖注入机制进行设置。

#### 为什么测试存根在软件测试中很重要？

[Test Stubs](../T/test-stub.md) 在[software testing](../S/software-testing.md) 中至关重要，因为它们通过模拟与被测单元交互的软件模块的行为来促进组件的**隔离测试**。这种隔离有助于查明设备本身内部的缺陷，而不会受到可能与当前测试无关或尚未开发的系统其他部分的干扰。
  通过使用存根，测试人员可以更有效地**控制[test environment](../T/test-environment.md)**，提供特定的输入并模拟各种场景，包括错误条件。这种控制对于确保单元测试**可靠**和**可重复**至关重要，这是可靠测试策略的关键方面。
  存根还在**持续集成**环境中发挥着重要作用，其中自动化测试需要快速高效地运行。它们通过避免依赖于缓慢、不稳定或不可用的外部系统或组件来帮助降低测试的复杂性和执行时间。
  此外，存根可用于**模拟具有法律或道德限制的功能**，例如第三方服务或支付网关，从而允许在不违反协议或产生费用的情况下进行全面测试。
  从本质上讲，[Test Stubs](../T/test-stub.md) 是确保高质量、健壮和可维护代码不可或缺的工具，因为它们使开发人员能够以受控和可预测的方式验证代码的正确性。

#### 测试存根与模拟对象有何不同？

[Test Stubs](../T/test-stub.md) 和模拟对象都在 [unit testing](../U/unit-testing.md) 中用于模拟依赖关系，但它们有不同的目的并在不同的上下文中使用。
  **[Test Stubs](../T/test-stub.md)** 是返回硬编码数据的简单实现。它们主要用于通过用可预测和可控的替代品替换复杂、不可用或不确定的组件来隔离被测系统。存根通常没有任何断言；他们是被动的，只提供预设的回复。
  另一方面，**模拟对象**更加复杂。它们用于验证被测系统与其依赖项之间的交互。模拟可以根据期望进行编程，这意味着它们可以断言是否使用正确的参数、正确的次数或以正确的顺序调用它们。它们是活跃的，因为如果预期的交互没有发生，它们可能会导致测试失败。
  总之，虽然 [Test Stub](../T/test-stub.md) 可用于模拟返回一组固定数据的数据源，但模拟对象将用于确保一个方法调用具有特定参数的另一个方法。模拟是关于行为[verification](../V/verification.md)，而存根是关于状态[verification](../V/verification.md)。
  这是一个简单的例子来说明差异：

  ```
  // Stub example
  function fetchDataStub() {
    return "fixed data";
  }
  // Mock example using a mock library like Jest
  const mockFunction = jest.fn();
  mockFunction.mockReturnValue("dynamic data based on expectations");
  // In the test, you would verify the mock was called
  expect(mockFunction).toHaveBeenCalledWith(expectedParams);
  ```实际上，在 Stub 和 Mock 之间进行选择取决于您是否需要验证被测系统的行为，或者只是为其提供执行其功能所需的数据。

#### 单元测试中测试存根的作用是什么？

在[unit testing](../U/unit-testing.md) 中，**[test stubs](../T/test-stub.md)** 充当与被测单元交互的缺失组件或模块的**占位符**。它们为测试期间进行的方法调用提供**预定义的响应**，确保单元测试可以独立于外部系统或服务运行。
  通过使用[test stubs](../T/test-stub.md)，您可以隔离被测单元，这使您可以在受控环境中验证单元行为的正确性。存根对于模拟在测试期间交互**不可用**或**昂贵**的组件的行为特别有用，例如[databases](../D/database.md)、Web 服务或第三方库。
  实现[test stub](../T/test-stub.md) 时，您通常会硬编码与[test case](../T/test-case.md) 相关的响应。例如，如果被测单元需要来自 [database](../D/database.md) 的数据，则存根可能会返回一组固定的记录，而无需实际查询真正的 [database](../D/database.md)。

  ```
  function fetchDataStub() {
    return [
      { id: 1, name: 'Alice' },
      { id: 2, name: 'Bob' }
    ];
  }
  ```存根还可以配置为通过引发异常或返回错误代码来模拟**错误条件**，从而允许您测试被测单元如何处理故障。
  将[test stubs](../T/test-stub.md) 纳入您的测试策略可增强[test suite](../T/test-suite.md) 的**可靠性**和**速度**，因为它们消除了对外部因素的依赖。当使用 JUnit 或 Mockito 等测试框架时，可以使用内置机制或注释轻松集成存根，从而简化测试过程并保持不同 [test cases](../T/test-case.md) 之间的一致性。

#### 使用测试存根有哪些优点和缺点？

**使用[Test Stubs](../T/test-stub.md)的优点：**

- **隔离：**
    存根允许通过模拟相关组件的行为来隔离测试单个代码单元。

- **简单性：**
    当测试所需的功能很少时，它们比完整的模拟对象更容易实现。

- **控制：**
    测试人员可以控制依赖项的响应，这可用于测试各种场景，包括故障模式。

- **速度：**
    存根比与真实依赖项或复杂模拟集成更快，从而加快测试执行速度。

- **决定论：**
    它们提供一致的结果，确保测试不受外部因素或依赖项状态变化的影响。
  **使用[Test Stubs](../T/test-stub.md)的缺点：**

- **有限反馈：**
    存根可能会过度简化依赖项的行为，这可能无法揭示集成或交互问题。

- **维护：**
    随着系统的发展，存根可能会变得过时，并且需要维护以匹配真实组件的行为。

- **过度使用：**
    过度依赖存根可能会导致错误的安全感，因为现实世界的复杂性尚未得到充分测试。

- **整合缺陷：**
    它们无助于发现集成缺陷，因为它们没有模仿真实组件的确切行为。

- **状态管理：**
    存根可以是无状态的，并且可能不适合依赖项状态很重要的测试场景。
  有效使用[test stubs](../T/test-stub.md)需要平衡其优点与潜在缺点，确保它们补充其他测试策略以提供全面的[test coverage](../T/test-coverage.md)。

- **隔离：**
    存根允许通过模拟相关组件的行为来隔离测试单个代码单元。

- **简单性：**
    当测试所需的功能很少时，它们比完整的模拟对象更容易实现。

- **控制：**
    测试人员可以控制依赖项的响应，这可用于测试各种场景，包括故障模式。

- **速度：**
    存根比与真实依赖项或复杂模拟集成更快，从而加快测试执行速度。

- **决定论：**
    它们提供一致的结果，确保测试不受外部因素或依赖项状态变化的影响。

- **有限反馈：**
    存根可能会过度简化依赖项的行为，这可能无法揭示集成或交互问题。

- **维护：**
    随着系统的发展，存根可能会变得过时，并且需要维护以匹配真实组件的行为。

- **过度使用：**
    过度依赖存根可能会导致错误的安全感，因为现实世界的复杂性尚未得到充分测试。

- **整合缺陷：**
    它们无助于发现集成缺陷，因为它们没有模仿真实组件的确切行为。

- **状态管理：**
    存根可以是无状态的，并且可能不适合依赖项状态很重要的测试场景。

＃＃＃ 执行

#### 测试存根是如何实现的？

实施 **[Test Stub](../T/test-stub.md)** 通常涉及以下步骤：

1. **确定依赖关系**
    需要用存根替换的被测单元。

2. **创建存根类**
    实现接口或继承依赖项的类。

3. **重写方法**
    在测试过程中需要控制，提供必要的硬编码响应或行为。

4. **实例化存根**
    在你的测试中和
    **注入**
    通常通过构造函数注入、方法注入或属性设置将其注入到被测单元中。

5. **配置存根**
    ，如有必要，返回特定值或模拟特定测试用例的某些条件。
  下面是一个使用假设的 `EmailService` 接口的 TypeScript 简单示例：

  ```
  interface EmailService {
    sendEmail(to: string, subject: string, body: string): boolean;
  }
  class TestEmailServiceStub implements EmailService {
    sendEmail(to: string, subject: string, body: string): boolean {
      // Simulate successful email sending
      return true;
    }
  }
  // Usage in a test
  const testEmailService = new TestEmailServiceStub();
  const componentUnderTest = new ComponentThatUsesEmailService(testEmailService);
  // Assert that the component behaves correctly when email sending is successful
  ```请记住**保持存根简单**并仅关注测试所需的行为。避免存根中的逻辑与[test scenario](../T/test-scenario.md) 不直接相关。这确保了测试保持可维护性，并且存根不会成为测试套件中复杂性或潜在[bugs](../B/bug.md) 的来源。

1. **确定依赖关系**
    需要用存根替换的被测单元。

2. **创建存根类**
    实现接口或继承依赖项的类。

3. **重写方法**
    在测试过程中需要控制，提供必要的硬编码响应或行为。

4. **实例化存根**
    在你的测试中和
    **注入**
    通常通过构造函数注入、方法注入或属性设置将其注入到被测单元中。

5. **配置存根**
    ，如有必要，返回特定值或模拟特定测试用例的某些条件。

#### 测试存根的关键要素是什么？

**[Test Stub](../T/test-stub.md)** 的关键要素包括：

- **预定义响应**：存根为测试期间进行的函数调用提供硬编码响应。
  - **简化逻辑**：它们包含最少的逻辑，仅足以使测试通过。
  - **接口实现**：存根必须遵守它们所替换的组件的接口。
  - **配置**：可以将它们配置为针对不同的输入返回不同的输出，以模拟各种场景。
  - **状态[Verification](../V/verification.md)** ：某些存根可能允许在测试执行后进行状态验证。
  - **错误模拟**：它们可以设计为通过返回错误代码或引发异常来模拟错误条件。
  - **性能**：存根可以是轻量级的，以减少测试中的性能开销。

  ```
  // Example in TypeScript
  class MyServiceStub implements MyServiceInterface {
    fetchData(): Data {
      // Return a fixed response regardless of input
      return { isValid: true, items: [] };
    }
  }
  ```

- **集成**：存根应轻松与测试套件集成，不需要大量设置。
  - **[Maintainability](../M/maintainability.md)** ：随着接口或需求的变化，它们应该易于维护和更新。
  - **隔离**：存根通过消除对外部系统或组件的依赖来帮助隔离被测系统。
  请记住使存根尽可能**简单**，并且仅在必要时使用它们以避免测试过于复杂。它们应该是实现隔离的工具，而不是复制复杂逻辑的手段。

- **预定义响应**：存根为测试期间进行的函数调用提供硬编码响应。
  - **简化逻辑**：它们包含最少的逻辑，仅足以使测试通过。
  - **接口实现**：存根必须遵守它们所替换的组件的接口。
  - **配置**：可以将它们配置为针对不同的输入返回不同的输出，以模拟各种场景。
  - **状态[Verification](../V/verification.md)** ：某些存根可能允许在测试执行后进行状态验证。
  - **错误模拟**：它们可以设计为通过返回错误代码或引发异常来模拟错误条件。
  - **性能**：存根可以是轻量级的，以减少测试中的性能开销。
  - **集成**：存根应轻松与测试套件集成，不需要大量设置。
  - **[Maintainability](../M/maintainability.md)** ：随着接口或需求的变化，它们应该易于维护和更新。
  - **隔离**：存根通过消除对外部系统或组件的依赖来帮助隔离被测系统。

#### 您能提供一个测试存根的示例吗？

当然！下面是一个假设场景中的 [Test Stub](../T/test-stub.md) 示例，您正在测试依赖于数据存储库的服务。存根将模拟数据存储库的行为。

  ```
  public class DataRepositoryStub extends DataRepository {
      private boolean throwError;
      public DataRepositoryStub(boolean throwError) {
          this.throwError = throwError;
      }
      @Override
      public Data fetchData() {
          if (throwError) {
              throw new DataLoadException("Failed to fetch data.");
          }
          return new Data("Stubbed data");
      }
  }
  ```在此 Java 示例中，`DataRepositoryStub` 扩展了 `DataRepository` 类，并重写了 `fetchData` 方法。布尔值 `throwError` 确定存根是否应模拟成功的数据获取或引发异常以模拟错误情况。
  要在单元测试中使用此存根：

  ```
  @Test
  public void testServiceWithDataRepositoryStub() {
      DataRepositoryStub stub = new DataRepositoryStub(false); // Set to true to simulate an error
      DataService service = new DataService(stub);
      Data result = service.getData();
      assertNotNull(result);
      assertEquals("Stubbed data", result.getContent());
  }
  ```在测试中，您使用`false` 实例化`DataRepositoryStub` 以模拟正常行为。如果您想测试错误处理，请使用`true` 实例化它。然后使用存根测试 `DataService`，确保它能够按预期处理正常和异常情况。

#### 测试存根如何用于模拟异常或错误情况？

[Test Stubs](../T/test-stub.md) 可用于模拟异常或错误条件，方法是显式编码它们以在调用时返回错误响应或引发异常。这使得测试人员能够验证被测系统 (SUT) 如何处理这些场景，而不必依赖实际的依赖项来失败。
  要模拟异常，您可以将存根配置为在调用某个方法时抛出特定的异常类型。当您想要测试 SUT 的错误处理或对外部服务故障的恢复能力时，这特别有用。
  例如，在使用 JUnit 的 Java 中，您可以创建一个抛出 `IOException` 的存根：

  ```
  public class MyStub implements DependencyInterface {
      @Override
      public void performAction() throws IOException {
          throw new IOException("Simulated exception");
      }
  }
  ```在此存根中，`performAction` 方法被重写，以便在每次调用该方法时抛出 `IOException`，从而允许您测试 SUT 对此异常的反应。
  要模拟错误条件，您可以将存根配置为返回错误代码、空对象或 SUT 在实际场景中可能遇到的任何其他失败指示符。
  例如，如果您的 SUT 与返回状态代码的服务交互，您可以模拟失败响应：

  ```
  public class MyStub implements ServiceInterface {
      @Override
      public Response performService() {
          return new Response(500, "Internal Server Error");
      }
  }
  ```在此示例中，`performService` 方法返回带有 500 状态代码的 `Response` 对象，模拟服务器错误。这允许您测试您的 SUT 如何处理此类故障。

#### 创建测试存根时有哪些最佳实践？

创建[test stubs](../T/test-stub.md)时，请遵循以下最佳实践，以确保它们有效且可维护：

- **保持存根简单**：存根应该简单，仅模拟测试所需的行为。避免添加不直接有助于测试目的的逻辑。
  - **使用描述性名称**：选择能够清楚表明存根角色及其模拟条件的名称，有助于可读性和维护。
  - **隔离测试**：确保每个存根的使用方式不会影响其他测试。存根不应在测试之间引入共享状态。
  - **参数化存根**：如果可能，使存根可配置，以便它们可以在不同的 [test scenarios](../T/test-scenario.md) 之间重复使用。
  - **验证交互**：如果与存根的交互很重要，请验证被测系统是否按预期与存根交互。
  - **清理**：每次测试后，清理所有资源或状态，以防止对后续测试产生副作用。
  - **文档存根**：评论为什么需要存根以及应该如何使用它，特别是如果它的行为从其实现中不是立即显而易见的。
  - **匹配真实行为**：确保存根的行为与其所代表的真实组件的行为紧密匹配，以避免 [false positives](../F/false-positive.md) 或负面结果。
  - **版本控制**：将存根视为代码库的一部分，通过适当的更改跟踪在版本控制下维护它们。
  - **审查和重构**：定期审查和重构存根，以保持它们的相关性并与不断发展的代码库保持一致。

  ```
  // Example of a simple, well-named test stub in TypeScript
  function alwaysReturnsTrueStub(): boolean {
    return true;
  }
  ```通过遵循这些实践，您将创建健壮且可靠的[test stubs](../T/test-stub.md)，从而有助于更有效和高效的测试过程。

- **保持存根简单**：存根应该简单，仅模拟测试所需的行为。避免添加不直接有助于测试目的的逻辑。
  - **使用描述性名称**：选择能够清楚表明存根角色及其模拟条件的名称，有助于可读性和维护。
  - **隔离测试**：确保每个存根的使用方式不会影响其他测试。存根不应在测试之间引入共享状态。
  - **参数化存根**：如果可能，使存根可配置，以便它们可以在不同的 [test scenarios](../T/test-scenario.md) 之间重复使用。
  - **验证交互**：如果与存根的交互很重要，请验证被测系统是否按预期与存根交互。
  - **清理**：每次测试后，清理所有资源或状态，以防止对后续测试产生副作用。
  - **文档存根**：评论为什么需要存根以及应该如何使用它，特别是如果它的行为从其实现中不是立即显而易见的。
  - **匹配真实行为**：确保存根的行为与其所代表的真实组件的行为紧密匹配，以避免 [false positives](../F/false-positive.md) 或负面结果。
  - **版本控制**：将存根视为代码库的一部分，通过适当的更改跟踪在版本控制下维护它们。
  - **审查和重构**：定期审查和重构存根，以保持它们的相关性并与不断发展的代码库保持一致。

### 与测试框架集成

#### 测试存根如何与流行的测试框架集成？

将[test stubs](../T/test-stub.md) 与流行的测试框架集成通常涉及利用框架的功能在[test execution](../T/test-execution.md) 期间用存根替换真正的依赖项。这是一个简洁的指南：
  **JUnit**：
  JUnit 没有内置的存根机制，但它允许与存根库轻松集成。使用 `@BeforeEach` 或 `@Before` 注释在每次测试之前设置存根。

  ```
  @BeforeEach
  public void setUp() {
      Dependency stub = createStub();
      testInstance.setDependency(stub);
  }
  ```**测试NG**：
  与 JUnit 类似，使用 `@BeforeMethod` 来配置存根。 TestNG 对 `@DataProvider` 参数化测试的支持对于将存根输入到测试中也很有用。

  ```
  @BeforeMethod
  public void setUp() {
      Dependency stub = createStub();
      testInstance.setDependency(stub);
  }
  ```**模拟**：
  虽然 Mockito 主要是一个模拟框架，但它可用于使用 `when().thenReturn()` 语法创建存根。它与 JUnit 和 TestNG 无缝集成。

  ```
  @Test
  public void test() {
      Dependency stub = mock(Dependency.class);
      when(stub.method()).thenReturn(value);
      // ...
  }
  ```**RSpec（红宝石）**：
  可以使用 `allow` 或 `expect` 方法设置存根，并且 RSpec 的 `before` 块用于在示例之前准备存根。

  ```
  before do
    allow(dependency).to receive(:method).and_return(value)
  end
  ```**pytest（Python）**：
  使用固定装置创建存根并将其注入测试中。 `monkeypatch` 夹具对于存根特别有用。

  ```
  def test_function(monkeypatch):
      def mock_method():
          return value
      monkeypatch.setattr('module.Class.method', mock_method)
      # ...
  ```在所有情况下，请确保在测试后**拆除**或**重置**，以避免交叉测试污染，通常由框架自动处理或使用 `@After`/`@AfterMethod` 注释或等效的拆除方法。

#### 如何在 JUnit 中创建测试存根？

在 JUnit 中创建 [test stub](../T/test-stub.md) 涉及编写具有预定义行为的接口或类的简单实现。此行为被硬编码以返回特定值或执行模拟真实场景的某些操作。这是分步指南：

1. **识别您想要存根的依赖项**。这可以是被测单元与之交互的接口或具体类。
  2. **创建一个存根类**来实现接口或扩展您要存根的类。
  3. **用您想要模拟的行为覆盖接口或类的方法**。根据测试需要返回固定值或执行简单操作。
  4. **在测试中实例化存根**并将其传递给被测单元。
  下面是 JUnit 中的存根示例：

  ```
  public interface ExternalService {
      int performAction();
  }
  public class ExternalServiceStub implements ExternalService {
      @Override
      public int performAction() {
          // Return a fixed value to simulate the behavior
          return 42;
      }
  }
  public class MyTest {
      @Test
      public void testMethod() {
          ExternalService stub = new ExternalServiceStub();
          MyClass myClass = new MyClass(stub);
          int result = myClass.useExternalService();
          assertEquals(42, result);
      }
  }
  ```在此示例中，`ExternalServiceStub` 是通过返回固定值来模拟外部服务行为的存根。 `MyClass` 实例在测试中使用此存根，允许您在与外部服务交互时控制[test environment](../T/test-environment.md) 并验证`MyClass` 的行为。

1. **识别您想要存根的依赖项**。这可以是被测单元与之交互的接口或具体类。
  2. **创建一个存根类**来实现接口或扩展您要存根的类。
  3. **用您想要模拟的行为覆盖接口或类的方法**。根据测试需要返回固定值或执行简单操作。
  4. **在测试中实例化存根**并将其传递给被测单元。

#### 如何在 Mockito 中创建测试存根？

在 Mockito 中创建 [test stub](../T/test-stub.md) 非常简单。使用`mock` 方法创建所需类或接口的存根。然后，使用 `when` 和 `thenReturn` 方法为要存根的特定调用定义存根的行为。这是一个简洁的例子：

  ```
  import static org.mockito.Mockito.*;
  // Create a stub instance
  MyClass myClassStub = mock(MyClass.class);
  // Define stub behavior for a method
  when(myClassStub.myMethod("input")).thenReturn("expectedOutput");
  // Use the stub in a test
  String result = myClassStub.myMethod("input");
  assertEquals("expectedOutput", result);
  ```对于抛出异常的方法，请使用`thenThrow`：

  ```
  when(myClassStub.myMethod("input")).thenThrow(new RuntimeException());
  ```要处理具有不同参数或返回值的多个调用，请链接 `thenReturn` 调用或使用 `any()` 等参数匹配器：

  ```
  when(myClassStub.myMethod(anyString()))
      .thenReturn("firstCall")
      .thenReturn("secondCall");
  // or for different arguments
  when(myClassStub.myMethod("firstInput")).thenReturn("firstOutput");
  when(myClassStub.myMethod("secondInput")).thenReturn("secondOutput");
  ```请记住静态导入 Mockito 以提高可读性。另外，请确保您的存根的使用方式不违反最佳实践，例如应验证的过度存根或存根方法。

#### 在不同的测试框架中使用测试存根有什么区别？

在各种测试框架中使用[test stubs](../T/test-stub.md) 的差异源于每个框架提供的**语法**、**功能**和**集成功能**：

- **JUnit**：存根手动创建为简单类，或使用带有 Mockito 扩展的 `@Mock` 注释。 JUnit 5 的扩展模型允许与模拟库无缝集成。

    ```
    public class StubService implements Service {
        public String operation() {
            return "stubbed response";
        }
    }
    ```

- **TestNG**：与JUnit类似，但具有不同的注释和更灵活的测试配置。 TestNG 允许通过数据提供者和工厂方法进行更复杂的存根。

    ```
    public class StubService implements Service {
        public String operation() {
            return "stubbed response";
        }
    }
    ```

- **RSpec (Ruby)**：存根是使用 `allow` 和 `receive` 方法创建的，提供了一种更像**DSL 的**方法。

    ```
    allow(service).to receive(:operation).and_return("stubbed response")
    ```

- **Pytest (Python)**：利用固定装置和猴子补丁来存根方法或函数。 Pytest 的装置提供强大的 [setup](../S/setup.md) 和拆卸功能。

    ```
    def test_operation(monkeypatch):
        def mock_operation():
            return "stubbed response"
        monkeypatch.setattr('module.Service.operation', mock_operation)
    ```

- **Mocha (JavaScript)**：存根是使用Sinon.js 或其他库创建的，为[verification](../V/verification.md) 和存根提供丰富的[APIs](../A/api.md) 行为。

    ```
    const sinon = require('sinon');
    let stub = sinon.stub(service, 'operation').returns("stubbed response");
    ```每个框架的存根方法都会影响 [test automation](../T/test-automation.md) 工程师如何**快速**和**轻松**地编写和维护测试。框架的选择通常取决于语言生态系统和项目的具体需求，例如测试的复杂性或对某些功能（如异步测试或与其他工具的集成）的需求。

- **JUnit**：存根手动创建为简单类，或使用带有 Mockito 扩展的 `@Mock` 注释。 JUnit 5 的扩展模型允许与模拟库无缝集成。

    ```
    public class StubService implements Service {
        public String operation() {
            return "stubbed response";
        }
    }
    ```

- **TestNG**：与JUnit类似，但具有不同的注释和更灵活的测试配置。 TestNG 允许通过数据提供者和工厂方法进行更复杂的存根。

    ```
    public class StubService implements Service {
        public String operation() {
            return "stubbed response";
        }
    }
    ```

- **RSpec (Ruby)**：存根是使用 `allow` 和 `receive` 方法创建的，提供了一种更像**DSL 的**方法。

    ```
    allow(service).to receive(:operation).and_return("stubbed response")
    ```

- **Pytest (Python)**：利用固定装置和猴子补丁来存根方法或函数。 Pytest 的装置提供强大的 [setup](../S/setup.md) 和拆卸功能。

    ```
    def test_operation(monkeypatch):
        def mock_operation():
            return "stubbed response"
        monkeypatch.setattr('module.Service.operation', mock_operation)
    ```

- **Mocha (JavaScript)**：存根是使用Sinon.js 或其他库创建的，为[verification](../V/verification.md) 和存根提供丰富的[APIs](../A/api.md) 行为。

    ```
    const sinon = require('sinon');
    let stub = sinon.stub(service, 'operation').returns("stubbed response");
    ```

#### 测试存根如何与其他测试工具和技术结合使用？

[Test Stubs](../T/test-stub.md) 可以与各种测试工具和技术集成以增强测试过程：

- **[Integration Testing](../I/integration-testing.md)**：存根可以模拟尚未开发或不可用的组件，从而允许早期[integration testing](../I/integration-testing.md)。
  - **持续集成 (CI)**：在 CI 管道中，存根确保测试可以自主运行，而不依赖于外部系统，从而实现更可靠的构建。
  - **行为驱动开发 ([BDD](../B/bdd.md))**：存根可用于模拟系统的预期行为，即使某些组件未完全实现，也允许测试 [BDD](../B/bdd.md) 场景。
  - **服务虚拟化**：存根可以充当虚拟服务，模仿第三方[APIs](../A/api.md)或在测试期间成本高昂或难以访问的服务。
  - **[Performance Testing](../P/performance-testing.md)**：通过删除系统的某些部分，您可以隔离特定组件并对其进行压力测试，以识别性能瓶颈。
  - **[Test Data](../T/test-data.md) 管理**：存根可以配置为返回不同的数据集，方便使用各种数据场景进行测试，而无需操作真实的[database](../D/database.md)。
  - **[End-to-End Testing](../E/end-to-end-testing.md)**：虽然不能替代实际集成的测试，但可以在早期[end-to-end testing](../E/end-to-end-testing.md) 中使用存根来模拟外部系统的行为。
  - **测试隔离**：存根有助于隔离被测系统，从而更容易查明故障。
  - **[Regression Testing](../R/regression-testing.md)**：它们使回归测试能够独立于外部系统运行，外部系统可能会随着时间的推移而变化并影响测试结果。
  通过将[Test Stubs](../T/test-stub.md)与这些工具和技术相结合，[test automation](../T/test-automation.md)工程师可以创建一个强大而灵活的测试环境，满足各种测试需求，同时最大限度地减少对外部系统的依赖。

- **[Integration Testing](../I/integration-testing.md)**：存根可以模拟尚未开发或不可用的组件，从而允许早期[integration testing](../I/integration-testing.md)。
  - **持续集成 (CI)**：在 CI 管道中，存根确保测试可以自主运行，而不依赖于外部系统，从而实现更可靠的构建。
  - **行为驱动开发 ([BDD](../B/bdd.md))**：存根可用于模拟系统的预期行为，即使某些组件未完全实现，也允许测试 [BDD](../B/bdd.md) 场景。
  - **服务虚拟化**：存根可以充当虚拟服务，模仿第三方[APIs](../A/api.md)或在测试期间成本高昂或难以访问的服务。
  - **[Performance Testing](../P/performance-testing.md)**：通过删除系统的某些部分，您可以隔离特定组件并对其进行压力测试，以识别性能瓶颈。
  - **[Test Data](../T/test-data.md) 管理**：存根可以配置为返回不同的数据集，方便使用各种数据场景进行测试，而无需操作真实的[database](../D/database.md)。
  - **[End-to-End Testing](../E/end-to-end-testing.md)**：虽然不能替代实际集成的测试，但可以在早期[end-to-end testing](../E/end-to-end-testing.md) 中使用存根来模拟外部系统的行为。
  - **测试隔离**：存根有助于隔离被测系统，从而更容易查明故障。
  - **[Regression Testing](../R/regression-testing.md)**：它们使回归测试能够独立于外部系统运行，外部系统可能会随着时间的推移而变化并影响测试结果。
