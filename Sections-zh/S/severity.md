# 严重性

<!-- TOC START -->
- [关于严重性的问题？](#关于严重性的问题？)
  - [基础知识和重要性](#基础知识和重要性)
    - [软件测试中严重性的定义是什么？](#软件测试中严重性的定义是什么？)
    - [为什么理解严重性在软件测试中很重要？](#为什么理解严重性在软件测试中很重要？)
    - [错误跟踪中的严重性与优先级有何不同？](#错误跟踪中的严重性与优先级有何不同？)
  - [严重级别](#严重级别)
    - [软件测试有哪些不同的严重级别？](#软件测试有哪些不同的严重级别？)
    - [如何确定错误的严重级别？](#如何确定错误的严重级别？)
    - [高严重性错误对软件有何影响？](#高严重性错误对软件有何影响？)
  - [严重性和错误生命周期](#严重性和错误生命周期)
    - [严重性如何影响错误生命周期？](#严重性如何影响错误生命周期？)
    - [严重性在错误分类中扮演什么角色？](#严重性在错误分类中扮演什么角色？)
    - [bug 的严重性如何影响其解决时间？](#bug-的严重性如何影响其解决时间？)
  - [不同测试阶段的严重性](#不同测试阶段的严重性)
    - [单元测试中如何考虑严重性？](#单元测试中如何考虑严重性？)
    - [集成测试中如何考虑严重性？](#集成测试中如何考虑严重性？)
    - [系统测试中如何考虑严重性？](#系统测试中如何考虑严重性？)
    - [验收测试中如何考虑严重性？](#验收测试中如何考虑严重性？)
  - [测试管理的严重性](#测试管理的严重性)
    - [严重性如何影响测试用例设计？](#严重性如何影响测试用例设计？)
    - [严重性如何影响测试执行计划？](#严重性如何影响测试执行计划？)
    - [严重性如何影响测试报告？](#严重性如何影响测试报告？)
<!-- TOC END -->

严重性

衡量缺陷对应用程序系统的影响。具有重大系统影响的缺陷被分配更高的等级

严重程度

水平，通常由

品质保证

工程师。

## 关于严重性的问题？

### 基础知识和重要性

#### 软件测试中严重性的定义是什么？

在[software testing](../S/software-testing.md) 中，**[severity](../S/severity.md)** 指的是缺陷对软件操作的影响。它指示[bug](../B/bug.md) 可以影响系统功能、性能或稳定性的程度。 [Severity](../S/severity.md) 通常分为**严重**、**高**、**中**和**低**等类别，反映了从系统崩溃或数据丢失到不会严重影响用户体验的小问题的范围。确定[severity](../S/severity.md) 是一项技术评估，不一定考虑解决问题的时间表或业务优先级。对于[test automation](../T/test-automation.md) 工程师来说，准确评估和分配[severity](../S/severity.md) 至关重要，以确保及时解决最具影响力的缺陷并保持软件产品的质量。

#### 为什么理解严重性在软件测试中很重要？

了解[software testing](../S/software-testing.md) 中的[severity](../S/severity.md) 至关重要，因为它有助于有效地**分配资源**并**确定**测试和[bug](../B/bug.md) 修复工作的优先级。 [Severity](../S/severity.md)表示缺陷对系统运行的影响，这直接影响与软件发布相关的**风险**。
  当识别出 [bug](../B/bug.md) 时，了解其 [severity](../S/severity.md) 允许测试工程师向利益相关者**传达潜在后果**，确保首先解决最关键的问题。这种优先级确保软件在发布前满足其**质量标准**和**[functional requirements](../F/functional-requirements.md)**。
  此外，[severity](../S/severity.md) 理解有助于**风险管理**。高[severity](../S/severity.md) [bugs](../B/bug.md) 可能会带来重大风险，例如数据丢失、安全漏洞或系统崩溃，这可能会给最终用户和公司带来可怕的影响。通过关注这些[bugs](../B/bug.md)，团队可以降低风险并防止昂贵的发布后修复或对公司声誉的损害。
  此外，[severity](../S/severity.md) 在**测试计划**中发挥着作用。 [Test cases](../T/test-case.md) 涵盖容易出现高[severity](../S/severity.md) 问题的功能可以在测试周期的早期执行。这种早期检测可以让我们有更多的时间来解决严重缺陷并管理其对项目时间表的影响。
  最后，[severity](../S/severity.md) 评估有助于测试过程中的**持续改进**。通过分析过去缺陷的[severity](../S/severity.md)，团队可以识别可能需要更强大的测试或设计改进的应用程序区域，从而在未来的版本中实现更高的质量。

#### 错误跟踪中的严重性与优先级有何不同？

[bug](../B/bug.md) 跟踪中的[Severity](../S/severity.md) 和[priority](../P/priority.md) 是不同但相关的概念。 **[Severity](../S/severity.md)** 指[bug](../B/bug.md) 对系统功能的影响，从严重的系统崩溃到轻微的 UI 问题。这是对[bug](../B/bug.md) 技术影响的客观衡量。
  另一方面，**[Priority](../P/priority.md)** 表示应根据业务需求、客户影响或发布计划等因素处理 [bug](../B/bug.md) 的顺序。这是团队做出的主观决定，通常受到外部利益相关者的影响。
  虽然高[severity](../S/severity.md) [bug](../B/bug.md) 通常命令高[priority](../P/priority.md)，但情况并非总是如此。例如，影响很少使用的功能的严重 [bug](../B/bug.md) 可能会被赋予比关键组件中中等 [bug](../B/bug.md) 更低的[priority](../P/priority.md)。相反，如果影响关键营销功能，低[severity](../S/severity.md) 外观问题可能会被优先考虑。
  本质上，[severity](../S/severity.md) 是关于[bug](../B/bug.md) 的技术效果，而[priority](../P/priority.md) 是关于在项目目标的背景下修复它的紧迫性。两者对于有效的[bug](../B/bug.md) 管理和确保质量和交付时间的平衡至关重要。

### 严重级别

#### 软件测试有哪些不同的严重级别？

[software testing](../S/software-testing.md) 中的 [Severity](../S/severity.md) 级别通常范围从 **严重** 到 **轻微**：

- **严重**：该缺陷导致系统故障或对系统安全构成重大威胁。必须立即解决它，因为它会影响业务运营和数据完整性。
  - **高**：[bug](../B/bug.md) 会严重损害功能，但有一个解决方法。应在产品发布前解决。
  - **中**：此级别表示影响功能的问题，但影响小于高 [severity](../S/severity.md) 问题。在解决高[severity](../S/severity.md)问题后应该修复它。
  - **低**：该缺陷会造成不便，通常与不影响应用程序核心功能的 UI 或可用性问题相关。
  - **次要**：这些是不需要立即关注的小问题，并且对应用程序功能的影响最小。
  每个组织可能有自己的一组[severity](../S/severity.md)级别或定义，但上述类别在行业中常用。 [Severity](../S/severity.md) 级别指导[bugs](../B/bug.md) 的处理顺序，并帮助有效管理测试和开发工作。

- **严重**：该缺陷导致系统故障或对系统安全构成重大威胁。必须立即解决它，因为它会影响业务运营和数据完整性。
  - **高**：[bug](../B/bug.md) 会严重损害功能，但有一个解决方法。应在产品发布前解决。
  - **中**：此级别表示影响功能的问题，但影响小于高 [severity](../S/severity.md) 问题。在解决高[severity](../S/severity.md)问题后应该修复它。
  - **低**：该缺陷会造成不便，通常与不影响应用程序核心功能的 UI 或可用性问题相关。
  - **次要**：这些是不需要立即关注的小问题，并且对应用程序功能的影响最小。

#### 如何确定错误的严重级别？

[bug](../B/bug.md) 的[severity](../S/severity.md) 级别是通过评估其**对系统功能**、**用户体验**和**业务运营**的影响来确定的。要评估[severity](../S/severity.md)，请考虑以下因素：

- **功能影响**：错误如何影响应用程序功能？
    它是否会导致完全故障、部分故障或轻微的不便？

- **数据影响**：该错误是否会导致数据丢失、损坏或损害数据完整性？
  - **频率**：错误发生的频率是多少？
    它是容易重现还是罕见的事件？

- **范围**：问题是否仅限于特定模块，或者是否对整个应用程序产生广泛影响？
  - **用户影响**：该错误如何影响最终用户？
    考虑对可用性的直接影响以及对用户感知和满意度的间接影响。

- **解决方法可用性**：用户能否通过替代方法绕过该问题，或者该错误是否会在没有解决方法的情况下阻止关键功能？
  - **法律与合规性**：该错误是否会导致不遵守监管要求或合同义务？
  考虑这些因素后，[bug](../B/bug.md) 通常分为 **严重**、**高**、**中** 或 **低** [severity](../S/severity.md) 等类别。分类通常是测试人员、开发人员和产品经理共同做出的决定，确保对[bug](../B/bug.md) 的影响有一个平衡的视角。该评估指导优先顺序和解决工作，确保最有害的问题得到及时解决。

- **功能影响**：错误如何影响应用程序功能？
    它是否会导致完全故障、部分故障或轻微的不便？

- **数据影响**：该错误是否会导致数据丢失、损坏或损害数据完整性？
  - **频率**：错误发生的频率是多少？
    它是容易重现还是罕见的事件？

- **范围**：问题是否仅限于特定模块，或者是否对整个应用程序产生广泛影响？
  - **用户影响**：该错误如何影响最终用户？
    考虑对可用性的直接影响以及对用户感知和满意度的间接影响。

- **解决方法可用性**：用户能否通过替代方法绕过该问题，或者该错误是否会在没有解决方法的情况下阻止关键功能？
  - **法律与合规性**：该错误是否会导致不遵守监管要求或合同义务？

#### 高严重性错误对软件有何影响？

高 [severity](../S/severity.md) [bugs](../B/bug.md) 对软件有重大影响，因为它们通常表明可能导致系统崩溃、数据丢失或安全漏洞的关键问题。这些[bugs](../B/bug.md)经常：

- **阻止**
    主要功能，阻止用户执行基本操作。

- **需要立即关注**
    和资源，可能会扰乱开发工作流程并导致重新确定任务的优先级。

- **增加风险**
    如果在开发周期的后期发现它们会错过发布截止日期。

- **影响客户信任**
    如果它们投入生产，特别是当它们损害数据完整性或隐私时，我们会感到满意。

- **需要广泛的测试**
    后修复以确保问题得到解决而不会引入新问题，否则会进一步延迟发布。
  在[test automation](../T/test-automation.md) 中，高[severity](../S/severity.md) [bugs](../B/bug.md) 可能会导致：

- **重新评估[test coverage](../T/test-coverage.md)**
    了解为什么这个错误没有被更早地发现。

- **测试策略的调整**
    对关键领域进行更严格的检查。

- **增加维护**
    如果错误导致应用程序代码库发生重大变化，则测试脚本的数量。
  总体而言，高[severity](../S/severity.md) [bugs](../B/bug.md) 需要迅速而彻底的响应，以维持[software quality](../S/software-quality.md) 和项目时间表。

- **阻止**
    主要功能，阻止用户执行基本操作。

- **需要立即关注**
    和资源，可能会扰乱开发工作流程并导致重新确定任务的优先级。

- **增加风险**
    如果在开发周期的后期发现它们会错过发布截止日期。

- **影响客户信任**
    如果它们投入生产，特别是当它们损害数据完整性或隐私时，我们会感到满意。

- **需要广泛的测试**
    后修复以确保问题得到解决而不会引入新问题，否则会进一步延迟发布。

- **重新评估[test coverage](../T/test-coverage.md)**
    了解为什么这个错误没有被更早地发现。

- **测试策略的调整**
    对关键领域进行更严格的检查。

- **增加维护**
    如果错误导致应用程序代码库发生重大变化，则测试脚本的数量。

### 严重性和错误生命周期

#### 严重性如何影响错误生命周期？

[Severity](../S/severity.md) 通过影响开发和测试阶段处理[bugs](../B/bug.md) 的**顺序**和**紧迫性**来影响[bug](../B/bug.md) 生命周期。高[severity](../S/severity.md) [bugs](../B/bug.md) 通常会导致**发布过程停止**，直到它们得到解决，因为它们可能会对系统或最终用户体验造成重大损害。这些[bugs](../B/bug.md) 通常被**升级**到开发团队优先事项的首位。
  相反，较低的[severity](../S/severity.md) [bugs](../B/bug.md) 可能会安排在以后的版本中进行修复，或者可能与其他次要修复捆绑在一起。用于修复[bugs](../B/bug.md)的**工作流程**和**资源分配**通常直接与其[severity](../S/severity.md)相关；关键[bugs](../B/bug.md)可能需要高级开发人员立即关注或导致**加班**，而次要问题可以分配给经验不足的团队成员或在正常开发周期中解决。
  此外，[severity](../S/severity.md) 会影响与利益相关者的**沟通**​​。高[severity](../S/severity.md) 问题通常需要立即向内部团队和潜在的外部利益相关者发出通知和详细报告，具体取决于[bug](../B/bug.md) 的性质和业务环境。
  在[automated testing](../A/automated-testing.md) 环境中，[severity](../S/severity.md) 还可以影响**自动化策略**。覆盖应用程序关键区域的测试可能会在持续集成管道中更频繁地运行或使用更高的[priority](../P/priority.md)，以确保尽早捕获并解决高[severity](../S/severity.md) [bugs](../B/bug.md)。
  总体而言，[severity](../S/severity.md) 是与 [bug](../B/bug.md) 修复相关的 **决策过程** 的关键因素，影响从优先级和资源管理到利益相关者沟通和测试策略的各个方面。

#### 严重性在错误分类中扮演什么角色？

在[bug](../B/bug.md) 分类中，**[severity](../S/severity.md)** 在有关**资源分配**和**[bug](../B/bug.md) 修复顺序**的决策过程中发挥着关键作用。它有助于评估 [bug](../B/bug.md)** 对应用程序功能和用户体验的影响。在分类会议期间，团队评估[severity](../S/severity.md) 以了解问题的**紧迫性**和**范围**。
  高[severity](../S/severity.md) [bugs](../B/bug.md) 通常需要**立即关注**，并可能导致开发和测试工作的**重新确定优先级**。如果它们对产品的稳定性或安全性构成重大风险，它们还可能触发对发布时间表的**重新评估**。相反，较低的 [severity](../S/severity.md) [bugs](../B/bug.md) 可能会安排在以后的冲刺或发布中，从而使团队能够首先关注更关键的问题。
  [severity](../S/severity.md) 评估会影响与利益相关者的**沟通**​​，因为高[severity](../S/severity.md) 问题可能需要立即通知和详细报告。它还指导**风险管理策略**，确保最具破坏性的[bugs](../B/bug.md)得到及时解决，以尽量减少其对最终产品的影响。
  在[automated testing](../A/automated-testing.md) 场景中，[severity](../S/severity.md) 可以规定**自动化策略**，例如优先为应用程序的关键区域创建自动化测试，以在未来的开发周期中快速识别和解决高[severity](../S/severity.md) [bugs](../B/bug.md) 问题。
  最终，在分类过程中理解并准确评估[bug](../B/bug.md) [severity](../S/severity.md) 可确保团队能够保持**平衡的工作量**，**优化[quality assurance](../Q/quality-assurance.md) 流程**，并在所需的时间范围内交付**可靠的软件产品**。

#### bug 的严重性如何影响其解决时间？

[bug](../B/bug.md) 的 **[severity](../S/severity.md)** 通常指示其解决方案的紧迫性。高[severity](../S/severity.md) [bugs](../B/bug.md)，例如导致数据丢失、安全漏洞或系统崩溃的问题，通常会**立即**解决，因为它们可能严重影响应用程序的功能或用户体验。这些[bugs](../B/bug.md)可以停止生产或发布过程，直到解决为止。
  相反，较低级别的[severity](../S/severity.md) [bugs](../B/bug.md)（例如较小的 UI 问题或拼写错误）可能会安排在未来版本中或在不太重要的维护时段内解决。它们的解决时间通常较长，因为它们不会妨碍核心功能，并且通常被认为在短期内“可以容忍”。
  解决时间还受到[bug](../B/bug.md) 的**复杂性**和资源的**可用性**的影响。即使是高[severity](../S/severity.md) [bug](../B/bug.md)，如果需要进行大量调查或者在系统架构中根深蒂固，也可能需要更长的时间才能解决。此外，如果没有关键人员或必要的资源，尽管[severity](../S/severity.md)，解决方案可能会延迟。
  实际上，解决时间是[bug](../B/bug.md) 的[severity](../S/severity.md) 和开发过程的**实用性** 之间的平衡。虽然[severity](../S/severity.md) 推动更快的响应，但其他因素（例如资源分配、冲刺计划和解决方法的存在）可以调整解决问题所需的实际时间。

### 不同测试阶段的严重性

#### 单元测试中如何考虑严重性？

在 **[unit testing](../U/unit-testing.md)** 中，与其他测试阶段相比，[severity](../S/severity.md) 通常不太受重视，因为重点是单独验证应用程序的最小可测试部分。然而，当在单元级别识别出缺陷时，仍然可以根据其对被测单元功能的影响来考虑其[severity](../S/severity.md)。
  如果单元测试失败，则表明存在缺陷，范围可能从预期输出的微小差异到阻止单元执行其预期功能的严重故障。在这种情况下，[severity](../S/severity.md) 通常隐含地很高，因为单元测试旨在确保单个函数或方法的正确性，而这些函数或方法是应用程序的基本构建块。
  自动化单元测试旨在频繁运行并提供快速反馈，因此开发人员通常会在将代码集成到更大的系统之前**立即**解决任何故障。这一立即行动减少了对 [unit testing](../U/unit-testing.md) 级别的详细[severity](../S/severity.md) 分类的需要。
  但是，在某些情况下，如果单元测试失败是由于不妨碍整体功能的非关键方面造成的，或者是已取消优先级的已知问题，则 [severity](../S/severity.md) 可能会被认为较低，并且修复可能会被推迟。该决定通常是根据项目的优先级和时间表做出的。
  总之，虽然 [severity](../S/severity.md) 是测试后期阶段的关键概念，但在 [unit testing](../U/unit-testing.md) 中，任何导致测试失败的缺陷通常都会得到紧急处理，这反映了由于单元级代码的基础性质而隐含的高[severity](../S/severity.md)。

#### 集成测试中如何考虑严重性？

在[integration testing](../I/integration-testing.md) 中，**[severity](../S/severity.md)** 是识别、评估和解决集成组件或系统之间交互产生的缺陷时的关键因素。与[unit testing](../U/unit-testing.md) 不同，[unit testing](../U/unit-testing.md) 侧重于单个代码单元，[integration testing](../I/integration-testing.md) 评估集体操作，其中缺陷通常具有更广泛的影响。
  [Severity](../S/severity.md) 在这种情况下有助于衡量缺陷对系统功能、稳定性和性能的影响。高[severity](../S/severity.md) 问题（例如导致系统崩溃或数据损坏的问题）通常会在低[severity](../S/severity.md) 问题（例如不影响整体操作的微小 UI 差异）之前得到解决。
  [Test automation](../T/test-automation.md) 工程师使用[severity](../S/severity.md) 来确定缺陷修复的优先级，尤其是在时间限制或资源有限的情况下。自动[test suites](../T/test-suite.md)可被设计为立即标记高[severity](../S/severity.md)缺陷，触发警报以进行快速调查。这可以确保最关键的问题得到及时解决，从而降低重大故障进入测试或生产后期阶段的风险。
  在规划[test execution](../T/test-execution.md)时，覆盖关键集成路径的测试可能会更频繁地运行或使用更高的[priority](../P/priority.md)，特别是如果它们之前发现了高[severity](../S/severity.md)缺陷。在测试报告中，[severity](../S/severity.md) 提供了一个明确的指标，用于向利益相关者传达系统的健康状况，影响发布准备情况和资源分配的决策。
  总之，[integration testing](../I/integration-testing.md) 中的[severity](../S/severity.md) 是确定缺陷解决优先级、通知测试计划和沟通风险的关键指标，以确保最有影响力的问题得到有效解决。

#### 系统测试中如何考虑严重性？

在[system testing](../S/system-testing.md) 中，**[severity](../S/severity.md)** 是决定[bugs](../B/bug.md) 的处理顺序及其所需关注程度的关键因素。它与 [priority](../P/priority.md) 等其他因素一起考虑，但它特指缺陷对系统运行的影响。
  [Severity](../S/severity.md) 用于评估[bug](../B/bug.md) 可以**影响系统的功能、性能或稳定性**的程度。高[severity](../S/severity.md)问题（例如导致系统崩溃或数据丢失的问题）通常会在较低[severity](../S/severity.md)问题（例如不妨碍核心功能的小UI故障）之前得到解决。
  在[system testing](../S/system-testing.md)期间，[test cases](../T/test-case.md)可以根据它们旨在发现的缺陷的潜在[severity](../S/severity.md)进行加权或排序。 [Test automation](../T/test-automation.md) 工程师使用[severity](../S/severity.md) 来确定要运行哪些自动化测试以及何时运行的优先级，尤其是在时间或资源有限的情况下。例如，涵盖关键系统组件的测试可能会更频繁地运行或先于其他组件运行。
  当发现高[severity](../S/severity.md)缺陷时，它可以触发对受影响区域的**集中测试工作**，以确保相关功能不会受到损害。这可能涉及额外的自动回归测试或有针对性的[exploratory testing](../E/exploratory-testing.md)。
  在测试报告中，[severity](../S/severity.md) 是一个关键指标。它可以帮助利益相关者了解系统的健康状况并就发布准备情况做出明智的决策。报告通常包括 [severity](../S/severity.md) 分发，以强调突出缺陷的严重性，影响继续/不继续的决策。

#### 验收测试中如何考虑严重性？

在[acceptance testing](../A/acceptance-testing.md) 中，**[severity](../S/severity.md)** 是评估软件产品是否满足指定验收标准的关键因素。它指导有关产品发布准备情况的决策过程。高[severity](../S/severity.md) 问题通常表明可能**危害用户体验**或导致**系统故障**的根本问题，因此必须在产品被接受之前解决。
  验收测试旨在模拟现实世界的使用情况，并确保产品能够在现场环境中执行其预期功能。当遇到[bug](../B/bug.md)时，它的[severity](../S/severity.md)反映了它破坏这些关键功能的程度。 **对功能、安全性或性能**产生严重影响的 [Bugs](../B/bug.md) 通常被视为阻碍因素，必须在获得接受之前解决。
  在[acceptance testing](../A/acceptance-testing.md)期间，自动化工程师重点关注：

- **识别**
    和
    **记录**
    可能妨碍用户有效操作软件的严重错误。

- **评估**
    严重性以确定其是否属于该版本可接受的风险阈值。

- **优先考虑**
    解决严重错误，以确保产品在发布时稳定且功能齐全。
  [acceptance testing](../A/acceptance-testing.md) 中的[severity](../S/severity.md) 评估不仅是为了识别缺陷，也是为了确保产品提供**优质的用户体验**并满足**业务要求**。发现的任何严重问题都必须立即传达给利益相关者，以便就产品的发布准备情况做出明智的决策。

- **识别**
    和
    **记录**
    可能妨碍用户有效操作软件的严重错误。

- **评估**
    严重性以确定其是否属于该版本可接受的风险阈值。

- **优先考虑**
    解决严重错误，以确保产品在发布时稳定且功能齐全。

### 测试管理的严重性

#### 严重性如何影响测试用例设计？

[Severity](../S/severity.md) 通过规定测试工作的**焦点**和**深度**来影响[test case](../T/test-case.md) 设计。高[severity](../S/severity.md)区域通常需要**鲁棒**[test cases](../T/test-case.md)来覆盖广泛的场景，包括边缘情况和压力条件。这些领域的[Test cases](../T/test-case.md) 在设计时考虑到了**彻底性**，通常采用**[negative testing](../N/negative-testing.md)** 技术来确保系统可以处理无效输入或意外的用户行为。
  例如，如果某个功能与安全性或数据完整性相关，则其失败将被视为高[severity](../S/severity.md)。 [Test cases](../T/test-case.md) 此类功能将包括：

  ```
  // Pseudocode for a high-severity test case
  test('Sensitive data encryption', () => {
    const sensitiveData = 'user_password';
    const encryptedData = encrypt(sensitiveData);
    expect(encryptedData).not.toBe(sensitiveData);
    expect(isEncrypted(encryptedData)).toBe(true);
  });
  ```相比之下，较低[severity](../S/severity.md) 区域可能会使用更**直接**和**更简单**[test cases](../T/test-case.md) 进行测试，重点关注最常见和预期的[use cases](../U/use-case.md)。这些[test cases](../T/test-case.md)可能不会深入研究罕见场景或压力条件，因为故障的影响不太重要。
  [Test case](../T/test-case.md) 设计还考虑[bug](../B/bug.md) 与[severity](../S/severity.md) 一起发生的**可能性**。故障可能性高的高[severity](../S/severity.md)区域可能有**额外的[test cases](../T/test-case.md)**或**自动检查**以快速捕获潜在的回归。
  最终，[severity](../S/severity.md) 指导[test case](../T/test-case.md) 设计中的**资源分配**和**时间**，确保软件最关键的方面经过彻底测试且可靠。

#### 严重性如何影响测试执行计划？

[Severity](../S/severity.md) 通过指定执行[test cases](../T/test-case.md) 的**顺序**和**[priority](../P/priority.md)** 来影响[test execution](../T/test-execution.md) 规划。首先测试可能导致重大功能故障或数据丢失的高[severity](../S/severity.md) 问题，以确保软件最关键的方面稳定。这种方法有助于在测试周期的早期识别和解决最具破坏性的缺陷。
  [Test cases](../T/test-case.md) 覆盖具有已知高[severity](../S/severity.md) 问题的应用程序区域，可以**优先**并更频繁地执行（例如在[regression testing](../R/regression-testing.md) 中），以确认这些问题已得到解决并且没有再次出现。相反，[severity](../S/severity.md) 问题较低的区域可能测试频率较低或紧迫性较低。
  在[automated testing](../A/automated-testing.md) 中，[test suites](../T/test-suite.md) 可以组织运行高[severity](../S/severity.md) [test cases](../T/test-case.md) 作为**冒烟测试**或**健全性测试**套件的一部分，以快速评估构建的运行状况。这确保任何构建或发布候选版本都满足进一步测试或部署的最低标准。
  此外，在规划[test execution](../T/test-execution.md)时，为高[severity](../S/severity.md)[test scenarios](../T/test-scenario.md)分配适当的**资源**和**时间**至关重要。这可能涉及建立更强大的测试环境或投入更多时间用于[test execution](../T/test-execution.md)和分析。
  总之，[severity](../S/severity.md) 将[test execution](../T/test-execution.md) 的重点引导到应用程序最关键的领域，确保最具影响力的问题得到及时解决，从而优化测试工作并提高软件的整体质量。

#### 严重性如何影响测试报告？

[Severity](../S/severity.md) 通过指导缺陷的**沟通**​​和**管理**来影响测试报告。在报告测试结果时，[severity](../S/severity.md) 会明确指示 [bug](../B/bug.md) 对系统功能的**影响**。 [Test reports](../T/test-report.md) 通常包括每个缺陷的 **[severity](../S/severity.md) 评级**，以帮助利益相关者了解潜在风险和修复的紧迫性。
  在自动化测试报告中，[severity](../S/severity.md) 评级可以向适当的团队成员触发**警报**和**通知**。例如，高[severity](../S/severity.md) [bug](../B/bug.md) 可能会自动通知产品经理或首席开发人员，促使立即采取行动。这可确保关键问题得到及时解决，从而降低发布时出现重大问题的风险。
  此外，[severity](../S/severity.md) 可以影响报告缺陷的**排序**。 [Test reports](../T/test-report.md) 可能会被排序，以在顶部显示最严重的 [bugs](../B/bug.md)，确保它们首先受到关注。这有助于根据对产品的潜在影响确定缺陷解决工作的优先级。
  此外，[test reports](../T/test-report.md) 中的[severity](../S/severity.md) 评级可用于生成一段时间内的**指标**和**趋势**，从而提供对软件质量的深入了解。高[severity](../S/severity.md) [bugs](../B/bug.md) 趋势下降可能表明[software quality](../S/software-quality.md) 有所改进，而上升趋势可能表明需要进行工艺或设计更改。
  总之，测试报告中的[severity](../S/severity.md)：

- 传达缺陷的影响。
  - 触发警报以立即采取行动。
  - 优先考虑报告中的错误。
  - 生成质量指标和趋势。
  通过在测试报告中有效利用[severity](../S/severity.md)，团队可以确保突出和解决关键问题，从而专注于交付高质量的软件。

- 传达缺陷的影响。
  - 触发警报以立即采取行动。
  - 优先考虑报告中的错误。
  - 生成质量指标和趋势。
