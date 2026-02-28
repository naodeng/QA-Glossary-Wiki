# 自下而上的集成

<!-- TOC START -->
- [相关术语：](#相关术语：)
- [关于自下而上集成的问题吗？](#关于自下而上集成的问题吗？)
  - [基础知识和重要性](#基础知识和重要性)
    - [什么是自下而上集成？](#什么是自下而上集成？)
    - [为什么自下而上的集成在软件测试中很重要？](#为什么自下而上的集成在软件测试中很重要？)
    - [自下而上集成的关键原则是什么？](#自下而上集成的关键原则是什么？)
    - [自下而上的集成与自上而下的集成有何不同？](#自下而上的集成与自上而下的集成有何不同？)
    - [在软件开发过程中如何实现自下而上的集成？](#在软件开发过程中如何实现自下而上的集成？)
    - [自下而上集成涉及哪些步骤？](#自下而上集成涉及哪些步骤？)
    - [实施自下而上集成有哪些挑战以及如何克服这些挑战？](#实施自下而上集成有哪些挑战以及如何克服这些挑战？)
    - [您能否提供一个自下而上集成的实际示例？](#您能否提供一个自下而上集成的实际示例？)
  - [测试](#测试)
    - [自下而上集成中的测试是如何进行的？](#自下而上集成中的测试是如何进行的？)
    - [自下而上集成中通常使用哪些类型的测试？](#自下而上集成中通常使用哪些类型的测试？)
    - [自下而上的集成如何影响整个测试过程？](#自下而上的集成如何影响整个测试过程？)
    - [测试工具在自下而上的集成中扮演什么角色？](#测试工具在自下而上的集成中扮演什么角色？)
    - [如何有效地设计测试用例以实现自下而上的集成？](#如何有效地设计测试用例以实现自下而上的集成？)
  - [高级概念](#高级概念)
    - [自下而上的集成与敏捷或 DevOps 等其他软件开发方法有何关系？](#自下而上的集成与敏捷或-devops-等其他软件开发方法有何关系？)
    - [持续集成在自下而上集成中的作用是什么？](#持续集成在自下而上集成中的作用是什么？)
    - [自下而上的集成如何运用在微服务架构中？](#自下而上的集成如何运用在微服务架构中？)
    - [自下而上集成的最佳实践是什么？](#自下而上集成的最佳实践是什么？)
    - [自下而上的集成如何提高软件质量和可靠性？](#自下而上的集成如何提高软件质量和可靠性？)
<!-- TOC END -->

自下而上的集成测试

首先测试较低级别的模块，然后将它们与较高级别的模块集成并测试。在此过程中，可以使用“驱动程序”来协助测试。

## 相关术语：

- [Top-Down Integration](../T/top-down-integration.md)

## 关于自下而上集成的问题吗？

### 基础知识和重要性

#### 什么是自下而上集成？

[Bottom-up integration](../B/bottom-up-integration.md) 是一种**测试方法**，首先测试应用程序的最低级别（例如单个功能或模块），然后将它们集成到更高级别的组合中，并最终集成到完整的系统中。此方法依赖于使用**测试驱动程序**来模拟可能尚未开发或测试的更高级别模块。
  在实践中，开发人员首先为最小的代码单元编写单元测试，然后逐渐集成这些单元以形成更大的组件。每个集成组件都经过功能测试，此过程将持续进行，直到整个系统完成集成和验证。
  [bottom-up integration](../B/bottom-up-integration.md) 的常用工具集包括 [unit testing](../U/unit-testing.md) 框架（例如 JUnit for Java 或 PyTest for Python）以及模拟对象或存根来模拟更高级别模块的行为。 [Test cases](../T/test-case.md) 应重点关注集成单元之间的接口，以确保正确的通信和数据流。
  [Bottom-up integration](../B/bottom-up-integration.md) 在系统的较低级别组件稳定且定义明确的情况下特别有效。它允许及早检测单元级别的缺陷，与开发周期后期发现的缺陷相比，修复这些缺陷更具成本效益。然而，它可能会将系统整体功能和用户界面的测试推迟到集成过程的后期阶段。
  在**持续集成**环境中，[bottom-up integration](../B/bottom-up-integration.md) 可以在提交新代码时自动频繁运行单元测试，确保更改不会破坏现有功能。

#### 为什么自下而上的集成在软件测试中很重要？

[Bottom-up integration](../B/bottom-up-integration.md) 在[software testing](../S/software-testing.md) 中至关重要，因为它允许在开发或测试高级组件之前**早期测试低级组件**及其交互。这种方法有助于在**组件级别**问题升级为更复杂的系统范围问题之前识别它们。通过首先关注应用程序的**构建块**，开发人员和测试人员可以确保每个部分都能独立正常运行，从而简化与系统其他部分集成时的调试过程。
  此外，[bottom-up integration](../B/bottom-up-integration.md) 支持创建 **[test stubs](../T/test-stub.md)** 和 **驱动程序**，这对于模拟尚未开发的更高级别模块的行为至关重要。这实现了**连续测试环境**，可以在其中独立验证组件，从而促进更加**模块化和可扩展**的测试方法。
  在 **[test automation](../T/test-automation.md)** 的上下文中，[bottom-up integration](../B/bottom-up-integration.md) 与各个模块的 **单元测试** 和 **集成测试** 的开发非常一致。随着新组件的开发，可以逐步构建自动化测试，从而允许在进行更改时有效地执行**[regression testing](../R/regression-testing.md)**。
  [bottom-up integration](../B/bottom-up-integration.md) 的重要性还体现在它对 **[software quality](../S/software-quality.md) 和可靠性** 的贡献。通过确保每个组件在集成之前都经过彻底测试，最终产品出现缺陷的可能性会大大降低。这种方法在复杂系统中或使用**微服务架构**时特别有用，其中服务是独立开发和部署的。

#### 自下而上集成的关键原则是什么？

**[bottom-up integration](../B/bottom-up-integration.md)** 的关键原则侧重于从**基本单元向上**构建系统。它从**最低级别模块**的集成开始，然后是依赖于这些模块的较高级别模块。以下是原则：

- **首先测试低级组件**：开始使用最基本的代码单元进行测试，以确保它们在与更高级别的组件集成之前正常工作。
  - **[Incremental Testing](../I/incremental-testing.md)** ：一次集成和测试一个组件，这有助于隔离错误并简化调试。
  - **使用测试驱动程序**：使用测试驱动程序来模拟尚未开发或集成的高级模块。
  - **早期原型**：允许早期部分系统原型，为早期评估提供有形产品。
  - **存根替换**：随着集成的升级，用实际组件替换存根（在自上而下的集成中使用）。
  - **[Regression Testing](../R/regression-testing.md)** ：在每个集成步骤之后，执行回归测试以确保新的更改不会破坏现有功能。
  - **持续集成**：当新组件可用时持续集成，这与敏捷和 DevOps 实践保持一致。
  实际上，[bottom-up integration](../B/bottom-up-integration.md) 需要 **[test harness](../T/test-harness.md)** 来协调测试驱动程序并管理[test cases](../T/test-case.md)。这对于独立开发服务的**微服务架构**至关重要。有效的[test case](../T/test-case.md) 设计应针对集成组件之间的接口。持续集成工具可以自动化构建和[test process](../T/test-process.md)，从而强化自下而上的方法。最佳实践包括维护**干净的代码库**、**自动化回归测试**和**频繁集成**以最大程度地减少集成问题。

- **首先测试低级组件**：开始使用最基本的代码单元进行测试，以确保它们在与更高级别的组件集成之前正常工作。
  - **[Incremental Testing](../I/incremental-testing.md)** ：一次集成和测试一个组件，这有助于隔离错误并简化调试。
  - **使用测试驱动程序**：使用测试驱动程序来模拟尚未开发或集成的高级模块。
  - **早期原型**：允许早期部分系统原型，为早期评估提供有形产品。
  - **存根替换**：随着集成的升级，用实际组件替换存根（在自上而下的集成中使用）。
  - **[Regression Testing](../R/regression-testing.md)** ：在每个集成步骤之后，执行回归测试以确保新的更改不会破坏现有功能。
  - **持续集成**：当新组件可用时持续集成，这与敏捷和 DevOps 实践保持一致。

#### 自下而上的集成与自上而下的集成有何不同？

[Bottom-up integration](../B/bottom-up-integration.md) 和[top-down integration](../T/top-down-integration.md) 是[software testing](../S/software-testing.md) 的两种相反的方法。
  **[Bottom-up integration](../B/bottom-up-integration.md)** 从[unit testing](../U/unit-testing.md) 最低级别的模块开始，逐渐向上至较高级别的模块，从控制流的底部向上进行集成。通常不需要测试驱动程序，但很少使用[test stubs](../T/test-stub.md)，因为重点是从最低级别向上进行集成。
  相比之下，**[top-down integration](../T/top-down-integration.md)** 从顶层模块开始，逐步向下集成。这种方法需要使用[test stubs](../T/test-stub.md)来模拟尚未集成或开发的较低级别模块。
  主要区别在于整合过程的**起点**和**方向**。自下而上有利于对基本组件进行早期测试，而自上而下则强调对整个系统功能的早期测试。自下而上可以在继续之前展示较低级别的可靠性，而自上而下可以在流程的早期向利益相关者提供系统的工作框架。
  在实践中，这些方法可以结合在**三明治/混合集成**中，利用两者的优势来实现更全面、更高效的测试过程。这种方法同时集成了一些高层模块和低层模块，允许并行开发和测试。

#### 自下而上集成的优点和缺点是什么？

[Bottom-Up Integration](../B/bottom-up-integration.md)的优点：

- **低级组件的早期测试**：允许在进入更高级别的模块之前验证基本实用程序和服务功能。
  - **并行开发**：团队可以同时处理不同的模块，从而可能加快开发周期。
  - **早期原型**：有利于在流程的早期创建工作系统，这对于演示或进一步开发非常有用。
  - **故障定位**：由于高级模块尚未集成，因此更容易查明测试的较低级别模块内的缺陷。
  - **可重用代码**：鼓励创建可以独立测试的可重用模块。
  [Bottom-Up Integration](../B/bottom-up-integration.md) 的缺点：

- **延迟系统功能测试**：高级功能通常对用户最可见，在开发周期的后期进行测试。
  - **[Test Stubs](../T/test-stub.md)** ：可能需要开发测试驱动程序或存根来模拟更高级别的模块，这可能非常耗时并且需要额外的资源。
  - **集成复杂性**：随着添加更多模块，集成的复杂性可能会增加，可能导致管理依赖项的困难。
  - **有限的早期反馈**：利益相关者可能需要等待更长的时间才能看到系统的完整功能，这可能会延迟对系统范围问题的反馈。
  - **冗余测试的潜力**：如果不仔细管理，当模块集成到更大的系统中时，可能会出现冗余测试。
  - **低级组件的早期测试**：允许在进入更高级别的模块之前验证基本实用程序和服务功能。
  - **并行开发**：团队可以同时处理不同的模块，从而可能加快开发周期。
  - **早期原型**：有利于在流程的早期创建工作系统，这对于演示或进一步开发非常有用。
  - **故障定位**：由于高级模块尚未集成，因此更容易查明测试的较低级别模块内的缺陷。
  - **可重用代码**：鼓励创建可以独立测试的可重用模块。
  - **延迟系统功能测试**：高级功能通常对用户最可见，在开发周期的后期进行测试。
  - **[Test Stubs](../T/test-stub.md)** ：可能需要开发测试驱动程序或存根来模拟更高级别的模块，这可能非常耗时并且需要额外的资源。
  - **集成复杂性**：随着添加更多模块，集成的复杂性可能会增加，可能导致管理依赖项的困难。
  - **有限的早期反馈**：利益相关者可能需要等待更长的时间才能看到系统的完整功能，这可能会延迟对系统范围问题的反馈。
  - **冗余测试的潜力**：如果不仔细管理，当模块集成到更大的系统中时，可能会出现冗余测试。

＃＃＃ 执行

#### 在软件开发过程中如何实现自下而上的集成？

[Bottom-up integration](../B/bottom-up-integration.md) 在软件开发过程中实现，首先侧重于**低级单元**的测试**，例如函数、过程或类，然后逐步将它们集成到执行特定任务的集群或**子系统**中。一旦这些子系统得到验证，它们就会被组合起来形成应用程序的更大组件。
  在实现过程中，通常不需要**[test stubs](../T/test-stub.md)**，因为测试从层次结构底部的实际组件开始。但是，**测试驱动程序**可用于模拟尚未开发或集成的更高级别的模块。
  该过程涉及：

1. **[Unit Testing](../U/unit-testing.md)** ：对各个单元进行功能测试。
  2. **子系统集成**：将单元组合成子系统，然后进行测试。
  3. **子系统测试**：确保子系统内的集成单元正确协同工作。
  4. **系统集成**：子系统集成以形成完整的系统。
  5. **[System Testing](../S/system-testing.md)** ：整个系统经过测试是否符合要求。
  开发人员或测试工程师编写特定于单元和子系统功能的**[test cases](../T/test-case.md)**。这些 [test cases](../T/test-case.md) 使用自动化工具执行，例如 JUnit、[NUnit](../N/nunit.md) 或用于 [unit testing](../U/unit-testing.md) 的 TestNG，以及用于更高级别集成测试的 [Selenium](../S/selenium.md) 或 Appium。
  在整个过程中，**持续集成**工具（例如 Jenkins、Travis CI 或 CircleCI）可用于自动化构建和测试周期，确保新更改顺利集成并且不会破坏现有功能。
  当所有子系统组合在一起并且整个系统按预期运行并且所有测试均成功通过时，[Bottom-up integration](../B/bottom-up-integration.md) 就完成了。

1. **[Unit Testing](../U/unit-testing.md)** ：对各个单元进行功能测试。
  2. **子系统集成**：将单元组合成子系统，然后进行测试。
  3. **子系统测试**：确保子系统内的集成单元正确协同工作。
  4. **系统集成**：子系统集成以形成完整的系统。
  5. **[System Testing](../S/system-testing.md)** ：整个系统经过测试是否符合要求。

#### 自下而上集成涉及哪些步骤？

**[bottom-up integration](../B/bottom-up-integration.md)**涉及的步骤如下：

1. **[Unit Testing](../U/unit-testing.md)**：首先测试最低级别的模块，通常称为**[unit testing](../U/unit-testing.md)**。确保每个模块独立正常运行。
  2. **集成**：将逻辑上相关的模块组合成集群或**子系统**。如有必要，使用**驱动程序脚本**测试这些交互。
  3. **子系统测试**：验证每个子系统的功能和性能。解决此阶段发现的任何缺陷。
  4. **存根替换**：如果使用任何**存根**来模拟更高级别的模块，则当它们可用并经过测试时，它们将被替换为实际模块。
  5. **系统组装**：逐步整合子系统，形成完整的系统。对于每个集成步骤，运行**回归测试**以确保新代码不会破坏现有功能。
  6. **[System Testing](../S/system-testing.md)**：系统完全集成后，执行彻底的 **[system testing](../S/system-testing.md)** 以验证端到端功能和非[functional requirements](../F/functional-requirements.md)。
  7. **[Acceptance Testing](../A/acceptance-testing.md)**：执行 **[acceptance testing](../A/acceptance-testing.md)** 以确保系统满足业务要求并做好生产准备。
  在这些步骤中，使用**持续集成**实践来自动化构建和测试，确保对集成工作的即时反馈。利用**[test harness](../T/test-harness.md)** 管理[test execution](../T/test-execution.md) 和报告。请记住使用专为 [bottom-up integration](../B/bottom-up-integration.md) 设计的有效 [test cases](../T/test-case.md) 来维护 **[test suite](../T/test-suite.md)**。

1. **[Unit Testing](../U/unit-testing.md)**：首先测试最低级别的模块，通常称为**[unit testing](../U/unit-testing.md)**。确保每个模块独立正常运行。
  2. **集成**：将逻辑上相关的模块组合成集群或**子系统**。如有必要，使用**驱动程序脚本**测试这些交互。
  3. **子系统测试**：验证每个子系统的功能和性能。解决此阶段发现的任何缺陷。
  4. **存根替换**：如果使用任何**存根**来模拟更高级别的模块，则当它们可用并经过测试时，它们将被替换为实际模块。
  5. **系统组装**：逐步整合子系统，形成完整的系统。对于每个集成步骤，运行**回归测试**以确保新代码不会破坏现有功能。
  6. **[System Testing](../S/system-testing.md)**：系统完全集成后，执行彻底的**[system testing](../S/system-testing.md)** 以验证端到端功能和非[functional requirements](../F/functional-requirements.md)。
  7. **[Acceptance Testing](../A/acceptance-testing.md)**：执行 **[acceptance testing](../A/acceptance-testing.md)** 以确保系统满足业务要求并做好生产准备。

#### 自下而上集成常用哪些工具？

在[bottom-up integration](../B/bottom-up-integration.md)中，[test automation](../T/test-automation.md)工程师通常使用各种工具来促进该过程：

- **[Unit Testing](../U/unit-testing.md) 框架**：JUnit (Java)、[NUnit](../N/nunit.md) (.NET) 或 unittest (Python) 等工具对于在各个组件上创建和运行单元测试至关重要。
  - **模拟框架**：Mockito (Java)、Moq (.NET) 和 unittest.mock (Python) 允许测试人员创建模拟对象并模拟已测试和集成的较低级别模块的行为。
  - **[Integration Testing](../I/integration-testing.md) 工具**：TestNG (Java) 和 SpecFlow (.NET) 可用于编写更高级别的集成测试，以验证集成组件之间的交互。
  - **构建自动化工具**：Jenkins、Travis CI 和 CircleCI 支持持续集成，通常与 [bottom-up integration](../B/bottom-up-integration.md) 结合使用以自动化构建和 [test process](../T/test-process.md)。
  - **[Code Coverage](../C/code-coverage.md) 工具**：JaCoCo (Java)、dotCover (.NET) 和coverage.py (Python) 有助于评估测试覆盖代码库的程度，确保在所有集成级别进行彻底的测试。
  - **[Performance Testing](../P/performance-testing.md) 工具**：[JMeter](../J/jmeter.md) 和 Gadling 可用于测试集成组件的性能，确保它们满足所需的基准。
  - **测试工具**：可以开发自定义测试工具来执行和管理集成组件的测试，特别是在处理复杂的交互或特定的测试场景时。
  使用这些工具，[test automation](../T/test-automation.md) 工程师可以有效地实施[bottom-up integration](../B/bottom-up-integration.md)，确保每个组件在进行更高级别的集成之前在系统中正确运行。

- **[Unit Testing](../U/unit-testing.md) 框架**：JUnit (Java)、[NUnit](../N/nunit.md) (.NET) 或 unittest (Python) 等工具对于在各个组件上创建和运行单元测试至关重要。
  - **模拟框架**：Mockito (Java)、Moq (.NET) 和 unittest.mock (Python) 允许测试人员创建模拟对象并模拟已测试和集成的较低级别模块的行为。
  - **[Integration Testing](../I/integration-testing.md) 工具**：TestNG (Java) 和 SpecFlow (.NET) 可用于编写更高级别的集成测试，以验证集成组件之间的交互。
  - **构建自动化工具**：Jenkins、Travis CI 和 CircleCI 支持持续集成，通常与 [bottom-up integration](../B/bottom-up-integration.md) 结合使用以自动化构建和 [test process](../T/test-process.md)。
  - **[Code Coverage](../C/code-coverage.md) 工具**：JaCoCo (Java)、dotCover (.NET) 和coverage.py (Python) 有助于评估测试覆盖代码库的程度，确保在所有集成级别进行彻底的测试。
  - **[Performance Testing](../P/performance-testing.md) 工具**：[JMeter](../J/jmeter.md) 和 Gadling 可用于测试集成组件的性能，确保它们满足所需的基准。
  - **测试工具**：可以开发自定义测试工具来执行和管理集成组件的测试，特别是在处理复杂的交互或特定的测试场景时。

#### 实施自下而上集成有哪些挑战以及如何克服这些挑战？

**[bottom-up integration](../B/bottom-up-integration.md)** 中的挑战主要围绕**驱动程序开发**、**部分[system testing](../S/system-testing.md)** 和**顶层设计问题的后期检测**。克服这些需要战略方法：

- **驱动程序开发**：驱动程序模拟更高级别的模块，创建起来可能很复杂。为了缓解这种情况，请使用**自动化工具**根据接口定义生成驱动程序，确保一致性并节省时间。
  - **部分系统功能**：首先测试较低级别的模块意味着完整的系统功能要到后期才可用。使用模拟完整系统的模拟对象或服务来实现 **[incremental testing](../I/incremental-testing.md)** 以尽早验证交互。
  - **高级问题的晚期检测**：由于高级模块是最后测试的，因此设计缺陷可能直到过程后期才被注意到。定期审查高层设计并使用**持续集成**来尽快发现问题。
  - **集成复杂性**：随着集成的组件越来越多，复杂性也会增加。利用**模块化设计**和**重构**来保持系统的可管理性。
  - **[Test Case](../T/test-case.md) 设计**：在没有清晰的系统视图的情况下设计[test cases](../T/test-case.md) 可能具有挑战性。专注于**接口契约**和**行为规范**以确保彻底的测试。
  - **工具**：选择支持[bottom-up integration](../B/bottom-up-integration.md) 并可以处理驱动程序和存根创建的工具。用于 [unit testing](../U/unit-testing.md) 的 **JUnit** 或 **TestNG** 以及用于模拟的 **Mockito** 或 **WireMock** 等工具可能会很有用。
  通过使用正确的策略和工具应对这些挑战，[bottom-up integration](../B/bottom-up-integration.md) 可以得到有效管理，以确保软件产品强大而可靠。

- **驱动程序开发**：驱动程序模拟更高级别的模块，创建起来可能很复杂。为了缓解这种情况，请使用**自动化工具**根据接口定义生成驱动程序，确保一致性并节省时间。
  - **部分系统功能**：首先测试较低级别的模块意味着完整的系统功能要到后期才可用。使用模拟完整系统的模拟对象或服务来实现 **[incremental testing](../I/incremental-testing.md)** 以尽早验证交互。
  - **高级问题的晚期检测**：由于高级模块是最后测试的，因此设计缺陷可能直到过程后期才被注意到。定期审查高层设计并使用**持续集成**来尽快发现问题。
  - **集成复杂性**：随着集成的组件越来越多，复杂性也会增加。利用**模块化设计**和**重构**来保持系统的可管理性。
  - **[Test Case](../T/test-case.md) 设计**：在没有清晰的系统视图的情况下设计[test cases](../T/test-case.md) 可能具有挑战性。专注于**接口契约**和**行为规范**以确保彻底的测试。
  - **工具**：选择支持[bottom-up integration](../B/bottom-up-integration.md) 并可以处理驱动程序和存根创建的工具。用于 [unit testing](../U/unit-testing.md) 的 **JUnit** 或 **TestNG** 以及用于模拟的 **Mockito** 或 **WireMock** 等工具可能会很有用。

#### 您能否提供一个自下而上集成的实际示例？

考虑一个场景，您正在集成**支付处理系统**。该系统由`PaymentGateway`、`TransactionProcessor`、`AccountManager` 和`NotificationService` 等模块组成。
  在**[bottom-up integration](../B/bottom-up-integration.md)**方法中，您首先测试`PaymentGateway`模块，该模块直接与银行[APIs](../A/api.md)交互。您为银行[API](../A/api.md) 创建一个 **[test stub](../T/test-stub.md)** 来模拟响应。

  ```
  function mockBankAPI(response) {
    // Simulate bank API response
    return response;
  }
  ```接下来，您集成并测试依赖于`PaymentGateway` 的`TransactionProcessor`。您使用已经测试过的`PaymentGateway` 模块，确保`TransactionProcessor` 正确处理响应。

  ```
  function testTransactionProcessor() {
    const response = mockBankAPI({ success: true });
    const result = TransactionProcessor.process(response);
    assert(result.status === 'processed');
  }
  ```您可以使用 `AccountManager` 继续此过程，这可能依赖 `TransactionProcessor` 在交易后更新帐户余额。
  最后，您集成`NotificationService`，它向用户发送交易警报。它依赖 `AccountManager` 来获取用户联系方式。
  在整个过程中，您使用**测试驱动程序**来模拟更高级别的模块，直到它们被开发和集成。当所有模块自下而上集成后，您就可以对整个支付系统进行最终的集成测试。
  通过首先关注最低级别的单元，您可以确保在向上移动层次结构之前打下坚实的基础，从而实现更可靠的集成过程。

### 测试

#### 自下而上集成中的测试是如何进行的？

在**自下而上的集成测试**中，测试是从软件层次结构的最低级别启动的。 [Test automation](../T/test-automation.md) 工程师专注于**单元级别**，其中首先使用**单元测试**来测试各个组件或模块。这些组件通常不依赖于任何较低级别的模块或服务。
  一旦单元测试通过，测试人员就会继续测试**更高级别的模块**，通常使用**测试驱动程序**来模拟尚未开发或测试的更高级别模块的行为。这一过程不断迭代，组件被逐一集成和测试，沿着层次结构向上移动，直到整个系统作为一个整体进行测试。
  在此过程中，**存根**在实际模块可用并经过测试时将被替换。这种方法可以及早发现单元级别的缺陷，修复起来比开发周期后期发现的缺陷更具成本效益。
  [bottom-up integration](../B/bottom-up-integration.md) 中的[Test automation](../T/test-automation.md) 通常涉及编写[test scripts](../T/test-script.md)，首先单独验证模块的功能，然后与其他模块组合。自动化框架和工具如 **JUnit**、**TestNG**、**Mockito** 或 **[Selenium](../S/selenium.md)**（用于基于 Web 的界面）可用于创建和运行这些测试。
  下面是使用 **[Jest](../J/jest.md)** 在 TypeScript 中进行简单单元测试的示例：

  ```
  import { add } from './math';
  test('adds 1 + 2 to equal 3', () => {
    expect(add(1, 2)).toBe(3);
  });
  ```在此示例中，`add` 函数是一个较低级别的组件，在与应用程序的其他部分集成之前要进行测试。

#### 自下而上集成中通常使用哪些类型的测试？

在**自下而上的集成测试**中，通常使用以下类型的测试：

- **单元测试**：验证各个组件或单元的功能。这些是首次以自下而上的方法进行的测试。
  - **组件集成测试**：确保单元在组合时按预期一起工作。这些测试侧重于单元之间的交互。
  - **子系统测试**：随着更大的组件或子系统的集成，进行测试以验证它们的交互和行为。
  - **系统集成测试**：子系统组合后，系统集成测试将检查系统内不同子系统之间的通信和数据流是否正确。
  - **回归测试**：在每个集成步骤之后，都会运行回归测试以确认新代码不会对现有功能产生不利影响。
  - **性能测试**：在集成组件时评估系统的性能，确保满足性能基准。
  - **端到端测试**：虽然在 [top-down integration](../T/top-down-integration.md) 中更常见，但一旦构建了足够的系统来模拟真实场景，就可以在 [bottom-up integration](../B/bottom-up-integration.md) 中应用一些端到端测试。
  这些测试通常是自动化的，以提高效率和可靠性。 [Test automation](../T/test-automation.md) 框架和工具（例如 **JUnit**、**TestNG**、**[Selenium](../S/selenium.md)** 和 **Mockito**）通常用于促进自下而上的集成测试。

- **单元测试**：验证各个组件或单元的功能。这些是首次以自下而上的方法进行的测试。
  - **组件集成测试**：确保单元在组合时按预期一起工作。这些测试侧重于单元之间的交互。
  - **子系统测试**：随着更大的组件或子系统的集成，进行测试以验证它们的交互和行为。
  - **系统集成测试**：子系统组合后，系统集成测试将检查系统内不同子系统之间的通信和数据流是否正确。
  - **回归测试**：在每个集成步骤之后，都会运行回归测试以确认新代码不会对现有功能产生不利影响。
  - **性能测试**：在集成组件时评估系统的性能，确保满足性能基准。
  - **端到端测试**：虽然在 [top-down integration](../T/top-down-integration.md) 中更常见，但一旦构建了足够的系统来模拟真实场景，就可以在 [bottom-up integration](../B/bottom-up-integration.md) 中应用一些端到端测试。

#### 自下而上的集成如何影响整个测试过程？

[Bottom-up integration](../B/bottom-up-integration.md) 通过**将焦点**转移到首先测试较低级别的组件，然后将它们集成到更大的系统中来影响整个测试过程。这种方法**有利于早期发现较小单元内的缺陷**，与后来在更高级别的集成中发现的缺陷相比，修复起来更具成本效益。
  由于测试从最基本的单元开始，因此**依赖测试驱动程序**和存根来模拟尚未开发的更高级别的模块。这可能会导致**额外的开发开销**，但可以确保每个组件都经过彻底的隔离测试。
  该方法还会影响 **[test case](../T/test-case.md) 设计**，该设计必须细粒度以涵盖各个单元的功能。随着组件的集成，[test cases](../T/test-case.md) 需要不断发展以涵盖集成单元之间的交互。
  在自下而上的集成测试过程中， **[test harness](../T/test-harness.md)** 在管理和执行 [test cases](../T/test-case.md) 以及捕获较低级别组件的测试结果方面发挥着至关重要的作用。随着更多组件的集成，线束需要坚固耐用，以应对系统的复杂性。
  总体而言，[bottom-up integration](../B/bottom-up-integration.md) 可以带来**更加模块化和解耦的设计**，因为每个组件在集成到更大的系统之前都是单独开发和测试的。这可以增强[maintainability](../M/maintainability.md) 和软件的可扩展性。
  集成过程是迭代的，在集成的每个阶段都进行**持续测试**。这与**敏捷和 DevOps 实践**非常吻合，其中持续集成和持续测试是关键组成部分。
  通过首先关注基本元素，[bottom-up integration](../B/bottom-up-integration.md) 确保核心功能是可靠的，这有助于提高软件的**整体质量和可靠性**。

#### 测试工具在自下而上的集成中扮演什么角色？

在 [bottom-up integration](../B/bottom-up-integration.md) 中， **[test harness](../T/test-harness.md)** 对于在开发或测试依赖于较低级别组件的较高级别组件之前验证较低级别组件的行为至关重要。它充当那些较高级别组件的临时替代品，为较低级别的模块提供必要的输入并控制环境。
  [test harness](../T/test-harness.md) 通常包括 **驱动程序** 或 **[test scripts](../T/test-script.md)**，它们通过调用较低级别的模块并处理其输出来模拟较高模块的行为。这允许单独测试单个单元或小组单元，确保它们在集成到更大的系统中时正常工作。
  使用[test harness](../T/test-harness.md) 有助于在开发过程的最早阶段识别缺陷，这比稍后检测缺陷更具成本效益。它还允许回归测试的自动化，每次进行更改时都可以运行回归测试，以确保现有功能没有被破坏。
  以下是如何在 [bottom-up integration](../B/bottom-up-integration.md) 测试中使用 [test harness](../T/test-harness.md) 的简单示例：

  ```
  // Example driver function to test a lower-level component
  function testComponent() {
    const result = lowerLevelComponent(inputData);
    assert(expectedOutput, result);
  }
  ```在此示例中，`lowerLevelComponent` 是正在测试的单元，`inputData` 是模拟输入，`expectedOutput` 是测试的[expected result](../E/expected-result.md)。 `assert` 函数检查实际输出是否与预期输出匹配。

#### 如何有效地设计测试用例以实现自下而上的集成？

为[bottom-up integration](../B/bottom-up-integration.md) 有效地设计[test cases](../T/test-case.md) 需要首先关注**单元级别**，并确保在与更高级别的模块集成之前对每个组件进行彻底的测试。以下是一些策略：

- **从单元测试开始**：为最低级别的模块编写全面的单元测试。使用适合您所使用的语言和环境的单元测试框架。

  ```
  describe('LowLevelModule', () => {
    it('should perform basic function correctly', () => {
      // Unit test code here
    });
  });
  ```

- **模拟依赖** ：由于尚未集成更高级别的模块，因此使用
    **模拟**
    或
    **存根**
    模拟依赖模块的行为。

  ```
  // Example of mocking a dependency
  const mockDependency = {
    functionToMock: () => {
      // Mocked behavior
    },
  };
  ```

- **[Incremental testing](../I/incremental-testing.md)** ：由于模块已集成，请编写
    **集成测试**
    对于新的组合，确保它们正确交互。

  ```
  describe('IntegratedModules', () => {
    it('should work together seamlessly', () => {
      // Integration test code here
    });
  });
  ```

- **测试驱动程序**：开发**测试驱动程序**来模拟调用正在测试的较低级别模块的较高级别模块。
  - **回归测试**：在每个集成步骤之后，运行**回归测试**以确保没有引入新的错误。
  - **性能测试**：包括关键模块的性能测试，以确保它们在集成时满足所需的效率标准。
  - **端到端测试**：系统自下而上完全集成后，进行端到端测试以验证完整的系统功能。
  通过遵循这些策略，您可以确保每个组件本身都是健壮的，并且在集成时表现正确，从而形成可靠且可维护的系统。

- **从单元测试开始**：为最低级别的模块编写全面的单元测试。使用适合您所使用的语言和环境的单元测试框架。
  - **模拟依赖** ：由于尚未集成更高级别的模块，因此使用
    **模拟**
    或
    **存根**
    模拟依赖模块的行为。

- **[Incremental testing](../I/incremental-testing.md)** ：由于模块已集成，请编写
    **集成测试**
    对于新的组合，确保它们正确交互。

- **测试驱动程序**：开发**测试驱动程序**来模拟调用正在测试的较低级别模块的较高级别模块。
  - **回归测试**：在每个集成步骤之后，运行**回归测试**以确保没有引入新的错误。
  - **性能测试**：包括关键模块的性能测试，以确保它们在集成时满足所需的效率标准。
  - **端到端测试**：系统自下而上完全集成后，进行端到端测试以验证完整的系统功能。

### 高级概念

#### 自下而上的集成与敏捷或 DevOps 等其他软件开发方法有何关系？

自下而上的集成测试通过支持迭代开发和持续集成，与**敏捷**和**DevOps**方法相一致。在敏捷中，开发是渐进式的，[bottom-up integration](../B/bottom-up-integration.md) 允许在开发时测试更小的功能组件，非常适合 **sprints** 和 **[iterations](../I/iteration.md)**。这种方法确保模块尽早且频繁地进行测试，这符合敏捷对**持续反馈**和**适应**的强调。
  在 **DevOps** 上下文中，[bottom-up integration](../B/bottom-up-integration.md) 补充了 **CI/CD 管道**。随着较低级别组件的开发和测试，它们可以持续集成和交付，确保快速检测和解决集成问题。这支持**自动化**、**协作**和**快速交付**的 DevOps 目标。
  这两种方法都依赖于**模块化**和**[test automation](../T/test-automation.md)**，这是[bottom-up integration](../B/bottom-up-integration.md) 所固有的。可以为每个单元和服务编写自动化测试，当它们组合在一起时，测试可以扩展到涵盖集成组件，从而促进从开发到部署的平稳过渡。
  此外，[bottom-up integration](../B/bottom-up-integration.md) 首先关注较低级别的组件在使用 **微服务** 或组件由不同团队开发时（DevOps 环境中的常见场景）特别有用。它允许独立开发、测试和部署各个服务，从而增强**可扩展性**和**灵活性**——敏捷和DevOps的关键原则。

#### 持续集成在自下而上集成中的作用是什么？

持续集成 (CI) 在[bottom-up integration](../B/bottom-up-integration.md) 中发挥着**关键作用**，它确保独立开发和测试的各个单元在集成时**一致地协同工作**。 CI 自动化构建和测试过程，允许将代码更改“频繁集成”到共享存储库中。
  在 [bottom-up integration](../B/bottom-up-integration.md) 的背景下，CI 通过以下方式提供帮助：

- **自动化构建**：随着较低级别组件的开发，CI 服务器会自动编译代码并检查集成问题。
  - **运行自动化测试**：定期执行为较低级别组件创建的单元测试，确保新代码不会破坏现有功能。
  - **尽早检测集成问题**：通过经常集成和测试，可以快速识别问题，从而降低故障排除的复杂性。
  - **促进协作**：开发人员会立即收到有关其承诺的反馈，从而促进采用更具协作性和主动性的方法来解决集成问题。
  CI 通过维护稳定的代码库充当[bottom-up integration](../B/bottom-up-integration.md) 的**支柱**，在该代码库中可以持续集成和验证较低级别的组件，从而实现更可靠、更高效的开发流程。

- **自动化构建**：随着较低级别组件的开发，CI 服务器会自动编译代码并检查集成问题。
  - **运行自动化测试**：定期执行为较低级别组件创建的单元测试，确保新代码不会破坏现有功能。
  - **尽早检测集成问题**：通过经常集成和测试，可以快速识别问题，从而降低故障排除的复杂性。
  - **促进协作**：开发人员会立即收到有关其承诺的反馈，从而促进采用更具协作性和主动性的方法来解决集成问题。

#### 自下而上的集成如何运用在微服务架构中？

在**微服务架构**中，可以通过启动与**单个微服务**及其各自的**单元测试**的集成过程来利用[bottom-up integration](../B/bottom-up-integration.md)。一旦这些较小的组件经过测试，测试人员就可以逐渐集成和测试这些服务之间的交互。
  要在微服务中应用 [bottom-up integration](../B/bottom-up-integration.md)，请按照以下步骤操作：

1. **开发和测试单个微服务**：确保每个微服务独立按预期工作。
  2. **创建存根和驱动程序**：这些将模拟尚未集成的更高级别服务或组件的行为。
  3. **集成和测试微服务对**：重点关注它们之间的交互和接口。
  4. **扩展集成**：逐步向集成测试套件添加更多服务，验证它们的交互。
  5. **集成并测试整个系统**：集成所有微服务后，执行端到端测试以确保系统作为一个整体运行。
  在此过程中，使用**持续集成 (CI)** 工具来自动化测试和集成阶段，确保新代码提交不会破坏现有功能。
  对于微服务，[bottom-up integration](../B/bottom-up-integration.md) 有助于在问题升级到系统级别之前识别 **服务级别** 的问题，从而使调试更轻松、更高效。它还与微服务的**独立部署**性质非常吻合，因为每个服务都可以按照自己的时间表进行测试和部署。

1. **开发和测试单个微服务**：确保每个微服务独立按预期工作。
  2. **创建存根和驱动程序**：这些将模拟尚未集成的更高级别服务或组件的行为。
  3. **集成和测试微服务对**：重点关注它们之间的交互和接口。
  4. **扩展集成**：逐步向集成测试套件添加更多服务，验证它们的交互。
  5. **集成并测试整个系统**：集成所有微服务后，执行端到端测试以确保系统作为一个整体运行。

#### 自下而上集成的最佳实践是什么？

软件[test automation](../T/test-automation.md) 中[bottom-up integration](../B/bottom-up-integration.md) 的最佳实践包括：

- **从单元测试开始**：确保每个组件在集成之前都经过彻底的单元测试。使用 JUnit for Java 或 PyTest for Python 等测试框架来自动执行这些测试。
  - **创建[test stubs](../T/test-stub.md)和驱动程序**：为尚未开发的高层组件开发[test stubs](../T/test-stub.md)，为低层组件开发驱动程序，以模拟系统中尚未集成的部分。
  - $

    ```
    ```// TypeScript 中的示例测试驱动程序
  类 ComponentDriver {
  模拟输入（输入：任意）{
  // 模拟组件的输入
  }
  获取输出（）{
  // 获取组件的输出
  }
  }

  ```
  - **Incremental testing**: Integrate and test one component at a time. After adding a component, run all relevant tests to ensure it integrates correctly with the already tested components.
  - **Automate regression tests**: Use automation tools like Selenium or Appium to run regression tests after each integration to catch any new defects introduced.
  - **Use continuous integration (CI)**: Implement a CI system like Jenkins, CircleCI, or GitHub Actions to automatically build and test the application after each commit, ensuring early detection of integration issues.
  - **Monitor code coverage**: Use tools like Istanbul or JaCoCo to track code coverage and ensure that tests are adequately covering the integrated components.
  - **Prioritize critical path testing**: Focus on the critical paths through the system that are most likely to be used in production to ensure they are robust and well-tested.
  - **Refactor as necessary**: Don't hesitate to refactor code and tests when integrating components if it improves maintainability and readability.
  - **Document the integration process**: Keep clear documentation of the integration steps and test results to facilitate communication among team members and for future reference.
  ```

- **从单元测试开始**：确保每个组件在集成之前都经过彻底的单元测试。使用 JUnit for Java 或 PyTest for Python 等测试框架来自动执行这些测试。
  - **创建[test stubs](../T/test-stub.md)和驱动程序**：为尚未开发的较高级别组件开发[test stubs](../T/test-stub.md)，为较低级别组件开发驱动程序，以模拟系统中尚未集成的部分。
  - $

    ```
    ```

#### 自下而上的集成如何提高软件质量和可靠性？

[Bottom-up integration](../B/bottom-up-integration.md) 通过确保首先测试应用程序的最基本单元，有助于 **[software quality](../S/software-quality.md) 和可靠性**。这种方法允许在系统层次结构的**最低级别**检测和纠正错误，这比修复开发过程后期发现的问题更具成本效益且更简单。通过关注**组件和子系统**，开发人员可以在将其集成到更大的系统之前验证其功能和稳健性。
  每个单元在成为更大集合的一部分之前都经过彻底测试并证明可以按预期工作，因此可靠性得到增强。这降低了由较低级别的缺陷引起的系统范围故障的风险。此外，随着集成的向上推进，**[test coverage](../T/test-coverage.md)** 逐渐扩展，这有助于为应用程序奠定坚实的基础。
  测试期间较低级别模块的**隔离**允许更有针对性和更高效的调试。当测试失败时，很明显问题在于被测试的特定单元，而不是更高级别组件之间的交互。这种精度可以在开发周期中节省时间和资源。
  总之，[bottom-up integration](../B/bottom-up-integration.md) 通过以下方式支持 [software quality](../S/software-quality.md) 和可靠性：

- **早期发现**
    单位层面的缺陷。

- **增量[test coverage](../T/test-coverage.md)**
    这建立了对系统的信心。

- **高效调试**
    由于组件的隔离测试。

- **具有成本效益**
    在高级集成之前进行纠错。

- **强化基础**
    对于应用程序，从而减少系统范围的问题。

- **早期发现**
    单位层面的缺陷。

- **增量[test coverage](../T/test-coverage.md)**
    这建立了对系统的信心。

- **高效调试**
    由于组件的隔离测试。

- **具有成本效益**
    在高级集成之前进行纠错。

- **强化基础**
    对于应用程序，从而减少系统范围的问题。
