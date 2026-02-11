# 系统测试 (System Testing)
[系统测试 (System Testing)](#system-testing) [系统测试 (System testing)](/wiki/system-testing)

### 相关术语：
- [集成测试 (Integration Testing)](/glossary/integration-testing)
- [功能测试 (Functional Testing)](/glossary/functional-testing)
- [非功能测试 (Non-functional Testing)](/glossary/non-functional-testing)

## 关于系统测试的常见问题？

#### 基础与重要性
- **什么是软件测试中的系统测试？**
  **系统测试 (System testing)** 是一个 **高层级 (high-level)** 的测试阶段，在这个阶段，对一个完整的、集成后的系统进行评估，以验证其是否满足指定的需求。它涉及将系统作为一个整体进行测试，以确保所有组件和功能能够正确协同工作，通常在 **单元测试** 和 **[集成测试 (integration testing)](/wiki/integration-testing)** 之后执行。这一阶段检查整个系统是否符合业务需求，并评估系统是否已准备好发布。
  在 **系统测试** 期间，应用程序在一个高度模拟生产环境（软件最终部署的环境）的环境中进行测试。这包括对 **[功能需求 (functional requirements)](/wiki/functional-requirements)** 以及性能、安全性和易用性等非功能性需求的测试。其目的是识别任何可能影响用户体验或导致系统故障的缺陷。
  **系统测试** 的 **[测试用例 (test cases)](/wiki/test-case)** 源自系统的 **规范** 和 **[用例 (use cases)](/wiki/use-case)**，确保所有用户流和交互都得到测试。拥有一个覆盖各种场景（包括边缘情况和失败路径）的全面 **[测试套件 (test suite)](/wiki/test-suite)** 至关重要。
  **系统测试** 通常是自动化的，以提高效率和可重复性。自动化框架和工具执行预定义的 **[测试脚本 (test scripts)](/wiki/test-script)**，这些脚本可以使用不同的数据集多次运行，以彻底测试系统在各种条件下的行为。自动化有助于在系统发生更改时识别回归问题。
  总之，**系统测试** 是软件开发过程中的关键步骤，重点在于验证系统的功能并确保在发布到市场之前满足终端用户的需求。

- **为什么系统测试在软件开发生命周期中很重要？**
  **系统测试** 在软件开发生命周期中至关重要，因为它作为一个全面的 **[验证 (verification)](/wiki/verification)** 阶段，确保软件在类生产环境中的行为符合预期。它验证了各种系统组件的 **集成**，并根据指定需求检查端到端系统功能。通过模拟真实场景，**系统测试** 能够发现单元测试或集成测试可能遗漏的缺陷，因为后者侧重于单个模块或有限的交互。
  这一级别的测试是评估系统在各种条件下行为、评估 **[功能需求 (以非功能性为例)](/wiki/functional-requirements)**（如 **性能**、**安全性** 和 **易用性**）的第一个机会。它是软件交付给终端用户之前的一个关键检查点，降低了部署后可能产生的昂贵且损害组织声誉的问题风险。
  此外，**系统测试** 有助于确保 **合规性 (regulatory compliance)**，并且在具有严格质量标准的行业中可能是一个强制性步骤。它提供了一定程度的保证，证明软件能够满足技术和业务双重需求，这对于利益相关者的信心和产品成功至关重要。
  总之，**系统测试** 是一个关键阶段，充当着守门员的角色，确认软件已准备好发布并能够为用户提供预期价值，同时最大限度地减少对运营和客户满意度的潜在负面影响。

- **系统测试有哪些不同的类型？**
  不同类型的 **系统测试** 包括：
  - **[功能测试 (Functional Testing)](/wiki/functional-testing)**：根据功能需求/规范验证软件系统。
  - **[性能测试 (Performance Testing)](/wiki/performance-testing)**：评估系统在特定负载下的速度、响应能力和稳定性。
  - **[负载测试 (Load Testing)](/wiki/load-testing)**：检查系统如何处理大量数据或用户。
  - **[压力测试 (Stress Testing)](/wiki/stress-testing)**：确定系统在极端条件下的健壮性和错误处理能力。
  - **[易用性测试 (Usability Testing)](/wiki/usability-testing)**：确保系统用户友好且直观。
  - **[安全性测试 (Security Testing)](/wiki/security-testing)**：识别漏洞并确保数据免受未经授权的访问。
  - **[兼容性测试 (Compatibility Testing)](/wiki/compatibility-testing)**：验证系统在不同设备、浏览器和操作系统上是否按预期工作。
  - **恢复测试 (Recovery Testing)**：确认系统能从崩溃、硬件故障和其他类似问题中恢复。
  - **[可靠性测试 (Reliability Testing)](/wiki/reliability-testing)**：测量系统在预定条件下执行特定功能的能力。
  - **[回归测试 (Regression Testing)](/wiki/regression-testing)**：确保新的代码更改不会对现有功能产生不利影响。
  - **[探索性测试 (Exploratory Testing)](/wiki/exploratory-testing)**：一种允许测试人员探索系统并在没有预定义用例或脚本的情况下执行测试的方法。
  - **安装测试 (Installation Testing)**：确认系统在目标环境中正确安装并按预期工作。
  - **合规性测试 (Compliance Testing)**：检查系统是否遵循标准、法规或指南。
  每种类型都针对系统功能和性能的不同方面，确保在发布前进行全面评估。

- **系统测试与其他类型的测试有何不同？**
  **系统测试** 是评估完整且集成的软件系统以确保符合指定需求的测试级别。它与其他类型的测试的区别主要在于其 **范围 (scope)** 和 **目标 (objectives)**。
  - **[单元测试 (Unit Testing)](/wiki/unit-testing)**：专注于单个组件或代码段，以验证每个单元在隔离状态下正确运行。
  - **[集成测试 (Integration Testing)](/wiki/integration-testing)**：确保多个单元或组件按预期协同工作。
  - **[验收测试 (Acceptance Testing)](/wiki/acceptance-testing)**：根据业务需求验证软件，通常由最终用户进行，以确定系统是否可以交付。
  相比之下，**系统测试** 更为全面，关注被测整个系统的行为。它在 **高度模拟生产环境** 的环境中执行，包括硬件、软件和网络配置。这一级别的测试旨在识别只有在组件集成并在全系统背景下交互时才会出现缺陷。
  **系统测试** 通常由 **测试团队负责**，而不是编写代码的开发人员。它在集成测试之后和验收测试之前进行，作为软件发布到市场或移交给验收测试前的最终 **[验证 (verification)](/wiki/verification)**。
  虽然其他测试类型可能孤立地关注 **功能**、**性能** 或 **安全性**，但 **系统测试** 涵盖了所有这些方面，以确保对软件质量进行全面评估。这是捕捉可能在现实场景中影响用户体验或导致系统故障的问题的关键步骤。

- **系统测试员的作用是什么？**
  系统测试员的作用是 **验证 (validate)** 完整且集成的软件系统，以确保其满足指定需求。他们负责执行 **系统级 [测试用例 (test cases)](/wiki/test-case)**，模拟真实场景和端到端流程，这通常涉及与软件、硬件和网络环境的复杂交互。
  系统测试员必须具有 **大局观 (holistic view)**，了解软件架构和设计，以创建相关的测试用例，涵盖功能测试、非功能测试和 **[回归测试 (regression testing)](/wiki/regression-testing)**。他们还需要擅长识别和记录 **缺陷 (defects)**，并与开发人员密切合作以确保这些缺陷得到解决。
  其角色的一个关键方面是确保系统在各种条件下都能正确运行，这包括 **[压力测试 (stress testing)](/wiki/stress-testing)**、**[性能测试 (performance testing)](/wiki/performance-testing)** 和 **[安全性测试 (security-testing)](/wiki/security-testing)**。他们还必须在系统发布到生产环境前验证其是否符合所有监管标准和用户需求。
  除了 **[手动测试 (manual testing)](/wiki/manual-testing)**，系统测试员通常使用 **自动化框架** 来运行重复且费时的测试，从而提高资源利用效率并缩短反馈周期。他们必须维护并更新自动化 **[测试脚本 (test scripts)](/wiki/test-scripts)** 以与系统的新功能和更改保持同步。
  有效的沟通技巧对于系统测试员至关重要，因为他们经常需要与包括开发人员、业务分析师和利益相关者在内的其他团队成员协作，以确保对系统及其目标的共同理解。他们在软件是否已准备好发布的最终决策过程中发挥着关键作用。

#### 流程与技术
- **系统测试的流程是什么？**
  **系统测试** 的流程涉及一系列步骤，以根据指定需求验证完整且集成的软件系统。
  1. 最初创建一个 **[测试计划 (test plan)](/wiki/test-plan)**，概述测试策略、资源、进度和范围。
  2. 然后设计 **[测试用例 (test cases)](/wiki/test-case)** 以覆盖系统级的所有功能，通常使用 **黑盒测试** 技术，即不查看内部代码结构进行测试。
  3. 一旦测试用例准备就绪，就会设置一个模拟生产环境的 **[测试环境 (test environment)](/wiki/test-environment)**，以确保测试在接近真实使用的条件下运行。
  4. 随后 **执行测试用例**，手动或使用自动化工具验证系统行为和性能。在此阶段，经常编写并执行 **[测试脚本 (test scripts)](/wiki/test-script)** 来自动化重复测试和回归测试。
  5. 识别出的 **缺陷** 会通过 **缺陷管理系统** 进行报告和跟踪。每个缺陷都会被安排优先级、分配并由开发人员修复，然后系统会被重新测试以确认修复并检查是否有新问题。
  6. 在整个过程中，测试结果都会被记录，为所进行的测试提供证据。这包括日志、数据输出和屏幕捕获。
  7. 最后编译一份 **[测试报告 (test report)](/wiki/test-report)**，总结测试活动、结果和任何剩余风险。这份报告对于利益相关者做出系统发布就绪性的知情决策至关重要。

- **系统测试中使用了哪些不同的技术？**
  不同类型的系统测试技术专注于作为一个整体验证系统的功能、性能和可靠性。这些技术包括：
  - **[等价类划分 (Equivalence Partitioning)](/wiki/equivalence-partitioning)**：将输入数据划分为等价部分，以减少测试用例数量。
  - **边界值分析 (Boundary Value Analysis)**：在输入范围的边缘进行测试以捕捉偏一错误。
  - **[决策表测试 (Decision Table Testing)](/wiki/decision-table-testing)**：使用表格表示逻辑关系。
  - **[状态转换测试 (State Transition Testing)](/wiki/state-transition-testing)**：检查系统在各种状态和转换中的行为。
  - **[用例测试 (Use Case Testing)](/wiki/use-case-testing)**：确保系统能处理真实的商业场景。
  - **[探索性测试 (Exploratory Testing)](/wiki/exploratory-testing)**：学习、测试设计和执行同时进行。
  - **组合测试 (Combinatorial Testing)**：测试输入的不同组合。
  - **[安全性测试 (Security Testing)](/wiki/security-testing)**：识别系统中的漏洞。
  - **[性能测试 (Performance Testing)](/wiki/performance-testing)**：评估各种条件下的响应能力、稳定性和可扩展性。
  - **[负载测试 (Load Testing)](/wiki/load-testing)**：评估预期及峰值负载下的行为。
  - **[压力测试 (Stress Testing)](/wiki/stress-testing)**：通过极端条件测试健壮性。
  - **[兼容性测试 (Compatibility Testing)](/wiki/compatibility-testing)**：检查不同硬件、软件和网络环境。
  - **[可靠性测试 (Reliability Testing)](/wiki/reliability-testing)**：测量一段时间内的一致性。

- **系统测试是如何在敏捷方法中执行的？**
  在 **敏捷方法** 中，**系统测试** 被集成到迭代开发流程中。它随着开发冲刺或 **[迭代 (iterations)](/wiki/iteration)** 增量执行，确保新功能按预期工作且整个系统保持稳定。
  **协作** 是关键。测试人员通常与开发人员并行工作。
  **持续集成 (CI)** 工具被用来自动化构建和测试过程，提供即时反馈。
  **[测试驱动开发 (TDD)](/wiki/test-driven-development)** 和 **[行为驱动开发 (BDD)](/wiki/bdd)** 通常用于定义系统 **[测试用例 (test cases)](/wiki/test-case)**。
  **用户故事** 引导系统测试的创建，验收标准成为测试用例的基础。
  **[探索性测试 (Exploratory testing)](/wiki/exploratory-testing)** 也是其中一部分，用于识别结构化测试可能遗漏的问题。
  每次 **[迭代 (iteration)](/wiki/iteration)** 结束时的 **回顾总结** 提供了反思并调整系统测试流程的机会。
  ```yaml
  # 简单的系统测试 CI 流水线脚本示例
  pipeline {
      agent any
      stages {
          stage('Build') {
              steps {
                  sh 'make build'
              }
          }
          stage('Test') {
              steps {
                  sh 'make system-test'
              }
          }
      }
      post {
          always {
              sh 'make clean'
          }
      }
  }
  ```
  这种方法确保了系统测试是一个持续的、不可或缺的开发周期部分。

- **自动化在系统测试中的作用是什么？**
  在 **系统测试** 中，自动化通过 **提高效率**、**减少人为错误** 和 **加速 [测试用例 (test cases)](/wiki/test-case)** 执行发挥着核心作用。自动化支持执行繁重且重复的 **[测试套件 (test suites)](/wiki/test-suite)**，这在手动执行时会非常费时。
  自动化提供了 **[测试执行 (test execution)](/wiki/test-execution)** 的 **一致性**，确保每次运行都以相同方式进行，这对于识别间歇性问题至关重要。它还通过验证更改未损害现有功能来促进 **[回归测试 (regression-testing)](/wiki/regression-testing)**。
  **[测试自动化 (Test automation)](/wiki/test-automation)** 还会生成详尽的日志和报告，这对于调试很有价值。最后，自动化支持创建可重用的测试用例套件，从长期来看能 **节省时间和资源**。

- **系统测试常用工具有哪些？**
  常用的 **系统测试** 工具包括：
  - **[Selenium](/wiki/selenium)**：自动化 Web 浏览器的开源工具，支持多种语言编写 **[测试脚本 (test scripts)](/wiki/test-script)**。
  - **[HP Unified Functional Testing (UFT)](/wiki/functional-testing)**：支持 GUI 和 **[API 测试 (API testing)](/wiki/api-testing)**。
  - **TestComplete**：用于 Windows、Web、Android 和 iOS 的 **[自动化测试 (automated testing)](/wiki/automated-testing)** 平台。
  - **Ranorex**：一个 GUI **[测试自动化 (test automation)](/wiki/test-automation)** 框架。
  - **[Apache JMeter](/wiki/jmeter)**：专为 **[负载测试 (load-testing)](/wiki/load-testing)** 设计，也支持功能 **[系统测试 (system-testing)](/wiki/system-testing)**。
  - **IBM Rational Functional Tester (RFT)**：支持多种应用和脚本编写。
  - **Tricentis Tosca**：加速敏捷和 DevOps 迭代的持续测试平台。
  - **SoapUI**：功能强大的 Web Service 测试工具。
  - **[Postman](/wiki/postman)**：强大的 **[API 测试 (API testing)](/wiki/api-testing)** 工具，常用于获取系统测试所需的响应。
  - **Robot Framework**：开源的关键词驱动框架，用于 **[验收测试 (acceptance testing)](/wiki/acceptance-testing)** 和 **[测试驱动开发 (test-driven development)](/wiki/test-driven-development)**。

#### 挑战与最佳实践
- **系统测试中常见的挑战有哪些？**
  **系统测试** 的常见挑战包括：
  - **集成问题**：确保所有组件无缝协作，特别是第三方或遗留系统。
  - **环境差异**：测试、阶段和生产环境间的差异导致难以复现的 Bug。
  - **复杂的 [测试用例 (Test Cases)](/wiki/test-case)**：打造覆盖所有场景且不显冗余的用例。
  - **数据管理**：确保测试数据具代表性且符合隐私规范。
  - **性能与负载**：识别瓶颈需要专门的资源。
  - **[不稳定测试 (Flaky Tests)](/wiki/flaky-test)**：处理时好时坏的非确定性测试。
  - **资源约束**：硬件、软件或熟练人员的访问受限。
  - **时间限制**：质量与发布进度之间的权衡。
  - **测试维护**：随着系统演进不断更新脚本。
  - **[安全性测试 (Security Testing)](/wiki/security-testing)**：在满足合规性的同时确保系统无漏洞。

- **进行有效系统测试的最佳实践是什么？**
  - **明确目标**：确定你希望通过系统测试达到什么目的（如性能基准）。
  - **制定详尽的 [测试计划 (test plan)](/wiki/test-plan)**：包含用例、预期结果和通过标准。
  - **优先排序 [测试用例 (test cases)](/wiki/test-case)**：首先关注核心功能和高风险区域。
  - **结合手动与自动化测试**：自动化提效，手动满足探索性场景。
  - **保持可追溯性**：将用例链接到需求。
  - **实施持续集成**：提早发现集成问题。
  - **利用数据驱动测试**：使用不同数据集。
  - **执行 [回归测试 (regression-testing)](/wiki/regression-testing)**：定期复测旧功能。
  - **监控与测量**：收集缺陷密度和通过率等指标。
  - **记录详尽文档**：辅助调试和未来循环。

- **如何优化系统测试效率？**
  - 重视 **优先级排序** 和 **自动化**。
  - 对关键功能使用 **[质量风险驱动测试 (risk-based testing)](/wiki/risk-based-testing)**。
  - 利用 **[测试自动化 (test automation)](/wiki/test-automation)** 框架。
  - 应用 **[假阳性 (false positives)](/wiki/false-positive)** 识别机制确保测试稳定。
  - 实施 **持续集成**。
  - **并发测试** 是缩短时间的关键。
  - 高效的 **测试数据管理**，确保数据无需手动干预。
  - 通过 **重构** 优化 **[测试脚本 (test scripts)](/wiki/test-script)**，保持其 **模块化** 和 **易维护性**。
  - 分析 **[测试执行 (test execution)](/wiki/test-execution)** 瓶颈，精简 **[测试套件 (test suite)](/wiki/test-suite)**。
  - 加强团队间 **协作**。

- **如何使系统测试更有效？**
  - 根据风险排序 **[测试用例 (test cases)](/wiki/test-case)**。
  - 利用 **服务虚拟化** 模拟不可用系统。
  - 结合 **[探索性测试 (exploratory-testing)](/wiki/exploratory-testing)** 以发现脚本之外的问题。
  - 维护代码库减少不稳定性。

- **系统测试中应避免哪些常见错误？**
  - **忽视非功能性需求**。
  - **[测试覆盖率 (test-coverage)](/wiki/test-coverage) 不足**。
  - **在不真实的环境中测试**。
  - **过度依赖自动化**：不能完全取代手动探索性测试。
  - **忽视测试数据管理**。
  - **跳过 [回归测试 (regression-testing)](/wiki/regression-testing)**。
  - **未对 [缺陷 (bugs)](/wiki/bug) 进行优先级排序**。
  - **缺乏文档记录**。
  - **低估测试计划的重要性**。
