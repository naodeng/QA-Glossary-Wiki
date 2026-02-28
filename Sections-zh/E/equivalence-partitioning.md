# 等价划分

<!-- TOC START -->
- [关于等价划分的问题？](#关于等价划分的问题？)
  - [基础知识和重要性](#基础知识和重要性)
    - [软件测试中的等价划分是什么？](#软件测试中的等价划分是什么？)
    - [为什么等价划分在软件测试中很重要？](#为什么等价划分在软件测试中很重要？)
    - [使用等价分区的主要好处是什么？](#使用等价分区的主要好处是什么？)
    - [等价划分如何提高测试效率？](#等价划分如何提高测试效率？)
    - [软件测试中如何实现等价划分？](#软件测试中如何实现等价划分？)
    - [等价划分涉及哪些步骤？](#等价划分涉及哪些步骤？)
    - [等价划分有哪些示例？](#等价划分有哪些示例？)
    - [等价划分如何与其他测试技术结合使用？](#等价划分如何与其他测试技术结合使用？)
  - [挑战和解决方案](#挑战和解决方案)
    - [实施等价划分时遇到的常见挑战有哪些？](#实施等价划分时遇到的常见挑战有哪些？)
    - [如何克服这些挑战？](#如何克服这些挑战？)
    - [有效实施等价划分的最佳实践有哪些？](#有效实施等价划分的最佳实践有哪些？)
    - [如何使用等价划分来处理软件测试中的边缘情况？](#如何使用等价划分来处理软件测试中的边缘情况？)
  - [高级概念](#高级概念)
    - [等价划分在端到端测试中的作用是什么？](#等价划分在端到端测试中的作用是什么？)
    - [等价划分如何帮助减少测试用例的数量？](#等价划分如何帮助减少测试用例的数量？)
    - [等价划分如何应用于现实场景？](#等价划分如何应用于现实场景？)
    - [等价划分和边界值分析之间有什么关系？](#等价划分和边界值分析之间有什么关系？)
<!-- TOC END -->

等价划分

是一个

软件测试

用于减少数量的技术

测试用例

通过将软件单元的输入数据划分为等效数据的分区。不是测试每一个可能的输入，

等价划分

提议

测试用例

可以针对每个分区的代表值进行设计。基本原则是，如果软件对于分区中的一个值表现正确，那么它对于同一分区中的所有其他值也表现正确，反之亦然。

## 关于等价划分的问题？

### 基础知识和重要性

#### 软件测试中的等价划分是什么？

[Equivalence Partitioning](../E/equivalence-partitioning.md) 是一种**[black box testing](../B/black-box-testing.md)** 方法，它将软件单元的输入数据划分为等效数据的分区，从中可以导出[test cases](../T/test-case.md)。在此技术中，[test cases](../T/test-case.md) 被设计为至少覆盖每个分区一次。此方法假设系统将以类似方式处理一个分区中的所有值。如果某个条件对于分区中的一种场景成立，则假定该条件对于该分区中的所有其他场景都成立。
  要应用[equivalence partitioning](../E/equivalence-partitioning.md)，您首先要识别影响测试对象执行的输入数据。然后，将此数据划分为等价分区或集合，其中程序对于分区的每个成员的行为应相同。通常，您将为每个分区创建一个[test case](../T/test-case.md)。
  例如，如果输入接受 1 到 10 之间的值范围，您将创建三个分区：一个用于低于该范围的值，一个用于该范围内的值，一个用于高于该范围的值。然后，您可以从每个分区中选择一个代表值进行测试。
  [Equivalence partitioning](../E/equivalence-partitioning.md) 通常与**边界值分析**一起使用，其中 [test cases](../T/test-case.md) 旨在包含分区边界处的值。它还与其他测试技术相结合，例如**[decision table testing](../D/decision-table-testing.md)**或**[state transition testing](../S/state-transition-testing.md)**，以确保测试空间的全面覆盖。

  ```
  // Example of a simple equivalence partitioning test case in TypeScript
  function testInputValue(input: number): string {
    if (input >= 1 && input <= 10) {
      return 'Valid input';
    } else {
      return 'Invalid input';
    }
  }
  // Equivalence partitions: <1, 1-10, >10
  // Test cases for each partition
  console.assert(testInputValue(0) === 'Invalid input');
  console.assert(testInputValue(5) === 'Valid input');
  console.assert(testInputValue(11) === 'Invalid input');
  ```通过关注代表性值，[equivalence partitioning](../E/equivalence-partitioning.md) 有助于减少[test cases](../T/test-case.md) 的数量，节省时间和资源，同时仍确保彻底的测试。

#### 为什么等价划分在软件测试中很重要？

[Equivalence partitioning](../E/equivalence-partitioning.md) 在[software testing](../S/software-testing.md) 中至关重要，因为它确保应用程序功能的**全面覆盖**，而不需要过多的[test cases](../T/test-case.md)。通过将输入数据划分为**等效类**，其中每个分区预计被软件以相同的方式处理，测试人员可以从每个分区中选择一个**代表值**进行测试。这种方法的目标是有效地识别**缺陷**，因为分区中的一个缺陷可能表明同一类中存在更多缺陷。
  此外，[equivalence partitioning](../E/equivalence-partitioning.md) 通过迫使测试人员质疑系统应如何处理不同的输入类，帮助**识别不明确的需求**。它还支持创建更**集中且有效的[test cases](../T/test-case.md)**，因为它消除了冗余并增加了捕获代表各自类别的错误的可能性。
  在实践中，[equivalence partitioning](../E/equivalence-partitioning.md) 通常与**边界值分析**一起使用，后者测试每个分区的边缘。这种组合在用**最少的[test cases](../T/test-case.md)** 捕获大量潜在的[bugs](../B/bug.md) 方面特别强大。这是一种与 **[risk-based testing](../R/risk-based-testing.md)** 方法保持一致的战略方法，优先考虑可能影响用户体验的应用程序的最关键领域。
  通过在保持覆盖范围的同时减小[test suite](../T/test-suite.md) 的大小，[equivalence partitioning](../E/equivalence-partitioning.md) 不仅节省了时间，而且**优化了资源分配**，使其成为[test automation](../T/test-automation.md) 工程师的一项关键技术，旨在实现高效且有效的测试流程。

#### 使用等价分区的主要好处是什么？

[Equivalence partitioning](../E/equivalence-partitioning.md) 提供了几个主要优点：

- **减少[test cases](../T/test-case.md)** ：通过将输入分组到系统处理相同的类中，可以最大限度地减少所需的测试用例数量，同时仍然确保彻底覆盖。
  - **增加[test coverage](../T/test-coverage.md)** ：它确保考虑所有可能的输入类，这可能导致发现临时测试可能遗漏的缺陷。
  - **节省时间和资源**：测试用例较少，测试速度更快，资源占用更少，从而可以更有效地分配测试工作。
  - **简化测试设计**：通过关注代表性值，测试用例设计变得更加简单和易于管理。
  - **有利于缺陷识别**：由于输入是从每个分区中系统地选择的，因此更容易查明哪个输入类导致缺陷。
  - **提高测试质量**：结构化方法可以带来更严格的测试和更高质量的软件。
  - **增强[maintainability](../M/maintainability.md)**：基于等价分区的测试套件更容易维护和更新，以响应软件的变化。
  在实践中，[equivalence partitioning](../E/equivalence-partitioning.md) 通常与**边界值分析**等技术一起使用来处理边缘情况，确保针对典型和极端输入条件的全面[test strategy](../T/test-strategy.md)。

- **减少[test cases](../T/test-case.md)** ：通过将输入分组到系统处理相同的类中，可以最大限度地减少所需的测试用例数量，同时仍然确保彻底覆盖。
  - **增加[test coverage](../T/test-coverage.md)** ：它确保考虑所有可能的输入类，这可能导致发现临时测试可能遗漏的缺陷。
  - **节省时间和资源**：测试用例较少，测试速度更快，资源占用更少，从而可以更有效地分配测试工作。
  - **简化测试设计**：通过关注代表性值，测试用例设计变得更加简单和易于管理。
  - **有利于缺陷识别**：由于输入是从每个分区中系统地选择的，因此更容易查明哪个输入类导致缺陷。
  - **提高测试质量**：结构化方法可以带来更严格的测试和更高质量的软件。
  - **增强[maintainability](../M/maintainability.md)**：基于等价分区的测试套件更容易维护和更新，以响应软件中的更改。

#### 等价划分如何提高测试效率？

[Equivalence partitioning](../E/equivalence-partitioning.md) 允许测试人员从每个分区或等价类中**识别代表值**，从而简化测试过程。测试人员可以选择代表较大组的几个值，而不是测试每个可能的输入（这通常是不切实际或不可能的）。这种方法显着减少了所需的 [test cases](../T/test-case.md)** 数量，而不会影响覆盖范围，因为假设每个值都会从被测系统中引发类似的响应。
  通过关注这些代表性值，测试人员可以更有效地分配资源，将时间投入到应用程序中更复杂或高风险的领域。 [Equivalence partitioning](../E/equivalence-partitioning.md) 还有助于**识别特定输入范围内的缺陷**，从而更容易查明和解决潜在问题。
  在实践中，该技术可以与**自动化[test scripts](../T/test-script.md)**相结合，以进一步提高效率。测试人员可以为每个分区编写一个脚本，并使用不同的输入值运行它，确保以最少的手动干预覆盖各种场景。
  总体而言，[equivalence partitioning](../E/equivalence-partitioning.md) 通过以下方式提高测试效率：

- **最小化[test cases](../T/test-case.md)**的数量
    同时保持覆盖范围。

- **节省时间和资源**
    通过避免多余的测试。

- **简化测试设计**
    和维护。

- **增强缺陷检测**
    在特定的输入范围内。

- **促进自动化**
    ，允许快速重新测试和回归测试。
  通过将[equivalence partitioning](../E/equivalence-partitioning.md)集成到他们的测试策略中，自动化工程师可以用更少的测试实现彻底的覆盖，从而实现更加简化和更具成本效益的测试过程。

- **Minimizing the number of [test cases](../T/test-case.md)**
    同时保持覆盖范围。

- **节省时间和资源**
    通过避免多余的测试。

- **简化测试设计**
    和维护。

- **增强缺陷检测**
    在特定的输入范围内。

- **促进自动化**
    ，允许快速重新测试和回归测试。

＃＃＃ 执行

#### 软件测试中如何实现等价划分？

在[software testing](../S/software-testing.md) 中实现[equivalence partitioning](../E/equivalence-partitioning.md) 涉及将输入数据划分为可作为单个代表性集进行测试的分区。这是一个简洁的方法：

1. **识别**
    可测试的函数及其输入数据。

2. **除法**
    函数的输入数据
    **等效数据类**
    其中每个类应该代表一组值，这些值预计会被代码以类似的方式处理。

3. **选择**
    一个或多个有效和无效分区。有效分区是那些遵循应用程序规则的分区。无效分区包含应拒绝的数据。

4. **创建**
    每个分区的测试用例。通常，每个分区一个测试用例就足够了。

5. **写**
    测试脚本重点关注
    **边界值**
    这些分区，因为它们通常是缺陷的根源。

6. **执行**
    测试用例和
    **验证**
    结果与预期结果相反。

  ```
  // Example: Testing a function that accepts age as input
  function isAdult(age) {
    return age >= 18;
  }
  // Equivalence partitions might be: < 18, 18-65, > 65
  // Test cases could be:
  // 1. Age = 17 (just below the boundary)
  // 2. Age = 30 (well within a valid range)
  // 3. Age = 70 (above the typical adult age range)
  ```请记住**将** [equivalence partitioning](../E/equivalence-partitioning.md) 与其他技术（例如边界值分析）结合起来，以获得更彻底的测试策略。 **尽可能实现自动化**以简化流程，并随着应用程序的发展**审查**分区决策。保持[test cases](../T/test-case.md) **可维护**和**可重用**，以最大限度地发挥[equivalence partitioning](../E/equivalence-partitioning.md) 的优势。

1. **识别**
    可测试的函数及其输入数据。

2. **除法**
    函数的输入数据
    **等效数据类**
    其中每个类应该代表一组值，这些值预计会被代码以类似的方式处理。

3. **选择**
    一个或多个有效和无效分区。有效分区是那些遵循应用程序规则的分区。无效分区包含应拒绝的数据。

4. **创建**
    每个分区的测试用例。通常，每个分区一个测试用例就足够了。

5. **写**
    测试脚本重点关注
    **边界值**
    这些分区，因为它们通常是缺陷的根源。

6. **执行**
    测试用例和
    **验证**
    结果与预期结果相反。

#### 等价划分涉及哪些步骤？

[equivalence partitioning](../E/equivalence-partitioning.md)涉及的步骤如下：

1. **识别可测试的功能**
    在接受一系列输入的应用程序内。

2. **除法**
    这些输入到组或分区中，其中组的每个成员都应被函数同等对待。

3. **定义边界**
    对于每个分区，确保它们是互斥的并且集体详尽的。

4. **选择[test cases](../T/test-case.md)**
    — 每个分区中的一个，通常是代表该组的值。

5. **Design and write [test scripts](../T/test-script.md)**
    针对被测功能或系统执行这些测试用例。

6. **运行测试**
    和
    **记录结果**
    ，验证每个分区的代表值的输出是否符合预期。

7. **分析故障**
    细化分区或识别代码中的缺陷。

8. **重复**
    如果在测试阶段发现新分区的过程。
  This technique is often combined with **boundary value analysis** to select [test cases](../T/test-case.md) at the edges of each partition.确保每个分区至少使用一个输入进行测试，以最大限度地提高覆盖范围，同时最大限度地减少 [test cases](../T/test-case.md) 的数量，这一点至关重要。

1. **识别可测试的功能**
    在接受一系列输入的应用程序内。

2. **除法**
    这些输入到组或分区中，其中组的每个成员都应被函数同等对待。

3. **定义边界**
    对于每个分区，确保它们是互斥的并且集体详尽的。

4. **选择[test cases](../T/test-case.md)**
    — 每个分区中的一个，通常是代表该组的值。

5. **设计并编写[test scripts](../T/test-script.md)**
    针对被测功能或系统执行这些测试用例。

6. **运行测试**
    和
    **记录结果**
    ，验证每个分区的代表值的输出是否符合预期。

7. **分析故障**
    细化分区或识别代码中的缺陷。

8. **重复**
    如果在测试阶段发现新分区的过程。

#### 等价划分有哪些示例？

[equivalence partitioning](../E/equivalence-partitioning.md) 的示例通常涉及将输入数据划分为有效和无效分区，从中可以导出[test cases](../T/test-case.md)。以下是一些场景：

1. **输入字段验证**：对于接受 1 到 100 之间年龄的文本字段：
    - 有效分区：
      `25`
      （范围内）

- 无效分区：
      `-5`
      （低于范围），
      `150`
      （高于范围）

- 有效分区：
      `25`
      （范围内）

- 无效分区：
      `-5`
      （低于范围），
      `150`
      （高于范围）

2. **用户角色权限**：对于具有“管理员”、“用户”和“访客”角色的系统：
    - 有效分区：使用“管理员”进行测试以确保授予所有权限。
    - 无效分区：使用“Guest”进行测试以确保访问受到限制。
    - 有效分区：使用“管理员”进行测试以确保授予所有权限。
    - 无效分区：使用“Guest”进行测试以确保访问受到限制。
  3. **文件上传功能**：接受1MB到5MB之间的文件：
    - 有效分区：
      `3MB`
      文件（在范围内）

- 无效分区：
      `500KB`
      文件（低于范围），
      `10MB`
      文件（超出范围）

- 有效分区：
      `3MB`
      文件（在范围内）

- 无效分区：
      `500KB`
      文件（低于范围），
      `10MB`
      文件（超出范围）

4. **日期输入**：对于处理当年日期的系统：
    - 有效分区：
      `July 15, current year`

- 无效分区：
      `January 1, next year`
      ,
      `December 31, previous year`

- 有效分区：
      `July 15, current year`

- 无效分区：
      `January 1, next year`
      ,
      `December 31, previous year`

5. **折扣代码申请**：对于适用于 50 美元以上订单的折扣代码：
    - 有效分区：
      `$60`
      订单（有折扣资格）

- 无效分区：
      `$40`
      订单（不符合条件），
      `$0`
      订单（不购买）

- 有效分区：
      `$60`
      订单（有折扣资格）

- 无效分区：
      `$40`
      订单（不符合条件），
      `$0`
      订单（不购买）

6. **搜索功能**：对于接受 1-50 个字母数字字符的搜索功能：
    - 有效分区：
      `Alpha123`
      （范围内）

- 无效分区：
      （空字符串），
      `Alpha123...`
      （51 个字符）

- 有效分区：
      `Alpha123`
      （范围内）

- 无效分区：
      （空字符串），
      `Alpha123...`
      （51 个字符）
  通过使用每个分区的代表性值进行测试，您可以确保覆盖范围而无需进行冗余测试。

1. **输入字段验证**：对于接受 1 到 100 之间年龄的文本字段：
    - 有效分区：
      `25`
      （范围内）

- 无效分区：
      `-5`
      （低于范围），
      `150`
      （高于范围）

- 有效分区：
      `25`
      （范围内）

- 无效分区：
      `-5`
      （低于范围），
      `150`
      （高于范围）

2. **用户角色权限**：对于具有“管理员”、“用户”和“访客”角色的系统：
    - 有效分区：使用“管理员”进行测试以确保授予所有权限。
    - 无效分区：使用“Guest”进行测试以确保访问受到限制。
    - 有效分区：使用“管理员”进行测试以确保授予所有权限。
    - 无效分区：使用“Guest”进行测试以确保访问受到限制。
  3. **文件上传功能**：接受1MB到5MB之间的文件：
    - 有效分区：
      `3MB`
      文件（在范围内）

- 无效分区：
      `500KB`
      文件（低于范围），
      `10MB`
      文件（超出范围）

- 有效分区：
      `3MB`
      文件（在范围内）

- 无效分区：
      `500KB`
      文件（低于范围），
      `10MB`
      文件（超出范围）

4. **日期输入**：对于处理当年日期的系统：
    - 有效分区：
      `July 15, current year`

- 无效分区：
      `January 1, next year`
      ,
      `December 31, previous year`

- 有效分区：
      `July 15, current year`

- 无效分区：
      `January 1, next year`
      ,
      `December 31, previous year`

5. **折扣代码申请**：对于适用于 50 美元以上订单的折扣代码：
    - 有效分区：
      `$60`
      订单（有折扣资格）

- 无效分区：
      `$40`
      订单（不符合条件），
      `$0`
      订单（不购买）

- 有效分区：
      `$60`
      订单（有折扣资格）

- 无效分区：
      `$40`
      订单（不符合条件），
      `$0`
      订单（不购买）

6. **搜索功能**：对于接受 1-50 个字母数字字符的搜索功能：
    - 有效分区：
      `Alpha123`
      （范围内）

- 无效分区：
      （空字符串），
      `Alpha123...`
      （51 个字符）

- 有效分区：
      `Alpha123`
      （范围内）

- 无效分区：
      （空字符串），
      `Alpha123...`
      （51 个字符）

#### 等价划分如何与其他测试技术结合使用？

[Equivalence partitioning](../E/equivalence-partitioning.md)可以与**边界值分析（BVA）**有效结合，以增强[test coverage](../T/test-coverage.md)。虽然[equivalence partitioning](../E/equivalence-partitioning.md) 将输入数据划分为派生[test cases](../T/test-case.md) 的分区，但BVA 关注这些分区的边缘。通过集成两者，您可以确保典型值和边缘情况都得到测试，从而实现更稳健的测试。
  将 **[decision table testing](../D/decision-table-testing.md)** 与 [equivalence partitioning](../E/equivalence-partitioning.md) 结合起来也可能是有益的。决策表代表复杂的业务逻辑，可以针对不同的输入组合进行测试。 [Equivalence partitioning](../E/equivalence-partitioning.md)可用于从这些组合中选择代表性输入，确保对逻辑进行全面评估，而无需冗余测试。
  **[State transition testing](../S/state-transition-testing.md)** 是另一种补充 [equivalence partitioning](../E/equivalence-partitioning.md) 的技术。它涉及测试不同的系统状态和转换。 [Equivalence partitioning](../E/equivalence-partitioning.md) 可以帮助识别有效和无效的状态转换，然后可用于创建状态转换测试。
  对于 **[integration testing](../I/integration-testing.md)**，[equivalence partitioning](../E/equivalence-partitioning.md) 可用于创建 [test cases](../T/test-case.md) 以进行模块交互。通过识别集成输入和输出的分区，您可以确保针对典型和非典型数据集测试模块之间的交互。
  最后，当使用**自动测试生成工具**时，[equivalence partitioning](../E/equivalence-partitioning.md)可以指导输入数据集的生成。通过向工具提供识别的分区，它可以自动生成多样化且相关的[test cases](../T/test-case.md)，从而提高[automated testing](../A/automated-testing.md)的效率。
  通过将 [equivalence partitioning](../E/equivalence-partitioning.md) 与这些技术相结合，您可以实现更全面、更高效的测试流程，确保涵盖常见和关键的边缘情况。

### 挑战和解决方案

#### 实施等价划分时遇到的常见挑战有哪些？

实施[equivalence partitioning](../E/equivalence-partitioning.md)时遇到的常见挑战包括：

- **识别适当的分区**：确定正确的等价类需要深入了解应用程序的功能和输入域。不正确定义的分区可能会导致测试不充分。
  - **处理复杂的输入域**：对于具有复杂输入结构的应用程序，创建既全面又易于管理的等价类可能很困难。
  - **重叠分区**：存在创建重叠分区的风险，这可能会导致 [test cases](../T/test-case.md) 中出现冗余并浪费资源。
  - **边界识别**：虽然[equivalence partitioning](../E/equivalence-partitioning.md) 专注于将分区内的输入视为相同，但识别和正确测试分区之间的边界可能具有挑战性。
  - **数据驱动的应用程序**：严重依赖数据输入的应用程序可能需要动态等价类，这会使分区过程变得复杂。
  - **需求变化**：不断变化的需求可能会使现有分区失效，从而需要频繁审查和更新[test cases](../T/test-case.md)。
  - **与其他测试方法集成**：将[equivalence partitioning](../E/equivalence-partitioning.md) 与其他测试技术（如边界值分析）有效结合，需要仔细规划以避免重复工作。
  为了克服这些挑战，随着应用程序及其需求的发展，**定期审查和更新**等价类。使用支持[equivalence partitioning](../E/equivalence-partitioning.md)的**工具和框架**来管理复杂的输入域。确保团队成员之间**清晰的沟通**，以保持对分区的共同理解。最后，**将[equivalence partitioning](../E/equivalence-partitioning.md) 与其他测试策略仔细集成**，以最大限度地提高[test coverage](../T/test-coverage.md) 和效率。

- **识别适当的分区**：确定正确的等价类需要深入了解应用程序的功能和输入域。不正确定义的分区可能会导致测试不充分。
  - **处理复杂的输入域**：对于具有复杂输入结构的应用程序，创建既全面又易于管理的等价类可能很困难。
  - **重叠分区**：存在创建重叠分区的风险，这可能会导致 [test cases](../T/test-case.md) 中出现冗余并浪费资源。
  - **边界识别**：虽然[equivalence partitioning](../E/equivalence-partitioning.md) 专注于将分区内的输入视为相同，但识别和正确测试分区之间的边界可能具有挑战性。
  - **数据驱动的应用程序**：严重依赖数据输入的应用程序可能需要动态等价类，这会使分区过程变得复杂。
  - **需求变化**：不断变化的需求可能会使现有分区失效，从而需要频繁审查和更新[test cases](../T/test-case.md)。
  - **与其他测试方法集成**：将 [equivalence partitioning](../E/equivalence-partitioning.md) 与其他测试技术（如边界值分析）有效结合，需要仔细规划以避免重复工作。

#### 如何克服这些挑战？

克服[equivalence partitioning](../E/equivalence-partitioning.md) 中的挑战需要结合**战略规划**、**工具熟练程度**和**分析技能**。方法如下：

- **尽可能自动化**：使用测试自动化工具处理重复性任务，确保一致性并节省时间。自动化还可以帮助管理大量的等价类和测试用例。

  ```
  // Example: Automating test case generation
  const equivalenceClasses = defineEquivalenceClasses(inputDomain);
  const testCases = generateTestCases(equivalenceClasses);
  ```

- **与开发人员合作**：与开发人员合作以了解应用程序的逻辑，这可以帮助识别相关的等价类并避免无效的类。
  - **优先考虑[Test Cases](../T/test-case.md)**：首先关注高风险区域。根据失败的可能性和潜在[bugs](../B/bug.md) 的影响确定[test cases](../T/test-case.md) 的优先级。
  - **审查和优化**：定期审查等效类和[test cases](../T/test-case.md)，以确保它们与应用程序更改保持同步。
  - **组合技术**：将[equivalence partitioning](../E/equivalence-partitioning.md) 与边界值分析等其他测试技术结合使用，以更有效地覆盖边缘情况。
  - **利用领域知识**：应用领域专业知识来识别可能不会立即明显的微妙等价类。
  - **教育团队**：确保整个团队了解[equivalence partitioning](../E/equivalence-partitioning.md) 对于培养以质量为中心的方法的重要性。
  - **使用版本控制**：在版本控制系统中维护[test cases](../T/test-case.md) 和等效类，以跟踪更改并高效协作。
  通过集中解决这些挑战，[test automation](../T/test-automation.md) 工程师可以提高[equivalence partitioning](../E/equivalence-partitioning.md) 的有效性并提供更可靠的软件。

- **尽可能自动化**：使用测试自动化工具处理重复性任务，确保一致性并节省时间。自动化还可以帮助管理大量的等价类和测试用例。
  - **与开发人员合作**：与开发人员合作以了解应用程序的逻辑，这可以帮助识别相关的等价类并避免无效的类。
  - **优先考虑[Test Cases](../T/test-case.md)**：首先关注高风险区域。根据失败的可能性和潜在[bugs](../B/bug.md) 的影响确定[test cases](../T/test-case.md) 的优先级。
  - **审查和优化**：定期审查等效类和[test cases](../T/test-case.md)，以确保它们与应用程序更改保持同步。
  - **组合技术**：将[equivalence partitioning](../E/equivalence-partitioning.md) 与边界值分析等其他测试技术结合使用，以更有效地覆盖边缘情况。
  - **利用领域知识**：应用领域专业知识来识别可能不会立即明显的微妙等价类。
  - **教育团队**：确保整个团队了解[equivalence partitioning](../E/equivalence-partitioning.md) 对于培养以质量为中心的方法的重要性。
  - **使用版本控制**：在版本控制系统中维护[test cases](../T/test-case.md) 和等效类以跟踪更改并高效协作。

#### 有效实施等价划分的最佳实践有哪些？

要有效实施 **[equivalence partitioning](../E/equivalence-partitioning.md)**：

- **识别有效和无效分区**
    清楚地。确保每个分区都反映一组应由软件同等对待的输入条件。

- **选择代表值**
    从每个分区。选择典型且可能发现缺陷的值。

- **避免冗余测试**
    除非有特定原因，否则不要从同一分区中选择多个值。

- **考虑应用程序上下文**
    。了解业务逻辑以确定反映用户行为的有意义的分区。

- **明智地使用自动化**
    。自动从分区生成测试用例，以节省时间并减少人为错误。

- **结合边界值分析**
    进行彻底的测试。测试边界和分区值以捕获相差一的错误和类似问题。

- **审查和细化分区**
    随着应用程序的发展。添加新功能或对应用程序进行更改时更新分区。

- **记录你的方法**
    供将来参考和新团队成员使用。这有助于保持一致性和知识共享。
  以下是 TypeScript 中的一个简单示例，使用假设函数 `calculateDiscount`，该函数根据订单金额应用不同的折扣率：

  ```
  describe('calculateDiscount Equivalence Partitioning', () => {
    it('should apply 5% discount for orders between $50 and $100', () => {
      expect(calculateDiscount(75)).toEqual(3.75); // Representative of this partition
    });
    it('should apply 10% discount for orders between $101 and $500', () => {
      expect(calculateDiscount(250)).toEqual(25); // Representative of this partition
    });
    // Additional tests for other partitions...
  });
  ```通过关注这些实践，您可以确保 [equivalence partitioning](../E/equivalence-partitioning.md) 在您的 [test automation](../T/test-automation.md) 工作中高效且有效地应用。

- **识别有效和无效分区**
    清楚地。确保每个分区都反映一组应由软件同等对待的输入条件。

- **选择代表值**
    从每个分区。选择典型且可能发现缺陷的值。

- **避免冗余测试**
    除非有特定原因，否则不要从同一分区中选择多个值。

- **考虑应用程序上下文**
    。了解业务逻辑以确定反映用户行为的有意义的分区。

- **明智地使用自动化**
    。自动从分区生成测试用例，以节省时间并减少人为错误。

- **结合边界值分析**
    进行彻底的测试。测试边界和分区值以捕获相差一的错误和类似问题。

- **审查和细化分区**
    随着应用程序的发展。添加新功能或对应用程序进行更改时更新分区。

- **记录你的方法**
    供将来参考和新团队成员使用。这有助于保持一致性和知识共享。

#### 如何使用等价划分来处理软件测试中的边缘情况？

[Equivalence partitioning](../E/equivalence-partitioning.md) 通过对系统应同等对待的输入进行分组来简化[test case](../T/test-case.md) 设计。为了处理边缘情况，可以通过考虑这些分区的边界来扩展该技术。虽然 [equivalence partitioning](../E/equivalence-partitioning.md) 假设系统将同等地处理分区中的所有值，但边缘情况通常发生在这些分区的极端处。
  为了有效管理边缘情况，测试人员应该：

- **确定边界条件**
    对于每个等价分区。这些是分区最末端的值，例如最大和最小可能值。

- **创建额外的[test cases](../T/test-case.md)**
    专门针对这些边界条件。这是边界值分析 (BVA) 补充等价分区的地方，重点关注每个分区边缘的值。

- **考虑相差一的错误**
    ，这在边缘很常见。测试边界内部和外部的值以捕获这些错误。
  For example, if an input field accepts ages from 1 to 100, [equivalence partitioning](../E/equivalence-partitioning.md) might suggest a valid partition (1-100) and two invalid partitions (less than 1, more than 100).要处理边缘情况，请测试边界：1 和 100 表示有效分区，0 和 101 表示无效分区。
  By combining [equivalence partitioning](../E/equivalence-partitioning.md) with careful attention to boundary conditions, testers can ensure that edge cases are not overlooked, leading to more robust and reliable software.

- **确定边界条件**
    对于每个等价分区。这些是分区最末端的值，例如最大和最小可能值。

- **Create additional [test cases](../T/test-case.md)**
    专门针对这些边界条件。这是边界值分析 (BVA) 补充等价分区的地方，重点关注每个分区边缘的值。

- **考虑相差一的错误**
    ，这在边缘很常见。测试边界内部和外部的值以捕获这些错误。

### 高级概念

#### 等价划分在端到端测试中的作用是什么？

在[end-to-end testing](../E/end-to-end-testing.md) 中，**[equivalence partitioning](../E/equivalence-partitioning.md)** 通过对应产生类似结果的输入进行分组，在确保全面覆盖应用程序工作流程方面发挥着至关重要的作用。该技术允许测试人员从每个分区中选择代表值，从而验证系统在各种场景中的行为，而无需测试每个可能的输入。
  当应用于端到端场景时，[equivalence partitioning](../E/equivalence-partitioning.md) 有助于识别可以使用最小但有效的[test cases](../T/test-case.md) 集进行测试的关键路径和功能。它通过关注数据从开始到结束流经整个系统时的有效性来简化流程，确保每个功能区域都经过充分测试。
  通过使用[equivalence partitioning](../E/equivalence-partitioning.md)，[test automation](../T/test-automation.md) 工程师可以制作**高级[test cases](../T/test-case.md)** 来模拟跨系统集成组件的用户交互和数据处理。在处理复杂系统时，这种方法特别有用，因为在复杂系统中测试输入和状态的每种可能的组合是不切实际的。
  实际上，[end-to-end testing](../E/end-to-end-testing.md) 中的 [equivalence partitioning](../E/equivalence-partitioning.md) 可能涉及：

- 在工作流程开始时定义用户输入的分区。
  - 识别代表工作流程结束时系统响应的输出分区。
  - 选择触发不同应用程序路径的输入值，确保覆盖典型用例和异常条件。
  最终，[end-to-end testing](../E/end-to-end-testing.md) 中的[equivalence partitioning](../E/equivalence-partitioning.md) 确保[test automation](../T/test-automation.md) 既高效又有效，以更少、更有针对性的测试覆盖广泛的场景。

- 在工作流程开始时定义用户输入的分区。
  - 识别代表工作流程结束时系统响应的输出分区。
  - 选择触发不同应用程序路径的输入值，确保覆盖典型用例和异常条件。

#### 等价划分如何帮助减少测试用例的数量？

[Equivalence partitioning](../E/equivalence-partitioning.md) 允许测试人员识别预期产生类似结果的输入并将其分组到**等价类**，从而帮助减少[test cases](../T/test-case.md) 的数量。通过这样做，只需要测试每个类中的几个[test cases](../T/test-case.md)，而不是详尽地检查每个可能的输入。这种方法假设如果分区中的一个 [test case](../T/test-case.md) 通过，同一分区中的其他情况也将通过，从而显着减少所需的测试总数。
  例如，如果输入字段接受从 1 到 100 的数字，您可以创建两个分区，而不是写入 100 个单独的 [test cases](../T/test-case.md)：一个用于有效输入 (1-100)，另一个用于无效输入（其他所有内容）。然后，从每个分区中选择代表性值，例如 1、50 和 100 作为有效范围，以及一些超出范围的值作为无效分区。该策略确保使用最少的 [test cases](../T/test-case.md) 集覆盖所有可能的场景，从而优化时间和资源。
  在实践中，[equivalence partitioning](../E/equivalence-partitioning.md)经常与**边界值分析**结合使用，其中[test cases](../T/test-case.md)是围绕每个分区的边缘设计的。通过关注最有可能发生错误的区域（例如输入限制和边界），测试人员可以进一步增强[test suite](../T/test-suite.md) 的有效性，而无需不必要的重复工作。

#### 等价划分如何应用于现实场景？

[Equivalence partitioning](../E/equivalence-partitioning.md)实际上可以应用于输入数据或操作条件可以分为几组从而从系统中引发相同响应的场景。例如，考虑一个接受年龄作为输入的 Web 表单。您可以创建“18 岁以下”、“18 至 65 岁”和“65 岁以上”等分区，而不是测试每个可能的年龄。然后，您可以从每个分区中选择一个代表值进行测试，确保覆盖不同的用户群体。
  在[API testing](../A/api-testing.md) 中，如果端点接受参数值的范围，您可以将该范围划分为有效组、无效组和边界组。通过使用每个分区的值进行测试，您可以断言 [API](../A/api.md) 在其预期操作范围内的行为，而无需对每个可能的输入进行冗余测试。
  对于[performance testing](../P/performance-testing.md)，[equivalence partitioning](../E/equivalence-partitioning.md) 可应用于用户负载级别。您可以使用代表性负载级别（例如“轻”、“中”、“重”和“峰值”）进行测试，以了解不同压力条件下的系统性能，而不是一次增加一个用户。
  在[database](../D/database.md) 测试中，您可以根据数据类型、大小或格式等标准对数据集进行分区。使用每个分区的子集进行测试可确保[database](../D/database.md) 按预期处理各种数据。
  在进行配置测试时，可以根据不同的系统配置或环境进行分区。从每个分区中选择一个代表性集有助于验证软件在各种 [setups](../S/setup.md) 上的行为是否一致。

  ```
  // Pseudo-code example for age input validation
  const agePartitions = {
    minor: 16, // representative of under 18
    adult: 30, // representative of 18 to 65
    senior: 70 // representative of over 65
  };
  for (const [group, age] of Object.entries(agePartitions)) {
    test(`Age input for ${group}`, () => {
      const response = submitAgeForm(age);
      expect(response).toBeValid();
    });
  }
  ```通过关注每个分区中的代表性[test cases](../T/test-case.md)，您可以使用更少的[test cases](../T/test-case.md) 实现全面的[test coverage](../T/test-coverage.md)，从而节省时间和资源，同时保持对软件质量的信心。

#### 等价划分和边界值分析之间有什么关系？

[Equivalence Partitioning](../E/equivalence-partitioning.md) (EP) and Boundary Value Analysis (BVA) are complementary testing techniques used to design [test cases](../T/test-case.md). EP divides input data of a software module into partitions of equivalent data from which [test cases](../T/test-case.md) can be derived.相比之下，BVA 侧重于这些分区边缘的值。
  EP 和 BVA 之间的关系是 **BVA 通常应用于 EP 标识的等价分区**的边界。 EP 确保每个分区至少由一个 [test case](../T/test-case.md) 表示，而 BVA 确保这些分区的边界经过彻底测试。这是因为**错误更有可能发生在输入范围的边缘**而不是中间。
  通过结合 EP 和 BVA，测试人员可以创建一组更强大的[test cases](../T/test-case.md)，涵盖代表性值和可能导致缺陷的边缘情况。使用 EP，测试人员可以确定要测试的内容，而使用 BVA，他们可以准确地确定应重点关注输入范围极端值的位置。
  实际上，在识别等效分区后，测试人员通常会从每个分区的**中间选择 [test cases](../T/test-case.md)（使用 EP），然后用 [test cases](../T/test-case.md) 对其进行补充，以测试每个分区的**上限和下限**（使用 BVA）。这种双重方法有助于通过最少的[test cases](../T/test-case.md) 集实现全面的[test coverage](../T/test-coverage.md)，从而确保测试过程的效率和有效性。
