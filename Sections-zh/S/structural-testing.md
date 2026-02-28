# 结构测试

<!-- TOC START -->
- [有关结构测试的问题吗？](#有关结构测试的问题吗？)
  - [基础知识和重要性](#基础知识和重要性)
    - [什么是结构测试？](#什么是结构测试？)
    - [为什么结构测试在软件开发中很重要？](#为什么结构测试在软件开发中很重要？)
    - [结构测试和功能测试之间的主要区别是什么？](#结构测试和功能测试之间的主要区别是什么？)
    - [结构测试如何提高软件产品的整体质量？](#结构测试如何提高软件产品的整体质量？)
  - [技术和类型](#技术和类型)
    - [结构测试中使用了哪些不同的技术？](#结构测试中使用了哪些不同的技术？)
    - [什么是白盒测试以及它与结构测试有何关系？](#什么是白盒测试以及它与结构测试有何关系？)
    - [结构测试中语句覆盖率和分支覆盖率有什么区别？](#结构测试中语句覆盖率和分支覆盖率有什么区别？)
    - [结构测试中的路径测试是什么？](#结构测试中的路径测试是什么？)
  - [实施和工具](#实施和工具)
    - [实施结构测试涉及哪些步骤？](#实施结构测试涉及哪些步骤？)
    - [结构测试中常用的工具有哪些？](#结构测试中常用的工具有哪些？)
    - [结构测试如何实现自动化？](#结构测试如何实现自动化？)
    - [实施结构测试时有哪些最佳实践？](#实施结构测试时有哪些最佳实践？)
  - [挑战和解决方案](#挑战和解决方案)
    - [结构测试过程中面临哪些常见挑战？](#结构测试过程中面临哪些常见挑战？)
    - [如何缓解这些挑战？](#如何缓解这些挑战？)
    - [成功的结构测试有哪些例子？](#成功的结构测试有哪些例子？)
    - [结构测试如何集成到持续集成/持续部署（CI/CD）管道中？](#结构测试如何集成到持续集成持续部署（cicd）管道中？)
<!-- TOC END -->

结构测试

评估软件代码结构。结合白盒和

玻璃盒测试

，它主要由开发人员完成，以确保系统完整性而不是功能。

## 有关结构测试的问题吗？

### 基础知识和重要性

#### 什么是结构测试？

[Structural testing](../S/structural-testing.md)，也称为**[white box testing](../W/white-box-testing.md)**，重点关注软件代码的内部结构。设计[test cases](../T/test-case.md)需要了解应用程序的内部工作原理，确保代码中的所有路径、分支和语句至少执行一次。
  在[structural testing](../S/structural-testing.md)中，**[code coverage](../C/code-coverage.md)**是一个关键指标，其中包括**语句覆盖率**，确保每行代码都被执行，以及**分支覆盖率**，它测试通过控制结构的每个可能的路径，例如if-else或switch-case语句。 **[Path testing](../P/path-testing.md)** 是另一种技术，涉及通过代码测试所有可能的路径，这可能是详尽的，但确保彻底的测试。
  自动化 [structural testing](../S/structural-testing.md) 涉及编写直接与代码交互的[test scripts](../T/test-script.md)。 Java 的 **JUnit** 或 Python 的 **pytest** 等工具可用于编写执行 [structural testing](../S/structural-testing.md) 的单元测试。这些测试可以集成到 **CI/CD 管道**中，在每次代码提交时自动运行，以确保持续的质量控制。
  [structural testing](../S/structural-testing.md) 中的最佳实践包括：

- 写作
    **清晰、可维护[test cases](../T/test-case.md)**
    当代码更改时可以轻松更新。

- 确保
    **高[code coverage](../C/code-coverage.md)**
    捕获尽可能多的问题。

- 将测试集成到
    **构建过程**
    以获得持续的反馈。

- 使用
    **模拟和存根**
    隔离部分代码以进行更有针对性的测试。
  [structural testing](../S/structural-testing.md) 中的挑战通常涉及维护复杂代码库的[test cases](../T/test-case.md) 并确保测试跟上快速开发的步伐。定期重构测试代码并确定测试关键路径的优先级可以帮助缓解这些挑战。

- 写作
    **清晰、可维护[test cases](../T/test-case.md)**
    当代码更改时可以轻松更新。

- 确保
    **高[code coverage](../C/code-coverage.md)**
    捕获尽可能多的问题。

- 将测试集成到
    **构建过程**
    以获得持续的反馈。

- 使用
    **模拟和存根**
    隔离部分代码以进行更有针对性的测试。

#### 为什么结构测试在软件开发中很重要？

[Structural testing](../S/structural-testing.md) 对于识别 [functional testing](../F/functional-testing.md) 可能遗漏的缺陷至关重要。它确保所有代码路径都得到执行，揭示隐藏的错误和边缘情况。通过关注内部结构，它促进了对复杂逻辑分支和循环的彻底测试，从而产生健壮且可靠的代码。 [Structural testing](../S/structural-testing.md) 还有助于优化[code coverage](../C/code-coverage.md) 指标，指导开发人员编写更多可测试的代码并保持高标准。
  自动化[structural testing](../S/structural-testing.md)可以显着提高效率和准确性。自动化测试可以频繁且一致地运行，从而快速捕获回归。 [code coverage](../C/code-coverage.md) 分析器等工具无缝集成到 CI/CD 工作流程中，提供有关代码更改影响的实时反馈。
  最佳实践包括在开发周期的早期开始，优先考虑关键路径以获得最大影响，并根据代码更改不断完善测试。诸如初始 [setup](../S/setup.md) 时间长和保持测试相关性等挑战可以通过增量实施和定期审查来缓解。
  成功的[structural testing](../S/structural-testing.md) 示例通常涉及可靠性至关重要的复杂系统，例如金融软件或安全关键系统。在这些场景中，结构方法提供的测试深度对于确保系统完整性和性能至关重要。

  ```
  // Example of a simple automated structural test case in TypeScript
  describe('Calculator', () => {
    test('should add two numbers correctly', () => {
      expect(add(2, 3)).toBe(5);
    });
  });
  ```总之，[structural testing](../S/structural-testing.md) 是全面测试策略的关键组成部分，提供对代码质量和系统行为的深入洞察。

#### 结构测试和功能测试之间的主要区别是什么？

[Structural testing](../S/structural-testing.md)，通常称为**白盒测试**，专注于软件的内部结构，检查代码、设计和架构。设计 [test cases](../T/test-case.md) 需要了解应用程序的内部工作原理，其中通常涉及 **[code coverage](../C/code-coverage.md)** 指标，例如语句、分支和路径覆盖率。
  相比之下，[functional testing](../F/functional-testing.md) 或**黑盒测试** 根据要求评估软件的功能。它不需要深入了解代码结构，并且基于通过提供输入和检查输出来测试软件功能。功能测试根据定义的规范和[use cases](../U/use-case.md) 验证软件行为。
  主要区别包括：

- **范围**：结构测试检查内部代码路径和结构，而功能测试评估最终用户功能。
  - **知识**：结构需要深入的代码知识；功能性则不然。
  - **[Test Case](../T/test-case.md) Design** ：结构测试用例源自代码；功能测试用例源自需求和用户故事。
  - **目标**：结构性目标是发现内部缺陷；功能的目的是验证软件是否从最终用户的角度完成了它应该做的事情。
  - **工具**：结构测试经常使用可以分析和检测代码的工具；功能测试工具模拟用户交互。
  在实践中，两种测试类型是相辅相成的，[structural testing](../S/structural-testing.md) 确保代码在内部按预期工作，[functional testing](../F/functional-testing.md) 确认其满足外部期望。

- **范围**：结构测试检查内部代码路径和结构，而功能测试评估最终用户功能。
  - **知识**：结构需要深入的代码知识；功能性则不然。
  - **[Test Case](../T/test-case.md) Design** ：结构测试用例源自代码；功能测试用例源自需求和用户故事。
  - **目标**：结构性目标是发现内部缺陷；功能的目的是验证软件是否从最终用户的角度完成了它应该做的事情。
  - **工具**：结构测试经常使用可以分析和检测代码的工具；功能测试工具模拟用户交互。

#### 结构测试如何提高软件产品的整体质量？

[Structural testing](../S/structural-testing.md) 通过确保应用程序的内部操作符合规范且无错误来增强[software quality](../S/software-quality.md)。它在各种条件下**验证代码行为**，从而检测到[functional testing](../F/functional-testing.md) 可能会错过的隐藏[bugs](../B/bug.md)。通过关注代码路径、分支和语句，[structural testing](../S/structural-testing.md) 验证代码的所有部分都已执行，从而降低了未经测试的逻辑和潜在故障的风​​险。
  将[structural testing](../S/structural-testing.md) 纳入开发过程可促进**更高的[code coverage](../C/code-coverage.md) 指标**，这通常与更少的功能缺陷相关。它还鼓励开发人员编写更多**可维护和健壮的代码**，因为使代码可测试的过程通常会带来更好的软件设计。
  自动化[structural testing](../S/structural-testing.md)工具可以快速识别尚未执行的代码部分，为开发人员提供即时反馈。这种快速反馈循环允许“快速修复”问题，这比修复在开发周期后期或发布后发现的[bugs](../B/bug.md)更具成本效益。
  此外，[structural testing](../S/structural-testing.md) 在**高风险领域**尤其有价值，例如金融交易、数据处理和安全功能，其中精确的内部行为至关重要。通过严格测试这些领域，[structural testing](../S/structural-testing.md) 有助于提高软件产品的整体可靠性和安全性。
  最终，[structural testing](../S/structural-testing.md) 是全面测试策略的关键组成部分，补充[functional testing](../F/functional-testing.md) 以提供全面且经过彻底验证的软件产品。

### 技术和类型

#### 结构测试中使用了哪些不同的技术？

[structural testing](../S/structural-testing.md) 中使用的不同技术包括：

- **条件覆盖**：确保所有布尔表达式都被评估为 true 和 false。
  - **决策覆盖率**：与分支覆盖率类似，但侧重于确保代码中的每个决策都采用所有可能的结果。
  - **多条件覆盖**：通过评估多条件决策中的所有条件组合来扩展条件覆盖范围。
  - **循环覆盖**：测试代码中的循环以确保正确执行和终止，包括边缘情况，例如不进入循环或仅执行一次。
  - **数据流覆盖**：重点关注变量接收值的点和使用这些值的点，确保测试这些点之间的路径。
  - **[Mutation Testing](../M/mutation-testing.md)** ：涉及对代码进行小的更改（突变体）并检查测试用例是否可以检测到更改，从而评估测试用例的有效性。

  ```
  // Example of condition coverage in pseudocode
  if (a && b) {
    // Test with a=true, b=false; a=false, b=true; a=true, b=true
  }
  ```每种技术都针对代码结构的不同方面，结合起来可以提供更全面的评估。经验丰富的自动化工程师可以利用这些技术来识别代码中可能容易出错的特定区域，从而确保稳健的测试策略。

- **条件覆盖**：确保所有布尔表达式都被评估为 true 和 false。
  - **决策覆盖率**：与分支覆盖率类似，但侧重于确保代码中的每个决策都采用所有可能的结果。
  - **多条件覆盖**：通过评估多条件决策中的所有条件组合来扩展条件覆盖范围。
  - **循环覆盖**：测试代码中的循环以确保正确执行和终止，包括边缘情况，例如不进入循环或仅执行一次。
  - **数据流覆盖**：重点关注变量接收值的点和使用这些值的点，确保测试这些点之间的路径。
  - **[Mutation Testing](../M/mutation-testing.md)** ：涉及对代码进行小的更改（突变体）并检查测试用例是否可以检测到更改，从而评估测试用例的有效性。

#### 什么是白盒测试以及它与结构测试有何关系？

[White box testing](../W/white-box-testing.md)，也称为 **clear box** 或 **[glass box testing](../G/glass-box-testing.md)**，是一种测试人员可以全面了解软件内部工作原理的方法，包括代码结构、算法和逻辑。这项技术需要对代码库有深入的了解，通常由具有编程技能的开发人员或测试工程师来执行。
  相对于[structural testing](../S/structural-testing.md)，[white box testing](../W/white-box-testing.md) 是**核心组件**。 [Structural testing](../S/structural-testing.md) 重点关注软件的内部结构，[white box testing](../W/white-box-testing.md) 提供检查和验证该结构的方法。它涉及根据应用程序的内部路径、代码结构和编码实践创建[test cases](../T/test-case.md)。
  [white box testing](../W/white-box-testing.md) 的典型执行方式如下：

  ```
  1. Analyze the source code for potential vulnerabilities.
  2. Identify all possible execution paths.
  3. Develop and execute test cases that cover these paths.
  4. Assess the code for logic errors, dead code, and possible optimizations.
  5. Verify the flow of inputs and outputs through the code.
  6. Ensure that all paths are tested for maximum coverage.
  ```[White box testing](../W/white-box-testing.md) 是实现**高[code coverage](../C/code-coverage.md)** 指标（例如语句和分支覆盖率）不可或缺的一部分。它允许测试人员识别现有[test cases](../T/test-case.md)未执行的代码区域，确保发现并纠正隐藏的缺陷。
  通过在[structural testing](../S/structural-testing.md)中利用[white box testing](../W/white-box-testing.md)，自动化工程师可以确保对软件架构进行彻底检查，从而获得更强大、更可靠的软件产品。

#### 结构测试中语句覆盖率和分支覆盖率有什么区别？

语句覆盖率和分支覆盖率都是[structural testing](../S/structural-testing.md) 中用于评估[test cases](../T/test-case.md) 彻底性的指标。
  **语句覆盖率** 测量代码中已由 [test suite](../T/test-suite.md) 执行的可执行语句的百分比。目标是确保每行代码至少测试一次。但是，它并不能保证所有可能的结果或路径都经过测试。

  ```
  if (condition) {
    executeStatement1(); // Tested
  }
  executeStatement2(); // Tested
  ```在上面的示例中，如果在测试期间同时执行`executeStatement1` 和`executeStatement2`，则无论`condition` 为真还是假，语句覆盖率为100%。
  **分支覆盖率**，也称为决策覆盖率，更进一步确保每个控制结构的每个分支（例如 `if` 和 `case` 语句）都得到执行。这意味着每个条件的正确结果和错误结果都会被测试。

  ```
  if (condition) {
    executeStatement1(); // Tested when condition is true
  } else {
    executeStatement3(); // Must be tested when condition is false
  }
  executeStatement2(); // Tested
  ```要实现 100% 分支覆盖率，测试必须覆盖 `if` 条件的 true 和 false 分支。这通常需要比语句覆盖更多的[test cases](../T/test-case.md)，因为它侧重于代码中的决策点。
  总之，**语句覆盖**涉及执行所有代码行，而**分支覆盖**确保采用通过控制结构的每条可能的路线。分支覆盖通常意味着语句覆盖，但反之则不然；实现高语句覆盖率并不能保证高分支覆盖率。

#### 结构测试中的路径测试是什么？

[Path testing](../P/path-testing.md) 是 **[structural testing](../S/structural-testing.md)** 策略，重点是在组件或系统内执行所有可能的执行路径。它基于控制流来识别程序在执行过程中可能采取的每条潜在路径，包括循环、分支和条件语句。
  在[path testing](../P/path-testing.md)中，主要目标是确保所有路径至少执行一次，这有助于发现很少使用的路径中可能发生的错误。这是通过创建将遍历每个路径的 **[test cases](../T/test-case.md)** 来实现的。
  为了有效地实现[path testing](../P/path-testing.md)，您通常会使用：

- **控制流程图 (CFG)**
    可视化路径。

- **循环复杂度**
    确定线性独立路径的数量，从而确定所需测试用例的数量。
  [Path testing](../P/path-testing.md) 比分支覆盖范围更细化，因为它考虑事件的顺序，而不仅仅是条件分支的覆盖范围。它对于需要对代码可靠性具有高度信心的关键组件特别有用。
  然而，由于复杂系统中可能存在大量路径，[path testing](../P/path-testing.md) 可能具有挑战性。为了管理这一点，您可以关注**高风险路径**或使用启发式方法来确定更有可能包含缺陷的路径的优先级。
  自动化工具可以通过从 CFG 生成 [test cases](../T/test-case.md) 或识别尚未测试的路径来协助 [path testing](../P/path-testing.md)。将 [path testing](../P/path-testing.md) 集成到 [test suite](../T/test-suite.md) 中可以确保所有代码路径在测试条件下得到验证，从而显着增强软件的稳健性。

- **控制流程图 (CFG)**
    可视化路径。

- **循环复杂度**
    确定线性独立路径的数量，从而确定所需测试用例的数量。

### 实施和工具

#### 实施结构测试涉及哪些步骤？

要有效实施[structural testing](../S/structural-testing.md)，请按照下列步骤操作：

1. **确定测试项目**：选择需要测试的组件或系统。
  2. **了解结构**：熟悉测试项的内部工作原理，包括控制流、数据流以及相关代码复杂度。
  3. **制定[test plan](../T/test-plan.md)**：概述方法、资源、时间表和可交付成果。包括覆盖目标的标准，例如语句、分支或路径覆盖。
  4. **创建[test cases](../T/test-case.md)**：根据覆盖标准，设计[test cases](../T/test-case.md)来执行代码的各个部分。使用工具或手动分析以确保彻底性。
  5. **准备[test environment](../T/test-environment.md)**：设置必要的基础设施，包括[test data](../T/test-data.md)、[databases](../D/database.md) 和系统配置。
  6. **执行[test cases](../T/test-case.md)**：手动或使用自动化工具运行测试。记录结果并监控覆盖率指标。
  7. **分析结果**：评估通过、失败或未覆盖区域的结果。调查未能识别缺陷的情况。
  8. **报告结果**：记录缺陷、覆盖级别以及与 [test plan](../T/test-plan.md) 的任何偏差。将这些内容传达给开发团队。
  9. **重新测试**：修复后，重新测试受影响的区域，以确保问题得到解决并且不会引入新问题。
  10. **完善测试**：根据调查结果和代码更改不断改进[test cases](../T/test-case.md) 和覆盖范围。
  11. **与 CI/CD 集成**：在 CI/CD 管道内自动执行结构测试，以确保持续反馈和[quality assurance](../Q/quality-assurance.md)。
  通过执行以下步骤，您可以系统地实施[structural testing](../S/structural-testing.md)，以增强软件的可靠性和[maintainability](../M/maintainability.md)。

1. **确定测试项目**：选择需要测试的组件或系统。
  2. **了解结构**：熟悉测试项的内部工作原理，包括控制流、数据流以及相关代码复杂度。
  3. **制定[test plan](../T/test-plan.md)**：概述方法、资源、时间表和可交付成果。包括覆盖目标的标准，例如语句、分支或路径覆盖。
  4. **创建[test cases](../T/test-case.md)**：根据覆盖标准，设计[test cases](../T/test-case.md)来执行代码的各个部分。使用工具或手动分析以确保彻底性。
  5. **准备[test environment](../T/test-environment.md)**：设置必要的基础设施，包括[test data](../T/test-data.md)、[databases](../D/database.md) 和系统配置。
  6. **执行[test cases](../T/test-case.md)**：手动或使用自动化工具运行测试。记录结果并监控覆盖率指标。
  7. **分析结果**：评估通过、失败或未覆盖区域的结果。调查未能识别缺陷的情况。
  8. **报告结果**：记录缺陷、覆盖级别以及与 [test plan](../T/test-plan.md) 的任何偏差。将这些内容传达给开发团队。
  9. **重新测试**：修复后，重新测试受影响的区域，以确保问题得到解决并且不会引入新问题。
  10. **完善测试**：根据调查结果和代码更改不断改进[test cases](../T/test-case.md) 和覆盖范围。
  11. **与 CI/CD 集成**：在 CI/CD 管道内自动执行结构测试，以确保持续反馈和 [quality assurance](../Q/quality-assurance.md)。

#### 结构测试中常用的工具有哪些？

**[structural testing](../S/structural-testing.md)** 的常用工具包括：

- **[Code Coverage](../C/code-coverage.md) 分析器**：**JaCoCo**、**Clover** 和 **Istanbul** 等工具测量测试期间执行的代码量，提供对语句、分支和路径覆盖率的见解。
  - **静态分析工具**：**SonarQube**、**Coverity** 和 **Fortify** 分析源代码中的潜在漏洞和编码标准违规，这可以告知结构 [test cases](../T/test-case.md)。
  - **[Unit Testing](../U/unit-testing.md) 框架**：**JUnit** (Java)、**[NUnit](../N/nunit.md)** (.NET)、**pytest** (Python) 和 **Mocha** (JavaScript) 用于编写和执行单元测试，这是 [structural testing](../S/structural-testing.md) 的关键组件。
  - **模拟框架**：**Mockito** (Java)、**Moq** (.NET) 和 **unittest.mock** (Python) 等工具模拟未测试的组件，允许对特定代码路径进行隔离测试。
  - **Profiler 工具**：**VisualVM**、**YourKit** 和 **dotTrace** 有助于识别性能瓶颈并优化代码路径，这些可以作为结构测试的目标。
  - **集成开发环境 (IDE)**：**Eclipse**、**IntelliJ IDEA** 和 **Visual Studio** 通常具有 [code coverage](../C/code-coverage.md) 和 [unit testing](../U/unit-testing.md) 的内置或插件支持功能，从而在开发环境中促进 [structural testing](../S/structural-testing.md)。
  - **持续集成工具**：**Jenkins**、**Travis CI** 和 **CircleCI** 可以作为 CI/CD 管道的一部分自动执行结构测试。
  这些工具通过提供对代码结构和[test coverage](../T/test-coverage.md)的详细见解，帮助自动化并增强[structural testing](../S/structural-testing.md)的有效性，最终有助于提高代码质量和可靠性。

- **[Code Coverage](../C/code-coverage.md) 分析器**：**JaCoCo**、**Clover** 和 **Istanbul** 等工具测量测试期间执行的代码量，提供对语句、分支和路径覆盖率的见解。
  - **静态分析工具**：**SonarQube**、**Coverity** 和 **Fortify** 分析源代码中的潜在漏洞和编码标准违规，这可以告知结构 [test cases](../T/test-case.md)。
  - **[Unit Testing](../U/unit-testing.md) 框架**：**JUnit** (Java)、**[NUnit](../N/nunit.md)** (.NET)、**pytest** (Python) 和 **Mocha** (JavaScript) 用于编写和执行单元测试，这是 [structural testing](../S/structural-testing.md) 的关键组件。
  - **模拟框架**：**Mockito** (Java)、**Moq** (.NET) 和 **unittest.mock** (Python) 等工具模拟未测试的组件，允许对特定代码路径进行隔离测试。
  - **Profiler 工具**：**VisualVM**、**YourKit** 和 **dotTrace** 有助于识别性能瓶颈并优化代码路径，这些可以作为结构测试的目标。
  - **集成开发环境 (IDE)**：**Eclipse**、**IntelliJ IDEA** 和 **Visual Studio** 通常具有 [code coverage](../C/code-coverage.md) 和 [unit testing](../U/unit-testing.md) 的内置或插件支持功能，从而在开发环境中促进 [structural testing](../S/structural-testing.md)。
  - **持续集成工具**：**Jenkins**、**Travis CI** 和 **CircleCI** 可以作为 CI/CD 管道的一部分自动执行结构测试。

#### 结构测试如何实现自动化？

自动化[structural testing](../S/structural-testing.md) 涉及验证软件内部工作的脚本测试。利用 **[unit testing](../U/unit-testing.md) 框架**（例如用于 Java 的 JUnit 或用于 .NET 的 [NUnit](../N/nunit.md)）来创建涵盖各种代码路径的 [test cases](../T/test-case.md)。利用 **[code coverage](../C/code-coverage.md) 工具**（例如 JaCoCo 或 Istanbul）来测量测试期间执行的代码的范围并识别未测试的部分。

  ```
  @Test
  public void testMethod() {
      MyClass myClass = new MyClass();
      int result = myClass.computeSomething();
      assertEquals("Expected result not obtained", expectedValue, result);
  }
  ```结合 SonarQube 等**静态分析工具**，无需执行代码即可检测潜在问题。使用**模拟框架**（例如 Mockito 或 Moq）来模拟依赖关系，确保代码单元的隔离测试。

  ```
  import { MyClass } from './MyClass';
  import { MyDependency } from './MyDependency';
  import { jest } from '@jest/globals';
  jest.mock('./MyDependency');
  test('MyClass calls MyDependency method correctly', () => {
    const myDependencyInstance = new MyDependency();
    const myClassInstance = new MyClass(myDependencyInstance);
    myClassInstance.performAction();
    expect(myDependencyInstance.someMethod).toHaveBeenCalled();
  });
  ```使用 Randoop 或 EvoSuite 等工具自动生成 [test cases](../T/test-case.md)，这些工具根据代码的行为创建测试。将这些工具集成到您的 **CI/CD 管道**中，以便在每次提交或构建时自动运行测试，确保立即反馈更改的影响。
  请记住定期**重构测试**以保持其有效性和可读性。保持测试**集中且快速**，以促进频繁执行，并确定测试关键路径的优先级，以最大限度地提高自动化工作的价值。

#### 实施结构测试时有哪些最佳实践？

实施 [structural testing](../S/structural-testing.md) 时，请考虑以下最佳实践：

- **设计[test cases](../T/test-case.md)**，覆盖代码中所有可能的路径、分支和语句。使用工具来衡量覆盖率并瞄准高覆盖率指标，但不要仅仅依赖这些数字；了解背景和风险领域。
  - **优先考虑关键路径**和更容易出错或对系统影响更大的组件。分配更多资源来彻底测试这些领域。
  - **纳入代码审查**以确保代码可测试并识别可能需要更深入测试的潜在领域。
  - **在必要时重构代码**以使其更具可测试性。这可能涉及将复杂的功能分解为更小、更易于管理的部分。
  - **尽可能自动化**，特别是对于[regression testing](../R/regression-testing.md)。使用与您的开发环境完美集成的自动化框架和工具。
  - **在单元测试、集成测试和系统测试之间保持平衡**。确保不同级别的测试足以涵盖代码的结构方面。
  - **通过代码更改使测试保持最新**。实施更新测试和代码修改的流程，以防止测试失效。
  - **使用模拟对象和存根**来隔离被测代码，尤其是在处理外部依赖项或复杂的系统交互时。
  - **将 [structural testing](../S/structural-testing.md) 集成到 CI/CD 管道**，以确保每次构建时自动运行测试，为开发人员提供即时反馈。
  - **清楚地记录[test cases](../T/test-case.md)和结果**，使其他人更容易理解测试的目的和结果的影响。
  - **根据反馈和指标不断审查和改进**测试流程，以适应代码库和技术堆栈的变化。
  - **设计[test cases](../T/test-case.md)**，覆盖代码中所有可能的路径、分支和语句。使用工具来衡量覆盖率并瞄准高覆盖率指标，但不要仅仅依赖这些数字；了解背景和风险领域。
  - **优先考虑关键路径**和更容易出错或对系统影响更大的组件。分配更多资源来彻底测试这些领域。
  - **纳入代码审查**以确保代码可测试并识别可能需要更深入测试的潜在领域。
  - **在必要时重构代码**以使其更具可测试性。这可能涉及将复杂的功能分解为更小、更易于管理的部分。
  - **尽可能自动化**，特别是对于[regression testing](../R/regression-testing.md)。使用与您的开发环境完美集成的自动化框架和工具。
  - **在单元测试、集成测试和系统测试之间保持平衡**。确保不同级别的测试足以涵盖代码的结构方面。
  - **通过代码更改使测试保持最新**。实施更新测试和代码修改的流程，以防止测试失效。
  - **使用模拟对象和存根**来隔离被测代码，尤其是在处理外部依赖项或复杂的系统交互时。
  - **将 [structural testing](../S/structural-testing.md) 集成到 CI/CD 管道**，以确保每次构建时自动运行测试，为开发人员提供即时反馈。
  - **清楚地记录[test cases](../T/test-case.md)和结果**，使其他人更容易理解测试的目的和结果的影响。
  - **根据反馈和指标不断审查和改进**测试流程，以适应代码库和技术堆栈的变化。

### 挑战和解决方案

#### 结构测试过程中面临哪些常见挑战？

[structural testing](../S/structural-testing.md) 中的常见挑战包括：

- **复杂性**：由于路径数量巨大，测试复杂系统中所有可能的路径可能会令人畏惧。
  - **耗时**：实现高水平的覆盖（例如路径或分支覆盖）可能非常耗时。
  - **资源密集型**：结构测试通常需要大量的计算资源来执行所有测试用例。
  - **确定正确的工具**：选择能够满足结构测试特定要求的适当工具可能很困难。
  - **维护[Test Cases](../T/test-case.md)**：随着代码库的发展，维护和更新测试用例以反映变化可能具有挑战性。
  - **不稳定**：由于计时问题或外部依赖性，测试可能会间歇性地通过或失败，从而导致不可靠的结果。
  - **理解代码内部**：测试人员需要深入了解代码内部，这可能并不总是可行或可用。
  - **与 CI/CD 集成**：确保结构测试在 CI/CD 管道中高效运行而不减慢交付过程需要仔细规划和优化。
  缓解策略包括优先考虑[test cases](../T/test-case.md)、使用模拟对象来模拟复杂的依赖关系、采用静态代码分析工具以及将测试集成到更小、更易于管理的单元中。 [test cases](../T/test-case.md) 的持续重构以及开发人员和测试人员之间的协作也可以帮助解决这些挑战。

- **复杂性**：由于路径数量巨大，测试复杂系统中所有可能的路径可能会令人畏惧。
  - **耗时**：实现高水平的覆盖（例如路径或分支覆盖）可能非常耗时。
  - **资源密集型**：结构测试通常需要大量的计算资源来执行所有测试用例。
  - **确定正确的工具**：选择能够满足结构测试特定要求的适当工具可能很困难。
  - **维护[Test Cases](../T/test-case.md)**：随着代码库的发展，维护和更新测试用例以反映变化可能具有挑战性。
  - **不稳定**：由于计时问题或外部依赖性，测试可能会间歇性地通过或失败，从而导致不可靠的结果。
  - **理解代码内部**：测试人员需要深入了解代码内部，这可能并不总是可行或可用。
  - **与 CI/CD 集成**：确保结构测试在 CI/CD 管道中高效运行而不减慢交付过程需要仔细规划和优化。

#### 如何缓解这些挑战？

缓解[structural testing](../S/structural-testing.md) 中的挑战涉及战略规划和高效执行。 **根据风险和复杂性确定 [test cases](../T/test-case.md)** 的优先级，以确保首先覆盖关键路径。利用**代码分析工具**来识别现有测试未执行的代码区域，并重点关注这些区域以提高覆盖率。
  **尽可能自动化**，但要有选择性。使用自动化来处理重复的大容量测试，但请记住，某些场景可能需要手动 [inspection](../I/inspection.md) 或者可能不适合自动化。 **定期重构测试**以保持其有效性并减少不稳定。这包括更新测试以反映代码库中的更改，并改进其设计以使其更健壮且更易于维护。
  **利用模拟对象和服务虚拟化**来模拟不可用或过于复杂而无法包含在每次测试运行中的组件。这有助于隔离被测系统并专注于正在测试的代码。
  **实施持续集成**以在每次提交时自动运行结构测试。这有助于及早发现问题并使代码库保持在可发布状态。
  **与开发人员合作**以确保代码可测试。这可能涉及在代码审查期间倡导可测试性或与开发人员结对编写测试。
  **定期审慎地审查测试结果**，以识别模式或重复出现的问题。使用此信息来不断调整和改进您的测试策略。
  请记住，[structural testing](../S/structural-testing.md) 是一个迭代过程。根据反馈和项目不断变化的需求定期**审查和调整**您的方法。

#### 成功的结构测试有哪些例子？

[structural testing](../S/structural-testing.md) 成功的例子通常涉及以下场景：测试导致识别和解决仅通过[functional testing](../F/functional-testing.md) 可能无法检测到的缺陷。以下是一些：

- **谷歌的厕所测试**：谷歌工程师通过在浴室隔间张贴的一系列传单分享测试知识。一份传单重点介绍了使用[code coverage](../C/code-coverage.md) 工具来识别代码库中未经测试的部分，从而改进[test suites](../T/test-suite.md)。
  - **NASA 的软件保障技术中心 (SATC)**：通过应用 [structural testing](../S/structural-testing.md) 技术，SATC 能够检测飞行软件中的关键错误，如果不解决这些错误可能会导致任务失败。
  - **Netflix 的 Chaos Monkey**：虽然不是一个纯粹的 [structural testing](../S/structural-testing.md) 工具，但 Chaos Monkey 通过故意禁用服务器来测试 Netflix 基础设施的弹性，以确保系统能够承受任何单个实例的损失。
  - **Microsoft 使用静态分析工具**：Microsoft 将静态分析工具集成到其开发过程中，这些工具在部署之前执行 [structural testing](../S/structural-testing.md) 以识别安全漏洞和关键代码缺陷。
  - **开源项目**：许多开源项目使用 Travis CI 等持续集成服务，它在每次提交时运行结构测试。 Django 和 Angular 等项目具有强大的 [test suites](../T/test-suite.md)，其中包括 [structural testing](../S/structural-testing.md) 来维护代码质量。
  在每种情况下，[structural testing](../S/structural-testing.md) 通过确保软件组件的内部工作尽可能无缺陷，成为维护高质量、可靠软件的关键。

- **谷歌的厕所测试**：谷歌工程师通过在浴室隔间张贴的一系列传单分享测试知识。一份传单重点介绍了使用[code coverage](../C/code-coverage.md) 工具来识别代码库中未经测试的部分，从而改进[test suites](../T/test-suite.md)。
  - **NASA 的软件保障技术中心 (SATC)**：通过应用 [structural testing](../S/structural-testing.md) 技术，SATC 能够检测飞行软件中的关键错误，如果不解决这些错误可能会导致任务失败。
  - **Netflix 的 Chaos Monkey**：虽然不是纯粹的 [structural testing](../S/structural-testing.md) 工具，但 Chaos Monkey 通过故意禁用服务器来测试 Netflix 基础设施的弹性，以确保系统能够承受任何单个实例的损失。
  - **Microsoft 使用静态分析工具**：Microsoft 将静态分析工具集成到其开发过程中，这些工具在部署之前执行 [structural testing](../S/structural-testing.md) 以识别安全漏洞和关键代码缺陷。
  - **开源项目**：许多开源项目使用 Travis CI 等持续集成服务，它在每次提交时运行结构测试。 Django 和 Angular 等项目具有强大的 [test suites](../T/test-suite.md)，其中包括 [structural testing](../S/structural-testing.md) 来维护代码质量。

#### 结构测试如何集成到持续集成/持续部署（CI/CD）管道中？

将 [structural testing](../S/structural-testing.md) 集成到 **CI/CD 管道** 涉及自动化 [test execution](../T/test-execution.md) 作为构建和部署过程的一部分。这是一个简洁的指南：

1. **自动化结构测试**：确保使用适当的工具和框架自动化所有结构测试。测试应该可以通过命令行或通过 [test runner](../T/test-runner.md) [API](../A/api.md) 执行。
  2. **配置构建管道**：修改构建脚本以包含结构[test execution](../T/test-execution.md)。使用 Jenkins、Travis CI 或 GitLab CI 等工具来触发这些测试。
  3. **设置触发器**：定义结构测试的管道触发器。常见的做法包括在每次提交、夜间构建或管道中的特定阶段运行测试。
  4. **管理依赖项**：确保管道具有安装结构测试运行所需的任何依赖项的步骤。
  5. **[Test Environment](../T/test-environment.md)**：配置一致的测试环境，尽可能与生产匹配，以确保测试可靠性。
  6. **测试报告**：实施测试报告工具来收集和可视化测试结果。这应包括有关 [code coverage](../C/code-coverage.md) 和任何检测到的问题的详细信息。
  7. **快速失败**：将管道配置为在测试失败时停止。这确保了即时反馈并防止错误代码在管道中进一步发展。
  8. **质量关卡**：根据[structural testing](../S/structural-testing.md) 指标（例如[code coverage](../C/code-coverage.md) 阈值）建立质量关卡。仅当构建符合定义的标准时才允许它们通过这些门。
  9. **反馈循环**：集成通知以提醒开发人员测试结果，从而能够快速响应故障或问题。
  10. **持续改进**：定期审查测试结果和覆盖率报告，以确定 [test suite](../T/test-suite.md) 中需要额外测试或潜在改进的领域。
  通过遵循这些步骤，[structural testing](../S/structural-testing.md) 成为 CI/CD 流程的无缝且不可或缺的一部分，有助于提高代码质量和更可靠的软件版本。

1. **自动化结构测试**：确保使用适当的工具和框架自动化所有结构测试。测试应该可以通过命令行或通过 [test runner](../T/test-runner.md) [API](../A/api.md) 执行。
  2. **配置构建管道**：修改构建脚本以包含结构[test execution](../T/test-execution.md)。使用 Jenkins、Travis CI 或 GitLab CI 等工具来触发这些测试。
  3. **设置触发器**：定义结构测试的管道触发器。常见的做法包括在每次提交、夜间构建或管道中的特定阶段运行测试。
  4. **管理依赖项**：确保管道具有安装结构测试运行所需的任何依赖项的步骤。
  5. **[Test Environment](../T/test-environment.md)**：配置尽可能与生产匹配的一致测试环境，以确保测试可靠性。
  6. **测试报告**：实施测试报告工具来收集和可视化测试结果。这应包括[code coverage](../C/code-coverage.md) 的详细信息以及任何检测到的问题。
  7. **快速失败**：将管道配置为在测试失败时停止。这确保了即时反馈并防止错误代码在管道中进一步发展。
  8. **质量关卡**：根据[structural testing](../S/structural-testing.md) 指标（例如[code coverage](../C/code-coverage.md) 阈值）建立质量关卡。仅当构建符合定义的标准时才允许它们通过这些门。
  9. **反馈循环**：集成通知以提醒开发人员测试结果，从而能够快速响应故障或问题。
  10. **持续改进**：定期审查测试结果和覆盖率报告，以确定 [test suite](../T/test-suite.md) 中需要额外测试或潜在改进的领域。
