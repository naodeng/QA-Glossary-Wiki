# 用例

<!-- TOC START -->
- [相关术语：](#相关术语：)
- [有关用例的问题吗？](#有关用例的问题吗？)
  - [基础知识和重要性](#基础知识和重要性)
    - [软件测试中的用例是什么？](#软件测试中的用例是什么？)
    - [为什么用例在软件开发中很重要？](#为什么用例在软件开发中很重要？)
    - [用例的关键组成部分是什么？](#用例的关键组成部分是什么？)
    - [用例如何帮助理解系统功能？](#用例如何帮助理解系统功能？)
    - [用例和测试用例有什么区别？](#用例和测试用例有什么区别？)
  - [用例图](#用例图)
    - [什么是用例图？](#什么是用例图？)
    - [用例图的元素是什么？](#用例图的元素是什么？)
    - [如何创建用例图？](#如何创建用例图？)
    - [用例图中参与者的角色是什么？](#用例图中参与者的角色是什么？)
    - [用例图如何帮助系统设计？](#用例图如何帮助系统设计？)
  - [用例场景](#用例场景)
    - [什么是用例场景？](#什么是用例场景？)
    - [用例场景与用例有何不同？](#用例场景与用例有何不同？)
    - [如何编写用例场景？](#如何编写用例场景？)
    - [用例场景在软件测试中的作用是什么？](#用例场景在软件测试中的作用是什么？)
    - [用例场景如何帮助识别系统中的潜在问题？](#用例场景如何帮助识别系统中的潜在问题？)
  - [高级概念](#高级概念)
    - [什么是用例套件？](#什么是用例套件？)
    - [用例和用户故事之间有什么区别？](#用例和用户故事之间有什么区别？)
    - [用例在敏捷开发中的作用是什么？](#用例在敏捷开发中的作用是什么？)
    - [如何在非功能测试中使用用例？](#如何在非功能测试中使用用例？)
    - [编写用例时要避免哪些常见错误？](#编写用例时要避免哪些常见错误？)
<!-- TOC END -->

详细描述用户如何与系统交互的描述。它为系统开发和测试奠定了基础。

## 相关术语：

- [Use Case Testing](../U/use-case-testing.md)

## 有关用例的问题吗？

### 基础知识和重要性

#### 软件测试中的用例是什么？

在[software testing](../S/software-testing.md)中，**[use case](../U/use-case.md)**是参与者（用户或其他系统）对系统的特定使用的描述。它概述了实现特定目标所需的参与者和系统之间的交互顺序。 [Use cases](../U/use-case.md) 在[functional testing](../F/functional-testing.md) 中发挥了重要作用，因为它们从最终用户的角度定义了系统必须满足的要求。
  [use case](../U/use-case.md) 通常包括**主要成功场景**（标准事件流程），并且还可以描述**替代流程**和**例外流程**，涵盖不同的使用场景和错误条件。这种全面的覆盖范围确保从 [use cases](../U/use-case.md) 派生的测试可以验证系统在各种条件下的行为是否正确。
  [Use cases](../U/use-case.md) 不仅仅是关于[happy path](../H/happy-path.md)；它们还封装了场景开始之前必须满足的**前提条件**以及场景完成后应该满足的**[postconditions](../P/postcondition.md)**。这有助于设置[test environments](../T/test-environment.md) 并评估[test executions](../T/test-execution.md) 的结果。
  在[test automation](../T/test-automation.md) 中，[use cases](../U/use-case.md) 指导自动[test scripts](../T/test-script.md) 的创建。这些脚本模拟参与者的操作和输入以验证系统的响应。通过自动化[use cases](../U/use-case.md)，测试人员可以有效地为[regression testing](../R/regression-testing.md)重复这些场景，确保新的更改不会破坏现有功能。
  虽然[use cases](../U/use-case.md) 专注于用户交互，但他们也可以通过强调性能和可用性注意事项来通知[non-functional testing](../N/non-functional-testing.md)。例如，描述大容量事务场景的 [use case](../U/use-case.md) 可以导致模拟重负载条件的性能测试。

#### 为什么用例在软件开发中很重要？

[Use cases](../U/use-case.md) 在软件开发中至关重要，因为它们提供了一种**结构化的方式来捕获[functional requirements](../F/functional-requirements.md)**。它们描述了用户如何与系统交互，提供了预期行为和结果的清晰画面。这有助于**定义系统的范围**并确保考虑所有利益相关者的期望。
  在[test automation](../T/test-automation.md) 的上下文中，[use cases](../U/use-case.md) 充当创建**综合[test plans](../T/test-plan.md)** 的基础。它们有助于确定要测试的关键路径，并确保系统在真实用户使用时按预期运行。通过关注用户交互，[use cases](../U/use-case.md) 使测试人员能够确定优先级并设计涵盖**关键功能**的测试。
  此外，[use cases](../U/use-case.md) 通过提供易于理解的通用语言，促进团队成员之间的**沟通**​​。这在**跨职能团队**中尤其重要，因为成员可能拥有不同的专业领域。 [Use cases](../U/use-case.md) 有助于弥合技术和非技术利益相关者之间的差距，确保每个人对系统应该做什么有共同的理解。
  总之，[use cases](../U/use-case.md) 很重要，因为它们：

- 定义系统范围和功能。
  - 帮助创建有效的自动化测试计划。
  - 根据用户交互确定测试的优先级。
  - 加强团队之间的沟通和理解。
  通过关注用户交互和结果，[use cases](../U/use-case.md) 有助于开发强大的、以用户为中心的软件系统以及创建有效的自动化测试。

- 定义系统范围和功能。
  - 帮助创建有效的自动化测试计划。
  - 根据用户交互确定测试的优先级。
  - 加强团队之间的沟通和理解。

#### 用例的关键组成部分是什么？

[use case](../U/use-case.md) 的关键组件包括：

- **标题**：一个清晰的描述性名称，封装了用例的目的。
  - **主要参与者**：启动用例的主要实体，通常是用户角色或外部系统。
  - **利益相关者和利益**：在用例结果中拥有既得利益的其他实体的列表。
  - **先决条件**：在启动用例之前必须满足的条件。
  - **[Postconditions](../P/postcondition.md)** ：成功完成用例后必须满足的条件。
  - **主要成功场景**：逐步叙述，描述实现目标的标准事件流程。
  - **扩展**：可能发生的替代流程，包括异常和错误情况。
  - **特殊要求**：任何相关的非功能性要求或约束，例如性能标准或法规遵从性。
  - **使用频率**：表明用例可能启动的频率。
  - **杂项**：任何其他相关信息，例如数据变化或相关业务规则。
  这些组件确保[use cases](../U/use-case.md)是全面的，并提供对参与者和系统之间交互的清晰理解。它们充当创建 [test cases](../T/test-case.md) 和验证系统预期行为的场景的基础。

- **标题**：一个清晰的描述性名称，封装了用例的目的。
  - **主要参与者**：启动用例的主要实体，通常是用户角色或外部系统。
  - **利益相关者和利益**：在用例结果中拥有既得利益的其他实体的列表。
  - **先决条件**：在启动用例之前必须满足的条件。
  - **[Postconditions](../P/postcondition.md)** ：成功完成用例后必须满足的条件。
  - **主要成功场景**：逐步叙述，描述实现目标的标准事件流程。
  - **扩展**：可能发生的替代流程，包括异常和错误情况。
  - **特殊要求**：任何相关的非功能性要求或约束，例如性能标准或法规遵从性。
  - **使用频率**：表明用例可能启动的频率。
  - **杂项**：任何其他相关信息，例如数据变化或相关业务规则。

#### 用例如何帮助理解系统功能？

[Use cases](../U/use-case.md) 通过提供用户如何与系统交互以实现特定目标的**结构化描述**，促进对系统功能的**深入理解**。他们提供了一个**叙述**，指导测试人员完成一系列步骤，揭示系统在各种条件下的**预期行为**。这种叙述有助于测试人员**设想**用户的观点，并**验证**系统支持所有预期的[use cases](../U/use-case.md)，确保满足**[functional requirements](../F/functional-requirements.md)**。
  通过概述用户（参与者）和系统之间的**交互**，[use cases](../U/use-case.md) 帮助**识别**需要彻底测试的**关键路径**。它们还**突出**系统不同部分之间的依赖关系和**交互**，这对于设计**集成测试**至关重要。
  在[test automation](../T/test-automation.md) 中，[use cases](../U/use-case.md) 对于**定义自动化测试的范围**很有帮助。它们可以直接转换为**自动化[test scripts](../T/test-script.md)**来模拟用户的操作，为通过或失败测试提供**明确的标准**。 [use cases](../U/use-case.md) 和自动化测试之间的这种一致性确保了自动化工作**集中**并且与用户的需求**相关**。
  此外，通过将自动化测试与[use cases](../U/use-case.md) 的全范围进行比较，[use cases](../U/use-case.md) 可用于**检测[test coverage](../T/test-coverage.md) 中的间隙**。这种比较可以揭示**未经测试的路径**或**场景**，从而促使创建额外的自动化测试来覆盖这些领域。
  总之，[use cases](../U/use-case.md) 是了解系统功能并确保 [test automation](../T/test-automation.md) 工作与用户需求和系统行为**一致**的**重要工具**。

#### 用例和测试用例有什么区别？

**[use case](../U/use-case.md)** 是从最终用户角度对系统功能的高级描述。它概述了参与者（用户或其他系统）和系统之间为实现目标而进行的交互。 [Use cases](../U/use-case.md) 关注系统行为的**意图**和**目的**，而不详细说明实现它的具体步骤。
  相反，**[test case](../T/test-case.md)** 是一组条件和变量，测试人员将在这些条件和变量下确定被测系统是否满足要求或正常工作。 [Test cases](../T/test-case.md) 更加细化，包括详细的输入、执行步骤和[expected results](../E/expected-result.md)。它们旨在验证软件的实施，确保其满足指定的要求。
  [use cases](../U/use-case.md) 是关于系统应该做什么**，而[test cases](../T/test-case.md) 是关于**如何** 验证系统是否执行其应该执行的操作。 [Test cases](../T/test-case.md) 源自[use cases](../U/use-case.md) 和其他规范，例如[functional requirements](../F/functional-requirements.md)。它们对于系统测试至关重要，通常包括正面和负面场景，以确保全面覆盖。
  总之，[use cases](../U/use-case.md) 描述了**所需的系统交互**，并作为创建 [test cases](../T/test-case.md) 的基础，这是验证这些交互的**实际步骤**。 [Test automation](../T/test-automation.md) 工程师使用[use cases](../U/use-case.md) 来了解系统功能的范围和上下文，然后开发[test cases](../T/test-case.md) 来自动化该功能的[verification](../V/verification.md)。

### 用例图

#### 什么是用例图？

**[use case](../U/use-case.md) 图**是**外部参与者**与正在开发的**系统**之间交互的直观表示。它描绘了用户（参与者）与系统交互以实现目标的各种方式，从外部角度突出了系统的功能。
  在[test automation](../T/test-automation.md) 的上下文中，[use case](../U/use-case.md) 图充当识别[test scenarios](../T/test-scenario.md) 的高级指南。它包括**参与者**（用户或其他系统）、**[use cases](../U/use-case.md)**（参与者想要实现的目标）和**关联**（将参与者连接到他们所参与的[use cases](../U/use-case.md)的线路）。或者，它还可以描述**系统边界**（以描绘系统的范围），以及**包含**或**扩展**关系（以显示[use cases](../U/use-case.md)之间的共享或条件步骤）。
  通过可视化交互和关系，该图有助于确保在 [test case](../T/test-case.md) 创建过程中考虑所有功能路径。它还可以揭示可能影响测试策略的复杂性和依赖性。
  以下是 [use case](../U/use-case.md) 图表语法的简单示例：

  ```
  @startuml
  left to right direction
  actor Customer
  actor Bank
  rectangle BankingSystem {
    Customer -- (Withdraw Money)
    Customer -- (Deposit Money)
    (Transfer Funds) .> (Withdraw Money) : extends
    Bank -- (Create Account)
  }
  @enduml
  ```此 UML（统一建模语言）片段将生成一个图表，显示客户与银行系统交互以提取和存入资金，以及可以创建帐户的银行参与者。 “转账”[use case](../U/use-case.md)是“提款”[use case](../U/use-case.md)的延伸，表示转账包括提款的步骤。

#### 用例图的元素是什么？

[use case](../U/use-case.md) 图的元素包括：

- **Actors** ：代表与系统交互的外部实体，例如用户或其他系统。
  - **[Use Cases](../U/use-case.md)** ：描述参与者与系统之间为实现目标而进行的交互的省略号。
  - **系统边界**：框架用例的矩形，定义系统的范围。
  - **关联**：将参与者连接到用例的线，表示参与交互。
  - **包含**：带有虚线的定向箭头，表明一个用例包含另一个用例的功能。
  - **扩展**：带有虚线的有向箭头，表示一个用例在某些条件下扩展另一个用例。
  - **泛化**：带有空心箭头的实线，说明参与者或用例之间的继承。
  [Use case](../U/use-case.md) 图是指定系统内参与者和 [use cases](../U/use-case.md) 之间的关系和交互的可视化表示。它们充当讨论和管理系统需求的工具。

- **Actors** ：代表与系统交互的外部实体，例如用户或其他系统。
  - **[Use Cases](../U/use-case.md)** ：描述参与者与系统之间为实现目标而进行的交互的省略号。
  - **系统边界**：框架用例的矩形，定义系统的范围。
  - **关联**：将参与者连接到用例的线，表示参与交互。
  - **包含**：带有虚线的定向箭头，表明一个用例包含另一个用例的功能。
  - **扩展**：带有虚线的有向箭头，表示一个用例在某些条件下扩展另一个用例。
  - **泛化**：带有空心箭头的实线，说明参与者或用例之间的继承。

#### 如何创建用例图？

创建**[use case](../U/use-case.md) 图**涉及以下步骤：

1. **标识系统边界**：定义系统内部和外部的内容，通常用矩形表示。
  2. **确定参与者**：列出与系统交互的所有外部实体。参与者可以是用户或其他系统。
  3. **找到[use cases](../U/use-case.md)**：枚举系统应为每个参与者执行的所有功能。
  4. **将演员连接到[use cases](../U/use-case.md)**：在演员和他们各自的[use cases](../U/use-case.md)之间画线以显示交互。
  5. **包含关系**：必要时使用包含、扩展或泛化关系来显示 [use cases](../U/use-case.md) 之间的依赖关系。
  6. **审查和验证**：确保图表准确地表示所有用户交互和系统功能。
  这是一个使用文本描述的 Markdown 简单示例：

  ```
  # Use Case Diagram Example
  ## System Boundary
  Rectangle: Online Shopping System
  ## Actors
  - Customer
  - Payment Gateway
  ## Use Cases
  - Browse Items
  - Add Item to Cart
  - Checkout
  - Make Payment
  ## Connections
  - Customer -> Browse Items
  - Customer -> Add Item to Cart
  - Customer -> Checkout
  - Checkout -> Make Payment
  - Make Payment -> Payment Gateway
  ## Relationships
  - Checkout -> Make Payment (include)
  ```请记住保持图表**简单**并**关注**用户交互。避免出现太多细节混乱，这些细节可以保留用于更详细的 [use case](../U/use-case.md) 场景或其他图表。

1. **标识系统边界**：定义系统内部和外部的内容，通常用矩形表示。
  2. **确定参与者**：列出与系统交互的所有外部实体。参与者可以是用户或其他系统。
  3. **找到[use cases](../U/use-case.md)**：枚举系统应为每个参与者执行的所有功能。
  4. **将演员连接到[use cases](../U/use-case.md)**：在演员和他们各自的[use cases](../U/use-case.md)之间画线以显示交互。
  5. **包含关系**：必要时使用包含、扩展或泛化关系来显示 [use cases](../U/use-case.md) 之间的依赖关系。
  6. **审查和验证**：确保图表准确地表示所有用户交互和系统功能。

#### 用例图中参与者的角色是什么？

在 [use case](../U/use-case.md) 图中，**参与者**表示与系统交互的角色，包括用户和其他系统。它们是通过请求系统执行功能来启动[use case](../U/use-case.md) 的外部实体。参与者有助于定义系统的边界，并明确谁或什么将与系统交互。它们不是系统本身的一部分，但对于指定系统的上下文和要求至关重要。在[test automation](../T/test-automation.md) 中，了解参与者对于确定测试系统的不同角度至关重要，确保在[test cases](../T/test-case.md) 中考虑到所有用户交互。

#### 用例图如何帮助系统设计？

[use case](../U/use-case.md) 图通过从用户的角度提供系统功能的**视觉表示**来帮助系统设计。它有助于识别不同参与者和系统之间的**交互**，确保在设计中考虑到所有用户交互。该可视化工具突出显示了**系统范围**，阐明了包含哪些功能以及哪些功能在系统边界之外。
  通过规划[use cases](../U/use-case.md)，设计人员可以发现系统不同部分之间的**冗余**和**依赖关系**，这可以导致更加**模块化**和**可扩展**的架构。它还促进利益相关者之间的**沟通**​​，因为该图很容易被技术和非技术团队成员理解，从而弥合了用户需求和系统开发人员之间的差距。
  在 [test automation](../T/test-automation.md) 的上下文中，该图充当创建与用户交互一致的 **[test plans](../T/test-plan.md)** 和 **[test scripts](../T/test-script.md)** 的基础。它确保[test cases](../T/test-case.md)涵盖[use cases](../U/use-case.md)代表的所有功能，从而形成全面的[test coverage](../T/test-coverage.md)。此外，它还可用于根据现实场景中 [use case](../U/use-case.md) 的频率和重要性来 **确定 [test cases](../T/test-case.md)** 的优先级，从而优化测试工作。
  总体而言，[use case](../U/use-case.md) 图是系统设计中的一种战略工具，有助于实现以用户为中心的方法，确保最终产品符合用户的需求和期望，同时促进结构化且高效的测试过程。

### 用例场景

#### 什么是用例场景？

**[use case](../U/use-case.md) 场景**是详细的叙述，描述用户（或“参与者”）和系统之间为实现特定目标而进行的交互。它概述了参与者完成任务所采取的一系列步骤，包括任何系统响应。与可能包含多个场景的更广泛的 [use case](../U/use-case.md) 不同，[use case](../U/use-case.md) 场景专注于单个事件流。
  [Use case](../U/use-case.md) 场景对于**[test automation](../T/test-automation.md)** 很有帮助，因为它们为创建[test scripts](../T/test-script.md) 提供了基础。它们有助于可视化功能的端到端功能，可以将其转换为自动化[test cases](../T/test-case.md)。这些场景确保自动化测试涵盖应用程序的实际使用情况。
  以下是 Markdown 格式的 [use case](../U/use-case.md) 场景示例：

  ```
  **Title:** Withdraw Cash from ATM
  **Primary Actor:** Bank Customer
  **Preconditions:**
  - The ATM is operational.
  - The customer has a valid bank card and PIN.
  **Main Flow:**
  1. Customer inserts their bank card.
  2. System prompts for the PIN.
  3. Customer enters the PIN.
  4. System validates the PIN and displays transaction options.
  5. Customer selects 'Withdraw Cash'.
  6. System prompts for the amount.
  7. Customer enters the amount.
  8. System dispenses cash and prints a receipt.
  9. Customer takes the cash and receipt.
  10. System ejects the bank card.
  11. Customer takes the card.
  **Postconditions:**
  - Customer has received the correct amount of cash.
  - The customer's account balance is updated.
  - The ATM is ready for the next transaction.
  ```在[test automation](../T/test-automation.md) 中，此类场景对于定义[test cases](../T/test-case.md) 的范围并确保自动化测试准确反映用户交互至关重要。它们还有助于在边缘情况和潜在系统问题影响最终用户之前识别它们。

#### 用例场景与用例有何不同？

**[use case](../U/use-case.md)** 通过描述**参与者**（用户或其他系统）与系统本身之间的交互来实现目标，从而概述了系统的[functional requirements](../F/functional-requirements.md)。这是一个相对抽象的高级描述，重点关注交互的意图和最终结果。
  相比之下，**[use case](../U/use-case.md) 场景**是特定的叙述或事件流，说明了通过[use case](../U/use-case.md) 的单一路径。它提供了参与者行为和系统响应的详细、逐步说明。 [Use case](../U/use-case.md) 场景是具体示例，展示了如何在实践中满足要求。
  [use case](../U/use-case.md) 可能会声明用户可以处理事务，而 [use case](../U/use-case.md) 场景将详细说明处理该事务的步骤，例如登录、输入事务详细信息、提交事务进行处理以及接收确认​​。
  [Use case](../U/use-case.md) 场景在[test automation](../T/test-automation.md) 中特别有用，因为它们将[use case](../U/use-case.md) 的抽象需求转换为有形的[test scripts](../T/test-script.md)。每个场景都可以作为 [test case](../T/test-case.md) 的基础，确保系统在特定情况下按预期运行。
  下面是一个例子来说明差异：
  **[Use Case](../U/use-case.md)**：用户管理他们的个人资料。
  **[Use Case](../U/use-case.md) 场景**：

1. 用户登录系统。
  2. 用户导航至个人资料管理页面。
  3. 用户更新他们的电子邮件地址。
  4. 用户保存更改。
  5. 系统确认更新。
  该场景为[test automation](../T/test-automation.md) 提供了清晰的序列，而[use case](../U/use-case.md) 则定义了更广泛的功能。

1. 用户登录系统。
  2. 用户导航至个人资料管理页面。
  3. 用户更新他们的电子邮件地址。
  4. 用户保存更改。
  5. 系统确认更新。

#### 如何编写用例场景？

编写 [use case](../U/use-case.md) 场景涉及详细说明用户或系统为实现应用程序中的特定目标而采取的步骤。这是一个简洁的指南：

1. **识别参与者**：确定谁正在与系统交互（例如，用户、外部系统）。
  2. **定义目标**：明确说明参与者试图实现的目标。
  3. **设置先决条件**：列出启动场景之前必须满足的所有条件。
  4. **列举主要流程**：概述参与者为实现目标而采取的主要步骤顺序。为了清晰起见，请使用简单的编号句子。
  5. **描述替代流程**：捕获主流流程的任何变化，处理不同的选择或异常。
  6. **指定[Postconditions](../P/postcondition.md)**：描述[use case](../U/use-case.md)完成后系统的状态，确保达到目标。
  7. **包括成功标准**：从参与者的角度定义什么将使 [use case](../U/use-case.md) 成功。
  以下是登录 [use case](../U/use-case.md) 场景的简化示例：

  ```
  Actor: User
  Goal: Successfully log into the system
  Preconditions:
  - User is registered.
  - Login page is accessible.
  Main Flow:
  1. User navigates to the login page.
  2. User enters username and password.
  3. User clicks the login button.
  4. System validates credentials.
  5. User is redirected to the homepage.
  Alternative Flows:
  A. Invalid credentials:
     1. System displays an error message.
     2. User can attempt to re-enter credentials.
  Postconditions:
  - User is logged in and has access to the system.
  Success Criteria:
  - User gains access to the homepage within 5 seconds after clicking the login button.
  ```请记住保持场景**现实**并**关注**用户交互，避免使用技术术语以确保利益相关者的清晰度。

1. **识别参与者**：确定谁正在与系统交互（例如，用户、外部系统）。
  2. **定义目标**：明确说明参与者试图实现的目标。
  3. **设置先决条件**：列出启动场景之前必须满足的所有条件。
  4. **列举主要流程**：概述参与者为实现目标而采取的主要步骤顺序。为了清晰起见，请使用简单的编号句子。
  5. **描述替代流程**：捕获主流流程的任何变化，处理不同的选择或异常。
  6. **指定[Postconditions](../P/postcondition.md)**：描述[use case](../U/use-case.md)完成后系统的状态，确保达到目标。
  7. **包括成功标准**：从参与者的角度定义什么将使 [use case](../U/use-case.md) 成功。

#### 用例场景在软件测试中的作用是什么？

在[software testing](../S/software-testing.md) 中，**[use case](../U/use-case.md) 场景**在指导 **[test scripts](../T/test-script.md)** 和 **[test cases](../T/test-case.md)** 的创建方面发挥着至关重要的作用。它提供了一系列详细的步骤，表示参与者（通常是用户）和系统之间的特定交互，以实现目标。这个详细的叙述包括**前提条件**、**触发器**和**[postconditions](../P/postcondition.md)**，为测试人员提供了清晰的遵循路径。
  [Use case](../U/use-case.md) 场景在 **[functional testing](../F/functional-testing.md)** 中非常有用，因为它们确保所有 [functional requirements](../F/functional-requirements.md) 都通过现实世界的模拟进行验证。它们有助于发现通过独立的单元测试可能不明显的**功能缺陷**和**工作流程问题**。通过涵盖各种可能的路径，包括**替代流程**和**异常路径**，[use case](../U/use-case.md)场景使测试人员能够执行彻底的**边界值**和**[negative testing](../N/negative-testing.md)**。
  此外，它们还作为**自动回归测试**的基础，确保新的更改不会破坏现有功能。测试人员可以自动化场景，以在每次[iteration](../I/iteration.md) 或部署后快速验证系统的行为。
  在 **[performance testing](../P/performance-testing.md)** 中，场景有助于对负载和压力条件下的用户行为进行建模。它们可用于为虚拟用户编写操作脚本，以模拟现实世界的使用模式，从而识别性能瓶颈。
  最后，[use case](../U/use-case.md) 场景通过代表用户的观点来为 **[user acceptance testing](../U/user-acceptance-testing.md) (UAT)** 做出贡献，这对于确保系统在上线前满足业务需求和用户期望至关重要。

#### 用例场景如何帮助识别系统中的潜在问题？

[Use case](../U/use-case.md) 场景有助于通过模拟系统的实际使用情况来识别潜在问题。它们提供了一个**叙述**，描述用户如何与系统交互以实现目标。这个叙述有助于揭示：

- **边缘案例**：场景可以突出显示用户可能采取的不太明显的路径或交互，这些路径或交互经常被忽视，但可能会导致意外行为。
  - **集成点**：它们揭示系统如何与外部系统或模块交互，查明潜在的集成问题。
  - **用户体验问题**：通过逐步完成用户所执行的步骤，场景可能会揭示出可能导致用户错误的繁琐或不直观的工作流程。
  - **安全漏洞**：它们可以通过概述不同类型的用户如何与系统交互来帮助识别与安全相关的场景，例如访问控制问题或数据隐私问题。
  - **性能瓶颈**：涉及复杂交互或高数据负载的场景可以帮助识别实际条件下的性能问题。
  - **需求差距**：通过详细说明具体的操作和结果，[use case](../U/use-case.md) 场景可以暴露缺失的需求或对预期功能的误解。
  - **回归效应**：当系统发生更改时，场景有助于确保现有功能不受影响，从而揭示潜在的回归问题。
  将[use case](../U/use-case.md) 场景纳入[test automation](../T/test-automation.md) 策略可确保测试以用户为中心并专注于实际应用程序，从而形成更强大、更可靠的系统。

- **边缘案例**：场景可以突出显示用户可能采取的不太明显的路径或交互，这些路径或交互经常被忽视，但可能会导致意外行为。
  - **集成点**：它们揭示系统如何与外部系统或模块交互，查明潜在的集成问题。
  - **用户体验问题**：通过逐步完成用户所执行的步骤，场景可能会揭示出可能导致用户错误的繁琐或不直观的工作流程。
  - **安全漏洞**：它们可以通过概述不同类型的用户如何与系统交互来帮助识别与安全相关的场景，例如访问控制问题或数据隐私问题。
  - **性能瓶颈**：涉及复杂交互或高数据负载的场景可以帮助识别实际条件下的性能问题。
  - **需求差距**：通过详细说明具体的操作和结果，[use case](../U/use-case.md) 场景可以暴露缺失的需求或对预期功能的误解。
  - **回归效应**：当系统发生更改时，场景有助于确保现有功能不受影响，从而揭示潜在的回归问题。

### 高级概念

#### 什么是用例套件？

**[use case](../U/use-case.md) 套件** 是相关[use cases](../U/use-case.md) 的集合，分组用于在软件[test automation](../T/test-automation.md) 期间将它们作为一个整体进行管理和执行。它充当一组有组织的场景，涵盖特定的特性、功能或系统方面。套件中的每个[use case](../U/use-case.md)代表被测系统的不同路径或变体，确保全面覆盖。
  在[test automation](../T/test-automation.md) 中，[use case](../U/use-case.md) 套件通常被实现为一组一起执行的自动化[test scripts](../T/test-script.md)。该套件可以定制以验证一组特定的需求或模拟特定的用户旅程。通过运行 [use case](../U/use-case.md) 套件，[test automation](../T/test-automation.md) 工程师可以验证系统在多种场景和条件下的行为是否符合预期。
  以下是如何在代码中表示 [use case](../U/use-case.md) 套件的示例：

  ```
  describe('Login Use Case Suite', () => {
    it('should allow a user with valid credentials to log in', () => {
      // Test code for valid login
    });
    it('should reject a user with invalid credentials', () => {
      // Test code for invalid login
    });
    it('should lock the account after multiple failed login attempts', () => {
      // Test code for account lock
    });
    // Additional use case scenarios...
  });
  ```在此示例中，`describe` 块定义了套件，每个`it` 块代表该套件中的一个单独的[use case](../U/use-case.md) 场景。通过对相关场景进行分组，工程师可以更轻松地管理和维护他们的[test automation](../T/test-automation.md)工作。

#### 用例和用户故事之间有什么区别？

**[use case](../U/use-case.md)** 是对用户如何与系统交互以实现特定目标的详细描述，通常捕获系统在各种条件下的行为。它包括主要的成功场景以及替代路径和例外情况，重点关注用户（参与者）和系统之间的交互。
  相比之下，**用户故事**是从需要新功能的人（通常是系统的用户或客户）的角度讲述的对功能的简短描述。用户故事通常以非正式的自然语言编写，并遵循一个简单的模板：“作为[用户类型]，我想要[采取行动]，以便[获得利益/价值]。”它们是 [Agile development](../A/agile-development.md) 中使用的工具，用于从最终用户的角度捕获产品功能。
  [use cases](../U/use-case.md) 提供了一种结构化且详细的方法来捕获[functional requirements](../F/functional-requirements.md) 和系统使用场景，而用户故事则提供了一种快速的对话式方法，可以捕获用户需求的本质。用户故事更多地是关于“什么”和“为什么”，而[use cases](../U/use-case.md) 则深入研究“如何”。用户故事通常伴随着验收标准，这是故事被认为是完整的必须满足的一组条件。
  在[test automation](../T/test-automation.md) 中，用户故事可以指导[test scenarios](../T/test-scenario.md) 的创建，重点关注用户的预期结果和收益，而[use cases](../U/use-case.md) 可以为更全面的测试提供信息，包括替代流程和异常处理。

#### 用例在敏捷开发中的作用是什么？

在[Agile development](../A/agile-development.md) 中，[use cases](../U/use-case.md) 在**弥合用户需求与软件功能迭代实现之间的差距**方面发挥着至关重要的作用。它们充当创建用户故事的**蓝图**，用户故事是敏捷方法中的主要工作单元。
  [Use cases](../U/use-case.md) 从用户的角度提供系统交互的**高级概述**，确保开发团队和利益相关者对系统的功能有共同的理解。这种共同的理解有助于**确定**功能的优先级并规划[iterations](../I/iteration.md)或冲刺。
  在待办事项细化和冲刺计划期间，[use cases](../U/use-case.md) 通常被**分解**成更小、更易于管理的用户故事，以适应[iteration](../I/iteration.md)。然后，这些用户故事用于创建**验收标准**，该标准通过定义软件必须满足才能被视为完成的条件来指导[test automation](../T/test-automation.md)工作。
  此外，[use cases](../U/use-case.md) 有助于**识别功能性和非[functional requirements](../F/functional-requirements.md) 的[test scenarios](../T/test-scenario.md)**，确保全面的[test coverage](../T/test-coverage.md)。他们还通过强调在[iterations](../I/iteration.md) 中应保持稳定的关键路径和交互来帮助**[regression testing](../R/regression-testing.md)**。
  总之，[Agile development](../A/agile-development.md) 中的[use cases](../U/use-case.md) 有助于：

- 指导用户故事的创建和验收标准。
  - 确保对系统功能有共同的理解。
  - 优先发展工作。
  - 确定测试场景以实现全面覆盖。
  - 通过概述关键系统交互来支持回归测试。
  - 指导用户故事的创建和验收标准。
  - 确保对系统功能有共同的理解。
  - 优先发展工作。
  - 确定测试场景以实现全面覆盖。
  - 通过概述关键系统交互来支持回归测试。

#### 如何在非功能测试中使用用例？

[Use cases](../U/use-case.md) 可以通过提供**上下文框架**来评估性能、安全性和可用性等系统属性，从而在[non-functional testing](../N/non-functional-testing.md) 中发挥重要作用。虽然[use cases](../U/use-case.md) 传统上与[functional requirements](../F/functional-requirements.md) 相关，但它们也可以概述非功能性质量至关重要的场景。
  例如，描述高流量场景的[use case](../U/use-case.md)可用于导出性能测试，确保系统能够处理指定的负载。同样，涉及用户身份验证的[use cases](../U/use-case.md)可以导致专注于授权和数据保护的安全测试。
  在[usability testing](../U/usability-testing.md) 中，[use cases](../U/use-case.md) 有助于理解用户交互，并可用于评估系统的易用性和可访问性。通过模拟 [use case](../U/use-case.md) 中概述的操作和体验，测试人员可以评估系统支持用户实现其目标的程度。
  要在[non-functional testing](../N/non-functional-testing.md)中利用[use cases](../U/use-case.md)：

- **识别关键[use cases](../U/use-case.md)**
    具有重大的非功能性影响。

- **翻译这些[use cases](../U/use-case.md)**
    转化为特定的非功能性需求。

- **设计测试**
    挑战用例所描述的系统的非功能方面。

- **执行测试**
    根据用例设定的期望来验证系统的性能、安全性、可用性等。
  通过这样做，您可以确保[non-functional testing](../N/non-functional-testing.md) 立足于现实且相关的用户场景，从而提供对系统整体质量的全面评估。

- **识别关键[use cases](../U/use-case.md)**
    具有重大的非功能性影响。

- **翻译这些[use cases](../U/use-case.md)**
    转化为特定的非功能性需求。

- **设计测试**
    挑战用例所描述的系统的非功能方面。

- **执行测试**
    根据用例设定的期望来验证系统的性能、安全性、可用性等。

#### 编写用例时要避免哪些常见错误？

编写[use cases](../U/use-case.md)时，请避免以下常见错误：

- **忽视用户视角**：始终关注用户的观点。 [Use cases](../U/use-case.md) 过于以系统为中心可能会错过用户交互和期望。
  - **太笼统或太详细**：取得平衡是关键。过于笼统的[use cases](../U/use-case.md) 缺乏可操作的信息，而太多的细节可能会让人不知所措和困惑。
  - **忽略替代流程**：不要只关注[happy path](../H/happy-path.md)。考虑替代流程和例外流程以确保全面覆盖。
  - **混合功能**：每个[use case](../U/use-case.md) 应代表一个功能或目标。组合多个目标可能会导致混乱和可测试性问题。
  - **忽略非[Functional Requirements](../F/functional-requirements.md)**：虽然[use cases](../U/use-case.md) 主要关注[functional requirements](../F/functional-requirements.md)，但考虑可能影响场景的性能、可用​​性和安全性方面也很重要。
  - **无法更新**：随着系统的发展，[use cases](../U/use-case.md) 也应该如此。过时的[use cases](../U/use-case.md)会导致不相关或不正确的测试。
  - **缺乏清晰的范围**：定义[use case](../U/use-case.md)将覆盖和不覆盖的范围，以防止范围蔓延并确保集中测试。
  - **定义不明确的参与者**：清楚地识别所涉及的参与者及其角色。这里的歧义可能会导致测试不完整。
  - **术语不一致**：在整个 [use cases](../U/use-case.md) 中使用一致的语言和术语以避免混淆。
  - **跳过验证**：与利益相关者一起验证 [use cases](../U/use-case.md) 以确保准确性和完整性。
  请记住，精心设计的[use cases](../U/use-case.md) 是有效[test automation](../T/test-automation.md) 的基础，为测试团队提供清晰且可操作的场景。

- **忽视用户视角**：始终关注用户的观点。 [Use cases](../U/use-case.md) 过于以系统为中心可能会错过用户交互和期望。
  - **太笼统或太详细**：取得平衡是关键。过于笼统的[use cases](../U/use-case.md) 缺乏可操作的信息，而太多的细节可能会让人不知所措和困惑。
  - **忽略替代流程**：不要只关注[happy path](../H/happy-path.md)。考虑替代流程和例外流程以确保全面覆盖。
  - **混合功能**：每个[use case](../U/use-case.md) 应代表一个功能或目标。组合多个目标可能会导致混乱和可测试性问题。
  - **忽略非[Functional Requirements](../F/functional-requirements.md)**：虽然[use cases](../U/use-case.md) 主要关注[functional requirements](../F/functional-requirements.md)，但考虑可能影响场景的性能、可用​​性和安全性方面也很重要。
  - **无法更新**：随着系统的发展，[use cases](../U/use-case.md) 也应该如此。过时的[use cases](../U/use-case.md)会导致不相关或不正确的测试。
  - **缺乏清晰的范围**：定义[use case](../U/use-case.md)将覆盖和不覆盖的范围，以防止范围蔓延并确保集中测试。
  - **定义不明确的参与者**：清楚地识别所涉及的参与者及其角色。这里的歧义可能会导致测试不完整。
  - **术语不一致**：在整个 [use cases](../U/use-case.md) 中使用一致的语言和术语以避免混淆。
  - **跳过验证**：与利益相关者一起验证 [use cases](../U/use-case.md) 以确保准确性和完整性。
