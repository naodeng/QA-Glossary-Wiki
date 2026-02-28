# 敏捷测试

<!-- TOC START -->
- [相关术语：](#相关术语：)
  - [另请参阅：](#另请参阅：)
- [关于敏捷测试的问题？](#关于敏捷测试的问题？)
  - [基础知识和重要性](#基础知识和重要性)
    - [什么是敏捷测试？](#什么是敏捷测试？)
    - [敏捷测试在软件开发中的重要性是什么？](#敏捷测试在软件开发中的重要性是什么？)
    - [敏捷测试与传统测试方法有何不同？](#敏捷测试与传统测试方法有何不同？)
    - [敏捷测试的关键原则是什么？](#敏捷测试的关键原则是什么？)
  - [流程和技术](#流程和技术)
    - [敏捷测试有哪些不同阶段？](#敏捷测试有哪些不同阶段？)
    - [常见的敏捷测试方法有哪些？](#常见的敏捷测试方法有哪些？)
    - [敏捷测试中使用的关键技术是什么？](#敏捷测试中使用的关键技术是什么？)
    - [测试如何集成到敏捷开发过程中？](#测试如何集成到敏捷开发过程中？)
  - [角色和职责](#角色和职责)
    - [测试人员在敏捷团队中的角色是什么？](#测试人员在敏捷团队中的角色是什么？)
    - [敏捷中测试人员的职责与传统测试角色有何不同？](#敏捷中测试人员的职责与传统测试角色有何不同？)
    - [哪些技能对于敏捷测试人员来说很重要？](#哪些技能对于敏捷测试人员来说很重要？)
    - [测试人员如何在敏捷中与其他团队成员协作？](#测试人员如何在敏捷中与其他团队成员协作？)
  - [工具和技术](#工具和技术)
    - [敏捷测试中常用的工具有哪些？](#敏捷测试中常用的工具有哪些？)
    - [这些工具如何支持敏捷测试流程？](#这些工具如何支持敏捷测试流程？)
    - [自动化在敏捷测试中的作用是什么？](#自动化在敏捷测试中的作用是什么？)
    - [敏捷测试中如何实现持续集成？](#敏捷测试中如何实现持续集成？)
  - [挑战和解决方案](#挑战和解决方案)
    - [敏捷测试中面临哪些常见挑战？](#敏捷测试中面临哪些常见挑战？)
    - [如何克服这些挑战？](#如何克服这些挑战？)
    - [有效敏捷测试的最佳实践有哪些？](#有效敏捷测试的最佳实践有哪些？)
    - [敏捷测试如何随着时间的推移而改进？](#敏捷测试如何随着时间的推移而改进？)
<!-- TOC END -->

敏捷测试

符合敏捷软件开发的原则。与传统方法不同，测试从项目一开始就开始，开发和测试同时进行。这种密切的协作确保了任务的高效完成。

## 相关术语：

- [Agile Development](../A/agile-development.md)
- [Iteration](../I/iteration.md)
- [Scrum](../S/scrum.md)

### 另请参阅：

- [Wikipedia](https://en.wikipedia.org/wiki/Agile_testing)

## 关于敏捷测试的问题？

### 基础知识和重要性

#### 什么是敏捷测试？

[Agile Testing](../A/agile-testing.md) 是遵循敏捷软件开发原则的 **[software testing](../S/software-testing.md) 实践**。这是一个迭代测试过程，其中**需求通过自组织跨职能团队之间的协作而演变**。 [Agile Testing](../A/agile-testing.md) 与迭代开发方法保持一致，并确保测试不是一个单独的阶段，而是开发生命周期的一个组成部分。
  在[Agile Testing](../A/agile-testing.md) 中，测试人员从项目一开始就积极参与，确保持续反馈和增量改进。测试与开发在**短[iterations](../I/iteration.md)**（称为冲刺）中并行进行，允许**持续集成**和频繁的功能验证。
  敏捷团队中的测试人员与开发人员、业务分析师和其他团队成员密切合作，根据用户故事和验收标准创建 **[test cases](../T/test-case.md)** 和 **自动化测试**。他们专注于 **[exploratory testing](../E/exploratory-testing.md)**、**[test-driven development](../T/test-driven-development.md) (TDD)** 和 **行为驱动开发 ([BDD](../B/bdd.md))**，以确保软件满足业务需求且具有高质量。
  [Agile Testing](../A/agile-testing.md) 强调需要**灵活的[test plans](../T/test-plan.md)**，它可以适应需求的变化，并鼓励通过文档进行**面对面的沟通**。目标是提供有关产品质量的**快速反馈**，并确保及时解决任何问题。
  [Test automation](../T/test-automation.md) 是[Agile Testing](../A/agile-testing.md) 的关键组件，使团队能够快速、频繁地执行回归测试。常用工具包括[Selenium](../S/selenium.md)、JUnit、TestNG、Cucumber和SpecFlow，它们支持自动化[test scripts](../T/test-script.md)的快速开发和执行。
  [Agile Testing](../A/agile-testing.md) 是一个持续的过程，要求测试人员积极主动、适应和协作，以确保软件满足客户的期望并以最少的缺陷交付。

#### 敏捷测试在软件开发中的重要性是什么？

[Agile Testing](../A/agile-testing.md) 在软件开发中至关重要，原因有几个。它确保**质量**从一开始就融入到产品中，而不是事后才想到。通过使测试活动与迭代开发过程保持一致，[Agile Testing](../A/agile-testing.md) 可以实现**早期缺陷检测**和**解决**，从而减少周期后期修复[bugs](../B/bug.md) 的成本和工作量。
  [Agile Testing](../A/agile-testing.md) 专注于**持续反馈**，可以**快速响应变化**，无论是不断变化的客户需求还是对产品使用的新见解。这种适应性对于提供真正满足用户需求并可在必要时进行调整的产品至关重要。
  此外，[Agile Testing](../A/agile-testing.md) 促进了一种**协作文化**，其中测试人员与开发人员、业务分析师和其他利益相关者密切合作。这种合作促进了对产品目标和质量标准的共同理解，从而形成了更具凝聚力和高效能的团队。
  将**自动化**纳入[Agile Testing](../A/agile-testing.md)也很重要，因为它支持频繁且可靠的测试，使团队能够在不影响质量的情况下保持高速交付。自动化测试提供了一个安全网，促进**持续集成**和**部署**实践，这是敏捷方法论的核心。
  最终，[Agile Testing](../A/agile-testing.md) 旨在更快、更高效地向客户交付**价值**，同时保持高标准的质量并适应发生的变化。它是敏捷精神的一个组成部分，它优先考虑客户满意度和有效的团队动力，而不是严格的流程和文档。

#### 敏捷测试与传统测试方法有何不同？

[Agile Testing](../A/agile-testing.md) 与传统测试方法的不同之处在于开发周期内的**灵活性**、**协作**和**集成**。与测试是开发后的一个单独阶段的传统方法不同，[Agile Testing](../A/agile-testing.md) 是**连续**和**迭代**，测试是在功能开发时编写和执行的。
  在传统测试中，需求是预先定义的，并且通常保持静态，从而导致**瀑布**方法。然而，[Agile Testing](../A/agile-testing.md) 即使在开发过程的后期，也会接受需求的变化，以确保产品与用户需求保持一致。
  敏捷中的测试人员是**跨职能团队**的一部分，与开发人员、产品所有者和其他利益相关者密切合作。这与传统方法形成鲜明对比，传统方法中测试人员通常在孤岛中工作，仅在开发阶段之后才参与。
  [Agile Testing](../A/agile-testing.md) 严重依赖**自动化**来保持 [iterations](../I/iteration.md) 的快速步伐。自动化测试是为[regression testing](../R/regression-testing.md) 创建的，并集成到**持续集成 (CI)** 管道中，提供有关代码更改的即时反馈。
  **沟通**​​是@​​@PROTECTED_61@@ 的关键，每天的站立会议和频繁的协作取代了正式的文档和状态会议。测试人员应该积极主动，尽早提出担忧和建议，而不是在漫长的测试周期结束时报告问题。
  总之，[Agile Testing](../A/agile-testing.md) 的特点是**适应性**、**团队集成**和**持续反馈循环**，与传统测试方法的顺序且通常僵化的方法形成鲜明对比。

#### 敏捷测试的关键原则是什么？

[Agile Testing](../A/agile-testing.md) 的主要原则包括：

- **持续反馈**：[Agile testing](../A/agile-testing.md) 向开发团队提供有关产品当前状态的持续反馈，确保及时发现并解决问题。
  - **协作**：测试人员与开发人员、业务分析师和其他团队成员密切合作，以确保对产品及其需求有共同的理解。
  - **[Incremental Testing](../I/incremental-testing.md)**：测试是在开发的同时逐步进行的，可以及早发现缺陷并降低修复它们的成本。
  - **[Test-Driven Development](../T/test-driven-development.md) (TDD)**：在编写需要测试的代码之前编写测试可以确保代码从一开始就满足要求。
  - **简单性**：专注于提供价值的简单有效的测试，避免不必要的复杂性，从而减慢开发过程。
  - **适应性**：[Agile testing](../A/agile-testing.md) 能够适应需求或优先级的变化，使团队能够快速有效地进行调整。
  - **持续改进**：定期审查和改进[Agile testing](../A/agile-testing.md)实践，培养持续学习和增强的文化。
  - **以用户为中心**：测试的设计考虑了最终用户，确保产品满足用户的需求和期望。
  - **自动化**：在可能的情况下，测试是自动化的，以加快测试过程，并允许频繁的[regression testing](../R/regression-testing.md)，而无需额外成本。
  - **整个团队的责任**：测试不仅仅是测试人员的责任；整个团队对产品的质量负责。
  通过遵守这些原则，[Agile testing](../A/agile-testing.md) 旨在及时有效地交付高质量的软件，重点关注客户满意度和对变化的响应能力。

- **持续反馈**：[Agile testing](../A/agile-testing.md) 向开发团队提供有关产品当前状态的持续反馈，确保及时发现并解决问题。
  - **协作**：测试人员与开发人员、业务分析师和其他团队成员密切合作，以确保对产品及其需求有共同的理解。
  - **[Incremental Testing](../I/incremental-testing.md)**：测试是在开发的同时逐步进行的，可以及早发现缺陷并降低修复它们的成本。
  - **[Test-Driven Development](../T/test-driven-development.md) (TDD)**：在编写需要测试的代码之前编写测试可以确保代码从一开始就满足要求。
  - **简单性**：专注于提供价值的简单有效的测试，避免不必要的复杂性，从而减慢开发过程。
  - **适应性**：[Agile testing](../A/agile-testing.md) 能够适应需求或优先级的变化，使团队能够快速有效地进行调整。
  - **持续改进**：定期审查和改进[Agile testing](../A/agile-testing.md)实践，培养持续学习和增强的文化。
  - **以用户为中心**：测试的设计考虑了最终用户，确保产品满足用户的需求和期望。
  - **自动化**：在可能的情况下，测试是自动化的，以加快测试过程，并允许频繁的[regression testing](../R/regression-testing.md)，而无需额外成本。
  - **整个团队的责任**：测试不仅仅是测试人员的责任；整个团队对产品的质量负责。

### 流程和技术

#### 敏捷测试有哪些不同阶段？

[Agile Testing](../A/agile-testing.md) 涉及与 [Agile development](../A/agile-development.md) 的迭代性质相一致的几个阶段。这些阶段并不是严格线性的，而是随着项目的发展经常重叠和重复：

- **冲刺计划**：测试人员与开发人员和产品负责人合作，定义可测试的用户故事和验收标准。
  - **测试设计**：一旦定义了用户故事，测试人员就开始设计测试。他们创建[test cases](../T/test-case.md)并确定必要的[test data](../T/test-data.md)。
  - $

    ```
    ```// 示例：[Test case](../T/test-case.md) 登录功能的伪代码
  描述（“登录功能”，（）=> {
  it("应该使用有效凭据对用户进行身份验证", () => {
  期望（验证（'validUser'，'validPass'））。toBeTruthy（）;
  });
  });

  ```
  - **Test Development**: Testers write automated test scripts alongside development to ensure that new features are tested as soon as they are completed.
  - **Continuous Testing**: Automated tests are run frequently to provide immediate feedback on the quality of the codebase.
  - **Test Execution**: Manual and automated tests are executed to validate the functionality against the acceptance criteria.
  - **Exploratory Testing**: Testers perform unscripted testing to discover defects that automated tests might miss.
  - **Regression Testing**: Automated regression tests are run to ensure that new changes haven't adversely affected existing functionality.
  - **Review and Retrospective**: The team reviews test results and discusses improvements for the next iteration.
  - **Release Testing**: Prior to release, testers perform final validation to ensure the product is ready for production.
  - **Post-Release Testing**: After deployment, testing continues to monitor the performance and user feedback for any issues that need to be addressed in future sprints.
  ```

- **冲刺计划**：测试人员与开发人员和产品负责人合作，定义可测试的用户故事和验收标准。
  - **测试设计**：一旦定义了用户故事，测试人员就开始设计测试。他们创建[test cases](../T/test-case.md)并确定必要的[test data](../T/test-data.md)。
  - $

    ```
    ```

#### 常见的敏捷测试方法有哪些？

常见的 [Agile testing](../A/agile-testing.md) 方法包括：

- **行为驱动开发 ([BDD](../B/bdd.md))**：通过以可读且可执行的格式定义规范来关注应用程序的业务行为。 Cucumber 和 SpecFlow 等工具支持 [BDD](../B/bdd.md)。
  - **[Test-Driven Development](../T/test-driven-development.md) (TDD)**：涉及在实际代码之前编写测试。它有助于确保代码满足要求并鼓励简单的设计。经常使用 JUnit 和 [NUnit](../N/nunit.md) 等 xUnit 框架。
  - **验收[Test-Driven Development](../T/test-driven-development.md) (ATDD)**：与 TDD 类似，但重点是捕获用户故事的验收标准。它鼓励业务、测试人员和开发人员之间的协作。
  - **[Exploratory Testing](../E/exploratory-testing.md)**：鼓励测试人员在没有预定义测试的情况下探索软件，提高创造力并发现脚本测试可能遗漏的问题。
  - **[Session-Based Testing](../S/session-based-testing.md)**：结构化[exploratory testing](../E/exploratory-testing.md)，涉及针对特定领域的不间断测试会话，并记录结果和指标以供审查。
  - **[Pair Testing](../P/pair-testing.md)**：两名团队成员（通常是开发人员和测试人员）一起进行测试活动，分享想法和见解以尽早发现缺陷。
  - **持续测试**：持续集成/持续部署 (CI/CD) 的一部分，其中频繁运行自动化测试，以提供与候选软件发布相关的业务风险的即时反馈。
  每种方法都补充了协作、灵活性和交付高质量软件的敏捷原则，简称[iterations](../I/iteration.md)。敏捷测试人员经常结合这些方法来适应团队的独特环境和要求。

- **行为驱动开发 ([BDD](../B/bdd.md))**：通过以可读和可执行的格式定义规范来关注应用程序的业务行为。 Cucumber 和 SpecFlow 等工具支持[BDD](../B/bdd.md)。
  - **[Test-Driven Development](../T/test-driven-development.md) (TDD)**：涉及在实际代码之前编写测试。它有助于确保代码满足要求并鼓励简单的设计。经常使用 JUnit 和 [NUnit](../N/nunit.md) 等 xUnit 框架。
  - **验收[Test-Driven Development](../T/test-driven-development.md) (ATDD)**：与 TDD 类似，但重点是捕获用户故事的验收标准。它鼓励业务、测试人员和开发人员之间的协作。
  - **[Exploratory Testing](../E/exploratory-testing.md)**：鼓励测试人员在没有预定义测试的情况下探索软件，提高创造力并发现脚本测试可能遗漏的问题。
  - **[Session-Based Testing](../S/session-based-testing.md)**：结构化[exploratory testing](../E/exploratory-testing.md)，涉及针对特定领域的不间断测试会话，并记录结果和指标以供审查。
  - **[Pair Testing](../P/pair-testing.md)**：两名团队成员（通常是开发人员和测试人员）一起进行测试活动，分享想法和见解以尽早发现缺陷。
  - **持续测试**：持续集成/持续部署 (CI/CD) 的一部分，其中频繁运行自动化测试，以提供与候选软件发布相关的业务风险的即时反馈。

#### 敏捷测试中使用的关键技术是什么？

[Agile Testing](../A/agile-testing.md) 中使用的关键技术包括：

- **[Test-Driven Development](../T/test-driven-development.md) (TDD)**：在代码之前编写测试以定义所需的功能。

    ```
    test('adds 1 + 2 to equal 3', () => {
      expect(sum(1, 2)).toBe(3);
    });
    ```

- **行为驱动开发 ([BDD](../B/bdd.md))**：通过用自然语言指定行为来扩展 TDD。

    ```
    describe('User login', () => {
      it('succeeds with correct credentials', () => {
        expect(login('user', 'pass')).toBe(true);
      });
    });
    ```

- **验收[Test-Driven Development](../T/test-driven-development.md) (ATDD)**：在实施之前协作定义验收标准和测试。
  - **[Exploratory Testing](../E/exploratory-testing.md)**：同时学习、测试设计和执行，以发现脚本测试未涵盖的缺陷。
  - **[Pair Testing](../P/pair-testing.md)**：两个具有不同观点的团队成员一起测试相同的功能以增强覆盖范围。
  - **持续测试**：在开发过程中自动运行测试以获取即时反馈。
  - **[Session-Based Testing](../S/session-based-testing.md)**：具有特定目标和时间框架的结构化[exploratory testing](../E/exploratory-testing.md) 会议。
  - **[Risk-Based Testing](../R/risk-based-testing.md)**：根据失败风险和潜在缺陷的影响确定测试的优先级。
  - **示例规范**：与利益相关者合作创建示例来阐明需求、推动开发和测试。
  - **Mob 测试**：整个团队一起测试软件，分享见解和知识。
  通过采用这些技术，敏捷团队的目标是确保整个开发过程的质量，而不是将测试视为一个单独的阶段。这种方法可以实现更快的反馈，促进协作，并始终专注于为客户提供价值。

- **[Test-Driven Development](../T/test-driven-development.md) (TDD)**：在代码之前编写测试以定义所需的功能。

    ```
    test('adds 1 + 2 to equal 3', () => {
      expect(sum(1, 2)).toBe(3);
    });
    ```

- **行为驱动开发 ([BDD](../B/bdd.md))**：通过用自然语言指定行为来扩展 TDD。

    ```
    describe('User login', () => {
      it('succeeds with correct credentials', () => {
        expect(login('user', 'pass')).toBe(true);
      });
    });
    ```

- **验收[Test-Driven Development](../T/test-driven-development.md) (ATDD)**：在实施之前协作定义验收标准和测试。
  - **[Exploratory Testing](../E/exploratory-testing.md)**：同时学习、测试设计和执行，以发现脚本测试未涵盖的缺陷。
  - **[Pair Testing](../P/pair-testing.md)**：两个具有不同观点的团队成员一起测试相同的功能以增强覆盖范围。
  - **持续测试**：在开发过程中自动运行测试以获取即时反馈。
  - **[Session-Based Testing](../S/session-based-testing.md)**：具有特定目标和时间框架的结构化[exploratory testing](../E/exploratory-testing.md) 会议。
  - **[Risk-Based Testing](../R/risk-based-testing.md)**：根据失败风险和潜在缺陷的影响确定测试的优先级。
  - **示例规范**：与利益相关者合作创建示例来阐明需求、推动开发和测试。
  - **Mob 测试**：整个团队一起测试软件，分享见解和知识。

#### 测试如何集成到敏捷开发过程中？

通过**持续协作**和**[iteration](../I/iteration.md)**将测试融入**[Agile development](../A/agile-development.md)周期**。每个冲刺都从规划会议开始，其中**测试人员**和**开发人员**一起定义**用户故事**和**验收标准**，确保对功能及其测试方式有共同的理解。
  在开发过程中，测试人员与开发人员并行工作，通常采用 **[Test-Driven Development](../T/test-driven-development.md) (TDD)** 或 **行为驱动开发 ([BDD](../B/bdd.md))** 在编写代码之前创建自动化测试。当功能完成时，会立即运行这些测试来验证功能，从而促进**持续反馈**。
  **每日站会**包括测试状态更新，提高透明度并允许团队及时解决问题。测试人员参与**细化会议**，以澄清需求并为即将到来的冲刺做好准备，确保采用积极主动的方法进行测试规划。
  在**持续集成 (CI)** 环境中，每次代码提交都会触发自动化测试。这提供了快速验证并有助于及早识别回归。团队审查测试结果并相应地调整待办事项和[test cases](../T/test-case.md)。
  在每个冲刺结束时，团队都会进行**冲刺评审**，其中演示已完成的功能，并进行**回顾**以反思流程并改进实践。测试人员提供有关[test coverage](../T/test-coverage.md)、质量指标和风险评估的见解，影响下一个[iteration](../I/iteration.md)。
  总之，敏捷测试是一项**持续的协作工作**，与开发活动紧密结合，确保质量从一开始就内置到产品中，并通过频繁的迭代周期进行维护。

### 角色和职责

#### 测试人员在敏捷团队中的角色是什么？

在**敏捷团队**中，测试人员的角色是多方面的。测试人员是**开发生命周期**不可或缺的一部分，从产品构思的初始阶段到发布的最后阶段都积极参与。他们与开发人员、业务分析师、产品所有者和其他利益相关者密切合作，以确保对产品及其需求有共同的理解。
  敏捷中的测试人员负责：

- **创建[test cases](../T/test-case.md)**
    和
    **[test plans](../T/test-plan.md)**
    符合用户故事和验收标准。

- 表演
    **[exploratory testing](../E/exploratory-testing.md)**
    发现结构化测试可能无法揭示的问题。

- 参与
    **持续测试**
    作为开发周期的一部分，确保新功能在开发时得到测试。

- 提供
    **即时反馈**
    给开发团队，促进快速解决缺陷。

- 倡导
    **质量**
    整个开发过程，而不仅仅是最后。

- 协助
    **提炼用户故事**
    和
    **验收标准**
    确保它们是可测试的且清晰的。

- 参加
    **敏捷仪式**
    例如每日站立会议、冲刺计划、回顾和回顾，以与团队的目标和进度保持一致。

- **与开发人员合作**
    创造
    **自动化测试**
    作为持续集成管道的一部分。

- 帮助维持和改善
    **[test automation](../T/test-automation.md) 框架**
    和
    **[test suites](../T/test-suite.md)**
    以确保它们有效且高效。
  敏捷环境中的测试人员积极主动，不断适应变化，并专注于通过高质量的软件为客户提供价值。他们不仅仅是测试专家，而且是团队成功的关键贡献者。

- **创建[test cases](../T/test-case.md)**
    和
    **[test plans](../T/test-plan.md)**
    符合用户故事和验收标准。

- 表演
    **[exploratory testing](../E/exploratory-testing.md)**
    发现结构化测试可能无法揭示的问题。

- 参与
    **持续测试**
    作为开发周期的一部分，确保新功能在开发时得到测试。

- 提供
    **即时反馈**
    给开发团队，促进快速解决缺陷。

- 倡导
    **质量**
    整个开发过程，而不仅仅是最后。

- 协助
    **提炼用户故事**
    和
    **验收标准**
    确保它们是可测试的且清晰的。

- 参加
    **敏捷仪式**
    例如每日站立会议、冲刺计划、回顾和回顾，以与团队的目标和进度保持一致。

- **与开发人员合作**
    创造
    **自动化测试**
    作为持续集成管道的一部分。

- 帮助维持和改善
    **[test automation](../T/test-automation.md) 框架**
    和
    **[test suites](../T/test-suite.md)**
    以确保它们有效且高效。

#### 敏捷中测试人员的职责与传统测试角色有何不同？

在敏捷中，测试人员是开发团队不可或缺的一部分，在**冲刺**中工作以确保持续集成和交付。与测试是一个单独阶段的传统角色不同，敏捷测试人员从**项目开始**就参与其中，参与规划、设计和审查会议。
  随着需求的发展，敏捷测试人员必须具有**适应性**并适应**变化**。他们与开发人员密切合作，通常以**结对编程**的方式来创建和运行测试，确保即时反馈。这种合作促进了整个团队的**“测试心态”**，鼓励所有成员对质量承担责任。
  **持续测试**是一项核心职责，测试人员经常在开发功能时编写**自动化回归测试**。他们必须优先考虑哪些测试要自动化，以便在最短的时间内提供最佳的覆盖范围。敏捷测试人员还专注于 **[exploratory testing](../E/exploratory-testing.md)** 以发现自动化测试可能遗漏的问题。
  该职位需要**强大的技术技能**，包括编码和使用自动化工具，以及**软技能**，例如沟通和解决问题。敏捷测试人员必须能够清楚地阐明测试结果，并与团队成员建设性地合作解决问题。
  敏捷测试人员还负责维护 **[test environment](../T/test-environment.md)** 并确保其与生产环境保持一致以避免出现差异。他们必须熟练使用**版本控制**和**持续集成工具**来管理他们的[test scripts](../T/test-script.md)并与团队共享结果。
  总体而言，敏捷测试人员积极主动、协作且技术娴熟，在迭代和高效地交付高质量软件方面发挥着关键作用。

#### 哪些技能对于敏捷测试人员来说很重要？

对于敏捷测试人员来说，有几项技能对于成功至关重要：

- **适应性**：敏捷环境是动态的，要求测试人员快速调整以适应需求或项目方向的变化。
  - **技术熟练程度**：熟练掌握各种测试工具和编程语言（例如 Java、Python）对于创建和维护自动化测试脚本至关重要。
  - **沟通**​​：清晰简洁的沟通对于与开发人员、产品所有者和其他利益相关者的合作至关重要。
  - **批判性思维**：敏捷测试人员必须能够分析需求和用户故事以创建有效的测试用例。
  - **持续学习**：保持最新的测试方法和工具对于改进流程和效率是必要的。
  - **协作**：与跨职能团队密切合作，确保质量是共同的责任。
  - **以用户为中心**：设计测试时优先考虑最终用户体验，以确保产品满足他们的需求。
  - **理解敏捷原则**：了解敏捷方法，使测试活动与团队的方法保持一致。
  - **[Exploratory testing](../E/exploratory-testing.md) 技能**：无需正式测试用例即可快速学习和深入测试新功能的能力。
  - **解决问题**：识别、分析和解决测试过程中出现的问题。
  - **自动化策略**：知道何时以及自动化什么，以最大限度地提高测试套件的价值和可维护性。
  这些技能帮助敏捷测试人员有效地实现团队快速交付高质量软件的目标。

- **适应性**：敏捷环境是动态的，要求测试人员快速调整以适应需求或项目方向的变化。
  - **技术熟练程度**：熟练掌握各种测试工具和编程语言（例如 Java、Python）对于创建和维护自动化测试脚本至关重要。
  - **沟通**​​：清晰简洁的沟通对于与开发人员、产品所有者和其他利益相关者的合作至关重要。
  - **批判性思维**：敏捷测试人员必须能够分析需求和用户故事以创建有效的测试用例。
  - **持续学习**：保持最新的测试方法和工具对于改进流程和效率是必要的。
  - **协作**：与跨职能团队密切合作，确保质量是共同的责任。
  - **以用户为中心**：设计测试时优先考虑最终用户体验，以确保产品满足他们的需求。
  - **理解敏捷原则**：了解敏捷方法，使测试活动与团队的方法保持一致。
  - **[Exploratory testing](../E/exploratory-testing.md) skills** : Ability to quickly learn and test new features in-depth without formal test cases.
  - **解决问题**：识别、分析和解决测试过程中出现的问题。
  - **自动化策略**：知道何时以及自动化什么，以最大限度地提高测试套件的价值和可维护性。

#### 测试人员如何在敏捷中与其他团队成员协作？

在敏捷中，测试人员与**开发人员**、**产品所有者**和其他团队成员密切合作，以确保对产品及其需求有共同的理解。他们参与**每日站立会议**来讨论进展、障碍和计划。在**冲刺计划**期间，测试人员帮助定义**验收标准**并提供有关用户故事可测试性的输入。
  测试人员在**结对编程**或**群体测试**会话中与开发人员一起工作，在开发周期的早期创建和执行测试。他们还参与**代码审查**，以在代码合并之前识别潜在问题。
  **持续沟通**是关键，测试人员通常嵌入跨职能团队中，营造共享知识和技能的环境。他们使用**即时消息工具**、**问题跟踪系统**和**wiki 页面**来保持测试活动的透明度和最新信息。
  在**冲刺回顾**中，测试人员提供有关质量和流程改进的见解，确保测试随着团队的实践而发展。通过倡导质量，他们帮助团队优先考虑**技术债务**和**[bug](../B/bug.md)修复**。
  测试人员还通过验证用户故事是否满足验收标准以及从用户的角度提供有关产品行为的反馈来支持**产品所有者**。这种合作确保产品不仅按预期工作，而且满足用户的需求和期望。

  ```
  // Example of a communication snippet in a messaging tool
  tester: "I've noticed a recurring issue with feature X. Can we discuss potential causes in today's stand-up?"
  developer: "Sure, I've seen it too. Let's review the logs together after the meeting."
  ```

### 工具和技术

#### 敏捷测试中常用的工具有哪些？

[Agile Testing](../A/agile-testing.md) 中常用的工具包括：

- **[Selenium](../S/selenium.md)** ：用于自动化网络浏览器的开源工具。它支持多种语言和浏览器。
  - **[JIRA](../J/jira.md)** ：广泛用于错误跟踪、问题跟踪和项目管理。
  - **Cucumber** ：支持具有简单语言规范的行为驱动开发（BDD）。
  - **Jenkins**：一种开源 CI/CD 工具，可自动化软件交付过程的各个阶段。
  - **Git**：用于在软件开发过程中跟踪源代码更改的版本控制系统。
  - **TestRail**：与问题跟踪系统集成的测试用例和测试管理软件工具。
  - **Appium**：用于在 iOS 和 Android 平台上自动化移动应用程序的开源工具。
  - **[Postman](../P/postman.md)** ：用于API测试，允许用户快速构造复杂的HTTP请求。
  - **SpecFlow** ：将业务需求绑定到 .NET 代码并支持 BDD 的 .NET 工具。
  - **JUnit/TestNG** ：用于 Java 单元测试的框架，提供注释来标识测试方法。
  - **Mockito**：Java 中单元测试的模拟框架。
  - **REST-assured**：用于简化 RESTful API 测试的 Java DSL。
  - **Puppeteer** ：一个 Node 库，提供高级 API 来通过 DevTools 协议控制 Chrome 或 Chromium。
  这些工具支持[Agile Testing](../A/agile-testing.md)的各个方面，从[test case management](../T/test-case-management.md)到持续集成，并满足不同的测试需求，例如[unit testing](../U/unit-testing.md)、[integration testing](../I/integration-testing.md)、[functional testing](../F/functional-testing.md)和[acceptance testing](../A/acceptance-testing.md)。它们促进快速反馈和持续改进，这是敏捷方法论的标志。

- **[Selenium](../S/selenium.md)** ：用于自动化 Web 浏览器的开源工具。它支持多种语言和浏览器。
  - **[JIRA](../J/jira.md)** ：广泛用于错误跟踪、问题跟踪和项目管理。
  - **Cucumber** ：支持具有简单语言规范的行为驱动开发（BDD）。
  - **Jenkins**：一种开源 CI/CD 工具，可自动化软件交付过程的各个阶段。
  - **Git**：用于在软件开发过程中跟踪源代码更改的版本控制系统。
  - **TestRail**：与问题跟踪系统集成的测试用例和测试管理软件工具。
  - **Appium**：用于在 iOS 和 Android 平台上自动化移动应用程序的开源工具。
  - **[Postman](../P/postman.md)** ：用于API测试，允许用户快速构造复杂的HTTP请求。
  - **SpecFlow** ：将业务需求绑定到 .NET 代码并支持 BDD 的 .NET 工具。
  - **JUnit/TestNG** ：用于 Java 单元测试的框架，提供注释来标识测试方法。
  - **Mockito**：Java 中单元测试的模拟框架。
  - **REST-assured**：用于简化 RESTful API 测试的 Java DSL。
  - **Puppeteer** ：一个 Node 库，提供高级 API 来通过 DevTools 协议控制 Chrome 或 Chromium。

#### 这些工具如何支持敏捷测试流程？

[Test automation](../T/test-automation.md) 工具通过实现快速反馈和持续改进来支持**[Agile Testing](../A/agile-testing.md) 流程**，这是敏捷方法论的核心。这些工具允许团队频繁执行测试并及早发现问题，从而促进**持续集成**和**持续交付**。
  自动化测试可以集成到**构建管道**中，在提交更改时自动运行。这可确保新代码不会破坏现有功能，从而在整个开发过程中保持**软件的健康**。
  **版本控制集成**是这些工具的另一个功能，允许[test scripts](../T/test-script.md) 与应用程序代码一起发展。测试人员可以更新自动化测试以反映用户故事或验收标准的变化，从而保持[test suite](../T/test-suite.md)的相关性和有效性。
  **并行执行功能**减少了运行大量[test suites](../T/test-suite.md)所需的时间，从而为开发人员提供更快的反馈。这在敏捷中至关重要，因为时间限制[iterations](../I/iteration.md) 要求效率。
  此外，[test automation](../T/test-automation.md) 工具通常带有**报告功能**，可以提供对[test coverage](../T/test-coverage.md) 和缺陷趋势的见解。这些数据对于敏捷团队在回顾期间确定流程改进领域非常有价值。
  这些工具中的协作功能可帮助测试人员、开发人员和其他利益相关者共享结果并共同解决问题。这与敏捷强调团队协作和质量集体所有权相一致。
  最后，许多 [test automation](../T/test-automation.md) 工具支持**行为驱动开发 ([BDD](../B/bdd.md))** 和 **[test-driven development](../T/test-driven-development.md) (TDD)**，这是敏捷中常用的方法，以确保测试从一开始就符合客户要求。

#### 自动化在敏捷测试中的作用是什么？

在[Agile Testing](../A/agile-testing.md)中，自动化在保持快速开发周期的节奏和确保对产品质量的即时反馈方面发挥着关键作用。自动化通过快速可靠地执行一套测试来支持**持续集成**和**持续交付**，这对于频繁发布至关重要。
  自动化测试充当安全网，有助于及早发现回归和缺陷。它们使测试人员能够通过自动化重复且耗时的任务来专注于更复杂的[exploratory testing](../E/exploratory-testing.md)。在变更频繁的敏捷中，自动化可确保在引入新变更后现有功能保持不变。
  此外，自动化促进了 **[Test-Driven Development](../T/test-driven-development.md) (TDD)** 和 **行为驱动开发 ([BDD](../B/bdd.md))**，其中测试是在代码之前编写的，并作为开发指南。这些实践中的自动化测试确认代码满足预定义的标准并且行为符合预期。
  为了无缝集成到敏捷流程中，自动化测试必须：

- **可维护**：易于根据应用程序中的更改进行更新。
  - **可靠**：始终提供准确的结果。
  - **快速**：在支持快速迭代的时间范围内执行。
  敏捷中的自动化不仅仅涉及测试本身，还涉及**[test data](../T/test-data.md) 生成**、**环境[setup](../S/setup.md)** 和**部署过程**。这种全面的自动化方法可以帮助敏捷团队以与快速交付的敏捷精神相匹配的速度交付高质量的软件。

- **可维护**：易于根据应用程序中的更改进行更新。
  - **可靠**：始终提供准确的结果。
  - **快速**：在支持快速迭代的时间范围内执行。

#### 敏捷测试中如何实现持续集成？

[Agile Testing](../A/agile-testing.md) 中的持续集成 (CI) 可以通过设置 CI 服务器来实现，只要向版本控制系统提交新代码，该服务器就会自动触发一组测试。 **[Test automation](../T/test-automation.md)** 在这里至关重要，因为它允许快速反馈应用程序的运行状况。
  首先，配置 CI 服务器（例如 Jenkins、CircleCI、Travis CI）以监视存储库的更改。检测到更改后，CI 服务器应该：

1. **拉取最新代码**
    来自主分支。

2. **构建应用程序**
    确保新代码集成没有问题。

3. **运行自动化测试**
    ，其中应包括单元测试、集成测试和任何其他相关的自动化检查。
  使用像 Git Flow 这样的**分支策略**来管理不同的开发线并确保主分支保持稳定。功能分支可用于新工作，然后在测试后合并到主分支中。
  实施 **[test-driven development](../T/test-driven-development.md) (TDD)** 或 **行为驱动开发 ([BDD](../B/bdd.md))** 以确保在代码之前编写测试，从而提升 [test coverage](../T/test-coverage.md) 和质量。
  确保[test suite](../T/test-suite.md) **可维护且可扩展**。测试应该快速、可靠且相关。 [Flaky tests](../F/flaky-test.md) 必须修复或删除以维持对 CI 流程的信任。
  最后，将**测试结果报告**集成到 CI 管道中。这应该提供有关测试结果的清晰反馈，使团队能够轻松快速解决问题。
  通过遵循这些步骤，CI 成为 [Agile Testing](../A/agile-testing.md) 不可或缺的一部分，使团队能够及早发现并解决问题，从而在整个开发过程中保持 [software quality](../S/software-quality.md) 的高标准。

1. **拉取最新代码**
    来自主分支。

2. **构建应用程序**
    确保新代码集成没有问题。

3. **运行自动化测试**
    ，其中应包括单元测试、集成测试和任何其他相关的自动化检查。

### 挑战和解决方案

#### 敏捷测试中面临哪些常见挑战？

[Agile Testing](../A/agile-testing.md) 中的常见挑战包括：

- **保持测试质量**
    在快速发布周期下可能会很困难，因为进行彻底测试的时间较少。

- **适应不断变化的要求**
    通常会导致返工并可能破坏测试策略。

- **确保足够的[test coverage](../T/test-coverage.md)**
    在功能不断发展的动态环境中是具有挑战性的。

- **平衡自动化和[manual testing](../M/manual-testing.md)**
    至关重要；过度依赖其中任何一个都可能是有害的。

- **集成新工具和技术**
    可能很复杂且耗时。

- **协作与沟通**
    跨职能团队之间的沟通必须持续有效，以避免误解并确保每个人都与目标保持一致。

- **技术债务**
    如果测试没有给予足够的重视，可能会累积，导致潜在的缺陷并增加未来的维护工作。

- **资源限制**
    例如对测试环境或数据的访问受限可能会阻碍测试过程。

- **[Flaky tests](../F/flaky-test.md)**
    可能会成为一个重大问题，尤其是随着自动化使用的增加，导致对测试结果的不信任。

- **性能和[security testing](../S/security-testing.md)**
    通常被留在周期的后期，这可能导致关键问题发现得太晚。
  为了克服这些挑战，团队可以：

- 确定测试套件的优先级并不断完善。
  - 采用左移方法在开发过程的早期进行测试。
  - 使用测试驱动开发（TDD）和行为驱动开发（BDD）来确保满足需求。
  - 实施服务虚拟化以减轻环境和数据限制。
  - 定期审查和维护自动化测试以减少不稳定。
  - 在每个冲刺中分配时间来解决技术债务。
  - 确保从开发过程一开始就考虑性能和安全性。
  - **保持测试质量**
    在快速发布周期下可能会很困难，因为进行彻底测试的时间较少。

- **适应不断变化的要求**
    通常会导致返工并可能破坏测试策略。

- **确保足够的[test coverage](../T/test-coverage.md)**
    在功能不断发展的动态环境中是具有挑战性的。

- **平衡自动化和[manual testing](../M/manual-testing.md)**
    至关重要；过度依赖其中任何一个都可能是有害的。

- **集成新工具和技术**
    可能很复杂且耗时。

- **协作与沟通**
    跨职能团队之间的沟通必须持续有效，以避免误解并确保每个人都与目标保持一致。

- **技术债务**
    如果测试没有给予足够的重视，可能会累积，导致潜在的缺陷并增加未来的维护工作。

- **资源限制**
    例如对测试环境或数据的访问受限可能会阻碍测试过程。

- **[Flaky tests](../F/flaky-test.md)**
    可能会成为一个重大问题，尤其是随着自动化使用的增加，导致对测试结果的不信任。

- **性能和[security testing](../S/security-testing.md)**
    通常被留在周期的后期，这可能导致关键问题发现得太晚。

- 确定测试套件的优先级并不断完善。
  - 采用左移方法在开发过程的早期进行测试。
  - 使用测试驱动开发（TDD）和行为驱动开发（BDD）来确保满足需求。
  - 实施服务虚拟化以减轻环境和数据限制。
  - 定期审查和维护自动化测试以减少不稳定。
  - 在每个冲刺中分配时间来解决技术债务。
  - 确保从开发过程一开始就考虑性能和安全性。

#### 如何克服这些挑战？

克服 [Agile Testing](../A/agile-testing.md) 中的挑战需要采取战略方法并采用针对敏捷环境量身定制的最佳实践。以下是一些策略：

- **拥抱变化**：敏捷就是适应变化。使用**重构**来保持测试代码可维护并适应应用程序中的频繁更改。
  - **持续学习**：随时了解最新的测试技术和工具。鼓励团队内部的知识共享，以培养集体专业知识。
  - **[Test-Driven Development](../T/test-driven-development.md) (TDD)**：实施 TDD 以确保在代码之前编写测试，从而产生设计更好、更可测试且可靠的软件。
  - **结对编程**：将测试人员与开发人员结对，以增强理解并改进[test coverage](../T/test-coverage.md)。这种合作还有助于及早发现潜在问题。
  - **自动化[Regression Testing](../R/regression-testing.md)**：投资强大的自动化回归套件，以快速验证新更改不会对现有功能产生不利影响。
  - **确定测试优先级**：专注于提供最重要风险覆盖的高价值测试。使用[risk-based testing](../R/risk-based-testing.md) 确定[test cases](../T/test-case.md) 的优先级。
  - **持续集成 (CI)**：将测试集成到 CI 管道中，以确保立即反馈应用程序的运行状况。
  - **可扩展[Test Environments](../T/test-environment.md)**：使用容器化和虚拟化根据需要快速设置和拆除[test environments](../T/test-environment.md)。
  - **[Performance Testing](../P/performance-testing.md)**：在开发周期的早期纳入[performance testing](../P/performance-testing.md)，以便在问题升级之前检测并解决问题。
  - **反馈循环**：建立简短的反馈循环，将调查结果快速传达给开发团队，从而能够迅速采取行动。
  - **冲刺回顾**：利用回顾来反思测试过程并确定需要改进的领域。
  通过实施这些策略，[Agile Testing](../A/agile-testing.md) 可以变得更加高效、有效，并与敏捷软件开发的动态本质保持一致。

- **拥抱变化**：敏捷就是适应变化。使用**重构**来保持测试代码可维护并适应应用程序中的频繁更改。
  - **持续学习**：随时了解最新的测试技术和工具。鼓励团队内部的知识共享，以培养集体专业知识。
  - **[Test-Driven Development](../T/test-driven-development.md) (TDD)**：实施 TDD 以确保在代码之前编写测试，从而产生设计更好、更可测试且可靠的软件。
  - **结对编程**：将测试人员与开发人员结对，以增强理解并改进[test coverage](../T/test-coverage.md)。这种合作还有助于及早发现潜在问题。
  - **自动化[Regression Testing](../R/regression-testing.md)**：投资强大的自动化回归套件，以快速验证新更改不会对现有功能产生不利影响。
  - **确定测试优先级**：专注于提供最重要风险覆盖的高价值测试。使用[risk-based testing](../R/risk-based-testing.md) 确定[test cases](../T/test-case.md) 的优先级。
  - **持续集成 (CI)**：将测试集成到 CI 管道中，以确保立即反馈应用程序的运行状况。
  - **可扩展[Test Environments](../T/test-environment.md)**：使用容器化和虚拟化根据需要快速设置和拆除[test environments](../T/test-environment.md)。
  - **[Performance Testing](../P/performance-testing.md)**：在开发周期的早期纳入[performance testing](../P/performance-testing.md)，以便在问题升级之前检测并解决问题。
  - **反馈循环**：建立简短的反馈循环，将调查结果快速传达给开发团队，从而能够迅速采取行动。
  - **冲刺回顾**：利用回顾来反思测试过程并确定需要改进的领域。

#### 有效敏捷测试的最佳实践有哪些？

有效[Agile Testing](../A/agile-testing.md) 的最佳实践包括：

- **密切合作**
    与开发人员、业务分析师和产品所有者一起确保对需求的共同理解并促进快速反馈循环。

- **优先测试**
    基于商业价值和风险。专注于可能显着影响用户体验的高影响领域。

- **编写自动化测试**
    在代码开发的同时，而不是之后。这确保了新功能的立即验证。

- **保持干净[test suite](../T/test-suite.md)**
    通过定期重构测试并删除过时或冗余的测试。

- **实施[Test-Driven Development](../T/test-driven-development.md) (TDD)**
    或行为驱动开发 (BDD) 在实际代码之前创建测试，确保代码从一开始就满足要求。

- **使用持续集成 (CI)**
    自动对新代码提交运行测试，尽早发现问题。

- **尽早且经常测试**
    当缺陷更容易修复且成本更低时识别缺陷。

- **让测试成为每个人的责任**
    ，不仅仅是测试人员。鼓励开发人员编写单元测试并参与测试计划。

- **利用结对编程**
    或 mob 编程来提高质量并共享有关系统和测试的知识。

- **调整和发展您的测试策略**
    基于反馈和项目不断变化的需求。

- **明智地使用指标**
    衡量测试工作的有效性并指导改进。
  通过遵循这些实践，敏捷团队可以确保测试成为开发过程中不可或缺的一部分，从而获得更高质量的软件和更高效的交付。

- **密切合作**
    与开发人员、业务分析师和产品所有者一起确保对需求的共同理解并促进快速反馈循环。

- **优先测试**
    基于商业价值和风险。专注于可能显着影响用户体验的高影响领域。

- **编写自动化测试**
    在代码开发的同时，而不是之后。这确保了新功能的立即验证。

- **保持干净[test suite](../T/test-suite.md)**
    通过定期重构测试并删除过时或冗余的测试。

- **实施[Test-Driven Development](../T/test-driven-development.md) (TDD)**
    或行为驱动开发 (BDD) 在实际代码之前创建测试，确保代码从一开始就满足要求。

- **使用持续集成 (CI)**
    自动对新代码提交运行测试，尽早发现问题。

- **尽早且经常测试**
    当缺陷更容易修复且成本更低时识别缺陷。

- **让测试成为每个人的责任**
    ，不仅仅是测试人员。鼓励开发人员编写单元测试并参与测试计划。

- **利用结对编程**
    或 mob 编程来提高质量并共享有关系统和测试的知识。

- **调整和发展您的测试策略**
    基于反馈和项目不断变化的需求。

- **明智地使用指标**
    衡量测试工作的有效性并指导改进。

#### 敏捷测试如何随着时间的推移而改进？

随着时间的推移，改进[Agile Testing](../A/agile-testing.md)需要持续的反馈循环和适应。 **频繁的回顾**至关重要，让团队能够反思哪些是有效的，哪些是无效的。在这些会议期间，讨论测试策略、工具有效性和协作问题。
  **测试指标**应仔细选择和监控，以跟踪进度并确定需要改进的领域。缺陷密度、[test coverage](../T/test-coverage.md) 和周期时间等指标可以深入了解测试过程的效率和有效性。
  **[Test automation](../T/test-automation.md)** 是持续改进的关键领域。定期审查和重构自动化套件，以确保其保持可靠和可维护。结合**[shift-left testing](../S/shift-left-testing.md)** 实践来更早地检测问题，减少修复[bugs](../B/bug.md) 的成本和工作量。
  **[Pair testing](../P/pair-testing.md)** 可以促进知识共享并改进[test coverage](../T/test-coverage.md)。将测试人员与开发人员或其他测试人员配对可以带来不同的观点并增强[test scenarios](../T/test-scenario.md)。
  **跨职能培训**有助于创建一支能够处理各种任务的多才多艺的团队。鼓励团队成员互相学习，无论是测试、开发还是领域知识。
  **使用新工具和技术进行实验**可以带来改进。但是，请确保任何新工具都能与现有工作流程良好集成并真正增加价值。
  最后，保持**以用户为中心**。定期收集用户反馈并将其纳入测试过程，以确保产品满足用户的真实需求和期望。
