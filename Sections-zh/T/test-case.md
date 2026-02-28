# 测试用例

<!-- TOC START -->
- [相关术语：](#相关术语：)
  - [另请参阅：](#另请参阅：)
- [关于测试用例的问题？](#关于测试用例的问题？)
  - [基础知识和重要性](#基础知识和重要性)
    - [软件测试中的测试用例是什么？](#软件测试中的测试用例是什么？)
    - [为什么创建测试用例很重要？](#为什么创建测试用例很重要？)
    - [测试用例的关键组成部分是什么？](#测试用例的关键组成部分是什么？)
    - [测试用例如何提高软件产品的整体质量？](#测试用例如何提高软件产品的整体质量？)
    - [测试用例和测试场景有什么区别？](#测试用例和测试场景有什么区别？)
  - [创建和执行](#创建和执行)
    - [创建测试用例的步骤是什么？](#创建测试用例的步骤是什么？)
    - [测试用例在测试执行中的作用是什么？](#测试用例在测试执行中的作用是什么？)
    - [如何执行测试用例？](#如何执行测试用例？)
    - [可以使用哪些工具来创建和管理测试用例？](#可以使用哪些工具来创建和管理测试用例？)
    - [如何确定测试用例的成功或失败？](#如何确定测试用例的成功或失败？)
  - [类型和示例](#类型和示例)
    - [测试用例有哪些不同类型？](#测试用例有哪些不同类型？)
    - [你能提供一个好的测试用例的例子吗？](#你能提供一个好的测试用例的例子吗？)
    - [什么是正测试用例和负测试用例？](#什么是正测试用例和负测试用例？)
    - [什么是功能测试用例？](#什么是功能测试用例？)
    - [什么是非功能测试用例？](#什么是非功能测试用例？)
  - [最佳实践](#最佳实践)
    - [编写有效测试用例的最佳实践有哪些？](#编写有效测试用例的最佳实践有哪些？)
    - [如何确保测试用例涵盖所有可能的场景？](#如何确保测试用例涵盖所有可能的场景？)
    - [创建测试用例时要避免哪些常见错误？](#创建测试用例时要避免哪些常见错误？)
    - [测试用例应该多久审查和更新一次？](#测试用例应该多久审查和更新一次？)
    - [如何提高测试用例的可重用性？](#如何提高测试用例的可重用性？)
<!-- TOC END -->

一个

测试用例

是测试输入、条件、程序和预期结果的详细规范。它确保全面的程序评估并识别潜在的遗漏错误。

## 相关术语：

- [Test Script](../T/test-script.md)
- [Test Scenario](../T/test-scenario.md)

### 另请参阅：

- [Wikipedia](https://en.wikipedia.org/wiki/Test_case)

## 关于测试用例的问题？

### 基础知识和重要性

#### 软件测试中的测试用例是什么？

[software testing](../S/software-testing.md) 中的 **[Test Case](../T/test-case.md)** 是一组条件或变量，测试人员将在这些条件或变量下确定应用程序、软件系统或其功能之一是否按照最初为其建立的那样工作。 [test cases](../T/test-case.md) 的准备是测试过程中的关键步骤，因为它们有助于确保软件按预期运行并满足所有要求。
  [Test cases](../T/test-case.md) 是测试周期的基础，因为它们提供了记录的测试实例，可以跟踪该实例以供将来复制并确保[functional requirements](../F/functional-requirements.md) 的覆盖范围。它们被设计为尽可能原子，这意味着它们一次测试一件事，并且通常分组为 [test suites](../T/test-suite.md) 以进行更好的组织。
  在执行[test case](../T/test-case.md)时，测试人员按照其中概述的步骤来验证特定的功能或特性。然后将结果与 [expected results](../E/expected-result.md) 进行比较，以确定测试是否通过或失败。此过程对于识别缺陷并确保软件满足所需的质量标准至关重要。
  在[test automation](../T/test-automation.md)、[test cases](../T/test-case.md) 中，使用编程语言或测试工具编写脚本并自动执行，从而允许对应用程序的行为进行频繁且一致的验证。自动化[test cases](../T/test-case.md)对于[regression testing](../R/regression-testing.md)特别有用，其中先前开发和测试的软件会被再次测试，以确保现有功能能够在新的更改下正常工作。

#### 为什么创建测试用例很重要？

除了对 [software quality](../S/software-quality.md) 的直接贡献之外，创建 **[Test Case](../T/test-case.md)** 至关重要。它作为测试的**蓝图**，确保所有功能都得到系统验证。 [Test Cases](../T/test-case.md) 为测试提供**记录的基础**，促进可重复性和可重用性，这在 [regression testing](../R/regression-testing.md) 以及需要由不同团队成员或在开发生命周期的不同阶段执行测试时尤其重要。
  它们还支持**可追溯性**，将要求与其 [verification](../V/verification.md) 步骤联系起来，这对于保持符合行业标准和法规至关重要。这种可追溯性确保每个需求都有相应的测试，并且需求的任何更改都可以反映在[Test Cases](../T/test-case.md)中。
  此外，明确定义的[Test Cases](../T/test-case.md)可以成为利益相关者（包括开发人员、测试人员和业务分析师）之间**沟通**​​的一种方式，以确保对正在测试的内容和原因有共同的理解。它们有助于识别测试差距并防止重复测试工作。
  在[test automation](../T/test-automation.md) 的上下文中，[Test Cases](../T/test-case.md) 是创建**自动化[test scripts](../T/test-script.md)** 的基础。它们指导 [test scripts](../T/test-script.md) 的开发以及适当的自动化工具和框架的选择。
  最后，[Test Cases](../T/test-case.md) 为**估计**测试所需的时间和精力提供了基础，这对于项目规划和管理至关重要。它们还可以作为 [test coverage](../T/test-coverage.md) 和执行的证据，这对于审计、审查和流程改进很有价值。

#### 测试用例的关键组成部分是什么？

**[Test Case](../T/test-case.md)** 的关键组件包括：

- **[Test Case](../T/test-case.md) ID**：用于跟踪的唯一标识符。
  - **标题/描述**：测试的简短摘要。
  - **先决条件**：执行之前必须满足的任何要求。
  - **测试步骤**：详细的执行说明。
  - **[Test Data](../T/test-data.md)** ：测试期间需要的特定输入。
  - **[Expected Result](../E/expected-result.md)** ：应用程序行为正确时的预期结果。
  - **[Actual Result](../A/actual-result.md)** ：执行期间的实际结果；测试后填写。
  - **[Postconditions](../P/postcondition.md)** ：测试执行后应用程序的状态。
  - **通过/失败标准**：明确规则以确定测试是否通过或失败。
  - **[Priority](../P/priority.md)** ：测试用例的重要性级别，通常指导执行顺序。
  - **自动/手动**：指示测试是自动执行还是需要手动执行。
  - **可追溯性**：链接到需求或设计文档以确保覆盖范围。
  - **评论**：附加注释或观察结果。
  Markdown 中的示例：

  ```
  - **Test Case ID**: TC_001
  - **Title/Description**: Verify login with valid credentials
  - **Preconditions**: User is on login page
  - **Test Steps**:
    1. Enter valid username
    2. Enter valid password
    3. Click on login button
  - **Test Data**:
    - Username: testuser
    - Password: securePass123
  - **Expected Result**: User is redirected to the dashboard
  - **Actual Result**: *To be filled after execution*
  - **Postconditions**: User is logged in
  - **Pass/Fail Criteria**: Login successful, dashboard is displayed
  - **Priority**: High
  - **Automated/Manual**: Automated
  - **Traceability**: Req_ID_101
  - **Comments**: None
  ```

- **[Test Case](../T/test-case.md) ID**：用于跟踪的唯一标识符。
  - **标题/描述**：测试的简短摘要。
  - **先决条件**：执行之前必须满足的任何要求。
  - **测试步骤**：详细的执行说明。
  - **[Test Data](../T/test-data.md)** ：测试期间需要的特定输入。
  - **[Expected Result](../E/expected-result.md)** ：应用程序行为正确时的预期结果。
  - **[Actual Result](../A/actual-result.md)** ：执行期间的实际结果；测试后填写。
  - **[Postconditions](../P/postcondition.md)** ：测试执行后应用程序的状态。
  - **通过/失败标准**：明确规则以确定测试是否通过或失败。
  - **[Priority](../P/priority.md)** ：测试用例的重要性级别，通常指导执行顺序。
  - **自动/手动**：指示测试是自动执行还是需要手动执行。
  - **可追溯性**：链接到需求或设计文档以确保覆盖范围。
  - **评论**：附加注释或观察结果。

#### 测试用例如何提高软件产品的整体质量？

[Test Cases](../T/test-case.md) 对于确保软件产品的**质量**至关重要。它们充当测试的**蓝图**，详细说明应执行测试的条件和预期结果。通过这些案例仔细验证软件功能的各个方面，测试人员可以识别实际与[expected results](../E/expected-result.md)之间的差异，这表明存在缺陷或[bugs](../B/bug.md)。
  [Test Cases](../T/test-case.md) 的聚合形成了**全面的[test suite](../T/test-suite.md)**，涵盖了软件的各个方面，包括功能性、非功能性、积极和消极场景。这种广泛的覆盖范围确保了软件在不同的条件下进行检查，这有助于发现在常规使用过程中可能不明显的隐藏问题。
  此外，[Test Cases](../T/test-case.md) 有助于 **[regression testing](../R/regression-testing.md)** 进程。随着软件的发展，[Test Cases](../T/test-case.md) 可以重新执行，以确认新的更改不会对现有功能产生不利影响。这对于长期维护[software quality](../S/software-quality.md) 至关重要。
  结构良好的[Test Cases](../T/test-case.md) 提供的**可追溯性**也提高了产品的质量。它们可以链接回特定要求，确保满足所有客户期望并且不会忽视任何关键功能。
  本质上，[Test Cases](../T/test-case.md) 是[software quality](../S/software-quality.md) 验证的基础。它们提供了结构化的测试方法，促进全面覆盖，支持[regression testing](../R/regression-testing.md)，并确保需求的可追溯性，所有这些对于交付高质量的软件产品都是至关重要的。

#### 测试用例和测试场景有什么区别？

**[Test Case](../T/test-case.md)** 和 **[Test Scenario](../T/test-scenario.md)** 之间的区别在于它们的范围和细节。 **[Test Case](../T/test-case.md)** 是一组特定的操作、条件和输入，用于验证软件的特定特性或功能。它很详细，包括 [expected results](../E/expected-result.md) 以确定某个功能是否正常工作。
  相反，**[Test Scenario](../T/test-scenario.md)** 是要测试的功能的高级描述。它概述了用户可能遇到的情况，但没有深入探讨要采取的具体步骤。 [Test Scenarios](../T/test-scenario.md) 范围更广，用于确保测试时考虑所有可能的情况。
  [Test Case](../T/test-case.md) 是 **“如何”** 指南，而 [Test Scenario](../T/test-scenario.md) 则更多是 **“做什么”** 指南。场景涵盖多个[Test Cases](../T/test-case.md)，因为它们概述了可以通过多种不同方式进行测试的情况。 [Test Scenarios](../T/test-scenario.md) 帮助识别[Test Cases](../T/test-case.md)，这反过来又用于应用程序的详细测试。
  例如，[Test Scenario](../T/test-scenario.md) 可能是“验证登录功能”。在这种情况下，可以创建多个[Test Cases](../T/test-case.md)，例如：

- 测试案例 1：使用有效凭据验证登录。
  - 测试案例 2：使用无效凭据验证登录。
  - 测试案例 3：使用空白用户名和密码字段验证登录。
  本质上，[Test Scenarios](../T/test-scenario.md) 不太详细，涵盖了更广泛的应用程序行为，而[Test Cases](../T/test-case.md) 是旨在验证软件特定功能的详细指令。

- 测试案例 1：使用有效凭据验证登录。
  - 测试案例 2：使用无效凭据验证登录。
  - 测试案例 3：使用空白用户名和密码字段验证登录。

### 创建和执行

#### 创建测试用例的步骤是什么？

创建 [Test Case](../T/test-case.md) 涉及以下步骤：

1. **确定测试需求**：根据软件需求和规范确定需要测试的内容。
  2. **定义测试目标**：明确说明[Test Case](../T/test-case.md) 旨在验证或确认的内容。
  3. **选择[Test Data](../T/test-data.md)**：选择适当的输入数据，可以包括有效值、无效值和边界值。
  4. **确定[Expected Results](../E/expected-result.md)**：根据验证[Test Case](../T/test-case.md) 的要求定义预期结果。
  5. **开发测试程序**：概述执行[Test Case](../T/test-case.md)的步骤，包括[setup](../S/setup.md)、执行和拆卸操作。
  6. **编写测试步骤**：详细说明执行测试所需的每个步骤，包括应用程序导航和 [test data](../T/test-data.md) 的输入。
  7. **分配先决条件**：指定执行 [Test Case](../T/test-case.md) 之前必须满足的任何必要条件。
  8. **执行[Test Case](../T/test-case.md)**：手动运行[Test Case](../T/test-case.md) 或使用自动化工具来验证功能。
  9. **记录[Actual Results](../A/actual-result.md)**：记录[Test Case](../T/test-case.md) 执行的结果。
  10. **比较预期和[Actual Results](../A/actual-result.md)**：根据预期和[actual results](../A/actual-result.md)的对齐情况评估[Test Case](../T/test-case.md)是否通过或失败。
  11. **记录缺陷**：如果[Test Case](../T/test-case.md) 失败，记录遇到的任何缺陷或问题。
  12. **审查和完善**：定期审查和更新[Test Case](../T/test-case.md)，以确保其仍然有效和相关。
  请记住在每个步骤中保持清晰和简洁，以促进其他团队成员的理解和执行。

1. **确定测试需求**：根据软件需求和规范确定需要测试的内容。
  2. **定义测试目标**：明确说明[Test Case](../T/test-case.md) 旨在验证或确认的内容。
  3. **选择[Test Data](../T/test-data.md)**：选择适当的输入数据，可以包括有效值、无效值和边界值。
  4. **确定[Expected Results](../E/expected-result.md)**：根据验证[Test Case](../T/test-case.md) 的要求定义预期结果。
  5. **开发测试程序**：概述执行[Test Case](../T/test-case.md)的步骤，包括[setup](../S/setup.md)、执行和拆卸操作。
  6. **编写测试步骤**：详细说明执行测试所需的每个步骤，包括应用程序导航和 [test data](../T/test-data.md) 的输入。
  7. **分配先决条件**：指定执行 [Test Case](../T/test-case.md) 之前必须满足的任何必要条件。
  8. **执行[Test Case](../T/test-case.md)**：手动运行[Test Case](../T/test-case.md)或使用自动化工具来验证功能。
  9. **记录[Actual Results](../A/actual-result.md)**：记录[Test Case](../T/test-case.md)执行的结果。
  10. **比较预期和[Actual Results](../A/actual-result.md)**：根据预期和[actual results](../A/actual-result.md)的对齐情况评估[Test Case](../T/test-case.md)是否通过或失败。
  11. **记录缺陷**：如果[Test Case](../T/test-case.md) 失败，记录遇到的任何缺陷或问题。
  12. **审查和完善**：定期审查和更新[Test Case](../T/test-case.md)，以确保其仍然有效和相关。

#### 测试用例在测试执行中的作用是什么？

在[test execution](../T/test-execution.md) 中，**[Test Case](../T/test-case.md)** 充当测试过程的基本单元。它充当一组特定的条件，在这些条件下测试人员将确定应用程序的特定方面是否按预期工作。每个[Test Case](../T/test-case.md) 均单独且隔离地执行，以确保它验证其要测试的功能。
  在执行期间，[Test Case](../T/test-case.md) 为测试人员提供了清晰的步骤顺序，其中包括前提条件、输入值和[expected results](../E/expected-result.md)。这种结构化方法确保测试是可重复的，并且可以在不同的测试周期或由不同的测试人员一致地运行。
  [Test Case](../T/test-case.md) 的执行会导致以下结果之一：

- **通过**：软件的行为与预期结果一致。
  - **失败**：软件的行为偏离预期结果，表明存在缺陷。
  - **阻止**：由于外部因素（例如对其他测试用例的依赖或未解决的错误），测试用例无法执行。
  - **跳过**：故意不执行测试用例，可能是因为它超出了特定测试运行的范围。
  [Test Case](../T/test-case.md) 执行的结果对于识别缺陷、验证修复和确保软件满足其要求至关重要。通过仔细记录结果，测试人员向开发团队提供有价值的反馈，这对于维护 [software quality](../S/software-quality.md) 和指导未来的开发工作至关重要。

- **通过**：软件的行为与预期结果一致。
  - **失败**：软件的行为偏离预期结果，表明存在缺陷。
  - **阻止**：由于外部因素（例如对其他测试用例的依赖或未解决的错误），测试用例无法执行。
  - **跳过**：故意不执行测试用例，可能是因为它超出了特定测试运行的范围。

#### 如何执行测试用例？

在软件[test automation](../T/test-automation.md)中执行[test case](../T/test-case.md)通常涉及以下步骤：

1. **选择[test case](../T/test-case.md)**：识别您要从[test management](../T/test-management.md) 工具或存储库执行的[test case](../T/test-case.md)。
  2. **设置[test environment](../T/test-environment.md)**：确保[test environment](../T/test-environment.md) 准备好必要的配置、数据和资源。
  3. **运行测试**：使用[test automation](../T/test-automation.md) 工具执行[test case](../T/test-case.md)。这可以通过命令行界面、GUI 或集成开发环境 (IDE) 来完成。例如：
    或

    ```
    testcafe chrome tests/e2e/test-case.js
    ```

    ```
    describe('Login Test', () => {
      it('should navigate to login page and login', () => {
        browser.url('https://example.com/login');
        $('#username').setValue('user');
        $('#password').setValue('pass');
        $('button=Login').click();
        expect(browser).toHaveUrl('https://example.com/dashboard');
      });
    });
    ```

4. **监控执行**：实时或通过查看日志来观察[test execution](../T/test-execution.md) 进程，以确保其按预期进行。
  5. **查看结果**：执行后，分析结果，根据预期结果确定[test case](../T/test-case.md) 是通过还是失败。
  6. **报告**：在 [test management](../T/test-management.md) 工具或缺陷跟踪系统中记录结果，包括任何屏幕截图、日志或错误消息。
  7. **清理**：如有必要，将[test environment](../T/test-environment.md)重置为干净状态，为下一个[test execution](../T/test-execution.md)做好准备。
  请记住根据被测应用程序的最新版本验证[test case](../T/test-case.md)，以确保测试结果的准确性和相关性。

1. **选择 [test case](../T/test-case.md)**：识别您想要从 [test management](../T/test-management.md) 工具或存储库执行的 [test case](../T/test-case.md)。
  2. **设置[test environment](../T/test-environment.md)**：确保为[test environment](../T/test-environment.md) 准备好必要的配置、数据和资源。
  3. **运行测试**：使用[test automation](../T/test-automation.md) 工具执行[test case](../T/test-case.md)。这可以通过命令行界面、GUI 或集成开发环境 (IDE) 来完成。例如：
    或

    ```
    testcafe chrome tests/e2e/test-case.js
    ```

    ```
    describe('Login Test', () => {
      it('should navigate to login page and login', () => {
        browser.url('https://example.com/login');
        $('#username').setValue('user');
        $('#password').setValue('pass');
        $('button=Login').click();
        expect(browser).toHaveUrl('https://example.com/dashboard');
      });
    });
    ```

4. **监控执行**：实时或通过查看日志来观察[test execution](../T/test-execution.md) 进程，以确保其按预期进行。
  5. **查看结果**：执行后，分析结果，根据预期结果确定[test case](../T/test-case.md) 是通过还是失败。
  6. **报告**：在 [test management](../T/test-management.md) 工具或缺陷跟踪系统中记录结果，包括任何屏幕截图、日志或错误消息。
  7. **清理**：如有必要，将[test environment](../T/test-environment.md)重置为干净状态，为下一个[test execution](../T/test-execution.md)做好准备。

#### 可以使用哪些工具来创建和管理测试用例？

要创建和管理[test cases](../T/test-case.md)，可以使用各种工具来满足不同的需求和偏好。以下是一些流行工具的列表：

- **TestRail**：基于 Web 的测试用例管理工具，允许您管理、跟踪和组织您的软件测试工作。
  - **Zephyr**：Zephyr 与 JIRA 集成，为测试用例创建、执行和报告提供端到端解决方案。
  - **qTest**：作为 Tricentis 平台的一部分，qTest 提供测试用例管理，并实时集成到 JIRA 和其他开发工具。
  - **TestLink**：一个开源测试管理工具，支持测试用例创建、管理和执行跟踪。
  - **Xray**：一个 JIRA 插件，可促进测试管理，包括直接在 JIRA 内创建测试用例和报告。
  - **PractiTest**：一种 SaaS 测试管理工具，为测试用例管理提供全面的解决方案，包括与自动化框架的集成。
  - **TestLodge**：一个简单的测试管理工具，可让您轻松管理测试用例、需求和运行。
  - **TestCaseLab**：一个简单的测试用例管理工具，专为 QA 工程师设计，可以有效地创建和管理测试用例。
  - **SpiraTest**：提供具有需求和缺陷跟踪的集成测试用例管理，支持手动和自动测试。
  这些工具通常包括**版本控制**、**[test execution](../T/test-execution.md) 历史**、**可追溯性**和**报告功能**等功能，以帮助简化[test case management](../T/test-case-management.md) 流程。选择工具时，请考虑集成功能、易用性以及与团队工作流程和目标相符的特定功能等因素。

- **TestRail**：基于 Web 的测试用例管理工具，允许您管理、跟踪和组织您的软件测试工作。
  - **Zephyr**：Zephyr 与 JIRA 集成，为测试用例创建、执行和报告提供端到端解决方案。
  - **qTest**：作为 Tricentis 平台的一部分，qTest 提供测试用例管理，并实时集成到 JIRA 和其他开发工具。
  - **TestLink**：一个开源测试管理工具，支持测试用例创建、管理和执行跟踪。
  - **Xray**：一个 JIRA 插件，可促进测试管理，包括直接在 JIRA 内创建测试用例和报告。
  - **PractiTest**：一种 SaaS 测试管理工具，为测试用例管理提供全面的解决方案，包括与自动化框架的集成。
  - **TestLodge**：一个简单的测试管理工具，可让您轻松管理测试用例、需求和运行。
  - **TestCaseLab**：一个简单的测试用例管理工具，专为 QA 工程师设计，可以有效地创建和管理测试用例。
  - **SpiraTest**：提供具有需求和缺陷跟踪的集成测试用例管理，支持手动和自动测试。

#### 如何确定测试用例的成功或失败？

确定[Test Case](../T/test-case.md) 的**成功或失败**取决于**预期结果**与**[actual result](../A/actual-result.md)**。如果软件的行为与预定义的 **[expected result](../E/expected-result.md)** 一致，则 [Test Case](../T/test-case.md) 被视为**成功**。相反，如果结果出现偏差，则表明存在潜在缺陷或需求不匹配，则失败。
  要对此进行评估，请按照下列步骤操作：

1. **运行[Test Case](../T/test-case.md)**
    使用所选的测试自动化工具或框架。

2. **捕获[actual result](../A/actual-result.md)**
    当被测软件执行这些步骤时。

3. **比较**
    实际结果与
    **[expected result](../E/expected-result.md)**
    记录在测试用例中。

4. **标记[Test Case](../T/test-case.md)**
    作为
    **通过**
    如果结果一致，或者
    **失败**
    如果他们不这样做。

5.可选地，
    **记录缺陷**
    对于失败的案例，提供详细信息供开发人员解决。
  自动化测试通常利用**断言**以编程方式执行此比较：

  ```
  assert.equals(actualResult, expectedResult, "Test Case failed: Actual result does not match expected result.");
  ```测试中的**不稳定**可能会使评估变得复杂。如果 [Test Case](../T/test-case.md) 不一致地通过或失败，请调查环境问题、计时问题或非确定性行为。
  **[Code coverage](../C/code-coverage.md)** 工具还可以通过突出显示未经测试的路径来帮助确定[Test Cases](../T/test-case.md) 的有效性，尽管它们并不直接指示通过/失败状态。
  请记住，一次失败可能很严重，并且通过并不能保证[bugs](../B/bug.md) 不存在。持续监控和分析测试结果对于保持 [test suite](../T/test-suite.md) 有效性至关重要。

1. **运行[Test Case](../T/test-case.md)**
    使用所选的测试自动化工具或框架。

2. **捕获[actual result](../A/actual-result.md)**
    当被测软件执行这些步骤时。

3. **比较**
    实际结果与
    **[expected result](../E/expected-result.md)**
    记录在测试用例中。

4. **标记[Test Case](../T/test-case.md)**
    作为
    **通过**
    如果结果一致，或者
    **失败**
    如果他们不这样做。

5.可选地，
    **记录缺陷**
    对于失败的案例，提供详细信息供开发人员解决。

### 类型和示例

#### 测试用例有哪些不同类型？

软件[test automation](../T/test-automation.md) 中不同类型的[test cases](../T/test-case.md) 包括：

- **单元[Test Cases](../T/test-case.md)**：以代码的各个组件或函数为目标，以验证每个部分是否独立正确运行。
  - **集成[Test Cases](../T/test-case.md)**：确保多个组件或系统按预期协同工作。
  - **系统[Test Cases](../T/test-case.md)**：验证完整且集成的软件产品，以检查其是否满足指定要求。
  - **Smoke [Test Cases](../T/test-case.md)**：也称为“[build verification testing](../B/build-verification-testing.md)”，它们是 [test cases](../T/test-case.md) 的子集，用于验证应用程序的基本功能，以确保其稳定以进行进一步测试。
  - **回归[Test Cases](../T/test-case.md)**：旨在检查新代码更改是否对现有功能产生不利影响。
  - **性能@@PR​​OTECTED_18@@**：评估应用程序在特定工作负载下的响应能力、稳定性、可扩展性和速度。
  - **加载[Test Cases](../T/test-case.md)**：通过模拟多个用户同时访问应用程序来确定系统在正常和峰值条件下的行为方式。
  - **强调[Test Cases](../T/test-case.md)**：使系统超出其正常运行能力，通常达到临界点，以确定其阈值。
  - **安全[Test Cases](../T/test-case.md)**：识别软件中可能导致安全漏洞的漏洞。
  - **可用性[Test Cases](../T/test-case.md)**：评估应用程序的用户界面和用户体验，以确保其用户友好。
  - **兼容性[Test Cases](../T/test-case.md)**：检查软件是否在不同设备、浏览器、操作系统等上按预期运行。
  - **探索性[Test Cases](../T/test-case.md)**：基于测试人员的知识、经验、分析技能和直觉来探索软件的功能，无需预定义步骤。
  - **[API](../A/api.md) [Test Cases](../T/test-case.md)**：通过测试 [APIs](../A/api.md) 及其交互来验证应用程序内构建架构的逻辑。
  - **UI [Test Cases](../T/test-case.md)**：专注于图形界面以及用户如何与其交互，确保元素可见、操作可行且 UI 正确响应。
  每种类型的[test case](../T/test-case.md) 在确保全面的[test coverage](../T/test-coverage.md) 和高质量软件产品的交付方面都发挥着至关重要的作用。

- **单元[Test Cases](../T/test-case.md)**：以代码的各个组件或函数为目标，以验证每个部分是否独立正确运行。
  - **集成[Test Cases](../T/test-case.md)**：确保多个组件或系统按预期协同工作。
  - **系统[Test Cases](../T/test-case.md)**：验证完整且集成的软件产品，以检查其是否满足指定的要求。
  - **Smoke [Test Cases](../T/test-case.md)**：也称为“[build verification testing](../B/build-verification-testing.md)”，它们是 [test cases](../T/test-case.md) 的子集，用于验证应用程序的基本功能，以确保其稳定以进行进一步测试。
  - **回归[Test Cases](../T/test-case.md)**：旨在检查新代码更改是否对现有功能产生不利影响。
  - **性能@@PR​​OTECTED_38@@**：评估应用程序在特定工作负载下的响应能力、稳定性、可扩展性和速度。
  - **加载[Test Cases](../T/test-case.md)**：通过模拟多个用户同时访问应用程序来确定系统在正常和峰值条件下的行为方式。
  - **压力[Test Cases](../T/test-case.md)**：使系统超出其正常运行能力，通常达到临界点，以确定其阈值。
  - **安全[Test Cases](../T/test-case.md)**：识别软件中可能导致安全漏洞的漏洞。
  - **可用性[Test Cases](../T/test-case.md)**：评估应用程序的用户界面和用户体验，以确保其用户友好。
  - **兼容性[Test Cases](../T/test-case.md)**：检查软件是否在不同设备、浏览器、操作系统等上按预期运行。
  - **探索性[Test Cases](../T/test-case.md)**：基于测试人员的知识、经验、分析技能和直觉，在没有预定义步骤的情况下探索软件的功能。
  - **[API](../A/api.md) [Test Cases](../T/test-case.md)**：通过测试 [APIs](../A/api.md) 及其交互来验证应用程序内构建架构的逻辑。
  - **UI [Test Cases](../T/test-case.md)**：专注于图形界面以及用户如何与其交互，确保元素可见、操作可行且 UI 正确响应。

#### 你能提供一个好的测试用例的例子吗？

  ```
  Example Test Case: **User Login Functionality**
  **ID**: TC_LOGIN_01
  **Title**: Verify successful login with valid credentials
  **Preconditions**: User is on the login page, and the test environment is set up.
  **Test Steps**:
  1. Enter a valid username in the username field.
  2. Enter the corresponding password in the password field.
  3. Click the 'Login' button.
  **Expected Result**: The user is redirected to the homepage and greeted with a welcome message.
  **Actual Result**: *To be filled after test execution*
  **Postconditions**: User is logged out and returned to the login page.
  **Status**: *To be filled after test execution (Pass/Fail)*
  **Remarks**: *Any additional information or observations*
  **Automated Script Reference**: `loginTest.js`
  **Execution Logs**: *Link or reference to detailed execution logs*
  **Attachments**: *Screenshots or videos, if applicable*
  **Priority**: High
  **Automated**: Yes
  **Author**: *Test Engineer's Name*
  **Created On**: *Date of creation*
  **Last Executed On**: *Date of last execution*
  **Version**: 1.0
  **Tags**: `Login`, `Smoke Test`
  This test case ensures that users with valid credentials can access the system, which is critical for any application requiring authentication. It's designed to be concise for quick understanding and execution while providing all necessary details for automation scripts.
  ```

#### 什么是正测试用例和负测试用例？

正 [Test Cases](../T/test-case.md) 旨在验证系统在提供有效输入或在预期条件下执行时是否按预期运行。他们确认软件的功能按照要求和规范正常工作。主要目标是证明该软件能够实现其应有的功能。

  ```
  // Example of a positive test case in pseudocode
  function testLoginWithValidCredentials() {
    enterUsername("validUser");
    enterPassword("correctPassword");
    clickLogin();
    assert(isLoggedIn() == true);
  }
  ```另一方面，否定[Test Cases](../T/test-case.md)确保系统可以正常处理无效输入或意外的用户行为。这些[test cases](../T/test-case.md)对于验证软件的稳健性和错误处理能力至关重要。他们的目的是通过以软件设计无法处理的方式测试软件来暴露缺陷。

  ```
  // Example of a negative test case in pseudocode
  function testLoginWithInvalidCredentials() {
    enterUsername("invalidUser");
    enterPassword("wrongPassword");
    clickLogin();
    assert(isLoggedIn() == false);
    assert(getErrorMessage() == "Invalid credentials");
  }
  ```正面和负面[test cases](../T/test-case.md)对于全面的测试策略都至关重要，有助于确保软件功能齐全且具有弹性。

#### 什么是功能测试用例？

**功能@@PR​​OTECTED_1@@** 是为验证软件应用程序的特定特性或功能而执行的一组操作。与关注性能、安全性或可用性的非功能性[test cases](../T/test-case.md) 不同，功能性[test cases](../T/test-case.md) 关注系统的功能。他们通过向软件提供输入并检查输出来针对[functional requirements](../F/functional-requirements.md) 验证软件。
  功能@@PR​​OTECTED_5@@ 通常以粒度级别编写，以覆盖应用程序的各个功能或部分。它们可以是积极的，测试系统对预期输入的响应，也可以是消极的，确保系统妥善处理错误或意外的输入。
  要编写函数[test case](../T/test-case.md)，您需要：

1. 确定要测试的功能。
  2. 定义测试输入或条件。
  3. 确定预期结果。
  这是伪代码的简化示例：

  ```
  // Test Case: Verify login functionality for a valid user
  function testLoginValidUser() {
    navigateToLoginPage();
    enterUsername("validUser");
    enterPassword("correctPassword");
    clickLoginButton();
    assertUserIsLoggedIn();
  }
  ```在此示例中，[test case](../T/test-case.md) 旨在确认具有有效凭据的用户可以成功登录。 [test case](../T/test-case.md) 是否成功由最后的断言决定，该断言检查用户是否登录。如果断言通过，则认为[test case](../T/test-case.md) 成功；否则，[test case](../T/test-case.md) 成功。如果失败，则[test case](../T/test-case.md) 已发现缺陷。

1. 确定要测试的功能。
  2. 定义测试输入或条件。
  3. 确定预期结果。

#### 什么是非功能测试用例？

**非功能性[Test Case](../T/test-case.md)** 侧重于定义系统**如何**运行的软件系统的各个方面，而不是系统**做什么**。这些[test cases](../T/test-case.md) 与系统在某些约束下的行为有关，包括性能、安全性、可用性、可靠性和可扩展性等属性。
  与验证特定操作或功能的功能性[test cases](../T/test-case.md) 不同，非功能性[test cases](../T/test-case.md) 验证系统的非[functional requirements](../F/functional-requirements.md)，这些非[functional requirements](../F/functional-requirements.md) 与任何特定功能或用户操作无关。他们确保软件满足一定的质量和用户体验标准。
  例如，用于性能的非功能性 [test case](../T/test-case.md) 可能会测量系统在重负载下响应请求所需的时间。用于安全的[test case](../T/test-case.md) 可能会评估系统抵御[SQL](../S/sql.md) 注入攻击的能力。
  以下是用于提高性能的非功能性 [test case](../T/test-case.md) 示例：

  ```
  Test Case ID: NF_TC_001
  Objective: Assess system response time under peak load.
  Preconditions: System is operational with a database containing 1 million records.
  Test Steps:
  1. Simulate 1000 concurrent users accessing the system.
  2. Measure the response time for each user action.
  Expected Result: All user actions should receive a response within 2 seconds.
  ```非功能性[test cases](../T/test-case.md)对于确保软件的稳健性、效率和用户满意度至关重要。它们使用各种工具和技术执行，例如用于[load testing](../L/load-testing.md)的[performance testing](../P/performance-testing.md)工具（例如[JMeter](../J/jmeter.md)、LoadRunner）和用于漏洞扫描的[security testing](../S/security-testing.md)工具（例如OWASP ZAP、Nessus）。

### 最佳实践

#### 编写有效测试用例的最佳实践有哪些？

编写有效[test cases](../T/test-case.md) 的最佳实践包括：

- **清晰简洁**：写出简单易懂的[test cases](../T/test-case.md)。避免歧义，以确保任何人都可以执行它们。
  - **使用描述性名称**：选择反映[test case](../T/test-case.md)用途的名称，以便更容易一目了然地识别其意图。
  - **优先考虑[Test Cases](../T/test-case.md)**：根据业务影响、关键功能和故障可能性订购[test cases](../T/test-case.md)。
  - **包括先决条件**：在执行测试之前清楚地说明任何所需的状态或所需的配置。
  - **定义[Expected Results](../E/expected-result.md)**：指定正确的结果应该是什么，以便毫无疑问测试是否通过或失败。
  - **使它们独立**：每个[test case](../T/test-case.md) 应该是独立的，而不是依赖于另一个的结果。
  - **参数化数据**：使用数据驱动的测试来避免硬编码值，从而提高灵活性并减少维护。
  - **版本控制**：将[test cases](../T/test-case.md)置于版本控制之下以跟踪更改并维护历史记录。
  - **同行评审**：由同行评审 [test cases](../T/test-case.md) 以发现错误并提高质量。
  - **适当时自动化**：自动化重复、需要精确或需要频繁运行的[test cases](../T/test-case.md)。
  - **维护可追溯性**：将 [test cases](../T/test-case.md) 链接到需求或用户故事，以确保覆盖范围并促进 [impact analysis](../I/impact-analysis.md)。
  - **定期重构**：使 [test cases](../T/test-case.md) 保持最新状态，并随着应用程序的发展进行重构，以提高效率和清晰度。
  - **明智地使用注释**：包括注释来解释 [test case](../T/test-case.md) 中的复杂逻辑或决策，但避免过度注释。
  - **避免 [Test Case](../T/test-case.md) 重复**：在创建新的 [test cases](../T/test-case.md) 之前检查现有的 [test cases](../T/test-case.md) 以防止冗余。
  - **平衡正面和负面测试**：确保正面（预期行为）和负面（处理无效或意外输入）[test cases](../T/test-case.md) 的混合。
  通过坚持这些实践，[test cases](../T/test-case.md) 将变得健壮、可维护并且在确保软件产品的质量方面具有价值。

- **清晰简洁**：写出简单易懂的[test cases](../T/test-case.md)。避免歧义，以确保任何人都可以执行它们。
  - **使用描述性名称**：选择反映[test case](../T/test-case.md)用途的名称，使其更容易一目了然地识别其意图。
  - **优先考虑[Test Cases](../T/test-case.md)**：根据业务影响、关键功能和故障可能性订购[test cases](../T/test-case.md)。
  - **包括先决条件**：在执行测试之前清楚地说明任何所需的状态或所需的配置。
  - **定义[Expected Results](../E/expected-result.md)**：指定正确的结果应该是什么，以便毫无疑问测试是通过还是失败。
  - **使它们独立**：每个[test case](../T/test-case.md) 应该是独立的，而不是依赖于另一个的结果。
  - **参数化数据**：使用数据驱动的测试来避免硬编码值，从而提高灵活性并减少维护。
  - **版本控制**：将[test cases](../T/test-case.md)置于版本控制之下以跟踪更改并维护历史记录。
  - **同行评审**：由同行评审 [test cases](../T/test-case.md) 以发现错误并提高质量。
  - **适当时自动化**：自动化重复、需要精确或需要频繁运行的[test cases](../T/test-case.md)。
  - **维护可追溯性**：将 [test cases](../T/test-case.md) 链接到需求或用户故事，以确保覆盖范围并促进 [impact analysis](../I/impact-analysis.md)。
  - **定期重构**：使 [test cases](../T/test-case.md) 保持最新状态，并随着应用程序的发展进行重构，以提高效率和清晰度。
  - **明智地使用注释**：包括注释来解释 [test case](../T/test-case.md) 中的复杂逻辑或决策，但避免过度注释。
  - **避免 [Test Case](../T/test-case.md) 重复**：在创建新的 [test cases](../T/test-case.md) 之前检查现有的 [test cases](../T/test-case.md) 以防止冗余。
  - **平衡正面和负面测试**：确保正面（预期行为）和负面（处理无效或意外输入）[test cases](../T/test-case.md) 的混合。

#### 如何确保测试用例涵盖所有可能的场景？

确保[Test Case](../T/test-case.md)涵盖所有可能的场景涉及多种技术的组合：

- **[Equivalence Partitioning](../E/equivalence-partitioning.md)** ：将输入分为应同等对待的组。测试每个分区的一名代表。
  - **边界值分析**：关注输入范围的边缘情况，因为边界处经常出现错误。
  - **[Decision Table Testing](../D/decision-table-testing.md)** ：创建一个涵盖输入和相应操作的所有可能组合的表。
  - **[State Transition Testing](../S/state-transition-testing.md)** ：识别所有可能的状态和转换，以确保所有路径都经过测试。
  - **[Use Case Testing](../U/use-case-testing.md)** ：基于真实使用场景进行测试以涵盖功能要求。
  - **组合测试**：使用成对测试等工具生成涵盖所有输入参数组合的最小测试用例集。
  - **[Risk-Based Testing](../R/risk-based-testing.md)** ：根据故障的可能性和影响确定测试的优先级。
  - **[Exploratory Testing](../E/exploratory-testing.md)** ：通过临时会话补充结构化测试，以发现正式方法可能遗漏的场景。
  - **用户故事和验收标准**：确保测试用例符合用户期望和业务需求。
  - **同行评审**：让其他工程师评审测试用例以识别缺失的场景。
  - **自动测试生成工具**：利用可以根据模型或规范生成测试用例的工具。
  请记住，由于时间和资源的限制，测试每种可能的场景并不总是可行或实际的。专注于最关键的路径并使用风险评估来指导[test coverage](../T/test-coverage.md)。定期重新访问和更新 [test cases](../T/test-case.md) 以适应软件的变化以及对其使用的新理解。

- **[Equivalence Partitioning](../E/equivalence-partitioning.md)** ：将输入分为应同等对待的组。测试每个分区的一名代表。
  - **边界值分析**：关注输入范围的边缘情况，因为边界处经常出现错误。
  - **[Decision Table Testing](../D/decision-table-testing.md)** ：创建一个涵盖输入和相应操作的所有可能组合的表。
  - **[State Transition Testing](../S/state-transition-testing.md)** ：识别所有可能的状态和转换，以确保所有路径都经过测试。
  - **[Use Case Testing](../U/use-case-testing.md)** ：基于真实使用场景进行测试以涵盖功能需求。
  - **组合测试**：使用成对测试等工具生成涵盖所有输入参数组合的最小测试用例集。
  - **[Risk-Based Testing](../R/risk-based-testing.md)** ：根据故障的可能性和影响确定测试的优先级。
  - **[Exploratory Testing](../E/exploratory-testing.md)** ：通过临时会话补充结构化测试，以发现正式方法可能遗漏的场景。
  - **用户故事和验收标准**：确保测试用例符合用户期望和业务需求。
  - **同行评审**：让其他工程师评审测试用例以识别缺失的场景。
  - **自动测试生成工具**：利用可以根据模型或规范生成测试用例的工具。

#### 创建测试用例时要避免哪些常见错误？

创建[Test Case](../T/test-case.md)时要避免的常见错误：

- **忽略[Test Case](../T/test-case.md) 独立性**：每个测试用例应该是独立的并且独立于其他测试用例，以避免级联故障。
  - **歧义**：测试用例必须清晰且精确。不明确的步骤可能会导致执行和结果不一致。
  - **过多的细节**：虽​​然清晰度很重要，但过多的细节会使测试用例难以维护。仅包括理解和执行所必需的内容。
  - **忽略[Negative Testing](../N/negative-testing.md)** ：仅关注积极的情况可能会错过潜在的缺陷。包括负面测试用例以确保稳健的测试。
  - **不优先考虑**：所有测试用例并不相同。根据风险、功能重要性和使用频率对它们进行优先级排序。
  - **缺乏版本控制**：测试用例不断发展。如果没有版本控制，您将无法跟踪更改或在需要时恢复到以前的版本。
  - **评审不足**：同行评审可以发现作者可能错过的错误。跳过审查可能会影响测试用例的质量。
  - **糟糕的命名约定**：名称应该快速传达测试用例的目的。不一致或不明确的命名可能会导致混乱。
  - **不规划可重用性**：设计测试用例时考虑可重用性，从长远来看可以节省时间和精力。
  - **忽视数据管理**：硬编码测试数据可能会限制测试的适用性。尽可能使用数据驱动的方法。
  - **忽略[Test Environment](../T/test-environment.md)** ：不指定所需的测试环境可能会因环境差异而导致误报或误报。
  - **无法更新[Test Cases](../T/test-case.md)**：随着软件的发展，测试用例也应该发展。需要定期更新以保持相关性。
  - **不考虑维护**：测试用例应该易于维护。避免复杂的结构，这会使维护成为一场噩梦。
  - **忽略[Test Case](../T/test-case.md) 独立性**：每个测试用例应该是独立的并且独立于其他测试用例，以避免级联失败。
  - **歧义**：测试用例必须清晰且精确。不明确的步骤可能会导致执行和结果不一致。
  - **过多的细节**：虽​​然清晰度很重要，但过多的细节会使测试用例难以维护。仅包括理解和执行所必需的内容。
  - **忽略[Negative Testing](../N/negative-testing.md)** ：仅关注积极的情况可能会错过潜在的缺陷。包括负面测试用例以确保稳健的测试。
  - **不优先考虑**：所有测试用例并不相同。根据风险、功能重要性和使用频率对它们进行优先级排序。
  - **缺乏版本控制**：测试用例不断发展。如果没有版本控制，您将无法跟踪更改或在需要时恢复到以前的版本。
  - **评审不足**：同行评审可以发现作者可能错过的错误。跳过审查可能会影响测试用例的质量。
  - **糟糕的命名约定**：名称应该快速传达测试用例的目的。不一致或不明确的命名可能会导致混乱。
  - **不规划可重用性**：设计测试用例时考虑可重用性，从长远来看可以节省时间和精力。
  - **忽视数据管理**：硬编码测试数据可能会限制测试的适用性。尽可能使用数据驱动的方法。
  - **忽略[Test Environment](../T/test-environment.md)** ：未指定所需的测试环境可能会因环境差异而导致误报或误报。
  - **无法更新[Test Cases](../T/test-case.md)**：随着软件的发展，测试用例也应该发展。需要定期更新以保持相关性。
  - **不考虑维护**：测试用例应该易于维护。避免复杂的结构，这会使维护成为一场噩梦。

#### 测试用例应该多久审查和更新一次？

[Test Cases](../T/test-case.md) 应**定期**进行审查和更新，以确保它们保持有效和相关。评论的频率可能受到以下几个因素的影响：

- **对应用程序进行任何更改之后**：只要软件有更新或更改，就应评估相关的测试用例，以确保它们仍然与新功能保持一致。
  - **新功能发布后**：新功能可能需要新的测试用例或对现有测试用例的修改。
  - **当发现缺陷时**：如果发现错误，则审查相关测试用例以识别覆盖范围中的任何差距至关重要。
  - **在敏捷环境中定期**：在敏捷中，在每次迭代或冲刺结束时审查测试用例以针对未来的周期进行改进是有益的。
  - **在 [Test Case](../T/test-case.md) 维护周期**：建立定期间隔（例如每季度、每半年）对测试用例套件进行全面审查。
  自动化工具可以通过跟踪应用程序代码库中的更改来帮助标记过时的[Test Cases](../T/test-case.md)。此外，版本控制系统可用于管理 [Test Cases](../T/test-case.md) 的更新，确保它们与软件修订版同步。

  ```
  // Example: Pseudo-code for a scheduled Test Case review process
  scheduleTestCaseReview(frequency) {
    if (frequency === 'afterChange') {
      onSoftwareChangeEvent(reviewTestCases);
    } else if (frequency === 'iterationEnd') {
      onIterationEndEvent(reviewTestCases);
    } else {
      setTimeInterval(reviewTestCases, frequency);
    }
  }
  ```**一致性**和**适应性**是关键； [Test Cases](../T/test-case.md) 应该与它们旨在测试的软件一起发展。

- **对应用程序进行任何更改之后**：只要软件有更新或更改，就应评估相关的测试用例，以确保它们仍然与新功能保持一致。
  - **新功能发布后**：新功能可能需要新的测试用例或对现有测试用例的修改。
  - **当发现缺陷时**：如果发现错误，则审查相关测试用例以识别覆盖范围中的任何差距至关重要。
  - **在敏捷环境中定期**：在敏捷中，在每次迭代或冲刺结束时审查测试用例以针对未来的周期进行改进是有益的。
  - **在 [Test Case](../T/test-case.md) 维护周期**：建立定期间隔（例如每季度、每半年）对测试用例套件进行全面审查。

#### 如何提高测试用例的可重用性？

为了提高[test automation](../T/test-automation.md)中[test cases](../T/test-case.md)的**可重用性**：

- **模块化测试**：将测试用例分解为更小的、可重用的模块或功能，可以以不同的方式组合以创建新的测试用例。

  ```
  function login(username, password) {
    // Code to perform login
  }
  function addItemToCart(item) {
    // Code to add item to shopping cart
  }
  ```

- **使用数据驱动的测试**：从测试脚本中外部化测试数据。这允许使用不同的数据集执行相同的测试用例，而无需修改代码。

  ```
  dataProvider("credentials", function*() {
    yield ["user1", "password1"];
    yield ["user2", "password2"];
  });
  test("Login with multiple users", async (username, password) => {
    await login(username, password);
    // Assertions here
  });
  ```

- **实现 [Page Object Model](../P/page-object-model.md) (POM)** ：将 UI 结构和行为封装在页面对象中。这减少了重复工作，并且在 UI 更改时使维护变得更加容易。

  ```
  class LoginPage {
    constructor() {
      this.usernameField = "#username";
      this.passwordField = "#password";
      this.submitButton = "#submit";
    }
    async login(username, password) {
      await setInput(this.usernameField, username);
      await setInput(this.passwordField, password);
      await click(this.submitButton);
    }
  }
  ```

- **参数化测试**：使用参数来概括测试用例，使其适用于不同的情况。

  ```
  test("Add multiple items to cart", async (items) => {
    for (const item of items) {
      await addItemToCart(item);
    }
    // Assertions here
  });
  ```

- **采用版本控制最佳实践**：在版本控制系统中以清晰的命名约定和目录结构组织[test scripts](../T/test-script.md)，以方便共享和重用[test cases](../T/test-case.md)。
  - **记录可重用组件**：确保所有可重用模块、函数和页面对象都有详细记录，使其他人更容易理解和使用它们。
  通过遵循这些实践，[test automation](../T/test-automation.md) 工程师可以创建一套灵活、可维护且可重用的[test cases](../T/test-case.md)，从而实现更高效的测试流程。

- **模块化测试**：将测试用例分解为更小的、可重用的模块或功能，可以以不同的方式组合以创建新的测试用例。
  - **使用数据驱动的测试**：从测试脚本中外部化测试数据。这允许使用不同的数据集执行相同的测试用例，而无需修改代码。
  - **实现 [Page Object Model](../P/page-object-model.md) (POM)** ：将 UI 结构和行为封装在页面对象中。这减少了重复工作，并且在 UI 更改时使维护变得更加容易。
  - **参数化测试**：使用参数来概括测试用例，使其适用于不同的情况。
  - **采用版本控制最佳实践**：在版本控制系统中组织[test scripts](../T/test-script.md)，具有清晰的命名约定和目录结构，以方便共享和重用[test cases](../T/test-case.md)。
  - **记录可重用组件**：确保所有可重用模块、函数和页面对象都有详细记录，使其他人更容易理解和使用它们。
