# 灰盒测试

<!-- TOC START -->
- [相关术语：](#相关术语：)
  - [另请参阅：](#另请参阅：)
- [关于灰盒测试的问题吗？](#关于灰盒测试的问题吗？)
  - [基础知识和重要性](#基础知识和重要性)
    - [什么是灰盒测试？](#什么是灰盒测试？)
    - [为什么灰盒测试在软件测试中很重要？](#为什么灰盒测试在软件测试中很重要？)
    - [灰盒测试的主要优势是什么？](#灰盒测试的主要优势是什么？)
    - [灰盒测试与黑盒和白盒测试有何不同？](#灰盒测试与黑盒和白盒测试有何不同？)
  - [技术和工具](#技术和工具)
    - [灰盒测试中常用的技术有哪些？](#灰盒测试中常用的技术有哪些？)
    - [灰盒测试中经常使用哪些工具？](#灰盒测试中经常使用哪些工具？)
    - [灰盒测试如何实现自动化？](#灰盒测试如何实现自动化？)
    - [自动化灰盒测试面临哪些挑战？](#自动化灰盒测试面临哪些挑战？)
  - [实施和流程](#实施和流程)
    - [灰盒测试涉及哪些步骤？](#灰盒测试涉及哪些步骤？)
    - [如何设计灰盒测试的测试用例？](#如何设计灰盒测试的测试用例？)
    - [测试人员在灰盒测试中的角色是什么？](#测试人员在灰盒测试中的角色是什么？)
    - [您如何评估灰盒测试的有效性？](#您如何评估灰盒测试的有效性？)
  - [现实世界的应用](#现实世界的应用)
    - [您能提供灰盒测试的实际应用示例吗？](#您能提供灰盒测试的实际应用示例吗？)
    - [灰盒测试如何应用于敏捷开发？](#灰盒测试如何应用于敏捷开发？)
    - [灰盒测试在现实场景中发现的常见问题有哪些？](#灰盒测试在现实场景中发现的常见问题有哪些？)
    - [灰盒测试如何集成到 CI/CD 管道中？](#灰盒测试如何集成到-cicd-管道中？)
<!-- TOC END -->

灰盒测试

涉及在对其内部工作原理有部分了解的情况下测试应用程序。它的目的是识别源自代码结构或其应用程序的问题。

## 相关术语：

- [Black Box Testing](../B/black-box-testing.md)
- [White Box Testing](../W/white-box-testing.md)
- [Glass Box Testing](../G/glass-box-testing.md)

### 另请参阅：

- [Wikipedia](https://en.wikipedia.org/wiki/Gray-box_testing)

## 关于灰盒测试的问题吗？

### 基础知识和重要性

#### 什么是灰盒测试？

[Grey Box Testing](../G/grey-box-testing.md) 结合了 **黑盒** 和 **[white box testing](../W/white-box-testing.md)** 方法的元素，允许测试人员在了解应用程序内部工作原理的部分知识的情况下设计[test cases](../T/test-case.md)。测试人员利用接口定义和高级图表来创建可以探索软件功能和结构方面的测试。
  为了自动化[Grey Box Testing](../G/grey-box-testing.md)，测试人员经常编写与用户界面和[API](../A/api.md)/后端层交互的脚本。这些脚本可以用各种编程语言编写，并使用自动化框架执行。 [Grey Box Testing](../G/grey-box-testing.md) 中的自动化通常涉及：

- **[API testing](../A/api-testing.md) 工具**
    例如用于后端测试的 Postman 或 REST-assured。

- **UI自动化工具**
    例如用于前端测试的 Selenium 或 Cypress。

- **代码分析工具**
    识别潜在的安全漏洞或性能瓶颈。
  自动化测试旨在针对代码知识和用户体验交叉的特定领域。例如，测试人员可以编写一个脚本，将特制请求发送到 [API](../A/api.md) 端点，以测试 [SQL](../S/sql.md) 注入漏洞，将应用程序数据处理的知识与从用户角度的测试技术相结合。
  为了评估有效性，测试人员分析[test coverage](../T/test-coverage.md)、缺陷检测率以及识别安全和性能问题的能力。 [Grey Box Testing](../G/grey-box-testing.md) 在不需要完全了解系统但纯粹的黑盒方法不足以确保彻底测试的情况下特别有效。

- **[API testing](../A/api-testing.md) 工具**
    例如用于后端测试的 Postman 或 REST-assured。

- **UI自动化工具**
    例如用于前端测试的 Selenium 或 Cypress。

- **代码分析工具**
    识别潜在的安全漏洞或性能瓶颈。

#### 为什么灰盒测试在软件测试中很重要？

[Grey Box Testing](../G/grey-box-testing.md) 在[software testing](../S/software-testing.md) 中至关重要，因为它通过利用对系统内部工作原理的部分了解，弥合了 **[Black Box Testing](../B/black-box-testing.md)** 和 **[White Box Testing](../W/white-box-testing.md)** 之间的差距。这种方法使测试人员能够设计更有效的[test scenarios](../T/test-scenario.md)，将高级系统行为和低级操作结合起来。
  通过关注软件界面及其结构之间的交互，[Grey Box Testing](../G/grey-box-testing.md) 可以发现单独通过黑盒或白盒方法可能无法检测到的不同类别的缺陷。它提供了一个平衡的视角，可以发现与数据结构或 [databases](../D/database.md) 的不当使用相关的问题，以及用户界面级别的不正确行为。
  此外，[Grey Box Testing](../G/grey-box-testing.md) 对于评估系统的**非功能属性**（例如安全性、性能和可扩展性）非常重要。由于测试人员了解软件的架构，因此他们可以模拟各种用户行为和系统状态来评估软件在压力或攻击下的性能，而这通常是 [Black Box Testing](../B/black-box-testing.md) 无法实现的。
  从本质上讲，[Grey Box Testing](../G/grey-box-testing.md) 通过提供利用系统外部和内部视角的全面测试策略，对软件产品的**[quality assurance](../Q/quality-assurance.md)** 做出了重大贡献。它确保软件不仅能够按照规范正确运行，而且能够抵御意外情况和恶意活动。

#### 灰盒测试的主要优势是什么？

[Grey Box Testing](../G/grey-box-testing.md) 的主要优点包括：

- **结合优势**：利用高级黑盒和低级白盒视角，使测试人员能够专注于应用程序的用户界面及其内部工作原理。
  - **效率**：比白盒测试更高效，因为它不需要深入研究代码库，同时仍然比黑盒测试更具洞察力。
  - **[Security testing](../S/security-testing.md)** ：特别有效
    **[security testing](../S/security-testing.md)**
    ，因为它可以识别用户界面和代码级别的漏洞。

- **智能@@PR​​OTECTED_53@@设计**：允许创建基于系统架构和数据流知识的智能测试用例。
  - **非侵入式**：无需完全访问源代码即可进行测试，这在使用第三方组件时非常有用。
  - **更好的覆盖范围**：通过结合一些内部结构的知识，实现比黑盒测试更好的测试覆盖范围。
  - **早期识别缺陷**：有利于及早发现与应用程序的使用及其潜在误用相关的缺陷。
  - **减少冗余**：通过关注黑盒或白盒测试未覆盖的区域，有助于减少测试冗余。
  通过在软件的内部和外部视图之间取得平衡，[grey box testing](../G/grey-box-testing.md) 提供了一种全面的方法，可以实现更强大、更安全的应用程序。

- **结合优势**：利用高级黑盒和低级白盒视角，使测试人员能够专注于应用程序的用户界面及其内部工作原理。
  - **效率**：比白盒测试更高效，因为它不需要深入研究代码库，同时仍然比黑盒测试更具洞察力。
  - **[Security testing](../S/security-testing.md)** ：特别有效
    **[security testing](../S/security-testing.md)**
    ，因为它可以识别用户界面和代码级别的漏洞。

- **智能@@PR​​OTECTED_57@@设计**：允许创建基于系统架构和数据流知识的智能测试用例。
  - **非侵入式**：无需完全访问源代码即可进行测试，这在使用第三方组件时非常有用。
  - **更好的覆盖范围**：通过结合一些内部结构的知识，实现比黑盒测试更好的测试覆盖范围。
  - **早期识别缺陷**：有利于及早发现与应用程序的使用及其潜在误用相关的缺陷。
  - **减少冗余**：通过关注黑盒或白盒测试未覆盖的区域，有助于减少测试冗余。

#### 灰盒测试与黑盒和白盒测试有何不同？

[Grey Box Testing](../G/grey-box-testing.md) 结合了 **[Black Box Testing](../B/black-box-testing.md)** 和 **[White Box Testing](../W/white-box-testing.md)** 的元素。在[Black Box Testing](../B/black-box-testing.md)中，测试人员在不了解内部工作原理的情况下评估软件，仅关注输入和输出。另一方面，[White Box Testing](../W/white-box-testing.md) 需要对代码有深入的了解，因为测试人员需要访问源代码并了解软件的架构和实现。
  [Grey Box Testing](../G/grey-box-testing.md) 在两者之间取得了平衡。测试人员对内部数据结构和算法有部分了解，但他们无法完全访问代码。这种方法允许测试人员设计[test cases](../T/test-case.md)，更有效地发现与数据流和应用程序使用不当相关的问题，而这些问题在[Black Box Testing](../B/black-box-testing.md)中可能会被忽视。
  与 [White Box Testing](../W/white-box-testing.md) 不同，[White Box Testing](../W/white-box-testing.md) 测试人员需要了解代码的复杂性，[Grey Box Testing](../G/grey-box-testing.md) 需要较少的详细知识，这使得不熟悉代码库的测试人员更容易理解。它还允许采用比 [Black Box Testing](../B/black-box-testing.md) 更集中的测试方法，因为系统内部的一些知识可以指导测试过程。
  本质上，[Grey Box Testing](../G/grey-box-testing.md) 在[White Box Testing](../W/white-box-testing.md) 的广泛知识要求和[Black Box Testing](../B/black-box-testing.md) 的无知识方法之间提供了**务实的平衡**，使测试人员能够发现单独通过其他两种方法可能无法检测到的不同类别的缺陷。

### 技术和工具

#### 灰盒测试中常用的技术有哪些？

**[Grey Box Testing](../G/grey-box-testing.md)** 中的常用技术包括：

- **矩阵测试**：识别可能影响多个系统的变量并创建矩阵来测试不同的组合。
  - **[Regression Testing](../R/regression-testing.md)** ：确保新的更改不会对现有功能产生不利影响。
  - **模式测试**：分析过去的事件和缺陷以预测和测试未来潜在的错误。
  - **[Orthogonal Array Testing](../O/orthogonal-array-testing.md)** ：使用正交数组系统地识别测试用例中的变化。
  - **故障注入方法**：引入故障来测试系统在错误条件下的行为。
  - **基于状态的测试**：检查应用程序在不同状态下的行为以及状态之间的转换。
  这些技术利用了系统内部工作原理的部分知识，结合了黑匣子和[white box testing](../W/white-box-testing.md)的元素，以实现更全面的[test coverage](../T/test-coverage.md)。测试人员使用这些方法来关注通常不被纯黑或[white box testing](../W/white-box-testing.md)方法覆盖的领域，例如用户交互、系统状态以及外部因素对系统行为的影响。

- **矩阵测试**：识别可能影响多个系统的变量并创建矩阵来测试不同的组合。
  - **[Regression Testing](../R/regression-testing.md)** ：确保新的更改不会对现有功能产生不利影响。
  - **模式测试**：分析过去的事件和缺陷以预测和测试未来潜在的错误。
  - **[Orthogonal Array Testing](../O/orthogonal-array-testing.md)** ：使用正交数组系统地识别测试用例中的变化。
  - **故障注入方法**：引入故障来测试系统在错误条件下的行为。
  - **基于状态的测试**：检查应用程序在不同状态下的行为以及状态之间的转换。

#### 灰盒测试中经常使用哪些工具？

在 **[Grey Box Testing](../G/grey-box-testing.md)** 中，经常使用提供高级应用程序交互和一定程度的内部可见性的工具。常用工具包括：

- **[Selenium](../S/selenium.md)** ：用于 Web 应用程序测试，允许测试人员与应用程序交互，同时还访问浏览器控制台日志和网络流量。
  - **SoapUI**：可用于测试 Web 服务，提供对功能方面和通信层的深入了解。
  - **[Postman](../P/postman.md)** ：虽然主要用于 API 测试，但它也可以用于灰盒测试，以检查系统如何处理请求和响应。
  - **Burp Suite**：一种安全测试工具，可适用于灰盒方法，提供对应用程序数据流和潜在漏洞的洞察。
  - **Wireshark**：网络协议分析器，帮助测试人员了解应用程序和服务器之间的网络流量。
  - **Fiddler**：一种 Web 调试代理，允许检查 HTTP(S) 流量，可用于修改请求和分析响应。
  - **AppScan** ：IBM 的安全测试工具，可用于灰盒测试以识别安全漏洞。
  - **OWASP ZAP**：一种开源工具，用于在灰盒测试期间查找 Web 应用程序中的漏洞。
  这些工具使测试人员能够执行监视网络流量、分析应用程序日志和操作输入数据以观察系统行为等操作，这对于 [Grey Box Testing](../G/grey-box-testing.md) 至关重要。测试人员经常编写脚本或使用现有的测试框架来自动化这些工具，将它们集成到测试工作流程中。

- **[Selenium](../S/selenium.md)** ：用于 Web 应用程序测试，允许测试人员与应用程序交互，同时还访问浏览器控制台日志和网络流量。
  - **SoapUI**：可用于测试 Web 服务，提供对功能方面和通信层的深入了解。
  - **[Postman](../P/postman.md)** ：虽然主要用于 API 测试，但它也可以用于灰盒测试，以检查系统如何处理请求和响应。
  - **Burp Suite**：一种安全测试工具，可适用于灰盒方法，提供对应用程序数据流和潜在漏洞的洞察。
  - **Wireshark**：网络协议分析器，帮助测试人员了解应用程序和服务器之间的网络流量。
  - **Fiddler**：一种 Web 调试代理，允许检查 HTTP(S) 流量，可用于修改请求和分析响应。
  - **AppScan** ：IBM 的安全测试工具，可用于灰盒测试以识别安全漏洞。
  - **OWASP ZAP**：一种开源工具，用于在灰盒测试期间查找 Web 应用程序中的漏洞。

#### 灰盒测试如何实现自动化？

自动化[Grey Box Testing](../G/grey-box-testing.md)涉及**访问内部结构**和**外部测试技术**的组合。要自动化此过程，请按照下列步骤操作：

1. **识别可访问的内部信息**，例如 [database](../D/database.md) 模式、算法模式或内部状态，这可以指导创建更有效的[test cases](../T/test-case.md)。
  2. **开发利用内部信息和外部接口的[test cases](../T/test-case.md)**。使用脚本或编程语言创建可以与软件的 [API](../A/api.md)、Web 服务或其他公开接口进行交互的自动化脚本。
  3. **选择适当的自动化工具**，既支持 [API testing](../A/api-testing.md) 又支持整合内部知识，例如 [Postman](../P/postman.md) 用于 [API testing](../A/api-testing.md) 或 [Selenium](../S/selenium.md) 用于 Web 应用程序，并通过自定义脚本进行增强以利用内部信息。
  4. **编写执行[test cases](../T/test-case.md)的自动化脚本**，模拟用户行为，同时检查内部状态或数据。例如：

  ```
  // Pseudo-code for a Grey Box test script
  const internalData = getInternalDataStructure();
  const response = apiCall('/endpoint', { param: 'value' });
  assert(response.status, 200);
  assert(internalData.hasExpectedState(), true);
  ```

1. **将脚本集成到您的[test suite](../T/test-suite.md)** 并将它们配置为自动运行，可以按需运行，也可以由特定事件（例如代码提交或构建）触发。
  2. **分析测试结果**以确保外部行为和内部结构都按预期运行。使用 [test automation](../T/test-automation.md) 框架的日志记录和报告功能来捕获和查看结果。
  通过将内部工作知识与自动化外部测试相结合，[Grey Box Testing](../G/grey-box-testing.md) 可以有效地实现自动化，以提供对软件质量的全面评估。

1. **识别可访问的内部信息**，例如 [database](../D/database.md) 模式、算法模式或内部状态，它们可以指导创建更有效的[test cases](../T/test-case.md)。
  2. **开发利用内部信息和外部接口的[test cases](../T/test-case.md)**。使用脚本或编程语言创建可以与软件的 [API](../A/api.md)、Web 服务或其他公开接口进行交互的自动化脚本。
  3. **选择适当的自动化工具**，支持 [API testing](../A/api-testing.md) 和整合内部知识的能力，例如 [Postman](../P/postman.md) 用于 [API testing](../A/api-testing.md) 或 [Selenium](../S/selenium.md) 用于 Web 应用程序，并通过自定义脚本进行增强以利用内部信息。
  4. **编写执行[test cases](../T/test-case.md)的自动化脚本**，模拟用户行为，同时检查内部状态或数据。例如：
  1. **将脚本集成到您的[test suite](../T/test-suite.md)** 并将它们配置为自动运行，可以按需运行，也可以由代码提交或构建等特定事件触发。
  2. **分析测试结果**以确保外部行为和内部结构都按预期运行。使用 [test automation](../T/test-automation.md) 框架的日志记录和报告功能来捕获和查看结果。

#### 自动化灰盒测试面临哪些挑战？

自动化 [Grey Box Testing](../G/grey-box-testing.md) 提出了几个挑战：

- **对内部结构的有限访问**：与[white box testing](../W/white-box-testing.md)不同，[grey box testing](../G/grey-box-testing.md)不提供对应用程序内部工作的完全访问，这使得创建涵盖系统各个方面的全面[test cases](../T/test-case.md)变得困难。
  - **动态环境**：灰盒测试通常在比 [white box testing](../W/white-box-testing.md) 中使用的环境更具动态性和更少控制的环境中运行。这种差异可能会导致测试结果不一致。
  - **理解系统行为的复杂性**：测试人员必须很好地理解应用程序的界面及其部分内部结构。这种双重焦点会使测试设计和自动化变得复杂。
  - **与不同工具集成**：[Grey box testing](../G/grey-box-testing.md) 可能需要集成多个工具才能访问[databases](../D/database.md)、日志和内部[APIs](../A/api.md)。确保这些工具无缝协作可能具有挑战性。
  - **黑盒和白盒方法之间的平衡**：在[grey box testing](../G/grey-box-testing.md) 中使用黑盒和[white box testing](../W/white-box-testing.md) 技术之间找到适当的平衡可能很困难。过度依赖一种方法可能会导致[test coverage](../T/test-coverage.md) 中出现空白。
  - **测试维护**：与任何[automated testing](../A/automated-testing.md) 一样，随着应用程序的发展维护[test scripts](../T/test-script.md) 可能非常耗时。灰盒测试可能需要更新以适应用户界面和底层架构的变化。
  - **[Performance testing](../P/performance-testing.md)**：[Grey box testing](../G/grey-box-testing.md) 通常包括[performance testing](../P/performance-testing.md)，由于需要模拟实际的用户行为和系统负载，自动化可能很复杂。
  应对这些挑战需要仔细规划、深入了解被测系统以及选择适当的工具和技术，以确保 [grey box testing](../G/grey-box-testing.md) 既有效又高效。

- **对内部结构的有限访问**：与[white box testing](../W/white-box-testing.md) 不同，[grey box testing](../G/grey-box-testing.md) 不提供对应用程序内部工作的完全访问权限，因此很难创建涵盖系统各个方面的全面[test cases](../T/test-case.md)。
  - **动态环境**：灰盒测试通常在比 [white box testing](../W/white-box-testing.md) 中使用的环境更具动态性和更少控制的环境中运行。这种差异可能会导致测试结果不一致。
  - **理解系统行为的复杂性**：测试人员必须很好地理解应用程序的界面及其部分内部结构。这种双重焦点会使测试设计和自动化变得复杂。
  - **与不同工具集成**：[Grey box testing](../G/grey-box-testing.md) 可能需要集成多个工具才能访问[databases](../D/database.md)、日志和内部[APIs](../A/api.md)。确保这些工具无缝协作可能具有挑战性。
  - **黑盒和白盒方法之间的平衡**：在[grey box testing](../G/grey-box-testing.md) 中使用黑盒和[white box testing](../W/white-box-testing.md) 技术之间找到适当的平衡可能很困难。过度依赖一种方法可能会导致[test coverage](../T/test-coverage.md) 中出现空白。
  - **测试维护**：与任何[automated testing](../A/automated-testing.md) 一样，随着应用程序的发展维护[test scripts](../T/test-script.md) 可能非常耗时。灰盒测试可能需要更新以适应用户界面和底层架构的变化。
  - **[Performance testing](../P/performance-testing.md)**：[Grey box testing](../G/grey-box-testing.md) 通常包括[performance testing](../P/performance-testing.md)，由于需要模拟实际的用户行为和系统负载，自动化可能很复杂。

### 实施和流程

#### 灰盒测试涉及哪些步骤？

[Grey Box Testing](../G/grey-box-testing.md) 涉及黑盒知识和[White Box testing](../W/white-box-testing.md) 方法的组合来设计和执行测试。以下是所涉及的典型步骤：

1. **了解系统架构**：部分了解内部工作原理，包括[database](../D/database.md)模式、代码访问路径等。
  2. **识别用户角色和权限**：确定不同的用户角色以了解系统在不同访问级别下的行为。
  3. **制定测试策略**：将架构知识与外部行为相结合，创建涵盖功能和结构方面的稳健测试策略。
  4. **创建[test cases](../T/test-case.md)**：开发[test cases](../T/test-case.md)，重点关注系统输入和输出，以及内部程序状态和数据结构。
  5. **准备[test environment](../T/test-environment.md)**：设置一个与生产环境非常相似的环境，包括[databases](../D/database.md)、服务器和网络配置。
  6. **执行[test cases](../T/test-case.md)**：运行测试，监视应用程序的外部行为和内部事件。
  7. **监控系统行为**：使用调试工具和日志来观察[test execution](../T/test-execution.md)期间的系统行为。
  8. **分析结果**：根据 [expected results](../E/expected-result.md) 评估结果的功能正确性和正确的内部操作。
  9. **报告结果**：记录任何缺陷或问题，包括它们对系统功能和性能的影响。
  10. **迭代**：根据发现细化[test cases](../T/test-case.md)，并根据需要重新测试。
  在整个过程中，在不了解系统的完整内部结构（如[Black Box Testing](../B/black-box-testing.md)）和了解其工作原理（如[White Box Testing](../W/white-box-testing.md)）之间保持平衡。

1. **了解系统架构**：部分了解内部工作原理，包括[database](../D/database.md)模式、代码访问路径等。
  2. **识别用户角色和权限**：确定不同的用户角色以了解系统在不同访问级别下的行为。
  3. **制定测试策略**：将架构知识与外部行为相结合，创建涵盖功能和结构方面的稳健测试策略。
  4. **创建[test cases](../T/test-case.md)**：开发[test cases](../T/test-case.md)，重点关注系统输入和输出，以及内部程序状态和数据结构。
  5. **准备[test environment](../T/test-environment.md)**：设置一个与生产环境非常相似的环境，包括[databases](../D/database.md)、服务器和网络配置。
  6. **执行[test cases](../T/test-case.md)**：运行测试，监视应用程序的外部行为和内部事件。
  7. **监控系统行为**：使用调试工具和日志来观察[test execution](../T/test-execution.md)期间的系统行为。
  8. **分析结果**：根据 [expected results](../E/expected-result.md) 评估结果的功能正确性和正确的内部操作。
  9. **报告结果**：记录任何缺陷或问题，包括它们对系统功能和性能的影响。
  10. **迭代**：根据发现细化[test cases](../T/test-case.md)，并根据需要重新测试。

#### 如何设计灰盒测试的测试用例？

为[Grey Box Testing](../G/grey-box-testing.md) 设计[test cases](../T/test-case.md) 涉及黑盒和[White Box Testing](../W/white-box-testing.md) 方法的组合。这是一个简洁的指南：

1. **了解系统架构**：部分了解内部工作原理、数据流和结构。
  2. **识别用户角色和权限**：[Test cases](../T/test-case.md) 应涵盖不同的用户角色及其与系统的交互。
  3. **使用接口和[API](../A/api.md)文档**：创建与系统的[APIs](../A/api.md)和接口交互的测试，确保它们按预期运行。
  4. **关注集成点**：关注不同组件或系统交互的区域。
  5. **利用错误消息和日志**：使用它们来了解测试中系统的行为并完善您的[test cases](../T/test-case.md)。
  6. **实施基于状态的测试**：根据应用程序可能处于的不同状态以及它们之间的转换来设计[test cases](../T/test-case.md)。
  7. **应用[database](../D/database.md) 测试技术**：包括与[database](../D/database.md) 交互的测试，以验证数据完整性和事务。
  8. **考虑安全方面**：测试 [SQL](../S/sql.md) 注入和跨站点脚本等漏洞。
  9. **使用智能@@PR​​OTECTED_79@@**：生成反映现实场景和边缘情况的[test data](../T/test-data.md)。
  10. **自动化回归测试**：确保系统更改后核心功能按预期工作。
  11. **确定关键路径的优先级**：专注于最重要的功能和用户旅程。
  12. **监控性能**：包括测量负载下的响应时间和系统行为的测试。
  当您对系统行为有更多了解并添加新功能时，请记住迭代和完善[test cases](../T/test-case.md)。

1. **了解系统架构**：部分了解内部工作原理、数据流和结构。
  2. **识别用户角色和权限**：[Test cases](../T/test-case.md) 应涵盖不同的用户角色及其与系统的交互。
  3. **使用接口和[API](../A/api.md)文档**：创建与系统的[APIs](../A/api.md)和接口交互的测试，确保它们按预期运行。
  4. **关注集成点**：关注不同组件或系统交互的区域。
  5. **利用错误消息和日志**：使用它们来了解测试中系统的行为并完善您的[test cases](../T/test-case.md)。
  6. **实施基于状态的测试**：根据应用程序可能处于的不同状态以及它们之间的转换来设计[test cases](../T/test-case.md)。
  7. **应用[database](../D/database.md) 测试技术**：包括与[database](../D/database.md) 交互的测试，以验证数据完整性和事务。
  8. **考虑安全方面**：测试 [SQL](../S/sql.md) 注入和跨站点脚本等漏洞。
  9. **使用智能@@PR​​OTECTED_90@@**：生成反映现实场景和边缘情况的[test data](../T/test-data.md)。
  10. **自动化回归测试**：确保系统更改后核心功能按预期工作。
  11. **确定关键路径的优先级**：专注于最重要的功能和用户旅程。
  12. **监控性能**：包括测量负载下的响应时间和系统行为的测试。

#### 测试人员在灰盒测试中的角色是什么？

在 **[Grey Box Testing](../G/grey-box-testing.md)** 中，测试人员的角色是多方面的，结合了应用程序内部工作及其外部接口的知识。测试人员必须：

- 了解
    **部分内部结构**
    应用程序的信息，包括数据库模式和内部状态。

- 设计
    **[test cases](../T/test-case.md)**
    针对应用程序的特定领域，由高级架构和详细设计文档提供信息。

- 利用
    **接口驱动**
    测试技术，重点关注 API、Web 服务和其他端点。

- 申请
    **情境知识**
    识别和测试组件之间的集成点和数据流。

- 执行测试来评估
    **功能性**
    和
    **不起作用**
    系统的各个方面，例如性能和安全性。

- 与开发人员和黑盒测试人员合作，确保全面覆盖和理解系统。
  - 分析结果并
    **识别差异**
    在预期行为和实际行为之间，需要外部行为观察和内部逻辑理解之间的平衡。

- 使用
    **调试工具**
    和
    **日志**
    利用他们对系统内部结构的了解，在测试失败时跟踪问题。

- 提供
    **反馈**
    为开发和测试团队提供更有针对性、更高效的问题解决方法。
  测试人员必须善于在对系统了解太少和太多之间找到中间立场，利用他们的部分知识来最大限度地提高测试效率，而不会被通常为白盒测试保留的细节所困扰。

- 了解
    **部分内部结构**
    应用程序的信息，包括数据库模式和内部状态。

- 设计
    **[test cases](../T/test-case.md)**
    针对应用程序的特定领域，由高级架构和详细设计文档提供信息。

- 利用
    **接口驱动**
    测试技术，重点关注 API、Web 服务和其他端点。

- 申请
    **情境知识**
    识别和测试组件之间的集成点和数据流。

- 执行测试来评估
    **功能性**
    和
    **不起作用**
    系统的各个方面，例如性能和安全性。

- 与开发人员和黑盒测试人员合作，确保全面覆盖和理解系统。
  - 分析结果并
    **识别差异**
    在预期行为和实际行为之间，需要外部行为观察和内部逻辑理解之间的平衡。

- 使用
    **调试工具**
    和
    **日志**
    利用他们对系统内部结构的了解，在测试失败时跟踪问题。

- 提供
    **反馈**
    为开发和测试团队提供更有针对性、更高效的问题解决方法。

#### 您如何评估灰盒测试的有效性？

评估[Grey Box Testing](../G/grey-box-testing.md) 的有效性涉及评估测试的**覆盖率** 和**质量**。可以通过确定测试对应用程序的不同路径和状态进行测试的程度来测量覆盖范围，通常结合使用**[code coverage](../C/code-coverage.md) 工具**和**基于状态的分析**。另一方面，质量取决于发现的缺陷数量、这些缺陷的[severity](../S/severity.md)，以及测试与用户期望和要求的一致性程度。
  衡量有效性：

- **跟踪缺陷发现**：记录测试期间发现的缺陷的数量和严重程度。严重缺陷的高检出率可能表明测试效果良好。
  - **测量[Code Coverage](../C/code-coverage.md)** ：使用工具测量测试期间执行的代码的百分比。目标是高覆盖率，同时认识到 100% 并不总是可行或必要的。
  - **分析测试结果**：查看模式的测试结果。特定领域的频繁失败可能表明存在更系统性的问题。
  - **评估测试维护**：考虑维护测试所需的工作量。过于复杂或脆弱的测试可能会降低整体有效性。
  - **检查测试相关性**：确保测试与应用程序的用例和用户故事保持相关。不相关的测试会浪费资源并影响有效性指标。
  - **反馈循环**：与开发人员和利益相关者实施反馈循环，以确保测试提供价值并根据获得的见解完善测试方法。
  通过关注这些领域，您可以全面了解您[Grey Box Testing](../G/grey-box-testing.md) 工作的有效性。

- **跟踪缺陷发现**：记录测试期间发现的缺陷的数量和严重程度。严重缺陷的高检出率可能表明测试效果良好。
  - **测量[Code Coverage](../C/code-coverage.md)** ：使用工具测量测试期间执行的代码的百分比。目标是高覆盖率，同时认识到 100% 并不总是可行或必要的。
  - **分析测试结果**：查看模式的测试结果。特定领域的频繁失败可能表明存在更系统性的问题。
  - **评估测试维护**：考虑维护测试所需的工作量。过于复杂或脆弱的测试可能会降低整体有效性。
  - **检查测试相关性**：确保测试与应用程序的用例和用户故事保持相关。不相关的测试会浪费资源并影响有效性指标。
  - **反馈循环**：与开发人员和利益相关者实施反馈循环，以确保测试提供价值并根据获得的见解完善测试方法。

### 现实世界的应用

#### 您能提供灰盒测试的实际应用示例吗？

**[Grey Box Testing](../G/grey-box-testing.md)** 的实际应用程序通常涉及了解应用程序的接口及其底层结构是有益的。以下是一些示例：

1. **Web 应用程序安全**：[Grey box testing](../G/grey-box-testing.md) 用于评估安全漏洞，例如[SQL](../S/sql.md) 注入、跨站点脚本和会话管理缺陷。测试人员对架构的了解有限，并通过模拟攻击来识别安全漏洞。
  2. **[API Testing](../A/api-testing.md)**：测试[APIs](../A/api.md)时，采用灰盒方法来验证响应和数据结构。测试人员可以访问 [API](../A/api.md) 文档，并且可以制作超越简单黑盒输入输出验证的测试。
  3. **[Integration Testing](../I/integration-testing.md)**：在[integration testing](../I/integration-testing.md)中，灰盒技术有助于验证集成组件之间的数据流和交互。测试人员可能了解 [database](../D/database.md) 模式或消息队列系统来创建更有洞察力的测试。
  4. **[Performance Testing](../P/performance-testing.md)**：[Grey box testing](../G/grey-box-testing.md) 用于监视负载下的系统行为。测试人员可以利用系统架构的知识来识别瓶颈或内存泄漏。
  5. **[Database](../D/database.md) 测试**：测试人员使用灰盒方法来验证数据完整性和一致性。他们可能了解[database](../D/database.md) 架构，可以编写更有针对性的[SQL](../S/sql.md) 查询来进行测试。
  通过结合外部和内部视角，[grey box testing](../G/grey-box-testing.md)提供了一种平衡的方法，可以发现纯黑或[white box testing](../W/white-box-testing.md)方法可能遗漏的问题。

1. **Web 应用程序安全**：[Grey box testing](../G/grey-box-testing.md) 用于评估安全漏洞，例如[SQL](../S/sql.md) 注入、跨站点脚本和会话管理缺陷。测试人员对架构的了解有限，并通过模拟攻击来识别安全漏洞。
  2. **[API Testing](../A/api-testing.md)**：测试[APIs](../A/api.md)时，采用灰盒方法来验证响应和数据结构。测试人员可以访问[API](../A/api.md) 文档，并且可以制作超越简单黑盒输入输出验证的测试。
  3. **[Integration Testing](../I/integration-testing.md)**：在[integration testing](../I/integration-testing.md)中，灰盒技术有助于验证集成组件之间的数据流和交互。测试人员可能知道 [database](../D/database.md) 模式或消息队列系统来创建更有洞察力的测试。
  4. **[Performance Testing](../P/performance-testing.md)**：[Grey box testing](../G/grey-box-testing.md) 用于监视负载下的系统行为。测试人员可以利用系统架构的知识来识别瓶颈或内存泄漏。
  5. **[Database](../D/database.md) 测试**：测试人员使用灰盒方法来验证数据完整性和一致性。他们可能了解 [database](../D/database.md) 架构，可以编写更有针对性的 [SQL](../S/sql.md) 查询来进行测试。

#### 灰盒测试如何应用于敏捷开发？

在 **[Agile development](../A/agile-development.md)** 中，[Grey Box Testing](../G/grey-box-testing.md) 被迭代且增量地应用，与 **冲刺周期** 保持一致。对应用程序内部工作原理有部分了解的测试人员创建的测试将用户视角与内部结构洞察相结合。
  在每个冲刺期间，测试人员：

- **协作**
    与开发人员一起了解可能影响测试的系统架构或代码的变化。

- **更新**
    现有的测试用例反映应用程序中的任何新功能或更改。

- **执行**
    灰盒测试可验证功能行为以及与底层组件的交互。

- **分析**
    测试结果可识别黑盒测试中不明显的潜在安全问题、集成问题或数据流问题。

- **提供反馈**
    快速反馈给开发团队，确保问题可以在冲刺内得到解决。
  测试人员使用**[API](../A/api.md) 调用**、**[database](../D/database.md) 查询**和**代码分析**来制作超越用户界面的[test scenarios](../T/test-scenario.md)。通过这样做，他们可以查明集成级别和应用程序堆栈各层之间的弱点。
  敏捷中的 [Grey Box Testing](../G/grey-box-testing.md) 通常使用支持功能性和 [non-functional testing](../N/non-functional-testing.md) 的工具实现自动化，例如用于 Web 应用程序的 **[Selenium](../S/selenium.md)** 或用于 [API testing](../A/api-testing.md) 的 **[Postman](../P/postman.md)**。自动化脚本与应用程序代码一起在版本控制中维护，确保它们随着应用程序的发展而更新。
  将[Grey Box Testing](../G/grey-box-testing.md) 纳入**持续集成 (CI)** 管道至关重要。每次构建都会触发自动灰盒测试，提供有关最近更改影响的即时反馈，从而支持**持续改进**的敏捷原则。

- **协作**
    与开发人员一起了解可能影响测试的系统架构或代码的变化。

- **更新**
    现有的测试用例反映应用程序中的任何新功能或更改。

- **执行**
    灰盒测试可验证功能行为以及与底层组件的交互。

- **分析**
    测试结果可识别黑盒测试中不明显的潜在安全问题、集成问题或数据流问题。

- **提供反馈**
    快速反馈给开发团队，确保问题可以在冲刺内得到解决。

#### 灰盒测试在现实场景中发现的常见问题有哪些？

**[Grey Box Testing](../G/grey-box-testing.md)** 中的常见问题通常与应用程序内部工作的部分知识有关。以下是一些现实世界的挑战：

- **有限的覆盖范围**：测试人员可能无法完全访问源代码，从而导致测试覆盖范围存在潜在差距。
  - **理解的复杂性**：需要在高级架构和详细的内部行为之间实现知识的平衡，这可能很难实现。
  - **对文档的依赖**：测试通常基于架构图和技术文档，这些文档可能已过时或不准确。
  - **集成挑战**：灰盒测试可能需要复杂的设置才能与用户界面和后端交互，这可能非常耗时。
  - **安全约束**：对系统某些部分的访问可能受到限制，从而限制了测试的深度。
  - **性能开销**：对系统进行灰盒测试可能会带来不反映实际使用情况的性能开销。
  - **结果不明确**：如果没有对系统的全面了解，就很难解释某些测试结果或区分预期行为和意外行为。
  在实践中，这些问题需要在系统内部知识和外部行为之间取得仔细的平衡，要求测试人员善于在黑盒和[white box testing](../W/white-box-testing.md)方法之间找到中间立场。

- **有限的覆盖范围**：测试人员可能无法完全访问源代码，从而导致测试覆盖范围存在潜在差距。
  - **理解的复杂性**：需要在高级架构和详细的内部行为之间实现知识的平衡，这可能很难实现。
  - **对文档的依赖**：测试通常基于架构图和技术文档，这些文档可能已过时或不准确。
  - **集成挑战**：灰盒测试可能需要复杂的设置才能与用户界面和后端交互，这可能非常耗时。
  - **安全约束**：对系统某些部分的访问可能受到限制，从而限制了测试的深度。
  - **性能开销**：对系统进行灰盒测试可能会带来不反映实际使用情况的性能开销。
  - **结果不明确**：如果没有对系统的全面了解，就很难解释某些测试结果或区分预期行为和意外行为。

#### 灰盒测试如何集成到 CI/CD 管道中？

将 [Grey Box Testing](../G/grey-box-testing.md) 集成到 CI/CD 管道中涉及自动和手动步骤的组合，以确保彻底的覆盖和高效的测试。这是一个简洁的指南：

1. **识别[test cases](../T/test-case.md)**
    涵盖功能和内部结构，重点关注白盒测试和黑盒测试重叠的领域。

2. **自动化**
    如有可能。使用可以与用户界面和 API/数据库层交互的脚本或工具。

3. **配置**
    您的 CI/CD 工具可在构建后或部署到临时环境后触发灰盒测试。

4. **运行测试**
    为了节省时间，并行使用容器化或虚拟化来模拟不同的环境。

5. **分析结果**
    结合自动报告和手动审查来了解任何故障或异常的背景。

6. **调整[test cases](../T/test-case.md)**
    以及基于反馈和代码更改的脚本，以保持测试的相关性和有效性。

7. **监控**
    持续关注灰盒测试可能检测到的性能、安全性和集成问题。

8. **文件**
    发现并确保知识在团队内共享，以改进整体测试策略。

  ```
  stages:
    - build
    - test
    - deploy
  grey_box_test:
    stage: test
    script:
      - echo "Running Grey Box Tests..."
      - ./run_grey_box_tests.sh
    only:
      - master
      - develop
  ```在脚本`run_grey_box_tests.sh` 中，包含用于执行[Grey Box testing](../G/grey-box-testing.md) 套件的命令。确保将管道配置为在检测到严重问题时出现故障，从而立即引起注意。

1. **识别[test cases](../T/test-case.md)**
    涵盖功能和内部结构，重点关注白盒测试和黑盒测试重叠的领域。

2. **自动化**
    如有可能。使用可以与用户界面和 API/数据库层交互的脚本或工具。

3. **配置**
    您的 CI/CD 工具可在构建后或部署到临时环境后触发灰盒测试。

4. **运行测试**
    为了节省时间，并行使用容器化或虚拟化来模拟不同的环境。

5. **分析结果**
    结合自动报告和手动审查来了解任何故障或异常的背景。

6. **调整[test cases](../T/test-case.md)**
    以及基于反馈和代码更改的脚本，以保持测试的相关性和有效性。

7. **监控**
    持续关注灰盒测试可能检测到的性能、安全性和集成问题。

8. **文件**
    发现并确保知识在团队内共享，以改进整体测试策略。
