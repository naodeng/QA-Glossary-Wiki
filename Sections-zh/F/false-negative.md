# 假阴性

<!-- TOC START -->
- [相关术语：](#相关术语：)
  - [另请参阅：](#另请参阅：)
- [关于假阴性的问题？](#关于假阴性的问题？)
  - [基础知识和理解](#基础知识和理解)
    - [软件测试中的漏报是什么？](#软件测试中的漏报是什么？)
    - [假阴性与假阳性有何不同？](#假阴性与假阳性有何不同？)
    - [软件测试中漏报的潜在原因有哪些？](#软件测试中漏报的潜在原因有哪些？)
    - [漏报如何影响整个测试过程？](#漏报如何影响整个测试过程？)
    - [软件测试中有哪些误报的例子？](#软件测试中有哪些误报的例子？)
  - [预防和处理](#预防和处理)
    - [可以使用哪些策略来防止漏报？](#可以使用哪些策略来防止漏报？)
    - [发生漏报时如何处理？](#发生漏报时如何处理？)
    - [识别漏报后应采取哪些步骤？](#识别漏报后应采取哪些步骤？)
    - [自动化如何帮助减少漏报的发生？](#自动化如何帮助减少漏报的发生？)
    - [质量保证在防止漏报方面发挥什么作用？](#质量保证在防止漏报方面发挥什么作用？)
  - [高级概念](#高级概念)
    - [漏报与测试覆盖率的概念有何关系？](#漏报与测试覆盖率的概念有何关系？)
    - [假阴性对回归测试有什么影响？](#假阴性对回归测试有什么影响？)
    - [漏报如何影响测试套件的可靠性？](#漏报如何影响测试套件的可靠性？)
    - [漏报如何影响敏捷开发中“快速失败”的概念？](#漏报如何影响敏捷开发中快速失败的概念？)
    - [漏报如何影响持续集成和部署过程？](#漏报如何影响持续集成和部署过程？)
<!-- TOC END -->

在

软件测试

, 一个

假阴性

指测试未能识别系统中实际存在的缺陷或问题的情况。换句话说，测试错误地表明软件运行正常，而实际上存在故障或问题

漏洞

。

漏报

可能会给人一种错误的安全感，导致团队相信软件的质量比实际的质量要高。此类错误尤其令人担忧，因为它可能会导致关键缺陷被忽视并到达生产环境，从而可能给用户或企业带来不良后果。

## 相关术语：

- [False Positive](../F/false-positive.md)

### 另请参阅：

- [Wikipedia](https://en.wikipedia.org/wiki/False_positives_and_false_negatives)

## 关于假阴性的问题？

### 基础知识和理解

#### 软件测试中的漏报是什么？

在[software testing](../S/software-testing.md) 中，当测试错误地通过而未能检测到现有缺陷时，会发生 **[false negative](../F/false-negative.md)**。这可能会导致未检测到的问题被推入生产环境，从而可能导致操作问题并影响用户体验。
  处理 [false negative](../F/false-negative.md) 涉及：

1. **调查**
    根本原因。

2. **修正**
    测试用例或环境设置。

3. **[Retesting](../R/retesting.md)**
    以确认现在已检测到问题。

4. **审查**
    类似问题的相关测试用例。

5. **更新中**
    测试策略以减轻未来发生的情况。
  自动化可以通过确保[test execution](../T/test-execution.md)和环境[setup](../S/setup.md)的一致性来减少[false negatives](../F/false-negative.md)。然而，定期**审查和维护**自动化测试以保持其有效性至关重要。
  [Quality assurance](../Q/quality-assurance.md) 通过执行严格的测试设计、彻底的审查流程和持续改进实践，在防止 [false negatives](../F/false-negative.md) 方面发挥着关键作用。
  [False negatives](../F/false-negative.md) 可能会给[test coverage](../T/test-coverage.md) 带来软件运行状况的误导性印象，从而破坏[test coverage](../T/test-coverage.md)。他们还可以通过允许 [bugs](../B/bug.md) 不被发现来破坏 [regression testing](../R/regression-testing.md)，从而可能在以后引起更严重的问题。
  在[agile development](../A/agile-development.md) 中，[false negatives](../F/false-negative.md) 由于延迟了缺陷检测而与“快速失败”原则发生冲突。对于持续集成和部署，它们可能会损害自动化管道的可靠性，从而导致错误构建的升级。
  为了最大限度地减少[false negatives](../F/false-negative.md)的影响，必须培养质量文化，投资于稳健的测试设计，并对[test execution](../T/test-execution.md)和分析保持警惕。

1. **调查**
    根本原因。

2. **修正**
    测试用例或环境设置。

3. **[Retesting](../R/retesting.md)**
    以确认现在已检测到问题。

4. **审查**
    类似问题的相关测试用例。

5. **更新中**
    测试策略以减轻未来发生的情况。

#### 假阴性与假阳性有何不同？

与 **[false negative](../F/false-negative.md)** 相比，**[false negative](../F/false-negative.md)** 测试错误地通过了缺陷，而 **[false positive](../F/false-positive.md)** 则在测试错误地使功能功能失败时发生。 [False positives](../F/false-positive.md) 可能与 [false negatives](../F/false-negative.md) 一样具有破坏性，导致在调试不存在的问题时浪费精力。
  虽然 [false negatives](../F/false-negative.md) 可能允许 [bugs](../B/bug.md) 进入生产环境，但 [false positives](../F/false-positive.md) 可能会破坏对测试套件的信任并引起不必要的警报。这两种类型的错误都需要检查 [test cases](../T/test-case.md) 和自动化脚本以确保准确性和可靠性。
  [False positives](../F/false-positive.md) 通常源于：

- 由于计时问题或外部依赖性而导致不稳定的测试
  - 不正确的测试断言或数据
  - 环境问题，例如配置问题或网络不稳定
  处理 [false positives](../F/false-positive.md) 涉及：

- 分析并纠正根本原因
  - 提高测试稳定性和准确性
  - 确保测试是幂等且可重复的
  在自动化 CI/CD 管道中，[false positives](../F/false-positive.md) 可以停止交付过程，需要立即注意以维持流程。平衡测试的敏感性以检测真正的问题而不被误报所困扰是至关重要的。

- 由于计时问题或外部依赖性而导致不稳定的测试
  - 不正确的测试断言或数据
  - 环境问题，例如配置问题或网络不稳定
  - 分析并纠正根本原因
  - 提高测试稳定性和准确性
  - 确保测试是幂等且可重复的

#### 软件测试中漏报的潜在原因有哪些？

[software testing](../S/software-testing.md) 中[false negatives](../F/false-negative.md) 的潜在原因可能包括：

- **[Flaky tests](../F/flaky-test.md)** ：在不更改代码的情况下间歇性通过或失败的测试可以掩盖真正的问题。
  - **不充分的[test data](../T/test-data.md)** ：如果测试数据不能代表生产数据，则可能不会触发某些缺陷。
  - **写得不好的断言**：不能准确反映需求的断言可能无法检测缺陷。
  - **计时问题**：未正确处理的异步操作可能会导致测试在确定实际结果之前通过。
  - **[Test environment](../T/test-environment.md) 差异**：测试环境和生产环境之间的差异可能会导致问题被忽视。
  - **过时的测试**：尚未更新以反映最近的代码更改的测试可能无法捕获新的缺陷。
  - **[Code coverage](../C/code-coverage.md) 间隙**：没有足够测试覆盖的应用程序区域可能包含未检测到的错误。
  - **配置错误[test tools](../T/test-tool.md)**：工具设置不正确可能会导致错过缺陷或误解测试结果。
  - **人为错误**：测试用例设计、实施或结果解释中的错误可能会导致被忽视的问题。
  为了缓解这些原因，定期检查和维护[test cases](../T/test-case.md)、数据和环境至关重要。此外，实施强大的日志记录和监控可以帮助识别测试结果和实际系统行为之间的差异。

- **[Flaky tests](../F/flaky-test.md)** ：在不更改代码的情况下间歇性地通过或失败的测试可以掩盖真正的问题。
  - **不充分的[test data](../T/test-data.md)** ：如果测试数据不能代表生产数据，则可能不会触发某些缺陷。
  - **写得不好的断言**：不能准确反映需求的断言可能无法检测缺陷。
  - **计时问题**：未正确处理的异步操作可能会导致测试在确定实际结果之前通过。
  - **[Test environment](../T/test-environment.md) 差异**：测试环境和生产环境之间的差异可能会导致问题被忽视。
  - **过时的测试**：尚未更新以反映最近的代码更改的测试可能无法捕获新的缺陷。
  - **[Code coverage](../C/code-coverage.md) 间隙**：没有足够测试覆盖的应用程序区域可能包含未检测到的错误。
  - **配置错误[test tools](../T/test-tool.md)**：工具设置不正确可能会导致错过缺陷或误解测试结果。
  - **人为错误**：测试用例设计、实施或结果解释中的错误可能会导致被忽视的问题。

#### 漏报如何影响整个测试过程？

[False negatives](../F/false-negative.md) 可能会**破坏测试过程中的信任**，导致**错误的安全感**。当测试未能检测到实际缺陷时，团队可能会继续部署，但只会在生产中遇到问题。这可能会导致**计划外工作**、**客户不满意**以及潜在的**收入损失**。
  随着时间的推移，[false negatives](../F/false-negative.md) 可能会**侵蚀[test suite](../T/test-suite.md) 的可信度**。如果利益相关者认为测试不可靠，他们可能会**降低其价值**，这可能会导致测试基础设施和资源的投资减少。
  此外，[false negatives](../F/false-negative.md) 可以**掩盖其他问题的存在**。例如，由于缺陷而应失败的测试可能会因不相关的问题而通过，例如[test environment](../T/test-environment.md)中的配置错误。这可能会分散对真正问题的注意力，导致在故障排除和诊断问题时**浪费精力**。
  在**风险管理**的背景下，[false negatives](../F/false-negative.md)可能导致**不充分的风险评估**。基于有缺陷的测试结果做出的决策可能无法准确反映实际风险，可能导致修复和更新的**不适当的优先级**。
  最后，在**敏捷或 CI/CD 环境**中，[false negatives](../F/false-negative.md) 的存在可能会破坏连续反馈流。这可能会减慢开发速度并延迟功能和修复的交付，最终影响开发周期的**速度和效率**。

#### 软件测试中有哪些误报的例子？

[software testing](../S/software-testing.md) 中的 [false negatives](../F/false-negative.md) 示例可能会因上下文和正在运行的测试类型而有很大差异。以下是一些场景：

1. **[Flaky Tests](../F/flaky-test.md)**：由于计时问题或外部依赖性，测试间歇性失败，但在特定运行中，尽管存在缺陷，但测试仍然通过。

    ```
    // Flaky test example
    it('should update the user profile', async () => {
      const profile = await getUserProfile();
      profile.email = 'new_email@example.com';
      await saveUserProfile(profile);
      // Flaky: Relies on timing for the profile to be saved
      expect(await getUserProfile()).toEqual(profile);
    });
    ```

2. **不完整的断言**：测试的断言没有完全覆盖功能，遗漏了一个缺陷。

    ```
    // Incomplete assertion example
    it('should calculate the total price', () => {
      const cart = { items: [{ price: 10 }, { price: 20 }] };
      const total = calculateTotal(cart);
      // Only checks if total is a number, not the correct sum
      expect(typeof total).toBe('number');
    });
    ```

3. **[Test Environment](../T/test-environment.md) 差异**：[test environment](../T/test-environment.md) 与生产不匹配，导致缺陷未被检测到。

    ```
    // Environment-specific test
    it('should connect to the database', () => {
      const dbConnection = connectToDatabase();
      // Passes if test environment has a different configuration
      expect(dbConnection.isConnected).toBeTruthy();
    });
    ```

4. **模拟/存根问题**：即使实际实现存在缺陷，错误配置的模拟或存根也可能导致测试通过。

    ```
    // Mocking issue example
    jest.mock('apiService', () => ({
      fetchData: jest.fn().mockResolvedValue('mocked data'),
    }));
    it('should fetch data from the API', async () => {
      const data = await fetchData();
      // Test passes due to mocked implementation, not actual API behavior
      expect(data).toBe('mocked data');
    });
    ```

5. **数据敏感性**：[test data](../T/test-data.md) 并不代表现实世界的场景，因此会遗漏边缘情况。

    ```
    // Data sensitivity example
    it('should process a transaction', () => {
      const transaction = { amount: 100, currency: 'USD' };
      const result = processTransaction(transaction);
      // Passes for this data set but may fail for different currencies or amounts
      expect(result).toHaveProperty('status', 'success');
    });
    ```在每种情况下，[test suite](../T/test-suite.md) 可能会报告通过，但由于概述的问题，代码库中可能仍然存在缺陷。

1. **[Flaky Tests](../F/flaky-test.md)**：由于计时问题或外部依赖性，测试间歇性失败，但在特定运行中，尽管存在缺陷，但测试仍会通过。

    ```
    // Flaky test example
    it('should update the user profile', async () => {
      const profile = await getUserProfile();
      profile.email = 'new_email@example.com';
      await saveUserProfile(profile);
      // Flaky: Relies on timing for the profile to be saved
      expect(await getUserProfile()).toEqual(profile);
    });
    ```

2. **不完整的断言**：测试的断言没有完全覆盖功能，遗漏了一个缺陷。

    ```
    // Incomplete assertion example
    it('should calculate the total price', () => {
      const cart = { items: [{ price: 10 }, { price: 20 }] };
      const total = calculateTotal(cart);
      // Only checks if total is a number, not the correct sum
      expect(typeof total).toBe('number');
    });
    ```

3. **[Test Environment](../T/test-environment.md) 差异**：[test environment](../T/test-environment.md) 与生产不匹配，导致缺陷未被检测到。

    ```
    // Environment-specific test
    it('should connect to the database', () => {
      const dbConnection = connectToDatabase();
      // Passes if test environment has a different configuration
      expect(dbConnection.isConnected).toBeTruthy();
    });
    ```

4. **模拟/存根问题**：即使实际实现存在缺陷，错误配置的模拟或存根也可能导致测试通过。

    ```
    // Mocking issue example
    jest.mock('apiService', () => ({
      fetchData: jest.fn().mockResolvedValue('mocked data'),
    }));
    it('should fetch data from the API', async () => {
      const data = await fetchData();
      // Test passes due to mocked implementation, not actual API behavior
      expect(data).toBe('mocked data');
    });
    ```

5. **数据敏感性**：[test data](../T/test-data.md) 并不代表现实世界的场景，因此会遗漏边缘情况。

    ```
    // Data sensitivity example
    it('should process a transaction', () => {
      const transaction = { amount: 100, currency: 'USD' };
      const result = processTransaction(transaction);
      // Passes for this data set but may fail for different currencies or amounts
      expect(result).toHaveProperty('status', 'success');
    });
    ```

### 预防和处理

#### 可以使用哪些策略来防止漏报？

要防止软件 [test automation](../T/test-automation.md) 中出现 [false negatives](../F/false-negative.md)，请考虑以下策略：

- **审查和完善[Test Cases](../T/test-case.md)**：定期审查[test cases](../T/test-case.md) 的准确性和相关性。更新它们以反映应用程序中的更改并消除任何可能导致误解的歧义。
  - **提高[Test Data](../T/test-data.md) 质量**：确保[test data](../T/test-data.md) 代表生产数据。使用数据清理和匿名技术来维护数据完整性而不损害隐私。
  - **增强[Test Environment](../T/test-environment.md)稳定性**：尽可能模仿生产环境。解决可能导致不稳定测试行为的环境问题，例如网络延迟或资源限制。
  - **有效利用断言**：写出清晰准确的断言。避免过于宽泛或不具体的断言，否则可能会错过失败。
  - **实施强大的错误处理**：设计测试以优雅地处理意外情况。这包括正确的异常处理和恢复场景。
  - **同步[Test Execution](../T/test-execution.md)**：引入等待或同步点来处理异步操作和动态内容，减少与时序相关的[false negatives](../F/false-negative.md)。
  - **定期更新自动化工具**：保持自动化框架和工具处于最新状态，以利用改进和[bug](../B/bug.md)修复，从而减少[false negatives](../F/false-negative.md)。
  - **进行代码审查**：对 [test scripts](../T/test-script.md) 进行同行审查，以发现可能导致 [false negatives](../F/false-negative.md) 的潜在问题。
  - **监控测试不稳定**：跟踪 [flaky tests](../F/flaky-test.md) 并调查根本原因。解决竞争条件或不可靠依赖项等问题。
  - **促进协作**：鼓励开发人员、测试人员和运营人员之间进行协作，以分享有助于识别和预防 [false negatives](../F/false-negative.md) 的知识和见解。
  通过实施这些策略，[test automation](../T/test-automation.md) 工程师可以最大限度地减少[false negatives](../F/false-negative.md) 的发生，确保测试过程更加可靠和有效。

- **审查和完善[Test Cases](../T/test-case.md)**：定期审查[test cases](../T/test-case.md) 的准确性和相关性。更新它们以反映应用程序中的更改并消除任何可能导致误解的歧义。
  - **提高[Test Data](../T/test-data.md) 质量**：确保[test data](../T/test-data.md) 代表生产数据。使用数据清理和匿名技术来维护数据完整性而不损害隐私。
  - **增强[Test Environment](../T/test-environment.md)稳定性**：尽可能模仿生产环境。解决可能导致不稳定测试行为的环境问题，例如网络延迟或资源限制。
  - **有效利用断言**：写出清晰准确的断言。避免过于宽泛或不具体的断言，否则可能会错过失败。
  - **实施强大的错误处理**：设计测试以优雅地处理意外情况。这包括正确的异常处理和恢复场景。
  - **同步[Test Execution](../T/test-execution.md)**：引入等待或同步点来处理异步操作和动态内容，减少与时序相关的[false negatives](../F/false-negative.md)。
  - **定期更新自动化工具**：保持自动化框架和工具处于最新状态，以利用改进和[bug](../B/bug.md)修复，从而减少[false negatives](../F/false-negative.md)。
  - **进行代码审查**：对 [test scripts](../T/test-script.md) 进行同行审查，以发现可能导致 [false negatives](../F/false-negative.md) 的潜在问题。
  - **监控测试不稳定**：跟踪 [flaky tests](../F/flaky-test.md) 并调查根本原因。解决竞争条件或不可靠依赖项等问题。
  - **促进协作**：鼓励开发人员、测试人员和运营人员之间进行协作，以分享有助于识别和预防 [false negatives](../F/false-negative.md) 的知识和见解。

#### 发生漏报时如何处理？

有效处理[false negative](../F/false-negative.md)需要立即采取行动和长期战略相结合。这是一个简洁的指南：

1. **隔离事件**：一旦检测到漏报，隔离测试用例，防止其影响其他测试。
  2. **分析和重现** ：分析测试结果和环境，了解发生假阴性的原因。尝试重现该问题以确保它不是一次性事件。
  3. **修复测试**：如果漏报是由于测试本身的缺陷造成的，例如不正确的断言或计时问题，请更新测试以准确反映预期行为。
  4. **改进[Test Data](../T/test-data.md)** ：确保测试数据具有代表性和最新性，以避免测试场景与实际使用情况不匹配。
  5. **增强[Test Environment](../T/test-environment.md)** ：使测试环境与生产环境尽可能保持一致，以减少差异。
  6. **监控不稳定**：实施一个系统来跟踪不稳定的测试。如果测试经常导致漏报，请优先修复或重构它。
  7. **更新文档**：记录误报以及解决该问题所采取的步骤，以便有记录供将来参考。
  8. **教育团队**：与您的团队分享经验教训，以防止将来出现类似问题。
  通过执行这些步骤，您可以减轻[false negatives](../F/false-negative.md) 的影响并提高[test automation](../T/test-automation.md) 套件的可靠性。请记住，目标是确保您的自动化测试始终提供值得信赖的反馈来支持开发过程。

1. **隔离事件**：一旦检测到漏报，隔离测试用例，防止其影响其他测试。
  2. **分析和重现** ：分析测试结果和环境，了解发生假阴性的原因。尝试重现该问题以确保它不是一次性事件。
  3. **修复测试**：如果漏报是由于测试本身的缺陷造成的，例如不正确的断言或计时问题，请更新测试以准确反映预期行为。
  4. **改进[Test Data](../T/test-data.md)** ：确保测试数据具有代表性和最新性，以避免测试场景与实际使用情况不匹配。
  5. **增强[Test Environment](../T/test-environment.md)** ：使测试环境尽可能与生产环境保持一致，以减少差异。
  6. **监控不稳定**：实施一个系统来跟踪不稳定的测试。如果测试经常导致漏报，请优先修复或重构它。
  7. **更新文档**：记录误报以及解决该问题所采取的步骤，以便有记录供将来参考。
  8. **教育团队**：与您的团队分享经验教训，以防止将来出现类似问题。

#### 识别漏报后应采取哪些步骤？

识别[false negative](../F/false-negative.md)后：

1. **分析**
    通过检查测试日志、代码和测试数据来找出根本原因。

2. **正确**
    测试脚本或环境设置（如果它们导致了问题）。

3. **更新**
    测试用例以确保它准确地检测到预期的故障。

4. **重新运行**
    确认假阴性的测试已解决。

5. **文件**
    事件和解决方案以供将来参考。

6. **沟通**
    与团队一起调查结果以提高认识。

7. **审查**
    潜在类似问题的相关测试用例。

8. **监控**
    测试套件可以快速捕获任何重复发生的情况。

9. **重构**
    必要时进行测试以提高可靠性和可维护性。

10. **增强**
    更准确地说，是检测机制或断言。

  ```
  // Example: Enhancing an assertion in a test script
  expect(actualValue).toBeCloseTo(expectedValue, precision);
  ```

1. **整合**
    将吸取的经验教训纳入测试策略，以防止未来出现漏报。

2. **调整**
    阈值或启发式（如果它们导致漏报）。

3. **考虑**
    需要额外或替代工具来改进检测。

4. **优先考虑**
    根据对产品质量的潜在影响进行修复。

5. **验证**
    定期测试整个测试套件的有效性以确保可靠性。

1. **分析**
    通过检查测试日志、代码和测试数据来找出根本原因。

2. **正确**
    测试脚本或环境设置（如果它们导致了问题）。

3. **更新**
    测试用例以确保它准确地检测到预期的故障。

4. **重新运行**
    确认假阴性的测试已解决。

5. **文件**
    事件和解决方案以供将来参考。

6. **沟通**
    与团队一起调查结果以提高认识。

7. **审查**
    潜在类似问题的相关测试用例。

8. **监控**
    测试套件可以快速捕获任何重复发生的情况。

9. **重构**
    必要时进行测试以提高可靠性和可维护性。

10. **增强**
    更准确地说，是检测机制或断言。

1. **整合**
    将吸取的经验教训纳入测试策略，以防止未来出现漏报。

2. **调整**
    阈值或启发式（如果它们导致漏报）。

3. **考虑**
    需要额外或替代工具来改进检测。

4. **优先考虑**
    根据对产品质量的潜在影响进行修复。

5. **验证**
    定期测试整个测试套件的有效性以确保可靠性。

#### 自动化如何帮助减少漏报的发生？

通过确保[test execution](../T/test-execution.md)中的**一致性**和**准确性**，自动化可以显着**减少[software testing](../S/software-testing.md)中的[false negatives](../F/false-negative.md)**。自动化测试是脚本化的，一旦编写，每次运行时都会执行相同的操作，这消除了可能导致[false negatives](../F/false-negative.md)的人为错误因素。
  使用**持续集成**工具，可以频繁运行自动化测试，确保代码库中的更改得到一致验证，这有助于及早发现可能会被遗漏和错误标记为通过的问题（[false negatives](../F/false-negative.md)）。
  此外，自动化支持实现**全面的[test suites](../T/test-suite.md)**，它可以覆盖广泛的场景，包括可能无法彻底手动测试的边缘情况。这种广泛的覆盖范围增加了发现缺陷的可能性。
  自动化测试还可以与实时跟踪和报告测试结果的**监控工具**集成。这种集成可以帮助快速识别测试结果中可能指示[false negative](../F/false-negative.md)的任何异常，从而可以立即进行调查和解决。
  此外，自动化框架通常带有**内置重试机制**，可以配置为自动重新运行失败的测试，以排除间歇性问题或环境问题作为失败的原因，从而减少[false negatives](../F/false-negative.md)的机会。
  最后，自动化允许实施**数据驱动测试**，其中使用各种输入组合执行测试。这种方法确保应用程序针对更广泛的数据集进行测试，这可以发现如果不进行测试则可能导致[false negatives](../F/false-negative.md) 的缺陷。
  总之，自动化通过提供一致、准确和广泛的测试能力来增强对真阴性的检测。

#### 质量保证在防止漏报方面发挥什么作用？

[Quality Assurance](../Q/quality-assurance.md) (QA) 通过确保[test automation](../T/test-automation.md) 框架、[test cases](../T/test-case.md) 和整体测试环境稳健可靠，在**预防[false negatives](../F/false-negative.md)** 中发挥着关键作用。质量检查团队负责：

- **设计全面的[test cases](../T/test-case.md)**
    涵盖广泛的场景，包括边缘情况，以最大限度地减少由于未经测试的路径而导致漏报的风险。

- **保持准确和最新的[test data](../T/test-data.md)**
    确保测试反映现实条件并能够准确检测故障。

- **定期审查和更新[test scripts](../T/test-script.md)**
    与应用程序中的更改保持一致，从而防止过时的测试造成的漏报。

- **实施制衡**
    例如代码审查和结对编程，以捕获测试代码中可能导致漏报的错误。

- **监控[test execution](../T/test-execution.md)**
    快速识别并解决测试环境或测试基础设施中可能导致漏报的任何问题。

- **分析测试结果**
    彻底区分真实通行证和漏报，确保调查任何可疑通行证。

- **确保正确的配置管理**
    以便测试在一致的环境中运行，减少环境因素导致漏报的机会。
  通过关注这些领域，QA 有助于为[test automation](../T/test-automation.md) 奠定坚实的基础，降低[false negatives](../F/false-negative.md) 的可能性并保持测试过程的完整性。

- **设计全面的[test cases](../T/test-case.md)**
    涵盖广泛的场景，包括边缘情况，以最大限度地减少由于未经测试的路径而导致漏报的风险。

- **保持准确和最新的[test data](../T/test-data.md)**
    确保测试反映现实条件并能够准确检测故障。

- **定期审查和更新[test scripts](../T/test-script.md)**
    与应用程序中的更改保持一致，从而防止过时的测试造成的漏报。

- **实施制衡**
    例如代码审查和结对编程，以捕获测试代码中可能导致漏报的错误。

- **监控[test execution](../T/test-execution.md)**
    快速识别并解决测试环境或测试基础设施中可能导致漏报的任何问题。

- **分析测试结果**
    彻底区分真实通行证和漏报，确保调查任何可疑通行证。

- **确保正确的配置管理**
    以便测试在一致的环境中运行，减少环境因素导致漏报的机会。

### 高级概念

#### 漏报与测试覆盖率的概念有何关系？

[False negatives](../F/false-negative.md) 可以通过提供**误导性的安全感**来**破坏[test coverage](../T/test-coverage.md) 的有效性**。 [Test coverage](../T/test-coverage.md) 通常测量 [test suite](../T/test-suite.md) 执行源代码的程度。但是，如果 [test case](../T/test-case.md) 由于 [false negative](../F/false-negative.md)（存在缺陷但测试未检测到它）而通过，则覆盖率指标可能无法准确反映代码可靠性的真实状态。
  在 [test coverage](../T/test-coverage.md) 较高的情况下，利益相关者可能会相信该软件经过了充分测试且稳定。但是，[false negatives](../F/false-negative.md) 可能意味着某些缺陷未被捕获，尽管在测试期间正在执行代码路径。这可能会导致软件版本中出现**未识别的风险**，因为覆盖率指标不考虑测试结果的准确性。
  为了保持 [test coverage](../T/test-coverage.md) 的完整性，确保测试不仅覆盖代码，而且**有效地断言**正确的行为至关重要。这涉及：

- 严格的测试用例设计，覆盖不同场景。
  - 持续审查和增强测试用例以捕获边缘情况。
  - 实施
    **强大的断言机制**
    以减少忽视故障的可能性。
  通过主动解决[false negatives](../F/false-negative.md)，[test automation](../T/test-automation.md) 工程师可以确保高[test coverage](../T/test-coverage.md) 转化为高[software quality](../S/software-quality.md)，从而保持对[test suite](../T/test-suite.md) 检测缺陷能力的信任。

- 严格的测试用例设计，覆盖不同场景。
  - 持续审查和增强测试用例以捕获边缘情况。
  - 实施
    **强大的断言机制**
    以减少忽视故障的可能性。

#### 假阴性对回归测试有什么影响？

[regression testing](../R/regression-testing.md) 中的[False negatives](../F/false-negative.md) 可能会对软件的质量和稳定性产生**重大影响**。当测试未能检测到现有缺陷时，软件可能会通过管道进行**未检测到的问题**，并有可能进入生产阶段。这可能会导致：

- **未发现的回归**：关键功能可能会在未被注意到的情况下崩溃，从而导致糟糕的用户体验。
  - **风险增加**：随着测试套件提供的安全网变得不可靠，对发布的信心会降低。
  - **浪费资源**：需要额外的时间和精力来诊断和修复本应尽早发现的问题。
  - **延迟发布**：后期发现问题可能会导致发布延迟并增加开发成本。
  为了减轻这些影响，团队应该：

- 定期
    **审查和更新**
    测试用例以确保它们与应用程序同步。

- 实施
    **强大的日志记录**
    和
    **监控**
    发现测试中漏掉的问题。

- 使用
    **[risk-based testing](../R/risk-based-testing.md)**
    优先考虑应用程序中最关键的领域。

- 培养一个
    **品质文化**
    ，开发人员和测试人员密切合作以了解变更及其潜在影响。
  总之，[false negatives](../F/false-negative.md) 可能会破坏[regression testing](../R/regression-testing.md) 的有效性，但通过积极主动的策略和对质量的关注，可以将其影响降至最低。

- **未发现的回归**：关键功能可能会在未被注意到的情况下崩溃，从而导致糟糕的用户体验。
  - **风险增加**：随着测试套件提供的安全网变得不可靠，对发布的信心会降低。
  - **浪费资源**：需要额外的时间和精力来诊断和修复本应尽早发现的问题。
  - **延迟发布**：后期发现问题可能会导致发布延迟并增加开发成本。
  - 定期
    **审查和更新**
    测试用例以确保它们与应用程序同步。

- 实施
    **强大的日志记录**
    和
    **监控**
    发现测试中漏掉的问题。

- 使用
    **[risk-based testing](../R/risk-based-testing.md)**
    优先考虑应用程序中最关键的领域。

- 培养一个
    **品质文化**
    ，开发人员和测试人员密切合作以了解变更及其潜在影响。

#### 漏报如何影响测试套件的可靠性？

[False negatives](../F/false-negative.md) 可以**破坏[test suites](../T/test-suite.md) 中的信任**，导致**错误的安全感**。当测试未能检测到实际缺陷时，团队可能会继续部署，但只会在生产中遇到问题。这可能会导致**意外停机**、**客户不满意**以及**由于需要修补或回滚而导致成本增加**。
  此外，[false negatives](../F/false-negative.md) 可以**扭曲用于衡量软件质量的指标**，例如缺陷密度或平均故障时间。这种不实陈述可能会影响决策过程、资源分配和开发任务的优先级。
  在**持续集成 (CI)** 和 **持续部署 (CD)** 的背景下，[false negatives](../F/false-negative.md) 可能会导致通过管道推广不稳定的构建，从而损害交付过程的完整性。这也可能**增加开发人员和测试人员的工作量**，他们必须识别并纠正遗漏的缺陷。
  为了维护 [test suites](../T/test-suite.md) 的可靠性，**定期审查和更新** [test cases](../T/test-case.md) 至关重要，确保它们对应用程序中的更改敏感。此外，结合**代码审查**、**结对编程**和**跨职能团队协作**可以帮助及早发现和预防[false negatives](../F/false-negative.md)。
  在奉行“快速失败”理念的敏捷环境中，[false negatives](../F/false-negative.md) 可能会破坏反馈循环，延迟问题的识别和产品的迭代改进。因此，维护健壮可靠的[test suite](../T/test-suite.md) 对于敏捷团队实现快速[iterations](../I/iteration.md) 和频繁发布的好处至关重要。

#### 漏报如何影响敏捷开发中“快速失败”的概念？

[test automation](../T/test-automation.md) 中的[False negatives](../F/false-negative.md) 可能会严重破坏[agile development](../A/agile-development.md) 中的**快速失败**原则。该原则强调快速识别和解决问题以保持快速开发速度并确保高质量交付成果的重要性。当测试由于[false negatives](../F/false-negative.md)而错误地通过时，缺陷可能会漏掉而未被发现，从而导致：

- **延迟反馈**：开发人员不会实时收到缺陷警报，这可能会导致在开发周期后期进行更复杂且耗时的修复。
  - **技术债务增加**：随着缺陷的累积而未被注意到，代码库的质量会下降，可能会导致更难以解决的问题的滚雪球效应。
  - **信任被侵蚀**：测试套件的可靠性受到损害，这可能导致对测试结果的怀疑以及对失败测试的潜在忽视。
  - **资源分配不当**：团队可能会在新功能或重构工作上浪费时间和资源，而没有意识到存在需要首先解决的潜在问题。
  为了与**快速失败**方法保持一致，团队应该：

- 实施稳健的
    **测试验证**
    以确保测试能够准确地检测到故障。

- 行为
    **频繁的测试回顾**
    捕捉可能导致漏报的情况。

- 利用
    **监控和警报**
    检测可能指示漏报的测试行为异常的系统。

- 培养一种文化
    **持续改进**
    定期更新测试套件以反映应用程序中的更改并尽早发现缺陷。

- **延迟反馈**：开发人员不会实时收到缺陷警报，这可能会导致在开发周期后期进行更复杂且耗时的修复。
  - **技术债务增加**：随着缺陷的累积而未被注意到，代码库的质量会下降，可能会导致更难以解决的问题的滚雪球效应。
  - **信任被侵蚀**：测试套件的可靠性受到损害，这可能导致对测试结果的怀疑以及对失败测试的潜在忽视。
  - **资源分配不当**：团队可能会在新功能或重构工作上浪费时间和资源，而没有意识到存在需要首先解决的潜在问题。
  - 实施稳健的
    **测试验证**
    以确保测试能够准确地检测到故障。

- 行为
    **频繁的测试回顾**
    捕捉可能导致漏报的情况。

- 利用
    **监控和警报**
    检测可能指示漏报的测试行为异常的系统。

- 培养一种文化
    **持续改进**
    定期更新测试套件以反映应用程序中的更改并尽早发现缺陷。

#### 漏报如何影响持续集成和部署过程？

[False negatives](../F/false-negative.md) 在持续集成 (CI) 和部署的背景下可能会导致**重大风险**和**低效率**。当测试未能检测到实际缺陷时，这些 [bugs](../B/bug.md) 可能会通过 CI 管道传播，并可能到达生产环境。这可能会导致：

- **未检测到的问题**：严重错误可能会进入生产环境，导致系统故障或用户面临的问题，从而损害软件和组织的声誉。
  - **无效的反馈循环**：CI 依赖自动化测试来提供快速反馈。漏报会破坏这一点，导致错误的安全感和延迟识别问题。
  - **资源浪费**：时间和资源花费在部署和监控错误版本上，只有在最终检测到问题时才将其回滚。
  - **信任侵蚀**：随着时间的推移，测试套件的可靠性受到质疑，这可能会导致人们对测试过程和自动化工作的信心下降。
  为了减轻这些影响，至关重要的是：

- **审查测试结果**：定期分析测试结果以确保准确性。
  - **监控部署**：实施监控和警报工具以快速捕获部署后的问题。
  - **改进测试设计**：不断完善测试以涵盖可能导致漏报的边缘情况和场景。
  - **促进协作**：鼓励开发人员、测试人员和运营人员共同努力，了解和解决误报的根本原因。
  通过主动解决[false negatives](../F/false-negative.md)，团队可以维护 CI/CD 管道的完整性，确保只有经过充分测试的高质量代码才能部署到生产中。

- **未检测到的问题**：严重错误可能会进入生产环境，导致系统故障或用户面临的问题，从而损害软件和组织的声誉。
  - **无效的反馈循环**：CI 依赖自动化测试来提供快速反馈。漏报会破坏这一点，导致错误的安全感和延迟识别问题。
  - **资源浪费**：时间和资源花费在部署和监控错误版本上，只有在最终检测到问题时才将其回滚。
  - **信任侵蚀**：随着时间的推移，测试套件的可靠性受到质疑，这可能会导致人们对测试过程和自动化工作的信心下降。
  - **审查测试结果**：定期分析测试结果以确保准确性。
  - **监控部署**：实施监控和警报工具以快速捕获部署后的问题。
  - **改进测试设计**：不断完善测试以涵盖可能导致漏报的边缘情况和场景。
  - **促进协作**：鼓励开发人员、测试人员和运营人员共同努力，了解和解决误报的根本原因。
