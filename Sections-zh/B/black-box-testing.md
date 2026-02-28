# 黑盒测试

<!-- TOC START -->
- [相关术语：](#相关术语：)
  - [另请参阅：](#另请参阅：)
- [有关黑盒测试的问题吗？](#有关黑盒测试的问题吗？)
  - [基础知识和重要性](#基础知识和重要性)
    - [什么是黑盒测试？](#什么是黑盒测试？)
    - [为什么黑盒测试很重要？](#为什么黑盒测试很重要？)
    - [黑盒测试的主要目标是什么？](#黑盒测试的主要目标是什么？)
    - [黑盒测试的优点和缺点是什么？](#黑盒测试的优点和缺点是什么？)
    - [黑盒测试与白盒测试有何不同？](#黑盒测试与白盒测试有何不同？)
  - [技巧](#技巧)
    - [有哪些不同的黑盒测试技术？](#有哪些不同的黑盒测试技术？)
    - [黑盒测试中的等价划分是什么？](#黑盒测试中的等价划分是什么？)
    - [黑盒测试中的边界值分析是什么？](#黑盒测试中的边界值分析是什么？)
    - [黑盒测试中的决策表测试是什么？](#黑盒测试中的决策表测试是什么？)
    - [黑盒测试中的状态转换测试是什么？](#黑盒测试中的状态转换测试是什么？)
    - [黑盒测试中的用例测试是什么？](#黑盒测试中的用例测试是什么？)
  - [流程和实施](#流程和实施)
    - [黑盒测试涉及哪些步骤？](#黑盒测试涉及哪些步骤？)
    - [黑盒测试是如何进行的？](#黑盒测试是如何进行的？)
    - [选择黑盒测试技术的标准是什么？](#选择黑盒测试技术的标准是什么？)
    - [黑盒测试使用哪些工具？](#黑盒测试使用哪些工具？)
  - [现实世界的应用](#现实世界的应用)
    - [黑盒测试的一些现实示例是什么？](#黑盒测试的一些现实示例是什么？)
    - [黑盒测试如何用于敏捷开发？](#黑盒测试如何用于敏捷开发？)
    - [黑盒测试如何用于软件开发生命周期（SDLC）？](#黑盒测试如何用于软件开发生命周期（sdlc）？)
    - [黑盒测试如何用于端到端 (E2E) 测试？](#黑盒测试如何用于端到端-e2e-测试？)
<!-- TOC END -->

黑盒测试

评估软件时不考虑其内部工作原理。通常专注于功能或

验收测试

，任何人都可以完成，无论他们对代码库的熟悉程度如何。

## 相关术语：

- [White Box Testing](../W/white-box-testing.md)
- [Grey Box Testing](../G/grey-box-testing.md)
- [Glass Box Testing](../G/glass-box-testing.md)

### 另请参阅：

- [Wikipedia](https://en.wikipedia.org/wiki/Black-box_testing)

## 有关黑盒测试的问题吗？

### 基础知识和重要性

#### 什么是黑盒测试？

[Black Box Testing](../B/black-box-testing.md) 是[software testing](../S/software-testing.md) 的一种方法，它评估应用程序的功能，而无需查看其内部结构或工作原理。该技术侧重于软件应用程序的输入和输出，用于确保软件满足指定的要求并在各种场景中按预期运行。
  测试人员从软件的外部角度创建[test cases](../T/test-case.md)，通常源自对软件预期功能的描述，包括：

- **用户要求**
  - **规格**
  - **技术设计**
  测试人员选择输入来练习代码中的路径并确定适当的输出，而无需知道软件如何处理输入或正在执行什么代码。 [Black Box Testing](../B/black-box-testing.md)几乎适用于[software testing](../S/software-testing.md)的所有级别：单元、集成、系统和验收。
  它特别适用于：

- **根据用户要求进行验证**
  - **行为测试**
  - **绩效评估**
  由于重点在于软件的外部行为，[Black Box Testing](../B/black-box-testing.md) 可以由不了解编程语言或被测试系统内部结构知识的测试人员使用。
  在实践中，[Black Box Testing](../B/black-box-testing.md) 涉及：

1.了解软件的功能和用户交互。
  2. 设计涵盖所有可能的输入和使用场景的测试用例。
  3. 执行测试并将实际结果与预期结果进行比较。
  4. 将任何差异报告为缺陷，供开发团队解决。
  这种方法对于识别软件行为差异和确保产品稳健、可靠并满足用户期望至关重要。

- **用户要求**
  - **规格**
  - **技术设计**
  - **根据用户要求进行验证**
  - **行为测试**
  - **绩效评估**
  1.了解软件的功能和用户交互。
  2. 设计涵盖所有可能的输入和使用场景的测试用例。
  3. 执行测试并将实际结果与预期结果进行比较。
  4. 将任何差异报告为缺陷，供开发团队解决。

#### 为什么黑盒测试很重要？

[Black Box Testing](../B/black-box-testing.md) 至关重要，因为它可以评估系统的功能，而无需了解其内部工作原理。这种方法反映了最终用户的交互，确保从外部角度验证软件。它有助于**识别系统的实际行为与其指定需求之间的差异**，重点关注软件的功能而不是软件的工作方式。
  通过将软件视为“黑匣子”，测试人员可以制作[test cases](../T/test-case.md)来检查系统的**对输入的响应**、**各种条件下的行为**以及**输出生成**。这确保了系统满足用户的期望和要求，这对于用户满意度和软件接受度至关重要。
  此外，[Black Box Testing](../B/black-box-testing.md) 独立于系统的实现，使其能够适应广泛的应用，并且有利于测试设计或实现中**频繁变化**的系统。它还允许非技术利益相关者（例如业务分析师或最终用户）的参与，他们可以提供有关系统[functional requirements](../F/functional-requirements.md)的宝贵见解。
  从本质上讲，[Black Box Testing](../B/black-box-testing.md) 是综合测试策略的关键组成部分，通过关注软件面向用户的方面，为 [White Box Testing](../W/white-box-testing.md) 提供了重要的平衡，这最终决定了应用程序在现实世界中的成功和接受度。

#### 黑盒测试的主要目标是什么？

**[Black Box Testing](../B/black-box-testing.md)** 的主要目标是：

- **验证[Functional Requirements](../F/functional-requirements.md)** ：确保软件满足最终用户预期的指定功能要求和行为，而不考虑内部代码结构。
  - **识别缺陷**：通过测试各种输入并观察输出来检测软件中的错误、错误和缺陷。
  - **提高质量**：通过在发布前发现并允许纠正问题来提高产品的整体质量。
  - **验证外部接口**：检查软件与其他系统和组件的接口，以确保它们正确交互。
  - **评估用户体验**：从用户的角度评估系统，以确认其用户友好并符合可用性标准。
  - **确保合规性**：确保软件遵守行业标准、法规和任何合同协议。
  - **降低风险**：通过在测试过程的早期发现问题来降低生产中系统故障的风险。
  - **支持维护**：通过确保更改或增强不会对现有功能产生不利影响，促进软件的维护。
  这些目标是通过各种技术和方法来实现的，所有这些技术和方法都侧重于从外部测试软件，而不了解应用程序的内部工作原理。

- **验证[Functional Requirements](../F/functional-requirements.md)** ：确保软件满足最终用户预期的指定功能要求和行为，而不考虑内部代码结构。
  - **识别缺陷**：通过测试各种输入并观察输出来检测软件中的错误、错误和缺陷。
  - **提高质量**：通过在发布前发现并允许纠正问题来提高产品的整体质量。
  - **验证外部接口**：检查软件与其他系统和组件的接口，以确保它们正确交互。
  - **评估用户体验**：从用户的角度评估系统，以确认其用户友好并符合可用性标准。
  - **确保合规性**：确保软件遵守行业标准、法规和任何合同协议。
  - **降低风险**：通过在测试过程的早期发现问题来降低生产中系统故障的风险。
  - **支持维护**：通过确保更改或增强不会对现有功能产生不利影响，促进软件的维护。

#### 黑盒测试的优点和缺点是什么？

[Black Box Testing](../B/black-box-testing.md) 的优点：

- **用户视角**：从用户的角度进行测试，确保软件满足用户的要求和期望。
  - **不需要代码知识**：测试人员不需要编程知识，允许非技术测试人员执行测试。
  - **无偏见测试**：测试人员不受内部代码结构的影响，从而对功能进行客观评估。
  - **并行开发**：测试可以与开发并行完成，因为它不依赖于内部代码结构。
  - **全面覆盖**：鼓励在不受代码结构限制的情况下测试所有功能需求。
  [Black Box Testing](../B/black-box-testing.md) 的缺点：

- **有限覆盖**：只能测试可能输入的子集，可能会遗漏某些缺陷。
  - **算法测试效率低**：不适合测试复杂算法，因为未检查内部工作原理。
  - **潜在冗余**：如果不了解内部代码，测试可能是重复的或不必要的。
  - **遗漏案例**：如果测试用例不够全面，某些路径或内部状态可能无法测试。
  - **对规格的依赖**：严重依赖准确和详细的规格；任何含糊之处都可能导致测试不充分。
  - **用户视角**：从用户的角度进行测试，确保软件满足用户的要求和期望。
  - **不需要代码知识**：测试人员不需要编程知识，允许非技术测试人员执行测试。
  - **无偏见测试**：测试人员不受内部代码结构的影响，从而对功能进行客观评估。
  - **并行开发**：测试可以与开发并行完成，因为它不依赖于内部代码结构。
  - **全面覆盖**：鼓励在不受代码结构限制的情况下测试所有功能需求。
  - **有限覆盖**：只能测试可能输入的子集，可能会遗漏某些缺陷。
  - **算法测试效率低**：不适合测试复杂算法，因为未检查内部工作原理。
  - **潜在冗余**：如果不了解内部代码，测试可能是重复的或不必要的。
  - **遗漏案例**：如果测试用例不够全面，某些路径或内部状态可能无法测试。
  - **对规格的依赖**：严重依赖准确和详细的规格；任何含糊之处都可能导致测试不充分。

#### 黑盒测试与白盒测试有何不同？

[Black Box Testing](../B/black-box-testing.md) 和[White Box Testing](../W/white-box-testing.md) 是[software testing](../S/software-testing.md) 的不同方法。 **[Black Box Testing](../B/black-box-testing.md)** 专注于在不了解内部代码结构、实现细节或内部路径的情况下检查软件功能。测试人员验证输入和输出，确保软件按预期运行。
  相比之下，**[White Box Testing](../W/white-box-testing.md)**（也称为透明盒测试、[Glass Box Testing](../G/glass-box-testing.md)、透明盒测试或基于代码的测试）需要对代码有深入的了解。测试人员需要访问源代码来设计[test cases](../T/test-case.md)，这使他们能够检查程序结构、逻辑和流程。这种方法使他们能够识别潜在的安全漏洞，确保测试逻辑路径，并查找特定的代码行为。
  [Black Box Testing](../B/black-box-testing.md) 将软件视为一个封闭的系统，而 [White Box Testing](../W/white-box-testing.md) 采用开放的视角，仔细检查内部运作。 [Black Box Testing](../B/black-box-testing.md) 通常由 QA 专业人员（可能不是程序员）执行，而 [White Box Testing](../W/white-box-testing.md) 通常由具有编程技能的开发人员或测试人员执行。
  Black Box 和[White Box Testing](../W/white-box-testing.md) 之间的选择取决于测试目标、可用资源和项目要求。 [Black Box Testing](../B/black-box-testing.md)适合验证整体软件功能和用户体验，而[White Box Testing](../W/white-box-testing.md)则非常适合优化代码结构、改进设计和确保彻底的路径覆盖。

### 技巧

#### 有哪些不同的黑盒测试技术？

[Black Box Testing](../B/black-box-testing.md) 技术超出了通常讨论的方法。以下是自动化工程师可能采用的其他技术：

- **[Error Guessing](../E/error-guessing.md)**：此技术依赖于测试人员的经验来猜测应用程序的问题区域。测试人员根据直觉和类似应用程序的过去知识创建[test cases](../T/test-case.md)。
  - **比较测试**：也称为竞争分析，涉及将软件与类似应用程序的优缺点进行比较，以确定潜在的改进领域。
  - **组合测试**：此方法测试输入和先决条件的所有可能组合。当多个参数可能影响结果并且您希望确保覆盖所有排列时，它非常有用。
  - **[Exploratory Testing](../E/exploratory-testing.md)**：虽然结构较少，但[exploratory testing](../E/exploratory-testing.md) 涉及同时学习、测试设计和执行。这是一种调查方法，测试人员在执行测试时主动控制测试的设计。
  - **语法测试**：当根据输入的特定语法选择输入值时使用。它对于需要结构化输入（例如编译器或数据转换程序）的系统特别有用。
  - **[Fuzz Testing](../F/fuzz-testing.md)**：一种自动化[software testing](../S/software-testing.md) 技术，涉及提供无效、意外或随机数据作为计算机程序的输入。然后监视程序是否有异常情况，例如崩溃或内置代码断言失败。
  每种技术都提供了不同的视角来检查软件，结合使用时提供全面的测试策略。自动化工程师可以利用这些技术来创建强大的[test suites](../T/test-suite.md)，从而在不了解内部工作原理的情况下有效地验证软件行为。

- **[Error Guessing](../E/error-guessing.md)**：此技术依赖于测试人员的经验来猜测应用程序的问题区域。测试人员根据直觉和类似应用程序的过去知识创建[test cases](../T/test-case.md)。
  - **比较测试**：也称为竞争分析，涉及将软件与类似应用程序的优缺点进行比较，以确定潜在的改进领域。
  - **组合测试**：此方法测试输入和先决条件的所有可能组合。当多个参数可能影响结果并且您希望确保覆盖所有排列时，它非常有用。
  - **[Exploratory Testing](../E/exploratory-testing.md)**：虽然结构较少，但[exploratory testing](../E/exploratory-testing.md) 涉及同时学习、测试设计和执行。这是一种调查方法，测试人员在执行测试时主动控制测试的设计。
  - **语法测试**：当根据输入的特定语法选择输入值时使用。它对于需要结构化输入（例如编译器或数据转换程序）的系统特别有用。
  - **[Fuzz Testing](../F/fuzz-testing.md)**：一种自动化[software testing](../S/software-testing.md) 技术，涉及提供无效、意外或随机数据作为计算机程序的输入。然后监视程序是否有异常情况，例如崩溃或内置代码断言失败。

#### 黑盒测试中的等价划分是什么？

[Equivalence Partitioning](../E/equivalence-partitioning.md) 是一种**[black box testing](../B/black-box-testing.md)** 技术，它将软件应用程序的输入数据划分为等效数据的分区，从中可以导出[test cases](../T/test-case.md)。通过这样做，假设系统将以相同的方式处理来自一个分区的所有值。此方法减少了需要开发的[test cases](../T/test-case.md) 总数，同时仍确保足够的[test coverage](../T/test-coverage.md)。
  在[Equivalence Partitioning](../E/equivalence-partitioning.md) 中，软件或系统的输入被分为预期表现出类似行为的组，因此测试每个组中的单个值被认为代表整个分区。例如，如果输入接受从 1 到 50 的值范围，则可以将该范围划分为 1-10、11-20 等分区，并且可以为每个分区设计测试。
  主要目标是识别与输入数据相关的**错误**。如果存在 [bug](../B/bug.md)，它应该会影响该分区的所有成员。该技术可以应用于所有级别的测试：单元、集成、系统和验收。
  下面是一个简单的伪代码示例，用于说明如何定义等价分区：

  ```
  IF input >= 1 AND input <= 10 THEN
    // Test cases for partition 1
  ELSIF input > 10 AND input <= 20 THEN
    // Test cases for partition 2
  ELSIF input > 20 AND input <= 30 THEN
    // Test cases for partition 3
  // ... and so on
  ENDIF
  ```使用[Equivalence Partitioning](../E/equivalence-partitioning.md)，测试人员可以最大化[test coverage](../T/test-coverage.md)，同时最小化[test cases](../T/test-case.md)的数量，从而提高测试效率。

#### 黑盒测试中的边界值分析是什么？

边界值分析 (BVA) 是一种 **[black box testing](../B/black-box-testing.md)** 技术，重点关注等价分区边缘的值。它基于这样的原理：错误往往发生在输入范围的边界处。 BVA 涉及为这些分区的**限制**内的值创建 [test cases](../T/test-case.md)。
  对于具有下限`L` 和上限`U` 的给定范围，BVA 建议为值`L`、`L+1`、`U` 和`U-1` 设计[test cases](../T/test-case.md)。此外，如果适用，还会测试边界 `L-1` 和 `U+1` 之外的值。
  考虑一个接受 1 到 100 之间整数值的输入字段。使用 BVA，您将测试边界值：`0`、`1`、`2`、`99`、`100` 和 `101`。
  BVA 通常与 **[Equivalence Partitioning](../E/equivalence-partitioning.md)** (EP) 结合使用，因为它们相辅相成。 EP 有助于确定要测试哪些值集（等价类），而 BVA 有助于查明这些集中的特定边界值。
  该技术在测试时特别有用：

- 基于范围的输入
  - 数组和列表边界
  - 具有边界相关逻辑的条件
  这是一种经济高效的方法，因为它减少了 [test cases](../T/test-case.md) 的数量，同时仍然很有可能在最容易出错的区域发现缺陷。 [Test automation](../T/test-automation.md) 工程师可以通过将这些边界值合并到其自动化[test suites](../T/test-suite.md) 中来利用 BVA，以确保彻底覆盖潜在的边缘情况。

- 基于范围的输入
  - 数组和列表边界
  - 具有边界相关逻辑的条件

#### 黑盒测试中的决策表测试是什么？

[Decision Table Testing](../D/decision-table-testing.md) 是一种 **系统** [black box testing](../B/black-box-testing.md) 技术，用于测试可应用于各种输入和条件的复杂业务逻辑。它涉及创建一个表，通常称为“因果表”，其中每一列代表输入的唯一组合，每一行对应于应根据这些输入采取的决策或操作。
  在这种方法中，您可以确定**条件**（原因）和**操作**（结果）来构建决策表。条件是输入状态或变量，而操作是结果或系统行为。决策表有助于确保考虑不同的输入组合，这使得它对于测试具有大量相互依赖变量的系统或处理可能被忽视的逻辑条件时特别有用。
  这是决策表结构的简化示例：

  ```
  | Conditions | C1 | C2 | C3 | C4 |
  |------------|----|----|----|----|
  | Input 1    | Y  | Y  | N  | N  |
  | Input 2    | Y  | N  | Y  | N  |
  |------------|----|----|----|----|
  | Actions    | A1 | A2 | A3 | A4 |
  |------------|----|----|----|----|
  ```在此表中，`Y` 和`N` 表示输入的不同状态，`A1` 至`A4` 表示对每个输入状态组合要采取的操作。
  要应用 [Decision Table Testing](../D/decision-table-testing.md)，您需要：

1. 确定所有相关条件和行动。
  2. 创建包含所有可能的条件组合的综合决策表。
  3. 确定每个组合的预期操作。
  4. 设计测试用例以验证系统对于每种组合的行为是否符合预期。
  该技术对于**[functional testing](../F/functional-testing.md)**特别有效，并确保覆盖所有可能的场景，这可以显着增强[test suite](../T/test-suite.md)的鲁棒性。

1. 确定所有相关条件和行动。
  2. 创建包含所有可能的条件组合的综合决策表。
  3. 确定每个组合的预期操作。
  4. 设计测试用例以验证系统对于每种组合的行为是否符合预期。

#### 黑盒测试中的状态转换测试是什么？

[State Transition Testing](../S/state-transition-testing.md) 是一种 **[black box testing](../B/black-box-testing.md)** 技术，当系统由有限数量的状态定义并且这些状态之间的转换受系统规则控制时使用。它对于输出不仅取决于当前输入还取决于输入历史记录的系统特别有用，例如事务系统、协议或有状态应用程序。
  在这种方法中，测试人员设计[test cases](../T/test-case.md)来验证状态之间的转换是否按预期发生，以及系统在每个状态下的行为是否正确。这涉及：

- 识别所有
    **国家**
    该软件可以在.

- 了解
    **过渡**
    由事件或条件触发的这些状态之间。

- 定义
    **输入或事件**
    导致转变。

- 确定
    **预期产出**
    或因转换而产生的动作。
  测试人员创建**状态转换图**或表格来可视化和理解各种状态和转换。这有助于系统地覆盖所有可能的路径。
  下面是登录过程状态转换表的一个简单示例：

  ```
  | Current State | Input         | Next State | Output           |
  |---------------|---------------|------------|------------------|
  | Logged Out    | Valid Login   | Logged In  | Access Granted   |
  | Logged Out    | Invalid Login | Logged Out | Error Message    |
  | Logged In     | Logout        | Logged Out | Logout Successful|
  ```[State Transition Testing](../S/state-transition-testing.md) 确保软件正确处理序列相关行为，并且对于发现与状态更改相关的缺陷（这些缺陷可能无法通过其他黑盒技术暴露）特别有效。

- 识别所有
    **国家**
    该软件可以在.

- 了解
    **过渡**
    由事件或条件触发的这些状态之间。

- 定义
    **输入或事件**
    导致转变。

- 确定
    **预期产出**
    或因转换而产生的动作。

#### 黑盒测试中的用例测试是什么？

[Use Case Testing](../U/use-case-testing.md) 是一种 **[black box testing](../B/black-box-testing.md)** 技术，涉及基于 **[use cases](../U/use-case.md)** 创建 [test cases](../T/test-case.md)。 [use case](../U/use-case.md) 描述系统如何与外部实体（如用户或其他系统）交互以实现特定目标。在这种方法中，测试人员专注于**用户场景**和**[functional requirements](../F/functional-requirements.md)**来验证系统的行为是否符合预期。
  测试人员开发[test cases](../T/test-case.md)，涵盖[use case](../U/use-case.md)的完整流程，包括**主要流程**（标准操作）和**替代流程**（错误条件和其他分支）。这可确保测试用户可能通过应用程序采用的所有路径。 [Use Case Testing](../U/use-case-testing.md) 对于识别在单元或组件测试中可能不明显的**集成**和**系统级问题**特别有用。
  以下是电子商务应用程序的 [use case](../U/use-case.md) 的简化示例：

  ```
  Use Case: Purchase Product
  1. User selects a product.
  2. User adds the product to the shopping cart.
  3. User proceeds to checkout.
  4. User enters payment information.
  5. System processes payment.
  6. System confirms the order and sends an email to the user.
  ```基于此[use case](../U/use-case.md)，将创建[test cases](../T/test-case.md)来覆盖每个步骤，包括用户输入无效支付信息或系统无法处理支付的情况。
  [Use Case Testing](../U/use-case-testing.md) 之所以有效，是因为它**以用户为中心**，确保系统满足最终用户的需求和期望。这也是一种**验证业务流程**并确保系统正确支持它们的方法。

### 流程和实施

#### 黑盒测试涉及哪些步骤？

**[Black Box Testing](../B/black-box-testing.md)**涉及的步骤如下：

1. **了解需求**：查看软件需求和规范以了解预期行为。
  2. **定义测试目标**：确定您想要验证的内容，例如功能、可用性或性能。
  3. **测试计划**：确定要使用的范围、资源、时间表和方法。
  4. **设计[Test Cases](../T/test-case.md)**：创建涵盖所有可能的输入、输出和用户交互的测试用例。
    - 使用类似的技术
      *边界值分析*
      ,
      *等价划分*
      ,
      *决策表测试*
      等

- 使用类似的技术
      *边界值分析*
      ,
      *等价划分*
      ,
      *决策表测试*
      等

5. **准备[Test Environment](../T/test-environment.md)** ：设置测试环境以模拟生产设置。
  6. **[Test Execution](../T/test-execution.md)** ：在软件上运行设计的测试用例。
    - 记录结果并将其与预期结果进行比较。
    - 记录结果并将其与预期结果进行比较。
  7. **缺陷报告**：将发现的任何差异记录为缺陷，供开发团队解决。
  8. **[Retesting](../R/retesting.md)** ：修复缺陷后，重新测试软件以确保修复按预期工作。
  9. **[Regression Testing](../R/regression-testing.md)** ：检查新的更改是否不会对现有功能产生不利影响。
  10. **测试结束**：编译测试结果，评估覆盖范围，并评估测试过程的质量。
  在整个这些步骤中，保持清晰简洁的文档，以提高透明度和将来参考。在适用的情况下使用自动化工具来提高效率和可重复性。

1. **了解需求**：查看软件需求和规范以了解预期行为。
  2. **定义测试目标**：确定您想要验证的内容，例如功能、可用性或性能。
  3. **测试计划**：确定要使用的范围、资源、时间表和方法。
  4. **设计[Test Cases](../T/test-case.md)**：创建涵盖所有可能的输入、输出和用户交互的测试用例。
    - 使用类似的技术
      *边界值分析*
      ,
      *等价划分*
      ,
      *决策表测试*
      等

- 使用类似的技术
      *边界值分析*
      ,
      *等价划分*
      ,
      *决策表测试*
      等

5. **准备[Test Environment](../T/test-environment.md)** ：设置测试环境以模拟生产设置。
  6. **[Test Execution](../T/test-execution.md)** ：在软件上运行设计的测试用例。
    - 记录结果并将其与预期结果进行比较。
    - 记录结果并将其与预期结果进行比较。
  7. **缺陷报告**：将发现的任何差异记录为缺陷，供开发团队解决。
  8. **[Retesting](../R/retesting.md)** ：修复缺陷后，重新测试软件以确保修复按预期工作。
  9. **[Regression Testing](../R/regression-testing.md)** ：检查新更改是否不会对现有功能产生不利影响。
  10. **测试结束**：编译测试结果，评估覆盖范围，并评估测试过程的质量。

#### 黑盒测试是如何进行的？

[Black Box Testing](../B/black-box-testing.md)通过以下步骤执行：

1. **了解要求和规格**
    软件的功能来确定系统应该做什么。

2. **开发[test cases](../T/test-case.md)**
    涵盖规范中提到的所有功能。这些测试用例应该关注输入和预期输出，而不考虑内部代码结构。

3. **选择[Black Box Testing](../B/black-box-testing.md)技术**
    例如等价划分、边界值分析、决策表测试、状态转换测试或用例测试来创建有效的测试场景。

4. **准备[test data](../T/test-data.md)**
    对于测试用例，确保混合使用正面和负面测试场景。

5. **执行[test cases](../T/test-case.md)**
    通过提供输入并将实际输出与预期结果进行比较。

6. **记录结果**
    测试用例并将任何差异记录为缺陷。

7. **重新测试**
    修复缺陷后，确认问题已解决并且没有引入新问题。

8. **报告**
    测试过程，包括覆盖范围、缺陷发现和软件质量评估。
  在执行过程中，[automated testing](../A/automated-testing.md)工具可用于输入[test data](../T/test-data.md)、记录结果并比较结果。工具多种多样，从简单的记录和回放工具到可以集成到持续集成/持续部署 (CI/CD) 管道中的更复杂的测试框架。

  ```
  // Example of a simple automated black box test case in TypeScript
  describe('Login Functionality', () => {
    it('should allow a user to log in with valid credentials', () => {
      const input = { username: 'user1', password: 'pass123' };
      const expectedOutput = { success: true, message: 'Login successful' };
      const actualOutput = loginFunction(input);
      expect(actualOutput).toEqual(expectedOutput);
    });
  });
  ```这种方法确保从用户的角度测试系统，验证软件的功能和可用性。

1. **了解要求和规格**
    软件的功能来确定系统应该做什么。

2. **开发[test cases](../T/test-case.md)**
    涵盖规范中提到的所有功能。这些测试用例应该关注输入和预期输出，而不考虑内部代码结构。

3. **选择[Black Box Testing](../B/black-box-testing.md)技术**
    例如等价划分、边界值分析、决策表测试、状态转换测试或用例测试来创建有效的测试场景。

4. **准备[test data](../T/test-data.md)**
    对于测试用例，确保混合使用正面和负面测试场景。

5. **执行[test cases](../T/test-case.md)**
    通过提供输入并将实际输出与预期结果进行比较。

6. **记录结果**
    测试用例并将任何差异记录为缺陷。

7. **重新测试**
    修复缺陷后，确认问题已解决并且没有引入新问题。

8. **报告**
    测试过程，包括覆盖范围、缺陷发现和软件质量评估。

#### 选择黑盒测试技术的标准是什么？

选择 **[Black Box Testing](../B/black-box-testing.md)** 技术取决于几个标准：

- **应用程序类型**：考虑被测应用程序的类型。例如，Web 应用程序可能会从 **[State Transition Testing](../S/state-transition-testing.md)** 等技术中受益更多，而金融应用程序可能需要严格的**边界值分析**。
  - **测试目标**：使技术与测试的具体目标保持一致。如果目标是验证业务流程，**[Use Case Testing](../U/use-case-testing.md)** 可能是最佳选择。
  - **软件的复杂性**：对于复杂的系统，**[Equivalence Partitioning](../E/equivalence-partitioning.md)** 和 **边界值分析** 等技术的组合可能是有效的。
  - **风险评估**：高风险区域可能需要使用涵盖广泛输入和用户行为的技术进行更彻底的测试，例如**[Decision Table Testing](../D/decision-table-testing.md)**。
  - **资源可用性**：考虑可用的时间和人力。有些技术比其他技术需要更多的准备和执行时间。
  - **文档**：文档的可用性和质量会影响选择。例如，**[Decision Table Testing](../D/decision-table-testing.md)** 需要详细规范。
  - **客户要求**：有时，选择是由特定客户或监管机构的测试要求驱动的。
  - **以前的缺陷**：分析以前版本的缺陷，以确定哪些区域容易出现错误，并选择专注于这些区域的技术。
  - **[Test Coverage](../T/test-coverage.md)**：确保所选技术提供应用程序功能所需的[test coverage](../T/test-coverage.md)。
  - **工具支持**：支持该技术的工具的可用性也可能是一个决定因素，因为它可以提高效率和有效性。
  总之，选择应该是基于应用特性、测试目标和可用资源的战略决策，旨在最大化[test coverage](../T/test-coverage.md)和缺陷检测。

- **应用程序类型**：考虑被测应用程序的类型。例如，Web 应用程序可能会从 **[State Transition Testing](../S/state-transition-testing.md)** 等技术中受益更多，而金融应用程序可能需要严格的**边界值分析**。
  - **测试目标**：使技术与测试的具体目标保持一致。如果目标是验证业务流程，**[Use Case Testing](../U/use-case-testing.md)** 可能是最佳选择。
  - **软件的复杂性**：对于复杂的系统，**[Equivalence Partitioning](../E/equivalence-partitioning.md)** 和 **边界值分析** 等技术的组合可能是有效的。
  - **风险评估**：高风险区域可能需要使用涵盖广泛输入和用户行为的技术进行更彻底的测试，例如**[Decision Table Testing](../D/decision-table-testing.md)**。
  - **资源可用性**：考虑可用的时间和人力。有些技术比其他技术需要更多的准备和执行时间。
  - **文档**：文档的可用性和质量会影响选择。例如，**[Decision Table Testing](../D/decision-table-testing.md)** 需要详细的规范。
  - **客户要求**：有时，选择是由特定客户或监管机构的测试要求驱动的。
  - **以前的缺陷**：分析以前版本的缺陷，以确定哪些区域容易出现错误，并选择专注于这些区域的技术。
  - **[Test Coverage](../T/test-coverage.md)**：确保所选技术提供应用程序功能所需的[test coverage](../T/test-coverage.md)。
  - **工具支持**：支持该技术的工具的可用性也可能是一个决定因素，因为它可以提高效率和有效性。

#### 黑盒测试使用哪些工具？

[Black Box Testing](../B/black-box-testing.md) 工具可以促进测试过程，而无需了解内部代码结构。这些工具专注于输入和输出验证。以下是一些常用的工具：

- **[Selenium](../S/selenium.md)** ：用于自动化网络浏览器的开源工具。它支持多种语言和框架。

  ```
  WebDriver driver = new ChromeDriver();
  driver.get("http://www.example.com");
  WebElement element = driver.findElement(By.id("element_id"));
  element.sendKeys("test input");
  driver.quit();
  ```

- **Appium** ：将 Selenium 的框架扩展到移动应用程序（Android 和 iOS）。

  ```
  DesiredCapabilities caps = new DesiredCapabilities();
  caps.setCapability("platformName", "iOS");
  caps.setCapability("deviceName", "iPhone Simulator");
  caps.setCapability("app", "/path/to/app.zip");
  AppiumDriver driver = new IOSDriver<>(new URL("http://127.0.0.1:4723/wd/hub"), caps);
  ```

- **QTP/UFT（统一[Functional Testing](../F/functional-testing.md)）**：Micro Focus 的商业工具，用于功能性和带有可视化界面的[regression testing](../R/regression-testing.md)。
  - **TestComplete**：另一个支持桌面、移动和 Web 应用程序的商业工具。
  - **SoapUI**：主要用于[API testing](../A/api-testing.md)，它允许测试人员在不同的 Web [APIs](../A/api.md) 上执行自动化功能、回归、合规性和负载测试。
  - **[JMeter](../J/jmeter.md)**：用于[performance testing](../P/performance-testing.md)的Apache项目，也可以为[functional testing](../F/functional-testing.md)的Web应用程序进行配置。
  - **[Postman](../P/postman.md)**：[API testing](../A/api-testing.md) 的工具，允许用户通过用户友好的界面构建和执行自动化测试。
  - **机器人框架**：用于[acceptance testing](../A/acceptance-testing.md) 和接受[test-driven development](../T/test-driven-development.md) (ATDD) 的关键字驱动[test automation](../T/test-automation.md) 框架。
  每个工具都提供独特的功能和集成，允许测试人员根据被测应用程序和测试过程的具体要求选择最合适的工具。

- **[Selenium](../S/selenium.md)** ：用于自动化网络浏览器的开源工具。它支持多种语言和框架。
  - **Appium** ：将 Selenium 的框架扩展到移动应用程序（Android 和 iOS）。
  - **QTP/UFT（统一[Functional Testing](../F/functional-testing.md)）**：Micro Focus 的商业工具，用于功能性和带有可视化界面的[regression testing](../R/regression-testing.md)。
  - **TestComplete**：另一个支持桌面、移动和 Web 应用程序的商业工具。
  - **SoapUI**：主要用于[API testing](../A/api-testing.md)，它允许测试人员在不同的 Web [APIs](../A/api.md) 上执行自动化功能、回归、合规性和负载测试。
  - **[JMeter](../J/jmeter.md)**：用于[performance testing](../P/performance-testing.md)的Apache项目，也可以为[functional testing](../F/functional-testing.md)的Web应用程序进行配置。
  - **[Postman](../P/postman.md)**：[API testing](../A/api-testing.md) 的工具，允许用户通过用户友好的界面构建和执行自动化测试。
  - **机器人框架**：用于[acceptance testing](../A/acceptance-testing.md) 和接受[test-driven development](../T/test-driven-development.md) (ATDD) 的关键字驱动[test automation](../T/test-automation.md) 框架。

#### 黑盒测试中如何编写有效的测试用例？

在[Black Box Testing](../B/black-box-testing.md) 中编写有效的[test cases](../T/test-case.md) 需要关注软件的外部行为而不是其内部结构。以下是关键策略：

- **了解用户需求**
    彻底确保测试用例与软件的预期功能一致。

- **识别[test scenarios](../T/test-scenario.md)**
    涵盖应用程序的所有功能方面，包括边缘情况。

- 使用
    **边界值分析**
    和
    **[Equivalence Partitioning](../E/equivalence-partitioning.md)**
    最大限度地减少测试用例，同时最大限度地扩大覆盖范围。

- 合并
    **[Decision Table Testing](../D/decision-table-testing.md)**
    用于复杂的业务规则，以确保测试所有可能的组合。

- 申请
    **[State Transition Testing](../S/state-transition-testing.md)**
    适用于具有有限数量的状态或模式的应用。

- 杠杆
    **[Use Case Testing](../U/use-case-testing.md)**
    模拟真实世界的使用情况以及用户与系统的交互。

- **优先考虑[test cases](../T/test-case.md)**
    基于风险和重要性，首先关注最重要的领域。

- 确保测试用例
    **独立**
    并且可以按任意顺序执行，无需依赖。

- 写
    **清晰简洁**
    对每个步骤的预期结果进行测试以避免歧义。

- **审查和完善**
    定期测试用例以适应用户需求的变化并纳入先前测试周期的反馈。

- 使用
    **自动化工具**
    在适当的情况下提高测试用例的效率和可重复性。
  请记住，目标是验证软件是否满足用户期望并在所有场景中正常运行，而不考虑应用程序的内部工作原理。

- **了解用户需求**
    彻底确保测试用例与软件的预期功能一致。

- **识别[test scenarios](../T/test-scenario.md)**
    涵盖应用程序的所有功能方面，包括边缘情况。

- 使用
    **边界值分析**
    和
    **[Equivalence Partitioning](../E/equivalence-partitioning.md)**
    最大限度地减少测试用例，同时最大限度地扩大覆盖范围。

- 合并
    **[Decision Table Testing](../D/decision-table-testing.md)**
    用于复杂的业务规则，以确保测试所有可能的组合。

- 申请
    **[State Transition Testing](../S/state-transition-testing.md)**
    适用于具有有限数量的状态或模式的应用。

- 杠杆
    **[Use Case Testing](../U/use-case-testing.md)**
    模拟真实世界的使用情况以及用户与系统的交互。

- **优先考虑[test cases](../T/test-case.md)**
    基于风险和重要性，首先关注最重要的领域。

- 确保测试用例
    **独立**
    并且可以按任意顺序执行，无需依赖。

- 写
    **清晰简洁**
    对每个步骤的预期结果进行测试以避免歧义。

- **审查和完善**
    定期测试用例以适应用户需求的变化并纳入先前测试周期的反馈。

- 使用
    **自动化工具**
    在适当的情况下提高测试用例的效率和可重复性。

### 现实世界的应用

#### 黑盒测试的一些现实示例是什么？

**[Black Box Testing](../B/black-box-testing.md)** 的真实示例包括：

- **用户界面 (UI) 测试**：在不知道内部代码结构的情况下验证 Web 应用程序的 UI 元素，如按钮、表单和导航。
  - **[Functional Testing](../F/functional-testing.md)**：通过在不了解底层服务逻辑的情况下执行交易来测试电子商务应用程序中支付网关的功能。
  - **[System Testing](../S/system-testing.md)**：验证完整且集成的软件产品（例如移动应用程序），以确保其满足指定要求。
  - **[Acceptance Testing](../A/acceptance-testing.md)**：对客户关系管理 (CRM) 系统进行测试，以确定其是否满足业务需求和用户期望。
  - **[Regression Testing](../R/regression-testing.md)**：更新流媒体服务平台后，确保视频播放和用户身份验证等现有功能仍然按预期工作。
  - **[Exploratory Testing](../E/exploratory-testing.md)**：通过探索和实验手动测试项目管理工具中的新功能，以发现意外行为。
  - **临时测试**：在没有任何特定 [test cases](../T/test-case.md) 的情况下随机测试 GPS 导航应用程序以发现潜在缺陷。
  - **[Compatibility Testing](../C/compatibility-testing.md)**：检查生产力软件是否在不同操作系统、浏览器和设备上一致运行。
  - **[Performance Testing](../P/performance-testing.md)**：测量 [API](../A/api.md) 在各种负载条件下的响应时间和吞吐量，而不检查内部工作情况。
  这些示例中的每一个都演示了 **[Black Box Testing](../B/black-box-testing.md)** 在评估软件组件或系统的外部功能方面的应用，而无需深入研究内部代码结构或实现细节。

- **用户界面 (UI) 测试**：在不知道内部代码结构的情况下验证 Web 应用程序的 UI 元素，如按钮、表单和导航。
  - **[Functional Testing](../F/functional-testing.md)**：通过在不了解底层服务逻辑的情况下执行交易来测试电子商务应用程序中支付网关的功能。
  - **[System Testing](../S/system-testing.md)**：验证完整且集成的软件产品（例如移动应用程序），以确保其满足指定要求。
  - **[Acceptance Testing](../A/acceptance-testing.md)**：对客户关系管理 (CRM) 系统进行测试，以确定其是否满足业务需求和用户期望。
  - **[Regression Testing](../R/regression-testing.md)**：更新流媒体服务平台后，确保视频播放和用户身份验证等现有功能仍然按预期工作。
  - **[Exploratory Testing](../E/exploratory-testing.md)**：通过探索和实验手动测试项目管理工具中的新功能，以发现意外行为。
  - **临时测试**：在没有任何特定 [test cases](../T/test-case.md) 的情况下随机测试 GPS 导航应用程序以发现潜在缺陷。
  - **[Compatibility Testing](../C/compatibility-testing.md)**：检查生产力软件是否在不同操作系统、浏览器和设备上一致运行。
  - **[Performance Testing](../P/performance-testing.md)**：测量 [API](../A/api.md) 在各种负载条件下的响应时间和吞吐量，而无需检查内部工作情况。

#### 黑盒测试如何用于敏捷开发？

在 **[Agile development](../A/agile-development.md)** 中，[Black Box Testing](../B/black-box-testing.md) 被集成到迭代过程的各个阶段。测试人员通常与开发人员并行工作，根据用户故事和验收标准创建[test cases](../T/test-case.md)，而不了解被测试项目的内部工作原理。这种方法通过关注用户视角和产品功能来符合敏捷原则。
  在每个冲刺期间，[Black Box Testing](../B/black-box-testing.md) 用于验证新功能并回归测试现有功能。敏捷团队可以使用**自动化[Black Box Testing](../B/black-box-testing.md)**为每个构建快速执行一套测试，确保持续集成和交付管道提供有关应用程序运行状况的即时反馈。
  测试人员与敏捷团队中的开发人员和产品所有者密切合作，以便随着需求的发展快速调整[test plans](../T/test-plan.md)。这种协作对于保持敏捷冲刺的节奏并确保测试始终符合当前用户的期望至关重要。
  **[Exploratory testing](../E/exploratory-testing.md)** 是敏捷中经常使用的一种技术，是 [Black Box Testing](../B/black-box-testing.md) 的一种形式，其中测试人员在没有预定义 [test cases](../T/test-case.md) 的情况下主动探索软件，这增强了结构化测试可能错过的问题的发现。
  总之，敏捷中的[Black Box Testing](../B/black-box-testing.md) 是关于：

- 从用户角度进行测试
  - 使测试与用户故事和验收标准保持一致
  - 将测试集成到持续交付管道中
  - 通过密切的团队协作快速适应变化
  - 采用探索性测试来发现意外问题
  通过使用[Black Box Testing](../B/black-box-testing.md)，敏捷团队确保软件始终满足用户需求，并快速识别和解决任何潜在缺陷，从而保持敏捷软件开发的速度和质量。

- 从用户角度进行测试
  - 使测试与用户故事和验收标准保持一致
  - 将测试集成到持续交付管道中
  - 通过密切的团队协作快速适应变化
  - 采用探索性测试来发现意外问题

#### 黑盒测试如何用于软件开发生命周期（SDLC）？

[Black Box Testing](../B/black-box-testing.md) 在各个阶段集成到**[Software Development Life Cycle](../S/software-development-life-cycle.md) (SDLC)** 中，以确保应用程序按照用户的角度预期运行。在**需求收集阶段**，[black box testing](../B/black-box-testing.md) 有助于了解用户需求并设计反映用户场景的测试。
  在**设计阶段**，测试人员根据需求准备[test plans](../T/test-plan.md)和案例，而不考虑内部代码结构。随着**开发阶段**的进展，[black box testing](../B/black-box-testing.md) 用于根据要求验证开发的功能。这通常通过 **[manual testing](../M/manual-testing.md)** 或 **自动 [UI testing](../U/ui-testing.md)** 完成。
  在**测试阶段**，使用**边界值分析**、**[equivalence partitioning](../E/equivalence-partitioning.md)**和**[decision table testing](../D/decision-table-testing.md)**等黑盒方法来确保全面覆盖应用程序的功能。这些技术有助于识别通过代码 [inspection](../I/inspection.md) 或 [white box testing](../W/white-box-testing.md) 方法可能不明显的缺陷。
  在**暂存或预生产环境**中，[black box testing](../B/black-box-testing.md) 对于 **[system testing](../S/system-testing.md)** 和 **[user acceptance testing](../U/user-acceptance-testing.md) (UAT)** 至关重要，确保软件满足业务需求并准备好部署。
  最后，在**部署阶段**之后，[black box testing](../B/black-box-testing.md) 以**[regression testing](../R/regression-testing.md)** 的形式继续，以验证新更改不会对现有功能产生不利影响。当更新或补丁发布时，它也用于**[maintenance testing](../M/maintenance-testing.md)**。
  在整个 SDLC 中，[black box testing](../B/black-box-testing.md) 为 [quality assurance](../Q/quality-assurance.md) 提供了一种以用户为中心的方法，补充了[white box testing](../W/white-box-testing.md) 并确保软件从内到外和从外到内得到验证。

#### 黑盒测试如何用于端到端 (E2E) 测试？

在**端到端 (E2E) 测试**中，**[Black Box Testing](../B/black-box-testing.md)** 用于根据要求验证集成系统。测试人员不知道应用程序的内部工作原理，而是模拟用户行为，以确保所有互连的组件按预期一起运行。
  E2E测试涉及：

- **模拟真实用户场景**：测试人员创建从头到尾模仿用户操作的测试，涵盖典型的用户流程。
  - **在类似生产的环境中测试应用程序**：这包括与数据库、网络通信、外部服务和其他应用程序的交互。
  - **验证功能性和非[functional requirements](../F/functional-requirements.md)** ：在确保功能按预期工作的同时，测试人员还检查性能、可用​​性和可靠性。
  测试人员使用 [Selenium](../S/selenium.md)、[Cypress](../C/cypress.md) 或 Playwright 等自动化工具来编写这些场景的脚本，然后运行这些工具来验证应用程序的行为。这种方法有助于识别单元或集成测试可能遗漏的问题。
  **例子**：

  ```
  describe('User Registration and Login Process', () => {
    it('should register a new user', () => {
      // Steps to simulate user registration
    });
    it('should login with the new user', () => {
      // Steps to simulate user login
    });
    // Additional tests for subsequent user actions
  });
  ```通过关注用户的角度，黑盒端到端测试确保软件满足业务需求并为最终用户提供优质的体验。

- **模拟真实用户场景**：测试人员创建从头到尾模仿用户操作的测试，涵盖典型的用户流程。
  - **在类似生产的环境中测试应用程序**：这包括与数据库、网络通信、外部服务和其他应用程序的交互。
  - **验证功能性和非[functional requirements](../F/functional-requirements.md)** ：在确保功能按预期工作的同时，测试人员还检查性能、可用​​性和可靠性。
