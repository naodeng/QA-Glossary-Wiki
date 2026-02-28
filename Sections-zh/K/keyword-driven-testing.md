# 关键字驱动测试

<!-- TOC START -->
- [相关术语：](#相关术语：)
- [有关关键字驱动测试的问题吗？](#有关关键字驱动测试的问题吗？)
  - [基础知识和重要性](#基础知识和重要性)
    - [什么是关键字驱动测试？](#什么是关键字驱动测试？)
    - [为什么关键字驱动测试在软件测试中很重要？](#为什么关键字驱动测试在软件测试中很重要？)
    - [关键字驱动测试的关键组成部分是什么？](#关键字驱动测试的关键组成部分是什么？)
    - [关键字驱动测试如何提高测试效率？](#关键字驱动测试如何提高测试效率？)
    - [关键字驱动测试是如何实施的？](#关键字驱动测试是如何实施的？)
    - [关键字驱动测试涉及哪些步骤？](#关键字驱动测试涉及哪些步骤？)
    - [关键字驱动测试常用哪些工具？](#关键字驱动测试常用哪些工具？)
    - [如何创建用于自动化测试的关键字驱动框架？](#如何创建用于自动化测试的关键字驱动框架？)
  - [优点和缺点](#优点和缺点)
    - [关键字驱动测试的优点是什么？](#关键字驱动测试的优点是什么？)
    - [关键字驱动测试有哪些缺点？](#关键字驱动测试有哪些缺点？)
    - [在什么情况下关键字驱动测试最有益？](#在什么情况下关键字驱动测试最有益？)
    - [关键字驱动测试与其他测试方法相比如何？](#关键字驱动测试与其他测试方法相比如何？)
  - [实际应用](#实际应用)
    - [您能否提供一个有效使用关键字驱动测试的情况示例？](#您能否提供一个有效使用关键字驱动测试的情况示例？)
    - [关键字驱动测试如何应用于敏捷开发？](#关键字驱动测试如何应用于敏捷开发？)
    - [关键字驱动测试有哪些实际应用？](#关键字驱动测试有哪些实际应用？)
    - [如何将关键字驱动测试集成到持续集成/持续部署 (CI/CD) 管道中？](#如何将关键字驱动测试集成到持续集成持续部署-cicd-管道中？)
<!-- TOC END -->

关键词驱动测试

是一个

功能测试

接近哪里

测试用例

设计与其执行是分开的。关键字代表用户对测试对象的操作，使得

测试用例

更清晰、更可维护。

## 相关术语：

- [Data-Driven Testing](../D/data-driven-testing.md)

## 有关关键字驱动测试的问题吗？

### 基础知识和重要性

#### 什么是关键字驱动测试？

[Keyword Driven Testing](../K/keyword-driven-testing.md) (KDT) 是[test automation](../T/test-automation.md) 中的一种脚本技术，其中[test case](../T/test-case.md) 指令与实际[test script](../T/test-script.md) 逻辑分开。它利用一组预定义的关键字来表示要在被测应用程序 (AUT) 上执行的操作。这些关键字是用户交互或系统状态的抽象表示，使测试更易于阅读和维护。
  在 KDT 中，[test data](../T/test-data.md) 和关键字通常存储在外部数据文件或表中，允许非技术涉众为测试创建和修改做出贡献，而无需了解底层代码。该方法提高了代码和[test cases](../T/test-case.md)的可重用性，因为相同的关键字可以在不同的[test scripts](../T/test-script.md)中使用。
  [Test automation](../T/test-automation.md) 工程师通过首先定义关键字及其相关操作来实现 KDT。然后，他们通过以反映执行测试所需的用户交互的方式对这些关键字进行排序来创建[test cases](../T/test-case.md)。 [test automation](../T/test-automation.md) 框架解释关键字并在 AUT 上执行相应的操作。
  KDT 通常与其他测试方法结合使用，以增强 [test coverage](../T/test-coverage.md) 和效率。在测试需要快速适应应用程序的变化而无需大量修改脚本的情况下，它特别有效。虽然 KDT 具有多种优势，但它也有局限性，例如设置关键字库所需的初始时间投入以及降低 [test script](../T/test-script.md) 粒度的潜力。

#### 为什么关键字驱动测试在软件测试中很重要？

[Keyword Driven Testing](../K/keyword-driven-testing.md) (KDT) 在[software testing](../S/software-testing.md) 中很重要，原因有几个。它促进**[test automation](../T/test-automation.md)逻辑**与实际[test case](../T/test-case.md)的解耦，这意味着非技术利益相关者可以为测试设计做出贡献，而无需了解底层代码。这种抽象也有利于**更容易维护**；当UI改变时，只有关键字需要更新，而不是单独的测试。
  KDT 支持代码的**可重用性**。关键字可以跨多个[test cases](../T/test-case.md)使用，减少冗余和编写测试脚本所需的工作量。这种可重用性还导致测试编写和执行方式的**一致性**，从而更容易理解和管理[test suite](../T/test-suite.md)。
  此外，KDT 允许具有不同技术专业水平的团队成员之间**更好的协作**。测试人员可以使用一组通用关键字定义[test cases](../T/test-case.md)，而自动化工程师则专注于实现这些关键字。
  在**可扩展性**方面，KDT 框架可以随着项目的增长而不会变得难以管理。随着关键字数量的增加，可以将它们组织到库中，从而使其易于管理和扩展。
  最后，KDT 可以相对轻松地集成到**CI/CD 管道**和**敏捷实践**中。它与敏捷环境中的迭代开发和频繁变化很好地结合在一起，并且关键字可以快速更新以反映新的需求或功能。
  从本质上讲，KDT 是一种关键方法，可以增强协作、[maintainability](../M/maintainability.md) 和[test automation](../T/test-automation.md) 中的可扩展性，使其成为旨在实现高效且有效的测试流程的团队的宝贵方法。

#### 关键字驱动测试的关键组成部分是什么？

[Keyword Driven Testing](../K/keyword-driven-testing.md) (KDT) 的关键组件包括：

- **关键字**：这些是 KDT 的构建块，表示可以在被测应用程序 (AUT) 上执行的操作。每个关键字对应于执行特定操作的函数或方法，例如“单击”、“输入文本”或“验证元素”。
  - **[Test Data](../T/test-data.md)**：关键字用于在 AUT 上执行操作的数据。它与[test scripts](../T/test-script.md) 分开，以允许数据驱动的测试和更轻松的维护。
  - **[Test Scripts](../T/test-script.md)**：这些是形成[test cases](../T/test-case.md) 的关键字序列。脚本以表格格式编写，即使对于非程序员来说也易于阅读和编写。
  - **函数库**：实现与关键字关联的操作的函数或方法的集合。该库是高级关键字和低级技术实现之间的桥梁。
  - **[Test Runner](../T/test-runner.md)**：读取[test scripts](../T/test-script.md)，解释关键字，并从函数库中调用相应函数来执行测试的引擎。
  - **结果报告器**：记录 [test executions](../T/test-execution.md) 结果的组件，生成详细说明哪些测试通过、失败以及原因的日志和报告。
  - **[Test Management](../T/test-management.md)**：组织和管理[test cases](../T/test-case.md)、脚本、数据和结果，通常与其他工具集成以进行版本控制、[bug](../B/bug.md) 跟踪和项目管理。
  使用这些组件，KDT 从[test case](../T/test-case.md) 设计中抽象出[test case](../T/test-case.md) 实现，从而为[test automation](../T/test-automation.md) 提供更加结构化和可维护的方法。

- **关键字**：这些是 KDT 的构建块，表示可以在被测应用程序 (AUT) 上执行的操作。每个关键字对应于执行特定操作的函数或方法，例如“单击”、“输入文本”或“验证元素”。
  - **[Test Data](../T/test-data.md)**：关键字用于在 AUT 上执行操作的数据。它与[test scripts](../T/test-script.md) 分开，以允许数据驱动的测试和更轻松的维护。
  - **[Test Scripts](../T/test-script.md)**：这些是形成[test cases](../T/test-case.md) 的关键字序列。脚本以表格格式编写，即使对于非程序员来说也易于阅读和编写。
  - **函数库**：实现与关键字关联的操作的函数或方法的集合。该库是高级关键字和低级技术实现之间的桥梁。
  - **[Test Runner](../T/test-runner.md)**：读取[test scripts](../T/test-script.md)，解释关键字，并从函数库中调用相应函数来执行测试的引擎。
  - **结果报告器**：记录 [test executions](../T/test-execution.md) 结果的组件，生成日志和报告，详细说明哪些测试通过、失败以及原因。
  - **[Test Management](../T/test-management.md)**：组织和管理[test cases](../T/test-case.md)、脚本、数据和结果，通常与其他工具集成以进行版本控制、[bug](../B/bug.md) 跟踪和项目管理。

#### 关键字驱动测试如何提高测试效率？

[Keyword Driven Testing](../K/keyword-driven-testing.md) (KDT) 主要通过**将测试逻辑与[test data](../T/test-data.md)**分离来提高测试效率，允许非技术利益相关者为测试创建和维护做出贡献。这种抽象使关键字和[test scripts](../T/test-script.md)具有**更高级别的可重用性**，因为通用功能可以封装到单个关键字中。
  效率增益通过以下方式实现：

- **更容易维护**：被测应用程序的更改可能只需要更新关键字，而不是整个测试套件。
  - **提高可读性**：以业务可读格式编写的测试用例可以更轻松地理解测试的目的和操作。
  - **更快的测试创建**：一旦建立了关键字库，只需组合现有关键字即可创建新的测试。
  - **增强协作**：具有不同技术技能的团队成员可以为测试过程做出贡献，因为创建或修改测试不需要理解代码。
  - **更好的资源利用率**：测试人员可以专注于创建更复杂的测试，并将执行留给更少的技术资源甚至自动化流程。
  通过利用 KDT，组织可以简化其测试流程，减少 [test script](../T/test-script.md) 开发和维护所花费的时间，并最终加速软件产品的交付。

- **更容易维护**：被测应用程序的更改可能只需要更新关键字，而不是整个测试套件。
  - **提高可读性**：以业务可读格式编写的测试用例可以更轻松地理解测试的目的和操作。
  - **更快的测试创建**：一旦建立了关键字库，只需组合现有关键字即可创建新的测试。
  - **增强协作**：具有不同技术技能的团队成员可以为测试过程做出贡献，因为创建或修改测试不需要理解代码。
  - **更好的资源利用率**：测试人员可以专注于创建更复杂的测试，并将执行留给更少的技术资源甚至自动化流程。

＃＃＃ 执行

#### 关键字驱动测试是如何实施的？

[Keyword Driven Testing](../K/keyword-driven-testing.md) (KDT) 是通过一系列将测试设计与[test execution](../T/test-execution.md) 分开的步骤来实现的。这是一个简洁的指南：

1. **识别关键字**：确定应用程序中常用的操作，例如“登录”、“clickButton”或“verifyText”。
  2. **创建关键字函数**：编写执行这些操作的函数。如果可能的话，每个函数都应该是可重用的并且独立于应用程序。

    ```
    function clickButton(buttonName) {
        // Code to click a button
    }
    ```

3. **设计[Test Cases](../T/test-case.md)**：以表格形式定义[test cases](../T/test-case.md)，并包含关键字和相应的参数。这可以通过电子表格或任何其他简单的数据驱动格式来完成。
    关键字参数1参数2open浏览器URLinputText用户名user1inputText密码pass123clickButton登录

4. **开发[Test Scripts](../T/test-script.md)**：创建读取[test cases](../T/test-case.md) 并使用指定参数调用关键字函数的脚本。

    ```
    testRunner.run('path/to/testcase.xlsx');
    ```

5. **执行测试**：运行[test scripts](../T/test-script.md)。运行程序应该解释关键字和参数，然后调用适当的函数。
  6. **报告结果**：捕获每个关键字执行的结果并以可读的格式报告它们。
  通过执行这些步骤，您可以实施 KDT 方法来增强测试 [maintainability](../M/maintainability.md) 并促进代码重用。请记住使关键字尽可能抽象，以最大限度地提高其在不同[test cases](../T/test-case.md) 中的效用。

1. **识别关键字**：确定应用程序中常用的操作，例如“登录”、“clickButton”或“verifyText”。
  2. **创建关键字函数**：编写执行这些操作的函数。如果可能的话，每个函数都应该是可重用的并且独立于应用程序。

    ```
    function clickButton(buttonName) {
        // Code to click a button
    }
    ```

3. **设计[Test Cases](../T/test-case.md)**：以表格形式定义[test cases](../T/test-case.md)，并包含关键字和相应的参数。这可以通过电子表格或任何其他简单的数据驱动格式来完成。
    关键字参数1参数2open浏览器URLinputText用户名user1inputText密码pass123clickButton登录

4. **开发[Test Scripts](../T/test-script.md)**：创建读取[test cases](../T/test-case.md) 并使用指定参数调用关键字函数的脚本。

    ```
    testRunner.run('path/to/testcase.xlsx');
    ```

5. **执行测试**：运行[test scripts](../T/test-script.md)。运行程序应该解释关键字和参数，然后调用适当的函数。
  6. **报告结果**：捕获每个关键字执行的结果并以可读的格式报告它们。

#### 关键字驱动测试涉及哪些步骤？

[Keyword Driven Testing](../K/keyword-driven-testing.md) (KDT)涉及的步骤如下：

1. **识别[Test Cases](../T/test-case.md)**：确定需要测试的功能并概述[test cases](../T/test-case.md)。
  2. **定义关键字**：创建一组表示用户操作或与系统交互的操作词或短语。
  3. **创建[Test Data](../T/test-data.md)**：为[test cases](../T/test-case.md) 准备必要的数据输入。
  4. **开发[Test Scripts](../T/test-script.md)**：编写将关键字映射到特定自动化命令或函数的脚本。这通常涉及创建与关键字对应的函数库。
  5. **设计测试步骤**：将关键字和[test data](../T/test-data.md)组合起来形成模拟用户操作的测试步骤。
  6. **组织[Test Suites](../T/test-suite.md)**：将相关测试步骤分组为[test cases](../T/test-case.md) 和[test suites](../T/test-suite.md)。
  7. **执行测试**：使用解释关键字并执行相应操作的自动化工具运行[test scripts](../T/test-script.md)。
  8. **记录结果**：捕获[test execution](../T/test-execution.md) 的结果，包括通过/失败状态和任何差异。
  9. **报告缺陷**：记录并报告测试期间发现的任何缺陷或问题。
  10. **维护测试工件**：根据需要更新关键字、[test data](../T/test-data.md) 和脚本，以适应被测应用程序中的更改。
  KDT 需要一种结构良好的方法来确保测试可重用、可维护且易于理解。定期审查和更新关键字库和相关脚本对于保持测试过程高效和有效至关重要。

1. **识别[Test Cases](../T/test-case.md)**：确定需要测试的功能并概述[test cases](../T/test-case.md)。
  2. **定义关键字**：创建一组表示用户操作或与系统交互的操作词或短语。
  3. **创建[Test Data](../T/test-data.md)**：为[test cases](../T/test-case.md) 准备必要的数据输入。
  4. **开发[Test Scripts](../T/test-script.md)**：编写将关键字映射到特定自动化命令或函数的脚本。这通常涉及创建与关键字对应的函数库。
  5. **设计测试步骤**：将关键字和[test data](../T/test-data.md)组合起来形成模拟用户操作的测试步骤。
  6. **组织[Test Suites](../T/test-suite.md)**：将相关测试步骤分组为[test cases](../T/test-case.md) 和[test suites](../T/test-suite.md)。
  7. **执行测试**：使用解释关键字并执行相应操作的自动化工具运行[test scripts](../T/test-script.md)。
  8. **记录结果**：捕获[test execution](../T/test-execution.md) 的结果，包括通过/失败状态和任何差异。
  9. **报告缺陷**：记录并报告测试期间发现的任何缺陷或问题。
  10. **维护测试工件**：根据需要更新关键字、[test data](../T/test-data.md) 和脚本，以适应被测应用程序中的更改。

#### 关键字驱动测试常用哪些工具？

**[Keyword Driven Testing](../K/keyword-driven-testing.md)** 的常用工具包括：

- **[Selenium](../S/selenium.md)** ：支持多种语言和浏览器的开源工具。可以使用 Robot Framework 等框架将其扩展为关键字驱动测试。
  - **机器人框架**：使用关键字驱动方法的开源自动化框架。它与 Selenium 集成以进行 Web 测试。
  - **QTP/UFT（统一[Functional Testing](../F/functional-testing.md)）**：Micro Focus 的商业工具，提供内置关键字视图来创建和执行测试。
  - **TestComplete** ：SmartBear 的商业工具，提供关键字驱动的测试功能，允许测试人员无需编写脚本即可创建自动化测试。
  - **Katalon Studio**：一种支持关键字驱动测试的自动化工具，构建在 Selenium 和 Appium 框架之上。
  - **Ranorex**：一种商业工具，提供关键字驱动的测试方法，使其适合各种技能水平的用户。
  - **Cucumber** ：支持行为驱动开发（BDD）的开源工具，可适用于使用 Gherkin 语言的关键字驱动测试。
  这些工具提供了各种功能来促进关键字驱动的测试，例如测试记录、关键字库以及与其他[software testing](../S/software-testing.md) 工具的轻松集成。经验丰富的自动化工程师可以利用这些工具来创建强大的关键字驱动框架，从而提高 [test automation](../T/test-automation.md) 效率。

- **[Selenium](../S/selenium.md)** ：支持多种语言和浏览器的开源工具。可以使用 Robot Framework 等框架将其扩展为关键字驱动测试。
  - **机器人框架**：使用关键字驱动方法的开源自动化框架。它与 Selenium 集成以进行 Web 测试。
  - **QTP/UFT（统一[Functional Testing](../F/functional-testing.md)）**：Micro Focus 的商业工具，提供内置关键字视图来创建和执行测试。
  - **TestComplete** ：SmartBear 的商业工具，提供关键字驱动的测试功能，允许测试人员无需编写脚本即可创建自动化测试。
  - **Katalon Studio**：一种支持关键字驱动测试的自动化工具，构建在 Selenium 和 Appium 框架之上。
  - **Ranorex**：一种商业工具，提供关键字驱动的测试方法，使其适合各种技能水平的用户。
  - **Cucumber** ：支持行为驱动开发（BDD）的开源工具，可适用于使用 Gherkin 语言的关键字驱动测试。

#### 如何创建用于自动化测试的关键字驱动框架？

创建关键字驱动的框架涉及几个步骤：

1. **识别关键字**：确定可以抽象为关键字的常见操作，例如`Login`、`ClickButton` 或`EnterText`。
  2. **设计关键字结构**：定义关键字的结构，包括名称、参数和返回值。
  3. **创建关键字函数**：实现执行关键字描述的操作的函数。使用 [test automation](../T/test-automation.md) 工具支持的编程语言。

  ```
  function EnterText(fieldIdentifier, textValue) {
      // Code to enter text into a field
  }
  ```

1. **开发[Test Scripts](../T/test-script.md)** ：使用关键字编写测试脚本。脚本应该具有可读性和可维护性，重点关注测试流程而不是技术细节。

  ```
  EnterText("username", "testuser");
  EnterText("password", "securepass");
  ClickButton("login");
  ```

1. **构建执行引擎**：开发或配置一个可以解释关键字并调用相应函数的执行引擎。
  2. **数据驱动方法**：（可选）与外部数据源集成以驱动使用不同数据集的测试。
  3. **日志记录和报告**：对关键字执行的操作实施日志记录并生成报告以提供对[test execution](../T/test-execution.md) 的深入了解。
  4. **维护**：定期更新关键字和脚本，以适应被测应用的变化。
  5. **审查和细化**：不断审查框架的有效性并细化关键字和功能，以实现更好的抽象和可重用性。
  请记住保持框架**模块化**和**可扩展**，以适应未来的[test cases](../T/test-case.md)和应用程序更改。使用版本控制来管理变更并与其他团队成员有效协作。

1. **识别关键字**：确定可以抽象为关键字的常见操作，例如`Login`、`ClickButton` 或`EnterText`。
  2. **设计关键字结构**：定义关键字的结构，包括名称、参数和返回值。
  3. **创建关键字函数**：实现执行关键字描述的操作的函数。使用 [test automation](../T/test-automation.md) 工具支持的编程语言。
  1. **开发[Test Scripts](../T/test-script.md)** ：使用关键字编写测试脚本。脚本应该具有可读性和可维护性，重点关注测试流程而不是技术细节。
  1. **构建执行引擎**：开发或配置一个可以解释关键字并调用相应函数的执行引擎。
  2. **数据驱动方法**：（可选）与外部数据源集成以驱动使用不同数据集的测试。
  3. **日志记录和报告**：对关键字执行的操作实施日志记录并生成报告以提供对[test execution](../T/test-execution.md) 的深入了解。
  4. **维护**：定期更新关键字和脚本，以适应被测应用的变化。
  5. **审查和细化**：不断审查框架的有效性并细化关键字和功能，以实现更好的抽象和可重用性。

### 优点和缺点

#### 关键字驱动测试的优点是什么？

[Keyword Driven Testing](../K/keyword-driven-testing.md) (KDT) 的优点包括：

- **抽象**：KDT 抽象测试自动化细节，允许非技术利益相关者理解并参与测试创建和验证。
  - **可重用性**：关键字可以在多个测试用例中重用，减少重复和维护工作。
  - **模块化**：被测应用程序的更改通常只需要更新单个关键字而不是整个测试，从而增强可维护性。
  - **可扩展性**：可以添加新关键字来扩展框架的功能，而无需更改现有测试。
  - **可读性**：用关键字编写的测试更具可读性和可理解性，这简化了同行评审和新团队成员的入职。
  - **关注点分离**：测试用例设计与关键字的技术实现分离，让测试人员专注于测试设计，开发人员专注于关键字实现。
  - **协作**：通过使用通用的、易于理解的测试用例语言来促进技术和非技术团队成员之间的协作。
  - **工具独立性**：关键字充当自动化工具的抽象层，可以在必要时更轻松地在工具之间进行迁移。
  在实践中，KDT 可以简化 [test automation](../T/test-automation.md) 流程，使其更加高效并可供更广泛的团队成员使用，同时还提供可扩展且可维护的方法来管理自动化测试。

- **抽象**：KDT 抽象测试自动化细节，允许非技术利益相关者理解并参与测试创建和验证。
  - **可重用性**：关键字可以在多个测试用例中重用，减少重复和维护工作。
  - **模块化**：被测应用程序的更改通常只需要更新单个关键字而不是整个测试，从而增强可维护性。
  - **可扩展性**：可以添加新关键字来扩展框架的功能，而无需更改现有测试。
  - **可读性**：用关键字编写的测试更具可读性和可理解性，这简化了同行评审和新团队成员的入职。
  - **关注点分离**：测试用例设计与关键字的技术实现分离，让测试人员专注于测试设计，开发人员专注于关键字实现。
  - **协作**：通过使用通用的、易于理解的测试用例语言来促进技术和非技术团队成员之间的协作。
  - **工具独立性**：关键字充当自动化工具的抽象层，可以在必要时更轻松地在工具之间进行迁移。

#### 关键字驱动测试有哪些缺点？

[Keyword Driven Testing](../K/keyword-driven-testing.md) (KDT) 有几个可能影响其有效性的缺点：

- **初始[Setup](../S/setup.md) 复杂性**：KDT 框架需要大量的前期投资来开发。这包括定义关键字、创建库和设置 [test infrastructure](../T/test-infrastructure.md)，这可能既耗时又复杂。
  - **维护开销**：随着时间的推移，随着应用程序的发展，关键字库和 [test scripts](../T/test-script.md) 可能需要大量维护才能使其保持最新，这可能会占用大量资源。
  - **学习曲线**：测试人员必须学习关键字的具体语法和范围，这对于那些不熟悉框架或刚接触自动化的人来说可能是一个障碍。
  - **有限的灵活性**：预定义的关键字可能会限制处理复杂[test scenarios](../T/test-scenario.md)的能力。测试人员可能会发现表达某些尚未被现有关键字封装的操作或验证具有挑战性。
  - **性能问题**：KDT 框架可能会引入性能瓶颈，特别是在关键字抽象层未优化的情况下，与更直接的脚本方法相比，会导致 [test execution](../T/test-execution.md) 时间变慢。
  - **工具依赖性**：KDT 的有效性通常与所使用工具的功能相关。如果该工具缺乏某些功能，则可能会限制关键字驱动方法所能实现的目标。
  - **简单测试的开销**：对于简单的[test cases](../T/test-case.md)，使用 KDT 框架的开销可能不合理，因为可以使用更简单的测试方法以更少的工作量实现相同的结果。
  - **初始[Setup](../S/setup.md) 复杂性**：KDT 框架需要大量的前期投资来开发。这包括定义关键字、创建库和设置 [test infrastructure](../T/test-infrastructure.md)，这可能既耗时又复杂。
  - **维护开销**：随着时间的推移，随着应用程序的发展，关键字库和[test scripts](../T/test-script.md)可能需要大量维护才能使其保持最新，这可能会占用大量资源。
  - **学习曲线**：测试人员必须学习关键字的具体语法和范围，这对于那些不熟悉框架或刚接触自动化的人来说可能是一个障碍。
  - **有限的灵活性**：预定义的关键字可能会限制处理复杂[test scenarios](../T/test-scenario.md)的能力。测试人员可能会发现表达某些尚未被现有关键字封装的操作或验证具有挑战性。
  - **性能问题**：KDT 框架可能会引入性能瓶颈，特别是在关键字抽象层未优化的情况下，与更直接的脚本方法相比，会导致[test execution](../T/test-execution.md) 时间变慢。
  - **工具依赖性**：KDT 的有效性通常与所使用工具的功能相关。如果该工具缺乏某些功能，则可能会限制关键字驱动方法所能实现的目标。
  - **简单测试的开销**：对于简单的[test cases](../T/test-case.md)，使用 KDT 框架的开销可能不合理，因为可以使用更简单的测试方法以更少的工作量实现相同的结果。

#### 在什么情况下关键字驱动测试最有益？

[Keyword Driven Testing](../K/keyword-driven-testing.md) 在以下情况下特别有用：

- **[Test cases](../T/test-case.md) 涉及高级别数据输入**：通过将测试逻辑与[test data](../T/test-data.md) 分离，可以在使用不同数据集测试类似功能时轻松修改和重用脚本。
  - **非技术利益相关者参与**：业务分析师或产品所有者可以通过定义关键字来为 [test case](../T/test-case.md) 设计做出贡献，从而使流程更具协作性。
  - **应用程序 UI 中的频繁更改**：关键字从底层自动化代码中抽象出测试步骤，因此 UI 中的更改可能需要对关键字进行最少的更新，而不是进行大量的脚本修改。
  - **具有重复操作的大型[test suites](../T/test-suite.md)**：它促进了关键字在不同[test cases](../T/test-case.md)之间的可重用性，减少了编写和维护脚本的工作量。
  - **具有不同技能水平的跨职能团队**：编程专业知识较少的团队成员可以编写和理解测试，而更多技术成员可以专注于实现强大的关键字。
  - **长期项目**：随着项目的发展，可以扩展关键字库，从而提供可扩展的自动化方法，以适应应用程序不断增长的复杂性。
  - **[Localization testing](../L/localization-testing.md)**：关键字可以设计为处理不同的数据集，以便在不同的语言环境中测试相同的功能，而无需更改测试逻辑。
  在这些场景中，[Keyword Driven Testing](../K/keyword-driven-testing.md) 简化了测试流程，增强了协作，并提高了[maintainability](../M/maintainability.md) 和[test automation](../T/test-automation.md) 工作的可扩展性。

- **[Test cases](../T/test-case.md) 涉及高级别数据输入**：通过将测试逻辑与[test data](../T/test-data.md) 分离，可以在使用不同数据集测试类似功能时轻松修改和重用脚本。
  - **非技术利益相关者参与**：业务分析师或产品所有者可以通过定义关键字来为 [test case](../T/test-case.md) 设计做出贡献，从而使流程更具协作性。
  - **应用程序 UI 中的频繁更改**：关键字从底层自动化代码中抽象出测试步骤，因此 UI 中的更改可能需要对关键字进行最少的更新，而不是进行大量的脚本修改。
  - **具有重复操作的大型[test suites](../T/test-suite.md)**：它促进了关键字在不同[test cases](../T/test-case.md)之间的可重用性，减少了编写和维护脚本的工作量。
  - **具有不同技能水平的跨职能团队**：编程专业知识较少的团队成员可以编写和理解测试，而更多技术成员可以专注于实现强大的关键字。
  - **长期项目**：随着项目的发展，可以扩展关键字库，从而提供可扩展的自动化方法，以适应应用程序不断增长的复杂性。
  - **[Localization testing](../L/localization-testing.md)**：关键字可以设计为处理不同的数据集，以便在不同区域设置中测试相同的功能，而无需更改测试逻辑。

#### 关键字驱动测试与其他测试方法相比如何？

[Keyword Driven Testing](../K/keyword-driven-testing.md) (KDT) 与 **数据驱动测试** (DDT)、**行为驱动开发** ([BDD](../B/bdd.md)) 和 **基于模型的测试** (MBT) 等方法在几个方面有所不同：

- **抽象级别**：与 DDT 相比，KDT 在更高的抽象级别上运行。 DDT 侧重于使用不同数据集参数化测试，而 KDT 将 [test data](../T/test-data.md) 和操作抽象为关键字，使其更具可读性和可维护性。
  - **[Test Case](../T/test-case.md) 设计**：在[BDD](../B/bdd.md) 中，测试是用描述应用程序行为的自然语言编写的，通常侧重于最终用户体验。然而，KDT 使用预定义的关键字来表示操作和数据，描述性较少，但更加系统化。
  - **测试维护**：由于其模块化特性，KDT 可以比传统的基于脚本的方法提供更好的[maintainability](../M/maintainability.md)。应用程序中的更改通常可以通过更新关键字而不是[test scripts](../T/test-script.md)来适应。
  - **技术知识**：KDT 框架可以设计为比基于脚本或 MBT 方法需要更少的技术知识，从而允许非技术利益相关者参与[test automation](../T/test-automation.md)。
  - **工具独立性**：KDT 通常与工具无关，这意味着同一组关键字可以在不同的自动化工具中使用，而其他方法可能与特定工具或语言更紧密地耦合。
  - **灵活性和可重用性**：KDT 的模块化方法促进了关键字在不同 [test cases](../T/test-case.md) 之间的可重用性，这在代码重复更常见的基于脚本的测试中不太常见。
  总之，KDT 提供了可读性、[maintainability](../M/maintainability.md) 和可重用性的独特组合，使其与其他可能优先考虑其他方面（例如详细行为描述 ([BDD](../B/bdd.md)) 或数据变化 (DDT)）的测试方法区分开来。

- **抽象级别**：与 DDT 相比，KDT 在更高的抽象级别上运行。 DDT 侧重于使用不同数据集参数化测试，而 KDT 将 [test data](../T/test-data.md) 和操作抽象为关键字，使其更具可读性和可维护性。
  - **[Test Case](../T/test-case.md) 设计**：在[BDD](../B/bdd.md) 中，测试是用自然语言编写的，描述应用程序的行为，通常关注最终用户体验。然而，KDT 使用预定义的关键字来表示操作和数据，描述性较少，但更加系统化。
  - **测试维护**：由于其模块化特性，KDT 可以比传统的基于脚本的方法提供更好的[maintainability](../M/maintainability.md)。应用程序中的更改通常可以通过更新关键字而不是[test scripts](../T/test-script.md)来适应。
  - **技术知识**：KDT 框架可以设计为比基于脚本或 MBT 方法需要更少的技术知识，从而允许非技术利益相关者参与[test automation](../T/test-automation.md)。
  - **工具独立性**：KDT 通常与工具无关，这意味着同一组关键字可以在不同的自动化工具中使用，而其他方法可能与特定工具或语言更紧密地耦合。
  - **灵活性和可重用性**：KDT 的模块化方法促进了不同 [test cases](../T/test-case.md) 之间关键字的可重用性，这在代码重复更常见的基于脚本的测试中不太常见。

### 实际应用

#### 您能否提供一个有效使用关键字驱动测试的情况示例？

**[Keyword Driven Testing](../K/keyword-driven-testing.md) (KDT)** 的有效 [use case](../U/use-case.md) 是在大型电子商务平台回归套件的自动化过程中进行的。该平台拥有跨网络和移动设备的多个用户界面，具有各种用户流程，例如帐户创建、产品搜索、购物车管理和结账流程。
  测试团队创建了一个全面的关键字库，其中封装了`EnterText`、`ClickButton`、`VerifyProductDetails` 和`CheckoutItem` 等操作。这些关键字抽象了底层的技术实现，允许测试人员以表格格式编写[test cases](../T/test-case.md)，而无需深厚的编程知识。
  例如，可以使用关键字自动简化结账流程，如下所示：

  ```
  OpenBrowser 'https://www.example-ecommerce.com'
  EnterText 'SearchBox', 'wireless headphones'
  ClickButton 'SearchSubmit'
  VerifyProductDetails 'ProductList', 'Wireless Headphones XYZ'
  ClickButton 'AddToCart'
  CheckoutItem
  ```这种方法使团队能够快速适应 UI 更改。当结帐按钮被重命名并移动到页面的不同部分时，只有`CheckoutItem` 关键字定义需要更新，而不是每个单独的[test case](../T/test-case.md)。
  此外，关键字驱动的方法促进了开发人员、测试人员和业务分析师之间更好的协作。业务分析师可以审查基于关键字的[test scripts](../T/test-script.md)，以确保它们符合业务需求，而开发人员可以随着应用程序的发展专注于维护关键字定义。
  KDT 框架支持并行执行以及与 CI/CD 管道的集成，显着减少回归套件的执行时间并改善开发团队的反馈循环。

#### 关键字驱动测试如何应用于敏捷开发？

[Keyword Driven Testing](../K/keyword-driven-testing.md) (KDT) 因其灵活性和可重用性而与[Agile development](../A/agile-development.md) 非常一致。在敏捷中，变化频繁且[iterations](../I/iteration.md) 快速，KDT 允许快速更新[test cases](../T/test-case.md)，而不需要深入的技术知识。
  **测试人员和利益相关者**可以协作定义代表被测应用程序内操作的关键字。这种合作确保每个人都清楚地了解[test coverage](../T/test-coverage.md)，并可以为测试设计过程做出贡献，从而促进**个人以及流程和工具交互的敏捷原则**。
  KDT的抽象层意味着当应用程序发生变化时，只需更新与关键字相关的底层代码。这**最大限度地减少了维护**，并允许[test suite](../T/test-suite.md)**快速适应**新功能或现有功能的更改。
  此外，KDT 可以集成到**敏捷仪式**中。例如，在待办事项细化或冲刺计划期间，团队可以为即将推出的功能定义关键字。这种主动方法意味着一旦功能准备好进行测试，就可以快速组装自动化[test cases](../T/test-case.md)。
  在实践**行为驱动开发 ([BDD](../B/bdd.md))** 的敏捷团队中，KDT 可以通过使用预定义关键字将自然语言场景转换为自动化测试来进行补充。这种协同作用增强了沟通并确保验收标准清楚地转化为自动化测试。
  最后，KDT 框架可以轻松集成到 **CI/CD 管道**，允许每次构建自动进行[regression testing](../R/regression-testing.md)，确保敏捷团队立即收到有关其变更影响的反馈。

#### 关键字驱动测试有哪些实际应用？

[Keyword Driven Testing](../K/keyword-driven-testing.md) (KDT) 查找各个领域的实际应用程序，其中 [test cases](../T/test-case.md) 可以抽象为关键字，使利益相关者更容易理解并为自动化测试做出贡献。以下是一些应用：

- **电子商务平台**：KDT 允许测试人员在不同的 [test scenarios](../T/test-scenario.md) 之间重复使用关键字，从而简化了用户界面和工作流程的测试，例如搜索、添加到购物车和结账流程。
  - **银行软件**：为了验证复杂的交易流程，KDT 有助于创建可读的[test cases](../T/test-case.md)，可以轻松修改以响应银行法规的频繁变化。
  - **医疗保健系统**：由于需要严格合规性和数据完整性，KDT 有助于自动执行患者登记、预约安排和医疗计费的重复测试。
  - **移动应用程序**：KDT 用于通过定义滑动、点击和捏合等手势的关键字来测试跨平台兼容性和用户交互。
  - **企业资源规划 (ERP) 系统**：KDT 通过使非技术利益相关者能够使用业务可读的关键字参与 [test automation](../T/test-automation.md) 来支持财务、人力资源和供应链管理等模块的测试。
  - **内容管理系统 (CMS)**：KDT 通过将复杂的操作抽象为简单的关键字，促进内容发布工作流程和用户权限的测试。
  - **游戏**：为了测试各种游戏场景和用户交互，KDT 允许测试人员编写开发团队可以轻松理解和修改的测试。
  在这些应用中，KDT 弥合了技术和非技术团队成员之间的差距，增强了协作并使[test automation](../T/test-automation.md) 流程更易于访问和维护。

- **电子商务平台**：KDT 允许测试人员在不同的 [test scenarios](../T/test-scenario.md) 之间重复使用关键字，从而简化了用户界面和工作流程的测试，例如搜索、添加到购物车和结账流程。
  - **银行软件**：为了验证复杂的交易流程，KDT 有助于创建可读的[test cases](../T/test-case.md)，可以轻松修改以响应银行法规的频繁变化。
  - **医疗保健系统**：由于需要严格合规性和数据完整性，KDT 有助于自动执行患者登记、预约安排和医疗计费的重复测试。
  - **移动应用程序**：KDT 用于通过定义滑动、点击和捏合等手势的关键字来测试跨平台兼容性和用户交互。
  - **企业资源规划 (ERP) 系统**：KDT 通过使非技术利益相关者能够使用业务可读的关键字参与 [test automation](../T/test-automation.md) 来支持财务、人力资源和供应链管理等模块的测试。
  - **内容管理系统 (CMS)**：KDT 通过将复杂的操作抽象为简单的关键字，促进内容发布工作流程和用户权限的测试。
  - **游戏**：为了测试各种游戏场景和用户交互，KDT 允许测试人员编写开发团队可以轻松理解和修改的测试。

#### 如何将关键字驱动测试集成到持续集成/持续部署 (CI/CD) 管道中？

将 **[Keyword Driven Testing](../K/keyword-driven-testing.md) (KDT)** 集成到 **CI/CD 管道** 涉及设置由管道的各个阶段触发的自动化 [test cases](../T/test-case.md)。这是一个简洁的指南：

1. **准备关键字驱动[Test Suites](../T/test-suite.md)**：确保您的关键字驱动测试是模块化的、可重用的且有详细记录。
  2. **版本控制集成**：将 [test scripts](../T/test-script.md) 和关键字定义与应用程序代码一起存储在版本控制系统 (VCS)（例如 Git）中。
  3. **CI/CD 工具配置**：配置您的 CI/CD 工具（例如 Jenkins、GitLab CI、CircleCI）以包含调用 KDT 框架的测试阶段。
  4. **自动测试触发**：在管道中设置触发器，以便在提交、合并后或按计划的时间间隔自动运行关键字驱动的测试。
  5. **环境[Setup](../S/setup.md)**：确保管道提供或访问可以部署和测试应用程序的[test environment](../T/test-environment.md)。
  6. **[Test Execution](../T/test-execution.md)**：使用命令行界面 (CLI) 或插件来执行关键字驱动的测试。例如：

    ```
    robot --variable BROWSER:Chrome tests/
    ```

7. **结果和报告**：收集测试结果并与报告工具集成以提供有关测试结果的反馈。如果关键测试无法确保立即得到关注，则构建失败。
  8. **反馈循环**：使用测试结果向开发团队通报问题。与 Slack 或电子邮件等通信工具集成以获取通知。
  9. **维护**：定期更新和维护关键字驱动的[test cases](../T/test-case.md)以反映应用程序中的更改。
  通过遵循这些步骤，KDT 成为 CI/CD 流程不可或缺的一部分，从而实现自动化、高效且可靠的测试，支持快速、持续的软件交付。

1. **准备关键字驱动的[Test Suites](../T/test-suite.md)**：确保您的关键字驱动的测试是模块化的、可重用的且有详细记录。
  2. **版本控制集成**：将 [test scripts](../T/test-script.md) 和关键字定义与应用程序代码一起存储在版本控制系统 (VCS)（例如 Git）中。
  3. **CI/CD 工具配置**：配置您的 CI/CD 工具（例如 Jenkins、GitLab CI、CircleCI）以包含调用 KDT 框架的测试阶段。
  4. **自动测试触发**：在管道中设置触发器，以便在提交、合并后或按计划的时间间隔自动运行关键字驱动的测试。
  5. **环境[Setup](../S/setup.md)**：确保管道提供或访问可以部署和测试应用程序的[test environment](../T/test-environment.md)。
  6. **[Test Execution](../T/test-execution.md)**：使用命令行界面 (CLI) 或插件来执行关键字驱动的测试。例如：

    ```
    robot --variable BROWSER:Chrome tests/
    ```

7. **结果和报告**：收集测试结果并与报告工具集成以提供有关测试结果的反馈。如果关键测试无法确保立即得到关注，则构建失败。
  8. **反馈循环**：使用测试结果向开发团队通报问题。与 Slack 或电子邮件等通信工具集成以获取通知。
  9. **维护**：定期更新和维护关键字驱动的[test cases](../T/test-case.md)以反映应用程序中的更改。
