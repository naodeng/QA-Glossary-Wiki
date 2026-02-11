# 测试用例 (Test Case)
[测试用例 (Test Case)](#test-case) [测试用例 (test case)](/wiki/test-case)

### 相关术语：
- 测试脚本 (Test Script)
- 测试场景 (Test Scenario)
[测试脚本 (Test Script)](/glossary/test-script) [测试场景 (Test Scenario)](/glossary/test-scenario)

### 另请参阅：
- 维基百科 (Wikipedia)
[维基百科 (Wikipedia)](https://en.wikipedia.org/wiki/Test_case)

## 关于测试用例的常见问题？

#### 基础与重要性
- **软件测试中的测试用例是什么？**
  **测试用例 (Test Case)** 是 **[软件测试 (software testing)](/wiki/software-testing)** 中的一组条件或变量，测试人员通过这些条件或变量来确定应用程序、软件系统或其某个功能是否按原定的设计运行。编写 **[测试用例 (test cases)](/wiki/test-case)** 是测试过程中的关键步骤，因为它们有助于确保软件按预期运行并满足所有需求。
  **测试用例** 是测试周期的基础，因为它们提供了测试的记录实例，可以追踪以备将来复现，并确保覆盖了 **[功能需求 (functional requirements)](/wiki/functional-requirements)**。它们在设计上尽可能保持原子性，即一次只测试一件事，并且经常被组织到 **[测试套件 (test suites)](/wiki/test-suite)** 中以便更好地管理。
  执行 **[测试用例 (test case)](/wiki/test-case)** 时，测试人员遵循其中概述的步骤来验证特定功能。然后将执行结果与 **[预期结果 (expected results)](/wiki/expected-result)** 进行比较，以确定测试通过还是失败。这对于识别缺陷和确保软件达到所需的质量标准至关重要。
  在 **[测试自动化 (test automation)](/wiki/test-automation)** 中，**[测试用例 (test cases)](/wiki/test-case)** 使用编程语言或测试工具编写脚本并自动执行。自动化 **[测试用例 (test cases)](/wiki/test-case)** 对于 **[回归测试 (regression testing)](/wiki/regression-testing)** 尤为有用。

- **为什么要创建测试用例？**
  创建 **测试用例 (Test Case)** 至关重要，它作为测试的 **蓝图**，确保所有功能都得到系统地验证。**[测试用例 (Test Cases)](/wiki/test-case)** 为测试提供了 **文档化的基础**，促进了重复性和可重用性，这在 **[回归测试 (regression testing)](/wiki/regression-testing)** 中尤为重要。
  它们还实现了 **可追溯性**，将需求与 **[验证 (verification)](/wiki/verification)** 步骤联系起来，确保每个需求都有对应的测试。
  此外，定义良好的 **[测试用例 (Test Cases)](/wiki/test-case)** 可以作为利益相关者之间的 **沟通** 手段。
  在 **[测试自动化 (test automation)](/wiki/test-automation)** 中，**[测试用例 (Test Cases)](/wiki/test-case)** 是创建 **自动化测试脚本** 的基础。
  最后，**[测试用例 (Test Cases)](/wiki/test-case)** 为 **估算** 测试所需的时间和工作量提供了依据，并作为 **[测试覆盖率 (test coverage)](/wiki/test-coverage)** 和执行的证据。

- **测试用例的关键组成部分有哪些？**
  **测试用例 (Test Case)** 的关键组成部分包括：
  - **测试用例 ID**：用于跟踪的唯一标识符。
  - **标题/说明**：测试的简要总结。
  - **前置条件**：执行前必须满足的要求。
  - **测试步骤**：详细的执行说明。
  - **测试数据**：测试期间需要的特定输入。
  - **预期结果**：应用程序正常运行时的预期结果。
  - **实际结果**：执行期间的实际产出；测试后填写。
  - **后置条件**：测试执行后的应用程序状态。
  - **通过/失败标准**：确定测试是否通过的明确规则。
  - **优先级 (Priority)**：测试用例的重要性级别。
  - **自动化/手动**：指示测试是自动化的还是需要手动执行。
  - **可追溯性**：链接到需求或设计文档。
  - **备注**：额外说明。

  **Markdown 示例：**
  - **测试用例 ID**: TC_001
  - **标题/说明**: 验证使用有效凭据登录
  - **前置条件**: 用户在登录页面
  - **测试步骤**:
    1. 输入有效用户名
    2. 输入有效密码
    3. 点击登录按钮
  - **测试数据**:
    - 用户名: testuser
    - 密码: securePass123
  - **预期结果**: 用户被重定向到仪表板
  - **实际结果**: *执行后填写*
  - **后置条件**: 用户已登录
  - **通过/失败标准**: 登录成功，显示仪表板
  - **优先级**: 高
  - **自动化/手动**: 自动化
  - **可追溯性**: Req_ID_101
  - **备注**: 无

- **测试用例如何提高软件产品的整体质量？**
  **[测试用例 (Test Cases)](/wiki/test-case)** 在确保软件 **质量** 方面起着关键作用。它们是测试的 **蓝图**。通过这些用例仔细验证软件功能的每个方面，测试人员可以识别出实际结果与 **[预期结果 (expected results)](/wiki/expected-result)** 之间的差异，这些差异通常预示着缺陷或 **[Bug (bugs)](/wiki/bug)**。
  **[测试用例 (Test Cases)](/wiki/test-case)** 的集合构成了 **全面的 [测试套件 (test suite)](/wiki/test-suite)**，涵盖了功能、非功能、正向和反向场景。
  此外，**[测试用例 (Test Cases)](/wiki/test-case)** 有助于 **[回归测试 (regression testing)](/wiki/regression-testing)** 过程，确保新变更不会影响现有功能，从而维持随时间变化的 **[软件质量 (software quality)](/wiki/software-quality)**。

- **测试用例和测试场景有什么区别？**
  **测试用例 (Test Case)** 和 **[测试场景 (Test Scenario)](/wiki/test-scenario)** 的区别在于它们的范围和详细程度。
  **测试用例 (Test Case)** 是一组具体的动作、条件和输入，用于验证软件的某个特定特性或功能。它是详细的，且包含 **[预期结果 (expected results)](/wiki/expected-result)**。
  相比之下，**测试场景 (Test Scenario)** 是对要测试的功能的高层描述。它概述了用户可能遇到的情况，但不涉及具体步骤。
  如果说 **[测试用例 (Test Case)](/wiki/test-case)** 是 **“如何做”** 的指南，那么 **[测试场景 (Test Scenario)](/wiki/test-scenario)** 更多是 **“做什么”** 的指南。一个场景可以涵盖多个 **[测试用例 (test cases)](/wiki/test-case)**。**[测试场景 (Test Scenarios)](/wiki/test-scenario)** 有助于识别 **[测试用例 (test cases)](/wiki/test-case)**。
  例如，一个 **[测试场景 (Test Scenario)](/wiki/test-scenario)** 可能是“验证登录功能”。在该场景下，可以创建多个 **[测试用例 (test cases)](/wiki/test-case)**，如：
  - 测试用例 1：验证使用有效凭据登录。
  - 测试用例 2：验证使用无效凭据登录。
  - 测试用例 3：验证用户名和密码为空时的登录。

#### 创建与执行
- **创建测试用例的步骤是什么？**
  创建 **[测试用例 (Test Case)](/wiki/test-case)** 涉及以下步骤：
  1. **识别测试需求**：根据软件需求识别需要测试的内容。
  2. **定义测试目标**：明确说明 **[测试用例 (Test Case)](/wiki/test-case)** 旨在验证什么。
  3. **选择 [测试数据 (test data)](/wiki/test-data)**：选择合适的输入数据（有效、无效、边界值）。
  4. **确定 [预期结果 (expected results)](/wiki/expected-result)**：定义预期的产出。
  5. **开发测试程序**：概述执行 **[测试用例 (Test Case)](/wiki/test-case)** 的步骤，包括 **[安装/设置 (setup)](/wiki/setup)** 和清理动作。
  6. **编写测试步骤**：详细描述执行测试所需的每个步骤。
  7. **分配前置条件**：指定执行前必须满足的条件。
  8. **执行 [测试用例 (Test Case)](/wiki/test-case)**：手动运行或使用自动化工具运行。
  9. **记录 [实际结果 (actual results)](/wiki/actual-result)**：记录执行结果。
  10. **比较预期结果与 [实际结果 (actual results)](/wiki/actual-result)**：评估测试是通过还是失败。
  11. **记录缺陷**：如果失败，记录遇到的问题。
  12. **评审与完善**：定期评审，保持 **[测试用例 (Test Case)](/wiki/test-case)** 的有效性。

- **测试用例在测试执行中的作用是什么？**
  在 **[测试执行 (test execution)](/wiki/test-execution)** 中，**测试用例 (Test Case)** 作为测试过程的基本单元。每个 **[测试用例 (test case)](/wiki/test-case)** 都是为了验证其预定的功能。
  执行过程中，**[测试用例 (Test Case)](/wiki/test-case)** 为测试人员提供了清晰的步骤序列、输入值和 **[预期结果 (expected results)](/wiki/expected-result)**。
  执行结果通常包括：
  - **通过 (Pass)**：行为符合预期。
  - **失败 (Fail)**：行为偏离预期，表示有缺陷。
  - **阻塞 (Blocked)**：由于外部因素无法执行。
  - **跳过 (Skipped)**：特意未执行。
  这些结果对于识别缺陷和维持 **[软件质量 (software quality)](/wiki/software-quality)** 至关重要。

- **如何执行测试用例？**
  在软件 **[测试自动化 (test automation)](/wiki/test-automation)** 中执行 **[测试用例 (test case)](/wiki/test-case)** 的典型步骤：
  1. **选择 [测试用例 (test case)](/wiki/test-case)**：从 **[测试管理 (test management)](/wiki/test-management)** 工具中识别。
  2. **准备 [测试环境 (test environment)](/wiki/test-environment)**。
  3. **运行测试**：使用 **[测试自动化 (test automation)](/wiki/test-automation)** 工具执行。
     ```javascript
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
  4. **监控 [测试执行 (test execution)](/wiki/test-execution)**。
  5. **评审结果**：根据预期产出判断 **[测试用例 (test case)](/wiki/test-case)** 是否通过。
  6. **报告**：在 **[测试管理 (test management)](/wiki/test-management)** 或缺陷跟踪系统中记录。
  7. **清理 [测试环境 (test environment)](/wiki/test-environment)**。

- **可以使用哪些工具来创建和管理测试用例？**
  - **TestRail**：基于 Web 的 **[测试用例管理 (test case management)](/wiki/test-case-management)** 工具。
  - **Zephyr**：集成在 JIRA 中。
  - **qTest**：Tricentis 平台的一部分。
  - **TestLink**：开源。
  - **Xray**：JIRA 插件。
  - **PractiTest**：SaaS 测试管理工具。
  - **TestLodge**：简单直观。
  - **TestCaseLab**：为 QA 工程师设计。
  - **SpiraTest**：集成测试管理。
  这些工具通常包含 **版本控制**、**[测试执行 (test execution)](/wiki/test-execution)** 历史、**可追溯性** 和 **报告** 等功能。

- **如何确定测试用例的成功或失败？**
  确定 **成功或失败 (success or failure)** 取决于 **预期产出 (expected outcome)** 与 **[实际结果 (actual result)](/wiki/actual-result)**。如果行为符合 **[预期结果 (expected result)](/wiki/expected-result)**，则 **[测试用例 (Test Case)](/wiki/test-case)** 被判定为 **成功 (successful)**。
  在 **[测试自动化 (test automation)](/wiki/test-automation)** 中，通常使用 **断言 (assertions)**：
  ```javascript
  assert.equals(actualResult, expectedResult, "Test Case failed: Actual result does not match expected result.");
  ```
  测试中的 **不稳定性 (Flakiness)** 可能会使这种评估变得复杂。
  **[代码覆盖率 (Code coverage)](/wiki/code-coverage)** 工具也可以辅助评估 **[测试用例 (Test Cases)](/wiki/test-case)** 的有效性。注意，单个失败可能是致命的，而全通并不保证没有 **[Bug (bug)](/wiki/bug)**。

#### 类型与示例
- **测试用例有哪些不同类型？**
  软件 **[测试自动化 (test automation)](/wiki/test-automation)** 中的 **[测试用例 (Test Cases)](/wiki/test-case)** 类型包括：
  - **单元测试用例 (Unit Test Cases)**：目标是代码的单个组件或函数。
  - **集成测试用例 (Integration Test Cases)**：确保多个组件协同工作。
  - **系统测试用例 (System Test Cases)**：验证完整的集成产品。
  - **冒烟测试用例 (Smoke Test Cases)**：执行基本功能的子集，也称 **[构建验证测试 (build verification testing)](/wiki/build-verification-testing)**。
  - **回归测试用例 (Regression Test Cases)**：检查新更改是否影响了现有功能。
  - **性能测试用例 (Performance Test Cases)**：评估响应能力、稳定性、扩展性。
  - **负载测试用例 (Load Test Cases)**：确定系统在正常及峰值负载下的行为。
  - **压力测试用例 (Stress Test Cases)**：将系统推向极限甚至崩溃点。
  - **安全测试用例 (Security Test Cases)**：识别漏洞。
  - **易用性测试用例 (Usability Test Cases)**：评估 UI/UX。
  - **兼容性测试用例 (Compatibility Test Cases)**：检查跨平台/浏览器表现。
  - **探索性测试用例 (Exploratory Test Cases)**：基于经验探索，无预定义步骤。
  - **[API (API)](/wiki/api) 测试用例**：通过测试 **[API (APIs)](/wiki/api)** 验证架构逻辑。
  - **UI 测试用例**：专注于图形界面和用户交互。
  每种类型对于确保 **[测试覆盖率 (test coverage)](/wiki/test-coverage)** 都至关重要。

- **你能提供一个好的测试用例示例吗？**
  **示例：用户登录功能**
  - **ID**: TC_LOGIN_01
  - **标题**: 验证使用有效凭据成功登录
  - **前置条件**: 用户在登录页面，测试环境已就绪。
  - **测试步骤**:
    1. 在用户名栏输入有效用户名。
    2. 在密码栏输入对应密码。
    3. 点击‘登录’按钮。
  - **预期结果**: 用户由于被重定向到主页并看到欢迎信息。
  - **实际结果**: *执行后填写*
  - **后置条件**: 用户注销并返回登录页面。
  - **状态**: *执行后填写 (通过/失败)*
  - **备注**: *补充观察*
  - **自动化脚本引用**: `loginTest.js`
  - **优先级**: 高
  - **自动化**: 是
  - **版本**: 1.0
  - **标签**: `Login`, `Smoke Test`

- **什么是正向测试用例和反向测试用例？**
  **正向 [测试用例 (Test Cases)](/wiki/test-case)** 验证系统在提供有效输入或在预期条件下时的行为。它们确认软件功能符合需求。
  ```javascript
  // 正向路径
  function testLoginWithValidCredentials() {
    enterUsername("validUser");
    enterPassword("correctPassword");
    clickLogin();
    assert(isLoggedIn() == true);
  }
  ```
  **反向 [测试用例 (test cases)](/wiki/test-case)** 则确保系统能优雅地处理无效输入或意外的用户行为，验证稳健性和错误处理。
  ```javascript
  // 反向路径
  function testLoginWithInvalidCredentials() {
    enterUsername("invalidUser");
    enterPassword("wrongPassword");
    clickLogin();
    assert(isLoggedIn() == false);
    assert(getErrorMessage() == "Invalid credentials");
  }
  ```

- **什么是功能测试用例？**
  **功能 [测试用例 (Test Case)](/wiki/test-case)** 是验证软件特定特性的动作集。它们根据 **[功能需求 (functional requirements)](/wiki/functional-requirements)**，通过输入并检查输出来验证系统“做什么”。
  ```javascript
  // 功能测试示例
  function testLoginValidUser() {
    navigateToLoginPage();
    enterUsername("validUser");
    enterPassword("correctPassword");
    clickLoginButton();
    assertUserIsLoggedIn();
  }
  ```

- **什么是非功能测试用例？**
  **非功能 [测试用例 (Test Case)](/wiki/test-case)** 关注系统“如何”运行，涉及性能、安全、易用性、可靠性和扩展性。它们验证系统的 **[非功能需求 (non-functional requirements)](/wiki/functional-requirements)**。
  例如性能 **[测试用例 (test case)](/wiki/test-case)**：
  - **ID**: NF_TC_001
  - **目标**: 评估峰值负载下的响应时间。
  - **预期结果**: 所有操作应在 2 秒内响应。
  通常使用 **[性能测试 (performance testing)](/wiki/performance-testing)** 工具（如 **[JMeter (JMeter)](/wiki/jmeter)** 进行 **[负载测试 (load testing)](/wiki/load-testing)**）或 **[安全测试 (security testing)](/wiki/security-testing)** 工具执行。

#### 最佳实践
- **编写有效测试用例的最佳实践有哪些？**
  - **清晰简洁**：使任何人都能轻松理解。
  - **使用描述性名称**。
  - **对 [测试用例 (Test Cases)](/wiki/test-case) 进行优先级排序**。
  - **包含前置条件**。
  - **定义 [预期结果 (expected results)](/wiki/expected-result)**。
  - **保持独立性**：每个 **[测试用例 (test case)](/wiki/test-case)** 都应是自包含的。
  - **参数化数据**。
  - **版本控制**。
  - **同行评审**。
  - **在适当时自动化**。
  - **维持可追溯性**：链接到需求以辅助 **[影响分析 (impact analysis)](/wiki/impact-analysis)**。
  - **定期重构**。
  - **避免重复**。
  - **平衡正反向测试**。

- **如何确保测试用例覆盖了所有可能的场景？**
  结合以下技术：
  - **[等价类划分 (Equivalence Partitioning)](/wiki/equivalence-partitioning)**。
  - **边界值分析**。
  - **判定表测试 (Decision Table Testing)**。
  - **状态转换测试 (State Transition Testing)**。
  - **用例测试 (Use Case Testing)**。
  - **组合测试**（如配对测试）。
  - **风险驱动测试 (Risk-Based Testing)**。
  - **探索性测试 (Exploratory Testing)**。
  - **用户故事和验收标准**。
  - **同行评审**。
  - **自动化测试生成工具**。
  由于资源限制，应关注关键路径并使用风险评估来指导 **[测试覆盖率 (test coverage)](/wiki/test-coverage)**。定期评审并更新 **[测试用例 (test cases)](/wiki/test-case)**。

- **创建测试用例时常见的错误有哪些？**
  - **忽视 [测试用例 (Test Case)](/wiki/test-case) 的独立性**：导致级联失败。
  - **模糊不清**：步骤不明确导致执行不一致。
  - **过度详细**：增加维护难度。
  - **忽视 [反向测试 (Negative Testing)](/wiki/negative-testing)**。
  - **未排序优先级**。
  - **缺乏版本控制**。
  - **评审不足**。
  - **命名规范差**。
  - **未规划重用性**。
  - **忽视管理 [测试环境 (test environment)](/wiki/test-environment)**。
  - **未能及时更新 [测试用例 (test cases)](/wiki/test-case)**。

- **测试用例应该多长时间评审和更新一次？**
  **[测试用例 (Test Cases)](/wiki/test-case)** 应该 **定期** 评审和更新：
  - 在应用程序任何变动后。
  - 在新特性发布后。
  - 在发现缺陷时（弥补覆盖缺口）。
  - 在敏捷环境中的迭代结束时。
  - 在常规的维护周期（如每季度）。
  自动化工具可以帮助标记过时的用例。一致性和 **适应性** 是关键。

- **如何提高测试用例的重用性？**
  - **模块化测试**：分解为可组合的功能块。
  - **使用数据驱动测试**：外部化测试数据。
  - **实施 [页面对象模型 (Page Object Model, POM)](/wiki/page-object-model)**：封装 UI 结构。
  - **参数化测试**：使其适用于不同场景。
  - **采用版本控制最佳实践**。
  - **文档化可重用组件**。
  通过这些方法，**[测试自动化 (test automation)](/wiki/test-automation)** 工程师可以创建灵活且易维护的 **[测试用例 (test cases)](/wiki/test-case)** 套件。
