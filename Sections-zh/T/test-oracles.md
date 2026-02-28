# 测试预言机

<!-- TOC START -->
- [相关术语：](#相关术语：)
- [关于测试预言机的问题？](#关于测试预言机的问题？)
  - [基础知识和重要性](#基础知识和重要性)
    - [软件测试中的测试预言机是什么？](#软件测试中的测试预言机是什么？)
    - [为什么测试预言机在软件测试中很重要？](#为什么测试预言机在软件测试中很重要？)
    - [测试预言机在端到端测试中扮演什么角色？](#测试预言机在端到端测试中扮演什么角色？)
    - [测试预言机如何提高软件产品的整体质量？](#测试预言机如何提高软件产品的整体质量？)
  - [类型和示例](#类型和示例)
    - [测试预言机有哪些不同类型？](#测试预言机有哪些不同类型？)
    - [您能否提供每种类型的测试预言机的示例？](#您能否提供每种类型的测试预言机的示例？)
    - [不同类型的测试预言机如何影响测试过程？](#不同类型的测试预言机如何影响测试过程？)
    - [Test Oracle 使用的一些实际示例有哪些？](#test-oracle-使用的一些实际示例有哪些？)
  - [实施和使用](#实施和使用)
    - [测试预言机是如何在测试框架中实现的？](#测试预言机是如何在测试框架中实现的？)
    - [在测试用例中使用测试预言机的步骤是什么？](#在测试用例中使用测试预言机的步骤是什么？)
    - [使用测试预言机的最佳实践是什么？](#使用测试预言机的最佳实践是什么？)
    - [测试预言机如何用于自动化测试？](#测试预言机如何用于自动化测试？)
  - [挑战和解决方案](#挑战和解决方案)
    - [使用测试预言机时面临哪些常见挑战？](#使用测试预言机时面临哪些常见挑战？)
    - [如何克服这些挑战？](#如何克服这些挑战？)
    - [测试预言机有哪些限制？](#测试预言机有哪些限制？)
    - [如何衡量测试预言机的有效性？](#如何衡量测试预言机的有效性？)
<!-- TOC END -->

确定测试是否成功的机制。

## 相关术语：

- [Test Stub](../T/test-stub.md)

## 关于测试预言机的问题？

### 基础知识和重要性

#### 软件测试中的测试预言机是什么？

**测试预言机**是一种机制或原则，用于确定软件系统在测试期间是否产生正确的结果。它充当事实来源，可以与测试的 [actual results](../A/actual-result.md) 进行比较以确定正确性。 [Test Oracles](../T/test-oracles.md) 可以是显式的，例如[test case](../T/test-case.md) 中指定的[expected results](../E/expected-result.md)，也可以是隐式的，依赖于有关系统行为的一般知识或假设。
  在实践中，[Test Oracles](../T/test-oracles.md) 可以像函数期望的**硬编码值**一样简单，也可以像预测一系列可接受结果的**模型**一样复杂。它们也可以是**启发式的**，其中 Oracle 是经验法则而不是精确的期望，或者是**统计性的**，使用概率来确定预期结果。
  实现测试 Oracle 涉及在运行测试之前定义 [expected results](../E/expected-result.md) 或行为。在[test execution](../T/test-execution.md)期间，捕获实际结果并将其与Oracle的期望进行比较。差异将被标记以供进一步调查。
  在[automated testing](../A/automated-testing.md) 中，[Test Oracles](../T/test-oracles.md) 在[test scripts](../T/test-script.md) 或框架内进行编码。它们对于在无需人工干预的情况下断言测试通过/失败状态至关重要。
  [Test Oracles](../T/test-oracles.md) 面临的挑战包括由于非确定性系统而导致的**不稳定**、难以为复杂系统定义正确的行为以及在 Oracle 本身中引入**偏差**或错误的可能性。
  为了克服这些挑战，必须定期审查和更新预言机，使用预言机类型的组合来覆盖测试的不同方面，并采用严格的验证方法来确保其准确性和可靠性。

#### 为什么测试预言机在软件测试中很重要？

测试预言机在 [software testing](../S/software-testing.md) 中至关重要，因为它是验证测试结果正确性的**真相来源**。它确定被测系统的行为是否符合[expected results](../E/expected-result.md)，这对于评估软件的可靠性和功能至关重要。
  如果没有测试预言机，测试人员将缺乏系统的方法来**验证测试结果**，从而导致主观判断和不一致的测试结果。这可能会导致未检测到的缺陷，增加生产失败的风险，并最终损害用户满意度和商业声誉。
  在[automated testing](../A/automated-testing.md) 中，测试预言机可以实现结果[verification](../V/verification.md)** 的自动化，减少对手动[inspection](../I/inspection.md) 的需求，并允许进行更广泛和严格的测试。它通过提供有关变更影响的即时反馈，有助于**持续集成**和**交付管道**。
  此外，明确定义的测试预言机可以改进测试[maintainability](../M/maintainability.md)并减少[false positives](../F/false-positive.md)或否定的可能性，这是[test automation](../T/test-automation.md)中的常见挑战。通过明确指定预期行为，它有助于创建更“稳健”和“可靠”的自动化测试。
  综上所述，测试预言机对于确保自动化测试准确反映软件的预期行为是必不可少的，从而在高质量软件产品的交付中发挥着关键作用。

#### 测试预言机在端到端测试中扮演什么角色？

在[end-to-end testing](../E/end-to-end-testing.md) 中，**测试 Oracle** 充当确定被测系统正确性的机制。它提供了与 [actual results](../A/actual-result.md) 进行比较的预期结果。鉴于端到端测试模拟真实的用户场景，测试预言机必须全面了解系统在各种环境和[use cases](../U/use-case.md) 中的行为。
  对于自动化端到端测试，测试预言机通常编码在 [test scripts](../T/test-script.md) 中。它在一系列操作之后断言应用程序的预期状态。这可能涉及检查 [database](../D/database.md) 状态、消息队列或 UI 输出，以确保整个流程按预期工作。

  ```
  // Example assertion in an end-to-end test
  expect(actualOutput).toEqual(expectedOutput);
  ```[end-to-end testing](../E/end-to-end-testing.md) 中测试预言机的有效性至关重要，因为它直接影响捕获整个系统缺陷的能力。配置错误的 Oracle 可能会导致 [false positives](../F/false-positive.md) 或负面结果，从而破坏对自动化测试的信任。
  为了保持可靠性，应定期审查和更新[Test Oracles](../T/test-oracles.md)，以反映系统预期行为的变化。这确保了它们保持准确和相关，为自动化[end-to-end testing](../E/end-to-end-testing.md)工作提供了坚实的基础。

#### 测试预言机如何提高软件产品的整体质量？

测试预言机通过充当验证测试结果正确性的**基准**，显着增强了[software quality](../S/software-quality.md)。它确保自动化测试产生**可靠**和**一致**结果，这对于识别缺陷并验证软件在各种条件下是否按预期运行至关重要。
  通过提供**预期结果**或**决策规则**，[Test Oracles](../T/test-oracles.md) 使自动化测试能够检测与期望行为的偏差，而无需人工干预。这有助于实现更**高效**和**全面**的测试过程，从而实现快速反馈和早期[bug](../B/bug.md)检测。
  将 [Test Oracles](../T/test-oracles.md) 纳入 [automated testing](../A/automated-testing.md) 框架有助于保持高水平的 **[test coverage](../T/test-coverage.md)** 和 **准确性**，因为它们有助于验证复杂的系统行为和业务逻辑。他们还通过确保新更改不会破坏现有功能来支持**[regression testing](../R/regression-testing.md)**。
  有效使用 [Test Oracles](../T/test-oracles.md) 有助于制定稳健的测试策略，这对于长期维护软件产品的**完整性**至关重要。通过确保自动化测试既**值得信赖**又**提供信息**，[Test Oracles](../T/test-oracles.md) 在持续交付和部署管道中发挥着关键作用，最终带来更高质量的软件产品。

### 类型和示例

#### 测试预言机有哪些不同类型？

不同类型的 [Test Oracles](../T/test-oracles.md) 包括：

- **派生预言**：使用现有的系统工件（例如模型、规范或软件的先前版本）来确定预期结果。
  - **指定的预言机**：依靠正式规范（例如需求文档或用户故事）来定义预期行为。
  - **统计预言**：采用统计模型或历史数据以一定的概率预测预期结果。
  - **共识预言机**：使用多个来源或专家之间的协议来确定预期结果。
  - **分析预言**：涉及数学或逻辑推理来确定正确的结果应该是什么。
  - **动态预言**：在测试执行期间动态生成预期结果，通常使用附加代码或算法。
  - **隐式预言**：基于一般期望，例如系统不应崩溃或产生未处理的异常，而没有特定的预期结果。
  每种类型都通过提供不同的方法来验证结果来影响测试过程，从严格遵守规范到更灵活的概率方法。通过在[test scripts](../T/test-script.md) 中嵌入预言机检查或利用单独的预言机服务，可以将它们集成到[automated testing](../A/automated-testing.md) 中。挑战包括确保预言机的准确性、处理不完整的规范以及处理预言机的复杂性。克服这些问题通常涉及预言机类型的组合、对预言机本身的彻底验证以及随着系统的发展定期更新预言机。限制包括潜在的[false positives](../F/false-positive.md) 或负面影响以及为非确定性系统创建预言机的困难。有效性是通过预言机以一致且可靠的方式正确识别通过和失败条件的能力来衡量的。

- **派生预言**：使用现有的系统工件（例如模型、规范或软件的先前版本）来确定预期结果。
  - **指定的预言机**：依靠正式规范（例如需求文档或用户故事）来定义预期行为。
  - **统计预言**：采用统计模型或历史数据以一定的概率预测预期结果。
  - **共识预言机**：使用多个来源或专家之间的协议来确定预期结果。
  - **分析预言**：涉及数学或逻辑推理来确定正确的结果应该是什么。
  - **动态预言**：在测试执行期间动态生成预期结果，通常使用附加代码或算法。
  - **隐式预言**：基于一般期望，例如系统不应崩溃或产生未处理的异常，而没有特定的预期结果。

#### 您能否提供每种类型的测试预言机的示例？

每种类型的测试预言机的示例：

- **派生预言**：使用现有系统文档或模型来预测预期结果。例如，如果记录了一个函数返回排序列表，则测试预言机将检查输出列表是否已排序。

    ```
    assert(isSorted(functionUnderTest(inputList)));
    ```

- **指定的预言机**：基于明确的规范。例如，计算器应用程序的 [test case](../T/test-case.md) 可能会检查加法函数是否返回指定的总和。

    ```
    assert(add(2, 2) === 4);
    ```

- **一致性预言机**：比较软件不同版本或配置的结果一致性。一种常见的方法是在新版本上运行相同的测试，并将结果与​​旧版本进行比较。

    ```
    assert(resultNewVersion === resultOldVersion);
    ```

- **统计预言**：使用统计方法来确定输出是否在可接受的方差范围内。这通常用于[performance testing](../P/performance-testing.md)，其中响应时间可能会波动。

    ```
    assert(average(responseTimes) < maxAllowedTime);
    ```

- **基于视角的预言机**：不同的利益相关者提供他们的期望，可以用作预言机。例如，安全专家可能会定义漏洞扫描的可接受阈值。

    ```
    assert(securityScanResults.vulnerabilities.length <= securityThreshold);
    ```

- **程序化预言机**：直接实现预言机逻辑的代码。例如，函数的单元测试可能包含基于预期行为的断言。

    ```
    assert(myFunctionUnderTest('input') === expectedOutput);
    ```每种类型的预言机都提供了不同的视角来评估软件，从而有助于实现更彻底、更稳健的测试过程。

- **派生预言**：使用现有系统文档或模型来预测预期结果。例如，如果记录了一个函数返回排序列表，则测试预言机将检查输出列表是否已排序。

    ```
    assert(isSorted(functionUnderTest(inputList)));
    ```

- **指定的预言机**：基于明确的规范。例如，计算器应用程序的 [test case](../T/test-case.md) 可能会检查加法函数是否返回指定的总和。

    ```
    assert(add(2, 2) === 4);
    ```

- **一致性预言机**：比较软件不同版本或配置的结果一致性。一种常见的方法是在新版本上运行相同的测试，并将结果与​​旧版本进行比较。

    ```
    assert(resultNewVersion === resultOldVersion);
    ```

- **统计预言**：使用统计方法来确定输出是否在可接受的方差范围内。这通常用于[performance testing](../P/performance-testing.md)，其中响应时间可能会波动。

    ```
    assert(average(responseTimes) < maxAllowedTime);
    ```

- **基于视角的预言机**：不同的利益相关者提供他们的期望，可以用作预言机。例如，安全专家可能会定义漏洞扫描的可接受阈值。

    ```
    assert(securityScanResults.vulnerabilities.length <= securityThreshold);
    ```

- **程序化预言机**：直接实现预言机逻辑的代码。例如，函数的单元测试可能包含基于预期行为的断言。

    ```
    assert(myFunctionUnderTest('input') === expectedOutput);
    ```

#### 不同类型的测试预言机如何影响测试过程？

不同类型的[Test Oracles](../T/test-oracles.md) 通过指导针对[expected results](../E/expected-result.md) 验证测试结果来影响测试过程。预言机的选择会影响测试的**效率**、**有效性**和**范围**。

- **指定预言机**使用正式规范来确定预期结果。它们可以使测试更加**可靠**，但创建和维护可能**耗时**。
  - **派生预言**基于现有系统状态或以前的版本。它们启用**[regression testing](../R/regression-testing.md)**，并且在正式规范不完整时很有用，但如果参考版本也有缺陷，则可能会错过新的缺陷。
  - **统计预言**依赖于概率模型，并在确切结果不可预测时使用。他们在测试中引入了**统计分析**，可以处理具有不确定性行为的复杂系统，但可能并不总能查明特定错误。
  - **共识预言机**使用多个来源或系统之间的协议来验证结果。当单一事实来源不可用时，它们可以有效地**检测异常**，但如果所有来源都具有相同的错误，则可能会**误导**。
  - **人类预言**涉及手动[inspection](../I/inspection.md)，并且在自动判断不可行时是必要的。它们**灵活**，可以捕捉微妙的问题，但**主观**且**可扩展性**有限。
  这些预言机的影响也体现在**测试设计**中，其中预言机的选择塑造了 [test cases](../T/test-case.md) 和 **[test coverage](../T/test-coverage.md)**。此外，预言机的**维护**至关重要，因为过时或不正确的预言机可能会导致[false positives](../F/false-positive.md)或负面结果，影响测试结果的**信任**。 [Test automation](../T/test-automation.md) 工程师必须平衡每种预言机类型的优点和缺点，以优化测试过程。

- **指定预言机**使用正式规范来确定预期结果。它们可以使测试更加**可靠**，但创建和维护可能**耗时**。
  - **派生预言**基于现有系统状态或以前的版本。它们启用**[regression testing](../R/regression-testing.md)**，并且在正式规范不完整时很有用，但如果参考版本也有缺陷，则可能会错过新的缺陷。
  - **统计预言**依赖于概率模型，并在确切结果不可预测时使用。他们在测试中引入了**统计分析**，可以处理具有不确定性行为的复杂系统，但可能并不总能查明特定错误。
  - **共识预言机**使用多个来源或系统之间的协议来验证结果。当单一事实来源不可用时，它们可以有效地**检测异常**，但如果所有来源都具有相同的错误，则可能会**误导**。
  - **人类预言**涉及手动[inspection](../I/inspection.md)，并且在自动判断不可行时是必要的。它们**灵活**，可以捕捉微妙的问题，但**主观**且**可扩展性**有限。

#### Test Oracle 使用的一些实际示例有哪些？

**测试 Oracle** 使用的实际示例包括：

- **一致性检查**：在多平台应用程序中，确保功能在 Windows、macOS 和 Linux 上表现一致。测试预言机验证这些环境中相同输入的输出是否一致。
  - **[Database](../D/database.md) 测试**：测试[database](../D/database.md) 迁移时，测试Oracle 可以比较迁移前后的查询结果，以确保数据完整性和一致性。
  - **[Regression Testing](../R/regression-testing.md)**：软件更新后，测试 Oracle 可以将当前应用程序行为与先前测试运行中定义的预期行为进行比较，以检测任何意外的更改。

  ```
  assert.equal(currentBehavior, expectedBehavior);
  ```

- **用户界面 (UI) 测试**：对于 Web 应用程序，测试 Oracle 可能会使用视觉回归工具来比较更改前后 UI 元素的屏幕截图，以确保像素完美的渲染。
  - **[Performance Testing](../P/performance-testing.md)**：在[load testing](../L/load-testing.md)期间，测试Oracle可以评估重负载下的响应时间是否满足预定义的性能标准。
  - **合规性测试**：在金融软件中，测试预言机可以验证贷款利率的计算是否符合监管标准。
  - **机器学习模型**：对于人工智能驱动的应用程序，测试预言机可以根据一组已知结果评估模型的预测，以衡量准确性。
  - **[API Testing](../A/api-testing.md)**：测试[APIs](../A/api.md) 时，测试Oracle 可以根据[API](../A/api.md) 规范中定义的[expected results](../E/expected-result.md) 验证响应结构、数据和状态代码。

  ```
  expect(response.status).toBe(200);
  expect(response.data).toMatchObject(expectedData);
  ```这些示例说明了 [Test Oracles](../T/test-oracles.md) 如何成为验证各种领域和场景中软件正确性、一致性和合规性的不可或缺的一部分。

- **一致性检查**：在多平台应用程序中，确保功能在 Windows、macOS 和 Linux 上表现一致。测试预言机验证这些环境中相同输入的输出是否一致。
  - **[Database](../D/database.md) 测试**：测试[database](../D/database.md) 迁移时，测试Oracle 可以比较迁移前后的查询结果，以确保数据完整性和一致性。
  - **[Regression Testing](../R/regression-testing.md)**：软件更新后，测试 Oracle 可以将当前应用程序行为与先前测试运行中定义的预期行为进行比较，以检测任何意外的更改。
  - **用户界面 (UI) 测试**：对于 Web 应用程序，测试 Oracle 可能会使用视觉回归工具来比较更改前后 UI 元素的屏幕截图，以确保像素完美的渲染。
  - **[Performance Testing](../P/performance-testing.md)**：在[load testing](../L/load-testing.md)期间，测试Oracle可以评估重负载下的响应时间是否满足预定义的性能标准。
  - **合规性测试**：在金融软件中，测试预言机可以验证贷款利率的计算是否符合监管标准。
  - **机器学习模型**：对于人工智能驱动的应用程序，测试预言机可以根据一组已知结果评估模型的预测，以衡量准确性。
  - **[API Testing](../A/api-testing.md)**：测试[APIs](../A/api.md) 时，测试Oracle 可以根据[API](../A/api.md) 规范中定义的[expected results](../E/expected-result.md) 验证响应结构、数据和状态代码。

### 实施和使用

#### 测试预言机是如何在测试框架中实现的？

在测试框架内实现**测试 Oracle** 涉及创建一种机制来确定被测系统的正确性。这是一个简洁的指南：

1. **定义预期结果**：对于每个[test case](../T/test-case.md)，指定[expected results](../E/expected-result.md)。这可能是系统在执行测试后应表现出的值、状态或行为。

    ```
    const expectedOutcome = "Success message displayed";
    ```

2. **自动化[Verification](../V/verification.md)**：编写断言语句，将实际结果与预期结果进行比较。

    ```
    assert(actualOutcome === expectedOutcome);
    ```

3. **使用外部来源**：如果预言机依赖于外部数据或系统，请集成[APIs](../A/api.md)或[databases](../D/database.md)以获取正确的状态或数据进行比较。

    ```
    const referenceData = getReferenceDataFromAPI();
    assert(systemOutput === referenceData);
    ```

4. **合并启发式**：对于启发式预言，编码输出应符合的规则或模式。

    ```
    assert(outputPattern.test(systemOutput));
    ```

5. **处理非确定性**：在处理概率预言时，包括统计方法来评估可接受范围内的输出。

    ```
    assert(isWithinAcceptableRange(systemOutput, expectedRange));
    ```

6. **利用工具和库**：利用现有库进行断言和比较，以简化实施。

    ```
    expect(systemOutput).to.equal(expectedOutcome);
    ```

7. **持续改进**：随着系统的发展，不断更新预言机以确保其保持准确和相关。
  请记住，预言机应该与 [test cases](../T/test-case.md) 一起**维护**，以确保它反映当前对系统正确行为的理解。

1. **定义预期结果**：对于每个[test case](../T/test-case.md)，指定[expected results](../E/expected-result.md)。这可能是系统在执行测试后应表现出的值、状态或行为。

    ```
    const expectedOutcome = "Success message displayed";
    ```

2. **自动化[Verification](../V/verification.md)**：编写断言语句，将实际结果与预期结果进行比较。

    ```
    assert(actualOutcome === expectedOutcome);
    ```

3. **使用外部来源**：如果预言机依赖于外部数据或系统，请集成[APIs](../A/api.md)或[databases](../D/database.md)以获取正确的状态或数据进行比较。

    ```
    const referenceData = getReferenceDataFromAPI();
    assert(systemOutput === referenceData);
    ```

4. **合并启发式**：对于启发式预言，编码输出应符合的规则或模式。

    ```
    assert(outputPattern.test(systemOutput));
    ```

5. **处理非确定性**：在处理概率预言时，包括统计方法来评估可接受范围内的输出。

    ```
    assert(isWithinAcceptableRange(systemOutput, expectedRange));
    ```

6. **利用工具和库**：利用现有库进行断言和比较，以简化实施。

    ```
    expect(systemOutput).to.equal(expectedOutcome);
    ```

7. **持续改进**：随着系统的发展，不断更新预言机以确保其保持准确和相关。

#### 在测试用例中使用测试预言机的步骤是什么？

要在 [test case](../T/test-case.md) 中使用 **测试 Oracle**，请按照以下步骤操作：

1. **根据规范或先前已知的输出确定 [test case](../T/test-case.md) 的预期结果**。这可以是特定值、值范围、状态或行为。
  2. **为您的[test case](../T/test-case.md) 选择适当的测试 Oracle 类型**。这可以是启发式的、正式的规范或之前记录的结果。
  3. **在您的 [test automation](../T/test-automation.md) 框架内实施测试 Oracle**。这可能涉及编写一个函数或方法来封装用于确定预期结果的逻辑。

    ```
    function testOracle(input) {
      // Logic to determine expected outcome
      return expectedOutcome;
    }
    ```

4. **执行[test case](../T/test-case.md)**并捕获实际结果。这通常是通过运行与被测软件交互的[test script](../T/test-script.md)来完成的。
  5. **使用测试预言机将实际结果与预期结果进行比较**。此步骤通常在[test script](../T/test-script.md) 内自动执行。

    ```
    const actualOutcome = runTest();
    const expectedOutcome = testOracle(input);
    assert.equal(actualOutcome, expectedOutcome);
    ```

6. **分析结果**。如果实际结果与预期结果相符，则测试通过。否则，它将失败，表明存在潜在缺陷。
  7. **记录任何差异**并将其报告为缺陷以供开发团队解决。
  8. **根据测试结果以及软件规范或行为的任何更改，根据需要完善测试预言机**。
  1. **根据规范或先前已知的输出确定 [test case](../T/test-case.md) 的预期结果**。这可以是特定值、值范围、状态或行为。
  2. **为您的[test case](../T/test-case.md) 选择适当的测试 Oracle 类型**。这可以是启发式的、正式的规范或之前记录的结果。
  3. **在[test automation](../T/test-automation.md) 框架内实施测试Oracle**。这可能涉及编写一个函数或方法来封装用于确定预期结果的逻辑。

    ```
    function testOracle(input) {
      // Logic to determine expected outcome
      return expectedOutcome;
    }
    ```

4. **执行[test case](../T/test-case.md)**并捕获实际结果。这通常是通过运行与被测软件交互的[test script](../T/test-script.md)来完成的。
  5. **使用测试预言机将实际结果与预期结果进行比较**。此步骤通常在[test script](../T/test-script.md) 内自动执行。

    ```
    const actualOutcome = runTest();
    const expectedOutcome = testOracle(input);
    assert.equal(actualOutcome, expectedOutcome);
    ```

6. **分析结果**。如果实际结果与预期结果相符，则测试通过。否则，它将失败，表明存在潜在缺陷。
  7. **记录任何差异**并将其报告为缺陷以供开发团队解决。
  8. **根据测试结果以及软件规范或行为的任何更改，根据需要完善测试预言机**。

#### 使用测试预言机的最佳实践是什么？

在软件[test automation](../T/test-automation.md) 中使用[Test Oracles](../T/test-oracles.md) 的最佳实践包括：

- **定义明确的预期结果**：在使用测试预言机验证 [test cases](../T/test-case.md) 的结果之前，确保 [expected results](../E/expected-result.md) 得到明确定义和理解。
  - **使用多个预言机**：结合不同类型的[Test Oracles](../T/test-oracles.md)来增加测试的覆盖范围和可靠性。这可以帮助减轻任何单一预言机的限制。
  - **保持预言机最新**：定期检查和更新您的[Test Oracles](../T/test-oracles.md)，以反映被测系统及其预期行为的变化。
  - **自动化预言机检查**：在可能的情况下，自动化验证过程以减少手动工作并提高[test execution](../T/test-execution.md)的速度。
  - **最小化预言机复杂性**：将 [Test Oracles](../T/test-oracles.md) 设计得尽可能简单，以降低预言机本身引入错误的风险。
  - **记录预言机基本原理**：清楚地记录 [expected results](../E/expected-result.md) 背后的推理和测试预言机的设计，以方便维护和理解。
  - **处理非确定性**：对于具有非确定性输出的系统，设计可以处理结果变化的[Test Oracles](../T/test-oracles.md)。
  - **验证[Test Oracles](../T/test-oracles.md)**：定期根据已知结果验证您的[Test Oracles](../T/test-oracles.md)，以确保它们正常运行。
  - **监控预言机性能**：跟踪[Test Oracles](../T/test-oracles.md)（包括[false positives](../F/false-positive.md) 和[false negatives](../F/false-negative.md)）的性能，以随着时间的推移提高其准确性。
  - **平衡成本和收益**：考虑实施和维护[Test Oracles](../T/test-oracles.md) 的成本与它们在增加[test coverage](../T/test-coverage.md) 和缺陷检测方面提供的收益。
  通过遵循这些最佳实践，[test automation](../T/test-automation.md) 工程师可以有效地利用[Test Oracles](../T/test-oracles.md) 来提高测试过程的可靠性和效率。

- **定义明确的预期结果**：在使用测试预言机验证 [test cases](../T/test-case.md) 的结果之前，确保 [expected results](../E/expected-result.md) 得到明确定义和理解。
  - **使用多个预言机**：结合不同类型的[Test Oracles](../T/test-oracles.md)来增加测试的覆盖范围和可靠性。这可以帮助减轻任何单一预言机的限制。
  - **保持预言机最新**：定期检查和更新您的[Test Oracles](../T/test-oracles.md) 以反映被测系统及其预期行为的变化。
  - **自动化预言机检查**：在可能的情况下，自动化验证过程以减少手动工作并提高[test execution](../T/test-execution.md)的速度。
  - **最小化预言机复杂性**：将 [Test Oracles](../T/test-oracles.md) 设计得尽可能简单，以降低预言机本身引入错误的风险。
  - **记录预言机基本原理**：清楚地记录 [expected results](../E/expected-result.md) 背后的推理和测试预言机的设计，以方便维护和理解。
  - **处理非确定性**：对于具有非确定性输出的系统，设计可以处理结果变化的[Test Oracles](../T/test-oracles.md)。
  - **验证[Test Oracles](../T/test-oracles.md)**：根据已知结果定期验证您的[Test Oracles](../T/test-oracles.md)，以确保它们正常运行。
  - **监控预言机性能**：跟踪[Test Oracles](../T/test-oracles.md)（包括[false positives](../F/false-positive.md) 和[false negatives](../F/false-negative.md)）的性能，以随着时间的推移提高其准确性。
  - **平衡成本和收益**：考虑实施和维护[Test Oracles](../T/test-oracles.md) 的成本与它们在增加[test coverage](../T/test-coverage.md) 和缺陷检测方面提供的收益。

#### 测试预言机如何用于自动化测试？

在[automated testing](../A/automated-testing.md) 中，**[Test Oracles](../T/test-oracles.md)** 被集成以验证[test cases](../T/test-case.md) 的结果。它们是确定软件是否按预期运行的事实来源。以下是它们的使用方法：

- **自动决策**：[Test Oracles](../T/test-oracles.md) 通过将预期结果与[actual results](../A/actual-result.md) 进行比较，自动判定测试通过或失败。
  - **持续集成**：它们嵌入到 CI/CD 管道中，以确保自动化测试对新提交产生可靠的反馈。
  - **数据驱动测试**：Oracle 使用数据集来验证一系列输入及其相应的输出，从而增强[test coverage](../T/test-coverage.md)。
  - **[Regression Testing](../R/regression-testing.md)**：它们通过断言未更改的功能在其他地方修改后仍然可以正常运行来帮助快速识别回归。
  - **[Performance Testing](../P/performance-testing.md)**：Oracle 通过根据可接受的阈值评估响应时间来评估系统性能。
  - **[API Testing](../A/api-testing.md)**：它们验证[API](../A/api.md) 响应、状态代码和数据完整性，以确保服务之间的无缝集成和通信。
  - **[UI Testing](../U/ui-testing.md)**：视觉预言根据预期的布局和功能评估用户界面，即使存在动态内容。
  在[automated testing](../A/automated-testing.md) 中实现[Test Oracles](../T/test-oracles.md) 涉及编写断言脚本或使用断言库/框架。例如，在 [Jest](../J/jest.md) 这样的 JavaScript 测试框架中，您可以使用：

  ```
  expect(actual).toBe(expected);
  ```最佳实践包括：

- **[Maintainability](../M/maintainability.md)** ：保持预言机简单且可维护，以减少误报/漏报。
  - **相关性**：确保它们与测试环境相关并且能够检测有意义的故障。
  - **效率**：优化预言机以避免不必要的复杂性，从而减慢测试执行速度。
  当绝对正确性无法实现时，可以通过改进预言机的逻辑并使用启发式或概率方法来缓解不稳定或预言机复杂性等挑战。测试预言机的有效性是通过其准确检测缺陷的能力及其对减少 [false positives](../F/false-positive.md) 和负面因素的贡献来衡量的。

- **自动决策**：[Test Oracles](../T/test-oracles.md) 通过将预期结果与 [actual results](../A/actual-result.md) 进行比较，自动判定测试通过或失败。
  - **持续集成**：它们嵌入到 CI/CD 管道中，以确保自动化测试对新提交产生可靠的反馈。
  - **数据驱动测试**：Oracle 使用数据集来验证一系列输入及其相应的输出，从而增强 [test coverage](../T/test-coverage.md)。
  - **[Regression Testing](../R/regression-testing.md)**：它们通过断言未更改的功能在其他地方修改后仍然可以正常运行来帮助快速识别回归。
  - **[Performance Testing](../P/performance-testing.md)**：Oracle 通过根据可接受的阈值评估响应时间来评估系统性能。
  - **[API Testing](../A/api-testing.md)**：它们验证[API](../A/api.md) 响应、状态代码和数据完整性，以确保服务之间的无缝集成和通信。
  - **[UI Testing](../U/ui-testing.md)**：视觉预言机根据预期的布局和功能评估用户界面，即使存在动态内容。
  - **[Maintainability](../M/maintainability.md)** ：保持预言机简单且可维护，以减少误报/漏报。
  - **相关性**：确保它们与测试环境相关并且能够检测有意义的故障。
  - **效率**：优化预言机以避免不必要的复杂性，从而减慢测试执行速度。

### 挑战和解决方案

#### 使用测试预言机时面临哪些常见挑战？

使用[Test Oracles](../T/test-oracles.md) 时的常见挑战包括：

- **Oracle问题**：确定正确的结果可能很困难，特别是对于定义预期结果并不简单的复杂系统。
  - **不稳定**：由于不确定性行为，测试预言机可能会产生不一致的结果，导致间歇性通过和失败的不稳定测试。
  - **覆盖范围有限**：它们可能无法涵盖所有​​可能的结果或系统状态，从而导致测试中的空白。
  - **维护开销**：随着系统的发展，维护测试预言机的相关性和准确性可能会占用大量资源。
  - **[False Positives](../F/false-positive.md)/Negatives**：错误地识别测试结果可能会导致浪费精力调查非问题或忽视真正的缺陷。
  - **性能**：测试预言机，尤其是那些涉及复杂逻辑或外部系统的预言机，可能会减慢测试过程。
  - **主观性**：基于人的预言依赖于个人判断，这可能会引入偏见和不一致。
  为了克服这些挑战，请考虑：

- 使用
    **启发式**
    以降低复杂性。

- 实施
    **重试机制**
    用于片状测试。

- 定期
    **审查和更新**
    测试神谕。

- 雇用
    **自动一致性检查**
    检测误报/漏报。

- 平衡测试预言机的使用
    **[exploratory testing](../E/exploratory-testing.md)**
    对于意外行为。

- 纳入
    **监控和记录**
    为不明确的测试结果提供额外信息。

- **Oracle问题**：确定正确的结果可能很困难，特别是对于定义预期结果并不简单的复杂系统。
  - **不稳定**：由于不确定性行为，测试预言机可能会产生不一致的结果，导致间歇性通过和失败的不稳定测试。
  - **覆盖范围有限**：它们可能无法涵盖所有​​可能的结果或系统状态，从而导致测试中的空白。
  - **维护开销**：随着系统的发展，维护测试预言机的相关性和准确性可能会占用大量资源。
  - **[False Positives](../F/false-positive.md)/Negatives**：错误地识别测试结果可能会导致浪费精力调查非问题或忽视真正的缺陷。
  - **性能**：测试预言机，尤其是那些涉及复杂逻辑或外部系统的预言机，可能会减慢测试过程。
  - **主观性**：基于人的预言依赖于个人判断，这可能会引入偏见和不一致。
  - 使用
    **启发式**
    以降低复杂性。

- 实施
    **重试机制**
    用于片状测试。

- 定期
    **审查和更新**
    测试神谕。

- 雇用
    **自动一致性检查**
    检测误报/漏报。

- 平衡测试预言机的使用
    **[exploratory testing](../E/exploratory-testing.md)**
    对于意外行为。

- 纳入
    **监控和记录**
    为不明确的测试结果提供额外信息。

#### 如何克服这些挑战？

使用[Test Oracles](../T/test-oracles.md)软件[test automation](../T/test-automation.md)克服挑战涉及战略方法和实际解决方案：

- **增强预言机决策**：实施**启发式**和**概率模型**来处理不明确或部分预言机信息，减少[false positives](../F/false-positive.md)和否定。
  - **减少维护**：利用**自我修复脚本**，自动适应应用程序中的微小变化，最大限度地减少频繁更新预言机的需要。
  - **改进[Test Coverage](../T/test-coverage.md)**：结合多种预言机类型，例如**启发式、一致性**和**基于规范的预言机**，以涵盖不同方面并提高测试套件的稳健性。
  - **利用机器学习**：采用**ML算法**从历史[test data](../T/test-data.md)中学习，提高预言机以更少的人工干预来预测和验证结果的能力。
  - **使用回退机制**：在预言不确定的情况下，实施**回退机制**，例如人工干预或与其他数据源的交叉引用。
  - **优化性能**：分析您的测试，以识别与预言机检查相关的性能瓶颈并进行相应优化，可能通过**缓存**或**并行化**预言机验证。
  - **持续学习**：鼓励**反馈循环**，其中预言机不断更新[test executions](../T/test-execution.md)的新发现，随着时间的推移提高其准确性。
  - **协作**：促进开发人员、测试人员和领域专家之间的**跨职能协作**，以完善预言机对应用程序预期行为的理解。
  - **工具集成**：将预言机与**现有测试框架**和**CI/CD管道**集成，以简化测试流程并确保预言机得到一致应用。
  - **文档**：维护关于如何使用和更新预言机的清晰**文档**，确保整个团队的知识转移和一致应用。
  通过正面应对这些挑战，[test automation](../T/test-automation.md) 工程师可以确保[Test Oracles](../T/test-oracles.md) 保持有效并为软件质量保证流程做出积极贡献。

- **增强预言机决策**：实施**启发式**和**概率模型**来处理不明确或部分预言机信息，减少[false positives](../F/false-positive.md)和否定。
  - **减少维护**：利用**自我修复脚本**，自动适应应用程序中的微小变化，最大限度地减少频繁更新预言机的需要。
  - **改进[Test Coverage](../T/test-coverage.md)**：结合多种预言机类型，例如**启发式、一致性**和**基于规范的预言机**，以涵盖不同方面并提高测试套件的稳健性。
  - **利用机器学习**：采用**ML算法**从历史[test data](../T/test-data.md)中学习，提高预言机以更少的人工干预来预测和验证结果的能力。
  - **使用回退机制**：在预言不确定的情况下，实施**回退机制**，例如人工干预或与其他数据源的交叉引用。
  - **优化性能**：分析您的测试，以识别与预言机检查相关的性能瓶颈并进行相应优化，可能通过**缓存**或**并行化**预言机验证。
  - **持续学习**：鼓励**反馈循环**，其中预言机会根据[test executions](../T/test-execution.md)的新发现不断更新，随着时间的推移提高其准确性。
  - **协作**：促进开发人员、测试人员和领域专家之间的**跨职能协作**，以完善预言机对应用程序预期行为的理解。
  - **工具集成**：将预言机与**现有测试框架**和**CI/CD管道**集成，以简化测试流程并确保预言机得到一致应用。
  - **文档**：维护关于如何使用和更新预言机的清晰**文档**，确保整个团队的知识转移和一致应用。

#### 测试预言机有哪些限制？

[Test Oracles](../T/test-oracles.md) 有几个限制，可能会影响它们在 [software testing](../S/software-testing.md) 中的有效性：

- **模糊性**：预言机可能并不总是提供清晰或精确的预期结果，导致测试结果解释的不确定性。
  - **部分[verification](../V/verification.md)** ：某些 Oracle 只能验证软件行为的子集，可能会遗漏未验证区域中的缺陷。
  - **复杂性**：复杂的系统可能需要同样复杂的预言机，这可能很难创建和维护。
  - **演变**：随着软件的演变，必须更新预言机以反映变化，这可能非常耗时且容易出错。
  - **主观性**：基于人的预言机，如专家意见，可能会引入主观性，导致结果不一致。
  - **Oracle 问题**：确定某些场景的正确行为本身就很困难，有时甚至无法创建明确的 Oracle。
  - **性能**：大规模测试需要高性能预言机，但创建和维护它们可能会占用大量资源。
  - **[False positives](../F/false-positive.md)/阴性**：不准确的预言机可能会导致误报（在没有缺陷时报告缺陷）或漏报（未能检测到实际缺陷）。
  为了减轻这些限制，结合多个预言机、不断审查和更新预言机并将它们与其他测试方法一起使用非常重要。此外，自动化 Oracle 更新并针对复杂或主观场景采用启发式 Oracle 可以帮助应对这些挑战。

- **模糊性**：预言机可能并不总是提供清晰或精确的预期结果，导致测试结果解释的不确定性。
  - **部分[verification](../V/verification.md)** ：某些 Oracle 只能验证软件行为的子集，可能会遗漏未验证区域中的缺陷。
  - **复杂性**：复杂的系统可能需要同样复杂的预言机，这可能很难创建和维护。
  - **演变**：随着软件的演变，必须更新预言机以反映变化，这可能非常耗时且容易出错。
  - **主观性**：基于人的预言机，如专家意见，可能会引入主观性，导致结果不一致。
  - **Oracle 问题**：确定某些场景的正确行为本身就很困难，有时甚至无法创建明确的 Oracle。
  - **性能**：大规模测试需要高性能预言机，但创建和维护它们可能会占用大量资源。
  - **[False positives](../F/false-positive.md)/阴性**：不准确的预言机可能会导致误报（在没有缺陷时报告缺陷）或漏报（未能检测到实际缺陷）。

#### 如何衡量测试预言机的有效性？

衡量**测试预言机**的有效性可以通过评估其识别缺陷的**准确性**、**可靠性**和**效率**来实现：

- **准确度**：确定**[false positive](../F/false-positive.md) 率**（测试在不应通过时失败）和**[false negative](../F/false-negative.md) 率**（测试在不应通过时通过）。较低的比率表示预言机更准确。

    ```
    accuracy = (true_positives + true_negatives) / (total_tests)
    ```

- **可靠性**：评估预言机在相同条件下产生相同结果的一致性。波动可能表明预言机决定论存在问题。
  - **效率**：评估预言机确定被测系统正确性所需的时间和资源。更快的结果和更少的计算成本是优选的。
  - **覆盖率**：分析预言机可以检测到各种缺陷的程度。这可以通过检查预言机执行的断言类型或检查来完成。
  - **[Maintainability](../M/maintainability.md)**：考虑软件发展时更新预言机所需的工作量。一个有效的预言机应该易于维护。
  为了量化这些方面，需要收集和分析测试运行中的数据，例如发现的缺陷数量、运行测试所需的时间以及预言机维护所需的工作量。使用此数据来计算准确性和效率等指标，并将其与预定义的基准或历史数据进行比较以衡量有效性。定期检查这些指标有助于完善预言机以获得更好的性能。

- **准确度**：确定 **[false positive](../F/false-positive.md) 率**（测试在不应通过时失败）和 **[false negative](../F/false-negative.md) 率**（测试在不应通过时通过）。较低的比率表示预言机更准确。

    ```
    accuracy = (true_positives + true_negatives) / (total_tests)
    ```

- **可靠性**：评估预言机在相同条件下产生相同结果的一致性。波动可能表明预言机决定论存在问题。
  - **效率**：评估预言机确定被测系统正确性所需的时间和资源。更快的结果和更少的计算成本是优选的。
  - **覆盖率**：分析预言机可以检测到各种缺陷的程度。这可以通过检查预言机执行的断言类型或检查来完成。
  - **[Maintainability](../M/maintainability.md)**：考虑软件发展时更新预言机所需的工作量。一个有效的预言机应该易于维护。
