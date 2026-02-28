# 实际结果

<!-- TOC START -->
- [对实际结果有疑问吗？](#对实际结果有疑问吗？)
  - [基础知识和重要性](#基础知识和重要性)
    - [软件测试中“实际结果”的定义是什么？](#软件测试中实际结果的定义是什么？)
    - [为什么确定“实际结果”在 e2e 测试中很重要？](#为什么确定实际结果在-e2e-测试中很重要？)
  - [比较和对比](#比较和对比)
    - [在什么情况下“实际结果”可能与“预期结果”不同？](#在什么情况下实际结果可能与预期结果不同？)
  - [实际应用](#实际应用)
    - [测试过程中如何记录“实际结果”？](#测试过程中如何记录实际结果？)
    - [用于捕获“实际结果”的常用工具或方法有哪些？](#用于捕获实际结果的常用工具或方法有哪些？)
    - [如何使用“实际结果”来识别和诊断软件错误或问题？](#如何使用实际结果来识别和诊断软件错误或问题？)
  - [高级概念](#高级概念)
<!-- TOC END -->

（又名结果）

这

实际结果

是进行测试后获得的结果。在测试阶段，

实际结果

与

测试用例

。所有测试结束后，将其与预期结果进行比较，记录任何差异。

## 对实际结果有疑问吗？

### 基础知识和重要性

#### 软件测试中“实际结果”的定义是什么？

在[software testing](../S/software-testing.md) 中，**[Actual Result](../A/actual-result.md)** 是执行测试时观察到的行为。它是执行测试步骤后应用程序的输出、响应或状态。然后将此结果与 **[Expected Result](../E/expected-result.md)** 进行比较，以确定测试是否通过或失败。 [Actual Results](../A/actual-result.md) 对于识别可能表明软件缺陷或需要改进的区域的差异至关重要。

  ```
  // Example of capturing Actual Result in an automated test script
  const actualResult = await page.title();
  expect(actualResult).toEqual(expectedTitle);
  ```[Actual Results](../A/actual-result.md) 通常记录在 [test management](../T/test-management.md) 工具中或直接记录在自动化测试的代码中。它们作为 [test execution](../T/test-execution.md) 的证据，对于测试过程中的可追溯性和问责制至关重要。当[Actual Results](../A/actual-result.md) 偏离[Expected Results](../E/expected-result.md) 时，它们会触发调查，从而导致[bug](../B/bug.md) 修复和增强，确保软件满足其预期要求和功能。

#### 为什么确定“实际结果”在 e2e 测试中很重要？

确定端到端 (e2e) 测试中的 **[Actual Result](../A/actual-result.md)** 对于验证**整个应用程序流程**的完整性至关重要。它确保每个集成组件从开始到结束按顺序运行时都能按预期运行。通过比较[Actual Result](../A/actual-result.md) 和[Expected Result](../E/expected-result.md)，测试人员可以确认系统在各种条件下是否按设计运行，包括**用户交互、数据处理和连接**。
  在 e2e 测试中，[Actual Result](../A/actual-result.md) 是 [test execution](../T/test-execution.md)** 的 **结果。它为评估系统是否符合业务要求和用户需求提供了**具体的基础**。当出现差异时，他们会突出显示可能影响用户体验或系统可靠性的**潜在问题**，从而促使进一步调查和完善。
  此外，[Actual Result](../A/actual-result.md) 有助于**维护测试可信度**。它为利益相关者提供了有关系统当前状态和测试策略有效性的切实证据。这种透明度对于**建立对软件质量的信心**以及做出有关发布和部署的明智决策至关重要。
  在[automated testing](../A/automated-testing.md) 中，捕获[Actual Result](../A/actual-result.md) 通常由自动化框架处理，该框架记录结果以供后续分析。这种**自动捕获**不仅简化了测试过程，而且**减少了人为错误**，确保报告结果一致且准确。

  ```
  // Example of capturing Actual Result in an automated test
  const actualResult = await performTestAction();
  assert.equal(actualResult, expectedResult, 'The actual result does not match the expected result.');
  ```通过关注[Actual Result](../A/actual-result.md)，[test automation](../T/test-automation.md) 工程师可以**直接影响**软件的开发周期，确保每个版本都满足成功产品所需的质量标准。

#### “实际结果”对整个测试过程有何贡献？

**[Actual Result](../A/actual-result.md)** 在测试过程中至关重要，因为它可直接指示系统在测试条件下的当前行为。通过比较[Actual Result](../A/actual-result.md) 和[Expected Result](../E/expected-result.md)，测试人员可以立即辨别[test case](../T/test-case.md) 是通过还是失败。这种比较对于验证软件的功能并确保其满足指定的要求至关重要。
  在[automated testing](../A/automated-testing.md) 中，[Actual Result](../A/actual-result.md) 通常由[test scripts](../T/test-script.md) 捕获并记录，然后自动将其与[Expected Result](../E/expected-result.md) 进行比较。这有利于快速反馈循环，允许快速识别故障并支持持续集成和交付管道根据测试结果继续或停止。
  当出现差异时，[Actual Result](../A/actual-result.md) 是调试的起点。它有助于查明缺陷的确切性质，指导开发人员找到根本原因。此外，跨多个测试运行分析[Actual Results](../A/actual-result.md) 中的模式可以揭示更大的问题，例如应用程序某些区域的性能下降或不稳定。
  总之，[Actual Result](../A/actual-result.md) 对于以下方面至关重要：

- **验证**
    软件行为违背预期。

- **自动化**
    测试脚本中的通过/失败决策。

- **调试**
    通过提供系统行为的具体证据。

- **分析**
    趋势和模式为未来的开发和测试工作提供信息。
  通过有效利用[Actual Result](../A/actual-result.md)，团队可以保持高[software quality](../S/software-quality.md)并加速开发生命周期。

- **验证**
    软件行为违背预期。

- **自动化**
    测试脚本中的通过/失败决策。

- **调试**
    通过提供系统行为的具体证据。

- **分析**
    趋势和模式为未来的开发和测试工作提供信息。

### 比较和对比

#### “预期结果”和“实际结果”有什么区别？

在软件[test automation](../T/test-automation.md) 中，**[Expected Result](../E/expected-result.md)** 是[test case](../T/test-case.md) 的预定义结果，基于要求或设计规范。它代表系统在特定条件下应表现出的行为。
  另一方面，**[Actual Result](../A/actual-result.md)** 是执行[test case](../T/test-case.md) 时系统实际表现出的行为。它是从被测系统获得的实时结果。
  预期和[Actual Results](../A/actual-result.md) 之间的比较对于确定[test case](../T/test-case.md) 的成功或失败至关重要。匹配表明系统的行为符合预期，而不匹配则可能揭示出缺陷或与预期行为的偏差。这种比较通常在[test scripts](../T/test-script.md) 中自动进行，其中使用断言或检查点来验证[Actual Result](../A/actual-result.md) 与[Expected Result](../E/expected-result.md) 是否一致。

  ```
  // Example of an assertion in a test script
  assert.equal(actualResult, expectedResult, 'The actual result does not match the expected result');
  ```这些结果之间的差异会触发进一步调查，以了解根本原因并纠正任何问题，确保软件符合其质量标准。

#### “实际结果”与“测试用例”有何关系？

在 **[Test Case](../T/test-case.md)** 上下文中，**[Actual Result](../A/actual-result.md)** 是执行测试时观察到的结果。它直接与 **[Expected Result](../E/expected-result.md)** 进行比较，以确定测试是否通过或失败。这种比较对于验证被测软件的行为至关重要。
  对于自动化测试，**[Actual Result](../A/actual-result.md)** 通常由 [test script](../T/test-script.md) 本身捕获。例如，在基于 [Selenium](../S/selenium.md) 的测试中，脚本可能包含如下断言：

  ```
  assertEquals("Expected text", element.getText());
  ```此处，`element.getText()` 是与预期文本进行比较的 **[Actual Result](../A/actual-result.md)**。如果它们匹配，则测试通过；否则，就会失败。
  **[Actual Result](../A/actual-result.md)** 对于查明 **[Test Case](../T/test-case.md)** 中发生故障的确切步骤至关重要。在复杂的场景中，它有助于将缺陷隔离到特定的模块或功能。此外，当测试失败时，**[Actual Result](../A/actual-result.md)** 可以深入了解[bug](../B/bug.md) 的性质，这有助于调试和解决问题。
  在持续集成环境中，**[Actual Result](../A/actual-result.md)** 通常会被记录并成为[test reports](../T/test-report.md) 的一部分。此信息对于利益相关者了解软件的当前状态以及开发人员在软件发布之前解决任何问题非常有价值。

#### 在什么情况下“实际结果”可能与“预期结果”不同？

由于各种原因，**[Actual Result](../A/actual-result.md)** 可能与 **[Expected Result](../E/expected-result.md)** 不同：

- **代码缺陷**：应用程序代码中的错误可能会导致意外行为。
  - **环境问题**：测试环境中的差异，例如配置、数据库或网络条件的差异。
  - **[Test Data](../T/test-data.md) 变异性**：不一致或不正确的测试数据可能会产生不同的结果。
  - **[Flaky Tests](../F/flaky-test.md)** ：表现出不确定性行为的测试通常会间歇性失败。
  - **不正确的期望**：预期结果可能基于过时或误解的要求。
  - **并发问题**：仅当多个进程或用户同时与系统交互时才会出现的问题。
  - **集成依赖项**：应用程序依赖的外部服务或组件出现故障。
  - **计时问题**：影响应用程序行为的竞争条件或超时。
  - **平台特定行为**：不同操作系统、浏览器或设备处理某些操作的方式存在差异。
  - **[Test Script](../T/test-script.md) 错误**：自动化脚本本身的错误，例如不正确的断言或同步问题。
  找出差异的原因对于解决问题和改进[software quality](../S/software-quality.md) 至关重要。

- **代码缺陷**：应用程序代码中的错误可能会导致意外行为。
  - **环境问题**：测试环境中的差异，例如配置、数据库或网络条件的差异。
  - **[Test Data](../T/test-data.md) 变异性**：不一致或不正确的测试数据可能会产生不同的结果。
  - **[Flaky Tests](../F/flaky-test.md)** ：表现出非确定性行为的测试通常会间歇性失败。
  - **不正确的期望**：预期结果可能基于过时或误解的要求。
  - **并发问题**：仅当多个进程或用户同时与系统交互时才会出现的问题。
  - **集成依赖项**：应用程序依赖的外部服务或组件出现故障。
  - **计时问题**：影响应用程序行为的竞争条件或超时。
  - **平台特定行为**：不同操作系统、浏览器或设备处理某些操作的方式存在差异。
  - **[Test Script](../T/test-script.md) 错误**：自动化脚本本身的错误，例如不正确的断言或同步问题。

### 实际应用

#### 测试过程中如何记录“实际结果”？

在测试过程中记录 **[Actual Result](../A/actual-result.md)** 通常需要对 [test execution](../T/test-execution.md) 之后的系统行为进行清晰、简洁的描述。它记录在 [test management](../T/test-management.md) 工具或 [test case](../T/test-case.md) 文档中，通常与相应的 **[Test Case](../T/test-case.md)** 和 **[Expected Result](../E/expected-result.md)** 一起记录，以便于比较。
  这是一个一般方法：

1. **执行[Test Case](../T/test-case.md)**：按照概述的步骤运行测试。
  2. **观察**：仔细观察系统的行为或输出。
  3. **记录**：立即记录观察到的行为。使用清晰的语言描述发生的情况，包括任何错误消息、系统响应或结果。
  4. **屏幕截图/日志**：附加屏幕截图、日志文件或视频（如果它们可以增加清晰度），特别是对于 UI 问题或复杂错误。
  5. **时间戳**：记下测试的时间和日期，因为这对于调试至关重要。
  6. **环境详细信息**：包括有关测试环境的详细信息，例如浏览器版本、设备或系统配置。
  7. **再现性**：表明重新测试后结果是否一致。
  8. **链接缺陷**：如果结果表明存在缺陷，则创建错误报告并将其链接到测试用例以进行跟踪。

  ```
  // Example of documenting an Actual Result in a test case template:
  {
    Test Case ID: TC_101,
    Test Steps: "Enter 'admin' in the username field and 'password123' in the password field. Click 'Login'.",
    Expected Result: "User is directed to the dashboard.",
    Actual Result: "Error message 'Invalid credentials' displayed. User not logged in.",
    Timestamp: "2023-04-01 10:30 UTC",
    Environment: "Chrome 89 on Windows 10",
    Reproducible: "Yes",
    Defect ID: "BUG_204"
  }
  ```确保 **[Actual Result](../A/actual-result.md)** 足够详细，使开发人员能够明确地理解问题，从而促进更快的解决和[retesting](../R/retesting.md)。

1. **执行[Test Case](../T/test-case.md)**：按照概述的步骤运行测试。
  2. **观察**：仔细观察系统的行为或输出。
  3. **记录**：立即记录观察到的行为。使用清晰的语言描述发生的情况，包括任何错误消息、系统响应或结果。
  4. **屏幕截图/日志**：附加屏幕截图、日志文件或视频（如果它们可以增加清晰度），特别是对于 UI 问题或复杂错误。
  5. **时间戳**：记下测试的时间和日期，因为这对于调试至关重要。
  6. **环境详细信息**：包括有关测试环境的详细信息，例如浏览器版本、设备或系统配置。
  7. **再现性**：表明重新测试后结果是否一致。
  8. **链接缺陷**：如果结果表明存在缺陷，则创建错误报告并将其链接到测试用例以进行跟踪。

#### 用于捕获“实际结果”的常用工具或方法有哪些？

捕获[test automation](../T/test-automation.md)中的**[Actual Result](../A/actual-result.md)**通常涉及多种工具和方法：

- **自动化[Test Scripts](../T/test-script.md)**：在**[Selenium](../S/selenium.md)**、**[Cypress](../C/cypress.md)**或**Appium**等框架中编写的脚本会在[test execution](../T/test-execution.md)期间自动捕获输出。例如：

    ```
    let actualResult = element.getText();
    ```

- **日志**：自动化测试通常旨在记录结果和错误。 **Log4j** for Java 或 **Winston** for [Node.js](../N/node-js.md) 等工具可用于记录实际结果。
  - **屏幕截图**：像 **[Selenium](../S/selenium.md)** 这样的工具可以在执行测试步骤时截取应用程序状态的屏幕截图，这对于 UI 测试很有用。
  - **视频录制**：一些测试框架（例如 **TestCafe**）或云服务（例如 **Sauce Labs**）提供视频录制功能来捕获 [test execution](../T/test-execution.md)。
  - **[API](../A/api.md) 响应**：对于 [API testing](../A/api-testing.md)，**[Postman](../P/postman.md)** 或 **RestAssured** 等工具捕获代表 [actual result](../A/actual-result.md) 的 HTTP 响应数据。
  - **性能数据**：**[JMeter](../J/jmeter.md)** 或 **Gattle** 等工具将时序和吞吐量数据捕获为 [actual results](../A/actual-result.md) for [performance testing](../P/performance-testing.md)。
  - **[Test Reports](../T/test-report.md)**：**JUnit**、**TestNG** 或 **Mocha** 等框架生成包含 [actual results](../A/actual-result.md) 的报告。这些可以与 **Jenkins** 或 **GitLab CI** 等 CI/CD 工具进一步集成，以实现全面的报告。
  - **自定义处理程序**：在测试代码中实现自定义事件处理程序或回调以捕获应用程序的特定数据点或状态。
  - **[Database](../D/database.md) 验证**：使用[SQL](../S/sql.md) 或NoSQL 命令直接查询[database](../D/database.md) 以捕获数据更改。
  - **文件输出**：将结果写入文件，例如 CSV 或 JSON，以便稍后解析和分析。
  每种方法都是根据需要捕获的**上下文**和正在执行的测试的**类型**来选择的。

- **自动化[Test Scripts](../T/test-script.md)**：在**[Selenium](../S/selenium.md)**、**[Cypress](../C/cypress.md)**或**Appium**等框架中编写的脚本会在[test execution](../T/test-execution.md)期间自动捕获输出。例如：

    ```
    let actualResult = element.getText();
    ```

- **日志**：自动化测试通常旨在记录结果和错误。 **Log4j** for Java 或 **Winston** for [Node.js](../N/node-js.md) 等工具可用于记录实际结果。
  - **屏幕截图**：像 **[Selenium](../S/selenium.md)** 这样的工具可以在执行测试步骤时截取应用程序状态的屏幕截图，这对于 UI 测试很有用。
  - **视频录制**：一些测试框架（例如 **TestCafe**）或云服务（例如 **Sauce Labs**）提供视频录制功能来捕获 [test execution](../T/test-execution.md)。
  - **[API](../A/api.md) 响应**：对于 [API testing](../A/api-testing.md)，**[Postman](../P/postman.md)** 或 **RestAssured** 等工具捕获代表 [actual result](../A/actual-result.md) 的 HTTP 响应数据。
  - **性能数据**：**[JMeter](../J/jmeter.md)** 或 **Gattle** 等工具将时序和吞吐量数据捕获为 [actual results](../A/actual-result.md) for [performance testing](../P/performance-testing.md)。
  - **[Test Reports](../T/test-report.md)**：**JUnit**、**TestNG** 或 **Mocha** 等框架生成包含 [actual results](../A/actual-result.md) 的报告。这些可以与 **Jenkins** 或 **GitLab CI** 等 CI/CD 工具进一步集成，以实现全面的报告。
  - **自定义处理程序**：在测试代码中实现自定义事件处理程序或回调以捕获应用程序的特定数据点或状态。
  - **[Database](../D/database.md) 验证**：使用[SQL](../S/sql.md) 或NoSQL 命令直接查询[database](../D/database.md) 以捕获数据更改。
  - **文件输出**：将结果写入文件，例如 CSV 或 JSON，以便稍后解析和分析。

#### 如何使用“实际结果”来识别和诊断软件错误或问题？

**[Actual Result](../A/actual-result.md)** 是识别软件 [bugs](../B/bug.md) 并对其进行故障排除的关键诊断工具。当[test case](../T/test-case.md) 执行产生与[Expected Result](../E/expected-result.md) 不同的[Actual Result](../A/actual-result.md) 时，这种差异标志着软件中存在潜在缺陷。
  为了诊断问题，工程师在[test environment](../T/test-environment.md) 和输入数据的上下文中分析[Actual Result](../A/actual-result.md)。他们可能会在不同的 [test cases](../T/test-case.md) 或条件下寻找结果中的模式或不一致之处。例如，如果某个功能在一组输入下按预期工作，但在另一组输入下则不然，这可能表明存在边界情况问题或数据处理[bug](../B/bug.md)。
  工程师还使用[Actual Result](../A/actual-result.md)来查明发生故障的确切步骤。通过检查此时应用程序的状态（包括日志、堆栈跟踪或 [database](../D/database.md) 状态），他们可以识别故障的根本原因。
  如果[Actual Result](../A/actual-result.md) 表明存在性能问题，例如响应时间较慢或资源瓶颈，工程师可以使用分析工具深入了解测试时系统的行为。
  [Automated testing](../A/automated-testing.md) 框架通常提供捕获和报告详细[Actual Results](../A/actual-result.md) 的功能，包括[test execution](../T/test-execution.md) 的屏幕截图或视频记录，这对于诊断 UI 问题非常宝贵。
  通过系统地分析[Actual Result](../A/actual-result.md)，工程师可以制定有关[bug](../B/bug.md)来源的假设，然后可以对其进行测试和验证，从而实现更有效的[bug](../B/bug.md)修复过程。

### 高级概念

#### “实际结果”如何影响回归测试？

在[regression testing](../R/regression-testing.md) 中，**[Actual Result](../A/actual-result.md)** 对于验证最近的代码更改是否不会对现有功能产生不利影响至关重要。它是软件修改后[test case](../T/test-case.md) 的结果。通过比较**[Actual Result](../A/actual-result.md)**与**[Expected Result](../E/expected-result.md)**，测试人员可以确定是否发生了回归错误。
  对于自动回归测试，**[Actual Result](../A/actual-result.md)** 通常由 [test scripts](../T/test-script.md) 捕获，并以编程方式与 **[Expected Result](../E/expected-result.md)** 进行比较。差异会触发测试失败，提醒工程师注意潜在的回归。这种比较通常是通过测试代码中的断言来完成的：

  ```
  assert.equal(actualResult, expectedResult, 'The actual result does not match the expected result.');
  ```当 **[Actual Result](../A/actual-result.md)** 与 **[Expected Result](../E/expected-result.md)** 匹配时，表明应用程序的行为与其之前的状态保持一致。相反，不匹配可能表明最近的更改引入了缺陷，需要进一步调查和潜在的代码修复。
  在持续集成环境中，**[Actual Result](../A/actual-result.md)** 是反馈循环的一部分，在每次代码提交后通知开发团队其应用程序的稳定性。这种即时反馈对于维护[software quality](../S/software-quality.md) 和加快开发周期至关重要。
  具有清晰 **[Actual Results](../A/actual-result.md)** 的自动回归测试可以快速识别已回归的特定功能，简化调试过程并确保软件版本符合质量标准。

#### “实际结果”在自动化测试中起什么作用？

在[automated testing](../A/automated-testing.md) 中，**[Actual Result](../A/actual-result.md)** 充当根据预期结果验证软件行为的关键数据点。它是 [test script](../T/test-script.md) 执行时产生的输出。然后，该结果会自动与 **[Expected Result](../E/expected-result.md)** 进行比较，以确定测试是否通过或失败。

  ```
  // Example of capturing Actual Result in an automated test
  const actualResult = performAction();
  assert.equal(actualResult, expectedResult, 'Test failed: Actual result does not match expected result.');
  ```**[Actual Result](../A/actual-result.md)** 对于查明发生差异的确切步骤至关重要，尤其是在复杂的 [test scenarios](../T/test-scenario.md) 中。当测试失败时，**[Actual Result](../A/actual-result.md)** 会立即提供有关故障性质的反馈，使工程师无需人工干预即可启动调试和根本原因分析。
  自动化测试通常将 **[Actual Result](../A/actual-result.md)** 记录到报告或仪表板中，提供 [test executions](../T/test-execution.md) 的历史记录。这有助于趋势分析并有助于了解软件随时间的稳定性。
  在持续集成和部署 (CI/CD) 管道中，**[Actual Result](../A/actual-result.md)** 可以触发工作流，例如通知、回滚或附加 [test suites](../T/test-suite.md)，具体取决于 [test cases](../T/test-case.md) 的成功或失败。
  总体而言，**[Actual Result](../A/actual-result.md)** 是[test automation](../T/test-automation.md) 的基石，能够高效、准确地验证软件功能，并以系统化和可扩展的方式驱动[quality assurance](../Q/quality-assurance.md) 流程。

#### “实际结果”差异如何有助于软件优化和改进？

**[Actual Results](../A/actual-result.md)** 和 **[Expected Results](../E/expected-result.md)** 之间的差异对于软件优化和改进至关重要。当[test case](../T/test-case.md) 的实际结果偏离预期时，就表明存在潜在缺陷或需要改进的区域。这些差异可能导致：

- **需求细化**：不一致可能会揭示需求中的误解或差距，从而促进更清晰、更精确的规范。
  - **代码优化**：测试过程中暴露的性能问题或意外行为可以指导开发人员优化算法和重构代码。
  - **增强的用户体验**：用户界面或工作流程中不同的实际结果可以突出可用性问题，从而导致改进，使软件更加直观和用户友好。
  - **更好的错误处理**：遇到预期结果中未考虑的错误或异常可以通过增强错误处理和消息传递来提高软件的稳健性。
  - **增加[test coverage](../T/test-coverage.md)**：差异通常会揭示未经测试的路径或边缘情况，从而扩展测试套件以获得更全面的覆盖范围。
  通过分析这些差异，团队可以迭代地改进他们的软件，从而产生更可靠、更高性能和以用户为中心的产品。记录和跟踪这些发现非常重要，以确保它们在未来的开发周期中得到解决。

- **需求细化**：不一致可能会揭示需求中的误解或差距，从而促进更清晰、更精确的规范。
  - **代码优化**：测试过程中暴露的性能问题或意外行为可以指导开发人员优化算法和重构代码。
  - **增强的用户体验**：用户界面或工作流程中不同的实际结果可以突出可用性问题，从而导致改进，使软件更加直观和用户友好。
  - **更好的错误处理**：遇到预期结果中未考虑的错误或异常可以通过增强错误处理和消息传递来提高软件的稳健性。
  - **增加[test coverage](../T/test-coverage.md)**：差异通常会揭示未经测试的路径或边缘情况，从而扩展测试套件以获得更全面的覆盖范围。
