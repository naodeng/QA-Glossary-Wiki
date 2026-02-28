# 功能需求

<!-- TOC START -->
- [有关功能要求的问题吗？](#有关功能要求的问题吗？)
  - [基础知识和重要性](#基础知识和重要性)
    - [功能要求是什么？](#功能要求是什么？)
    - [为什么功能需求在软件开发中很重要？](#为什么功能需求在软件开发中很重要？)
    - [功能性需求与非功能性需求有何不同？](#功能性需求与非功能性需求有何不同？)
    - [功能需求在 e2e 测试中的作用是什么？](#功能需求在-e2e-测试中的作用是什么？)
  - [身份证明和文件](#身份证明和文件)
    - [功能需求如何确定？](#功能需求如何确定？)
    - [记录功能需求的过程是什么？](#记录功能需求的过程是什么？)
    - [用于记录功能需求的常用工具或方法有哪些？](#用于记录功能需求的常用工具或方法有哪些？)
    - [功能需求文档中应包含哪些关键元素？](#功能需求文档中应包含哪些关键元素？)
  - [验证和确认](#验证和确认)
    - [功能需求如何验证和确认？](#功能需求如何验证和确认？)
    - [e2e 测试在功能需求验证中扮演什么角色？](#e2e-测试在功能需求验证中扮演什么角色？)
    - [验证功能需求时存在哪些常见挑战以及如何克服这些挑战？](#验证功能需求时存在哪些常见挑战以及如何克服这些挑战？)
  - [实际应用](#实际应用)
    - [您能否提供一些实际软件应用程序中功能需求的示例？](#您能否提供一些实际软件应用程序中功能需求的示例？)
    - [功能需求在软件项目的生命周期中如何演变？](#功能需求在软件项目的生命周期中如何演变？)
    - [定义功能需求时有哪些常见错误或陷阱以及如何避免它们？](#定义功能需求时有哪些常见错误或陷阱以及如何避免它们？)
<!-- TOC END -->

功能要求

定义软件系统或应用程序的预期行为，指定系统在流程、功能和特性方面应执行的操作。这些要求概述了系统与其用户以及任何其他外部系统或接口之间的交互。它们充当软件生命周期的设计、开发和测试阶段的基础。

## 有关功能要求的问题吗？

### 基础知识和重要性

#### 功能要求是什么？

[Functional requirements](../F/functional-requirements.md) 描述系统应该做什么，详细说明系统必须具备的行为、功能和特性。这些要求源自用户需求、业务目标或监管标准，通常以**用户故事**、**[use cases](../U/use-case.md)** 或**系统要求** 的形式进行阐述。
  为了确保清晰和精确，[functional requirements](../F/functional-requirements.md) 应该是：

- **具体**：明确定义功能或特性，没有歧义。
  - **可衡量**：包括可用于衡量需求满足情况的标准。
  - **可测试**：可通过测试、检查或分析进行验证。
  在[test automation](../T/test-automation.md) 中，[functional requirements](../F/functional-requirements.md) 是设计[test cases](../T/test-case.md) 和脚本的基础。它们指导**自动化测试**的开发，以验证系统在各种条件下是否按预期运行。
  例如，考虑电子商务平台的功能需求：

  ```
  The system shall allow users to add items to their shopping cart.
  ```自动化测试将模拟用户将商品添加到购物车，并验证该商品是否出现在购物车中、数量是否正确以及价格是否相应更新。
  [Functional requirements](../F/functional-requirements.md) 通常使用 **[JIRA](../J/jira.md)**、**Confluence** 或 **Trello** 等工具进行管理，这些工具有助于协作并跟踪随时间的变化。它们对于保持利益相关者之间的一致性并确保最终产品满足预期目的和用户需求至关重要。

- **具体**：明确定义功能或特性，没有歧义。
  - **可衡量**：包括可用于衡量需求满足情况的标准。
  - **可测试**：可通过测试、检查或分析进行验证。

#### 为什么功能需求在软件开发中很重要？

[Functional requirements](../F/functional-requirements.md) 在软件开发中至关重要，因为它们概述了系统应该做什么，指导设计、开发和测试过程。它们提供了对预期行为和功能的清晰理解，确保开发人员和利益相关者在软件目标上保持一致。
  对于[test automation](../T/test-automation.md) 工程师来说，[functional requirements](../F/functional-requirements.md) 是创建 **[test cases](../T/test-case.md)** 和 **脚本** 的基础。它们使工程师能够编写反映用户需求的自动化测试，并确保软件的每个功能按预期执行。如果没有明确定义的[functional requirements](../F/functional-requirements.md)，创建有效且全面的[test suites](../T/test-suite.md) 就具有挑战性，可能会导致[test coverage](../T/test-coverage.md) 中出现空白和未捕获的缺陷。
  此外，[functional requirements](../F/functional-requirements.md) 有助于建立软件的**验收标准**。它们用于衡量软件的完整性并确定它是否准备好发布。在敏捷环境中，[functional requirements](../F/functional-requirements.md) 经常发展，并且自动化测试必须相应地**维护**和**更新**，以保持相关性和有效性。
  总之，[functional requirements](../F/functional-requirements.md) 对于开发高质量软件至关重要，并构成系统高效的[test automation](../T/test-automation.md) 的基础，最终形成满足用户期望并在现实场景中可靠运行的产品。

#### 功能性需求与非功能性需求有何不同？

[Functional requirements](../F/functional-requirements.md) 指定系统应该做什么，详细说明行为、功能和特性。它们描述了用户交互和系统流程，例如“系统应允许用户使用用户名和密码登录”。
  另一方面，非[functional requirements](../F/functional-requirements.md) (NFR) 定义系统应如何执行，重点关注系统属性和质量。它们涵盖性能、安全性、可靠性和可用性等方面。例如，NFR 可能会声明：“系统应处理 1000 个并发用户，而不会降低性能。”
  [functional requirements](../F/functional-requirements.md) 涉及软件的特定操作和功能，而非[functional requirements](../F/functional-requirements.md) 则涉及用户体验和操作特征。 NFR 通常更难测量和验证，因为它们往往不如 [functional requirements](../F/functional-requirements.md) 具体。
  在[test automation](../T/test-automation.md)中，[functional requirements](../F/functional-requirements.md)导致创建[test cases](../T/test-case.md)来验证特定功能，而NFR则指导性能和安全测试等的开发。重要的是要考虑两者，以确保全面的测试策略符合用户期望和系统要求。

#### 功能需求在 e2e 测试中的作用是什么？

在**端到端 (e2e) 测试**中，[functional requirements](../F/functional-requirements.md) 充当创建 [test scenarios](../T/test-scenario.md) 的蓝图，从头到尾模拟应用程序的实际使用情况。它们定义了系统的预期行为，端到端测试必须验证这些行为，以确保应用程序的所有部分按预期协同工作。
  E2e 测试使用这些要求来：

- **设计[test cases](../T/test-case.md)**
    涵盖了应用程序功能的全部范围。

- **确保覆盖范围**
    系统中的用户交互和数据流。

- **验证关键路径**
    用户可能会遵循，确保他们达到指定的结果。

- **检测集成问题**
    单元和集成测试可能会错过，因为 e2e 测试与应用程序及其界面交互，就像用户一样。

- **评估发布准备情况**
    通过确认应用程序在密切反映生产的环境中按预期运行。
  对于自动化工程师来说，[functional requirements](../F/functional-requirements.md) 对于编写 e2e 测试脚本至关重要。它们指导选择适当的自动化工具和框架，并为可维护和可扩展的[test suites](../T/test-suite.md) 设计提供信息。

  ```
  // Example of an e2e test pseudocode based on functional requirements
  describe('User Login Flow', () => {
    it('should allow a user to log in with valid credentials', () => {
      navigateToLoginPage();
      enterCredentials('user@example.com', 'password123');
      submitLoginForm();
      expect(isLoggedIn()).toBe(true);
      expect(getWelcomeMessage()).toContain('Welcome, user!');
    });
  });
  ```通过将 e2e 测试与 [functional requirements](../F/functional-requirements.md) 保持一致，[test automation](../T/test-automation.md) 工程师可确保软件为最终用户提供预期价值并满足业务目标。

- **设计[test cases](../T/test-case.md)**
    涵盖了应用程序功能的全部范围。

- **确保覆盖范围**
    系统中的用户交互和数据流。

- **验证关键路径**
    用户可能会遵循，确保他们达到指定的结果。

- **检测集成问题**
    单元和集成测试可能会错过，因为 e2e 测试与应用程序及其界面交互，就像用户一样。

- **评估发布准备情况**
    通过确认应用程序在密切反映生产的环境中按预期运行。

### 身份证明和文件

#### 功能需求如何确定？

[Functional requirements](../F/functional-requirements.md) 通过**利益相关者访谈**、**用户故事**、**[use cases](../U/use-case.md)** 和 **业务流程建模** 的组合来确定。利益相关者，包括客户、最终用户和业务分析师，提供对系统所需行为的见解。
  **用户故事**是从需要新功能的人（通常是系统的用户或客户）角度讲述的对功能的简短描述。他们通常遵循一个简单的模板：“作为[类型的用户]，我想要[采取行动]，以便[获得利益/价值]。”
  **[Use cases](../U/use-case.md)** 更详细地介绍了用户如何与系统交互，概述了实现特定目标所采取的步骤。它们通过提供一系列事件和预期结果来帮助理解系统的[functional requirements](../F/functional-requirements.md)。
  **业务流程建模**涉及创建表示软件必须支持的业务流程的图表，这有助于识别促进这些流程所需的功能。
  此外，查看现有的**文档**和**系统分析**可以发现[functional requirements](../F/functional-requirements.md)。这可能包括分析当前系统以寻求新系统所需的改进或更改。
  **原型制作**也可以是一种通过构建系统或其部件的工作模型来识别[functional requirements](../F/functional-requirements.md)的方法，以更好地理解所需的功能。
  最后，随着项目的进展，**来自迭代开发的反馈**可以细化和识别额外的[functional requirements](../F/functional-requirements.md)。敏捷方法尤其鼓励持续反馈和[iteration](../I/iteration.md)，这可以帮助呈现最初可能并不明显的[functional requirements](../F/functional-requirements.md)。

#### 记录功能需求的过程是什么？

记录[functional requirements](../F/functional-requirements.md) 是一个将用户需求转化为书面规范的系统过程。首先，通过访谈、研讨会或调查问卷从利益相关者处**收集信息**。接下来，**定义清晰简洁的要求**；每个都应该是完整的、明确的和可测试的。使用 **用户故事** 或 **[use cases](../U/use-case.md)** 进行叙述性方法，或使用 **结构化模板** 进行更正式的规范。
  **为每项要求指定验收标准**，详细说明要被视为满足要求必须满足的条件。这对于[test automation](../T/test-automation.md) 至关重要，因为它指导[test cases](../T/test-case.md) 的开发。
  **逻辑地组织需求**，对相关功能进行分组以简化理解和测试。必要时使用**图表或模型**来可视化复杂的交互或数据流。
  **与利益相关者一起审查和修改**记录的要求，以确保准确性和完整性。这个迭代过程有助于完善规范并调整期望。
  **版本控制**对于在整个软件开发生命周期中跟踪更改和维护文档的完整性至关重要。
  最后，**将记录的需求**传达给开发和测试团队。清晰的文档可确保每个人保持一致，并且可以有效地设计和实施 [test automation](../T/test-automation.md) 策略。
  以下是 Markdown 格式的功能需求示例：

  ```
  - **Title**: User Login
  - **Description**: Users must be able to log in to the system using a username and password.
  - **Acceptance Criteria**:
    - Successful login with valid credentials.
    - Error message displayed for invalid credentials.
    - Account lockout after three consecutive failed attempts.
  ```这种格式确保 [test automation](../T/test-automation.md) 工程师能够轻松理解需求并可采取行动。

#### 用于记录功能需求的常用工具或方法有哪些？

记录 [functional requirements](../F/functional-requirements.md) 的常用工具和方法包括：

- **用户故事**：用类似工具捕获
    **[JIRA](../J/jira.md)**
    ,
    **特雷洛**
    , 或
    **Azure 开发运营**
    ，他们从最终用户的角度描述功能。

- **[Use Cases](../U/use-case.md)** ：解释系统如何与外部实体交互的详细叙述；通常通过诸如
    **Sparx Systems 企业架构师**
    。

- **[Requirements Management Tools](../R/requirements-management-tool.md)** ：例如
    **IBM Rational DOORS**
    或
    **螺旋 RM**
    ，这有助于随着时间的推移跟踪和维护需求。

- **维基页面**：诸如此类的平台
    **汇合**
    或
    **GitHub 维基**
    提供用于记录和更新需求的协作空间。

- **共享文档**：使用基于云的文档存储，例如
    **谷歌文档**
    或
    **微软 Office 365**
    允许实时协作。

- **原型设计工具**：类似的工具
    **巴尔萨米克**
    或
    **轴**
    有助于通过模型和线框图可视化需求。

- **功能跟踪电子表格**：对于小型项目来说简单而有效，使用
    **Excel**
    或
    **谷歌表格**
    列出并跟踪需求。

- **建模工具**：例如
    **UML图**
    创建于
    **清晰图表**
    或
    **维西奥**
    表示系统行为和交互。
  这些方法有助于清晰、结构化且易于访问的[functional requirements](../F/functional-requirements.md) 文档，这对于有效[test automation](../T/test-automation.md) 至关重要。它们使自动化工程师能够创建符合记录的软件功能期望的[test cases](../T/test-case.md)。

- **用户故事**：用类似工具捕获
    **[JIRA](../J/jira.md)**
    ,
    **特雷洛**
    , 或
    **Azure 开发运营**
    ，他们从最终用户的角度描述功能。

- **[Use Cases](../U/use-case.md)** ：解释系统如何与外部实体交互的详细叙述；通常通过诸如
    **Sparx Systems 企业架构师**
    。

- **[Requirements Management Tools](../R/requirements-management-tool.md)** ：例如
    **IBM Rational DOORS**
    或
    **螺旋 RM**
    ，这有助于随着时间的推移跟踪和维护需求。

- **维基页面**：诸如此类的平台
    **汇合**
    或
    **GitHub 维基**
    提供用于记录和更新需求的协作空间。

- **共享文档**：使用基于云的文档存储，例如
    **谷歌文档**
    或
    **微软 Office 365**
    允许实时协作。

- **原型设计工具**：类似的工具
    **巴尔萨米克**
    或
    **轴**
    有助于通过模型和线框图可视化需求。

- **功能跟踪电子表格**：对于小型项目来说简单而有效，使用
    **Excel**
    或
    **谷歌表格**
    列出并跟踪需求。

- **建模工具**：例如
    **UML图**
    创建于
    **清晰图表**
    或
    **维西奥**
    表示系统行为和交互。

#### 功能需求文档中应包含哪些关键元素？

功能需求文档中包含的关键要素是：

- **用户故事或[Use Cases](../U/use-case.md)**：描述用户和系统之间交互的简短叙述。
  - **业务规则**：定义适用于系统的操作、定义和约束。
  - **功能层次结构**：功能及其子功能的组织列表。
  - **数据流程图**：系统中数据移动的可视化表示。
  - **数据模型**：定义数据的处理和存储方式。
  - **外部接口**：指定系统如何与外部系统和用户交互。
  - **用户界面模型**：UI 的初步设计，以指导对功能的理解。
  - **验收标准**：用户故事被视为完整的特定条件。
  - **[Priority](../P/priority.md) 和关键性**：指示每个要求的重要性和影响。
  - **性能标准**：概述功能的预期性能水平。
  - **安全要求**：详细的安全功能和符合标准。
  - **错误处理和恢复**：定义错误条件下的系统行为。
  - **审计跟踪**：跟踪和记录系统活动的要求。
  - **监管要求**：确保遵守适用的法律和法规。
  - **可扩展性和[Maintainability](../M/maintainability.md)** ：考虑未来的增长和易于更新。
  每个需求都应该**清晰**、**简洁**和**可测试**，并具有唯一标识符以便于参考。让利益相关者参与创建过程至关重要，以确保捕获和理解所有需求。为了适应软件开发生命周期中的变化，定期审查和更新是必要的。

- **用户故事或[Use Cases](../U/use-case.md)**：描述用户和系统之间交互的简短叙述。
  - **业务规则**：定义适用于系统的操作、定义和约束。
  - **功能层次结构**：功能及其子功能的组织列表。
  - **数据流程图**：系统中数据移动的可视化表示。
  - **数据模型**：定义数据的处理和存储方式。
  - **外部接口**：指定系统如何与外部系统和用户交互。
  - **用户界面模型**：UI 的初步设计，以指导对功能的理解。
  - **验收标准**：用户故事被视为完整的特定条件。
  - **[Priority](../P/priority.md) 和关键性**：指出每个要求的重要性和影响。
  - **性能标准**：概述功能的预期性能水平。
  - **安全要求**：详细的安全功能和符合标准。
  - **错误处理和恢复**：定义错误条件下的系统行为。
  - **审计跟踪**：跟踪和记录系统活动的要求。
  - **监管要求**：确保遵守适用的法律和法规。
  - **可扩展性和[Maintainability](../M/maintainability.md)** ：考虑未来的增长和易于更新。

### 验证和确认

#### 功能需求如何验证和确认？

[Functional requirements](../F/functional-requirements.md) 通过 **[manual testing](../M/manual-testing.md)** 和 **[automated testing](../A/automated-testing.md)** 的组合进行验证和验证。 [Verification](../V/verification.md) 确保产品正确构建，符合指定要求，而验证则确认构建了正确的产品，满足用户需求。
  **自动[test scripts](../T/test-script.md)** 被写入以匹配[functional requirements](../F/functional-requirements.md)。这些脚本使用断言来检查软件是否按预期运行。例如：

  ```
  expect(actualOutput).toEqual(expectedOutput);
  ```**单元测试**验证各个组件或功能，而**集成测试**确保多个组件一起工作。 **系统测试**验证整个系统的功能。
  **行为驱动开发 ([BDD](../B/bdd.md))** Cucumber 或 SpecFlow 等框架允许用自然语言编写测试，将它们直接链接到 [functional requirements](../F/functional-requirements.md)：

  ```
  Feature: User login
    Scenario: Valid user login
      Given the user is on the login page
      When the user enters valid credentials
      Then the user is redirected to the dashboard
  ```**[Exploratory testing](../E/exploratory-testing.md)** 通过允许测试人员以脚本可能无法涵盖的方式验证需求来补充自动化，从而确保人的视角。
  **代码审查**和**结对编程**是通过对照预期功能仔细检查代码来帮助早期[verification](../V/verification.md) 需求的实践。
  **持续集成 (CI)** 系统对新代码提交运行自动化测试，提供有关 [functional requirements](../F/functional-requirements.md) 的 [verification](../V/verification.md) 状态的即时反馈。
  为了克服验证方面的挑战，请保持需求、测试和代码之间的**可追溯性**。使用 **[test coverage](../T/test-coverage.md) 工具** 确保测试所有要求。定期**审查和更新[test cases](../T/test-case.md)**以适应不断变化的需求。让[acceptance testing](../A/acceptance-testing.md) 的**利益相关者**参与进来，根据现实场景和期望来验证软件。

#### e2e 测试在功能需求验证中扮演什么角色？

端到端 (E2E) 测试在验证 **[functional requirements](../F/functional-requirements.md)** 是否得到满足方面发挥着至关重要的作用。它涉及从头到尾测试应用程序的完整流程，确保所有集成组件按预期一起运行。 E2E测试模拟真实的用户场景，不仅涵盖应用程序的前端，还涵盖其后端、[database](../D/database.md)以及与其他服务的交互。
  通过自动化 E2E 测试，您可以：

- **验证关键路径**
    ，例如用户注册、登录、数据处理和支付系统，这些对于应用程序功能至关重要。

- **检测问题**
    具有数据完整性和不同系统组件之间的通信。

- **确保一致性**
    不同环境中以及更改或更新后的应用程序行为。

- **降低风险**
    通过在每次部署后运行测试来减少回归。
  E2E测试应重点关注最**常见和关键的用户流程**，以有效验证应用程序是否满足其[functional requirements](../F/functional-requirements.md)。自动化 E2E 测试可以集成到持续集成和部署管道中，提供有关代码更改影响的快速反馈。

  ```
  // Example of an E2E test case in TypeScript using a testing framework
  describe('User Registration Flow', () => {
    it('should register a new user', async () => {
      await goToRegistrationPage();
      await fillOutRegistrationForm('testuser', 'password123');
      await submitRegistrationForm();
      expect(await isUserLoggedIn()).toBe(true);
    });
  });
  ```总之，E2E 测试确保应用程序从用户的角度按照预期运行，这是对 [functional requirements](../F/functional-requirements.md) 的最终验证。

- **验证关键路径**
    ，例如用户注册、登录、数据处理和支付系统，这些对于应用程序功能至关重要。

- **检测问题**
    具有数据完整性和不同系统组件之间的通信。

- **确保一致性**
    不同环境中以及更改或更新后的应用程序行为。

- **降低风险**
    通过在每次部署后运行测试来减少回归。

#### 验证功能需求时存在哪些常见挑战以及如何克服这些挑战？

验证[functional requirements](../F/functional-requirements.md) 通常会带来一些挑战，例如**不明确的规范**、**复杂的依赖关系**、**[test environment](../T/test-environment.md) 差异**和**数据管理问题**。克服这些问题需要采取战略方法：

- **模糊性**：确保需求清晰且可测试。与利益相关者合作完善任何模糊的要求。利用 Cucumber 等行为驱动开发 ([BDD](../B/bdd.md)) 框架来创建可执行规范。
  - **依赖关系**：模拟或存根外部系统和服务以隔离被测系统。 WireMock 或 Mockito 等工具可以模拟这些依赖关系。
  - **环境差异**：使用 Docker 等容器化工具保持跨环境的一致性，并使用 Terraform 等工具保持基础设施即代码。
  - **数据管理**：实施 [test data](../T/test-data.md) 创建和清理策略。使用 [database](../D/database.md) 版本控制工具（例如 Liquibase 或 Flyway）来管理架构更改并确保数据完整性。
  使用持续集成 (CI) 管道自动化验证过程有助于及早发现问题。 Jenkins 或 GitHub Actions 等工具可以针对新代码更改自动执行 [test suites](../T/test-suite.md)。
  此外，定期审查和更新 [test cases](../T/test-case.md) 以适应不断变化的要求。在[test case](../T/test-case.md) 审核会议期间与领域专家配对可以提供有价值的见解并确保覆盖关键业务路径。
  请记住，开发人员、测试人员和业务利益相关者之间的有效沟通和协作对于克服这些挑战至关重要。

- **模糊性**：确保需求清晰且可测试。与利益相关者合作完善任何模糊的要求。利用 Cucumber 等行为驱动开发 ([BDD](../B/bdd.md)) 框架来创建可执行规范。
  - **依赖关系**：模拟或存根外部系统和服务以隔离被测系统。 WireMock 或 Mockito 等工具可以模拟这些依赖关系。
  - **环境差异**：使用 Docker 等容器化工具保持跨环境的一致性，并使用 Terraform 等工具保持基础设施即代码。
  - **数据管理**：实施 [test data](../T/test-data.md) 创建和清理策略。使用 [database](../D/database.md) 版本控制工具（例如 Liquibase 或 Flyway）来管理架构更改并确保数据完整性。

### 实际应用

#### 您能否提供一些实际软件应用程序中功能需求的示例？

实际软件应用程序中[functional requirements](../F/functional-requirements.md) 的示例包括：

- **用户身份验证**：用户必须能够使用用户名和密码登录。尝试 3 次失败后，该帐户将被锁定 10 分钟。

    ```
    if (loginAttempts > 3) {
      lockAccount(userId);
    }
    ```

- **数据导出**：系统必须允许用户以 CSV 格式导出数据。导出应包括所有用户数据并遵守数据隐私法规。

    ```
    exportUserData(userId, Format.CSV);
    ```

- **付款处理**：当用户完成购买时，系统必须使用外部支付网关处理付款并提供交易收据。

    ```
    processPayment(userCart, paymentDetails);
    ```

- **搜索功能**：用户应该能够使用关键字搜索产品，并且系统必须在2秒内显示结果。

    ```
    searchProducts(searchTerm).then(displayResults);
    ```

- **订单跟踪**：下订单后，用户必须能够跟踪订单状态，随着订单经过“处理”、“已发货”和“已交付”等阶段，订单状态会实时更新。

    ```
    trackOrder(orderId).onUpdate(updateOrderStatus);
    ```

- **通知系统**：当收到新消息或订单状态有更新时，应用程序必须向用户发送通知。

    ```
    sendNotification(userId, notificationType);
    ```

- **内容管理**：管理员用户必须能够在内容管理系统中创建、更新和删除文章，并立即反映更改。

    ```
    manageArticle(action, articleData);
    ```这些示例说明了软件必须执行的特定、可测量和可测试的操作，以满足用户需求和业务目标。

- **用户身份验证**：用户必须能够使用用户名和密码登录。尝试 3 次失败后，该帐户将被锁定 10 分钟。

    ```
    if (loginAttempts > 3) {
      lockAccount(userId);
    }
    ```

- **数据导出**：系统必须允许用户以 CSV 格式导出数据。导出应包括所有用户数据并遵守数据隐私法规。

    ```
    exportUserData(userId, Format.CSV);
    ```

- **付款处理**：当用户完成购买时，系统必须使用外部支付网关处理付款并提供交易收据。

    ```
    processPayment(userCart, paymentDetails);
    ```

- **搜索功能**：用户应该能够使用关键字搜索产品，并且系统必须在2秒内显示结果。

    ```
    searchProducts(searchTerm).then(displayResults);
    ```

- **订单跟踪**：下订单后，用户必须能够跟踪订单状态，随着订单经过“处理”、“已发货”和“已交付”等阶段，订单状态会实时更新。

    ```
    trackOrder(orderId).onUpdate(updateOrderStatus);
    ```

- **通知系统**：当收到新消息或订单状态有更新时，应用程序必须向用户发送通知。

    ```
    sendNotification(userId, notificationType);
    ```

- **内容管理**：管理员用户必须能够在内容管理系统中创建、更新和删除文章，并立即反映更改。

    ```
    manageArticle(action, articleData);
    ```

#### 功能需求在软件项目的生命周期中如何演变？

[Functional requirements](../F/functional-requirements.md) 在软件项目的各个阶段不断发展，适应业务需求、用户反馈和技术发现的变化。
  **初始开发**：收集和定义需求，通常包含高级细节。随着利益相关者完善他们的愿景，它们可能会发生变化。
  **设计阶段**：随着系统架构的设计，需求变得更加详细。确定依赖关系和系统交互，从而可能改变需求。
  **实施**：当开发人员构建功能时，不可预见的技术限制可能需要进行需求调整。持续集成和定期代码审查有助于保持与需求的一致性。
  **测试**：在单元、集成和[system testing](../S/system-testing.md)期间，预期行为和实际行为之间的差异可能导致需求细化，以更好地反映可以实际实现和测试的内容。
  **[User Acceptance Testing](../U/user-acceptance-testing.md) (UAT)**：现实世界的使用和反馈可能会揭示需求中的差距或误解，从而提示更新以确保软件满足用户需求。
  **维护**：发布后，需求随着 [bug](../B/bug.md) 修复、增强和适应不断变化的市场或监管条件而变化。
  在整个生命周期中，**敏捷方法**鼓励需求的迭代细化，而**变更管理流程**确保系统地解决任何演变。开发人员、测试人员和利益相关者之间的有效沟通对于管理[functional requirements](../F/functional-requirements.md) 的发展至关重要。

#### 定义功能需求时有哪些常见错误或陷阱以及如何避免它们？

定义 [functional requirements](../F/functional-requirements.md) 时的常见错误包括**含糊**、**过于复杂**、**缺乏清晰度**和**不一致**。这些可能会导致[test automation](../T/test-automation.md) 中的误解、范围蔓延和挑战。
  为了避免这些陷阱：

- **具体**：使用精确的语言和清晰的定义。避免使用可以多种方式解释的模糊术语。
  - **优先考虑简单性**：将复杂的需求分解为更简单、可管理的部分。复杂的需求可能难以测试和自动化。
  - **让利益相关者参与**：确保所有相关方（包括开发人员、测试人员和业务分析师）都参与需求收集过程。这有助于获得不同的观点并更好地理解需求。
  - **迭代审查**：定期审查和细化需求，以确保它们随着项目的发展保持相关性和准确性。
  - **使用模型和图表**：使用用例图或用户故事等模型补充文本要求，以提供额外的上下文和清晰度。
  - **保持一致性**：确保所有要求彼此一致并与整个系统目标一致。不一致可能会导致测试自动化脚本中出现错误。
  - **变更管理**：实施强大的变更管理流程，以有效处理需求修改，并确保变更反映在测试自动化策略中。
  通过关注这些策略，[test automation](../T/test-automation.md) 工程师可以确保[functional requirements](../F/functional-requirements.md) 定义明确、清晰且可测试，从而实现更加有效和高效的[test automation](../T/test-automation.md)。

- **具体**：使用精确的语言和清晰的定义。避免使用可以多种方式解释的模糊术语。
  - **优先考虑简单性**：将复杂的需求分解为更简单、可管理的部分。复杂的需求可能难以测试和自动化。
  - **让利益相关者参与**：确保所有相关方（包括开发人员、测试人员和业务分析师）都参与需求收集过程。这有助于获得不同的观点并更好地理解需求。
  - **迭代审查**：定期审查和细化需求，以确保它们随着项目的发展保持相关性和准确性。
  - **使用模型和图表**：使用用例图或用户故事等模型补充文本要求，以提供额外的上下文和清晰度。
  - **保持一致性**：确保所有要求彼此一致并与整个系统目标一致。不一致可能会导致测试自动化脚本中出现错误。
  - **变更管理**：实施强大的变更管理流程，以有效处理需求修改，并确保变更反映在测试自动化策略中。
