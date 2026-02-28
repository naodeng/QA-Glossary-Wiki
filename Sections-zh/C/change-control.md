# 变更控制

<!-- TOC START -->
- [相关术语：](#相关术语：)
- [有关变更控制的问题吗？](#有关变更控制的问题吗？)
  - [基础知识和重要性](#基础知识和重要性)
    - [软件开发中的变更控制是什么？](#软件开发中的变更控制是什么？)
    - [为什么变更控制在软件开发中很重要？](#为什么变更控制在软件开发中很重要？)
    - [变更控制流程的关键组成部分是什么？](#变更控制流程的关键组成部分是什么？)
    - [变更控制如何提高软件产品的整体质量？](#变更控制如何提高软件产品的整体质量？)
  - [变更控制流程](#变更控制流程)
    - [典型的变更控制流程涉及哪些步骤？](#典型的变更控制流程涉及哪些步骤？)
    - [变更请求如何发起以及谁可以发起？](#变更请求如何发起以及谁可以发起？)
    - [变更控制委员会的作用是什么？](#变更控制委员会的作用是什么？)
    - [变更请求如何评估和批准？](#变更请求如何评估和批准？)
    - [实施变更控制流程时常见的挑战是什么以及如何缓解这些挑战？](#实施变更控制流程时常见的挑战是什么以及如何缓解这些挑战？)
  - [变更控制工具和技术](#变更控制工具和技术)
    - [软件开发中通常使用哪些工具来管理变更控制？](#软件开发中通常使用哪些工具来管理变更控制？)
    - [自动化如何应用于变更控制？](#自动化如何应用于变更控制？)
    - [在变更控制系统中记录变更的最佳实践是什么？](#在变更控制系统中记录变更的最佳实践是什么？)
    - [变更控制如何与版本控制和持续集成等其他软件开发流程集成？](#变更控制如何与版本控制和持续集成等其他软件开发流程集成？)
  - [变更控制和测试](#变更控制和测试)
    - [变更控制如何影响软件测试？](#变更控制如何影响软件测试？)
    - [什么是回归测试以及它与变更控制有何关系？](#什么是回归测试以及它与变更控制有何关系？)
    - [变更控制如何帮助管理测试环境？](#变更控制如何帮助管理测试环境？)
    - [变更控制如何有助于测试自动化？](#变更控制如何有助于测试自动化？)
<!-- TOC END -->

变更控制

，在上下文中

软件测试

，是指用于确保以受控和协调的方式对软件产品或系统进行修改或更新的正式过程。它涉及记录、评估、批准和监督开发过程期间和之后对软件、其环境或相关文档所做的任何更改。

## 相关术语：

- [Change Requests](../C/change-requests.md)

## 有关变更控制的问题吗？

### 基础知识和重要性

#### 软件开发中的变更控制是什么？

软件开发中的[Change control](../C/change-control.md) 是一个正式流程，用于确保以受控和协调的方式引入产品变更。它涉及对软件变更的跟踪、评估、批准和实施。此过程对于维护软件的完整性并确保修改不会损害其质量或功能至关重要。
  提出变更后，会记录在**变更请求** (CR) 中并提交进行分析。 CR 包括变更的理由、对系统的影响以及所需的资源等详细信息。 **[Change Control](../C/change-control.md) 委员会** (CCB) 通常由利益相关者和团队负责人组成，负责审查 CR 以决定其实施。
  评估考虑风险、成本和收益等因素。批准的变更将被安排并分配给相关的团队成员。 **版本控制系统**通常用于管理代码库中的更改，而**自动化工具**简化流程、跟踪更改并维护记录。
  [Change control](../C/change-control.md) 与 **[regression testing](../R/regression-testing.md)** 紧密集成，以确保新的更改不会对现有功能产生不利影响。自动回归测试作为[change control](../C/change-control.md) 流程的一部分被触发，以验证软件在修改后是否继续按预期运行。
  在[test automation](../T/test-automation.md) 中，[change control](../C/change-control.md) 帮助管理[test scripts](../T/test-script.md) 的更新，确保它们与最新的软件更改保持一致。它还通过控制何时以及如何应用更新，在维护 [test environments](../T/test-environment.md) 的稳定性和可靠性方面发挥着至关重要的作用。

#### 为什么变更控制在软件开发中很重要？

[Change control](../C/change-control.md) 在软件开发中对于在引入更改时保持**稳定性**和**可预测性**至关重要。它确保修改不会对现有功能产生不利影响或引入新的缺陷。通过系统地管理变更，团队可以避免**范围蔓延**，即不受控制的变更导致项目延迟和预算超支。
  有效的[change control](../C/change-control.md) 允许**可追溯性**，将更改与其源需求或问题联系起来，这对于[impact analysis](../I/impact-analysis.md) 和问责制至关重要。它还支持**遵守**行业标准和法规，这些标准和法规可能需要记录的流程来管理变更。
  在 [test automation](../T/test-automation.md) 上下文中，[change control](../C/change-control.md) 对于保持 [test scripts](../T/test-script.md) 和框架与应用程序的当前状态保持一致至关重要。它有助于确定何时何地需要更新测试，从而降低 [false positives](../F/false-positive.md) 或自动化测试结果中出现负面结果的风险。
  此外，[change control](../C/change-control.md) 通过提供清晰的沟通渠道来讨论和决定提议的变更，促进开发人员、测试人员和其他利益相关者之间的**协作**。这种协作对于确保 [test automation](../T/test-automation.md) 策略保持有效以及自动化测试继续在验证应用程序行为方面提供价值至关重要。
  最后，[change control](../C/change-control.md) 有助于**持续改进**。通过分析变更历史和结果，团队可以识别流程增强的模式和领域，从而实现更高效的开发和测试周期。

#### 变更控制流程的关键组成部分是什么？

[change control](../C/change-control.md) 流程的关键组件包括：

- **变更识别**：明确定义变更的构成。
  - **更改[Impact Analysis](../I/impact-analysis.md)**：评估更改对项目的潜在影响。
  - **更改优先级**：根据紧急程度、重要性和资源进行排名更改。
  - **批准机制**：为谁可以批准变更建立明确的协议。
  - **变更实施计划**：制定执行变更的详细计划。
  - **沟通计划**：确保所有利益相关者都了解变更及其影响。
  - **监控和报告**：跟踪变更进度并报告其状态。
  - **反馈循环**：创建一种在实施后收集反馈的方法，以从每次更改中学习。
  - **文档**：更新所有相关文档以反映更改。
  - **审计和审查**：定期审查变更流程的合规性和有效性。
  将这些组件集成到您的[change control](../C/change-control.md) 流程中将有助于保持软件产品的稳定性和质量，同时适应必要的更改。

- **变更识别**：明确定义变更的构成。
  - **更改[Impact Analysis](../I/impact-analysis.md)**：评估更改对项目的潜在影响。
  - **更改优先级**：根据紧急程度、重要性和资源进行排名更改。
  - **批准机制**：为谁可以批准变更建立明确的协议。
  - **变更实施计划**：制定执行变更的详细计划。
  - **沟通计划**：确保所有利益相关者都了解变更及其影响。
  - **监控和报告**：跟踪变更进度并报告其状态。
  - **反馈循环**：创建一种在实施后收集反馈的方法，以从每次更改中学习。
  - **文档**：更新所有相关文档以反映更改。
  - **审计和审查**：定期审查变更流程的合规性和有效性。

#### 变更控制如何提高软件产品的整体质量？

[Change control](../C/change-control.md) 确保对软件的任何修改都得到系统管理，从而降低引入缺陷或不一致的风险。通过维护变更的**清晰记录**，测试人员可以快速识别应用程序的哪些区域可能受到影响并需要[retesting](../R/retesting.md)。这对于 **[regression testing](../R/regression-testing.md)** 至关重要，因为需要在不影响现有功能的情况下验证更改。
  对于[test automation](../T/test-automation.md)，[change control](../C/change-control.md) 为[test scripts](../T/test-script.md) 提供了**稳定的参考**。自动化测试通常需要更新以适应最新的应用程序更改。有了详细记录的变更历史记录，自动化工程师可以有效地更新或创建新的测试来覆盖变更。
  此外，[change control](../C/change-control.md) 促进了需求、代码更改和[test cases](../T/test-case.md) 之间的**可追溯性**。这种可追溯性确保自动化测试保持相关性并专注于当前需求，从而增强[test coverage](../T/test-coverage.md)和[quality assurance](../Q/quality-assurance.md)。
  在具有 **持续集成** (CI) 和 **持续部署** (CD) 的环境中，[change control](../C/change-control.md) 有助于管理构建和部署管道中的更改流。自动化测试可以由 [change control](../C/change-control.md) 事件触发，确保更改在合并或发布之前由 [test suite](../T/test-suite.md) 进行验证。
  最后，[change control](../C/change-control.md) 允许团队根据变更的影响确定测试工作的优先级，从而有助于**风险管理**。高风险变更可以触发更广泛的自动化测试运行，而低风险变更可能只需要有针对性的测试子集，从而优化测试资源的使用。

### 变更控制流程

#### 典型的变更控制流程涉及哪些步骤？

[change control](../C/change-control.md) 进程中的典型步骤如下：

1. **识别**：识别出可能影响软件或其测试的更改。这可能是 [bug](../B/bug.md) 修复、功能增强或需求更改。
  2. **文档**：变更记录在**变更请求**表格中，详细说明范围、影响、理由和任何其他相关信息。
  3. **分析**：分析变更对项目的影响，包括风险、收益和资源需求。
  4. **审查**：变更请求由相关利益相关者审查，通常包括 **[Change Control](../C/change-control.md) 委员会 (CCB)**，以确保其与项目目标和优先级保持一致。
  5. **批准或拒绝**：根据审核，更改将被批准、拒绝或发回以获取更多信息。
  6. **规划**：如果获得批准，将创建实施变更的详细计划。这包括调度、资源分配和定义验收标准。
  7. **实施**：变更按照计划实施。这可能涉及代码更改、配置更新或其他修改。
  8. **测试**：进行严格的测试，包括**[regression testing](../R/regression-testing.md)**，以确保更改不会对现有功能产生不利影响。
  9. **文档更新**：更新所有相关文档以反映更改，包括[test cases](../T/test-case.md) 和用户手册。
  10. **发布**：变更在测试和审核成功后发布到生产环境。
  11. **监控**：实施后，对变更进行监控，以确保其按预期执行并且不会引入新问题。
  12. **关闭**：一旦确认变更稳定有效，变更请求就正式关闭。
  1. **识别**：识别出可能影响软件或其测试的更改。这可能是[bug](../B/bug.md) 修复、功能增强或需求更改。
  2. **文档**：变更记录在**变更请求**表格中，详细说明范围、影响、理由和任何其他相关信息。
  3. **分析**：分析变更对项目的影响，包括风险、收益和资源需求。
  4. **审查**：变更请求由相关利益相关者审查，通常包括 **[Change Control](../C/change-control.md) 委员会 (CCB)**，以确保其与项目目标和优先级保持一致。
  5. **批准或拒绝**：根据审核，更改将被批准、拒绝或发回以获取更多信息。
  6. **规划**：如果获得批准，将创建实施变更的详细计划。这包括调度、资源分配和定义验收标准。
  7. **实施**：变更按照计划实施。这可能涉及代码更改、配置更新或其他修改。
  8. **测试**：进行严格的测试，包括**[regression testing](../R/regression-testing.md)**，以确保更改不会对现有功能产生不利影响。
  9. **文档更新**：更新所有相关文档以反映更改，包括[test cases](../T/test-case.md) 和用户手册。
  10. **发布**：变更在测试和审核成功后发布到生产环境。
  11. **监控**：实施后，对变更进行监控，以确保其按预期执行并且不会引入新问题。
  12. **关闭**：一旦确认变更稳定有效，变更请求就正式关闭。

#### 变更请求如何发起以及谁可以发起？

变更请求可以由软件开发过程中的**任何利益相关者**发起，包括开发人员、测试人员、项目经理或业务分析师。发起者确定由于缺陷、增强或需求变更而需要进行修改，并通过 **[change control](../C/change-control.md) 系统**或工具提交正式请求。
  要发起变更请求，涉众通常会填写**变更请求表**或在项目管理或问题跟踪系统中创建票证。该表格应包括：

- 清晰
    **描述**
    的变化

- 的
    **原因**
    为了改变

- 的
    **影响**
    在当前系统上

- 的
    **紧急**
    和
    **[priority](../P/priority.md)**
    的变化
  提交后，变更请求将由 **[Change Control](../C/change-control.md) 委员会 (CCB)** 或指定机构进行审核，以进行评估和批准。 CCB 可能会要求提供更多信息或澄清，以评估变更对项目范围、时间表和资源的影响。
  在[test automation](../T/test-automation.md)的上下文中，[change requests](../C/change-requests.md)可以导致[test scripts](../T/test-script.md)、[test data](../T/test-data.md)和自动化框架的更新，以适应新的或修改的要求。对于 [test automation](../T/test-automation.md) 工程师来说，仔细跟踪这些变化以确保自动化测试的连续性和有效性至关重要。

- 清晰
    **描述**
    的变化

- 的
    **原因**
    为了改变

- 的
    **影响**
    在当前系统上

- 的
    **紧急**
    和
    **[priority](../P/priority.md)**
    的变化

#### 变更控制委员会的作用是什么？

**[Change Control](../C/change-control.md) 委员会 (CCB)** 是一组利益相关者，负责审查、评估以及批准或拒绝[change requests](../C/change-requests.md)。在[test automation](../T/test-automation.md) 的背景下，CCB 在确保自动化测试或测试框架的更改与项目目标保持一致并且不会引入不必要的风险方面发挥着关键作用。
  成员通常包括来自开发、测试、运营和业务部门的代表，确保对拟议变更的影响有不同的看法。 CCB 的作用包括：

- **评估影响**
    对现有测试自动化套件的更改。

- **优先考虑**
    根据风险、紧急程度和资源可用性等因素更改请求。

- **做出决定**
    是否实施、推迟或拒绝变更。

- **确保合规性**
    具有既定的标准和程序。

- **沟通决定**
    相关利益相关者，确保透明度。
  对于[test automation](../T/test-automation.md) 工程师，CCB 提供了一种结构化方法来管理可能影响[automated testing](../A/automated-testing.md) 结果的变更。通过与 CCB 合作，工程师确保他们对可测试性和自动化的担忧和见解在 [change control](../C/change-control.md) 流程中得到考虑。这种合作有助于在整个软件开发生命周期中保持 [test automation](../T/test-automation.md) 策略的完整性和有效性。

- **评估影响**
    对现有测试自动化套件的更改。

- **优先考虑**
    根据风险、紧急程度和资源可用性等因素更改请求。

- **做出决定**
    是否实施、推迟或拒绝变更。

- **确保合规性**
    具有既定的标准和程序。

- **沟通决定**
    相关利益相关者，确保透明度。

#### 变更请求如何评估和批准？

[Change requests](../C/change-requests.md) 根据其**影响**、**紧迫性**和**可行性**进行评估。评估过程通常包括以下步骤：

1. **初步审查**：团队成员（通常是领导或经理）进行初步评估，以确保请求完整且易于理解。
  2. **[Impact Analysis](../I/impact-analysis.md)**：团队分析变更将如何影响现有功能、系统性能和其他项目组件。这包括评估引入新缺陷的可能性。
  3. **资源估算**：估算实施变更所需的工作量，包括时间、人员和成本。
  4. **风险评估**：识别和评估与变更相关的风险，例如延迟或技术挑战。
  5. **批准流程**：变更请求提交给 **[Change Control](../C/change-control.md) 委员会 (CCB)** 或同等机构，由其审核分析并决定是否批准、拒绝或请求更多信息。
  6. **利益相关者咨询**：可以咨询主要利益相关者的意见，特别是当变更具有重大业务影响时。
  7. **决策沟通**：一旦做出决定，就会传达给相关方，并在[change control](../C/change-control.md)系统中更新变更请求。
  批准标准通常包括与项目目标的一致性、法规遵从性以及在不造成不当干扰的情况下增强产品的能力。批准的变更将被优先考虑并安排实施，而被拒绝的变更则被记录并附上原因以供将来参考。

1. **初步审查**：团队成员（通常是领导或经理）进行初步评估，以确保请求完整且易于理解。
  2. **[Impact Analysis](../I/impact-analysis.md)**：团队分析变更将如何影响现有功能、系统性能和其他项目组件。这包括评估引入新缺陷的可能性。
  3. **资源估算**：估算实施变更所需的工作量，包括时间、人员和成本。
  4. **风险评估**：识别和评估与变更相关的风险，例如延迟或技术挑战。
  5. **批准流程**：变更请求提交给 **[Change Control](../C/change-control.md) 委员会 (CCB)** 或同等机构，由其审核分析并决定是否批准、拒绝或请求更多信息。
  6. **利益相关者咨询**：可以咨询主要利益相关者的意见，特别是当变更具有重大业务影响时。
  7. **决策沟通**：一旦做出决定，就会传达给相关方，并在[change control](../C/change-control.md)系统中更新变更请求。

#### 实施变更控制流程时常见的挑战是什么以及如何缓解这些挑战？

实施 **[change control](../C/change-control.md) 流程** 可能面临多项挑战，包括：

- **抵制变革**：团队成员可能习惯于非正式流程并抵制结构化[change control](../C/change-control.md)。 **缓解**：培养持续改进的文化，并通过培训和清晰的沟通展示结构化流程的好处。
  - **官僚主义**：过于复杂的流程会减慢开发速度。 **缓解**：简化流程，仅包含必要的步骤，并在可能的情况下实现自动化。
  - **沟通不畅**：沟通不充分可能会导致误解和延误。 **缓解**：使用有助于清晰及时沟通的工具，并确保所有利益相关者随时了解情况。
  - **缺乏问责制**：如果没有明确的职责，变革可能无法得到妥善管理。 **缓解**：在[change control](../C/change-control.md) 流程中分配特定的角色和职责。
  - **工具不足**：不适合团队工作流程的工具可能会阻碍流程。 **缓解**：选择与现有系统集成良好且用户友好的工具。
  - **范围蔓延**：不受控制的更改可能会导致范围蔓延。 **缓解**：确保所有变更都得到正确记录并根据项目目标进行评估。
  - **测试不充分**：更改可能没有经过彻底测试，从而导致缺陷。 **缓解**：将[change control](../C/change-control.md) 与[automated testing](../A/automated-testing.md) 集成，以确保每个更改在部署前都经过测试。
  通过采用有针对性的策略应对这些挑战，可以更有效地实施[change control](../C/change-control.md)流程，从而改善[software quality](../S/software-quality.md)和项目成果。

- **抵制变革**：团队成员可能习惯于非正式流程并抵制结构化[change control](../C/change-control.md)。 **缓解**：培养持续改进的文化，并通过培训和清晰的沟通展示结构化流程的好处。
  - **官僚主义**：过于复杂的流程会减慢开发速度。 **缓解**：简化流程，仅包含必要的步骤，并在可能的情况下实现自动化。
  - **沟通不畅**：沟通不充分可能会导致误解和延误。 **缓解**：使用有助于清晰及时沟通的工具，并确保所有利益相关者随时了解情况。
  - **缺乏问责制**：如果没有明确的职责，变革可能无法得到妥善管理。 **缓解**：在[change control](../C/change-control.md) 流程中分配特定的角色和职责。
  - **工具不足**：不适合团队工作流程的工具可能会阻碍流程。 **缓解**：选择与现有系统集成良好且用户友好的工具。
  - **范围蔓延**：不受控制的更改可能会导致范围蔓延。 **缓解**：确保所有变更都得到正确记录并根据项目目标进行评估。
  - **测试不充分**：更改可能没有经过彻底测试，从而导致缺陷。 **缓解**：将 [change control](../C/change-control.md) 与 [automated testing](../A/automated-testing.md) 集成，以确保在部署之前测试每个更改。

### 变更控制工具和技术

#### 软件开发中通常使用哪些工具来管理变更控制？

在软件开发中管理[change control](../C/change-control.md)的常用工具包括：

- **版本控制系统 (VCS)**
    比如
    **吉特**
    ,
    **颠覆（SVN）**
    , 和
    **水星**
    。这些系统跟踪代码更改并允许分支和合并，从而促进协作工作和更改跟踪。

  ```
  git commit -m "Implement feature X"
  ```

- **问题跟踪系统**
    喜欢
    **[JIRA](../J/jira.md)**
    ,
    **虫虫**
    , 和
    **红矿**
    通过跟踪错误、功能请求和任务来帮助管理变更请求。

  ```
  // Example JIRA API call to create an issue
  const issue = {
    fields: {
      project: { key: "TEST" },
      summary: "Implement change control",
      description: "Details of the change...",
      issuetype: { name: "Task" }
    }
  };
  ```

- **代码审查工具**
    比如
    **格里特**
    ,
    **GitHub 拉取请求**
    , 和
    **GitLab 合并请求**
    确保更改在合并到主代码库之前经过审查和批准。

  ```
  // Example GitHub API call to create a pull request
  const pullRequest = {
    title: "Feature X Implementation",
    head: "feature-branch",
    base: "main",
    body: "Please review the changes for Feature X."
  };
  ```

- **持续集成/持续部署 (CI/CD) 平台**
    喜欢
    **詹金斯**
    ,
    **特拉维斯·CI**
    ,
    **圆CI**
    , 和
    **亚搏体育appGitLab CI/CD**
    自动执行变更的测试和部署，确保它们符合质量标准。

  ```
  pipeline {
    agent any
    stages {
      stage('Build') {
        steps {
          sh 'make'
        }
      }
      stage('Test') {
        steps {
          sh 'make test'
        }
      }
      stage('Deploy') {
        steps {
          sh 'make deploy'
        }
      }
    }
  }
  ```

- **配置管理工具**
    比如
    **安塞布尔**
    ,
    **厨师**
    ,
    **傀儡**
    , 和
    **地形**
    管理基础架构变更并确保环境一致。

  ```
  resource "aws_instance" "example" {
    ami           = "ami-0c55b159cbfafe1f0"
    instance_type = "t2.micro"
  }
  ```这些工具集成后，可以提供一个强大的框架来系统、高效地管理变更。

- **版本控制系统 (VCS)**
    比如
    **吉特**
    ,
    **颠覆（SVN）**
    , 和
    **水星**
    。这些系统跟踪代码更改并允许分支和合并，从而促进协作工作和更改跟踪。

- **问题跟踪系统**
    喜欢
    **[JIRA](../J/jira.md)**
    ,
    **虫虫**
    , 和
    **红矿**
    通过跟踪错误、功能请求和任务来帮助管理变更请求。

- **代码审查工具**
    比如
    **格里特**
    ,
    **GitHub 拉取请求**
    , 和
    **GitLab 合并请求**
    确保更改在合并到主代码库之前经过审查和批准。

- **持续集成/持续部署 (CI/CD) 平台**
    喜欢
    **詹金斯**
    ,
    **特拉维斯·CI**
    ,
    **圆CI**
    , 和
    **亚搏体育appGitLab CI/CD**
    自动执行变更的测试和部署，确保它们符合质量标准。

- **配置管理工具**
    比如
    **安塞布尔**
    ,
    **厨师**
    ,
    **傀儡**
    , 和
    **地形**
    管理基础架构变更并确保环境一致。

#### 自动化如何应用于变更控制？

自动化可以通过以下方式简化 **[change control](../C/change-control.md)** 流程：

- **自动化跟踪**
    变更请求，确保每个变更都被记录、分类并确定优先级，无需人工干预。

- **触发自动化测试**
    当提交更改时。这可以通过版本控制系统中的挂钩来完成，该挂钩启动一套相关的自动化回归测试。

- **自动化部署**
    不同环境的更改，从而实现一致且可重复的测试场景。

- **自动化报告**
    测试结果，可以直接链接到变更请求，提供有关变更影响的即时反馈。

- **强制合规**
    通过使用在允许更改继续之前检查必要的批准或文档的脚本来制定更改控制策略。

- **自动回滚过程**
    如果更改在测试期间失败，确保系统保持稳定和可用。
  例如，在持续集成[setup](../S/setup.md)中：

  ```
  on: push
  jobs:
    test:
      runs-on: ubuntu-latest
      steps:
      - uses: actions/checkout@v2
      - name: Run regression tests
        run: ./run-tests.sh
  ```每当代码被推送到存储库时，此脚本都会触发自动回归测试，有助于确保更改不会破坏现有功能。
  通过将自动化集成到[change control](../C/change-control.md)，[test automation](../T/test-automation.md) 工程师可以减少手动开销、加快变更管理流程并增强软件版本的可靠性。

- **自动化跟踪**
    变更请求，确保每个变更都被记录、分类并确定优先级，无需人工干预。

- **触发自动化测试**
    当提交更改时。这可以通过版本控制系统中的挂钩来完成，该挂钩启动一套相关的自动化回归测试。

- **自动化部署**
    不同环境的更改，从而实现一致且可重复的测试场景。

- **自动化报告**
    测试结果，可以直接链接到变更请求，提供有关变更影响的即时反馈。

- **强制合规**
    通过使用在允许更改继续之前检查必要的批准或文档的脚本来制定更改控制策略。

- **自动回滚过程**
    如果更改在测试期间失败，确保系统保持稳定和可用。

#### 在变更控制系统中记录变更的最佳实践是什么？

记录 [change control](../C/change-control.md) 系统中的更改的最佳实践包括：

- **具体而清晰**：清楚地描述变更，包括**范围**、**影响**和**理由**。避免含糊不清，以确保每个人都理解更改。
  - **使用标准化格式**：为[change requests](../C/change-requests.md)采用一致的模板，以便更轻松地查看和理解更改。
  - **包括必要的详细信息**：记录相关信息，例如**更改 ID**、**作者**、**日期**、**相关文档**和**受影响的组件**。
  - **维护更改日志**：保留所有更改（包括次要更新）的时间顺序日志，以提供全面的历史记录。
  - **将更改链接到[Test Cases](../T/test-case.md)**：将更改与特定[test cases](../T/test-case.md) 或场景关联，以促进可追溯性和[regression testing](../R/regression-testing.md)。
  - **版本控制**：使用版本控制系统跟踪文档更改，并使用引用更改请求 ID 的提交消息。
  - **审查和批准**：记录审查过程，包括批准变更的人员和时间，以保持问责制。
  - **传达变更**：将已批准的变更通知所有利益相关者，确保团队了解并能够相应地进行调整。
  - **存档旧文档**：保留旧版本的文档以供审核之用，但要清楚地将它们与当前版本区分开来。
  - **持续改进**：根据反馈和经验教训定期审查和完善文档流程。
  记录代码块中的更改的示例：

  ```
  // Change ID: 1234
  // Author: Jane Doe
  // Date: 2023-04-01
  // Description: Refactor login function to improve performance
  // Impact: Improves login speed by 50%
  // Rationale: User feedback indicated login delays
  // Affected Components: AuthModule, LoginService
  // Related Documents: AuthModuleSpec.md, PerformanceReport.pdf
  // Approved by: John Smith, 2023-04-02
  function optimizedLogin(userCredentials) {
    // Optimized code here
  }
  ```

- **具体而清晰**：清楚地描述变更，包括**范围**、**影响**和**理由**。避免含糊不清，以确保每个人都理解更改。
  - **使用标准化格式**：为[change requests](../C/change-requests.md)采用一致的模板，以便更轻松地查看和理解更改。
  - **包括必要的详细信息**：记录相关信息，例如**更改 ID**、**作者**、**日期**、**相关文档**和**受影响的组件**。
  - **维护更改日志**：保留所有更改（包括次要更新）的时间顺序日志，以提供全面的历史记录。
  - **将更改链接到[Test Cases](../T/test-case.md)**：将更改与特定[test cases](../T/test-case.md) 或场景相关联，以促进可追溯性和[regression testing](../R/regression-testing.md)。
  - **版本控制**：使用版本控制系统跟踪文档更改，并使用引用更改请求 ID 的提交消息。
  - **审查和批准**：记录审查过程，包括批准变更的人员和时间，以保持问责制。
  - **传达变更**：将已批准的变更通知所有利益相关者，确保团队了解并能够相应地进行调整。
  - **存档旧文档**：保留旧版本的文档以供审核之用，但要清楚地将它们与当前版本区分开来。
  - **持续改进**：根据反馈和经验教训定期审查和完善文档流程。

#### 变更控制如何与版本控制和持续集成等其他软件开发流程集成？

将 [change control](../C/change-control.md) 与 **版本控制** 和 **持续集成 (CI)** 集成可确保系统地管理更改并与代码库和自动构建流程保持一致。以下是它们的集成方式：

- **版本控制集成**：当更改请求被批准时，相关的代码更改应提交到版本控制系统，并引用更改请求 ID。这会在更改和代码之间创建可跟踪的链接，从而在必要时更容易进行审核和回滚。

    ```
    git commit -m "CR123: Adjust login timeout for better user experience"
    ```

- **分支策略**：使用功能或发布分支来隔离更改，直到它们准备好合并到主分支中。这可以保持主分支稳定并允许并行开发。

    ```
    git checkout -b feature/CR123-adjust-login-timeout
    ```

- **CI 集成**：配置 CI 管道以在代码提交时触发自动构建和测试。这可确保立即测试更改，并提供有关其影响的快速反馈。

    ```
    on:
      push:
        branches:
          - 'feature/*'
    jobs:
      build:
        runs-on: ubuntu-latest
        steps:
        - uses: actions/checkout@v2
        - name: Run tests
          run: make test
    ```

- **自动化部署**：如果自动化测试通过，CI 系统可以将更改部署到暂存环境以进行进一步测试，确保只有经过验证的更改才能部署到生产环境。
  - **监控和反馈**：部署后，监控应用程序是否存在问题，并将此信息反馈到 [change control](../C/change-control.md) 流程中，以通知未来的更改。
  通过将 [change control](../C/change-control.md) 与版本控制和 CI 集成，您可以创建一个**有凝聚力的生态系统**，在该生态系统中透明地进行更改、严格测试并可靠地部署，从而有助于提高软件的稳定性和质量。

- **版本控制集成**：当更改请求被批准时，相关的代码更改应提交到版本控制系统，并引用更改请求 ID。这会在更改和代码之间创建可跟踪的链接，从而在必要时更容易进行审核和回滚。

    ```
    git commit -m "CR123: Adjust login timeout for better user experience"
    ```

- **分支策略**：使用功能或发布分支来隔离更改，直到它们准备好合并到主分支中。这可以保持主分支稳定并允许并行开发。

    ```
    git checkout -b feature/CR123-adjust-login-timeout
    ```

- **CI 集成**：配置 CI 管道以在代码提交时触发自动构建和测试。这可确保立即测试更改，并提供有关其影响的快速反馈。

    ```
    on:
      push:
        branches:
          - 'feature/*'
    jobs:
      build:
        runs-on: ubuntu-latest
        steps:
        - uses: actions/checkout@v2
        - name: Run tests
          run: make test
    ```

- **自动化部署**：如果自动化测试通过，CI 系统可以将更改部署到暂存环境以进行进一步测试，确保只有经过验证的更改才能部署到生产环境。
  - **监控和反馈**：部署后，监控应用程序是否存在问题，并将此信息反馈到 [change control](../C/change-control.md) 流程中，以通知未来的更改。

### 变更控制和测试

#### 变更控制如何影响软件测试？

[Change control](../C/change-control.md) 显着影响[software testing](../S/software-testing.md)，需要**[test case](../T/test-case.md) 调整**和**[regression testing](../R/regression-testing.md)**。当引入更改时，必须**更新**自动化测试以适应新的需求或功能。这确保了测试在验证应用程序的行为时保持相关性和有效性。
  必须对自动化[test suites](../T/test-suite.md)进行**审查**和**完善**以适应变化，这可能涉及修改现有测试或创建新测试。此过程需要深入了解变更的范围及其对应用程序的潜在影响。
  此外，[change control](../C/change-control.md) 经常触发 **[regression testing](../R/regression-testing.md)** 以确保新的更改不会对现有功能产生不利影响。自动化回归测试在这里至关重要，因为它们可以在更改后快速验证应用程序的稳定性。
  [change control](../C/change-control.md) 与[test automation](../T/test-automation.md) 的有效集成涉及[test scripts](../T/test-script.md) 的**版本控制**，其中每个版本对应于应用程序的特定状态。这种做法允许测试人员在必要时恢复到早期版本并维护更改历史记录。
  此外，[change control](../C/change-control.md) 可能会影响 **[test environment](../T/test-environment.md) 管理**，因为更改可能需要不同的配置或数据集进行测试。自动化测试必须适应这些环境变化以保持其有效性。
  总之，[change control](../C/change-control.md) 直接影响[test automation](../T/test-automation.md)，因为要求[test scripts](../T/test-script.md) 持续**维护**和**适应**，推动了彻底**[regression testing](../R/regression-testing.md)** 的需求，并确保自动化测试始终与软件的当前状态**一致**。

#### 什么是回归测试以及它与变更控制有何关系？

[Regression testing](../R/regression-testing.md) 是[software testing](../S/software-testing.md) 的一种类型，用于验证先前开发和测试的软件在更改或与其他软件交互后是否仍能正常运行。更改可能包括软件增强、补丁、配置更改，甚至环境更改。
  在 [change control](../C/change-control.md) 的上下文中，[regression testing](../R/regression-testing.md) 至关重要，因为它确保新的代码更改不会对产品的现有功能产生不利影响。 [Change control](../C/change-control.md) 流程通常包括必须执行回归测试以验证更改影响的步骤。这在实施持续集成和持续部署 (CI/CD) 的环境中尤其重要，因为更改经常集成到主分支中，并且不得中断软件的运行。
  自动化 [regression testing](../R/regression-testing.md) 通常集成到 CI/CD 管道中。当变更请求被批准并实施时，可以自动触发相应的回归测试。这提供了有关更改影响的即时反馈，并有助于维护[software quality](../S/software-quality.md)。
  以下是如何使用伪代码在 CI/CD 管道中触发回归测试的示例：

  ```
  pipeline:
    trigger:
      - on: push
        branches:
          - main
    jobs:
      - name: Run Regression Tests
        script:
          - execute_regression_tests.sh
  ```在这种情况下，每次推送到`main`分支都会启动`Run Regression Tests`作业，该作业执行一个脚本来运行回归[test suite](../T/test-suite.md)。如果测试通过，则更改得到验证；如果没有，团队就会收到由最近的更改引起的潜在问题的警报。

#### 变更控制如何帮助管理测试环境？

[Change control](../C/change-control.md) 可以通过确保系统地跟踪、审查和实施对环境的**修改**来显着增强[test environments](../T/test-environment.md) 的管理。此过程最大限度地降低了**未经授权或不兼容的更改**的风险，这些更改可能导致测试结果不一致或系统停机。
  通过使用[change control](../C/change-control.md)，[test environments](../T/test-environment.md) 保持**稳定**和**可预测**，这对于可靠的自动化至关重要。 [Test automation](../T/test-automation.md) 工程师可以确信测试是针对已知配置执行的，测试结果的任何变化都是由于被测应用程序的变化，而不是环境的变化。
  当提出更改时，他们会经历一个**审查过程**，其中通常包括[impact analysis](../I/impact-analysis.md)。这可确保 [test automation](../T/test-automation.md) 套件得到更新或配置以适应这些更改。例如，如果要将新的浏览器版本引入[test environment](../T/test-environment.md)，则可能需要调整自动化脚本以保持兼容性。
  此外，[change control](../C/change-control.md) 有助于**回滚过程**。如果更改对[test environment](../T/test-environment.md)产生负面影响，它可以快速恢复到之前的状态，从而最大限度地减少对测试过程的干扰。
  最后，[change control](../C/change-control.md) 支持**可追溯性**。通过维护更改记录，[test automation](../T/test-automation.md) 工程师可以将测试失败与特定环境更改相关联，从而帮助更快地诊断和解决问题。
  总之，[change control](../C/change-control.md) 是维护[test environments](../T/test-environment.md) 完整性和可靠性的关键实践，而[test environments](../T/test-environment.md) 反过来又支持健壮且有效的[test automation](../T/test-automation.md)。

#### 变更控制如何有助于测试自动化？

通过确保自动化测试随着软件的发展保持相关性和有效性，[Change control](../C/change-control.md) 可以显着增强[test automation](../T/test-automation.md)。当引入变更时，**[change control](../C/change-control.md) 流程**确保对其进行系统记录、审查和批准。该文档为[test automation](../T/test-automation.md) 工程师提供了对更改内容的清晰见解，使他们能够相应地**更新或创建新的测试**。
  自动化测试可以**映射到特定更改**，从而允许有针对性的[regression testing](../R/regression-testing.md)。此映射可确保任何新的或更新的测试都集中在最有可能受最近更改影响的应用程序区域，从而优化测试工作和资源利用率。
  此外，[change control](../C/change-control.md) 可以通过提供应用更改的受控方法来促进**[test environments](../T/test-environment.md)** 的维护。这确保[test environments](../T/test-environment.md)反映被测应用程序的当前状态，这对于自动化测试的准确性至关重要。
  将[change control](../C/change-control.md) 合并到[test automation](../T/test-automation.md) 中还意味着自动化测试中的任何失败都可以快速与特定更改相关联，从而使**调试和故障排除**更加高效。这种对问题的快速识别可以带来更快的解决方案，最终有助于打造更强大、更可靠的软件产品。
  通过遵守[change control](../C/change-control.md)程序，[test automation](../T/test-automation.md)工程师可以确保他们的[test suites](../T/test-suite.md)始终与应用程序的当前状态保持一致，从而**最大化[test coverage](../T/test-coverage.md)**并**最小化缺陷渗透到生产中的风险**。
