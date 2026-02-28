# 模拟测试

<!-- TOC START -->
- [有关模拟测试的问题吗？](#有关模拟测试的问题吗？)
  - [基础知识和重要性](#基础知识和重要性)
    - [什么是模拟测试？](#什么是模拟测试？)
    - [为什么模拟测试在软件开发中很重要？](#为什么模拟测试在软件开发中很重要？)
    - [模拟测试和其他类型的测试之间的主要区别是什么？](#模拟测试和其他类型的测试之间的主要区别是什么？)
    - [模拟测试如何提高软件质量？](#模拟测试如何提高软件质量？)
    - [模拟测试的基本原则是什么？](#模拟测试的基本原则是什么？)
    - [软件开发项目中如何实施模拟测试？](#软件开发项目中如何实施模拟测试？)
    - [创建模拟对象涉及哪些步骤？](#创建模拟对象涉及哪些步骤？)
    - [模拟测试常用的工具有哪些？](#模拟测试常用的工具有哪些？)
    - [如何为数据库创建模拟测试？](#如何为数据库创建模拟测试？)
    - [实施模拟测试的最佳实践是什么？](#实施模拟测试的最佳实践是什么？)
  - [挑战和解决方案](#挑战和解决方案)
    - [模拟测试过程中面临哪些常见挑战？](#模拟测试过程中面临哪些常见挑战？)
    - [如何克服这些挑战？](#如何克服这些挑战？)
    - [模拟测试中常见的错误有哪些？](#模拟测试中常见的错误有哪些？)
    - [如何确保模拟测试有效？](#如何确保模拟测试有效？)
    - [如何将模拟测试集成到持续集成/持续部署（CI/CD）管道中？](#如何将模拟测试集成到持续集成持续部署（cicd）管道中？)
  - [高级概念](#高级概念)
    - [模拟测试在测试驱动开发（TDD）中的作用是什么？](#模拟测试在测试驱动开发（tdd）中的作用是什么？)
    - [模拟测试在微服务架构中如何工作？](#模拟测试在微服务架构中如何工作？)
    - [模拟测试中“存根”的概念是什么？](#模拟测试中存根的概念是什么？)
    - [测试中模拟和间谍有什么区别？](#测试中模拟和间谍有什么区别？)
<!-- TOC END -->

在测试中利用模拟对象来模仿真实对象。

## 有关模拟测试的问题吗？

### 基础知识和重要性

#### 什么是模拟测试？

[Mock testing](../M/mock-testing.md) 涉及使用 **模拟对象** 模拟真实对象的行为，以单独测试软件组件之间的交互。模拟对象被配置为返回特定值并捕获它们收到的调用。
  在[mock testing](../M/mock-testing.md) 中，您通常：

1. **设计模拟**
    模仿实际对象的行为。

2. **配置期望**
    将使用的方法和属性。

3. **执行测试**
    通过用模拟对象替换真实对象。

4. **验证**
    模拟对象按预期进行交互。
  要创建模拟对象，您可以：

  ```
  const mockObject = new Mock<SomeDependency>();
  mockObject.Setup(method => method.SomeFunction()).Returns(someValue);
  ```常用工具包括 **Mockito**、**Moq**、**Sinon.js** 和 **[Jest](../J/jest.md)**。
  对于[database](../D/database.md)，您可以模拟数据访问层或存储库，设置预期的查询及其结果：

  ```
  const mockRepository = new Mock<IDatabaseRepository>();
  mockRepository.Setup(repo => repo.Get(id)).Returns(fakeData);
  ```最佳实践包括：

- 测试用例的清晰分离。
  - 精确的期望配置以避免误报/漏报。
  - 测试之间的模拟状态的清理和重置。
  通过关注基本交互并使用工厂方法进行模拟创建，可以缓解过度模拟或维护复杂模拟[setups](../S/setup.md) 等挑战。
  为了确保有效性，请定期审查和重构模拟测试，以符合当前的系统行为和要求。
  通过将模拟测试包含在每个构建或部署上运行的 [test suite](../T/test-suite.md) 中，将模拟测试集成到 CI/CD 中。
  在 TDD 中，[mock testing](../M/mock-testing.md) 用于在实现实际组件之前测试驱动接口和交互的设计。

1. **设计模拟**
    模仿实际对象的行为。

2. **配置期望**
    将使用的方法和属性。

3. **执行测试**
    通过用模拟对象替换真实对象。

4. **验证**
    模拟对象按预期进行交互。

- 测试用例的清晰分离。
  - 精确的期望配置以避免误报/漏报。
  - 测试之间的模拟状态的清理和重置。

#### 为什么模拟测试在软件开发中很重要？

[Mock testing](../M/mock-testing.md) 在软件开发中对于隔离被测系统至关重要，确保测试不受外部依赖项或有状态组件的影响。通过使用模拟对象，开发人员可以模拟复杂的真实系统的行为，这些系统可能无法或难以配置用于测试目的。这种隔离有助于查明正在测试的代码单元内的缺陷，从而产生更可靠和可维护的代码。
  此外，[mock testing](../M/mock-testing.md) 有助于**并行测试**，允许同时测试系统的不同方面，而无需等待实际依赖项构建或可用。这可以显着**减少开发时间**并**提高效率**。
  模拟还支持**行为[verification](../V/verification.md)**，确保被测系统以预期的方式与其依赖项进行交互。这在**面向服务的架构**中尤其重要，其中组件之间的交互至关重要。
  此外，[mock testing](../M/mock-testing.md) 可以通过减少设置和维护复杂[test environments](../T/test-environment.md) 的需要来实现**成本节省**。它还允许**可重复的测试**，因为模拟对象可以配置为返回一致的结果，从而消除外部系统引起的不稳定。
  总之，[mock testing](../M/mock-testing.md) 是一种强大的技术，可以增强测试可靠性，减少与外部系统的耦合，并通过允许更加集中和受控的测试场景来加速开发过程。

#### 模拟测试和其他类型的测试之间的主要区别是什么？

[Mock testing](../M/mock-testing.md) 在几个关键方面与其他类型的测试不同：

- **隔离**：模拟通过模拟依赖关系来隔离正在测试的代码单元，确保测试不会因外部系统或组件的问题而失败。
  - **控制**：测试人员可以完全控制模拟对象的行为，使他们能够模拟各种场景，包括可能难以通过真实依赖关系重现的边缘情况和错误条件。
  - **速度**：使用模拟的测试运行速度更快，因为它们避免了设置实际依赖项并与实际依赖项交互的开销，例如 [databases](../D/database.md) 或 Web 服务。
  - **确定性**：模拟提供确定性行为，确保测试每次运行时都会产生相同的结果，而对于可能具有可变状态的真实依赖项而言，情况并非总是如此。
  - **焦点**：通过使用模拟，测试仅关注代码的逻辑，而不是与其他系统的集成，这是集成测试所涵盖的。
  以下是使用 [Jest](../J/jest.md) 在 TypeScript 中创建模拟的示例：

  ```
  import { myFunction } from './myModule';
  jest.mock('./myDependency', () => {
    return {
      myDependencyFunction: jest.fn(() => 'mocked value'),
    };
  });
  test('myFunction calls myDependencyFunction and uses the mocked value', () => {
    expect(myFunction()).toBe('mocked value');
  });
  ```相比之下，其他测试类型（例如 **[integration testing](../I/integration-testing.md)**、**[system testing](../S/system-testing.md)** 或 **[end-to-end testing](../E/end-to-end-testing.md)**）涉及使用真实系统，旨在测试应用程序的不同部分如何相互交互或与整个系统交互。

- **隔离**：模拟通过模拟依赖关系来隔离正在测试的代码单元，确保测试不会因外部系统或组件的问题而失败。
  - **控制**：测试人员可以完全控制模拟对象的行为，使他们能够模拟各种场景，包括可能难以通过真实依赖关系重现的边缘情况和错误条件。
  - **速度**：使用模拟的测试运行速度更快，因为它们避免了设置实际依赖项并与实际依赖项交互的开销，例如 [databases](../D/database.md) 或 Web 服务。
  - **确定性**：模拟提供确定性行为，确保测试每次运行时都会产生相同的结果，而对于可能具有可变状态的真实依赖项而言，情况并非总是如此。
  - **焦点**：通过使用模拟，测试仅关注代码的逻辑，而不是与其他系统的集成，这是集成测试所涵盖的。

#### 模拟测试如何提高软件质量？

[Mock testing](../M/mock-testing.md) 通过允许对组件进行**隔离测试**来增强[software quality](../S/software-quality.md)，确保每个部分都能正确运行，而不受外部依赖项的干扰。这种隔离有助于识别单元本身的缺陷，而不是与外部系统的交互，这些缺陷可以在集成测试中单独测试。
  通过使用模拟，您可以模拟各种场景，包括**错误条件**和**边缘情况**，这些场景可能难以通过实际依赖项重现。这种彻底性增强了[test coverage](../T/test-coverage.md) 并提高了软件的稳健性。
  模拟还有助于**更快、更可靠**的测试过程。由于不涉及外部系统，测试运行速度更快，并且不易因这些系统中的问题（例如网络延迟或停机）而导致失败。
  此外，[mock testing](../M/mock-testing.md) 支持**并行开发**。团队可以同时处理不同的组件，而无需等待依赖项的实际实现完成。
  最后，[mock testing](../M/mock-testing.md) 可以带来更好的**设计决策**，因为它通常需要清晰的界面和关注点分离才能有效实现。这可以带来更加模块化和可维护的代码库，这是高质量软件的标志。
  总之，[mock testing](../M/mock-testing.md) 通过实现隔离、彻底和高效的测试、促进并行开发以及鼓励良好的设计实践来改进[software quality](../S/software-quality.md)。

#### 模拟测试的基本原则是什么？

[Mock testing](../M/mock-testing.md) 依赖于几个基本原则来确保测试期间组件的有效模拟和隔离：

- **隔离**：Mock对象用于将被测系统与外部依赖项或不属于当前测试的组件隔离，确保测试不受外部因素的影响。
  - **模拟**：模拟模拟真实对象的行为，允许测试人员定义预期的交互和结果，这有助于测试系统对各种条件的反应。
  - **行为[Verification](../V/verification.md)**：使用模拟的测试通常侧重于验证被测系统是否以预期的方式与模拟进行交互，例如使用正确的参数调用方法。
  - **可配置性**：模拟具有高度可配置性，允许测试人员通过指定返回值、抛出异常或跟踪交互来设置不同的场景。
  - **可重复性**：模拟测试应该是可重复的并具有一致的结果，这对于[regression testing](../R/regression-testing.md)和持续集成至关重要。
  - **简单**：通过使用模拟，测试可以避免设置和拆除真实依赖项的复杂性，从而使测试更简单、更快。
  - **关注工作单元**：[Mock testing](../M/mock-testing.md) 鼓励通过单独测试来关注工作单元，从而促进更好的设计和更可维护的代码。
  请记住，[mock testing](../M/mock-testing.md) 应与其他测试方法结合使用以确保全面覆盖，因为它不测试与真实依赖项的集成。

- **隔离**：Mock对象用于将被测系统与外部依赖项或不属于当前测试的组件隔离，确保测试不受外部因素的影响。
  - **模拟**：模拟模拟真实对象的行为，允许测试人员定义预期的交互和结果，这有助于测试系统对各种条件的反应。
  - **行为[Verification](../V/verification.md)**：使用模拟的测试通常侧重于验证被测系统是否以预期的方式与模拟进行交互，例如使用正确的参数调用方法。
  - **可配置性**：模拟具有高度可配置性，允许测试人员通过指定返回值、抛出异常或跟踪交互来设置不同的场景。
  - **可重复性**：模拟测试应该是可重复的并具有一致的结果，这对于[regression testing](../R/regression-testing.md)和持续集成至关重要。
  - **简单**：通过使用模拟，测试可以避免设置和拆除真实依赖项的复杂性，从而使测试更简单、更快。
  - **关注工作单元**：[Mock testing](../M/mock-testing.md) 鼓励通过单独测试来关注工作单元，从而促进更好的设计和更可维护的代码。

＃＃＃ 执行

#### 软件开发项目中如何实施模拟测试？

[Mock testing](../M/mock-testing.md) 是通过一系列将模拟对象集成到测试框架中的战略步骤在软件开发项目中实现的。这是一个简洁的指南：

1. **确定依赖关系**
    被测系统 (SUT) 中需要隔离以进行单元测试的部分。

2. **设计模拟对象**
    复制真实依赖关系的行为，遵守相同的接口或契约。

3. **配置模拟对象**
    使用 Mockito、Moq 或 Sinon.js 等模拟框架返回预期数据、模拟异常或记录交互。

  ```
  // Example using Mockito in Java
  when(mockedDependency.methodToMock()).thenReturn(expectedValue);
  ```

1. **注入模拟对象**
    通常通过构造函数注入、setter 注入或依赖项注入框架将其注入到 SUT 中。

2. **写[test cases](../T/test-case.md)**
    专注于 SUT 的行为，利用模拟对象来控制测试环境。

3. **验证交互**
    SUT 和模拟对象之间，以确保使用预期参数调用正确的方法。

  ```
  // Example using Mockito in Java
  verify(mockedDependency).methodToMock();
  ```

1. **重构测试**
    当 SUT 发展时，根据需要确保模拟配置符合新的要求。

2. **集成模拟测试**
    进入自动化测试套件作为常规构建过程的一部分运行，确保它们有助于 CI/CD 反馈循环。
  通过遵循这些步骤，[mock testing](../M/mock-testing.md) 成为开发周期的无缝部分，从而可以及早发现问题并持续验证系统行为，而不受外部依赖的影响。

1. **确定依赖关系**
    被测系统 (SUT) 中需要隔离以进行单元测试的部分。

2. **设计模拟对象**
    复制真实依赖关系的行为，遵守相同的接口或契约。

3. **配置模拟对象**
    使用 Mockito、Moq 或 Sinon.js 等模拟框架返回预期数据、模拟异常或记录交互。

1. **注入模拟对象**
    通常通过构造函数注入、setter 注入或依赖项注入框架将其注入到 SUT 中。

2. **写[test cases](../T/test-case.md)**
    专注于 SUT 的行为，利用模拟对象来控制测试环境。

3. **验证交互**
    SUT 和模拟对象之间，以确保使用预期参数调用正确的方法。

1. **重构测试**
    当 SUT 发展时，根据需要确保模拟配置符合新的要求。

2. **集成模拟测试**
    进入自动化测试套件作为常规构建过程的一部分运行，确保它们有助于 CI/CD 反馈循环。

#### 创建模拟对象涉及哪些步骤？

创建模拟对象通常涉及以下步骤：

1. **确定要用模拟替换的依赖项**。这可以是外部服务、[database](../D/database.md) 或您的系统与之交互的任何其他组件。
  2. **定义依赖的接口**或类。模拟是基于真实对象实现的相同接口创建的。
  3. **使用模拟框架**创建模拟对象的实例。流行的框架包括用于 Java 的 Mockito、用于 .NET 的 Moq 和用于 JavaScript 的[Jest](../J/jest.md)。

    ```
    MyDependency mockDependency = Mockito.mock(MyDependency.class);
    ```

4. **配置模拟的行为**，以指定调用其方法时应发生的情况。这包括设置返回值或引发异常。

    ```
    Mockito.when(mockDependency.method()).thenReturn(value);
    ```

5. **将模拟注入**到被测系统中，替换真正的依赖项。这可以通过构造函数注入、setter 注入或使用依赖注入框架来完成。
  6. **编写测试**来测试被测系统，该系统现在使用模拟对象。
  7. **验证与模拟的交互**，以确保被测系统行为正确。这可能包括检查方法是否使用正确的参数调用或调用了一定次数。

    ```
    Mockito.verify(mockDependency).method(expectedArgument);
    ```

8. **运行测试**并检查结果。如果测试失败，请调查并纠正被测系统的行为或根据需要更新模拟配置。
  1. **确定要用模拟替换的依赖项**。这可以是外部服务、[database](../D/database.md) 或您的系统与之交互的任何其他组件。
  2. **定义依赖的接口**或类。模拟是基于真实对象实现的相同接口创建的。
  3. **使用模拟框架**创建模拟对象的实例。流行的框架包括用于 Java 的 Mockito、用于 .NET 的 Moq 和用于 JavaScript 的 [Jest](../J/jest.md)。

    ```
    MyDependency mockDependency = Mockito.mock(MyDependency.class);
    ```

4. **配置模拟的行为**，以指定调用其方法时应发生的情况。这包括设置返回值或引发异常。

    ```
    Mockito.when(mockDependency.method()).thenReturn(value);
    ```

5. **将模拟注入**到被测系统中，替换真正的依赖项。这可以通过构造函数注入、setter 注入或使用依赖注入框架来完成。
  6. **编写测试**来测试被测系统，该系统现在使用模拟对象。
  7. **验证与模拟的交互**，以确保被测系统行为正确。这可能包括检查方法是否使用正确的参数调用或调用了一定次数。

    ```
    Mockito.verify(mockDependency).method(expectedArgument);
    ```

8. **运行测试**并检查结果。如果测试失败，请调查并纠正被测系统的行为或根据需要更新模拟配置。

#### 模拟测试常用的工具有哪些？

[mock testing](../M/mock-testing.md) 的常用工具包括：

- **Mockito**：一种流行的 Java 模拟框架，允许您创建和配置模拟对象。使用示例：

    ```
    List mockedList = Mockito.mock(List.class);
    ```

- **Moq**：在.NET 中广泛用于使用流畅的 [API](../A/api.md) 创建模拟对象。例子：

    ```
    var mock = new Mock<IService>();
    ```

- **Sinon.js**：一个多功能的 JavaScript 模拟库，适用于 [Node.js](../N/node-js.md) 和浏览器环境。例子：

    ```
    const sinon = require('sinon');
    let mock = sinon.mock(myObj);
    ```

- **unittest.mock**：Python 标准库中的模拟库。例子：

    ```
    from unittest.mock import MagicMock
    mock = MagicMock()
    ```

- **RSpec Mocks**：一个模拟框架，是 Ruby 的 RSpec 测试库的一部分。例子：

    ```
    mock_model = double('Model')
    ```

- **[Jest](../J/jest.md)**：为 JavaScript 测试（特别是 React 应用程序）提供内置模拟库。例子：

    ```
    jest.mock('module_name');
    ```

- **NSubstitute**：.NET 的友好模拟库，具有简单明了的语法。例子：

    ```
    var substitute = Substitute.For<IService>();
    ```

- **EasyMock**：另一个为接口提供模拟对象的 Java 模拟库。例子：

    ```
    IMockBuilder<SomeClass> builder = EasyMock.createMockBuilder(SomeClass.class);
    ```这些工具提供了各种功能来创建、配置和验证模拟对象，有助于隔离被测系统并专注于被测试的行为。

- **Mockito**：一种流行的 Java 模拟框架，允许您创建和配置模拟对象。使用示例：

    ```
    List mockedList = Mockito.mock(List.class);
    ```

- **Moq**：在.NET 中广泛用于使用流畅的 [API](../A/api.md) 创建模拟对象。例子：

    ```
    var mock = new Mock<IService>();
    ```

- **Sinon.js**：一个多功能的 JavaScript 模拟库，适用于 [Node.js](../N/node-js.md) 和浏览器环境。例子：

    ```
    const sinon = require('sinon');
    let mock = sinon.mock(myObj);
    ```

- **unittest.mock**：Python 标准库中的模拟库。例子：

    ```
    from unittest.mock import MagicMock
    mock = MagicMock()
    ```

- **RSpec Mocks**：一个模拟框架，是 Ruby 的 RSpec 测试库的一部分。例子：

    ```
    mock_model = double('Model')
    ```

- **[Jest](../J/jest.md)**：为 JavaScript 测试（特别是 React 应用程序）提供内置模拟库。例子：

    ```
    jest.mock('module_name');
    ```

- **NSubstitute**：.NET 的友好模拟库，具有简单明了的语法。例子：

    ```
    var substitute = Substitute.For<IService>();
    ```

- **EasyMock**：另一个为接口提供模拟对象的 Java 模拟库。例子：

    ```
    IMockBuilder<SomeClass> builder = EasyMock.createMockBuilder(SomeClass.class);
    ```

#### 如何为数据库创建模拟测试？

要为 [database](../D/database.md) 创建模拟测试，请按照以下步骤操作：

1. **识别您的应用程序执行的需要测试的[database](../D/database.md) 操作**。
  2. **选择与您的测试环境兼容的模拟框架**，例如用于 Java 的 Mockito 或用于 .NET 的 Moq。
  3. **创建一个模拟[database](../D/database.md) 接口**，代表实际的[database](../D/database.md) 操作。此接口应模仿真实[database](../D/database.md) 服务的行为。

    ```
    public interface DatabaseService {
        User getUserById(String id);
        void updateUser(User user);
    }
    ```

4. **使用您选择的模拟框架实现模拟对象**。定义每个操作的预期行为，包括返回值或异常。

    ```
    DatabaseService mockDatabase = mock(DatabaseService.class);
    when(mockDatabase.getUserById("123")).thenReturn(new User("123", "Test User"));
    doThrow(new DatabaseException()).when(mockDatabase).updateUser(any(User.class));
    ```

5. **将模拟对象**注入到被测系统中，替换真正的[database](../D/database.md)依赖项。
  6. **使用模拟对象编写[test cases](../T/test-case.md)**，以通过受控、可预测的[database](../D/database.md) 交互来验证系统的行为。

    ```
    @Test
    public void testGetUser() {
        User user = userService.getUserById("123");
        assertEquals("Test User", user.getName());
    }
    ```

7. **运行测试**以确保它们通过模拟[database](../D/database.md)。根据需要调整模拟的行为以覆盖不同的场景。
  通过将系统与真实的[database](../D/database.md)隔离，您可以测试各种数据条件和错误情况，而无需依赖实际的[database](../D/database.md)，从而实现更快、更可靠的测试。

1. **识别您的应用程序执行的需要测试的[database](../D/database.md) 操作**。
  2. **选择与您的测试环境兼容的模拟框架**，例如用于 Java 的 Mockito 或用于 .NET 的 Moq。
  3. **创建一个模拟[database](../D/database.md) 接口**，代表实际的[database](../D/database.md) 操作。该接口应该模仿真实[database](../D/database.md) 服务的行为。

    ```
    public interface DatabaseService {
        User getUserById(String id);
        void updateUser(User user);
    }
    ```

4. **使用您选择的模拟框架实现模拟对象**。定义每个操作的预期行为，包括返回值或异常。

    ```
    DatabaseService mockDatabase = mock(DatabaseService.class);
    when(mockDatabase.getUserById("123")).thenReturn(new User("123", "Test User"));
    doThrow(new DatabaseException()).when(mockDatabase).updateUser(any(User.class));
    ```

5. **将模拟对象**注入到被测系统中，替换真正的[database](../D/database.md)依赖项。
  6. **使用模拟对象编写[test cases](../T/test-case.md)**，以通过受控、可预测的[database](../D/database.md) 交互来验证系统的行为。

    ```
    @Test
    public void testGetUser() {
        User user = userService.getUserById("123");
        assertEquals("Test User", user.getName());
    }
    ```

7. **运行测试**以确保它们通过模拟[database](../D/database.md)。根据需要调整模拟的行为以覆盖不同的场景。

#### 实施模拟测试的最佳实践是什么？

实施 [mock testing](../M/mock-testing.md) 的最佳实践包括：

- **设计可测试性**：确保您的代码是模块化的，以便轻松隔离组件以进行模拟。
  - **使用清晰的、描述性的命名约定**：命名模拟及其方法以反映其目的和行为。
  - **维护模拟**：根据它们模拟的实际组件的变化来更新模拟实现。
  - **避免过度模拟**：仅模拟隔离工作单元所必需的内容，以防止脆弱的测试。
  - **验证交互**：检查被测系统是否按预期与模拟进行交互。
  - **保持测试集中**：每个测试都应该验证行为的一个方面，以在测试失败时简化调试。
  - **使用依赖注入**：将模拟注入到被测系统中以替换真正的依赖项。
  - **设置期望**：定义模拟在使用之前应如何表现，包括返回值和异常。
  - **清理**：每次测试后重置或处置模拟，以避免测试之间的状态泄漏。
  - **记录模拟行为**：对复杂的模拟设置或行为进行评论，以帮助未来维护人员理解。
  - **审查模拟用法**：定期审查模拟用法，以确保它仍然与依赖项的实际行为保持一致。

  ```
  // Example of a mock setup with clear naming and behavior definition
  const mockService = {
    fetchData: jest.fn().mockResolvedValue({ data: 'mocked data' })
  };
  // Injecting the mock service
  const systemUnderTest = new SystemUnderTest(mockService);
  // Setting expectations and verifying interactions
  expect(mockService.fetchData).toHaveBeenCalledTimes(1);
  ```

- **平衡模拟保真度**：确保模拟足够准确，能够忠实地表示真实组件，而不会产生不必要的复杂性。
  - **自动化模拟更新**：使用可以根据实际组件接口自动生成和更新模拟的工具。
  - **设计可测试性**：确保您的代码是模块化的，以便轻松隔离组件以进行模拟。
  - **使用清晰的、描述性的命名约定**：命名模拟及其方法以反映其目的和行为。
  - **维护模拟**：根据它们模拟的实际组件的变化来更新模拟实现。
  - **避免过度模拟**：仅模拟隔离工作单元所必需的内容，以防止脆弱的测试。
  - **验证交互**：检查被测系统是否按预期与模拟进行交互。
  - **保持测试集中**：每个测试都应该验证行为的一个方面，以在测试失败时简化调试。
  - **使用依赖注入**：将模拟注入到被测系统中以替换真正的依赖项。
  - **设置期望**：定义模拟在使用之前应如何表现，包括返回值和异常。
  - **清理**：每次测试后重置或处置模拟，以避免测试之间的状态泄漏。
  - **记录模拟行为**：对复杂的模拟设置或行为进行评论，以帮助未来维护人员理解。
  - **审查模拟用法**：定期审查模拟用法，以确保它仍然与依赖项的实际行为保持一致。
  - **平衡模拟保真度**：确保模拟足够准确，能够忠实地表示真实组件，而不会产生不必要的复杂性。
  - **自动化模拟更新**：使用可以根据实际组件接口自动生成和更新模拟的工具。

### 挑战和解决方案

#### 模拟测试过程中面临哪些常见挑战？

[mock testing](../M/mock-testing.md) 中的常见挑战包括：

- **过度模拟**：过度使用模拟可能会导致测试脆弱且对实现中的更改过于敏感，从而使其难以维护。
  - **复杂性**：为复杂的依赖项或具有复杂行为的系统创建模拟可能非常耗时且容易出错。
  - **行为保真度**：确保模拟准确地复制它们所代表的真实对象的行为可能具有挑战性，导致测试中出现误报或漏报。
  - **测试可读性**：具有大量模拟或复杂设置的测试可能会变得难以理解，从而降低了其作为文档的价值。
  - **集成缺陷**：模拟可以隐藏组件之间的集成和交互问题，这些问题可能只会在更高级别的集成测试或生产中出现。
  - **状态管理**：管理不同测试用例之间的模拟状态可能很麻烦，特别是在测试未正确隔离时。
  - **工具限制**：模拟框架和工具可能存在限制，阻止某些行为被模拟，或者它们可能不支持最新的语言功能或框架。
  为了应对这些挑战，请采取以下做法：

- **最小模拟**：仅模拟隔离正在测试的工作单元所需的内容。
  - **清晰的抽象**：为组件设计清晰的接口，使它们更容易模拟。
  - **[Incremental Testing](../I/incremental-testing.md)** ：用集成测试补充模拟测试以捕获交互缺陷。
  - **测试隔离**：确保每个测试都是独立的并管理自己的模拟状态。
  - **文档**：记录复杂的模拟设置以帮助理解。
  - **工具熟练程度**：随时了解所选模拟工具的功能和最佳实践。
  - **过度模拟**：过度使用模拟可能会导致测试脆弱且对实现中的更改过于敏感，从而使其难以维护。
  - **复杂性**：为复杂的依赖项或具有复杂行为的系统创建模拟可能非常耗时且容易出错。
  - **行为保真度**：确保模拟准确地复制它们所代表的真实对象的行为可能具有挑战性，导致测试中出现误报或漏报。
  - **测试可读性**：具有大量模拟或复杂设置的测试可能会变得难以理解，从而降低了其作为文档的价值。
  - **集成缺陷**：模拟可以隐藏组件之间的集成和交互问题，这些问题可能只会在更高级别的集成测试或生产中出现。
  - **状态管理**：管理不同测试用例之间的模拟状态可能很麻烦，特别是在测试未正确隔离时。
  - **工具限制**：模拟框架和工具可能存在限制，阻止某些行为被模拟，或者它们可能不支持最新的语言功能或框架。
  - **最小模拟**：仅模拟隔离正在测试的工作单元所需的内容。
  - **清晰的抽象**：为组件设计清晰的接口，使它们更容易模拟。
  - **[Incremental Testing](../I/incremental-testing.md)** ：用集成测试补充模拟测试以捕获交互缺陷。
  - **测试隔离**：确保每个测试都是独立的并管理自己的模拟状态。
  - **文档**：记录复杂的模拟设置以帮助理解。
  - **工具熟练程度**：随时了解所选模拟工具的功能和最佳实践。

#### 如何克服这些挑战？

克服[mock testing](../M/mock-testing.md) 中的挑战需要战略方法和对细节的关注。以下是一些策略：

- **重构代码以实现可测试性**：确保代码库的设计考虑到了测试，这通常意味着使用支持依赖注入和松散耦合的设计模式。
  - **使用抽象层**：为外部服务和依赖项创建抽象层。这允许更容易的模拟并降低测试的复杂性。
  - **投资高质量的模拟框架**：利用有据可查且得到广泛支持的强大模拟框架。这可以简化模拟对象的创建和管理。
  - **定期审查和更新模拟**：使模拟对象和响应与它们所代表的依赖项的实际行为保持同步，以避免 [false positives](../F/false-positive.md) 或负面影响。
  - **自动模拟数据生成**：实施工具或脚本来自动生成模拟数据，确保[test cases](../T/test-case.md) 集多样化且真实。
  - **将模拟集成到 [Automated Testing](../A/automated-testing.md) 管道**：确保模拟测试是 [automated testing](../A/automated-testing.md) 套件的一部分，并作为 CI/CD 流程的一部分执行。
  - **监控[Test Coverage](../T/test-coverage.md)**：使用[code coverage](../C/code-coverage.md)工具来识别未测试的区域并相应地调整模拟测试。
  - **教育团队**：向团队提供有关最佳实践和正确使用 [mock testing](../M/mock-testing.md) 的培训和资源，以避免常见陷阱。
  - **同行评审**：对测试代码进行代码评审，包括模拟测试，以尽早发现问题并在团队内分享知识。
  - **平衡模拟与端到端测试**：用端到端测试补充模拟测试，以确保系统在类似生产的环境中按预期工作。
  通过实施这些策略，[test automation](../T/test-automation.md) 工程师可以缓解与[mock testing](../M/mock-testing.md) 相关的挑战，并提高[test suites](../T/test-suite.md) 的可靠性和有效性。

- **重构代码以实现可测试性**：确保代码库的设计考虑到了测试，这通常意味着使用支持依赖注入和松散耦合的设计模式。
  - **使用抽象层**：为外部服务和依赖项创建抽象层。这允许更容易的模拟并降低测试的复杂性。
  - **投资高质量的模拟框架**：利用有据可查且得到广泛支持的强大模拟框架。这可以简化模拟对象的创建和管理。
  - **定期审查和更新模拟**：使模拟对象和响应与它们所代表的依赖项的实际行为保持同步，以避免 [false positives](../F/false-positive.md) 或负面影响。
  - **自动模拟数据生成**：实施工具或脚本来自动生成模拟数据，确保[test cases](../T/test-case.md) 集多样化且真实。
  - **将模拟集成到 [Automated Testing](../A/automated-testing.md) 管道**：确保模拟测试是 [automated testing](../A/automated-testing.md) 套件的一部分，并作为 CI/CD 流程的一部分执行。
  - **监控[Test Coverage](../T/test-coverage.md)**：使用[code coverage](../C/code-coverage.md)工具来识别未测试的区域并相应地调整模拟测试。
  - **教育团队**：向团队提供关于最佳实践和正确使用 [mock testing](../M/mock-testing.md) 的培训和资源，以避免常见陷阱。
  - **同行评审**：对测试代码进行代码评审，包括模拟测试，以尽早发现问题并在团队内分享知识。
  - **平衡模拟与端到端测试**：用端到端测试补充模拟测试，以确保系统在类似生产的环境中按预期工作。

#### 模拟测试中常见的错误有哪些？

[mock testing](../M/mock-testing.md)期间的常见错误包括：

- **过度使用模拟**：过度依赖模拟可能会导致测试脆弱且不能代表现实场景。谨慎使用模拟，并且仅在必要时使用。
  - **不验证交互**：忘记验证被测系统是否按预期与模拟进行交互可能会导致遗漏缺陷。始终检查是否使用正确的参数调用了预期的方法。
  - **模拟您不拥有的东西**：为不受您的团队控制的外部依赖项创建模拟可能会导致测试在这些外部系统发生更改时中断。仅模拟您拥有或控制的组件。
  - **模拟配置不足**：错误设置模拟可能会导致[false positives](../F/false-positive.md) 或负面结果。确保模拟配置为准确模仿真实组件的行为。
  - **忽略副作用**：某些方法具有需要由模拟复制的副作用。忽视这些可能会导致测试不完整。
  - **不更新模拟**：随着代码库的发展，必须更新模拟以反映变化。过时的模拟可能会导致测试不正确地通过或在不应该的情况下失败。
  - **过度指定模拟**：设置模拟以期望具有精确参数的非常具体的调用可能会使测试变得脆弱。使用参数匹配器可以实现一定的灵活性。
  - **不隔离测试**：如果模拟 [setup](../S/setup.md) 或状态在测试之间共享，则可能导致测试间依赖和不可预测的结果。隔离每个[test case](../T/test-case.md)以确保它们独立运行。
  - **缺乏理解**：误解被模拟的系统可能会导致错误的假设和无效的测试。在模拟系统之前先彻底了解系统。
  - **过度使用模拟**：过度依赖模拟可能会导致测试脆弱且不能代表现实场景。谨慎使用模拟，并且仅在必要时使用。
  - **不验证交互**：忘记验证被测系统是否按预期与模拟进行交互可能会导致遗漏缺陷。始终检查是否使用正确的参数调用了预期的方法。
  - **模拟您不拥有的东西**：为不受您的团队控制的外部依赖项创建模拟可能会导致测试在这些外部系统发生更改时中断。仅模拟您拥有或控制的组件。
  - **模拟配置不足**：错误设置模拟可能会导致[false positives](../F/false-positive.md) 或负面结果。确保模拟配置为准确模仿真实组件的行为。
  - **忽略副作用**：某些方法具有需要由模拟复制的副作用。忽视这些可能会导致测试不完整。
  - **不更新模拟**：随着代码库的发展，必须更新模拟以反映变化。过时的模拟可能会导致测试不正确地通过或在不应该的情况下失败。
  - **过度指定模拟**：设置模拟以期望具有精确参数的非常具体的调用可能会使测试变得脆弱。使用参数匹配器可以实现一定的灵活性。
  - **不隔离测试**：如果模拟 [setup](../S/setup.md) 或状态在测试之间共享，则可能导致测试间依赖和不可预测的结果。隔离每个[test case](../T/test-case.md)以确保它们独立运行。
  - **缺乏理解**：误解被模拟的系统可能会导致错误的假设和无效的测试。在模拟系统之前先彻底了解系统。

#### 如何确保模拟测试有效？

为确保**模拟测试**有效：

- **验证模拟配置**：确保正确设置模拟以模仿预期行为。不正确的配置可能会导致[false positives](../F/false-positive.md) 或负面结果。
  - **保持模拟最新**：定期更新模拟以反映它们所代表的实际依赖项的变化。
  - **验证交互**：使用[verification](../V/verification.md)方法来检查被测系统是否按预期与模拟进行交互。
  - **隔离被测系统**：确保模拟是测试中的唯一变量，以准确评估系统的行为。
  - **使用实际数据**：模拟应该返回代表实际依赖关系将产生的数据。
  - **测试边缘情况**：包括测试系统如何通过模拟处理异常或边界条件的场景。
  - **审查和重构**：定期审查模拟测试以消除冗余并提高清晰度。
  - **与其他测试类型配对**：将模拟测试与其他测试方法相结合，以覆盖更多场景并增加对系统可靠性的信心。
  - **自动化模拟测试**：将模拟测试集成到您的自动化[test suite](../T/test-suite.md)中，以一致地运行它们并尽早捕获回归。
  - **监控覆盖率**：使用 [code coverage](../C/code-coverage.md) 工具确保模拟测试覆盖预期的代码路径。
  - **同行评审**：让同行评审模拟测试，以发现原作者可能忽略的问题。
  通过遵循这些准则，您可以提高模拟测试的有效性，并为更加强大和可靠的 [software testing](../S/software-testing.md) 流程做出贡献。

- **验证模拟配置**：确保正确设置模拟以模仿预期行为。不正确的配置可能会导致[false positives](../F/false-positive.md) 或负面结果。
  - **保持模拟最新**：定期更新模拟以反映它们所代表的实际依赖项的变化。
  - **验证交互**：使用 [verification](../V/verification.md) 方法来检查被测系统是否按预期与模拟进行交互。
  - **隔离被测系统**：确保模拟是测试中的唯一变量，以准确评估系统的行为。
  - **使用实际数据**：模拟应该返回代表实际依赖关系将产生的数据。
  - **测试边缘情况**：包括测试系统如何通过模拟处理异常或边界条件的场景。
  - **审查和重构**：定期审查模拟测试以消除冗余并提高清晰度。
  - **与其他测试类型配对**：将模拟测试与其他测试方法相结合，以覆盖更多场景并增加对系统可靠性的信心。
  - **自动化模拟测试**：将模拟测试集成到您的自动化[test suite](../T/test-suite.md)中，以一致地运行它们并尽早捕获回归。
  - **监控覆盖率**：使用 [code coverage](../C/code-coverage.md) 工具确保模拟测试覆盖预期的代码路径。
  - **同行评审**：让同行评审模拟测试，以发现原作者可能忽略的问题。

#### 如何将模拟测试集成到持续集成/持续部署（CI/CD）管道中？

将 [mock testing](../M/mock-testing.md) 集成到 CI/CD 管道中涉及自动执行模拟测试，作为构建和部署过程的一部分。这是一个简洁的指南：

1. **创建模拟测试**
    使用您喜欢的模拟框架。

2. **配置您的 CI/CD 工具**
    触发模拟测试。这可以通过在管道配置文件中包含测试阶段来完成。

3. **使用脚本**
    设置和拆除任何所需的模拟环境或服务。

4. **运行模拟测试**
    在进行集成测试之前，以确保组件在模拟其依赖项的情况下按预期运行。

5. **分析测试结果**
    自动。如果模拟测试失败，管道应该停止，以防止错误传播。

6. **报告生成**
    应该是自动化的，提供模拟测试结果的可见性。

7. **维护模拟测试**
    作为您的代码库的一部分，确保它们与您的应用程序一起发展。

  ```
  stages:
    - build
    - test
    - deploy
  test:
    stage: test
    script:
      - setup-mocks.sh
      - run-mock-tests.sh
    only:
      - master
  ```在上面的示例中，`setup-mocks.sh` 将配置必要的模拟对象和服务，而 `run-mock-tests.sh` 将执行模拟测试。 `only` 指令确保模拟测试在 master 分支上运行，这通常是部署之前发生合并的地方。

1. **创建模拟测试**
    使用您喜欢的模拟框架。

2. **配置您的 CI/CD 工具**
    触发模拟测试。这可以通过在管道配置文件中包含测试阶段来完成。

3. **使用脚本**
    设置和拆除任何所需的模拟环境或服务。

4. **运行模拟测试**
    在进行集成测试之前，以确保组件在模拟其依赖项的情况下按预期运行。

5. **分析测试结果**
    自动。如果模拟测试失败，管道应该停止，以防止错误传播。

6. **报告生成**
    应该是自动化的，提供模拟测试结果的可见性。

7. **维护模拟测试**
    作为您的代码库的一部分，确保它们与您的应用程序一起发展。

### 高级概念

#### 模拟测试在测试驱动开发（TDD）中的作用是什么？

在 **测试驱动开发 (TDD)** 中，[mock testing](../M/mock-testing.md) 通过模拟尚未实现或无法包含在单元测试中的真实对象的行为，发挥着关键作用。通过使用模拟，开发人员可以专注于被测试的单元，确保测试是隔离的，不依赖于外部系统或复杂的依赖关系。
  在编写失败测试、实现最少代码以通过测试、然后重构的 TDD 周期中，通常在第一阶段引入模拟。它们有助于指定与依赖项的预期交互，从而驱动接口的设计。当这些依赖项的实际实现可能非常耗时或者会在测试中引入不稳定时，这特别有用。
  模拟使开发人员能够验证是否使用预期参数调用了正确的方法，这对于系统不同部分之间的契约至关重要。这使得设计更加模块化并遵守**单一职责原则**。
  此外，通过使用模拟，TDD 中的反馈循环显着缩短，因为无需等待实际依赖项响应或可用。这加快了开发进程并有助于保持稳定的步伐。

  ```
  // Example of using a mock in TDD (TypeScript)
  test('should call dependency method with correct parameters', () => {
    const mockDependency = {
      performAction: jest.fn()
    };
    const systemUnderTest = new SystemUnderTest(mockDependency);
    systemUnderTest.execute();
    expect(mockDependency.performAction).toHaveBeenCalledWith('expected-param');
  });
  ```总之，TDD 中的[mock testing](../M/mock-testing.md) 确保每个单元都可以单独测试，支持更好的设计，并加快开发周期。

#### 模拟测试在微服务架构中如何工作？

在**微服务架构**中，[mock testing](../M/mock-testing.md) 涉及模拟微服务与之交互的外部服务的行为。这允许对相关服务进行**隔离测试**。
  要在微服务中实现[mock testing](../M/mock-testing.md)：

1. 识别
    **外部依赖**
    的微服务。

2. 创建
    **模拟对象**
    或
    **存根**
    使用模拟框架或工具来处理这些依赖项。

3. 配置微服务以在测试执行期间使用这些模拟而不是实际服务。
  4. 编写测试用例来执行微服务的功能，断言它在模拟接口上的行为正确。
  微服务中的模拟对于以下方面特别有用：

- **测试错误处理**
    通过模拟依赖关系的失败。

- **并行开发**
    相关服务尚不可用或正在同时开发。

- **持续集成**
    确保测试可以独立于环境运行。
  使用 JavaScript 模拟库的示例：

  ```
  const { myMicroservice } = require('./myMicroservice');
  const { mockDependencyService } = require('mocking-library');
  test('should handle dependency failure gracefully', () => {
    mockDependencyService({
      endpoint: '/external-service',
      method: 'GET',
      response: { status: 500 }
    });
    const response = myMicroservice.handleExternalService();
    expect(response).toEqual('Error handling logic executed');
  });
  ```**最佳实践**包括：

- 确保模拟
    **准确反映**
    真正依赖的行为。

- 保留模拟配置
    **最新**
    与服务合同。

- 使用
    **合同测试**
    验证模拟和实际服务是否符合预期的交互。

1. 识别
    **外部依赖**
    的微服务。

2. 创建
    **模拟对象**
    或
    **存根**
    使用模拟框架或工具来处理这些依赖项。

3. 配置微服务以在测试执行期间使用这些模拟而不是实际服务。
  4. 编写测试用例来执行微服务的功能，断言它在模拟接口上的行为正确。
  - **测试错误处理**
    通过模拟依赖关系的失败。

- **并行开发**
    相关服务尚不可用或正在同时开发。

- **持续集成**
    确保测试可以独立于环境运行。

- 确保模拟
    **准确反映**
    真正依赖的行为。

- 保留模拟配置
    **最新**
    与服务合同。

- 使用
    **合同测试**
    验证模拟和实际服务是否符合预期的交互。

#### 模拟测试中“存根”的概念是什么？

存根是 **[mock testing](../M/mock-testing.md)** 中使用的一种技术，用于用返回预定响应的 **简化实现** 替换被测系统的某些部分。它是**测试替身**的一种形式，代表实际功能，但由于副作用、缓慢或不确定性，这些功能要么未实现，要么在测试期间无法使用。
  与成熟的模拟不同，存根通常对如何调用它们没有期望。它们主要用于通过返回特定值或抛出异常来**控制被测系统的行为**，从而允许测试专注于由这些响应触发的代码路径。
  以下是使用流行存根库 Sinon.js 的 TypeScript 示例：

  ```
  import sinon from 'sinon';
  import { MyService } from './my-service';
  import { expect } from 'chai';
  describe('MyService', () => {
    it('should handle the response from a stubbed dependency', () => {
      const myService = new MyService();
      const stub = sinon.stub(myService, 'dependencyMethod').returns('stubbed value');
      const result = myService.callDependencyMethod();
      expect(result).to.equal('stubbed value');
      stub.restore();
    });
  });
  ```在此示例中，每当在 `MyService` 内调用 `dependencyMethod` 时，它都会被存根以返回 `'stubbed value'`。这允许测试验证行为而不依赖于 `dependencyMethod` 的实际实现。
  在处理**外部服务**、**[database](../D/database.md) 调用**或任何其他会在测试中引入复杂性或不确定性的组件时，存根特别有用。它有助于创建 **隔离** 和 **可预测** [test environments](../T/test-environment.md)，其中重点是正在测试的代码单元。

#### 如何使用模拟测试进行性能测试？

[Mock testing](../M/mock-testing.md) 可以在[performance testing](../P/performance-testing.md) 中使用来模拟那些不可用或成本太高而无法包含在全面性能测试中的组件的行为。通过用模拟替换这些组件，您可以**隔离**并测试负载下系统特定部分的性能，而无需外部系统的开销或干扰。
  例如，如果您正在测试依赖于第三方服务的应用程序，则可以使用模拟来**模拟真实服务的延迟**和**吞吐量**。这使您能够：

- **控制[test environment](../T/test-environment.md)**
    通过消除可能引入可变性的外部依赖性，可以更加可预测地实现。

- **模拟各种场景**
    ，例如高延迟或低带宽，以了解您的应用程序在不同条件下的行为方式。

- **压力测试**
    通过模拟高负载来控制各个组件，这对于实际的相关服务来说可能是不可能或不实用的。
  以下是在性能 [test scenario](../T/test-scenario.md) 中为服务创建模拟的示例：

  ```
  // Mock service that simulates a delay
  function mockService(delay) {
    return new Promise((resolve) => setTimeout(resolve, delay));
  }
  // Performance test using the mock service
  async function performanceTest() {
    const startTime = performance.now();
    await mockService(100); // Simulates a 100ms delay
    const endTime = performance.now();
    console.log(`Service call took ${endTime - startTime} milliseconds`);
  }
  ```在此代码中，`mockService` 模拟具有指定延迟的服务调用，`performanceTest` 测量完成调用所需的时间。通过调整延迟，您可以测试系统如何处理不同的响应时间。
  在[performance testing](../P/performance-testing.md) 中使用模拟是一种**经济高效**且**灵活**的方法，可以识别瓶颈并优化被测系统的性能。

- **控制[test environment](../T/test-environment.md)**
    通过消除可能引入可变性的外部依赖性，可以更加可预测地实现。

- **模拟各种场景**
    ，例如高延迟或低带宽，以了解您的应用程序在不同条件下的行为方式。

- **压力测试**
    通过模拟高负载来控制各个组件，这对于实际的相关服务来说可能是不可能或不实用的。

#### 测试中模拟和间谍有什么区别？

在[test automation](../T/test-automation.md) 中，**mock** 和 **spies** 在隔离代码单元进行测试时具有不同的目的。 **模拟**是一个替换真实组件的对象，具有预先编程的行为和期望集。它用于验证被测系统和模拟系统之间的交互。

  ```
  // Example of a mock
  const mockObject = {
    method: jest.fn().mockReturnValue("mocked value")
  };
  ```另一方面，**spy** 用于包装现有函数，允许测试记录有关如何使用该函数的信息，而不改变其行为。间谍可以跟踪函数调用、参数和返回值，如果需要，他们还可以更改函数的行为。

  ```
  // Example of a spy
  const spy = jest.spyOn(realObject, 'method');
  ```主要区别在于它们的用法：

- **模拟**
    是关于创建具有预设行为的接口或类的假版本，它们通常在实际实现无关或需要针对测试场景进行控制时使用。

- **间谍**
    是关于收集有关在测试执行期间如何使用函数的信息。当您需要断言使用正确的参数或正确的次数调用某些函数而不更改实际的实现时，它们非常有用。
  两者在不同的上下文中都很有价值，模拟更多的是控制外部依赖关系，间谍更多的是观察它们。

- **模拟**
    是关于创建具有预设行为的接口或类的假版本，它们通常在实际实现无关或需要针对测试场景进行控制时使用。

- **间谍**
    是关于收集有关在测试执行期间如何使用函数的信息。当您需要断言使用正确的参数或正确的次数调用某些函数而不更改实际的实现时，它们非常有用。
