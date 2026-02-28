# 验收测试

<!-- TOC START -->
- [相关术语：](#相关术语：)
  - [另请参阅：](#另请参阅：)
- [关于验收测试的问题？](#关于验收测试的问题？)
  - [基础知识和重要性](#基础知识和重要性)
    - [什么是验收测试？](#什么是验收测试？)
    - [为什么验收测试很重要？](#为什么验收测试很重要？)
    - [验收测试有哪些不同类型？](#验收测试有哪些不同类型？)
    - [验收测试如何融入软件开发生命周期？](#验收测试如何融入软件开发生命周期？)
    - [验收测试和其他类型的测试有什么区别？](#验收测试和其他类型的测试有什么区别？)
  - [技术和策略](#技术和策略)
    - [验收测试中使用哪些常见技术？](#验收测试中使用哪些常见技术？)
    - [您如何制定验收测试策略？](#您如何制定验收测试策略？)
    - [自动化在验收测试中的作用是什么？](#自动化在验收测试中的作用是什么？)
    - [验收测试中有哪些挑战以及如何克服这些挑战？](#验收测试中有哪些挑战以及如何克服这些挑战？)
    - [如何将验收测试集成到持续交付管道中？](#如何将验收测试集成到持续交付管道中？)
  - [工具和技术](#工具和技术)
    - [验收测试常用哪些工具？](#验收测试常用哪些工具？)
    - [这些工具在验收测试过程中有何帮助？](#这些工具在验收测试过程中有何帮助？)
    - [不同验收测试工具的优缺点是什么？](#不同验收测试工具的优缺点是什么？)
    - [API 在验收测试中的作用是什么？](#api-在验收测试中的作用是什么？)
    - [如何在验收测试中利用云技术？](#如何在验收测试中利用云技术？)
  - [最佳实践](#最佳实践)
    - [验收测试的最佳实践有哪些？](#验收测试的最佳实践有哪些？)
    - [如何随着时间的推移维护和更新验收测试？](#如何随着时间的推移维护和更新验收测试？)
    - [文档在验收测试中的作用是什么？](#文档在验收测试中的作用是什么？)
    - [如何使验收测试更加高效？](#如何使验收测试更加高效？)
    - [如何有效传达验收测试的结果？](#如何有效传达验收测试的结果？)
<!-- TOC END -->

验收测试

由潜在的最终用户或客户进行，以确定软件是否满足所需的规格并适合其预期用途。

## 相关术语：

- [User Acceptance Testing](../U/user-acceptance-testing.md)
- [FAT (Factory Acceptance Testing)](../F/fat-factory-acceptance-testing.md)

### 另请参阅：

- [Wikipedia](https://en.wikipedia.org/wiki/Acceptance_testing)

## 关于验收测试的问题？

### 基础知识和重要性

#### 什么是验收测试？

[Acceptance testing](../A/acceptance-testing.md) 是根据预定义标准验证**系统功能**和**业务需求**的阶段，确保软件已准备好投入生产。这通常是产品交付给客户或提供给最终用户之前的**最后一步**。这种形式的测试侧重于**用户体验**和**整体系统行为**而不是单个组件，通常涉及**真实场景**和**端到端工作流程**。
  要有效地执行[acceptance testing](../A/acceptance-testing.md)，请考虑以下事项：

- **定义明确的验收标准**：这些应该得到利益相关者的同意并构成测试用例的基础。
  - **优先考虑[test cases](../T/test-case.md)**：专注于提供最大价值的关键业务功能和用户旅程。
  - **利用用户反馈**：结合 Beta 测试人员或真实用户的见解来完善测试。
  - **适当时自动化**：虽然自动化可以提高效率，但某些测试可能需要手动、人性化的接触来评估可用性和美观性。
  - **审查和调整**：使用结果就产品的准备情况做出明智的决策并确定需要改进的领域。
  请记住，[acceptance testing](../A/acceptance-testing.md) 不仅仅是查找缺陷，而是确保产品满足业务需求并提供积极的用户体验。与利益相关者保持沟通渠道畅通，以协调期望和结果。

- **定义明确的验收标准**：这些应该得到利益相关者的同意并构成测试用例的基础。
  - **优先考虑[test cases](../T/test-case.md)**：专注于提供最大价值的关键业务功能和用户旅程。
  - **利用用户反馈**：结合 Beta 测试人员或真实用户的见解来完善测试。
  - **适当时自动化**：虽然自动化可以提高效率，但某些测试可能需要手动、人性化的接触来评估可用性和美观性。
  - **审查和调整**：使用结果就产品的准备情况做出明智的决策并确定需要改进的领域。

#### 为什么验收测试很重要？

[Acceptance testing](../A/acceptance-testing.md) 至关重要，因为它是产品发布到市场或交付给客户之前的**最终[verification](../V/verification.md)**。它确保软件满足**业务需求**并能够提供**所需的用户体验**。通过模拟实际使用情况，它可以验证端到端业务流程，而不仅仅是单个组件或功能。
  这种形式的测试通常是针对 [bugs](../B/bug.md) 和可能显着影响客户满意度和商业成功的问题的**最后一道防线**。它有助于识别**用户期望**与实际产品之间的任何差异，使团队能够在问题影响最终用户之前解决问题。
  此外，[acceptance testing](../A/acceptance-testing.md) 提供了明确的**产品验收指标**，为什么被视为“成品”设定了明确的标准。它还提供**法律合规性检查**，确保软件遵守与行业或市场相关的法规和标准。
  本质上，[acceptance testing](../A/acceptance-testing.md) 是为了**建立对产品质量及其部署准备情况的信心**。这是一个不仅可以审查功能，还可以审查应用程序的**可用性、可访问性和整体性能**的机会，这对于用户接受度至关重要。如果没有这个阶段，团队将面临发布可能无法完全满足客户需求或期望的产品的风险，从而导致支持成本增加、声誉受损，并可能导致产品在市场上失败。

#### 验收测试有哪些不同类型？

[Acceptance testing](../A/acceptance-testing.md) 可以分为几种类型，每种类型都有特定的重点和目的：

- **[User Acceptance Testing](../U/user-acceptance-testing.md) (UAT)**：旨在确保软件满足用户要求并可供实际使用。用户或利益相关者执行这些测试来验证端到端业务流程。
  - **业务[Acceptance Testing](../A/acceptance-testing.md) (BAT)**：专注于验证软件的业务目标。它与 UAT 类似，但具有更具战略性的视角，通常涉及高层业务利益相关者。
  - **[Alpha Testing](../A/alpha-testing.md)**：在软件发布给外部用户之前由内部员工执行，以尽早发现任何重大问题。
  - **[Beta Testing](../B/beta-testing.md)**：由一组选定的外部用户在现实环境中进行，从用户的角度识别任何问题。
  - **合同[Acceptance Testing](../A/acceptance-testing.md)**：确保软件满足合同要求，通常根据供应商和客户商定的标准清单执行。
  - **法规[Acceptance Testing](../A/acceptance-testing.md) (RAT)**：验证软件是否符合行业法规和标准，这在金融、医疗保健和航空等领域至关重要。
  - **操作[Acceptance Testing](../A/acceptance-testing.md) (OAT)**：也称为生产[Acceptance Testing](../A/acceptance-testing.md)，它检查备份、恢复和维护程序等操作方面。
  每种类型的[acceptance testing](../A/acceptance-testing.md) 用于验证软件部署和使用准备情况的不同方面，确保满足所有利益相关者的期望。

- **[User Acceptance Testing](../U/user-acceptance-testing.md) (UAT)**：旨在确保软件满足用户要求并可供实际使用。用户或利益相关者执行这些测试来验证端到端业务流程。
  - **业务[Acceptance Testing](../A/acceptance-testing.md) (BAT)**：专注于验证软件的业务目标。它与 UAT 类似，但具有更具战略性的视角，通常涉及高层业务利益相关者。
  - **[Alpha Testing](../A/alpha-testing.md)**：在软件发布给外部用户之前由内部员工执行，以尽早发现任何重大问题。
  - **[Beta Testing](../B/beta-testing.md)**：由一组选定的外部用户在现实环境中进行，从用户的角度识别任何问题。
  - **合同[Acceptance Testing](../A/acceptance-testing.md)**：确保软件满足合同要求，通常根据供应商和客户商定的标准清单执行。
  - **法规[Acceptance Testing](../A/acceptance-testing.md) (RAT)**：验证软件是否符合行业法规和标准，这在金融、医疗保健和航空等领域至关重要。
  - **操作[Acceptance Testing](../A/acceptance-testing.md) (OAT)**：也称为生产[Acceptance Testing](../A/acceptance-testing.md)，它检查备份、恢复和维护程序等操作方面。

#### 验收测试如何融入软件开发生命周期？

[Acceptance testing](../A/acceptance-testing.md) 是**软件开发生命周期 (SDLC)** 中的关键阶段，通常在 **[system testing](../S/system-testing.md)** 之后和产品上线之前执行，称为 **预发布** 阶段。它充当最终[verification](../V/verification.md)，以确保软件满足业务要求并准备好进行操作使用。
  在**敏捷方法**中，[acceptance testing](../A/acceptance-testing.md) 集成到[iterations](../I/iteration.md) 中，允许持续验证用户故事。这是涉及**开发人员**、**测试人员**和**利益相关者**的协作努力，以确认产品的功能与业务需求相符。
  对于**瀑布项目**，[acceptance testing](../A/acceptance-testing.md) 是一个独特的阶段，在广泛的[system testing](../S/system-testing.md) 之后遵循更线性的进展。在将软件移交给客户或提供给最终用户之前，它充当看门人的角色。
  在这两种情况下，重点都是验证**端到端业务流程**而不是单个组件，以确保软件在类似生产的环境中按预期运行。验收测试基于所有相关方同意的**预定义标准**。
  [acceptance testing](../A/acceptance-testing.md) 的结果对于**继续/不继续的决定**至关重要。成功通过表明该软件被认为**适合目的**，而任何重大问题都必须在发布前解决。此阶段也是验证**监管和合规性要求**（如果适用）的机会。
  将 [acceptance testing](../A/acceptance-testing.md) 纳入 SDLC 可确保最终产品不仅在技术上有效，而且还能为企业及其用户提供预期的价值。

#### 验收测试和其他类型的测试有什么区别？

[Acceptance testing](../A/acceptance-testing.md) 与其他测试类型的不同之处主要在于其**范围**和**利益相关者**。 [unit testing](../U/unit-testing.md) 专注于各个组件，[integration testing](../I/integration-testing.md) 确保系统的不同部分协同工作，[acceptance testing](../A/acceptance-testing.md) 则评估系统是否符合业务要求并评估其是否已准备好部署。
  **[Functional testing](../F/functional-testing.md)** 检查代码的特定功能，而 [acceptance testing](../A/acceptance-testing.md) 从最终用户的角度关注**整个应用程序的行为**。这是一种黑盒测试，应用程序的内部工作不是重点。
  另一方面，**[Performance testing](../P/performance-testing.md)** 衡量系统在特定工作负载下的响应能力和稳定性，这通常不是 [acceptance testing](../A/acceptance-testing.md) 的主要目标。
  **[Usability testing](../U/usability-testing.md)** 与用户体验有关，但它通常比 [acceptance testing](../A/acceptance-testing.md) 更主观且不那么正式，后者需要满足特定的标准。
  [Acceptance testing](../A/acceptance-testing.md) 通常是软件上线前的最后一步，涉及**真实场景**和**根据用户需求进行验证**。它通常由利益相关者或业务代表执行，他们不像 QA 或开发团队那样深入参与开发过程。这种外部视角对于确保软件满足其目标用户的需求和期望至关重要。
  总之，[acceptance testing](../A/acceptance-testing.md) 的独特之处在于它专注于从用户的角度验证产品是否已准备好投入生产，而不仅仅是验证技术正确性或性能基准。

### 技术和策略

#### 验收测试中使用哪些常见技术？

[acceptance testing](../A/acceptance-testing.md) 中使用的常用技术包括：

- **行为驱动开发 ([BDD](../B/bdd.md))**：利用 Cucumber、SpecFlow 或 Behat 等框架以利益相关者可以理解的自然语言编写测试。测试基于用户故事，以确保软件按预期运行。

    ```
    Feature: User login
      Scenario: Successful login with valid credentials
        Given the login page is displayed
        When the user enters valid credentials
        Then the user is redirected to the dashboard
    ```

- **[User Acceptance Testing](../U/user-acceptance-testing.md) (UAT)**：真实用户在模拟生产的环境中测试软件，以验证端到端业务流程。
  - **[Exploratory Testing](../E/exploratory-testing.md)**：测试人员在没有预定义[test cases](../T/test-case.md) 的情况下探索软件，以发现意外行为或[bugs](../B/bug.md)。
  - **[Session-Based Testing](../S/session-based-testing.md)**：具有特定重点或目标以及设定时间范围的结构化[exploratory testing](../E/exploratory-testing.md) 会议。
  - **基于清单的测试**：使用功能或要求列表作为指南，以确保所有功能都得到验证。
  - **Alpha/[Beta Testing](../B/beta-testing.md)**：将软件发布给组织外部的有限受众（alpha）或实际用户（beta）以收集反馈。
  - **自动化[Regression Testing](../R/regression-testing.md)**：运行自动化测试以确认最近的更改不会对现有功能产生不利影响。
  - **[Performance Testing](../P/performance-testing.md)**：评估系统在负载下的性能，以确保其满足速度和响应能力的验收标准。
  - **合规性测试**：验证软件是否符合行业标准、法规或合同协议。
  这些技术有助于确保软件满足业务需求，提供良好的用户体验，并且在发布之前不存在关键问题。

- **行为驱动开发 ([BDD](../B/bdd.md))**：利用 Cucumber、SpecFlow 或 Behat 等框架以利益相关者可以理解的自然语言编写测试。测试基于用户故事，以确保软件按预期运行。

    ```
    Feature: User login
      Scenario: Successful login with valid credentials
        Given the login page is displayed
        When the user enters valid credentials
        Then the user is redirected to the dashboard
    ```

- **[User Acceptance Testing](../U/user-acceptance-testing.md) (UAT)**：真实用户在模拟生产的环境中测试软件，以验证端到端业务流程。
  - **[Exploratory Testing](../E/exploratory-testing.md)**：测试人员在没有预定义[test cases](../T/test-case.md) 的情况下探索软件，以发现意外行为或[bugs](../B/bug.md)。
  - **[Session-Based Testing](../S/session-based-testing.md)**：具有特定重点或目标以及设定时间范围的结构化[exploratory testing](../E/exploratory-testing.md) 会议。
  - **基于清单的测试**：使用功能或要求列表作为指南，以确保所有功能都得到验证。
  - **Alpha/[Beta Testing](../B/beta-testing.md)**：将软件发布给组织外部的有限受众（alpha）或实际用户（beta）以收集反馈。
  - **自动化[Regression Testing](../R/regression-testing.md)**：运行自动化测试以确认最近的更改不会对现有功能产生不利影响。
  - **[Performance Testing](../P/performance-testing.md)**：评估系统在负载下的性能，以确保其满足速度和响应能力的验收标准。
  - **合规性测试**：验证软件是否符合行业标准、法规或合同协议。

#### 您如何制定验收测试策略？

制定 **[acceptance testing](../A/acceptance-testing.md) 策略**涉及几个关键步骤：

1. **定义验收标准**：与利益相关者合作，为每个功能或用户故事建立清晰且可衡量的验收标准。
  2. **优先考虑[Test Cases](../T/test-case.md)**：确定关键业务流程并相应地优先考虑[test cases](../T/test-case.md)。关注用户体验和业务需求。
  3. **选择测试技术**：选择适当的测试技术，例如[BDD](../B/bdd.md)（行为驱动开发）或示例规范以创建可理解且可执行的规范。
  4. **规划[Test Data](../T/test-data.md) 管理**：考虑数据隐私和合规性要求，确保不同场景下相关[test data](../T/test-data.md) 的可用性。
  5. **设计[Test Environment](../T/test-environment.md)**：建立一个稳定的[test environment](../T/test-environment.md)，尽可能模仿生产以发现特定于环境的问题。
  6. **明智地自动化**：自动回归和高[priority](../P/priority.md) [test cases](../T/test-case.md) 以节省时间和资源。保留[manual testing](../M/manual-testing.md) 用于探索性、可用性和临时场景。
  7. **与 CI/CD 集成**：将验收测试嵌入 CI/CD 管道中，以实现应用程序的早期和频繁验证。
  8. **监控和测量**：实施监控以跟踪[test coverage](../T/test-coverage.md)、通过/失败率和缺陷密度。使用这些指标来完善测试过程。
  9. **审查和调整**：与团队定期审查[test strategy](../T/test-strategy.md)，以适应应用程序或业务优先级的变化。
  10. **利益相关者沟通**：通过清晰、简洁的报告和仪表板让利益相关者了解情况，深入了解测试进度和结果。
  通过执行这些步骤，您可以创建一个稳健的 [acceptance testing](../A/acceptance-testing.md) 策略，该策略与业务目标保持一致并确保高质量的产品。

1. **定义验收标准**：与利益相关者合作，为每个功能或用户故事建立清晰且可衡量的验收标准。
  2. **优先考虑[Test Cases](../T/test-case.md)**：确定关键业务流程并相应地优先考虑[test cases](../T/test-case.md)。关注用户体验和业务需求。
  3. **选择测试技术**：选择适当的测试技术，例如[BDD](../B/bdd.md)（行为驱动开发）或示例规范以创建可理解且可执行的规范。
  4. **规划[Test Data](../T/test-data.md) 管理**：考虑数据隐私和合规性要求，确保不同场景下相关[test data](../T/test-data.md) 的可用性。
  5. **设计[Test Environment](../T/test-environment.md)**：建立一个稳定的[test environment](../T/test-environment.md)，尽可能模仿生产以发现特定于环境的问题。
  6. **明智地自动化**：自动回归和高[priority](../P/priority.md) [test cases](../T/test-case.md) 以节省时间和资源。保留[manual testing](../M/manual-testing.md) 用于探索性、可用性和临时场景。
  7. **与 CI/CD 集成**：将验收测试嵌入 CI/CD 管道中，以实现应用程序的早期和频繁验证。
  8. **监控和测量**：实施监控以跟踪[test coverage](../T/test-coverage.md)、通过/失败率和缺陷密度。使用这些指标来完善测试过程。
  9. **审查和调整**：与团队定期审查[test strategy](../T/test-strategy.md)，以适应应用程序或业务优先级的变化。
  10. **利益相关者沟通**：通过清晰、简洁的报告和仪表板让利益相关者了解情况，深入了解测试进度和结果。

#### 自动化在验收测试中的作用是什么？

自动化通过根据业务需求**简化**软件验证过程，在[acceptance testing](../A/acceptance-testing.md)中发挥**关键作用**。它可以重复且一致地执行[test cases](../T/test-case.md)，确保新功能或更改不会破坏现有功能。 [acceptance testing](../A/acceptance-testing.md) 中的自动化：

- **提高效率**
    通过减少运行测试所需的时间，特别是回归测试。

- **提高准确性**
    通过最大限度地减少重复任务中的人为错误。

- **促进可扩展性**
    测试工作覆盖更多功能和场景，而无需成比例增加时间或资源。

- **支持持续集成/持续部署（CI/CD）**
    通过允许自动化验收测试成为部署管道的一部分，提供有关应用程序生产准备情况的即时反馈。

- **实现更快的反馈周期**
    向开发人员和利益相关者提供帮助，加快开发进程并提高产品质量。

- **改善资源分配**
    让人类测试人员能够专注于探索性测试和其他人类判断至关重要的领域。
  自动化验收测试通常使用高级语言或通过允许行为驱动开发 ([BDD](../B/bdd.md)) 或特定领域语言 (DSL) 的框架来编写，使它们**非技术利益相关者可以理解**并确保测试符合业务语言和用户期望。

  ```
  // Example of an automated acceptance test using a BDD framework
  Feature: User login
    Scenario: Successful login with valid credentials
      Given the login page is displayed
      When the user enters valid credentials
      And the user submits the login form
      Then the user is redirected to the dashboard
  ```通过将自动化[acceptance testing](../A/acceptance-testing.md)集成到开发工作流程中，团队可以**持续验证**软件是否符合业务需求，**降低风险**，并**缩短上市时间**。

- **提高效率**
    通过减少运行测试所需的时间，特别是回归测试。

- **提高准确性**
    通过最大限度地减少重复任务中的人为错误。

- **促进可扩展性**
    测试工作覆盖更多功能和场景，而无需成比例增加时间或资源。

- **支持持续集成/持续部署（CI/CD）**
    通过允许自动化验收测试成为部署管道的一部分，提供有关应用程序生产准备情况的即时反馈。

- **实现更快的反馈周期**
    向开发人员和利益相关者提供帮助，加快开发进程并提高产品质量。

- **改善资源分配**
    让人类测试人员能够专注于探索性测试和其他人类判断至关重要的领域。

#### 验收测试中有哪些挑战以及如何克服这些挑战？

[Acceptance testing](../A/acceptance-testing.md) 面临多项挑战，包括**需求模糊**、**环境不匹配**和**利益相关者沟通**。为了克服这些：

- **澄清需求**：与利益相关者密切合作，确保需求清晰且可测试。使用**行为驱动开发 ([BDD](../B/bdd.md))** 等技术通过示例建立共识。
  - **复制生产环境**：确保测试环境密切反映生产环境，以避免出现差异。使用**基础设施即代码 (IaC)** 自动化环境 [setup](../S/setup.md) 并保持一致性。
  - **改善利益相关者的沟通**：定期向利益相关者通报测试进展情况，并让他们参与决策过程。实施**演示会议**和**反馈循环**以确保满足他们的期望。
  - **管理[test data](../T/test-data.md)**：创建准确反映生产场景的管理和生成[test data](../T/test-data.md) 的策略。利用**数据匿名化**和**合成数据生成**工具来维护数据完整性和隐私。
  - **明智地自动化**：将自动化工作重点放在提供最大价值且容易出现人为错误的测试上。保持手动和自动测试之间的平衡，以确保全面覆盖。
  - **处理不稳定**：为[flaky tests](../F/flaky-test.md)实施**重试机制**和**根本原因分析**，以确保可靠性。使用**容器化**来提供稳定且一致的[test environments](../T/test-environment.md)。
  - **监控反馈并采取行动**：设置**监控工具**来跟踪测试结果和性能。使用这些数据不断完善和改进[acceptance testing](../A/acceptance-testing.md)流程。
  - **澄清需求**：与利益相关者密切合作，确保需求清晰且可测试。使用**行为驱动开发 ([BDD](../B/bdd.md))** 等技术通过示例建立共识。
  - **复制生产环境**：确保测试环境密切反映生产环境，以避免出现差异。使用**基础设施即代码 (IaC)** 自动化环境 [setup](../S/setup.md) 并保持一致性。
  - **改善利益相关者的沟通**：定期向利益相关者通报测试进展情况，并让他们参与决策过程。实施**演示会议**和**反馈循环**以确保满足他们的期望。
  - **管理[test data](../T/test-data.md)**：创建准确反映生产场景的管理和生成[test data](../T/test-data.md) 的策略。利用**数据匿名化**和**合成数据生成**工具来维护数据完整性和隐私。
  - **明智地自动化**：将自动化工作重点放在提供最大价值且容易出现人为错误的测试上。保持手动和自动测试之间的平衡，以确保全面覆盖。
  - **处理不稳定**：为[flaky tests](../F/flaky-test.md)实施**重试机制**和**根本原因分析**，以确保可靠性。使用**容器化**来提供稳定且一致的[test environments](../T/test-environment.md)。
  - **监控反馈并采取行动**：设置**监控工具**来跟踪测试结果和性能。使用这些数据不断完善和改进[acceptance testing](../A/acceptance-testing.md)流程。

#### 如何将验收测试集成到持续交付管道中？

将[acceptance testing](../A/acceptance-testing.md) 集成到**持续交付 (CD) 管道**可确保新功能满足业务需求并准备好进行生产发布。为此，请按照下列步骤操作：

1. **自动化验收测试**：编写与用户故事或要求一致的自动化验收测试。使用像 Cucumber 这样的行为驱动开发 ([BDD](../B/bdd.md)) 框架来创建可读的场景。
  2. **版本控制**：将验收测试与应用程序代码一起存储在版本控制系统中，以保持 [test cases](../T/test-case.md) 与其涵盖的功能之间的同步。
  3. **持续集成服务器**：配置 CI 服务器（例如 Jenkins、CircleCI）以触发验收测试作为管道的一部分。这应该在单元和集成测试通过之后发生，以确保只有高质量的代码才能进行。
  4. **[Test Environment](../T/test-environment.md)**：设置一个模拟生产的专用[test environment](../T/test-environment.md)。使用 Terraform 或 Ansible 等基础设施即代码 (IaC) 工具来实现一致性和可重复性。
  5. **并行执行**：并行运行测试以减少执行时间。使用 Docker 或 Kubernetes 进行容器化可以帮助管理和扩展[test environments](../T/test-environment.md)。
  6. **把关**：在管道中实现把关机制。仅当验收测试通过时才允许更改进入下一阶段，以确保失败的代码不会进入生产环境。
  7. **反馈循环**：当测试失败时向开发人员提供立即反馈。将 [test reports](../T/test-report.md) 与 Slack 或电子邮件等通信工具集成。
  8. **持续监控**：持续监控[test suite](../T/test-suite.md)的健康状况。删除[flaky tests](../F/flaky-test.md)并更新测试以反映用户需求的变化。
  9. **部署决策**：使用测试结果做出有关部署的明智决策。自动部署通过验收标准的代码。
  通过将 [acceptance testing](../A/acceptance-testing.md) 嵌入到 CD 管道中，您可以确保每个更改在到达最终用户之前都根据预期的业务功能进行评估，从而保持高质量标准并降低生产问题的风险。

1. **自动化验收测试**：编写与用户故事或要求一致的自动化验收测试。使用像 Cucumber 这样的行为驱动开发 ([BDD](../B/bdd.md)) 框架来创建可读的场景。
  2. **版本控制**：将验收测试与应用程序代码一起存储在版本控制系统中，以保持 [test cases](../T/test-case.md) 与其所涵盖的功能之间的同步。
  3. **持续集成服务器**：配置 CI 服务器（例如 Jenkins、CircleCI）以触发验收测试作为管道的一部分。这应该在单元和集成测试通过之后发生，以确保只有高质量的代码才能进行。
  4. **[Test Environment](../T/test-environment.md)**：设置一个模拟生产的专用[test environment](../T/test-environment.md)。使用 Terraform 或 Ansible 等基础设施即代码 (IaC) 工具来实现一致性和可重复性。
  5. **并行执行**：并行运行测试以减少执行时间。使用 Docker 或 Kubernetes 进行容器化可以帮助管理和扩展[test environments](../T/test-environment.md)。
  6. **把关**：在管道中实现把关机制。仅当验收测试通过时才允许更改进入下一阶段，以确保失败的代码不会进入生产环境。
  7. **反馈循环**：当测试失败时向开发人员提供立即反馈。将 [test reports](../T/test-report.md) 与 Slack 或电子邮件等通信工具集成。
  8. **持续监控**：持续监控[test suite](../T/test-suite.md)的健康状况。删除[flaky tests](../F/flaky-test.md)并更新测试以反映用户需求的变化。
  9. **部署决策**：使用测试结果做出有关部署的明智决策。自动部署通过验收标准的代码。

### 工具和技术

#### 验收测试常用哪些工具？

[acceptance testing](../A/acceptance-testing.md) 的常用工具包括：

- **Cucumber** ：支持具有简单语言规范的行为驱动开发（BDD）。
  - **[Selenium](../S/selenium.md)** ：自动化浏览器，支持 Web 应用程序测试。
  - **SpecFlow**：通过将业务可读的行为规范绑定到底层实现，弥合领域专家和开发人员之间的沟通差距。
  - **FitNesse**：基于 wiki 的框架，允许用户在表格和可执行规范中定义测试。
  - **机器人框架**：一种关键字驱动的验收测试方法，对于非程序员来说很容易使用。
  - **JBehave**：BDD 框架，允许将故事编写为文档的一部分。
  - **TestComplete** ：为 Web、移动和桌面测试提供一套全面的功能。
  - **UFT（统一[Functional Testing](../F/functional-testing.md)）**：广泛使用的功能和回归测试工具，支持关键字和脚本接口。
  - **[Postman](../P/postman.md)** ：简化 API 测试，允许用户创建和共享测试套件。
  - **SoapUI**：用于测试 SOAP 和 REST Web 服务的工具。
  这些工具有助于根据业务需求验证软件，通常通过模拟用户行为的自动化 [test cases](../T/test-case.md) 或 [API](../A/api.md) 调用来确保系统满足商定的标准。它们可以集成到 CI/CD 管道中以进行持续验证，并支持各种编程语言和平台。每个工具都有其独特的功能，可能更适合某些场景或类型的应用程序。选择正确的工具取决于项目的具体需求，例如[test cases](../T/test-case.md)的复杂性、技术堆栈和团队的专业知识。

- **Cucumber** ：支持具有简单语言规范的行为驱动开发（BDD）。
  - **[Selenium](../S/selenium.md)** ：自动化浏览器，支持 Web 应用程序测试。
  - **SpecFlow**：通过将业务可读的行为规范绑定到底层实现，弥合领域专家和开发人员之间的沟通差距。
  - **FitNesse**：基于 wiki 的框架，允许用户在表格和可执行规范中定义测试。
  - **机器人框架**：一种关键字驱动的验收测试方法，对于非程序员来说很容易使用。
  - **JBehave**：BDD 框架，允许将故事编写为文档的一部分。
  - **TestComplete** ：为 Web、移动和桌面测试提供一套全面的功能。
  - **UFT（统一[Functional Testing](../F/functional-testing.md)）**：广泛使用的功能和回归测试工具，支持关键字和脚本接口。
  - **[Postman](../P/postman.md)** ：简化 API 测试，允许用户创建和共享测试套件。
  - **SoapUI**：用于测试 SOAP 和 REST Web 服务的工具。

#### 这些工具在验收测试过程中有何帮助？

[Test automation](../T/test-automation.md) 工具通过启用[test cases](../T/test-case.md) 的执行来简化[acceptance testing](../A/acceptance-testing.md) 流程，根据业务需求验证软件。这些工具**减少了重复[manual testing](../M/manual-testing.md)所需的时间和精力**，确保始终满足验收标准。
  通过自动化[test cases](../T/test-case.md)，团队可以快速识别回归和缺陷，从而实现**快速反馈**和纠正。这在频繁[iterations](../I/iteration.md) 和部署很常见的敏捷和 DevOps 环境中特别有用。持续集成 (CI) 管道可以触发自动验收测试，确保在部署之前根据用户验收标准审查新更改。
  此外，自动化工具支持**数据驱动测试**，允许测试人员轻松输入各种数据集来验证不同场景下的应用程序行为。这增强了[test coverage](../T/test-coverage.md) 和[acceptance testing](../A/acceptance-testing.md) 的可靠性。
  自动化测试还提供已测试内容的**清晰文档**，作为验收标准的活生生的工件。这种透明度有助于保持利益相关者、开发人员和测试人员之间的一致性。
  此外，这些工具通常具有**报告功能**，可以提供对测试结果的深入了解，从而更轻松地向所有感兴趣的各方传达产品的状态。
  总而言之，[test automation](../T/test-automation.md) 工具通过确保[test cases](../T/test-case.md) 的一致执行、提供有关软件质量的快速反馈、增强[test coverage](../T/test-coverage.md) 以及提供清晰的测试结果文档和报告来帮助[acceptance testing](../A/acceptance-testing.md)。

#### 不同验收测试工具的优缺点是什么？

[Acceptance testing](../A/acceptance-testing.md) 工具在功能、易用性和集成能力方面各不相同。以下是它们的优缺点的简要比较：
  **黄瓜**：

- **优点**：促进行为驱动开发（BDD），使用简单语言（Gherkin），与各种框架良好集成。
  - **缺点**：需要很好地理解 BDD，可能需要针对复杂的测试场景进行额外的设置。
  **[Selenium](../S/selenium.md)**：

- **优点**：支持多种浏览器和语言，拥有庞大的用户社区，并且高度灵活。
  - **缺点**：设置可能很复杂，由于浏览器自动化而执行速度较慢，可能需要额外的 API 测试工具。
  **健身**：

- **优点**：结合 wiki 进行文档记录和测试执行，有利于利益相关者之间的协作。
  - **缺点**：学习曲线陡峭，用户界面不够现代，可能无法很好地适应大型项目。
  **规格流程**：

- **优点**：与.NET集成，支持BDD，允许用自然语言编写测试。
  - **缺点**：主要针对.NET 项目，需要了解 BDD 原理。
  **机器人框架**：

- **优点**：关键字驱动，支持BDD，有许多针对不同应用程序的库。
  - **缺点**：语法对于开发人员来说可能不太直观，可能需要额外的 Python 知识。
  **测试咖啡馆**：

- **优点**：不需要 WebDriver，测试可以在所有流行的浏览器上运行，易于设置。
  - **缺点**：与 Selenium 相比不太成熟，集成可能较少。
  **UFT（统一[Functional Testing](../F/functional-testing.md)）**：

- **优点**：支持广泛的应用程序，包括强大的 IDE、广泛的对象识别。
  - **缺点**：昂贵，不太适合敏捷和持续集成环境。
  每种工具都有其优点和缺点，最佳选择取决于项目要求、团队专业知识和所使用的具体技术。

- **优点**：促进行为驱动开发（BDD），使用简单语言（Gherkin），与各种框架良好集成。
  - **缺点**：需要很好地理解 BDD，可能需要针对复杂的测试场景进行额外的设置。
  - **优点**：支持多种浏览器和语言，拥有庞大的用户社区，并且高度灵活。
  - **缺点**：设置可能很复杂，由于浏览器自动化而执行速度较慢，可能需要额外的 API 测试工具。
  - **优点**：结合 wiki 进行文档记录和测试执行，有利于利益相关者之间的协作。
  - **缺点**：学习曲线陡峭，用户界面不够现代，可能无法很好地适应大型项目。
  - **优点**：与.NET集成，支持BDD，允许用自然语言编写测试。
  - **缺点**：主要针对.NET 项目，需要了解 BDD 原理。
  - **优点**：关键字驱动，支持BDD，有许多针对不同应用程序的库。
  - **缺点**：语法对于开发人员来说可能不太直观，可能需要额外的 Python 知识。
  - **优点**：不需要 WebDriver，测试可以在所有流行的浏览器上运行，易于设置。
  - **缺点**：与 Selenium 相比不太成熟，集成可能较少。
  - **优点**：支持广泛的应用程序，包括强大的 IDE、广泛的对象识别。
  - **缺点**：昂贵，不太适合敏捷和持续集成环境。

#### API 在验收测试中的作用是什么？

[APIs](../A/api.md) 通过充当应用程序逻辑的**接口**，在[acceptance testing](../A/acceptance-testing.md) 中发挥**关键作用**。它们允许测试人员**验证**被测系统的行为，而无需用户界面。这对于 UI 可能不可用或完全开发的 **后端服务** 特别有用。
  使用[APIs](../A/api.md)，验收测试可以**验证**：

- 系统
    **反应正确**
    到给定的输入。

- **业务规则**
    都遵守。

- **集成**
    其他服务按预期运行。

- 系统
    **性能**
    满足所需的基准。
  [APIs](../A/api.md) 能够创建**可靠**、**可重复**并且可以快速执行的**自动验收测试**。它们促进开发周期中的**早期测试**，通常作为**持续集成/持续交付（CI/CD）**管道的一部分。
  此外，[APIs](../A/api.md) 提供了一定程度的**抽象**，允许在不依赖可能会频繁更改的 UI 的情况下测试系统。这导致**更稳定**和**可维护**验收测试。

  ```
  // Example of an API-based acceptance test in pseudo-code
  const response = await apiClient.createOrder(orderDetails);
  assert(response.status, 201);
  assert(response.data.orderId, expectedOrderId);
  ```总之，[APIs](../A/api.md) 是[acceptance testing](../A/acceptance-testing.md) 不可或缺的一部分，可以对系统的功能和性能进行**高效**、**早期**和**集中**的验证。

- 系统
    **反应正确**
    到给定的输入。

- **业务规则**
    都遵守。

- **集成**
    其他服务按预期运行。

- 系统
    **性能**
    满足所需的基准。

#### 如何在验收测试中利用云技术？

在[acceptance testing](../A/acceptance-testing.md) 中利用**云技术**具有多种优势。云平台按需提供**可扩展资源**，允许团队通过动态配置必要的基础设施来模拟现实世界的流量和使用模式。这对于[acceptance testing](../A/acceptance-testing.md) 的**性能和[load testing](../L/load-testing.md)** 方面特别有用。
  使用云服务，[test environments](../T/test-environment.md) 可以**快速且一致地复制**，确保验收测试在稳定且受控的环境中运行。这对于维护 [acceptance testing](../A/acceptance-testing.md) 进程的完整性至关重要。基于云的工具通常带有**内置分析和监控**，可用于在验收测试期间深入了解应用程序性能和用户体验。
  **持续集成/持续部署 (CI/CD) 管道**可以通过云服务进行增强，以在各种环境（包括类似生产的临时区域）中自动部署和运行验收测试。这种集成确保[acceptance testing](../A/acceptance-testing.md) 是交付过程的无缝部分。
  此外，云平台通常提供**全球数据中心**，这意味着可以在更靠近最终用户位置的位置执行验收测试，从而在延迟和用户体验方面提供更准确的结果。
  团队还可以从**成本节省**中受益，因为云服务通常遵循即用即付模式，这意味着您只需为测试阶段使用的资源付费。
  总之，云技术促进了更**高效、可扩展和现实的** [acceptance testing](../A/acceptance-testing.md) 流程，这可以带来更可靠和以用户为中心的最终产品。

### 最佳实践

#### 验收测试的最佳实践有哪些？

[acceptance testing](../A/acceptance-testing.md) 的最佳实践包括：

- **定义明确的验收标准**：与利益相关者合作建立明确的、可衡量的标准，功能必须满足这些标准才能被接受。
  - **与跨职能团队协作**：确保开发人员、测试人员和业务分析师一起工作以了解需求和结果。
  - **优先考虑用户体验**：专注于现实世界的使用场景，以验证端到端工作流程和用户满意度。
  - **保持测试可维护**：编写易于理解并随着应用程序发展而更新的测试。
  - **在适当的情况下自动化**：使用自动化来执行重复、耗时的测试，但请记住，某些探索性测试可能需要手动方法。
  - **使用类似生产的数据进行测试**：使用密切模仿生产的数据来确保测试真实并涵盖边缘情况。
  - **执行[regression testing](../R/regression-testing.md)** ：通过在验收套件中包含回归测试，确保新更改不会破坏现有功能。
  - **监控性能和安全性**：将性能和安全检查作为验收标准的一部分。
  - **对测试工件使用版本控制**：将测试用例、脚本和数据存储在版本控制系统中，以跟踪更改并有效协作。
  - **持续完善流程**：定期审查和调整您的测试流程，以解决效率低下的问题并纳入新的最佳实践。
  通过遵守这些实践，您可以确保 [acceptance testing](../A/acceptance-testing.md) 有效、高效，并符合利益相关者和最终用户的期望。

- **定义明确的验收标准**：与利益相关者合作建立明确的、可衡量的标准，功能必须满足这些标准才能被接受。
  - **与跨职能团队协作**：确保开发人员、测试人员和业务分析师一起工作以了解需求和结果。
  - **优先考虑用户体验**：专注于现实世界的使用场景，以验证端到端工作流程和用户满意度。
  - **保持测试可维护**：编写易于理解并随着应用程序发展而更新的测试。
  - **在适当的情况下自动化**：使用自动化来执行重复、耗时的测试，但请记住，某些探索性测试可能需要手动方法。
  - **使用类似生产的数据进行测试**：使用密切模仿生产的数据来确保测试真实并涵盖边缘情况。
  - **执行[regression testing](../R/regression-testing.md)** ：通过在验收套件中包含回归测试，确保新更改不会破坏现有功能。
  - **监控性能和安全性**：将性能和安全检查作为验收标准的一部分。
  - **对测试工件使用版本控制**：将测试用例、脚本和数据存储在版本控制系统中，以跟踪更改并有效协作。
  - **持续完善流程**：定期审查和调整您的测试流程，以解决效率低下的问题并纳入新的最佳实践。

#### 如何随着时间的推移维护和更新验收测试？

随着时间的推移维护和更新验收测试需要**结构化方法**以确保它们保持相关性和有效性：

- **定期审查[Test Cases](../T/test-case.md)**：安排定期审查验收测试，使其与应用程序中的新功能、要求和更改保持一致。
  - **重构测试**：通过重构测试以提高可读性、效率和[maintainability](../M/maintainability.md)，保持测试代码库干净。消除冗余并确保测试是模块化的。
  - **版本控制**：使用版本控制系统跟踪[test scripts](../T/test-script.md)中的更改，必要时可以回滚到以前的版本。
  - **[Test Data](../T/test-data.md) 管理**：有效管理[test data](../T/test-data.md)，确保其是最新的并代表生产数据。
  - **尽可能自动化**：使用可以修改[test cases](../T/test-case.md)或数据的脚本或工具，自动执行受重复更改影响的测试的更新过程。
  - **与利益相关者合作**：与开发人员、业务分析师和产品负责人密切合作，了解变更及其对验收标准的影响。
  - **持续集成**：将验收测试集成到 CI/CD 管道中，以确保每次构建时都执行它们，尽早发现问题。
  - **监控和警报**：对[test suite](../T/test-suite.md)实施监控，以检测由于应用程序更改而导致的不稳定或故障，并发出警报以立即采取行动。
  - **文档**：使 [test case](../T/test-case.md) 文档保持最新，以反映应用程序和测试的当前状态。
  - **反馈循环**：与团队建立反馈循环，讨论验收测试的有效性和潜在的改进。
  通过遵循这些实践，可以有效地维护和更新验收测试，确保它们继续提供价值并满足软件开发生命周期不断变化的需求。

- **定期审查[Test Cases](../T/test-case.md)**：安排定期审查验收测试，使其与应用程序中的新功能、要求和更改保持一致。
  - **重构测试**：通过重构测试以提高可读性、效率和[maintainability](../M/maintainability.md)，保持测试代码库干净。消除冗余并确保测试是模块化的。
  - **版本控制**：使用版本控制系统跟踪[test scripts](../T/test-script.md)中的更改，必要时可以回滚到以前的版本。
  - **[Test Data](../T/test-data.md) 管理**：有效管理[test data](../T/test-data.md)，确保其是最新的并代表生产数据。
  - **尽可能自动化**：使用可以修改 [test cases](../T/test-case.md) 或数据的脚本或工具，自动执行受重复更改影响的测试的更新过程。
  - **与利益相关者合作**：与开发人员、业务分析师和产品负责人密切合作，了解变更及其对验收标准的影响。
  - **持续集成**：将验收测试集成到 CI/CD 管道中，以确保每次构建时都执行它们，尽早发现问题。
  - **监控和警报**：对[test suite](../T/test-suite.md)实施监控，以检测由于应用程序更改而导致的不稳定或故障，并发出警报以立即采取行动。
  - **文档**：使 [test case](../T/test-case.md) 文档保持最新，以反映应用程序和测试的当前状态。
  - **反馈循环**：与团队建立反馈循环，讨论验收测试的有效性和潜在的改进。

#### 文档在验收测试中的作用是什么？

文档在[acceptance testing](../A/acceptance-testing.md) 中发挥着**关键作用**，作为理解、执行和评估测试标准的基础。它包括 **验收 [Test Plan](../T/test-plan.md) (ATP)**、**[test cases](../T/test-case.md)** 和 **[test scenarios](../T/test-scenario.md)**，概述了最终用户或客户认为系统可接受的条件。
  **[Test cases](../T/test-case.md)** 源自**需求文档**，对于确保应用程序的所有功能和非功能方面都得到验证至关重要。它们提供了测试条件、[expected results](../E/expected-result.md) 和验收标准的逐步描述。
  **可追溯性矩阵**将需求与其相应的测试联系起来，确保覆盖范围并帮助识别测试过程中的任何差距。这对于维护 [acceptance testing](../A/acceptance-testing.md) 阶段的完整性至关重要。
  **[Test reports](../T/test-report.md)** 记录验收测试的结果，包括发现的任何缺陷或问题。这些报告对于利益相关者就软件的生产准备情况做出明智的决策至关重要。
  总之，[acceptance testing](../A/acceptance-testing.md) 中的文档可确保：

- 明确要测试的内容以及成功的要素。
  - 测试执行的一致性。
  - 通过测试对需求的可追溯性来承担责任。
  - 向利益相关者有效传达测试结果和发现。
  适当的文档对于透明、高效和成功的[acceptance testing](../A/acceptance-testing.md) 流程是必不可少的。

- 明确要测试的内容以及成功的要素。
  - 测试执行的一致性。
  - 通过测试对需求的可追溯性来承担责任。
  - 向利益相关者有效传达测试结果和发现。

#### 如何使验收测试更加高效？

为了提高[acceptance testing](../A/acceptance-testing.md)的效率：

- **优先考虑[test cases](../T/test-case.md)**
    基于风险和业务影响。专注于直接影响用户体验的关键功能。

- 实施
    **[test data](../T/test-data.md) 管理**
    确保相关且高质量的数据可用于测试场景的实践。

- 利用
    **行为驱动开发 ([BDD](../B/bdd.md))**
    像 Cucumber 这样的框架可以创建兼作自动化测试的可读规范。

- **并行化测试**
    以减少执行时间。像 Selenium Grid 这样的工具可以在不同的环境中同时运行多个测试。

- **重复使用测试组件**
    并遵循 DRY（不要重复自己）原则，以最大限度地减少维护并提高一致性。

- **模拟外部依赖项**
    隔离被测系统并减少外部系统的不可预测性。

- **优化[test environment](../T/test-environment.md) [setup](../S/setup.md)**
    使用 Docker 等容器化工具快速启动一致的测试环境。

- **定期审查和重构测试**
    消除冗余并确保它们符合当前要求。

- **监控和分析测试结果**
    使用仪表板和报告工具快速识别和解决故障。

- **与利益相关者密切合作**
    确保验收标准明确并收集有关测试覆盖范围和结果的反馈。
  通过实施这些实践，您可以简化 [acceptance testing](../A/acceptance-testing.md) 流程、减少执行时间并维护高质量的[test suites](../T/test-suite.md)，从而为开发生命周期提供有价值的反馈。

- **优先考虑[test cases](../T/test-case.md)**
    基于风险和业务影响。专注于直接影响用户体验的关键功能。

- 实施
    **[test data](../T/test-data.md) 管理**
    确保相关且高质量的数据可用于测试场景的实践。

- 利用
    **行为驱动开发 ([BDD](../B/bdd.md))**
    像 Cucumber 这样的框架可以创建兼作自动化测试的可读规范。

- **并行化测试**
    以减少执行时间。像 Selenium Grid 这样的工具可以在不同的环境中同时运行多个测试。

- **重复使用测试组件**
    并遵循 DRY（不要重复自己）原则，以最大限度地减少维护并提高一致性。

- **模拟外部依赖项**
    隔离被测系统并减少外部系统的不可预测性。

- **优化[test environment](../T/test-environment.md) [setup](../S/setup.md)**
    使用 Docker 等容器化工具快速启动一致的测试环境。

- **定期审查和重构测试**
    消除冗余并确保它们符合当前要求。

- **监控和分析测试结果**
    使用仪表板和报告工具快速识别和解决故障。

- **与利益相关者密切合作**
    确保验收标准明确并收集有关测试覆盖范围和结果的反馈。

#### 如何有效传达验收测试的结果？

有效传达[acceptance testing](../A/acceptance-testing.md) 的结果涉及清晰、简洁且可操作的报告。使用**仪表板**提供实时状态更新，突出显示**通过/失败率**、**[test coverage](../T/test-coverage.md)** 和 **缺陷**。使用图表和图形等**视觉辅助工具**来快速理解。
  合并执行后生成的**自动报告**，确保它们包含必要的详细信息，例如 **[test case](../T/test-case.md) 描述**、**预期结果**、**[actual results](../A/actual-result.md)** 和 **[test execution](../T/test-execution.md)** 的证据（屏幕截图、日志）。为不同的利益相关者定制报告——为管理层提供摘要报告，为开发人员提供详细日志。
  当测试失败时，利用**通知系统**立即提醒团队。将这些通知集成到已使用的工具中，例如 Slack 或电子邮件。
  为了提高透明度和协作性，请使用[JIRA](../J/jira.md) 等**问题跟踪系统**来记录缺陷，将它们直接链接到失败的验收测试。这有利于可追溯性和优先级排序。
  确保所有相关方都可以访问**测试结果（可能通过共享存储库或基于网络的平台）。定期在团队会议中**审查测试结果**，讨论失败、[flaky tests](../F/flaky-test.md) 以及后续步骤。
  最后，维护一个随项目一起发展的**动态文档**或 wiki，从验收测试中获取见解和决策。这既可以作为历史记录，也可以作为未来参考的知识库。

  ```
  - **Dashboards** for real-time updates
  - **Automated reports** with essential details
  - **Visual aids** like charts and graphs
  - **Notification systems** for immediate alerts
  - **Issue tracking systems** for defect management
  - **Accessible test results** for all stakeholders
  - **Regular reviews** in team meetings
  - **Living document** for historical insights
  ```
