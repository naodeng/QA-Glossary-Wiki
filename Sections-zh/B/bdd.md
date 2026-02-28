# BDD

<!-- TOC START -->
- [相关术语：](#相关术语：)
  - [另请参阅：](#另请参阅：)
- [关于 BDD 有疑问吗？](#关于-bdd-有疑问吗？)
  - [基础知识和重要性](#基础知识和重要性)
    - [什么是行为驱动开发（BDD）？](#什么是行为驱动开发（bdd）？)
    - [为什么 BDD 在软件开发中很重要？](#为什么-bdd-在软件开发中很重要？)
    - [BDD 的关键原则是什么？](#bdd-的关键原则是什么？)
    - [BDD 与传统测试方法有何不同？](#bdd-与传统测试方法有何不同？)
    - [使用 BDD 有什么好处？](#使用-bdd-有什么好处？)
  - [实施和工具](#实施和工具)
    - [BDD 中常用的工具有哪些？](#bdd-中常用的工具有哪些？)
    - [BDD 在软件开发项目中是如何实现的？](#bdd-在软件开发项目中是如何实现的？)
    - [BDD 中“Given-When-Then”格式的作用是什么？](#bdd-中given-when-then格式的作用是什么？)
    - [如何编写一个好的 BDD 场景？](#如何编写一个好的-bdd-场景？)
    - [BDD 框架有哪些示例？](#bdd-框架有哪些示例？)
  - [BDD 和敏捷](#bdd-和敏捷)
    - [BDD 如何融入敏捷开发？](#bdd-如何融入敏捷开发？)
    - [BDD 和敏捷中的用户故事之间有什么关系？](#bdd-和敏捷中的用户故事之间有什么关系？)
    - [BDD 如何改善敏捷团队中的沟通？](#bdd-如何改善敏捷团队中的沟通？)
    - [BDD 如何帮助管理敏捷项目中的变更？](#bdd-如何帮助管理敏捷项目中的变更？)
  - [挑战和最佳实践](#挑战和最佳实践)
    - [实施 BDD 有哪些挑战？](#实施-bdd-有哪些挑战？)
    - [BDD 的最佳实践有哪些？](#bdd-的最佳实践有哪些？)
    - [如何克服这些挑战？](#如何克服这些挑战？)
    - [BDD 如何与其他测试方法集成？](#bdd-如何与其他测试方法集成？)
<!-- TOC END -->

BDD

（行为驱动开发）是一种敏捷软件开发方法，强调开发人员、测试人员和领域专家之间的协作。它侧重于从用户的角度理解和定义系统所需的行为。

BDD

鼓励使用简单、通俗易懂的语言描述软件行为，通常构造为“Given-When-Then”场景。这些描述既作为需求文档，又作为自动化测试的基础，确保软件开发符合用户的需求和期望。

## 相关术语：

- [Behavior Driven Development](../B/behavior-driven-development.md)
- [Gherkin](../G/gherkin.md)
- [Test Scenario](../T/test-scenario.md)

### 另请参阅：

- [Wikipedia](https://en.wikipedia.org/wiki/Behavior-driven_development)

## 关于 BDD 有疑问吗？

### 基础知识和重要性

#### 什么是行为驱动开发（BDD）？

行为驱动开发 ([BDD](../B/bdd.md)) 是一种软件开发方法，通过使用简单的、特定于领域的语言来描述系统行为，增强利益相关者（例如开发人员、测试人员和业务专业人员）之间的协作。 [BDD](../B/bdd.md) 专注于应用程序或系统的预期行为，其规范通常以可读且可理解的格式编写。这种方法鼓励所有相关方在编写任何代码之前就功能和需求达成共识。
  在[BDD](../B/bdd.md) 中，场景是使用 **Given-When-Then** 结构定义的，该结构概述了上下文 (Given)、操作 (When) 和预期结果 (Then)。这些场景既是文档也是自动化测试的基础。 [BDD](../B/bdd.md) 场景通常使用 Cucumber 或 SpecFlow 等工具编写，这些工具允许非技术利益相关者为 [test scenarios](../T/test-scenario.md) 做出贡献。

  ```
  Feature: User login
    Scenario: Successful login with valid credentials
      Given the user is on the login page
      When the user enters valid credentials
      Then the user is redirected to the homepage
  ```[BDD](../B/bdd.md) 通过将用户故事与行为规范联系起来与敏捷方法论集成，确保开发与业务目标紧密结合。它还有助于持续反馈和迭代开发。 [BDD](../B/bdd.md) 强调清晰的沟通，帮助团队尽早消除误解，降低缺陷和返工的风险。通过自动化场景，[BDD](../B/bdd.md) 支持持续集成和交付实践，使团队能够快速验证新功能和回归。

#### 为什么 BDD 在软件开发中很重要？

[BDD](../B/bdd.md) 对于软件开发中**增强利益相关者之间的协作**至关重要。它通过使用**自然语言**来描述系统行为，弥合了开发人员、测试人员和非技术参与者之间的沟通差距。这种共同的理解减少了误解，并确保各方对期望的结果有清晰的愿景。
  此外，[BDD](../B/bdd.md) 鼓励创建**可执行规范**，既充当文档又充当一套自动化测试。这种双重目的确保测试与业务需求保持一致，从而降低功能误解的风险并增加[test cases](../T/test-case.md)**的**相关性。
  通过从用户的角度关注所需的行为，[BDD](../B/bdd.md) 有助于**确定可提供最大业务价值的功能的优先级**。它还支持**持续反馈**，允许在整个开发周期中根据利益相关者的输入进行快速调整。
  在**变更不可避免**的环境中，[BDD](../B/bdd.md) 提供了一种结构化方法来实现**验收标准**，从而更轻松地管理变更并保持对需要开发或修改的内容的清晰了解。
  最后，[BDD](../B/bdd.md) 对 **自动化** 和 **[regression testing](../R/regression-testing.md)** 的强调确保新的更改不会破坏现有功能，从而产生更强大和可靠的软件。这种做法对于在快节奏的开发环境中保持高质量标准至关重要。
  总之，[BDD](../B/bdd.md) 很重要，因为它可以促进更好的沟通，形成对需求的共同理解，确保开发符合业务需求，并通过[automated testing](../A/automated-testing.md) 保持高质量。

#### BDD 的关键原则是什么？

[BDD](../B/bdd.md) 的主要原则是：

- **通用语言**：使用所有利益相关者（包括业务分析师、开发人员和测试人员）都能理解的通用语言来定义行为和预期结果。
  - **协作**：鼓励跨职能团队成员之间的协作，以获得对要开发的功能的共同理解，并确保软件满足业务需求。
  - **实时文档**：将 [BDD](../B/bdd.md) 场景视为随软件一起发展的实时文档。它们应该保持最新并反映当前对系统行为的理解。
  - **由外而内的开发**：从用户体验出发，逆向实现底层功能，确保软件是从用户需求的角度构建的。
  - **[Test Automation](../T/test-automation.md)**：自动化[BDD](../B/bdd.md) 场景作为验收测试，提供有关系统行为的快速反馈并充当变更的安全网。
  - **关注业务价值**：根据业务价值确定功能和场景的优先级，以确保首先交付系统最重要的方面。
  - **持续改进**：使用[BDD](../B/bdd.md)不断完善和提高对系统和系统本身的理解，营造持续学习和适应的环境。
  通过遵守这些原则，[BDD](../B/bdd.md) 帮助团队构建与业务目标和用户期望紧密结合的软件，同时通过[automated testing](../A/automated-testing.md) 和清晰的沟通保持高水平的质量。

- **通用语言**：使用所有利益相关者（包括业务分析师、开发人员和测试人员）都能理解的通用语言来定义行为和预期结果。
  - **协作**：鼓励跨职能团队成员之间的协作，以获得对要开发的功能的共同理解，并确保软件满足业务需求。
  - **实时文档**：将 [BDD](../B/bdd.md) 场景视为随软件一起发展的实时文档。它们应该保持最新并反映当前对系统行为的理解。
  - **由外而内的开发**：从用户体验出发，逆向实现底层功能，确保软件是从用户需求的角度构建的。
  - **[Test Automation](../T/test-automation.md)**：自动化[BDD](../B/bdd.md) 场景作为验收测试，提供有关系统行为的快速反馈并充当变更的安全网。
  - **关注业务价值**：根据业务价值确定功能和场景的优先级，以确保首先交付系统最重要的方面。
  - **持续改进**：使用[BDD](../B/bdd.md)不断完善和提高对系统和系统本身的理解，营造持续学习和适应的环境。

#### BDD 与传统测试方法有何不同？

[BDD](../B/bdd.md) 与传统测试方法的不同之处在于，它关注**最终用户的体验**和**行为**，而不是从纯粹的技术角度测试系统。传统方法通常涉及在代码开发后编写测试，主要基于技术规范。相比之下，[BDD](../B/bdd.md) 从**协作讨论**开始，在编写任何代码之前定义**预期行为**，使用所有利益相关者都可以访问的语言。
  [BDD](../B/bdd.md) 中的测试以 **自然语言风格** 编写，使用 **Given-When-Then** 格式，这使得非技术团队成员可以理解它们。这与传统的[test cases](../T/test-case.md)形成鲜明对比，传统的[test cases](../T/test-case.md)通常是用编程语言或测试框架语法编写的，业务利益相关者不太容易访问。
  [BDD](../B/bdd.md) 鼓励开发人员、测试人员和业务分析师之间**基于示例的持续沟通**。这种协作方法确保各方对要开发的功能有共同的理解，这在传统测试中不太常见，因为传统测试的重点可能更多地放在验证实施后的技术方面。
  此外，[BDD](../B/bdd.md) 测试充当随着应用程序一起发展的**活文档**。传统的测试方法可能会生成单独的测试文档，随着代码库的更改，这些文档可能会很快过时。
  最后，[BDD](../B/bdd.md) 与**敏捷实践**无缝集成，增强**迭代开发**和**反馈循环**，而传统测试方法可能并不与敏捷方法论本质上一致，有时可以遵循更**瀑布方法**。

#### 使用 BDD 有什么好处？

使用[BDD](../B/bdd.md) 的好处包括：

- **增强协作**：[BDD](../B/bdd.md) 鼓励开发人员、测试人员和非技术利益相关者之间的协作。这种共同的理解减少了沟通不畅，并确保软件满足业务需求。
  - **明确的要求**：在[BDD](../B/bdd.md)场景中使用自然语言可确保所有相关方的要求清晰且易于理解。
  - **实时文档**：[BDD](../B/bdd.md) 场景同时也是始终最新的文档，因为它们随着所描述的功能而发展。
  - **关注用户体验**：[BDD](../B/bdd.md) 对用户行为的重视有助于团队专注于为最终用户提供价值，而不仅仅是满足技术要求。
  - **早期缺陷发现**：通过在开发开始之前定义预期行为，团队可以在开发周期的早期识别问题。
  - **简化的 QA 流程**：自动化 [BDD](../B/bdd.md) 测试可以作为持续集成管道的一部分执行，从而提供有关应用程序运行状况的快速反馈。
  - **减少返工**：由于 [BDD](../B/bdd.md) 场景是预先定义并得到所有利益相关者同意的，因此由于误解需求而返工的可能性较小。
  - **促进[test automation](../T/test-automation.md)**：[BDD](../B/bdd.md) 框架使编写与业务目标一致的自动化测试变得更加容易。
  - **[Regression testing](../R/regression-testing.md)**：[BDD](../B/bdd.md) 场景可重复用于[regression testing](../R/regression-testing.md)，以确保新更改不会破坏现有功能。
  - **支持持续交付**：自动化[BDD](../B/bdd.md)测试可以成为部署管道的一部分，确保只有经过充分测试的功能才能交付到生产中。
  - **增强协作**：[BDD](../B/bdd.md) 鼓励开发人员、测试人员和非技术利益相关者之间的协作。这种共同的理解减少了沟通不畅，并确保软件满足业务需求。
  - **明确的要求**：在[BDD](../B/bdd.md)场景中使用自然语言可确保所有相关方的要求清晰且易于理解。
  - **实时文档**：[BDD](../B/bdd.md) 场景同时也是始终最新的文档，因为它们随着所描述的功能而发展。
  - **关注用户体验**：[BDD](../B/bdd.md) 对用户行为的重视有助于团队专注于为最终用户提供价值，而不仅仅是满足技术要求。
  - **早期缺陷发现**：通过在开发开始之前定义预期行为，团队可以在开发周期的早期识别问题。
  - **简化的 QA 流程**：自动化 [BDD](../B/bdd.md) 测试可以作为持续集成管道的一部分执行，从而提供有关应用程序运行状况的快速反馈。
  - **减少返工**：由于 [BDD](../B/bdd.md) 场景是预先定义并得到所有利益相关者同意的，因此由于误解需求而返工的可能性较小。
  - **促进[test automation](../T/test-automation.md)**：[BDD](../B/bdd.md) 框架使编写与业务目标一致的自动化测试变得更加容易。
  - **[Regression testing](../R/regression-testing.md)**：[BDD](../B/bdd.md) 场景可重复用于[regression testing](../R/regression-testing.md)，以确保新更改不会破坏现有功能。
  - **支持持续交付**：自动化[BDD](../B/bdd.md)测试可以成为部署管道的一部分，确保只有经过充分测试的功能才能交付到生产中。

### 实施和工具

#### BDD 中常用的工具有哪些？

常见的 [BDD](../B/bdd.md) 工具包括：

- **Cucumber** ：支持多种语言，使用 Gherkin 编写测试。
  - **SpecFlow** ：对于 .NET 项目，与 Visual Studio 集成。
  - **Behave** ：对于 Python，使用 Gherkin。
  - **JBehave** ：对于 Java 应用程序，使用 Gherkin。
  - **Serenity [BDD](../B/bdd.md)** ：增强报告，与 JBehave 和 Cucumber 集成。
  - **Lettuce** ：Python 工具，类似于 Cucumber。
  - **Calabash**：对于移动应用程序，支持 iOS 和 Android。
  - **Concordian** ：对于基于 Markdown 的规范，支持多种语言。
  这些工具通常与其他测试框架（如 JUnit、[NUnit](../N/nunit.md) 或 PyTest）集成，并且可以与 [Selenium](../S/selenium.md) 一起用于 [web automation](../W/web-automation.md) 或用于移动自动化的 Appium。它们促进了“Given When-Then”方法，并通过可执行规范支持实时文档。

- **Cucumber** ：支持多种语言，使用 Gherkin 编写测试。
  - **SpecFlow** ：对于 .NET 项目，与 Visual Studio 集成。
  - **Behave** ：对于 Python，使用 Gherkin。
  - **JBehave** ：对于 Java 应用程序，使用 Gherkin。
  - **Serenity [BDD](../B/bdd.md)** ：增强报告，与 JBehave 和 Cucumber 集成。
  - **Lettuce** ：Python 工具，类似于 Cucumber。
  - **Calabash**：对于移动应用程序，支持 iOS 和 Android。
  - **Concordian** ：对于基于 Markdown 的规范，支持多种语言。

#### BDD 在软件开发项目中是如何实现的？

在软件开发项目中实现 [BDD](../B/bdd.md) 涉及几个步骤：

1. **协作**：让利益相关者、开发人员和测试人员参与定义行为。利用研讨会或会议来讨论功能及其预期成果。
  2. **定义场景**：以**Given-When-Then** 格式编写场景。场景应该简洁，涵盖单一行为或结果。
  3. **自动化**：将场景转化为自动化测试。使用 [BDD](../B/bdd.md) 框架（例如 Cucumber、SpecFlow 或 Behave）将场景中的步骤绑定到测试代码。

  ```
  Feature: User login
  Scenario: Successful login with valid credentials
    Given the login page is displayed
    When the user enters valid credentials
    Then the user is redirected to the dashboard
  ```

1. **测试开发**：在实现功能之前开发测试。这确保测试驱动开发过程（[Test-Driven Development](../T/test-driven-development.md) - TDD）。
  2. **实现功能**：编写代码以使测试通过。代码应满足场景中描述的行为。
  3. **重构**：测试通过后，重构代码以提高质量和[maintainability](../M/maintainability.md)而不改变行为。
  4. **持续集成**：集成并运行 [BDD](../B/bdd.md) 测试作为 CI 管道的一部分，以尽早捕获回归。
  5. **反馈循环**：使用测试结果告知团队该功能的状态。通过表明已完成的行为，而失败则突出显示有待完成的工作。
  6. **文档**：将场景和测试结果视为系统行为的活文档。
  7. **迭代**：对新功能和更改重复该过程，保持与业务需求的一致性。
  请记住，[BDD](../B/bdd.md) 是迭代的。定期审查和完善场景，以确保它们保持相关性和价值。

1. **协作**：让利益相关者、开发人员和测试人员参与定义行为。利用研讨会或会议来讨论功能及其预期成果。
  2. **定义场景**：以**Given-When-Then** 格式编写场景。场景应该简洁，涵盖单一行为或结果。
  3. **自动化**：将场景转化为自动化测试。使用 [BDD](../B/bdd.md) 框架（例如 Cucumber、SpecFlow 或 Behave）将场景中的步骤绑定到测试代码。
  1. **测试开发**：在实现功能之前开发测试。这确保测试驱动开发过程（[Test-Driven Development](../T/test-driven-development.md) - TDD）。
  2. **实现功能**：编写代码以使测试通过。代码应满足场景中描述的行为。
  3. **重构**：测试通过后，重构代码以提高质量和[maintainability](../M/maintainability.md)而不改变行为。
  4. **持续集成**：集成并运行 [BDD](../B/bdd.md) 测试作为 CI 管道的一部分，以尽早捕获回归。
  5. **反馈循环**：使用测试结果告知团队该功能的状态。通过表明已完成的行为，而失败则突出显示有待完成的工作。
  6. **文档**：将场景和测试结果视为系统行为的活文档。
  7. **迭代**：对新功能和更改重复该过程，保持与业务需求的一致性。

#### BDD 中“Given-When-Then”格式的作用是什么？

**Given-When-Then** 格式是一种结构化的方式来编写功能的验收标准，确保利益相关者之间的清晰度和共同理解。在[BDD](../B/bdd.md) 中，此格式用于创建指导开发和测试过程的可执行规范。

- **鉴于**
    设置初始上下文或先决条件。

- **当**
    描述触发行为的动作或事件。

- **然后**
    概述预期的结果或成果。
  这种格式鼓励关注用户行为和结果，而不是技术实现细节。它有助于定义符合业务需求和用户期望的清晰简洁的[test cases](../T/test-case.md)。通过使用这种格式，[test automation](../T/test-automation.md) 工程师可以编写易于理解和维护的测试，并直接反映系统所需的行为。
  这是 [BDD](../B/bdd.md) 框架（如 Cucumber）中的示例：

  ```
  Feature: User login
    Scenario: Successful login with valid credentials
      Given the user is on the login page
      When the user enters valid credentials
      Then the user is redirected to the dashboard
  ```这种场景可以直接转化为自动化测试，确保软件按预期运行。 **Given-When-Then** 格式还促进技术和非技术团队成员之间的沟通，弥合业务需求和技术实施之间的差距。

- **鉴于**
    设置初始上下文或先决条件。

- **当**
    描述触发行为的动作或事件。

- **然后**
    概述预期的结果或成果。

#### 如何编写一个好的 BDD 场景？

编写一个好的[BDD](../B/bdd.md) 场景需要从用户的角度对软件行为进行清晰、简洁且易于理解的描述。以下是创建有效[BDD](../B/bdd.md) 场景的指南：

- **关注用户的需求**：每个场景都应解决特定的用户操作和预期结果。
  - **使用“Given-When-Then”格式**：此结构有助于保持清晰度和一致性。

    ```
    Given [initial context],
    When [event occurs],
    Then [ensure some outcomes].
    ```

- **具有声明性**：描述意图而不是实现细节。避免使用技术术语。
  - **保持简单**：每个场景都应该测试一种行为。复杂的场景可以分解为多个更简单的场景。
  - **使用实际示例**：提供代表实际[use cases](../U/use-case.md) 的数据。
  - **避免 UI 细节**：关注行为而不是按钮或字段等 UI 元素。
  - **使其可重用和可维护**：场景应该以可以在不同测试中重用的方式编写。
  - **与利益相关者合作**：确保技术和非技术团队成员都对场景进行审查，以确保其清晰度和准确性。
  - **定期审查和完善**：随着对系统的理解不断发展，更新场景以反映用户行为或需求的变化。
  - **谨慎自动化**：自动化场景时，确保测试代码与场景本身一样可读。
  通过遵守这些准则，您将创建 [BDD](../B/bdd.md) 场景，这些场景可以作为有价值的开发指南、自动化测试的基础以及团队成员之间清晰的沟通形式。

- **关注用户的需求**：每个场景都应解决特定的用户操作和预期结果。
  - **使用“Given-When-Then”格式**：此结构有助于保持清晰度和一致性。

    ```
    Given [initial context],
    When [event occurs],
    Then [ensure some outcomes].
    ```

- **具有声明性**：描述意图而不是实现细节。避免使用技术术语。
  - **保持简单**：每个场景都应该测试一种行为。复杂的场景可以分解为多个更简单的场景。
  - **使用实际示例**：提供代表实际[use cases](../U/use-case.md) 的数据。
  - **避免 UI 细节**：关注行为而不是按钮或字段等 UI 元素。
  - **使其可重用和可维护**：场景应该以可以在不同测试中重用的方式编写。
  - **与利益相关者合作**：确保技术和非技术团队成员都对场景进行审查，以确保其清晰度和准确性。
  - **定期审查和完善**：随着对系统的理解不断发展，更新场景以反映用户行为或需求的变化。
  - **谨慎自动化**：自动化场景时，确保测试代码与场景本身一样可读。

#### BDD 框架有哪些示例？

[BDD](../B/bdd.md) 框架允许以所有利益相关者都能理解的简单语言定义应用程序行为，从而促进行为驱动开发的实施。以下是一些示例：

- **Cucumber**：支持多种语言，如 Java、Ruby 和 JavaScript。它使用 [Gherkin](../G/gherkin.md) 语法来编写测试并与各种测试工具集成。

    ```
    Feature: User login
      Scenario: Valid user login
        Given the user is on the login page
        When the user enters valid credentials
        Then the user is redirected to the homepage
    ```

- **SpecFlow**：主要用于.NET 项目，它还使用[Gherkin](../G/gherkin.md) 并与[NUnit](../N/nunit.md)、MSTest 和xUnit 集成。

    ```
    Feature: User profile
      Scenario: Update user profile
        Given the user is logged in
        When the user updates their profile
        Then the profile changes should be saved
    ```

- **Behave**：使用 [Gherkin](../G/gherkin.md) 语言编写测试的 Python [BDD](../B/bdd.md) 框架。

    ```
    Feature: API response
      Scenario: Receive valid data from API
        Given the API is up and running
        When the client requests data
        Then the response should be successful and correct
    ```

- **JBehave**：基于 Java 的 [BDD](../B/bdd.md) 框架，鼓励使用 JUnit 并与 Maven 和 Ant 集成。

    ```
    @Given("a stock of symbol $symbol and a threshold of $threshold")
    @When("$symbol is traded at $price")
    @Then("the alert status should be $status")
    ```

- **Serenity [BDD](../B/bdd.md)**：通过提供集成报告和需求覆盖来增强 Cucumber 和 JBehave。

    ```
    Feature: Order basket
      Scenario: Adding items to the basket
        Given the user has an empty basket
        When the user adds a product to the basket
        Then the basket should contain the added product
    ```这些框架支持开发人员、测试人员和业务利益相关者之间的协作，确保每个人都清楚地了解软件的行为。

- **Cucumber**：支持多种语言，如 Java、Ruby 和 JavaScript。它使用 [Gherkin](../G/gherkin.md) 语法来编写测试并与各种测试工具集成。

    ```
    Feature: User login
      Scenario: Valid user login
        Given the user is on the login page
        When the user enters valid credentials
        Then the user is redirected to the homepage
    ```

- **SpecFlow**：主要用于.NET 项目，它还使用[Gherkin](../G/gherkin.md) 并与[NUnit](../N/nunit.md)、MSTest 和xUnit 集成。

    ```
    Feature: User profile
      Scenario: Update user profile
        Given the user is logged in
        When the user updates their profile
        Then the profile changes should be saved
    ```

- **Behave**：使用 [Gherkin](../G/gherkin.md) 语言编写测试的 Python [BDD](../B/bdd.md) 框架。

    ```
    Feature: API response
      Scenario: Receive valid data from API
        Given the API is up and running
        When the client requests data
        Then the response should be successful and correct
    ```

- **JBehave**：基于 Java 的 [BDD](../B/bdd.md) 框架，鼓励使用 JUnit 并与 Maven 和 Ant 集成。

    ```
    @Given("a stock of symbol $symbol and a threshold of $threshold")
    @When("$symbol is traded at $price")
    @Then("the alert status should be $status")
    ```

- **Serenity [BDD](../B/bdd.md)**：通过提供集成报告和需求覆盖来增强 Cucumber 和 JBehave。

    ```
    Feature: Order basket
      Scenario: Adding items to the basket
        Given the user has an empty basket
        When the user adds a product to the basket
        Then the basket should contain the added product
    ```

### BDD 和敏捷

#### BDD 如何融入敏捷开发？

[BDD](../B/bdd.md) 通过使开发活动与业务目标保持一致并促进开发人员、测试人员和非技术利益相关者之间的协作来适应[Agile development](../A/agile-development.md)。它鼓励团队通过在开发开始之前定义的**用户故事**和**验收标准**来关注用户的需求。这种预先的明确性有助于防止范围蔓延，并确保团队始终致力于最有价值的功能。
  在敏捷中，[BDD](../B/bdd.md) 场景通常源自待办事项细化或冲刺计划会议期间的用户故事。这些场景指导开发，提供软件应如何运行的清晰示例，可以直接转化为自动化测试。因此，[BDD](../B/bdd.md) 通过提供随项目发展的**动态文档**来补充敏捷实践。
  [BDD](../B/bdd.md) 场景的 **Given-When-Then** 格式可确保所有团队成员都能理解测试，从而增强 **沟通**​​ 和 **协作**。这种共同的理解在敏捷中至关重要，其中快速反馈和迭代开发是关键。
  [BDD](../B/bdd.md) 还通过提供一套可以自动运行的回归测试来支持敏捷的**持续集成**和**持续交付** (CI/CD)，确保新的更改不会破坏现有功能。
  通过将[BDD](../B/bdd.md)集成到敏捷中，团队可以确保他们不仅快速交付软件，而且有效满足业务需求，从而提高所生产软件的**质量**和**价值**。

#### BDD 和敏捷中的用户故事之间有什么关系？

在敏捷中，**用户故事**以简单的对话语言阐明客户需求，重点关注功能将为用户提供的价值。 **[BDD](../B/bdd.md)** 通过提供一种基于用户故事中描述的行为创建[test cases](../T/test-case.md) 的结构化方法来扩展此概念。 [BDD](../B/bdd.md) 和用户故事之间的关系是共生的； [BDD](../B/bdd.md) 场景直接源自用户故事，并以 **Given-When-Then** 格式表示，这反映了用户故事的叙述。
  这种关系确保：

- 发展是
    **以用户需求为导向**
    以及预期的系统行为。

- 测试场景是
    **明确传达**
    和
    **所有利益相关者都理解**
    ，包括非技术成员。

- 有一个
    **直接追溯**
    需求（用户故事）和自动化测试之间的关系，这有助于与应用程序一起维护和发展测试套件。
  [BDD](../B/bdd.md) 场景有效地成为用户故事的**详细规范**，它既可执行又可用作文档。这种紧密的集成通过促进协作、实现快速反馈循环并确保软件逐步发展并重点关注首先提供最有价值的功能来支持敏捷原则。

- 发展是
    **以用户需求为导向**
    以及预期的系统行为。

- 测试场景是
    **明确传达**
    和
    **所有利益相关者都理解**
    ，包括非技术成员。

- 有一个
    **直接追溯**
    需求（用户故事）和自动化测试之间的关系，这有助于与应用程序一起维护和发展测试套件。

#### BDD 如何改善敏捷团队中的沟通？

[BDD](../B/bdd.md) 通过**通用语言**促进对功能和需求的**共同理解**，从而增强敏捷团队中的沟通。 **Given-When-Then** 格式将技术规范转化为**人类可读的叙述**，允许开发人员、测试人员和非技术利益相关者有效协作。这种**协作**对于敏捷的迭代开发至关重要，因为需求可以快速发展。
  通过使用**[BDD](../B/bdd.md) 的特定领域语言**讨论场景，团队可以在开发开始之前澄清期望并减少歧义。这**防止误解**并确保所有团队成员对产品的行为有**一致的愿景**。 [BDD](../B/bdd.md) 场景还充当**实时文档**和**自动化测试**，提供从需求到实施和测试的清晰跟踪。
  此外，[BDD](../B/bdd.md) 鼓励**早期反馈**循环，因为利益相关者可以在编码之前审查和验证场景。这种**参与**有助于及早发现问题，降低变更成本并提高最终产品的质量。
  总之，[BDD](../B/bdd.md) 弥合了技术和非技术团队成员之间的沟通差距，使每个人都朝着**统一的目标**前进，并营造了一个**协作环境**，这对于[Agile development](../A/agile-development.md) 的成功至关重要。

#### BDD 如何帮助管理敏捷项目中的变更？

[BDD](../B/bdd.md) 通过确保规范和测试**以每个人都能理解的语言编写**来促进**敏捷变更管理**。这种通用语言有助于在发生变化时**团队保持一致**。当新需求出现或现有需求发生变化时，[BDD](../B/bdd.md) 场景可以快速**更新**以反映变化，同时充当文档和[test cases](../T/test-case.md)。
  **Given-When-Then** 格式对于管理变更特别有用，因为它清楚地概述了背景、行动和预期结果。这种清晰度使得更容易识别软件的哪些部分受到更改的影响。可以用最少的努力**重构**场景，确保自动化测试与需求保持同步。
  此外，[BDD](../B/bdd.md) 鼓励开发人员、测试人员和业务利益相关者之间的**持续协作**。这种持续的对话有助于尽早发现误解，并使团队能够更流畅地适应变化。当引入变更时，利益相关者可以看到对场景的直接影响，并就其影响进行有意义的讨论。
  通过将 [BDD](../B/bdd.md) 与 **版本控制系统** 集成，团队可以跟踪场景随时间的变化，提供有关软件如何以及为何发展的清晰历史记录。这使得管理和理解变更的影响变得更加容易，促进更平稳的过渡并降低回归风险。
  总之，[BDD](../B/bdd.md) 通过提供对可快速调整的需求的**清晰、共享的理解**、促进团队成员之间的**协作**以及提供在项目生命周期中**跟踪变更**的方法来支持敏捷变更管理。

### 挑战和最佳实践

#### 实施 BDD 有哪些挑战？

实施 [BDD](../B/bdd.md) 会带来一些挑战：

- **协作障碍**：有效的[BDD](../B/bdd.md) 需要开发人员、测试人员和非技术利益相关者之间的密切协作。实现这种级别的合作可能很困难，特别是在具有孤立部门或业务方不参与开发过程的组织中。
  - **编写有效的场景**：以 *Given-When-Then* 格式制作清晰、简洁且有价值的场景需要对领域有很好的理解，并且能够将需求抽象为行为描述。对于新接触 [BDD](../B/bdd.md) 的团队来说，这可能具有挑战性。
  - **维护动态文档**：随着项目的发展，保持 [BDD](../B/bdd.md) 文档最新可能会很麻烦。它需要纪律和持续关注，以确保场景始终反映应用程序的当前状态。
  - **工具集成**：将 [BDD](../B/bdd.md) 框架与现有工具和流程集成可能很复杂。确保 [BDD](../B/bdd.md) 工具与其他测试或 CI/CD 工具之间的兼容性和流畅的工作流程需要努力和专业知识。
  - **学习曲线**：[BDD](../B/bdd.md) 的新团队必须投入时间不仅要学习工具，还要学习 [BDD](../B/bdd.md) 背后的理念。这可能会减慢最初的开发工作，并可能会遇到习惯于传统测试方法的团队成员的阻力。
  - **开销**：编写和维护 [BDD](../B/bdd.md) 测试会增加开发过程的开销。团队必须确保 [BDD](../B/bdd.md) 的好处超过实施它所花费的时间和资源。
  - **非[functional requirements](../F/functional-requirements.md)**：[BDD](../B/bdd.md) 主要关注行为，有时会忽略非[functional requirements](../F/functional-requirements.md) 之类的性能和安全性，这对于软件项目的成功也至关重要。
  - **协作障碍**：有效的[BDD](../B/bdd.md) 需要开发人员、测试人员和非技术利益相关者之间的密切协作。实现这种级别的合作可能很困难，特别是在具有孤立部门或业务方不参与开发过程的组织中。
  - **编写有效的场景**：以 *Given-When-Then* 格式制作清晰、简洁且有价值的场景需要对领域有很好的理解，并且能够将需求抽象为行为描述。对于[BDD](../B/bdd.md) 的新团队来说，这可能具有挑战性。
  - **维护动态文档**：随着项目的发展，保持 [BDD](../B/bdd.md) 文档最新可能会很麻烦。它需要纪律和持续关注，以确保场景始终反映应用程序的当前状态。
  - **工具集成**：将 [BDD](../B/bdd.md) 框架与现有工具和流程集成可能很复杂。确保 [BDD](../B/bdd.md) 工具与其他测试或 CI/CD 工具之间的兼容性和流畅的工作流程需要努力和专业知识。
  - **学习曲线**：[BDD](../B/bdd.md) 的新团队必须投入时间不仅要学习工具，还要学习 [BDD](../B/bdd.md) 背后的理念。这可能会减慢最初的开发工作，并可能会遇到习惯于传统测试方法的团队成员的阻力。
  - **开销**：编写和维护 [BDD](../B/bdd.md) 测试会增加开发过程的开销。团队必须确保 [BDD](../B/bdd.md) 的好处超过实施它所花费的时间和资源。
  - **非[functional requirements](../F/functional-requirements.md)**：[BDD](../B/bdd.md) 主要关注行为，有时会忽略非[functional requirements](../F/functional-requirements.md) 之类的性能和安全性，这对于软件项目的成功也至关重要。

#### BDD 的最佳实践有哪些？

[BDD](../B/bdd.md) 的最佳实践包括：

- **协作**
    与所有利益相关者（包括开发人员、测试人员和业务分析师）合作，以确保对所需行为有共同的理解。

- **定义清晰简洁的场景**
    使用“Given-When-Then”格式，避免歧义和复杂性。

- **在实施之前写下场景**
    指导开发并确保软件实现预期行为。

- **自动化场景**
    作为持续集成过程的一部分，以验证软件在每次更改后是否按预期运行。

- 使用
    **特定领域语言**
    （DSL）以所有利益相关者都可以理解的方式表达场景。

- **保持场景可维护**
    通过避免重复并使他们专注于行为而不是实现细节。

- **定期重构**
    改善代码和场景的结构和清晰度。

- **优先考虑场景**
    基于业务价值和风险，首先关注最关键的方面。

- **审查和更新场景**
    反映需求的变化并确保它们保持相关性和准确性。

- **将 [BDD](../B/bdd.md) 与版本控制集成**
    跟踪变化并在整个团队中有效协作。

- **使用标签或注释**
    组织场景并运行与特定功能或问题相关的选择性测试。

- **监控测试结果**
    并及时采取行动以保持测试套件的可靠性。
  通过坚持这些实践，团队可以最大限度地发挥 [BDD](../B/bdd.md) 的优势，并保持高质量的协作开发流程。

- **协作**
    与所有利益相关者（包括开发人员、测试人员和业务分析师）合作，以确保对所需行为有共同的理解。

- **定义清晰简洁的场景**
    使用“Given-When-Then”格式，避免歧义和复杂性。

- **在实施之前写下场景**
    指导开发并确保软件实现预期行为。

- **自动化场景**
    作为持续集成过程的一部分，以验证软件在每次更改后是否按预期运行。

- 使用
    **特定领域语言**
    （DSL）以所有利益相关者都可以理解的方式表达场景。

- **保持场景可维护**
    通过避免重复并使他们专注于行为而不是实现细节。

- **定期重构**
    改善代码和场景的结构和清晰度。

- **优先考虑场景**
    基于业务价值和风险，首先关注最关键的方面。

- **审查和更新场景**
    反映需求的变化并确保它们保持相关性和准确性。

- **将 [BDD](../B/bdd.md) 与版本控制集成**
    跟踪变化并在整个团队中有效协作。

- **使用标签或注释**
    组织场景并运行与特定功能或问题相关的选择性测试。

- **监控测试结果**
    并及时采取行动以保持测试套件的可靠性。

#### 如何克服这些挑战？

克服 [BDD](../B/bdd.md) 实施中的挑战需要采取战略方法：

- **协作**：通过让所有利益相关者（包括开发人员、测试人员和业务分析师）参与[BDD](../B/bdd.md) 活动，培养协作文化。定期会议和研讨会可以帮助保持一致性。
  - **培训和知识共享**：投资于团队成员的全面培训，以确保他们了解[BDD](../B/bdd.md)原则和实践。鼓励召开知识共享会议，在整个团队中传播专业知识。
  - **工具掌握**：选择符合您团队技能和项目要求的 [BDD](../B/bdd.md) 工具。确保团队通过培训和实践熟练使用这些工具。
  - **实践的完善**：根据反馈和回顾不断完善[BDD](../B/bdd.md)实践。调整您的方法以适应项目和团队不断变化的需求。
  - **与现有流程集成**：将 [BDD](../B/bdd.md) 与现有开发和测试工作流程无缝集成。使用自动化来简化 CI/CD 管道中的 [BDD](../B/bdd.md) 流程。
  - **管理层支持**：通过展示 [BDD](../B/bdd.md) 在改善沟通和减少误解方面的价值，确保管理层的支持。突出显示展示[BDD](../B/bdd.md) 优势的成功案例和指标。
  - **渐进采用**：从小规模的试点项目开始，以证明 [BDD](../B/bdd.md) 的有效性。随着团队信心的增强，逐渐将其使用扩展到其他项目。
  - **应对技术挑战**：通过实施确保一致性和可靠性的稳健解决方案和实践，应对技术挑战，例如[test data](../T/test-data.md) 管理和环境[setup](../S/setup.md)。
  通过解决这些领域，团队可以有效地克服与 [BDD](../B/bdd.md) 相关的挑战，并充分利用其潜力来增强软件开发项目的协作、清晰度和质量。

- **协作**：通过让所有利益相关者（包括开发人员、测试人员和业务分析师）参与[BDD](../B/bdd.md) 活动，培养协作文化。定期会议和研讨会可以帮助保持一致性。
  - **培训和知识共享**：投资于团队成员的全面培训，以确保他们了解[BDD](../B/bdd.md)原则和实践。鼓励召开知识共享会议，在整个团队中传播专业知识。
  - **工具掌握**：选择符合您团队技能和项目要求的[BDD](../B/bdd.md) 工具。确保团队通过培训和实践熟练使用这些工具。
  - **实践的完善**：根据反馈和回顾不断完善[BDD](../B/bdd.md)实践。调整您的方法以适应项目和团队不断变化的需求。
  - **与现有流程集成**：将 [BDD](../B/bdd.md) 与现有开发和测试工作流程无缝集成。使用自动化来简化 CI/CD 管道中的 [BDD](../B/bdd.md) 流程。
  - **管理层支持**：通过展示[BDD](../B/bdd.md) 在改善沟通和减少误解方面的价值，确保管理层的支持。突出显示展示[BDD](../B/bdd.md) 优势的成功案例和指标。
  - **渐进采用**：从小规模的试点项目开始，以证明 [BDD](../B/bdd.md) 的有效性。随着团队信心的增强，逐渐将其使用扩展到其他项目。
  - **应对技术挑战**：通过实施确保一致性和可靠性的稳健解决方案和实践，应对技术挑战，例如[test data](../T/test-data.md) 管理和环境[setup](../S/setup.md)。

#### BDD 如何与其他测试方法集成？

将[BDD](../B/bdd.md) 与其他测试方法集成可以增强覆盖范围并确保解决不同的测试级别和观点。 **[Unit Testing](../U/unit-testing.md)** 可以通过 [BDD](../B/bdd.md) 场景进行补充，以确保各个组件满足行为预期。 **[Integration Testing](../I/integration-testing.md)** 可以与[BDD](../B/bdd.md) 保持一致，以验证组件之间的交互是否遵循定义的行为。
  对于 **[Test-Driven Development](../T/test-driven-development.md) (TDD)**，[BDD](../B/bdd.md) 场景可以用作起点。 TDD 侧重于实现细节，而 [BDD](../B/bdd.md) 提供了更高级别的视图。这种组合确保行为和实现都是正确的。
  **[Acceptance Testing](../A/acceptance-testing.md)** 自然地与[BDD](../B/bdd.md) 保持一致，因为[BDD](../B/bdd.md) 场景是以指定功能的接受标准的方式编写的。 [BDD](../B/bdd.md) 可用于自动化验收测试，确保软件满足业务需求。
  在**[Performance Testing](../P/performance-testing.md)**、[BDD](../B/bdd.md) 场景中可以指定与性能相关的行为，例如负载下的响应时间。这有助于创建与用户体验相关的性能测试。
  **[Exploratory Testing](../E/exploratory-testing.md)** 通过提供对预期行为的清晰理解，从[BDD](../B/bdd.md) 中受益，这可以指导测试人员进行探索。
  要将 [BDD](../B/bdd.md) 与这些方法集成，团队可以：

- 使用 BDD 场景作为其他测试用例的基础。
  - 确保 BDD 工具和框架与其他测试工具兼容。
  - 跨团队共享 BDD 场景以促进理解和协作。
  通过将[BDD](../B/bdd.md) 与其他测试方法集成，团队可以创建涵盖[software quality](../S/software-quality.md) 多个方面的全面测试策略。

- 使用 BDD 场景作为其他测试用例的基础。
  - 确保 BDD 工具和框架与其他测试工具兼容。
  - 跨团队共享 BDD 场景以促进理解和协作。
