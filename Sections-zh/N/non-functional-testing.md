# 非功能测试

<!-- TOC START -->
- [相关术语：](#相关术语：)
- [关于非功能测试的问题？](#关于非功能测试的问题？)
  - [基础知识和重要性](#基础知识和重要性)
    - [什么是非功能测试？](#什么是非功能测试？)
    - [为什么非功能测试很重要？](#为什么非功能测试很重要？)
    - [功能测试和非功能测试之间的主要区别是什么？](#功能测试和非功能测试之间的主要区别是什么？)
    - [非功能测试如何提高软件产品的整体质量？](#非功能测试如何提高软件产品的整体质量？)
  - [非功能测试的类型](#非功能测试的类型)
    - [非功能测试有哪些不同类型？](#非功能测试有哪些不同类型？)
    - [性能测试与负载测试有何不同？](#性能测试与负载测试有何不同？)
    - [压力测试的目的是什么？](#压力测试的目的是什么？)
    - [什么是可用性测试以及为什么它很重要？](#什么是可用性测试以及为什么它很重要？)
    - [什么是安全测试以及如何进行？](#什么是安全测试以及如何进行？)
  - [技术和工具](#技术和工具)
    - [非功能测试中使用了哪些技术？](#非功能测试中使用了哪些技术？)
    - [非功能测试常用哪些工具？](#非功能测试常用哪些工具？)
    - [如何为特定类型的非功能测试选择正确的工具？](#如何为特定类型的非功能测试选择正确的工具？)
    - [使用非功能测试工具的最佳实践有哪些？](#使用非功能测试工具的最佳实践有哪些？)
  - [实施与管理](#实施与管理)
    - [在软件开发生命周期中什么时候应该执行非功能测试？](#在软件开发生命周期中什么时候应该执行非功能测试？)
    - [项目中的非功能测试通常是如何管理的？](#项目中的非功能测试通常是如何管理的？)
    - [实施非功能测试有哪些挑战以及如何克服这些挑战？](#实施非功能测试有哪些挑战以及如何克服这些挑战？)
    - [非功能测试的结果如何有效地传达给利益相关者？](#非功能测试的结果如何有效地传达给利益相关者？)
<!-- TOC END -->

非功能测试

评估软件的非功能属性，例如可用性和性能，确保软件的整体能力和有效性。

## 相关术语：

- [Performance Testing](../P/performance-testing.md)
- [Load Testing](../L/load-testing.md)
- [Stress Testing](../S/stress-testing.md)
- [Scalability Testing](../S/scalability-testing.md)
- [Usability Testing](../U/usability-testing.md)
- [Reliability Testing](../R/reliability-testing.md)

## 关于非功能测试的问题？

### 基础知识和重要性

#### 什么是非功能测试？

[Non-functional testing](../N/non-functional-testing.md) 评估软件的操作方面，例如**性能**、**可靠性**、**可扩展性**和**资源使用情况**。它关注的是系统在特定条件下的**“表现如何”**，而不是它的**“什么”**，这由[functional testing](../F/functional-testing.md) 涵盖。此类测试对于验证系统的质量属性至关重要，例如**系统合规性**、**安全性**和**可用性**。
  对于[test automation](../T/test-automation.md) 工程师来说，[non-functional testing](../N/non-functional-testing.md) 涉及编写脚本和执行测量系统属性（如**响应时间**、**吞吐量**和**并发级别**）的测试。 **[JMeter](../J/jmeter.md)**、**LoadRunner** 和 **Gadling** 等工具通常用于模拟各种场景和工作负载。
  为了有效地自动化非功能测试，工程师必须了解系统的性能基准和操作要求。他们还应该精通设置模拟生产设置的 [test environments](../T/test-environment.md) 以确保准确的结果。
  自动化非功能测试通常集成到 CI/CD 管道中，以在整个开发生命周期中持续评估系统的性能。这有助于及早发现性能瓶颈和其他问题，从而降低生产故障的风险。
  总之，[non-functional testing](../N/non-functional-testing.md) 是软件质量保证的关键组成部分，重点关注影响用户满意度和系统稳健性的方面。自动化工程师必须选择适当的工具和技术来有效地测量和改进这些属性。

#### 为什么非功能测试很重要？

[Non-functional testing](../N/non-functional-testing.md) 至关重要，因为它确保了系统在各种条件下的**可靠性**、**可用性**和**性能**，而这些是[functional testing](../F/functional-testing.md) 未涵盖的。它解决了诸如**可扩展性**、**安全性**和**[maintainability](../M/maintainability.md)**等方面的问题，这些方面影响用户满意度和系统在生产中的操作行为。
  对于自动化工程师来说，将非功能测试纳入自动化套件意味着您可以**持续监控** CI/CD 管道中的这些属性。这种主动方法有助于及早发现潜在的瓶颈和漏洞，降低部署后出现故障的风险。
  此外，[non-functional testing](../N/non-functional-testing.md) 可以影响**技术选择**和**架构**决策，因为它经常揭示需要更好的基础设施或设计模式来满足性能和安全标准。它还在**遵守**行业法规和标准方面发挥着重要作用，这对于软件的市场接受度至关重要。
  通过自动化非功能测试，您可以确保这些关键方面不会被忽视，并得到一致和严格的测试。这将带来更加**强大和可靠的**软件产品，提高软件和组织的**声誉**，并最终有助于**更好的用户体验**。

#### 功能测试和非功能测试之间的主要区别是什么？

[Functional testing](../F/functional-testing.md) 重点验证软件应用程序的每个功能是否按照需求规范运行。这涉及检查用户界面、[APIs](../A/api.md)、[databases](../D/database.md)、安全性、客户端/服务器应用程序和软件功能。主要目标是确保软件按预期运行。
  另一方面，[Non-functional testing](../N/non-functional-testing.md) 处理非功能方面，例如软件的性能、可用​​性、可靠性和兼容性。它不测试特定行为，而是测试软件的操作方面。
  **主要区别**：

- **范围**：功能测试涉及功能的具体行为，而非功能测试涵盖软件的整体属性。
  - **验证与[Verification](../V/verification.md)**：功能测试是一种验证，确保产品满足用户的需求。非功能测试是一种验证，确保产品满足指定的要求。
  - **用户交互**：功能测试通常模仿用户交互，而非功能测试可能不直接涉及用户场景。
  - **执行**：功能测试可以是手动或自动的，但非功能测试由于其复杂性通常需要专门的测试工具。
  - **标准**：功能测试基于业务需求，而非功能测试基于性能基准和其他非功能标准。
  总之，[functional testing](../F/functional-testing.md) 是关于系统的 **“什么”**，而 [non-functional testing](../N/non-functional-testing.md) 是关于系统在特定条件下的 **“性能如何”**。

- **范围**：功能测试涉及功能的具体行为，而非功能测试涵盖软件的整体属性。
  - **验证与[Verification](../V/verification.md)**：功能测试是一种验证，确保产品满足用户的需求。非功能测试是一种验证，确保产品满足指定的要求。
  - **用户交互**：功能测试通常模仿用户交互，而非功能测试可能不直接涉及用户场景。
  - **执行**：功能测试可以是手动或自动的，但非功能测试由于其复杂性通常需要专门的测试工具。
  - **标准**：功能测试基于业务需求，而非功能测试基于性能基准和其他非功能标准。

#### 非功能测试如何提高软件产品的整体质量？

[Non-functional testing](../N/non-functional-testing.md) 通过确保产品满足**性能**、**可靠性**、**可用性**和**安全**标准等标准来增强[software quality](../S/software-quality.md)。它验证系统在各种条件和压力下的行为，[functional testing](../F/functional-testing.md) 不包括这些。通过关注**响应时间**、**资源使用**和**可扩展性**等方面，[non-functional testing](../N/non-functional-testing.md) 提供了对软件操作特性的深入了解。
  此类测试还检查是否符合法规和标准，这对于维持信任和避免法律问题至关重要。它有助于识别潜在的安全漏洞，确保用户数据受到保护并且系统能够抵御攻击。
  此外，[non-functional testing](../N/non-functional-testing.md)通过[usability testing](../U/usability-testing.md)评估用户体验，确认该产品直观且易于使用。这会显着影响客户满意度和保留率。
  将[non-functional testing](../N/non-functional-testing.md) 纳入开发生命周期可以带来更强大、更稳定的产品，能够在峰值负载和压力条件下正常运行。它还有助于优化系统以获得更好的性能，从而降低基础设施成本。
  通过解决这些方面，[non-functional testing](../N/non-functional-testing.md) 有助于打造更高质量的产品，不仅**正常工作**，而且**提供积极的用户体验**、**高效执行**，并**确保安全性和合规性**。这种全面的质量方法有助于打造出不仅功能齐全、而且可靠且具有市场竞争力的产品。

### 非功能测试的类型

#### 非功能测试有哪些不同类型？

不同类型的 [non-functional testing](../N/non-functional-testing.md) 包括：

- **[Compatibility Testing](../C/compatibility-testing.md)** ：确保软件在不同设备、操作系统版本、浏览器和其他系统环境中按预期运行。
  - **合规性测试**：验证软件是否遵守标准、法规或指南，例如数据隐私的 GDPR。
  - **灾难恢复测试**：评估软件从崩溃、硬件故障或其他灾难性事件中恢复的能力。
  - **效率测试**：评估软件的资源使用情况及其对系统性能的影响。
  - **安装测试**：确认软件安装正确并在目标系统上按预期运行。
  - **[Maintainability](../M/maintainability.md) 测试**：衡量软件维护的容易程度，包括代码可读性、更新过程和文档质量。
  - **可移植性测试**：检查软件从一个环境移动到另一个环境的难易程度。
  - **[Reliability Testing](../R/reliability-testing.md)** ：评估软件在指定时间内在预期条件下执行的能力。
  - **弹性测试**：评估软件在不丢失数据或功能的情况下处理故障和从故障中恢复的能力。
  - **[Scalability Testing](../S/scalability-testing.md)** ：确定软件处理增加的负载的能力以及扩展的潜力。
  - **[Volume Testing](../V/volume-testing.md)** ：测试软件在不降低性能的情况下处理大量数据的能力。
  每种类型都针对系统行为和质量的特定方面（超出 [functional requirements](../F/functional-requirements.md) 范围），以确保对软件的整体性能和用户体验进行全面评估。

- **[Compatibility Testing](../C/compatibility-testing.md)** ：确保软件在不同设备、操作系统版本、浏览器和其他系统环境中按预期运行。
  - **合规性测试**：验证软件是否遵守标准、法规或指南，例如数据隐私的 GDPR。
  - **灾难恢复测试**：评估软件从崩溃、硬件故障或其他灾难性事件中恢复的能力。
  - **效率测试**：评估软件的资源使用情况及其对系统性能的影响。
  - **安装测试**：确认软件安装正确并在目标系统上按预期运行。
  - **[Maintainability](../M/maintainability.md) 测试**：衡量软件维护的容易程度，包括代码可读性、更新过程和文档质量。
  - **可移植性测试**：检查软件从一个环境移动到另一个环境的难易程度。
  - **[Reliability Testing](../R/reliability-testing.md)** ：评估软件在指定时间内在预期条件下执行的能力。
  - **弹性测试**：评估软件在不丢失数据或功能的情况下处理故障和从故障中恢复的能力。
  - **[Scalability Testing](../S/scalability-testing.md)** ：确定软件处理增加的负载的能力以及扩展的潜力。
  - **[Volume Testing](../V/volume-testing.md)** ：测试软件在不降低性能的情况下处理大量数据的能力。

#### 性能测试与负载测试有何不同？

[Performance testing](../P/performance-testing.md) 和[load testing](../L/load-testing.md) 都是[non-functional testing](../N/non-functional-testing.md) 的子集，侧重于特定条件下系统行为的不同方面。
  **[Performance testing](../P/performance-testing.md)** 是一个广泛的术语，包括评估特定工作负载下系统的速度、响应能力和稳定性。它的目的是识别性能瓶颈并确保软件满足需求中指定的性能标准。
  另一方面，**[Load testing](../L/load-testing.md)** 是 [performance testing](../P/performance-testing.md) 的一种类型，专门检查系统在预期负载下的行为方式。这涉及在一段时间内模拟大量用户或交易，以验证系统的容量并确定它如何处理增加的数据量或用户流量。
  本质上，虽然所有[load testing](../L/load-testing.md) 都是[performance testing](../P/performance-testing.md) 的一种形式，但并非所有[performance testing](../P/performance-testing.md) 都是[load testing](../L/load-testing.md)。 [Performance testing](../P/performance-testing.md) 关注整体系统行为，而[load testing](../L/load-testing.md) 则关注系统对预期的特定负载条件的处理。

#### 压力测试的目的是什么？

[Stress testing](../S/stress-testing.md) 是**[non-functional testing](../N/non-functional-testing.md)** 的一种类型，旨在评估系统在极端条件下的**稳定性和可靠性**。它故意使系统承受**超出正常的负载水平**，以识别其**断点**并观察它如何从故障中恢复。目的是确保系统**正常降级**并能够保持数据完整性并在压力下继续以受控方式运行。 [Stress testing](../S/stress-testing.md) 对于在将软件部署到生产之前识别潜在的**瓶颈**和**非弹性**区域至关重要，这些问题可能会导致严重的停机或数据丢失。它还有助于验证系统是否按设计向备份系统发送适当的**警报**或**故障转移**。这种类型的测试对于需要高可用性的**任务关键型应用程序**以及可能遭受不可预测的用户流量或数据量峰值的应用程序尤其重要。

#### 什么是可用性测试以及为什么它很重要？

[Usability testing](../U/usability-testing.md) 评估软件应用程序对于最终用户而言的**简单**和**直观**。它是用户体验 (UX) 测试的关键组成部分，重点关注应用程序为用户提供的**效率**、**有效性**和**满意度**。与其他可能自动化的非功能测试不同，[usability testing](../U/usability-testing.md) 通常需要真实用户在观察下完成任务，以识别任何可用性问题。
  [usability testing](../U/usability-testing.md) 的重要性在于其以用户为中心的方法，这有助于确保软件满足用户的**实际需求**和**期望**。它可以发现其他测试方法可能不明显的用户界面设计、工作流程和信息架构问题。
  主要优点包括：

- **提高用户满意度**：通过解决可用性问题，软件变得更令人愉快且更易于使用，从而提高用户满意度和保留率。
  - **降低开发成本**：尽早发现可用性问题可以减少发布后昂贵的重新设计和重新开发的需要。
  - **提高生产力**：直观且易于使用的软件可以提高用户的生产力，这对于企业应用程序尤其重要。
  [Usability testing](../U/usability-testing.md) 应集成在从早期原型到最终产品的整个开发生命周期中，以确保用户体验的持续改进。这是一种协作努力，通常涉及设计师、开发人员和利益相关者，以创建不仅能够正常运行而且能够提供无缝且令人满意的用户体验的产品。

- **提高用户满意度**：通过解决可用性问题，软件变得更令人愉快且更易于使用，从而提高用户满意度和保留率。
  - **降低开发成本**：尽早发现可用性问题可以减少发布后昂贵的重新设计和重新开发的需要。
  - **提高生产力**：直观且易于使用的软件可以提高用户的生产力，这对于企业应用程序尤其重要。

#### 什么是安全测试以及如何进行？

[Security testing](../S/security-testing.md) 是 **[non-functional testing](../N/non-functional-testing.md)** 的一种类型，专注于验证软件系统是否按预期保护数据并维护功能。它旨在发现可能导致信息安全漏洞的漏洞、威胁和风险。
  要执行 [security testing](../S/security-testing.md)，请按照下列步骤操作：

1. **规划**：确定安全目标、定义范围并确定测试方法。
  2. **威胁建模**：分析应用程序以识别潜在的威胁和漏洞。
  3. **[Test Case](../T/test-case.md) 设计**：根据已识别的安全风险创建测试用例，重点关注身份验证、授权、数据完整性和机密性等领域。
  4. **静态分析**：使用工具检查代码是否存在安全缺陷，而不执行它。
  5. **动态分析**：执行应用程序并监控其行为以识别安全问题。
  6. **[Penetration Testing](../P/penetration-testing.md)** ：模拟对系统的攻击以识别可利用的漏洞。
  7. **安全审计**：通过衡量公司信息系统与一组既定标准的符合程度，对公司信息系统的安全性进行系统评估。
  8. **风险评估**：评估已识别的安全风险，以确定修复工作的优先顺序。
  9. **修复**：通过应用补丁、更改配置或修改代码来解决发现的漏洞。
  10. **[Retesting](../R/retesting.md)** ：验证漏洞是否已修复并且没有引入新问题。
  [security testing](../S/security-testing.md) 的常用工具包括 **静态应用程序 [security testing](../S/security-testing.md) (SAST)** 工具、**动态应用程序 [security testing](../S/security-testing.md) (DAST)** 工具和 **[penetration testing](../P/penetration-testing.md)** 工具，例如 OWASP ZAP 或 Metasploit。
  结果应清晰记录，突出风险并为利益相关者提供可行的见解。 [Security testing](../S/security-testing.md) 是迭代的，应尽早集成到**软件开发生命周期 (SDLC)** 中，以最大限度地减少变更的成本和影响。

1. **规划**：确定安全目标、定义范围并确定测试方法。
  2. **威胁建模**：分析应用程序以识别潜在的威胁和漏洞。
  3. **[Test Case](../T/test-case.md) 设计**：根据已识别的安全风险创建测试用例，重点关注身份验证、授权、数据完整性和机密性等领域。
  4. **静态分析**：使用工具检查代码是否存在安全缺陷，而不执行它。
  5. **动态分析**：执行应用程序并监控其行为以识别安全问题。
  6. **[Penetration Testing](../P/penetration-testing.md)** ：模拟对系统的攻击以识别可利用的漏洞。
  7. **安全审计**：通过衡量公司信息系统与一组既定标准的符合程度，对公司信息系统的安全性进行系统评估。
  8. **风险评估**：评估已识别的安全风险，以确定修复工作的优先顺序。
  9. **修复**：通过应用补丁、更改配置或修改代码来解决发现的漏洞。
  10. **[Retesting](../R/retesting.md)** ：验证漏洞是否已修复并且没有引入新问题。

### 技术和工具

#### 非功能测试中使用了哪些技术？

[Non-functional testing](../N/non-functional-testing.md) 技术因所测试的属性而异。以下是一些关键技术：

- **基准测试**：将系统性能与设定标准或竞争对手产品进行比较。
  - **合规性测试**：确保软件符合标准、法规和指南。
  - **灾难恢复测试**：模拟灾难场景来测试备份和恢复过程。
  - **[Endurance Testing](../E/endurance-testing.md)** ：评估系统在较长时间内的稳定性。
  - **[Failover Testing](../F/failover-testing.md)** ：验证系统是否可以处理组件故障并无缝切换到备份。
  - **安装测试**：检查安装过程以确保其用户友好且无错误。
  - **[Interoperability Testing](../I/interoperability-testing.md)** ：确保软件可以与其他系统或组件一起运行。
  - **[Load Testing](../L/load-testing.md)** ：评估系统在预期负载条件下的行为。
  - **[Maintainability](../M/maintainability.md) 测试**：衡量软件更新和修复的实施难易程度。
  - **可移植性测试**：检查软件从一种环境转移到另一种环境的能力。
  - **[Reliability Testing](../R/reliability-testing.md)** ：确定软件在指定时间段内特定条件下执行的能力。
  - **弹性测试**：测试系统从崩溃、硬件故障或其他类似问题中恢复的情况。
  - **资源使用测试**：监控不同条件下CPU、内存和磁盘空间等系统资源的使用情况。
  - **[Scalability Testing](../S/scalability-testing.md)** ：评估软件根据处理需求的变化而扩大或缩小的能力。
  - **[Volume Testing](../V/volume-testing.md)** ：检查系统处理大量数据的能力。
  这些技术使用专为[non-functional testing](../N/non-functional-testing.md)设计的各种工具和框架来应用，并且结果通常被量化以提供对系统性能和行为的清晰见解。

- **基准测试**：将系统性能与设定标准或竞争对手产品进行比较。
  - **合规性测试**：确保软件符合标准、法规和指南。
  - **灾难恢复测试**：模拟灾难场景来测试备份和恢复过程。
  - **[Endurance Testing](../E/endurance-testing.md)** ：评估系统在较长时间内的稳定性。
  - **[Failover Testing](../F/failover-testing.md)** ：验证系统是否可以处理组件故障并无缝切换到备份。
  - **安装测试**：检查安装过程以确保其用户友好且无错误。
  - **[Interoperability Testing](../I/interoperability-testing.md)** ：确保软件可以与其他系统或组件一起运行。
  - **[Load Testing](../L/load-testing.md)** ：评估系统在预期负载条件下的行为。
  - **[Maintainability](../M/maintainability.md) 测试**：衡量软件更新和修复的实施难易程度。
  - **可移植性测试**：检查软件从一种环境转移到另一种环境的能力。
  - **[Reliability Testing](../R/reliability-testing.md)** ：确定软件在指定时间段内特定条件下执行的能力。
  - **弹性测试**：测试系统从崩溃、硬件故障或其他类似问题中恢复的情况。
  - **资源使用测试**：监控不同条件下CPU、内存和磁盘空间等系统资源的使用情况。
  - **[Scalability Testing](../S/scalability-testing.md)** ：评估软件根据处理需求的变化而扩大或缩小的能力。
  - **[Volume Testing](../V/volume-testing.md)** ：检查系统处理大量数据的能力。

#### 非功能测试常用哪些工具？

[non-functional testing](../N/non-functional-testing.md) 的常用工具包括：

- **[JMeter](../J/jmeter.md)** ：专为性能和负载测试而设计的开源工具。
  - **LoadRunner**：广泛使用的性能测试工具，支持各种协议和技术。
  - **Gattle**：基于 Scala、Akka 和 Netty 的 Web 应用程序的高性能负载测试工具。
  - **WebLOAD**：用于负载、压力和性能测试的强大工具，支持复杂的场景。
  - **Nessus**：用于安全测试的综合漏洞扫描工具。
  - **Burp Suite**：用于执行 Web 应用程序安全测试的集成平台。
  - **Wireshark**：网络协议分析仪，用于网络故障排除、分析和安全测试。
  - **Apache Bench (ab)**：用于对 HTTP 服务器性能进行基准测试的简单工具。
  - **[Selenium](../S/selenium.md)** ：主要是功能测试工具，但可用于某些类型的非功能测试，例如浏览器兼容性。
  - **Appium** ：与 Selenium 类似，用于移动应用程序测试，包括不同设备上的性能方面。
  - **Owasp ZAP**：开源 Web 应用程序安全扫描器。
  - **SonarQube**：一种持续检查代码质量的工具，通过静态分析执行自动审查，以检测错误、代码异味和安全漏洞。
  - **New Relic**：一种 SaaS 产品，为实时应用程序提供性能监控。
  - **Dynatrace**：一种提供应用程序性能管理和云基础设施监控的工具。
  每个工具都有自己的优势，并根据[test scenario](../T/test-scenario.md) 的具体要求进行选择。

- **[JMeter](../J/jmeter.md)** ：专为性能和负载测试而设计的开源工具。
  - **LoadRunner**：广泛使用的性能测试工具，支持各种协议和技术。
  - **Gattle**：基于 Scala、Akka 和 Netty 的 Web 应用程序的高性能负载测试工具。
  - **WebLOAD**：用于负载、压力和性能测试的强大工具，支持复杂的场景。
  - **Nessus**：用于安全测试的综合漏洞扫描工具。
  - **Burp Suite**：用于执行 Web 应用程序安全测试的集成平台。
  - **Wireshark**：网络协议分析仪，用于网络故障排除、分析和安全测试。
  - **Apache Bench (ab)**：用于对 HTTP 服务器性能进行基准测试的简单工具。
  - **[Selenium](../S/selenium.md)** ：主要是功能测试工具，但可用于某些类型的非功能测试，例如浏览器兼容性。
  - **Appium** ：与 Selenium 类似，用于移动应用程序测试，包括不同设备上的性能方面。
  - **Owasp ZAP**：开源 Web 应用程序安全扫描器。
  - **SonarQube**：一种持续检查代码质量的工具，通过静态分析执行自动审查，以检测错误、代码异味和安全漏洞。
  - **New Relic**：一种 SaaS 产品，为实时应用程序提供性能监控。
  - **Dynatrace**：一种提供应用程序性能管理和云基础设施监控的工具。

#### 如何为特定类型的非功能测试选择正确的工具？

为特定类型的[non-functional testing](../N/non-functional-testing.md) 选择正确的工具涉及评估几个因素：

- **兼容性**：确保该工具支持您的应用程序的技术堆栈（例如网络、移动、API）。
  - **测试类型特异性**：选择专门用于您需要的非功能测试类型的工具，例如用于负载测试的性能测试工具或用于漏洞扫描的安全测试工具。
  - **集成**：寻找与您的 CI/CD 管道和您正在使用的其他测试工具无缝集成的工具。
  - **可扩展性**：该工具应该能够随着应用程序的增长处理负载和大小。
  - **易于使用**：更喜欢具有用户友好界面和良好文档的工具，以减少学习曲线。
  - **报告**：选择能够提供利益相关者可以理解的全面且可操作的报告的工具。
  - **成本**：根据您的预算考虑工具的成本，包括许可、培训和维护。
  - **社区和支持**：强大的社区和专业支持对于故障排除和最佳实践非常宝贵。
  - **定制**：定制测试以及与其他工具或框架集成的能力对于复杂的测试环境至关重要。
  - **试用和评估**：只要有可能，请使用免费试用来评估该工具是否适合您的特定需求。
  评估 [performance testing](../P/performance-testing.md) 工具的示例：

  ```
  // Assessing Apache JMeter for performance testing
  if (supportsTechnologyStack(application) && isSpecializedFor('performance')) {
    const integrationEase = checkIntegrationWithCI(application);
    const scalability = evaluateScalability(application);
    const usability = assessEaseOfUse('Apache JMeter');
    const reportingQuality = checkReportingCapabilities('Apache JMeter');
    const costEffectiveness = calculateCost('Apache JMeter');
    const communitySupport = checkCommunitySupport('Apache JMeter');
    const customizationOptions = checkCustomizationCapabilities('Apache JMeter');
    const trialSuccess = performTrialEvaluation('Apache JMeter', application);
    if (integrationEase && scalability && usability && reportingQuality && costEffectiveness && communitySupport && customizationOptions && trialSuccess) {
      // Tool is a good fit
    } else {
      // Consider alternative tools
    }
  }
  ```请记住根据项目需求的[priority](../P/priority.md) 权衡这些因素。

- **兼容性**：确保该工具支持您的应用程序的技术堆栈（例如网络、移动、API）。
  - **测试类型特异性**：选择专门用于您需要的非功能测试类型的工具，例如用于负载测试的性能测试工具或用于漏洞扫描的安全测试工具。
  - **集成**：寻找与您的 CI/CD 管道和您正在使用的其他测试工具无缝集成的工具。
  - **可扩展性**：该工具应该能够随着应用程序的增长处理负载和大小。
  - **易于使用**：更喜欢具有用户友好界面和良好文档的工具，以减少学习曲线。
  - **报告**：选择能够提供利益相关者可以理解的全面且可操作的报告的工具。
  - **成本**：根据您的预算考虑工具的成本，包括许可、培训和维护。
  - **社区和支持**：强大的社区和专业支持对于故障排除和最佳实践非常宝贵。
  - **定制**：定制测试以及与其他工具或框架集成的能力对于复杂的测试环境至关重要。
  - **试用和评估**：只要有可能，请使用免费试用来评估该工具是否适合您的特定需求。

#### 使用非功能测试工具的最佳实践有哪些？

使用 [non-functional testing](../N/non-functional-testing.md) 工具的最佳实践包括：

- **选择集成工具**
    与您现有的开发和测试环境一起简化工作流程。

- **尽可能自动化**
    ，但要认识到某些方面（例如某些安全测试）可能需要手动专业知识。

- **监控工具性能**
    并确保它们不会成为您测试过程中的瓶颈。

- 使用
    **版本控制**
    用于测试脚本和配置来跟踪更改并保持跨环境的一致性。

- **参数化测试**
    无需重写脚本即可轻松适应不同的环境和场景。

- **隔离[test environments](../T/test-environment.md)**
    从生产中防止意外影响并确保测试可靠性。

- **设定现实且有意义的阈值**
    用于性能、负载和压力测试，以反映实际的用户情况。

- **定期更新**
    您利用新功能和安全补丁的工具。

- **自定义报告**
    突出与利益相关者相关的关键指标和发现。

- **验证工具结果**
    手动检查以确保准确性和相关性。

- **记录[test cases](../T/test-case.md) 和结果**
    精心准备以供将来参考和合规需求。

- **优先测试**
    基于风险、使用模式和对业务的重要性。

- **培训你的团队**
    最大限度地发挥工具的潜力并确保正确使用。

- **与开发人员合作**
    了解系统架构并设计全面且有针对性的测试。
  通过遵循这些实践，您可以最大限度地提高 [non-functional testing](../N/non-functional-testing.md) 工具的有效性，并为高质量软件的交付做出贡献。

- **选择集成工具**
    与您现有的开发和测试环境一起简化工作流程。

- **尽可能自动化**
    ，但要认识到某些方面（例如某些安全测试）可能需要手动专业知识。

- **监控工具性能**
    并确保它们不会成为您测试过程中的瓶颈。

- 使用
    **版本控制**
    用于测试脚本和配置来跟踪更改并保持跨环境的一致性。

- **参数化测试**
    无需重写脚本即可轻松适应不同的环境和场景。

- **隔离[test environments](../T/test-environment.md)**
    从生产中防止意外影响并确保测试可靠性。

- **设定现实且有意义的阈值**
    用于性能、负载和压力测试，以反映实际的用户情况。

- **定期更新**
    您利用新功能和安全补丁的工具。

- **自定义报告**
    突出与利益相关者相关的关键指标和发现。

- **验证工具结果**
    手动检查以确保准确性和相关性。

- **记录[test cases](../T/test-case.md) 和结果**
    精心准备以供将来参考和合规需求。

- **优先测试**
    基于风险、使用模式和对业务的重要性。

- **培训你的团队**
    最大限度地发挥工具的潜力并确保正确使用。

- **与开发人员合作**
    了解系统架构并设计全面且有针对性的测试。

### 实施与管理

#### 在软件开发生命周期中什么时候应该执行非功能测试？

[Non-functional testing](../N/non-functional-testing.md) 应集成在整个**软件开发生命周期 (SDLC)** 中，但时间安排可能会根据测试类型和项目要求而有所不同。以下是何时执行 [non-functional testing](../N/non-functional-testing.md) 的关键点：

- **早期阶段**：初始开发阶段一开始，就从安全性、[maintainability](../M/maintainability.md) 和可靠性的基本检查开始。这有助于识别潜在问题，如果以后发现这些问题，成本可能会更高。
  - **[Functional Testing](../F/functional-testing.md)之后**：更全面的非功能测试（例如性能和[load testing](../L/load-testing.md)）通常在[functional testing](../F/functional-testing.md) 确保软件按预期运行之后进行。这是因为当软件功能稳定时，响应时间和可扩展性等非功能方面更有意义。
  - **持续集成 (CI)**：将某些非功能测试（例如代码质量和安全扫描）合并到 CI 管道中，以便为每个构建提供持续的反馈。
  - **发布前**：在预发布阶段进行最后几轮[non-functional testing](../N/non-functional-testing.md)，例如压力和[usability testing](../U/usability-testing.md)，以确保软件能够处理生产条件并且用户友好。
  - **发布后**：在生产环境中执行 [non-functional testing](../N/non-functional-testing.md) 以监控实际性能和安全性，并确保符合 SLA 和监管标准。
  请记住根据**风险评估**和**项目关键性**确定[non-functional testing](../N/non-functional-testing.md)的优先级。尽可能实现自动化以保持效率和一致性。

- **早期阶段**：初始开发阶段一开始，就从安全性、[maintainability](../M/maintainability.md) 和可靠性的基本检查开始。这有助于识别潜在问题，如果以后发现这些问题，成本可能会更高。
  - **[Functional Testing](../F/functional-testing.md)之后**：更全面的非功能测试，例如性能和[load testing](../L/load-testing.md)，通常在[functional testing](../F/functional-testing.md) 确保软件按预期运行之后进行。这是因为当软件功能稳定时，响应时间和可扩展性等非功能方面更有意义。
  - **持续集成 (CI)**：将某些非功能测试（例如代码质量和安全扫描）合并到 CI 管道中，以便为每个构建提供持续的反馈。
  - **发布前**：在预发布阶段进行最后几轮[non-functional testing](../N/non-functional-testing.md)，例如压力和[usability testing](../U/usability-testing.md)，以确保软件能够处理生产条件并且用户友好。
  - **发布后**：在生产环境中执行 [non-functional testing](../N/non-functional-testing.md) 以监控实际性能和安全性，并确保符合 SLA 和监管标准。

#### 项目中的非功能测试通常是如何管理的？

项目内的[Non-functional testing](../N/non-functional-testing.md) 通常通过**规划**、**执行**和**报告**阶段的组合进行管理，并集成到整个项目管理框架中。以下是简要概述：

- **规划**：定义非[functional requirements](../F/functional-requirements.md) (NFR) 并建立明确的测试目标。根据确定的非功能测试类型（例如性能、安全性、可用性）分配资源、设定时间表并选择适当的工具。
  - **执行**：使用选定的工具和方法实施测试。自动化测试作为持续集成 (CI) 管道的一部分或在专用测试阶段进行安排和运行。 [Test environments](../T/test-environment.md) 配置为尽可能模仿生产。
  - **监控**：持续监控[test executions](../T/test-execution.md)和系统行为以捕获相关数据。使用仪表板和实时报告来跟踪进度并尽早发现问题。
  - **分析**：根据预定义的基准和 NFR 评估测试结果。根据调查结果对系统质量和用户体验的影响确定优先级。
  - **沟通**​​：与利益相关者分享简洁、可操作的报告。突出显示关键指标、潜在风险和改进建议。
  - **审查和调整**：测试后分析会议有助于完善测试策略。吸取的经验教训会反馈到迭代改进的规划中。
  在整个过程中，协作工具和问题跟踪系统用于保持可见性和控制。 [Non-functional testing](../N/non-functional-testing.md) 集成到**敏捷**工作流程中，确保它与冲刺目标和发布时间表保持一致。该方法是迭代的，具有连续的反馈循环，使测试活动适应不断变化的项目需求以及从持续测试工作中获得的见解。

- **规划**：定义非[functional requirements](../F/functional-requirements.md) (NFR) 并建立明确的测试目标。根据确定的非功能测试类型（例如性能、安全性、可用性）分配资源、设定时间表并选择适当的工具。
  - **执行**：使用选定的工具和方法实施测试。自动化测试作为持续集成 (CI) 管道的一部分或在专用测试阶段进行安排和运行。 [Test environments](../T/test-environment.md) 配置为尽可能模仿生产。
  - **监控**：持续监控[test executions](../T/test-execution.md)和系统行为以捕获相关数据。使用仪表板和实时报告来跟踪进度并尽早发现问题。
  - **分析**：根据预定义的基准和 NFR 评估测试结果。根据调查结果对系统质量和用户体验的影响确定优先级。
  - **沟通**​​：与利益相关者分享简洁、可操作的报告。突出显示关键指标、潜在风险和改进建议。
  - **审查和调整**：测试后分析会议有助于完善测试策略。吸取的经验教训会反馈到迭代改进的规划中。

#### 实施非功能测试有哪些挑战以及如何克服这些挑战？

实施[non-functional testing](../N/non-functional-testing.md) 面临多项挑战，包括**资源分配**、**环境[setup](../S/setup.md)**、**[test data](../T/test-data.md) 管理**和**工具选择**。克服这些需要战略规划和高效执行。
  **资源分配**可能是一个障碍，因为非功能测试（例如性能或[load testing](../L/load-testing.md)）的高要求，通常需要强大的基础设施。通过使用提供可扩展性和灵活性的**基于云的服务**来优化资源，或考虑**虚拟化**来模拟各种环境。
  **环境[setup](../S/setup.md)**至关重要，因为非功能测试需要镜像生产环境才能产生准确的结果。使用**基础架构即代码 (IaC)** 工具来自动化环境配置并确保一致性。
  **[Test data](../T/test-data.md) 管理** 由于所需数据的数量和种类而具有挑战性。实施**数据生成工具**和**数据脱敏**技术以有效创建真实且安全的数据集。
  **工具选择**必须符合您的测试目标。根据工具与您的技术堆栈的**兼容性**、**可扩展性**、**报告功能**和**社区支持**来评估工具。考虑使用开源选项以提高灵活性并节省成本。
  最后，将非功能测试集成到您的 **CI/CD 管道**中，以确保它们是常规测试过程的一部分。这有助于及早发现问题并减少反馈循环。定期审查和**更新[test cases](../T/test-case.md)**以反映用户行为和系统更新的变化。向利益相关者有效传达结果至关重要；使用**仪表板**和**自动化报告**清晰简洁地呈现数据。

#### 非功能测试的结果如何有效地传达给利益相关者？

向利益相关者有效传达[non-functional testing](../N/non-functional-testing.md)的结果涉及以清晰、简洁的方式呈现数据，突出对软件质量和用户体验的影响。使用图形和图表等**视觉辅助工具**来描述性能指标、安全漏洞或可用性问题。根据利益相关者的技术理解水平定制沟通；例如，管理人员可能更喜欢高级摘要，而技术主管可能需要详细的报告。
  提供结果如何影响业务目标、用户满意度或潜在风险的**上下文分析**。使用**仪表板**提供对正在进行的测试的实时见解，使利益相关者能够在发生时监控进度和结果。包括与正在测试的非功能方面相关的**关键[performance indicators](../P/performance-indicator.md) (KPI)**，例如响应时间、吞吐量、错误率或安全漏洞尝试。
  讨论问题时，重点关注 **[severity](../S/severity.md)** 和 **影响** 而不是技术细节。提供解决任何已发现问题的**建议**，包括潜在的改进或减轻风险的必要措施。确保沟通**可操作**，使利益相关者能够根据测试结果做出明智的决策。
  对于更多技术利益相关者，为了清晰起见，请使用代码块包含相关日志或指标的片段：

  ```
  Error Rate: 0.5% (Threshold: <0.1%)
  Response Time: 850ms (Threshold: <500ms)
  ```最后，提供整个系统准备情况的**摘要**以及发布前需要注意的任何问题，确保利益相关者了解 [non-functional testing](../N/non-functional-testing.md) 结果对项目成功的影响。
