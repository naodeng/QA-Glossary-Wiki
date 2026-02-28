# 软件测试

<!-- TOC START -->
- [有关软件测试的问题吗？](#有关软件测试的问题吗？)
  - [基础知识和重要性](#基础知识和重要性)
    - [为什么软件测试很重要？](#为什么软件测试很重要？)
    - [软件测试有哪些不同级别？](#软件测试有哪些不同级别？)
    - [软件测试员的角色是什么？](#软件测试员的角色是什么？)
    - [质量保证和测试有什么区别？](#质量保证和测试有什么区别？)
  - [测试技术](#测试技术)
    - [白盒测试和黑盒测试有什么区别？](#白盒测试和黑盒测试有什么区别？)
    - [什么是灰盒测试？](#什么是灰盒测试？)
    - [什么是探索性测试？](#什么是探索性测试？)
    - [功能测试和非功能测试有什么区别？](#功能测试和非功能测试有什么区别？)
  - [测试工具和自动化](#测试工具和自动化)
    - [什么是自动化测试？](#什么是自动化测试？)
    - [自动化测试有什么好处？](#自动化测试有什么好处？)
    - [自动化测试有哪些流行的工具？](#自动化测试有哪些流行的工具？)
    - [Selenium 和 QTP 有什么区别？](#selenium-和-qtp-有什么区别？)
    - [Jenkins 在测试中的作用是什么？](#jenkins-在测试中的作用是什么？)
  - [测试管理](#测试管理)
    - [什么是测试用例？](#什么是测试用例？)
    - [什么是测试计划？](#什么是测试计划？)
    - [什么是测试套件？](#什么是测试套件？)
    - [什么是缺陷管理？](#什么是缺陷管理？)
    - [测试经理的角色是什么？](#测试经理的角色是什么？)
  - [高级概念](#高级概念)
    - [什么是性能测试？](#什么是性能测试？)
    - [什么是负载测试？](#什么是负载测试？)
    - [什么是可用性测试？](#什么是可用性测试？)
<!-- TOC END -->

软件测试

确认软件产品或应用程序正常运行、实现其预期目标并且没有缺陷。

## 有关软件测试的问题吗？

### 基础知识和重要性

#### 什么是软件测试？

[Software testing](../S/software-testing.md) 是**评估**和**验证**软件应用程序或系统是否执行其应执行的操作的过程。测试的目的可以是质量保证、功能@@PR​​OTECTED_32@@、性能评估或发现缺陷。测试涉及执行软件组件或系统组件以评估一个或多个感兴趣的属性。
  在 [test automation](../T/test-automation.md) 上下文中，[software testing](../S/software-testing.md) 通常指的是在将软件应用程序发布到生产环境之前使用**自动化工具和框架**对软件应用程序执行预先编写脚本的测试。自动化测试的范围可以从验证单个功能的简单单元测试到验证集成系统工作流程的复杂端到端测试。
  [automated testing](../A/automated-testing.md) 的目标是**提高效率**、**减少[test execution](../T/test-execution.md) 时间**，并提供**一致的[test coverage](../T/test-coverage.md)**。它对于[regression testing](../R/regression-testing.md) 特别有用，它确保新的更改不会给现有功能引入新的缺陷。自动化测试可以频繁运行，并且可以集成到持续集成和部署管道中，从而可以及早发现问题并更快地向开发人员提供反馈。

  ```
  // Example of a simple automated test case in TypeScript
  describe('Login Functionality', () => {
    it('should authenticate user with valid credentials', () => {
      const result = login('validUser', 'validPassword');
      expect(result).toBe(true);
    });
  });
  ```[Automated testing](../A/automated-testing.md) 需要仔细的规划和设计才能有效，并应随着软件的发展进行维护，以确保持续的相关性和有效性。

#### 为什么软件测试很重要？

[Software testing](../S/software-testing.md) 至关重要，因为它确保软件在部署给用户之前**正确**、**安全**和**高效**地运行。它可以识别开发阶段可能引入的缺陷和错误，从而提高软件的**质量**和**用户体验**。测试还验证软件要求是否得到满足，并有助于保持不同设备和平台之间的**一致性**。
  此外，测试对于**风险管理**至关重要，因为它可以防止现实操作中代价高昂且具有潜在危险的故障。从长远来看，它还可以通过尽早发现问题来节省成本，从而减少发布后对补丁和大量维护的需求。
  在**法规遵从性**的背景下，某些行业要求软件在发布之前满足特定标准。测试可确保合规性并避免因发布不合规软件而可能出现的法律问题。
  最后，在竞争激烈的市场中，公司的**声誉**可能会受到其软件产品质量的显着影响。有效的测试有助于通过提供可靠且高性能的产品来建立客户信任和忠诚度。
  总之，[software testing](../S/software-testing.md) 是软件开发生命周期中不可或缺的一部分，有助于交付高质量的软件，从而提高客户满意度、降低成本和强大的市场声誉。

#### 软件测试有哪些不同级别？

不同级别的[software testing](../S/software-testing.md) 确保软件的各个方面在开发生命周期的各个阶段都经过检查和验证。这些级别包括：

- **[Unit Testing](../U/unit-testing.md)**：专注于单个组件或代码单元，以验证每个组件或代码单元是否能够单独正常运行。通常，开发人员使用 JUnit 或 [NUnit](../N/nunit.md) 等框架编写和运行这些测试。
  - **[Integration Testing](../I/integration-testing.md)**：测试集成单元或组件之间的交互以检测接口缺陷。这可以使用增量方法（将单元一一组合）或使用存根和驱动程序来完成。
  - **[System Testing](../S/system-testing.md)**：验证完整且完全集成的软件产品，以确保其满足指定的要求。此级别涵盖广泛的测试类型，包括功能测试和非功能测试。
  - **[Acceptance Testing](../A/acceptance-testing.md)**：用于确定系统是否已准备好发布，通常涉及利益相关者或最终用户。它包括根据用户要求验证系统，并且可以细分为 Alpha 和[Beta testing](../B/beta-testing.md) 阶段。
  - **[Regression Testing](../R/regression-testing.md)**：在软件发生更改（如增强、修补或配置更改）后执行，以确保现有功能不受影响。这就是[test automation](../T/test-automation.md) 对于重复运行一组[test cases](../T/test-case.md) 特别有利的地方。
  每个级别都建立在前一个级别的基础上，确保在开发过程中尽早发现并解决问题。 [Test automation](../T/test-automation.md) 可以应用于所有这些级别，以提高效率和可靠性。

- **[Unit Testing](../U/unit-testing.md)**：专注于单个组件或代码单元，以验证每个组件或代码单元是否能够单独正常运行。通常，开发人员使用 JUnit 或 [NUnit](../N/nunit.md) 等框架编写和运行这些测试。
  - **[Integration Testing](../I/integration-testing.md)**：测试集成单元或组件之间的交互以检测接口缺陷。这可以使用增量方法（将单元一一组合）或使用存根和驱动程序来完成。
  - **[System Testing](../S/system-testing.md)**：验证完整且完全集成的软件产品，以确保其满足指定的要求。此级别涵盖广泛的测试类型，包括功能测试和非功能测试。
  - **[Acceptance Testing](../A/acceptance-testing.md)**：用于确定系统是否已准备好发布，通常涉及利益相关者或最终用户。它包括根据用户要求验证系统，并且可以细分为 Alpha 和[Beta testing](../B/beta-testing.md) 阶段。
  - **[Regression Testing](../R/regression-testing.md)**：在软件发生更改（如增强、修补或配置更改）后执行，以确保现有功能不受影响。这就是[test automation](../T/test-automation.md) 对于重复运行一组[test cases](../T/test-case.md) 特别有利的地方。

#### 软件测试员的角色是什么？

**软件测试人员**的角色涉及设计、开发和执行[test cases](../T/test-case.md)，以根据需求验证软件功能。测试人员通过进行不同类型的测试（例如单元、集成、系统和[acceptance testing](../A/acceptance-testing.md)）来确保软件在各种条件下按预期运行。他们负责识别缺陷，将其报告给开发团队，并在实施后验证修复。
  软件测试人员在 **[test automation](../T/test-automation.md)** 过程中也发挥着至关重要的作用。他们使用适合被测应用程序的语言和框架编写自动化脚本。测试人员维护和改进现有的[test automation](../T/test-automation.md)基础设施，确保自动化测试集成到持续集成和交付管道中。他们必须选择适当的工具用于[test case management](../T/test-case-management.md)、缺陷跟踪和报告，以增强测试过程。
  除了技术任务外，测试人员还与开发人员、产品经理和利益相关者合作，了解需求并确保在整个软件开发生命周期中满足质量标准。他们提供有关产品可用性、性能和安全性的宝贵反馈，有助于提高最终产品的整体质量。
  测试人员必须不断更新他们的技能，以跟上不断发展的测试方法和工具。他们应该倡导测试方面的最佳实践，并为软件开发中优先考虑质量的文化的发展做出贡献。

#### 质量保证和测试有什么区别？

[Quality Assurance](../Q/quality-assurance.md) (QA) 和测试是软件开发中密切相关的概念，但它们有不同的目的。
  **QA** 是一个主动的流程，重点是通过确保用于管理和创建可交付成果的流程充分且有效来防止缺陷。它涵盖整个软件开发生命周期，旨在改进开发和测试流程，以便在开发产品时不会出现缺陷。质量保证活动包括流程定义和实施、培训、审核和流程改进计划。
  另一方面，**测试**是一个反应过程，也是 QA 的一个子集。它涉及系统或应用程序的实际执行，旨在查找软件[bugs](../B/bug.md)。测试涉及 [verification](../V/verification.md) 和验证 - 确保软件满足指导其设计和开发的业务和技术要求，并按预期工作。
  本质上，QA 是关于**过程**和**预防**，而测试是关于**产品**和**检测**。质量保证的目的是改进和稳定生产（及其流程），以避免导致缺陷的问题，而测试的目的是识别产品本身的缺陷。测试是更广泛的 QA 流程中的一项关键活动，涉及软件和开发流程的整体 [quality management](../Q/quality-management.md)。

### 测试技术

#### 白盒测试和黑盒测试有什么区别？

[White box testing](../W/white-box-testing.md)，也称为透明、玻璃或[structural testing](../S/structural-testing.md)，涉及测试应用程序的内部结构或工作方式，而不是其功能。在[white box testing](../W/white-box-testing.md) 中，[test cases](../T/test-case.md) 是根据应用程序的内部代码路径、代码结构和软件本身的实现派生的。测试人员需要了解内部代码，通常是具有开发技能的开发人员或测试人员。
  另一方面，[Black box testing](../B/black-box-testing.md) 将软件视为“黑匣子”——不了解内部实现。 [Test cases](../T/test-case.md)是根据软件的规范和要求编写的。 [Black box testing](../B/black-box-testing.md) 专注于使用各种输入测试软件并根据预期结果验证输出。它通常由不需要了解应用程序的编码或内部结构的测试人员执行。
  总之，**[white box testing](../W/white-box-testing.md)** 是基于代码的测试，测试人员需要了解应用程序的内部工作原理，而 **[black box testing](../B/black-box-testing.md)** 是输入/输出驱动的测试，不需要了解代码。两者之间的选择取决于测试目标，[white box testing](../W/white-box-testing.md) 适用于算法测试、安全性和优化，[black box testing](../B/black-box-testing.md) 非常适合验证，[verification](../V/verification.md) 适用于软件行为。

#### 什么是灰盒测试？

[Grey box testing](../G/grey-box-testing.md) 是一种混合方法，结合了 **黑盒** 和 **[white box testing](../W/white-box-testing.md)** 方法的元素。它需要对应用程序的内部工作原理有部分了解，这使得测试人员能够更好地理解系统来设计[test cases](../T/test-case.md)。这种方法在测试 Web 应用程序时特别有用。
  在[grey box testing](../G/grey-box-testing.md) 中，测试人员可以访问详细的设计文档和[database](../D/database.md) 模式，但无法完全查看源代码。他们使用此信息来创建涵盖应用程序的用户界面及其底层结构（例如 [databases](../D/database.md) 和服务器）的测试。
  测试人员可以使用**调试器**或**监控系统**等工具来观察应用程序在[test execution](../T/test-execution.md)期间的行为。这使他们能够识别与数据流和异常处理相关的问题，而仅通过 [black box testing](../B/black-box-testing.md) 无法轻松找到这些问题。
  [Grey box testing](../G/grey-box-testing.md) 对于 **[integration testing](../I/integration-testing.md)**、**[security testing](../S/security-testing.md)** 和 **网络测试** 有效。它有助于识别与数据通信、用户权限和会话管理相关的问题，这对于应用程序的整体安全性和性能至关重要。
  通过利用黑盒和[white box testing](../W/white-box-testing.md) 的优势，[grey box testing](../G/grey-box-testing.md) 可以更全面地了解应用程序的行为和潜在漏洞。对于希望优化[test coverage](../T/test-coverage.md) 和效率的[test automation](../T/test-automation.md) 工程师来说，这是一个战略选择。

#### 什么是静态测试和动态测试？

[Static testing](../S/static-testing.md) 和[dynamic testing](../D/dynamic-testing.md) 是用于检测软件应用程序中的缺陷的两种方法。
  **[Static testing](../S/static-testing.md)** 涉及检查代码、需求或文档，但不执行程序。它通常在开发生命周期的早期阶段完成。技术包括审查、演练、[inspections](../I/inspection.md) 和案头检查。静态分析工具还可用于根据编码标准自动评估代码，发现潜在的[bugs](../B/bug.md)，并确保符合最佳实践。
  另一方面，**[Dynamic testing](../D/dynamic-testing.md)** 需要**执行**。它通过在各种条件下运行软件来验证软件的功能行为。此类测试检查给定输入的正确输出，并在模拟实际使用的环境中执行。 [Dynamic testing](../D/dynamic-testing.md) 可以进一步分为[unit testing](../U/unit-testing.md)、[integration testing](../I/integration-testing.md)、[system testing](../S/system-testing.md) 和[acceptance testing](../A/acceptance-testing.md)。
  两种测试类型是互补的。 [Static testing](../S/static-testing.md) 有助于及早发现问题，从而更具成本效益地修复问题，而 [dynamic testing](../D/dynamic-testing.md) 则可验证软件在压力下的操作行为和性能。结合这两种方法可以确保对软件质量进行更彻底的评估。

#### 什么是探索性测试？

[Exploratory testing](../E/exploratory-testing.md) 是 [software testing](../S/software-testing.md) 的一种方法，强调个人测试人员的个人自由和责任，通过将测试相关的学习、测试设计、[test execution](../T/test-execution.md) 和测试结果解释视为在整个项目中并行运行的相互支持的活动，不断优化其工作质量。它与更传统的脚本化测试形成鲜明对比，在脚本化测试中，[test cases](../T/test-case.md) 是提前设计的，详细指定了要采取的步骤和预期结果。
  在[exploratory testing](../E/exploratory-testing.md) 中，测试人员不受一组预定义[test cases](../T/test-case.md) 的限制，从而使他们能够更有创意、更灵敏地探测软件。他们通过动态设计和执行测试来探索应用程序，并在进展过程中了解系统的行为和风险。当没有规范或规范有限，或者在复杂、不断变化的环境中很难预测软件在所有情况下应如何表现时，这种方法特别有用。
  测试人员利用他们的技能、经验和直觉来发现、调查和了解系统。他们可能会使用工具来协助测试，但[exploratory testing](../E/exploratory-testing.md) 的核心是测试人员积极参与产品，经常记录他们的发现和想法，而不是遵循预先编写的计划。
  [Exploratory testing](../E/exploratory-testing.md) 不是随机测试；这是一个结构化且深思熟虑的过程，依赖于测试人员的智力、创造力以及对在任何特定时刻最重要的检查内容的洞察力。它通常与其他测试方法结合使用，以确保全面的测试过程。

#### 功能测试和非功能测试有什么区别？

[Functional testing](../F/functional-testing.md) 专注于通过测试功能和操作方面来评估系统行为与指定要求的**合规性**。它回答了“该软件是否能完成其应有的功能？”的问题。示例包括单元、集成、系统和[acceptance testing](../A/acceptance-testing.md)。
  另一方面，[Non-functional testing](../N/non-functional-testing.md) 根据[functional requirements](../F/functional-requirements.md) 未涵盖的标准评估系统的**准备情况**。它评估性能、可用​​性、可靠性和安全性等特征。这种形式的测试可以回答诸如“软件性能如何？”之类的问题。或“该软件的安全性如何？”常见类型包括性能、负载、压力、可用性和[security testing](../S/security-testing.md)。
  功能测试验证应用程序的特定操作和响应，而非功能测试则衡量应用程序在各种条件下的整体操作。两者对于确保全面了解软件质量都至关重要。

### 测试工具和自动化

#### 什么是自动化测试？

[Automated testing](../A/automated-testing.md) 是使用软件工具执行 **[test cases](../T/test-case.md)** 的过程，这些软件工具无需手动干预即可在软件应用程序上运行预先编写的测试。该方法用于验证软件产品的功能、可靠性和稳定性。自动化测试可以在一天中的任何时间重复运行，为开发团队提供即时反馈。
  以下是使用假设测试框架的 TypeScript 基本示例：

  ```
  describe('Login Functionality', () => {
    it('should authenticate user with valid credentials', () => {
      const loginPage = new LoginPage();
      loginPage.enterUsername('validUser');
      loginPage.enterPassword('validPass');
      loginPage.submit();
      expect(loginPage.isLoginSuccessful()).toBeTruthy();
    });
  });
  ```在此示例中，编写 **[test script](../T/test-script.md)** 来自动执行测试登录功能的过程。该脚本导航到登录页面，输入有效凭据，提交表单，并验证登录是否成功。
  [Automated testing](../A/automated-testing.md) 对于 **[regression testing](../R/regression-testing.md)** 特别有用，它确保新的更改不会破坏现有功能。它也有利于执行难以手动执行的**复杂[test cases](../T/test-case.md)**，或者需要在多个平台和设备上运行的测试。然而，这并不是灵丹妙药。随着应用程序的发展，自动化测试需要维护，并且最初的设置成本可能很高。

#### 自动化测试有什么好处？

[Automated testing](../A/automated-testing.md) 提供了多项优势，可以显着提高软件开发生命周期的效率和有效性：

- **一致性和准确性**：自动化确保每次都以相同的方式执行测试，从而消除人为错误。
  - **速度**：自动化测试的运行速度比手动测试快得多，从而实现更快的反馈和更快的开发周期。
  - **增加覆盖范围**：自动化可以轻松增加测试的范围和深度，从而提高软件质量。
  - **可重用性**：即使用户界面发生变化，测试脚本也可以在应用程序的不同版本之间重用。
  - **效率**：创建后，自动化测试可以以最小的额外成本运行任意多次。
  - **早期[Bug](../B/bug.md)检测**：自动化测试可以集成到持续集成管道中，从而可以及早检测缺陷。
  - **并行执行**：测试可以在不同的机器上并行运行，减少执行所需的时间。
  - **成本降低**：虽然有初始投资，但随着时间的推移，自动化测试通过减少每个测试周期所需的工作量来降低测试成本。
  - **改进的报告**：自动化工具可以生成详细的日志和报告，提供对测试执行和结果的见解。
  - **更好的资源分配**：自动化使 QA 工程师能够专注于需要人工判断的更复杂的测试任务。
  这些优势有助于实现更加稳健、高效和可靠的软件开发流程，最终带来更高质量的产品。

- **一致性和准确性**：自动化确保每次都以相同的方式执行测试，从而消除人为错误。
  - **速度**：自动化测试的运行速度比手动测试快得多，从而实现更快的反馈和更快的开发周期。
  - **增加覆盖范围**：自动化可以轻松增加测试的范围和深度，从而提高软件质量。
  - **可重用性**：即使用户界面发生变化，测试脚本也可以在应用程序的不同版本之间重用。
  - **效率**：创建后，自动化测试可以以最小的额外成本运行任意多次。
  - **早期[Bug](../B/bug.md) 检测**：自动化测试可以集成到持续集成管道中，从而可以及早检测缺陷。
  - **并行执行**：测试可以在不同的机器上并行运行，减少执行所需的时间。
  - **成本降低**：虽然有初始投资，但随着时间的推移，自动化测试通过减少每个测试周期所需的工作量来降低测试成本。
  - **改进的报告**：自动化工具可以生成详细的日志和报告，提供对测试执行和结果的见解。
  - **更好的资源分配**：自动化使 QA 工程师能够专注于需要人工判断的更复杂的测试任务。

#### 自动化测试有哪些流行的工具？

[automated testing](../A/automated-testing.md) 的热门工具包括：

- **[Selenium](../S/selenium.md)** ：支持多种语言和浏览器的开源工具。它广泛用于 Web 应用程序测试。
  - **Appium**：用于移动应用程序测试的开源工具。它支持 iOS 和 Android 平台。
  - **JUnit**
    和
    **TestNG**：Java 中的单元测试框架。它们提供注释来识别测试方法和各种其他功能来组织测试。

- **[Cypress](../C/cypress.md)** ：在浏览器中运行的基于 JavaScript 的现代端到端测试框架。
  - **[Postman](../P/postman.md)** ：API 测试工具，可轻松创建和执行 API 请求和自动化测试。
  - **Cucumber** ：通过普通语言解析器支持行为驱动开发（BDD），允许用自然语言编写测试脚本。
  - **机器人框架**：用于验收级别测试和验收测试驱动开发（ATDD）的关键字驱动测试自动化框架。
  - **SpecFlow** ：用于 BDD 的 .NET 工具，使用 Gherkin 语言创建人类可读的测试。
  - **HP UFT（以前称为 QTP）**：用于功能和回归测试的商业工具，具有用于测试自动化的可视化界面。
  - **SoapUI**：用于测试 SOAP 和 REST Web 服务的工具，专注于 API 测试。
  - **LoadRunner**：Micro Focus 的性能测试工具，可模拟用户活动以进行负载、压力和可扩展性测试。
  - **[JMeter](../J/jmeter.md)** ：专为负载测试和测量性能而设计的开源工具。
  每个工具都有自己的优势，并根据项目的具体要求进行选择，例如被测应用程序的类型、涉及的编程语言以及首选的测试方法。

- **[Selenium](../S/selenium.md)** ：支持多种语言和浏览器的开源工具。它广泛用于 Web 应用程序测试。
  - **Appium**：用于移动应用程序测试的开源工具。它支持 iOS 和 Android 平台。
  - **JUnit**
    和
    **TestNG**：Java 中的单元测试框架。它们提供注释来识别测试方法和各种其他功能来组织测试。

- **[Cypress](../C/cypress.md)** ：在浏览器中运行的基于 JavaScript 的现代端到端测试框架。
  - **[Postman](../P/postman.md)** ：API 测试工具，可轻松创建和执行 API 请求和自动化测试。
  - **Cucumber** ：通过普通语言解析器支持行为驱动开发（BDD），允许用自然语言编写测试脚本。
  - **机器人框架**：用于验收级别测试和验收测试驱动开发（ATDD）的关键字驱动测试自动化框架。
  - **SpecFlow** ：用于 BDD 的 .NET 工具，使用 Gherkin 语言创建人类可读的测试。
  - **HP UFT（以前称为 QTP）**：用于功能和回归测试的商业工具，具有用于测试自动化的可视化界面。
  - **SoapUI**：用于测试 SOAP 和 REST Web 服务的工具，专注于 API 测试。
  - **LoadRunner**：Micro Focus 的性能测试工具，可模拟用户活动以进行负载、压力和可扩展性测试。
  - **[JMeter](../J/jmeter.md)** ：专为负载测试和测量性能而设计的开源工具。

#### Selenium 和 QTP 有什么区别？

[Selenium](../S/selenium.md) 和 QTP (QuickTest Professional)，现在称为 UFT (Unified [Functional Testing](../F/functional-testing.md))，都是用于测试 Web 应用程序的自动化工具，但它们在几个方面有所不同：

- **开源与商业**：[Selenium](../S/selenium.md) 是一个开源工具，这意味着它可以免费使用并且任何人都可以修改。另一方面，UFT 是 Micro Focus 开发的商业产品，需要付费许可证。
  - **语言支持**：[Selenium](../S/selenium.md) 支持多种编程语言，如 Java、C#、Python、Ruby 和 JavaScript，从而实现[test script](../T/test-script.md) 开发的灵活性。 UFT 主要使用 VBScript。
  - **浏览器兼容性**：[Selenium](../S/selenium.md) 支持多种浏览器，包括 Chrome、Firefox、Internet Explorer、Safari 和 Opera。 UFT 的浏览器支持更为有限。
  - **操作系统支持**：[Selenium](../S/selenium.md)可以在Windows、macOS和Linux等各种操作系统上运行。 UFT 主要限于 Windows。
  - **与其他工具集成**：[Selenium](../S/selenium.md) 可以轻松地与 Jenkins for CI/CD 等其他工具集成，并且可以与 TestNG 或 JUnit 等各种框架一起使用。 UFT 具有内置集成功能，但可能无法提供相同级别的灵活性。
  - **社区和支持**：[Selenium](../S/selenium.md) 是开源的，拥有一个庞大的支持和协作社区。 UFT 是专有的，依赖于 Micro Focus 的官方支持，并且可能拥有较小的用户社区。
  - **IDE 支持**：[Selenium](../S/selenium.md) 有一个用于浏览器的 IDE 插件，用于录制和播放功能，而 UFT 则配备了成熟的 IDE。
  - **移动测试**：[Selenium](../S/selenium.md) 可以扩展到使用 Appium 的移动测试。 UFT 有一个姊妹工具 UFT Mobile，用于移动测试。
  总之，[Selenium](../S/selenium.md) 和 UFT 之间的选择可能取决于预算、语言偏好、浏览器支持以及对强大商业支持结构的需求等因素。

- **开源与商业**：[Selenium](../S/selenium.md) 是一个开源工具，这意味着它可以免费使用并且任何人都可以修改。另一方面，UFT 是 Micro Focus 开发的商业产品，需要付费许可证。
  - **语言支持**：[Selenium](../S/selenium.md) 支持多种编程语言，如 Java、C#、Python、Ruby 和 JavaScript，从而实现[test script](../T/test-script.md) 开发的灵活性。 UFT 主要使用 VBScript。
  - **浏览器兼容性**：[Selenium](../S/selenium.md) 支持多种浏览器，包括 Chrome、Firefox、Internet Explorer、Safari 和 Opera。 UFT 的浏览器支持更为有限。
  - **操作系统支持**：[Selenium](../S/selenium.md)可以在Windows、macOS和Linux等各种操作系统上运行。 UFT 主要限于 Windows。
  - **与其他工具集成**：[Selenium](../S/selenium.md) 可以轻松地与 Jenkins for CI/CD 等其他工具集成，并且可以与 TestNG 或 JUnit 等各种框架一起使用。 UFT 具有内置集成功能，但可能无法提供相同级别的灵活性。
  - **社区和支持**：[Selenium](../S/selenium.md) 是开源的，拥有一个庞大的支持和协作社区。 UFT 是专有的，依赖于 Micro Focus 的官方支持，并且可能拥有较小的用户社区。
  - **IDE 支持**：[Selenium](../S/selenium.md) 有一个用于浏览器的 IDE 插件，用于录制和播放功能，而 UFT 则配备了成熟的 IDE。
  - **移动测试**：[Selenium](../S/selenium.md) 可以扩展到使用 Appium 的移动测试。 UFT 有一个姊妹工具 UFT Mobile，用于移动测试。

#### Jenkins 在测试中的作用是什么？

Jenkins 在**持续集成（CI）**和**持续交付（CD）**管道中发挥着至关重要的作用，自动执行[test suites](../T/test-suite.md)并提供有关软件运行状况的即时反馈。它可以配置为触发对各种事件的测试，例如提交到版本控制系统或按计划进行。
  使用詹金斯，您可以：

- **自动化[test execution](../T/test-execution.md)** ：对代码更改自动运行测试以快速识别问题。
  - **并行化测试**：并行执行测试以减少测试套件运行所需的时间。
  - **管理[test environments](../T/test-environment.md)**：作为管道的一部分设置和拆除测试环境。
  - **与[test tools](../T/test-tool.md)**集成：使用插件与各种测试框架和工具连接。
  - **可视化测试结果**：生成报告和仪表板来分析测试结果。
  - **通知利益相关者**：向开发人员和团队发送有关测试结果的通知。
  用于运行测试的 Jenkins 管道脚本示例：

  ```
  pipeline {
      agent any
      stages {
          stage('Build') {
              steps {
                  // Build your application
              }
          }
          stage('Test') {
              steps {
                  // Run your test suite
                  sh 'execute-tests.sh'
              }
              post {
                  always {
                      // Collect and archive test reports
                      junit '**/target/surefire-reports/TEST-*.xml'
                  }
              }
          }
      }
  }
  ```从本质上讲，Jenkins 通过自动化来增强测试过程，从而确保持续评估 [software quality](../S/software-quality.md) 并及时检测和解决问题。

- **自动化[test execution](../T/test-execution.md)** ：对代码更改自动运行测试以快速识别问题。
  - **并行化测试**：并行执行测试以减少测试套件运行所需的时间。
  - **管理[test environments](../T/test-environment.md)**：作为管道的一部分设置和拆除测试环境。
  - **与[test tools](../T/test-tool.md)**集成：使用插件与各种测试框架和工具连接。
  - **可视化测试结果**：生成报告和仪表板来分析测试结果。
  - **通知利益相关者**：向开发人员和团队发送有关测试结果的通知。

### 测试管理

#### 什么是测试用例？

**[test case](../T/test-case.md)** 是一组条件或变量，测试人员将在这些条件或变量下确定应用程序或软件系统是否正常工作。它本质上是一个特定场景，由一系列步骤、[expected results](../E/expected-result.md) 和[actual results](../A/actual-result.md) 组成，旨在验证软件的特定功能或特性。
  每个[test case](../T/test-case.md) 包括：

- **[Test Case](../T/test-case.md) ID**：用于跟踪的唯一标识符。
  - **描述**：关于正在测试的内容的简介。
  - **先决条件**：执行之前必须满足的任何要求。
  - **测试步骤**：详细的执行说明。
  - **[Expected Result](../E/expected-result.md)** ：软件正常运行时的预期结果。
  - **[Actual Result](../A/actual-result.md)** ：执行测试时观察到的行为。
  - **[Postconditions](../P/postcondition.md)** ：测试执行后系统的状态。
  - **状态**：通过或失败取决于实际结果是否与预期结果匹配。
  [Test cases](../T/test-case.md) 是手册和[automated testing](../A/automated-testing.md) 的基础，为测试人员验证软件功能提供了清晰的框架。在[automated testing](../A/automated-testing.md)、[test cases](../T/test-case.md)中，使用特定于测试环境的工具和语言编写脚本，例如[Selenium](../S/selenium.md)使用Java或Python，并且可以重复执行而无需人工干预。

  ```
  // Example of a simple automated test case in TypeScript using a testing framework
  describe('Login Functionality', () => {
    it('should log in with valid credentials', () => {
      browser.url('https://example.com/login');
      $('#username').setValue('testuser');
      $('#password').setValue('testpass');
      $('#login').click();
      expect(browser).toHaveUrl('https://example.com/dashboard');
    });
  });
  ```精心设计的[test cases](../T/test-case.md) 对于有效[test coverage](../T/test-coverage.md) 并确保软件满足其要求至关重要。

- **[Test Case](../T/test-case.md) ID**：用于跟踪的唯一标识符。
  - **描述**：关于正在测试的内容的简介。
  - **先决条件**：执行之前必须满足的任何要求。
  - **测试步骤**：详细的执行说明。
  - **[Expected Result](../E/expected-result.md)** ：软件正常运行时的预期结果。
  - **[Actual Result](../A/actual-result.md)** ：执行测试时观察到的行为。
  - **[Postconditions](../P/postcondition.md)** ：测试执行后系统的状态。
  - **状态**：通过或失败取决于实际结果是否与预期结果匹配。

#### 什么是测试计划？

**[test plan](../T/test-plan.md)** 是一份正式文件，详细说明了预期测试活动的策略、资源、范围和时间表。它定义了项目内测试阶段的目标和里程碑，并作为行动的蓝图。 [test plan](../T/test-plan.md) 通常包括：

- **测试目标**：测试应实现的明确目标。
  - **测试范围**：要测试的功能和要排除的功能。
  - **[Test strategy](../T/test-strategy.md)** ：测试采用的高级方法。
  - **资源分配**：分配测试执行的人员和工具。
  - **[Test environment](../T/test-environment.md)** ：将执行测试的硬件和软件的规格。
  - **测试时间表**：测试准备、执行和评估的时间表。
  - **风险分析**：测试过程中的潜在风险和缓解计划。
  - **进入和退出标准**：开始和结束测试阶段必须满足的条件。
  - **可交付成果**：要生成的工件，例如测试用例、报告和缺陷日志。
  它是一个指南，使测试团队的工作与项目目标保持一致，并确保软件的关键方面得到系统验证。精心设计的[test plan](../T/test-plan.md) 对于高效[test management](../T/test-management.md) 至关重要，并可作为整个测试过程的参考点。

- **测试目标**：测试应实现的明确目标。
  - **测试范围**：要测试的功能和要排除的功能。
  - **[Test strategy](../T/test-strategy.md)** ：测试采用的高级方法。
  - **资源分配**：分配测试执行的人员和工具。
  - **[Test environment](../T/test-environment.md)** ：将执行测试的硬件和软件的规格。
  - **测试时间表**：测试准备、执行和评估的时间表。
  - **风险分析**：测试过程中的潜在风险和缓解计划。
  - **进入和退出标准**：开始和结束测试阶段必须满足的条件。
  - **可交付成果**：要生成的工件，例如测试用例、报告和缺陷日志。

#### 什么是测试套件？

**[test suite](../T/test-suite.md)** 是 **[test cases](../T/test-case.md)** 的集合，它们组合在一起以测试软件应用程序或应用程序中的特定功能。在[automated testing](../A/automated-testing.md) 中，[test suite](../T/test-suite.md) 可以由[test runner](../T/test-runner.md) 执行，并且通常以允许批量执行多个测试的方式构建。它充当逻辑上相关的测试的容器，无论是按测试目的（例如功能集）还是按级别（例如集成或[system testing](../S/system-testing.md)）。
  [Test suites](../T/test-suite.md) 通常按层次结构组织，套件位于顶层，各个[test cases](../T/test-case.md) 或更小的套件位于其下方。这可以更好地管理和执行测试以及聚合测试结果。 [Test suites](../T/test-suite.md) 可以设计为作为持续集成 (CI) 管道的一部分运行，从而能够定期反馈代码库的运行状况。
  在代码中，[test suite](../T/test-suite.md) 可能表示为类或模块，具体取决于所使用的编程语言和测试框架。例如，在像 JUnit 这样的基于 Java 的框架中，[test suite](../T/test-suite.md) 可以用 `@RunWith(Suite.class)` 进行注释，并包含要运行的测试类的列表：

  ```
  @RunWith(Suite.class)
  @Suite.SuiteClasses({
      TestClassOne.class,
      TestClassTwo.class
  })
  public class ExampleTestSuite {
      // This class remains empty, it is used only as a holder for the above annotations
  }
  ```[Test suites](../T/test-suite.md) 对于组织和维护大量自动化测试至关重要，使它们更具可维护性和可扩展性。它们还有助于有针对性的测试，并可用于对特定测试运行的测试进行分组，例如冒烟测试或[regression testing](../R/regression-testing.md)。

#### 什么是缺陷管理？

[Defect management](../D/defect-management.md) 是识别、记录、跟踪和解决软件产品缺陷的系统过程。它从发现缺陷开始，一直持续到缺陷被修复和验证或被认为不相关并被驳回。有效的[defect management](../D/defect-management.md) 涉及几个关键步骤：

- **识别**：通过测试或用户反馈识别缺陷。
  - **文档**：足够详细地记录缺陷，包括重现步骤、严重性和潜在影响。
  - **优先级**：评估缺陷的紧迫性和重要性，以确定缺陷的解决顺序。
  - **分配**：将缺陷分配给适当的团队或个人来解决。
  - **解决方案**：通过代码更改或配置调整来纠正缺陷。
  - **[Verification](../V/verification.md)** ：测试修复以确保缺陷得到解决并且没有引入新问题。
  - **关闭**：一旦验证并满足验收标准，就正式关闭缺陷。
  在整个过程中，团队成员之间的沟通与协作至关重要。 [Defect management](../D/defect-management.md) 工具通过提供用于跟踪和管理缺陷的集中平台来促进这一点。这些工具通常与其他软件开发和测试工具集成，从而实现从缺陷发现到解决的无缝工作流程。
  在 [test automation](../T/test-automation.md) 的背景下，[defect management](../D/defect-management.md) 确保自动化测试在捕获回归方面保持有效，并且及时解决代码更改引入的任何新缺陷，从而保持软件的整体质量和可靠性。

- **识别**：通过测试或用户反馈识别缺陷。
  - **文档**：足够详细地记录缺陷，包括重现步骤、严重性和潜在影响。
  - **优先级**：评估缺陷的紧迫性和重要性，以确定缺陷的解决顺序。
  - **分配**：将缺陷分配给适当的团队或个人来解决。
  - **解决方案**：通过代码更改或配置调整来纠正缺陷。
  - **[Verification](../V/verification.md)** ：测试修复以确保缺陷得到解决并且没有引入新问题。
  - **关闭**：一旦验证并满足验收标准，就正式关闭缺陷。

#### 测试经理的角色是什么？

**测试经理**在监督测试过程并确保软件符合质量标准方面发挥着至关重要的作用。他们的职责包括：

- **制定策略**
    总体测试方法和方法。

- **规划**
    和
    **日程安排**
    测试活动，确保资源得到有效分配。

- **管理**
    测试团队，包括招聘、培训和指导测试人员。

- **协调**
    与其他团队（例如开发和运营）合作，以确保软件开发生命周期内测试的一致性和集成。

- **监控**
    和
    **报告**
    关于测试进度、测试覆盖率和缺陷状态。

- **风险管理**
    ，识别潜在的质量问题并采取积极措施来缓解这些问题。

- **预算**
    用于测试活动，包括工具、环境和人员。

- **确保**
    符合行业标准和监管要求。

- **评估**
    和
    **实施**
    提高测试效率和有效性的测试工具和技术。

- **维护**
    和
    **改进**
    测试环境和基础设施。
  测试经理必须深入了解[software testing](../S/software-testing.md) 原则和实践，以及强大的领导和沟通技巧，以有效指导其团队并与利益相关者互动。他们通过确保正确的流程、工具和人员到位来交付高质量的软件，在 [test automation](../T/test-automation.md) 工作的成功中发挥着关键作用。

- **制定策略**
    总体测试方法和方法。

- **规划**
    和
    **日程安排**
    测试活动，确保资源得到有效分配。

- **管理**
    测试团队，包括招聘、培训和指导测试人员。

- **协调**
    与其他团队（例如开发和运营）合作，以确保软件开发生命周期内测试的一致性和集成。

- **监控**
    和
    **报告**
    关于测试进度、测试覆盖率和缺陷状态。

- **风险管理**
    ，识别潜在的质量问题并采取积极措施来缓解这些问题。

- **预算**
    用于测试活动，包括工具、环境和人员。

- **确保**
    符合行业标准和监管要求。

- **评估**
    和
    **实施**
    提高测试效率和有效性的测试工具和技术。

- **维护**
    和
    **改进**
    测试环境和基础设施。

### 高级概念

#### 什么是性能测试？

[Performance testing](../P/performance-testing.md) 是 [non-functional testing](../N/non-functional-testing.md) 的一种类型，用于评估系统在各种条件下的性能。它主要关注软件应用程序的**速度**、**可扩展性**、**可靠性**和**资源使用**。性能测试旨在模拟不同的场景，包括高用户负载、有限的计算资源和大数据输入/输出，以识别潜在的瓶颈并确保软件满足性能标准。
  [performance testing](../P/performance-testing.md) 的主要子类型包括：

- **[Load Testing](../L/load-testing.md)** ：确定系统在预期用户负载下的行为方式。
  - **[Stress Testing](../S/stress-testing.md)** ：评估极端条件下的系统稳定性。
  - **[Endurance Testing](../E/endurance-testing.md)** ：检查长时间内正常工作负载下的系统性能。
  - **峰值测试**：评估系统对用户负载突然大幅峰值的反应。
  - **[Volume Testing](../V/volume-testing.md)** ：测试系统处理大量数据的能力。
  - **[Scalability Testing](../S/scalability-testing.md)** ：确定系统是否可以纵向扩展或横向扩展以及对性能的影响。
  [Performance testing](../P/performance-testing.md) 工具通常提供响应时间、吞吐率和资源利用率水平等指标，这有助于识别与性能相关的问题。常见工具包括 **Apache [JMeter](../J/jmeter.md)**、**LoadRunner** 和 **Gadling**。

  ```
  // Example of a simple JMeter test plan snippet
  ThreadGroup num_threads=50 ramp_up=10s {
      HTTPSampler domain="www.example.com" path="/api/test" method="GET"
  }
  ```[Performance testing](../P/performance-testing.md) 对于验证软件能否在预期工作负载及超出预期工作负载下良好运行、确保良好的用户体验和系统可靠性至关重要。

- **[Load Testing](../L/load-testing.md)** ：确定系统在预期用户负载下的行为方式。
  - **[Stress Testing](../S/stress-testing.md)** ：评估极端条件下的系统稳定性。
  - **[Endurance Testing](../E/endurance-testing.md)** ：检查长时间内正常工作负载下的系统性能。
  - **峰值测试**：评估系统对用户负载突然大幅峰值的反应。
  - **[Volume Testing](../V/volume-testing.md)** ：测试系统处理大量数据的能力。
  - **[Scalability Testing](../S/scalability-testing.md)** ：确定系统是否可以纵向扩展或横向扩展以及对性能的影响。

#### 什么是负载测试？

[Load testing](../L/load-testing.md) 是 **[non-functional testing](../N/non-functional-testing.md)** 的一种类型，用于评估系统在给定时间内在预期负载下的性能。主要目标是在软件应用程序上线之前识别性能瓶颈。
  在[load testing](../L/load-testing.md)期间，系统会受到不断增加的请求量的影响，直到达到其指定容量的阈值。测量响应时间、吞吐量和资源利用率等关键指标，以确保应用程序可以处理高流量而不降低性能。
  [Load testing](../L/load-testing.md) 工具，例如 Apache [JMeter](../J/jmeter.md) 或 LoadRunner，模拟多个用户同时访问应用程序。这些工具可以深入了解系统在压力下的行为方式，并有助于调整性能。
  区分 [load testing](../L/load-testing.md) 和 **[stress testing](../S/stress-testing.md)** 至关重要。 [load testing](../L/load-testing.md) 检查系统在预期负载条件下的性能，[stress testing](../S/stress-testing.md) 则将系统推向极限以了解其如何处理极端条件。
  总之，[load testing](../L/load-testing.md) 对于验证应用程序能否满足其性能目标并在峰值负载条件下提供良好的用户体验至关重要。这是确保应用程序健壮、可靠并准备好发布的关键步骤。

#### 什么是压力测试？

[Stress testing](../S/stress-testing.md) 是 **[non-functional testing](../N/non-functional-testing.md)** 的一种，用于评估系统在极端条件下的性能。它涉及使系统承受超出其正常运行能力的负载和要求，以确定其在高应力下的行为并确定其断裂点。目标是确保系统保持可靠并优雅地失败，为其**阈值和限制**提供有价值的见解。
  在[stress testing](../S/stress-testing.md)期间，各种参数可能会达到极限，例如：

- **CPU使用率**
  - **内存消耗**
  - **磁盘 I/O**
  - **网络流量**
  这种形式的测试可以揭示在正常情况下可能不会出现的**同步问题**、**竞争条件**和**内存泄漏**。这对于**关键应用程序**尤其重要，因为停机可能会导致重大问题或成本。
  自动化工具通常用于模拟高压力条件，并分析结果以识别系统中任何潜在的瓶颈或弱点。这些信息对于开发人员在系统上线前优化系统性能和稳定性至关重要。
  总之，[stress testing](../S/stress-testing.md) 旨在将系统推向极限，以确保其能够承受极端条件，并发现可能损害其性能和可靠性的潜在故障点。

- **CPU使用率**
  - **内存消耗**
  - **磁盘 I/O**
  - **网络流量**

#### 什么是可用性测试？

[Usability testing](../U/usability-testing.md) 是一种通过对用户进行测试来评估产品的技术。这种形式的测试对于衡量软件应用程序的直观性和用户友好性至关重要。它涉及观察真实用户尝试完成产品任务并识别任何可用性问题、收集定性和定量数据以及确定参与者对产品的满意度。
  与其他可能关注功能正确性的测试方法不同，[usability testing](../U/usability-testing.md) 关注用户体验方面。它旨在揭示如何改进软件以提供更好的用户体验，其中包括确保界面易于导航、易于查找信息以及产品易于使用。
  在[usability testing](../U/usability-testing.md)期间，参与者通常被要求执行一系列任务，而观察者则观看、聆听和做笔记。目标是识别用户面临的任何困惑或问题，这可能会导致沮丧或错误。
  [usability testing](../U/usability-testing.md)期间经常评估的关键指标包括：

- **任务成功率**：用户是否能够成功完成任务。
  - **错误率**：用户犯错误的频率以及这些错误的严重性。
  - **任务完成时间**：用户完成任务需要多长时间。
  - **用户满意度**：用户对与产品交互的感受如何。
  [Usability testing](../U/usability-testing.md) 可以在开发的各个阶段进行，从早期原型到最终产品，从而实现迭代改进。它是以用户为中心的设计的重要组成部分，有助于确保软件满足预期用户的需求和期望。

- **任务成功率**：用户是否能够成功完成任务。
  - **错误率**：用户犯错误的频率以及这些错误的严重性。
  - **任务完成时间**：用户完成任务需要多长时间。
  - **用户满意度**：用户对与产品交互的感受如何。

#### 什么是安全测试？

[Security testing](../S/security-testing.md) 是一个旨在发现软件中可能导致安全漏洞的漏洞、威胁和风险的过程。其目标是确保软件系统即使在面临恶意攻击或其他安全威胁时也能够按预期保护数据并维持功能。
  [security testing](../S/security-testing.md) 的关键方面包括：

- **[Verification](../V/verification.md) 身份验证和授权**
    确保用户身份真实且拥有适当访问权限的机制。

- **数据加密验证**
    在存储和传输过程中保护敏感信息。

- **软件和基础设施评估**
    使用漏洞扫描器等工具查找已知漏洞。

- **[Penetration testing](../P/penetration-testing.md)**
    ，它模拟攻击以识别可利用的弱点。

- **安全代码审查**
    检测特定于安全的编码缺陷。

- **配置和部署管理测试**
    以确保安全的部署设置。
  [Security testing](../S/security-testing.md) 在开发生命周期中至关重要，应集成到持续集成/持续部署 (CI/CD) 管道中。自动化 [security testing](../S/security-testing.md) 工具，例如静态应用程序 [security testing](../S/security-testing.md) (SAST)、动态应用程序 [security testing](../S/security-testing.md) (DAST) 和交互式应用程序 [security testing](../S/security-testing.md) (IAST)，可用于尽早且频繁地识别安全问题。
  总之，[security testing](../S/security-testing.md) 可防止未经授权的访问和数据泄露，确保软件系统的机密性、完整性和可用性。

- **[Verification](../V/verification.md) 身份验证和授权**
    确保用户身份真实且拥有适当访问权限的机制。

- **数据加密验证**
    在存储和传输过程中保护敏感信息。

- **软件和基础设施评估**
    使用漏洞扫描器等工具查找已知漏洞。

- **[Penetration testing](../P/penetration-testing.md)**
    ，它模拟攻击以识别可利用的弱点。

- **安全代码审查**
    检测特定于安全的编码缺陷。

- **配置和部署管理测试**
    以确保安全的部署设置。
