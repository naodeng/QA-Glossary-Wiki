# gherkin

<!-- TOC START -->
- [相关术语：](#相关术语：)
- [关于gherkin的问题吗？](#关于gherkin的问题吗？)
  - [基础知识和重要性](#基础知识和重要性)
    - [Gherkin 是什么以及为什么它在软件测试中很重要？](#gherkin-是什么以及为什么它在软件测试中很重要？)
    - [Gherkin 文档的主要组成部分是什么？](#gherkin-文档的主要组成部分是什么？)
    - [Gherkin 如何改善技术和非技术利益相关者之间的沟通？](#gherkin-如何改善技术和非技术利益相关者之间的沟通？)
    - [Gherkin 在行为驱动开发 (BDD) 中的作用是什么？](#gherkin-在行为驱动开发-bdd-中的作用是什么？)
  - [语法和结构](#语法和结构)
    - [Gherkin 的基本语法是什么？](#gherkin-的基本语法是什么？)
    - [Gherkin 中使用了哪些不同的关键字以及它们的含义是什么？](#gherkin-中使用了哪些不同的关键字以及它们的含义是什么？)
    - [Gherkin 文件的结构如何？](#gherkin-文件的结构如何？)
    - [在 Gherkin 中编写步骤的规则是什么？](#在-gherkin-中编写步骤的规则是什么？)
    - [Gherkin 中背景的用途是什么？](#gherkin-中背景的用途是什么？)
  - [场景和功能](#场景和功能)
    - [Gherkin 中的功能是什么以及它是如何定义的？](#gherkin-中的功能是什么以及它是如何定义的？)
    - [Gherkin 中的场景是什么以及它是如何定义的？](#gherkin-中的场景是什么以及它是如何定义的？)
    - [Gherkin 中的场景和场景大纲有什么区别？](#gherkin-中的场景和场景大纲有什么区别？)
    - [Gherkin场景下如何传递参数？](#gherkin场景下如何传递参数？)
    - [Gherkin 中标签的用途是什么？](#gherkin-中标签的用途是什么？)
  - [高级概念](#高级概念)
    - [Gherkin 如何与 Cucumber 这样的自动化工具一起使用？](#gherkin-如何与-cucumber-这样的自动化工具一起使用？)
    - [编写 Gherkin 脚本的最佳实践是什么？](#编写-gherkin-脚本的最佳实践是什么？)
    - [如何在 Gherkin 中处理复杂的测试用例？](#如何在-gherkin-中处理复杂的测试用例？)
    - [Gherkin 在测试自动化方面有哪些局限性？](#gherkin-在测试自动化方面有哪些局限性？)
    - [Gherkin 如何在持续集成/持续部署 (CI/CD) 管道中使用？](#gherkin-如何在持续集成持续部署-cicd-管道中使用？)
<!-- TOC END -->

gherkin

是一种特定于领域的语言，主要用于行为驱动开发（

BDD

）。它提供了一种结构化且人类可读的格式来描述和记录软件功能的所需行为。

gherkin

的语法使用简单语言与特定关键字（例如“Given”、“When”、“Then”、“And”和“But”）相结合来定义先决条件、操作和预期结果。这些

gherkin

然后，场景可以用作系统行为的规范和自动化测试的基础，使其成为非技术利益相关者和技术团队之间的桥梁。

## 相关术语：

- [BDD (Behavior Driven Development)](../B/bdd-behavior-driven-development.md)
- [Test Scenario](../T/test-scenario.md)

## 关于gherkin的问题吗？

### 基础知识和重要性

#### Gherkin 是什么以及为什么它在软件测试中很重要？

[Gherkin](../G/gherkin.md) 是一种**特定于领域的语言**，旨在为软件功能创建清晰且可执行的规范。它在[software testing](../S/software-testing.md) 中的重要性在于它能够弥合[test automation](../T/test-automation.md) 的**技术**方面与**面向业务的**对功能应如何表现的理解之间的差距。
  通过使用自然语言格式，[Gherkin](../G/gherkin.md) 允许创建所有利益相关者（包括开发人员、测试人员和业务分析师）都很容易理解的 **[test cases](../T/test-case.md)**。这种共同的理解确保软件构建时具有正确的功能，并且测试符合用户的期望。
  在 [test automation](../T/test-automation.md) 的上下文中，[Gherkin](../G/gherkin.md) 充当编写**自动化验收测试**的基础。 Cucumber 等工具读取 [Gherkin](../G/gherkin.md) 文档并针对应用程序执行所描述的行为。这有助于验证软件的行为是否符合预期，并且通过确保新更改不会破坏现有功能来促进**[regression testing](../R/regression-testing.md)**。
  此外，[Gherkin](../G/gherkin.md) 的结构化格式允许跨不同场景重用步骤，使[test automation](../T/test-automation.md) 更加**高效**和**可维护**。它还通过场景大纲和示例支持**数据驱动测试**，允许测试多组输入，而无需重复[test scripts](../T/test-script.md)。
  总之，[Gherkin](../G/gherkin.md) 在[software testing](../S/software-testing.md) 中的重要性是多方面的：它增强了沟通，支持行为驱动的开发，并为编写和维护自动化测试提供了强大的框架，所有这些都有助于交付高质量的软件。

#### Gherkin 文档的主要组成部分是什么？

[Gherkin](../G/gherkin.md) 文档的主要组成部分是：

- **功能**：代表正在测试的系统的单个功能或方面。它提供了高级描述并充当相关场景的容器。

  ```
  Feature: Account Holder withdraws cash
  ```

- **背景**：指定功能文件中所有场景通用的步骤。它用于设置初始上下文。

  ```
  Background:
    Given the account balance is $100
  ```

- **场景**：定义验证系统行为的单个测试用例或示例。它由一系列步骤组成。

  ```
  Scenario: Account Holder withdraws cash within balance limit
  ```

- **场景大纲**：允许使用占位符和示例表使用不同的数据集多次运行相同的场景。

  ```
  Scenario Outline: Account Holder withdraws varying amounts
    When the Account Holder requests $<WithdrawalAmount>
    Then the account balance should be $<RemainingBalance>
    Examples:
    | WithdrawalAmount | RemainingBalance |
    | 50               | 50               |
    | 20               | 80               |
  ```

- **步骤**：定义要执行的操作（Given、When、Then）和断言。它们是场景和场景大纲的基本构建块。

  ```
  Given the account balance is $100
  When the Account Holder requests $20
  Then the ATM should dispense $20
  ```

- **标签**：用于组织功能和场景，使过滤和运行选择性测试变得更容易。

  ```
  @smoke
  Scenario: Account Holder withdraws cash within balance limit
  ```

- **注释**：以以下开头的行
    `#`
    被忽略，可用于添加附加信息或注释。

  ```
  # This is a comment explaining the following step
  Given the account balance is $100
  ```这些组件协同工作，创建一个可执行的规范，该规范可以被利益相关者理解，并可以通过 Cucumber 等工具实现自动化。

- **功能**：代表正在测试的系统的单个功能或方面。它提供了高级描述并充当相关场景的容器。
  - **背景**：指定功能文件中所有场景通用的步骤。它用于设置初始上下文。
  - **场景**：定义验证系统行为的单个测试用例或示例。它由一系列步骤组成。
  - **场景大纲**：允许使用占位符和示例表使用不同的数据集多次运行相同的场景。
  - **步骤**：定义要执行的操作（Given、When、Then）和断言。它们是场景和场景大纲的基本构建块。
  - **标签**：用于组织功能和场景，使过滤和运行选择性测试变得更容易。
  - **注释**：以以下开头的行
    `#`
    被忽略，可用于添加附加信息或注释。

#### Gherkin 如何改善技术和非技术利益相关者之间的沟通？

[Gherkin](../G/gherkin.md) 通过提供所有相关方都易于理解的**通用语言**，充当技术和非技术利益相关者之间的**沟通桥梁**。它使用简单的英语（或其他口语）方法来定义软件行为，使业务分析师、产品所有者、开发人员和测试人员能够有效协作。
  [Gherkin](../G/gherkin.md) 中使用**自然语言**结构意味着可以以对非技术利益相关者来说**直观**的方式编写需求和测试。这使他们能够积极参与验收标准的创建和审查，而无需了解底层技术实现。
  通过将需求表达为**可执行规范**，[Gherkin](../G/gherkin.md) 确保软件应执行的操作有**单一事实来源**。这降低了通过传统方式（例如冗长的文档或口头讨论）传达需求时可能发生的误解风险。
  此外，[Gherkin](../G/gherkin.md) 的**场景**和**功能**描述提供了软件功能的**高级概述**，这对于需要了解更广泛背景而不陷入技术细节的利益相关者来说非常有价值。
  [Gherkin](../G/gherkin.md) 的**协作性质**及其在[BDD](../B/bdd.md) 中的作用鼓励业务和技术团队成员之间**持续的对话**。这种持续的对话有助于澄清期望、发现隐藏的需求，并确保开发工作与业务目标紧密结合。
  总之，[Gherkin](../G/gherkin.md) 通过使参与项目的每个人都可以理解和访问复杂的软件行为来增强沟通，从而促进更好的协作并减少误解的可能性。

#### Gherkin 在行为驱动开发 (BDD) 中的作用是什么？

[Gherkin](../G/gherkin.md) 作为业务需求和技术实现之间的桥梁，在行为驱动开发 ([BDD](../B/bdd.md)) 中发挥着关键作用。它允许表达软件行为，而无需详细说明如何实现该功能，使其成为利益相关者之间**协作**和**共享理解**的重要工具。
  在[BDD](../B/bdd.md) 中，[Gherkin](../G/gherkin.md) 的主要作用是支持**创建可执行规范**。这些规范的编写方式可以直接转换为自动化测试。这是通过使用**特定于领域的语言**来实现的，该语言以逻辑且易于理解的术语描述软件的行为。
  [Gherkin](../G/gherkin.md) 的 **Given-When-Then** 格式对应于 [unit testing](../U/unit-testing.md) 中常用的 **Arrange-Act-Assert** 模式，这确保测试结构化且易于遵循。这种格式有助于定义清晰简洁的功能**验收标准**，确保所有利益相关者对要开发的内容有共同的理解。
  此外，[Gherkin](../G/gherkin.md) 有助于**活文档**。随着场景的更新以反映需求的变化，文档仍然保持最新且可操作。这个动态文档充当系统预期行为的**单一事实来源**，减少歧义并防止规范和实现之间的偏差。
  通过将 [Gherkin](../G/gherkin.md) 集成到 [BDD](../B/bdd.md) 流程中，团队可以确保**自动化测试与业务目标保持一致**，从而促进高效且有效地交付满足用户需求的高质量软件的开发流程。

### 语法和结构

#### Gherkin 的基本语法是什么？

[Gherkin](../G/gherkin.md) 的基本语法被设计为人类可读的，并允许描述软件行为，而无需详细说明该功能是如何实现的。 [Gherkin](../G/gherkin.md) 文档以关键字**功能**开头，后跟正在测试的整体功能的简短描述。每个功能都包含一个**场景**列表，这些示例说明了该功能在不同条件下应如何工作。
  场景以关键字 **场景** 开头，后跟简短描述。每个场景都由描述操作或检查的步骤组成。这些步骤使用关键字 **Given**、**When**、**Then**、**And** 和 **But** 分别描述上下文、操作和预期结果。
  以下是简单 [Gherkin](../G/gherkin.md) 语法的示例：

  ```
  Feature: User login
    Scenario: Successful login with valid credentials
      Given the user is on the login page
      When the user enters valid credentials
      Then the user is redirected to the homepage
    Scenario: Unsuccessful login with invalid credentials
      Given the user is on the login page
      When the user enters invalid credentials
      Then an error message is displayed
  ```场景中的每个步骤都应该是一个简单的语句，可以与[test automation](../T/test-automation.md) 框架中的步骤定义相匹配，其中包含执行步骤所描述的操作或[verification](../V/verification.md) 的代码。 [Gherkin](../G/gherkin.md) 的语法被设计为易于编写和理解，弥合了软件开发过程中技术和非技术参与者之间的差距。

#### Gherkin 中使用了哪些不同的关键字以及它们的含义是什么？

[Gherkin](../G/gherkin.md) 关键字是[Gherkin](../G/gherkin.md) 语言的核心构建块，每个关键字在定义和构建行为测试方面都有特定的用途。

- **功能**：描述软件功能并充当场景的容器。
  - **规则**
    （可选）：将共享相同业务规则的功能中的多个场景组合在一起。

- **背景**：为功能文件中的场景提供上下文；它包含所有场景通用的步骤，并在每个场景之前运行。
  - **场景**：表示要测试的单个行为或用例。
  - **场景大纲**：允许使用不同的数据集多次运行相同的场景，由
    **示例**
    。

- **示例**：附带场景大纲，以表格格式包含每次迭代的数据。
  - **给定**：描述测试行为之前系统的初始上下文。
  - **何时** ：指定触发行为的事件或操作。
  - **然后**：概述“何时”步骤发生后的预期结果或状态。
  - **和**
    ,
    **But** ：用于在 Give-When-Then 序列中添加附加步骤，而不重复关键字。

  ```
  Feature: User login
    Background:
      Given the user is on the login page
    Scenario: Successful login
      When the user enters valid credentials
      Then the user is redirected to the dashboard
    Scenario Outline: Data-driven login attempt
      When the user enters "<username>" and "<password>"
      Then the user "<result>"
      Examples:
        | username | password | result      |
        | user1    | pass1    | is logged in|
        | user2    | wrong    | is blocked  |
  ```每个关键字都会启动一个与 [test automation](../T/test-automation.md) 框架中的步骤定义相匹配的步骤，其中包含实际的可执行代码。

- **功能**：描述软件功能并充当场景的容器。
  - **规则**
    （可选）：将共享相同业务规则的功能中的多个场景组合在一起。

- **背景**：为功能文件中的场景提供上下文；它包含所有场景通用的步骤，并在每个场景之前运行。
  - **场景**：表示要测试的单个行为或用例。
  - **场景大纲**：允许使用不同的数据集多次运行相同的场景，由
    **示例**
    。

- **示例**：附带场景大纲，以表格格式包含每次迭代的数据。
  - **给定**：描述测试行为之前系统的初始上下文。
  - **何时** ：指定触发行为的事件或操作。
  - **然后**：概述“何时”步骤发生后的预期结果或状态。
  - **和**
    ,
    **But** ：用于在 Give-When-Then 序列中添加附加步骤，而不重复关键字。

#### Gherkin 文件的结构如何？

[Gherkin](../G/gherkin.md) 文件通常被构造为带有 `.feature` 扩展名的纯文本文档，包含单个功能规范。该文件以 **Feature** 关键字开头，后面是正在测试的功能的简短描述。这是功能或业务规则的高级定义。
  在功能描述下方，定义了一个或多个**场景**或**场景大纲**。这些是[test cases](../T/test-case.md)，指定系统的预期行为。每个场景都以 **Scenario** 关键字开头，后跟总结 [test case](../T/test-case.md) 的标题。
  场景由描述操作和结果的步骤组成。步骤以 **Given**、**When**、**Then**、**And** 或​​ **But** 关键字开始，它们对应于测试的 [setup](../S/setup.md)、操作和断言阶段。 **给定**步骤用于描述初始上下文，**何时**步骤指定事件或操作，**然后**步骤断言预期结果。
  **背景**可用于定义文件中所有场景通用的步骤，从而消除重复。
  **场景大纲**用于参数化测试，**示例**部分提供数据集。
  **标签**可以应用在功能、背景或单个场景之上，以对测试进行分类或过滤。

  ```
  Feature: User login
    Background:
      Given the user is on the login page
    @smoke
    Scenario: Successful login
      Given the user has valid credentials
      When the user attempts to login
      Then the user is redirected to the dashboard
    @regression
    Scenario Outline: Login with invalid credentials
      Given the user has entered <username> and <password>
      When the user attempts to login
      Then an error message <message> is displayed
      Examples:
        | username | password | message           |
        | admin    | wrong    | Invalid password  |
        | unknown  | pass123  | User does not exist |
  ```场景大纲中的参数由 `<` 和 `>` 表示，并在执行期间替换为 **Examples** 表中的值。

#### 在 Gherkin 中编写步骤的规则是什么？

在 [Gherkin](../G/gherkin.md) 中编写步骤时，请遵守以下规则以确保清晰度和功能性：

- **使用命令式语言**：将步骤编写为直接命令，例如，
    `Given the user is logged in`
    。

- **简洁**：保持步骤简短、切题，以增强可读性。
  - **避免技术术语**：使用所有利益相关者（而不仅仅是开发人员）都可以理解的语言。
  - **以动词开头**：每个步骤应以
    `Given`
    ,
    `When`
    ,
    `Then`
    ,
    `And`
    , 或
    `But`
    。

- **关注行为**：描述预期的行为，而不是实现细节。
  - **参数化**：对发生变化的数据使用变量，例如，
    `When the user enters "<username>"`
    。

- **对多个示例使用场景大纲**：当您有多个场景示例时，请将场景大纲与示例表一起使用。
  - **维护用户视角**：从用户与系统交互的角度进行编写。
  - **确保独立性**：每个场景都应该是独立的并且可以自行执行。
  - **避免 UI 细节**：不要引用按钮或字段等 UI 元素；专注于行动或结果。
  - **明智地使用背景**：常见步骤应放在背景部分，但要谨慎使用，以避免隐藏重要信息。
  编写良好的 [Gherkin](../G/gherkin.md) 步骤示例：

  ```
  Given the user has navigated to the login page
  When they enter their credentials
  And they click the login button
  Then they should be redirected to the dashboard
  ```请记住，目标是创建可理解、可维护且可执行的自动化测试场景。

- **使用命令式语言**：将步骤编写为直接命令，例如，
    `Given the user is logged in`
    。

- **简洁**：保持步骤简短、切题，以增强可读性。
  - **避免技术术语**：使用所有利益相关者（而不仅仅是开发人员）都可以理解的语言。
  - **以动词开头**：每个步骤应以
    `Given`
    ,
    `When`
    ,
    `Then`
    ,
    `And`
    , 或
    `But`
    。

- **关注行为**：描述预期的行为，而不是实现细节。
  - **参数化**：对发生变化的数据使用变量，例如，
    `When the user enters "<username>"`
    。

- **对多个示例使用场景大纲**：当您有多个场景示例时，请将场景大纲与示例表一起使用。
  - **维护用户视角**：从用户与系统交互的角度进行编写。
  - **确保独立性**：每个场景都应该是独立的并且可以自行执行。
  - **避免 UI 细节**：不要引用按钮或字段等 UI 元素；专注于行动或结果。
  - **明智地使用背景**：常见步骤应放在背景部分，但要谨慎使用，以避免隐藏重要信息。

#### Gherkin 中背景的用途是什么？

[Gherkin](../G/gherkin.md) 中的 **背景** 充当同一 **功能** 内多个 **场景** 的可重用上下文。它允许您定义所有场景通用的步骤，避免重复并保持场景简洁。背景中定义的步骤在每个场景之前执行，为接下来的特定测试奠定了基础。
  以下是如何使用背景的示例：

  ```
  Feature: User login
    Background:
      Given the user is on the login page
      And the database has the default set of users
    Scenario: Successful login with valid credentials
      When the user logs in with valid credentials
      Then the user is redirected to the dashboard
    Scenario: Unsuccessful login with invalid credentials
      When the user attempts to log in with invalid credentials
      Then an error message is displayed
  ```在此示例中，步骤“假定用户位于登录页面”和“[database](../D/database.md) 具有默认用户集”是这两种情况的常见先决条件。通过使用背景，您可以确保针对每个场景执行这些步骤，维护 DRY（不要重复）原则并提高 [Gherkin](../G/gherkin.md) 文档的可读性。

### 场景和功能

#### Gherkin 中的功能是什么以及它是如何定义的？

在[Gherkin](../G/gherkin.md) 中，**功能** 代表正在测试的系统的独特功能或方面。它提供了软件功能的高级描述，并充当相关场景集合的保护伞。
  功能在[Gherkin](../G/gherkin.md) 文件的开头使用关键字`Feature:` 进行定义，后面是所涵盖功能的简短描述。如果需要，此描述可以跨越多行。功能部分还可能包括提供上下文的背景叙述，这是可选的，但有助于理解功能的目的。
  以下是如何在 [Gherkin](../G/gherkin.md) 文件中定义功能的示例：

  ```
  Feature: User authentication
    As a user of the application
    I want to be able to log in with my credentials
    So that I can access my personal account information
  ```本节不包含任何可执行步骤，但为后续场景奠定了基础，其中将包含用于测试功能的实际“Given-When-Then”步骤。功能关键字后跟一个冒号和一个空格，然后是功能的标题。标题下方的描述是可选的，但为了清晰和利益相关者沟通，建议使用。

#### Gherkin 中的场景是什么以及它是如何定义的？

在[Gherkin](../G/gherkin.md) 中，**场景** 表示通过某个功能的单个路径或工作流程。它是使用关键字`Scenario` 后跟冒号和简洁描述正在测试的行为的标题来定义的。场景由一系列步骤组成，概述了给定情况、要采取的操作以及预期结果。这些步骤分别使用关键字`Given`、`When` 和`Then`，并且还可以包含`And` 和`But` 以获取其他上下文或操作。
  以下是 [Gherkin](../G/gherkin.md) 文档中的场景示例：

  ```
  Scenario: User logs in with valid credentials
    Given the login page is displayed
    When the user enters valid credentials
    And the user clicks on the login button
    Then the dashboard page should be displayed
  ```场景中的每个步骤都映射到 [test automation](../T/test-automation.md) 框架中的步骤定义，其中包含执行操作或验证步骤描述的结果的代码。场景应该是独立的，这意味着它们可以按任何顺序运行，并且不应该依赖于另一个场景生成的状态。这确保了测试的可靠性和可重复性。场景是 [Gherkin](../G/gherkin.md) 中用于描述系统行为的基本构建块，并作为 [BDD](../B/bdd.md) 方法中自动化测试的基础。

#### Gherkin 中的场景和场景大纲有什么区别？

在[Gherkin](../G/gherkin.md) 中，**场景** 表示描述软件的特定情况或[use case](../U/use-case.md) 的单个路径或示例。它使用 `Scenario` 关键字后跟描述性标题进行定义，并包含一系列步骤：`Given`、`When`、`Then`（以及可选的`And`、`But`）。

  ```
  Scenario: User logs in with valid credentials
    Given the login page is displayed
    When the user enters valid credentials
    Then the user is redirected to the dashboard
  ```另一方面，当您想要使用不同的数据集多次运行相同的场景时，可以使用**场景大纲**。它是用 `Scenario Outline` 关键字定义的，并包括一个包含变量和值表的 `Examples` 部分。 `Examples` 表中的每一行代表一组将用于运行场景的数据，从而有效地创建多个场景。

  ```
  Scenario Outline: User logs in with multiple sets of credentials
    Given the login page is displayed
    When the user enters <username> and <password>
    Then the user is <outcome>
  Examples:
    | username | password | outcome          |
    | user1    | pass1    | redirected to the dashboard |
    | user2    | pass2    | shown an error message      |
  ```主要区别在于 **Scenario** 适用于单个示例，而 **Scenario Outline** 适用于多个示例，其中模板由 `Examples` 表中的数据填充。这样可以使用不同的数据输入对类似场景进行更高效、更全面的测试。

#### Gherkin场景下如何传递参数？

[Gherkin](../G/gherkin.md) 场景中的参数使用 **场景大纲** 和 **示例** 表进行传递。场景大纲是一个模板，其中填充了示例表中的值。示例表中的每一行代表一组将用于运行场景大纲的参数。
  以下是传递参数的基本语法：

  ```
  Scenario Outline: Descriptive name of the scenario
    Given some initial context <param1>
    When an action is carried out <param2>
    Then a particular set of observable consequences should occur <param3>
  Examples:
    | param1 | param2 | param3 |
    | value1 | value2 | value3 |
    | value4 | value5 | value6 |
  ```在上述结构中，`<param1>`、`<param2>` 和`<param3>` 是场景大纲步骤中的占位符。执行场景时，这些占位符将替换为示例表中的相应值。示例表中的每一行都将导致使用指定参数单独执行场景大纲。
  这种方法允许数据驱动的测试，无需编写多个场景即可测试多组数据。它保持场景的可读性和可维护性，同时还提供了覆盖各种输入组合的灵活性。

#### Gherkin 中标签的用途是什么？

[Gherkin](../G/gherkin.md) 中的标签充当强大的组织工具，允许对场景进行分类和过滤。通过在方案或功能前面加上 `@` 符号和标签名称作为前缀，您可以将相关方案分组在一起，无论它们在功能文件中的位置如何。当您想要运行共享公共属性的特定测试子集（例如表示特定冲刺的标签、测试类型（例如`@smoke`、`@regression`）或特定功能区域）时，这特别有用。
  例如：

  ```
  @billing
  Feature: Refund transaction
    @smoke
    Scenario: Refund a transaction successfully
      Given a transaction exists
      When I issue a refund
      Then the refund should be processed
    @regression
    Scenario: Refund fails for canceled transactions
      Given a canceled transaction exists
      When I attempt to issue a refund
      Then the refund should be rejected
  ```在上面的示例中，`@billing` 标记可用于运行所有与计费相关的测试，而`@smoke` 和`@regression` 可用于在整个[test suite](../T/test-suite.md) 上运行特定类型的测试。标签还允许您根据场景所携带的标签包含或排除场景，从而促进跨不同环境或配置执行测试。
  像 Cucumber 这样的自动化工具可以利用这些标签来控制[test execution](../T/test-execution.md)，从而更容易集成到 CI/CD 管道中并随着代码库的增长来管理测试。标签增强了[test automation](../T/test-automation.md) 中[test suites](../T/test-suite.md) 的灵活性和[maintainability](../M/maintainability.md)。

### 高级概念

#### Gherkin 如何与 Cucumber 这样的自动化工具一起使用？

[Gherkin](../G/gherkin.md) 可以与 **Cucumber** 等自动化工具集成，以推动验收测试的自动化。在 [Gherkin](../G/gherkin.md) 中定义应用程序的行为后，Cucumber 使用这些规范来指导自动化过程。
  以下是集成通常的工作方式：

1. **功能文件** : 在中写入 Gherkin 场景
    `.feature`
    文件。

2. **步骤定义**：以 Cucumber 支持的编程语言（例如 Java、Ruby、JavaScript）实现步骤定义。 Gherkin 场景中的每个步骤都映射到将执行该操作的一段代码。

  ```
  @When("^the user logs in with username and password$")
  public void the_user_logs_in_with_username_and_password() {
      // Code to automate login action
  }
  ```

1. **运行测试**：使用Cucumber执行功能文件。 Cucumber 读取 [Gherkin](../G/gherkin.md) 步骤并将其与相应的步骤定义进行匹配以运行测试。
  2. **断言**：在步骤定义中，包括用于验证 [expected results](../E/expected-result.md) 结果的断言。

  ```
  @Then("^the user should be directed to the dashboard$")
  public void the_user_should_be_directed_to_the_dashboard() {
      // Assertion to verify the user is on the dashboard
  }
  ```

1. **钩子**：为[setup](../S/setup.md)和拆卸过程使用钩子（`@Before`、`@After`），例如在场景之前启动Web驱动程序并在场景之后关闭它。
  2. **标签**：使用 [Gherkin](../G/gherkin.md) 场景中定义的标签执行选择性测试，以实现高效 [test management](../T/test-management.md)。
  3. **报告**：[test execution](../T/test-execution.md) 之后，Cucumber 生成报告，提供对测试结果的深入了解，这对技术和非技术利益相关者都很有用。
  通过遵循这种方法，[test automation](../T/test-automation.md) 工程师可以创建一个健壮、可读且可维护的[test suite](../T/test-suite.md)，它与[BDD](../B/bdd.md) 方法保持一致，并促进跨团队协作。

1. **功能文件** : 在中写入 Gherkin 场景
    `.feature`
    文件。

2. **步骤定义**：以 Cucumber 支持的编程语言（例如 Java、Ruby、JavaScript）实现步骤定义。 Gherkin 场景中的每个步骤都映射到将执行该操作的一段代码。
  1. **运行测试**：使用Cucumber执行功能文件。 Cucumber 读取 [Gherkin](../G/gherkin.md) 步骤并将其与相应的步骤定义进行匹配以运行测试。
  2. **断言**：在步骤定义中，包括用于验证 [expected results](../E/expected-result.md) 结果的断言。
  1. **钩子**：为[setup](../S/setup.md)和拆卸过程使用钩子（`@Before`、`@After`），例如在场景之前启动Web驱动程序并在场景之后关闭它。
  2. **标签**：使用 [Gherkin](../G/gherkin.md) 场景中定义的标签执行选择性测试，以实现高效 [test management](../T/test-management.md)。
  3. **报告**：在[test execution](../T/test-execution.md)之后，Cucumber会生成报告，提供对测试结果的深入了解，这对技术和非技术利益相关者都很有用。

#### 编写 Gherkin 脚本的最佳实践是什么？

编写 [Gherkin](../G/gherkin.md) 脚本的最佳实践包括：

- **具有描述性**：对功能和场景使用清晰的描述性标题。避免使用技术术语。
  - **使用业务语言**：用业务语言编写场景，重点关注行为而不是实现。
  - **保持简单**：每个场景都应该简单并且仅测试一项功能。
  - **避免连词**：不要使用“And”或“But”等连词来链接步骤。每个步骤应该是独立的。
  - **明智地使用背景**：使用
    `Background`
    关键字表示功能文件中所有场景通用的步骤。

- **参数化场景**：使用场景大纲和示例来运行具有不同数据集的相同场景。
  - **保持可读性**：用主动语态编写步骤并确保它们像对话一样流畅。
  - **一致的风格**：在整个 Gherkin 脚本中坚持一致的风格和术语。
  - **使用标签**：应用标签对相关场景进行分组或将它们与特定的测试套件或功能相关联。
  - **限制断言**：理想情况下，每个场景都应该有一个断言，以保持焦点清晰。
  - **定期重构**：定期审查和重构场景以消除重复并提高清晰度。
  - **版本控制**：将 Gherkin 文件存储在版本控制中以跟踪更改并与团队成员协作。

  ```
  Feature: User login
    Background:
      Given the user is on the login page
    @smoke
    Scenario: Successful login with valid credentials
      When the user enters valid credentials
      Then the user is redirected to the dashboard
    @regression
    Scenario Outline: Login with invalid credentials
      When the user enters "<username>" and "<password>"
      Then the user should see an error message
      Examples:
        | username | password |
        | admin    | wrongpw  |
        | user1    |          |
  ```请记住与团队一起审查和调整您的[Gherkin](../G/gherkin.md) 脚本，以确保所有利益相关者的一致性和理解。

- **具有描述性**：对功能和场景使用清晰的描述性标题。避免使用技术术语。
  - **使用业务语言**：用业务语言编写场景，重点关注行为而不是实现。
  - **保持简单**：每个场景都应该简单并且仅测试一项功能。
  - **避免连词**：不要使用“And”或“But”等连词来链接步骤。每个步骤应该是独立的。
  - **明智地使用背景**：使用
    `Background`
    关键字表示功能文件中所有场景通用的步骤。

- **参数化场景**：使用场景大纲和示例来运行具有不同数据集的相同场景。
  - **保持可读性**：用主动语态编写步骤并确保它们像对话一样流畅。
  - **一致的风格**：在整个 Gherkin 脚本中坚持一致的风格和术语。
  - **使用标签**：应用标签对相关场景进行分组或将它们与特定的测试套件或功能相关联。
  - **限制断言**：理想情况下，每个场景都应该有一个断言，以保持焦点清晰。
  - **定期重构**：定期审查和重构场景以消除重复并提高清晰度。
  - **版本控制**：将 Gherkin 文件存储在版本控制中以跟踪更改并与团队成员协作。

#### 如何在 Gherkin 中处理复杂的测试用例？

在[Gherkin](../G/gherkin.md) 中处理复杂的[test cases](../T/test-case.md) 需要一种战略方法来保持可读性并确保场景易于理解。以下是一些提示：

- **如果可能的话，将复杂的场景分解成更小、更易于管理的场景。这有助于将每个场景集中于单一行为或结果。
  - 使用**场景大纲**来处理需要使用不同数据集运行的场景。这可以保持场景干燥（不要重复自己）并避免重复步骤。

  ```
  Scenario Outline: User logs in with different roles
    Given the login page is displayed
    When "<User>" logs in with "<Password>"
    Then the user should be redirected to the "<Role>" dashboard
    Examples:
      | User    | Password | Role    |
      | admin   | admin123 | admin   |
      | editor  | editpass | editor  |
      | viewer  | view123  | viewer  |
  ```

- **抽象常见步骤**
    使用
    `Background`
    关键字表示在同一功能内的多个场景中重复的步骤。

  ```
  Background:
    Given the user is logged in as an admin
  Scenario: Create a new user account
    When the admin creates a new user account
    Then the account should be successfully created
  ```

- **利用标签**
    在测试执行期间组织和过滤复杂的场景。标签可以应用于功能、场景或场景大纲。

  ```
  @smoke
  Scenario: Basic user login
    Given the login page is displayed
    ...
  @regression @login
  Scenario: Login with invalid credentials
    Given the login page is displayed
    ...
  ```

- **模块化步骤定义**
    创建可在不同场景中使用的可重用代码。这允许您从这些模块化步骤组成场景，从而有助于管理复杂性。
  请记住，目标是使[Gherkin](../G/gherkin.md) 场景保持清晰易懂，即使它们代表复杂的[test cases](../T/test-case.md)。

- **如果可能的话，将复杂的场景分解成更小、更易于管理的场景。这有助于将每个场景集中于单一行为或结果。
  - 使用**场景大纲**来处理需要使用不同数据集运行的场景。这可以保持场景干燥（不要重复自己）并避免重复步骤。
  - **抽象常见步骤**
    使用
    `Background`
    关键字表示在同一功能内的多个场景中重复的步骤。

- **利用标签**
    在测试执行期间组织和过滤复杂的场景。标签可以应用于功能、场景或场景大纲。

- **模块化步骤定义**
    创建可在不同场景中使用的可重用代码。这允许您从这些模块化步骤组成场景，从而有助于管理复杂性。

#### Gherkin 在测试自动化方面有哪些局限性？

[Gherkin](../G/gherkin.md) 的人类可读格式既是优点也是限制。它擅长描述行为，但可能难以处理**低级技术细节**。复杂的逻辑或数据操作很难清楚地表达，导致冗长或模糊的场景。
  另一个限制是**[maintainability](../M/maintainability.md)**。随着场景数量的增加，保持场景有序并避免重复变得具有挑战性。在不影响可读性或测试意图的情况下重构可能会很困难。
  [Gherkin](../G/gherkin.md) 的 **冗长** 也可能是一个缺点。为应用程序的各个方面编写详细的场景非常耗时，并且可能会导致功能文件冗长且难以导航。
  此外，[Gherkin](../G/gherkin.md) 并不适合所有类型的测试。它是针对**行为规范**而设计的，因此对于性能或安全性等[non-functional testing](../N/non-functional-testing.md) 来说效果较差。
  每个 [Gherkin](../G/gherkin.md) 步骤需要 **匹配的步骤定义** 可能会导致步骤定义的代码库很大，这需要额外的维护并可能引入冗余。
  最后，[Gherkin](../G/gherkin.md) 对**精确措辞**的依赖可能会导致自动化测试的脆弱性。即使底层行为没有改变，功能措辞的微小变化也可能需要更新相应的步骤定义。
  尽管存在这些限制，[Gherkin](../G/gherkin.md) 仍然是[BDD](../B/bdd.md) 的强大工具，促进协作并为描述和自动化软件行为提供清晰的框架。

#### Gherkin 如何在持续集成/持续部署 (CI/CD) 管道中使用？

[Gherkin](../G/gherkin.md) 可以集成到 CI/CD 管道中，以自动化 [acceptance testing](../A/acceptance-testing.md) 并确保新功能在部署之前遵循指定的行为。通过编写 [Gherkin](../G/gherkin.md) 场景（人类可读的软件行为规范），您可以创建一套可以作为自动化测试运行的可执行规范。
  在 CI/CD 管道中，将代码提交到版本控制系统后，管道会自动触发构建并运行各种测试。以下是 [Gherkin](../G/gherkin.md) 如何适应此过程：

1. **[Test Execution](../T/test-execution.md)**：像Cucumber这样的工具读取[Gherkin](../G/gherkin.md)文件并执行相应的步骤定义，这些定义是将[Gherkin](../G/gherkin.md)步骤与自动化代码相匹配的脚本。
  2. **集成**：通过配置构建服务器以在成功构建后运行 Cucumber [test suite](../T/test-suite.md)，将 [Gherkin](../G/gherkin.md) 场景集成到管道中。
  3. **反馈循环**：如果[Gherkin](../G/gherkin.md)方案失败，管道将停止，并通知开发人员修复问题。这可确保仅部署通过所有已定义行为的代码。
  4. **[Regression Testing](../R/regression-testing.md)**：[Gherkin](../G/gherkin.md) 场景在每次更改时都会重新执行，以尽早捕获回归。
  5. **文档**：[Gherkin](../G/gherkin.md) 场景充当实时文档，始终与应用程序的当前状态保持同步。
  6. **并行执行**：为了加快管道速度，[Gherkin](../G/gherkin.md) 场景可以跨多个[test environments](../T/test-environment.md) 并行执行。
  7. **标记**：[Gherkin](../G/gherkin.md) 中的标记允许选择性 [test execution](../T/test-execution.md)，可用于将测试分类为流程中的冒烟、回归或特定功能套件。
  通过将 [Gherkin](../G/gherkin.md) 纳入 CI/CD 流程，团队可确保软件按预期运行，并尽早发现任何偏差，从而在每个版本中保持高质量标准。

1. **[Test Execution](../T/test-execution.md)**：像Cucumber这样的工具读取[Gherkin](../G/gherkin.md)文件并执行相应的步骤定义，这些定义是将[Gherkin](../G/gherkin.md)步骤与自动化代码相匹配的脚本。
  2. **集成**：通过配置构建服务器以在成功构建后运行 Cucumber [test suite](../T/test-suite.md)，将[Gherkin](../G/gherkin.md) 场景集成到管道中。
  3. **反馈循环**：如果[Gherkin](../G/gherkin.md)方案失败，管道将停止，并通知开发人员修复问题。这可确保仅部署通过所有已定义行为的代码。
  4. **[Regression Testing](../R/regression-testing.md)**：[Gherkin](../G/gherkin.md) 场景在每次更改时都会重新执行，以尽早捕获回归。
  5. **文档**：[Gherkin](../G/gherkin.md) 场景充当动态文档，始终与应用程序的当前状态保持同步。
  6. **并行执行**：为了加快管道速度，[Gherkin](../G/gherkin.md) 场景可以跨多个[test environments](../T/test-environment.md) 并行执行。
  7. **标记**：[Gherkin](../G/gherkin.md) 中的标记允许选择性 [test execution](../T/test-execution.md)，可用于将测试分类为管道内的冒烟、回归或特定功能套件。
