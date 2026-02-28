# 预期结果

<!-- TOC START -->
- [对预期结果有疑问吗？](#对预期结果有疑问吗？)
  - [基础知识和重要性](#基础知识和重要性)
    - [软件测试中的“预期结果”是什么？](#软件测试中的预期结果是什么？)
    - [为什么定义“预期结果”在软件测试中很重要？](#为什么定义预期结果在软件测试中很重要？)
    - [“预期结果”对整个测试过程有何贡献？](#预期结果对整个测试过程有何贡献？)
    - [如果“预期结果”定义不正确会发生什么？](#如果预期结果定义不正确会发生什么？)
  - [创建和使用](#创建和使用)
    - [“预期结果”是如何创建的？](#预期结果是如何创建的？)
    - [谁通常负责定义“预期结果”？](#谁通常负责定义预期结果？)
    - [在测试过程中如何使用“预期结果”？](#在测试过程中如何使用预期结果？)
    - [在测试过程中“预期结果”会改变吗？](#在测试过程中预期结果会改变吗？)
  - [比较与分析](#比较与分析)
    - [使用哪些工具或技术来比较“预期结果”与“实际结果”？](#使用哪些工具或技术来比较预期结果与实际结果？)
    - [如果“预期结果”与“实际结果”不匹配，这意味着什么？](#如果预期结果与实际结果不匹配，这意味着什么？)
    - [如何分析“预期结果”与“实际结果”之间的差异？](#如何分析预期结果与实际结果之间的差异？)
  - [最佳实践](#最佳实践)
    - [定义“预期结果”的最佳实践有哪些？](#定义预期结果的最佳实践有哪些？)
    - [如何有效地记录“预期结果”？](#如何有效地记录预期结果？)
    - [定义“预期结果”时要避免哪些常见错误？](#定义预期结果时要避免哪些常见错误？)
    - [如何将“预期结果”有效地传达给测试团队？](#如何将预期结果有效地传达给测试团队？)
<!-- TOC END -->

特定情况下的预期结果

测试用例

运行。

## 对预期结果有疑问吗？

### 基础知识和重要性

#### 软件测试中的“预期结果”是什么？

在[software testing](../S/software-testing.md) 中，**[Expected Result](../E/expected-result.md)** 是[test case](../T/test-case.md) 在指定条件下执行时应产生的预定义输出或行为。它源自软件的需求或设计规范，并作为测试过程中验证系统实际响应正确性的基准。
  [Expected Results](../E/expected-result.md) 对于自动化测试至关重要，因为它们使自动化框架能够在无需人工干预的情况下确定通过或失败的结果。运行测试时，自动化工具会捕获 **[Actual Result](../A/actual-result.md)** 并将其与 [Expected Result](../E/expected-result.md) 进行比较。匹配确认系统按预期运行，而不匹配可能表明测试本身存在缺陷或问题。
  [Expected Results](../E/expected-result.md) 应**清晰**、**简洁**和**明确**，以确保[test automation](../T/test-automation.md) 可靠。它们通常以自动化工具可以轻松比较的格式表示，例如布尔值、字符串、数字或更复杂的数据结构。
  例如，登录函数的测试可能会将 [Expected Result](../E/expected-result.md) 定义为：

  ```
  {
    success: true,
    userId: 12345,
    message: "User logged in successfully."
  }
  ```然后，自动化脚本将断言 [Actual Result](../A/actual-result.md) 与该对象匹配以验证测试。如果 [Actual Result](../A/actual-result.md) 出现偏差，脚本会将测试标记为失败，从而促使进一步调查。

#### 为什么定义“预期结果”在软件测试中很重要？

定义 **[Expected Result](../E/expected-result.md)** 在 [software testing](../S/software-testing.md) 中至关重要，因为它充当验证软件行为正确性的基准。如果没有明确的预期结果，测试人员无法最终确定测试是否通过或失败，从而导致模糊性和潜在的缺陷监督。它确保软件的功能符合要求和设计规范，为[test execution](../T/test-execution.md)期间的比较提供具体基础。
  明确定义的 [expected result](../E/expected-result.md) 还允许执行断言检查，以编程方式比较预期结果和实际结果，从而促进自动化测试验证。这种比较对于持续集成和交付管道至关重要，其中自动化测试必须可靠地评估软件的稳定性，而无需人工干预。
  此外，当 [expected results](../E/expected-result.md) 没有明确定义时，可能会导致测试工作不一致，不同的测试人员可能对成功测试的构成有不同的解释。这种不一致可能会导致 [test coverage](../T/test-coverage.md) 中的差距以及对软件质量的错误信心。
  总之，[expected results](../E/expected-result.md) 的定义是结构化且有效的测试过程的基础，确保测试可重复、结果可解释以及软件满足其预期行为。

#### “预期结果”对整个测试过程有何贡献？

*预期结果*对于指导 **[test automation](../T/test-automation.md) 流程**至关重要。它充当根据预定义标准验证软件行为的**基准**。通过明确的预期结果，自动化测试可以**立即**并**准确**确定[test case](../T/test-case.md) 是否通过或失败，从而简化测试周期。
  在缺乏明确定义的[expected result](../E/expected-result.md)的情况下，自动化测试缺乏方向，可能导致**[false positives](../F/false-positive.md)或负面**。这种清晰度确保自动化测试**可靠**和**可维护**，因为团队成员可以轻松理解和更新它们。
  在[test execution](../T/test-execution.md)期间，自动化框架**比较**[expected result](../E/expected-result.md)与实际结果，标记差异。 [test scripts](../T/test-script.md) 中的 **断言** 通常可以促进这种比较：

  ```
  assert.equals(actualResult, expectedResult, "The results do not match.");
  ```当发生不匹配时，它们会触发对测试或应用程序代码中潜在缺陷或必要更新的**调查**。因此，[expected result](../E/expected-result.md) 充当[quality assurance](../Q/quality-assurance.md) 的**控制点**，确保软件满足其要求。
  此外，有据可查的[expected results](../E/expected-result.md) 支持团队成员之间的**协作**，因为它们可以清楚地了解每个测试旨在验证的内容。这种透明度对于**持续集成**和**交付管道**至关重要，其中测试需要由各个利益相关者执行和理解。
  总之，[expected results](../E/expected-result.md) 是 [test automation](../T/test-automation.md) 流程的**效率**和**有效性**不可或缺的一部分，确保 [software quality](../S/software-quality.md) 始终根据既定标准进行衡量。

#### 如果“预期结果”定义不正确会发生什么？

如果 **[Expected Result](../E/expected-result.md)** 定义不正确，可能会出现几个问题：

- **[False Positives](../F/false-positive.md)/Negatives** ：测试可能在应该失败时通过（误报），或者在应该通过时失败（误报），从而导致对软件质量的错误假设。
  - **浪费资源**：时间和精力花费在故障排除和调查“问题”上，而这些“问题”实际上是对预期行为的误解。
  - **沟通不畅**：预期结果的模糊性可能会导致团队成员之间产生混乱，从而可能导致测试实施不一致和产品目标不一致。
  - **无效测试**：测试套件的有效性受到损害，因为它可能无法准确反映用户要求或业务需求。
  - **延迟交付**：错误定义的预期结果可能会导致开发周期延迟，因为需要额外的时间来纠正和重新运行测试。
  - **差[Quality Assurance](../Q/quality-assurance.md)**：最终，如果未识别缺陷或由于预期结果不准确而错误地排除缺陷，则软件的质量可能会受到影响。
  为了缓解这些问题，请确保 [expected results](../E/expected-result.md) 在 [test execution](../T/test-execution.md) 之前由所有利益相关者**明确定义**、**审核**并**同意**。定期**审查和更新** [expected results](../E/expected-result.md) 以适应不断变化的需求。

- **[False Positives](../F/false-positive.md)/Negatives** ：测试可能在应该失败时通过（误报），或者在应该通过时失败（误报），从而导致对软件质量的错误假设。
  - **浪费资源**：时间和精力花费在故障排除和调查“问题”上，而这些“问题”实际上是对预期行为的误解。
  - **沟通不畅**：预期结果的模糊性可能会导致团队成员之间产生混乱，从而可能导致测试实施不一致和产品目标不一致。
  - **无效测试**：测试套件的有效性受到损害，因为它可能无法准确反映用户要求或业务需求。
  - **延迟交付**：错误定义的预期结果可能会导致开发周期延迟，因为需要额外的时间来纠正和重新运行测试。
  - **差[Quality Assurance](../Q/quality-assurance.md)**：最终，如果未识别缺陷或由于预期结果不准确而错误地排除缺陷，则软件的质量可能会受到影响。

### 创建和使用

#### “预期结果”是如何创建的？

创建 **[Expected Result](../E/expected-result.md)** 涉及分析软件的**要求**和**规范**，以确定 [test case](../T/test-case.md) 的正确结果。这是一个分步方法：

1. **审查要求**：彻底检查功能性和非[functional requirements](../F/functional-requirements.md) 或用户故事，以了解预期行为。
  2. **了解上下文**：考虑应用程序的上下文，包括用户期望和业务逻辑。
  3. **推导逻辑结果**：根据需求，推导给定输入或操作的逻辑结果。
  4. **与利益相关者协商**：与开发人员、业务分析师或产品所有者合作，以澄清任何歧义。
  5. **使用数据模型**：参考数据模型或模式来预测 [database](../D/database.md) 相关测试的结果。
  6. **考虑边缘情况**：确定边界条件和错误处理场景以定义其预期结果。
  7. **准确记录**：以清晰、明确的方式记录[expected result](../E/expected-result.md)，通常记录在[test case](../T/test-case.md) 本身内。
  8. **验证**：确保[expected result](../E/expected-result.md) 符合验收标准并经过同行评审。

  ```
  // Example: Test Case Expected Result Documentation
  test('User login with valid credentials', () => {
    const expected = { success: true, userId: '12345' };
    // ... test implementation ...
  });
  ```请记住，[expected result](../E/expected-result.md) 应该是**客观**、**可测试**和**可验证**。保持**简洁**和**精确**至关重要，以便于在[test execution](../T/test-execution.md)期间进行自动比较。

1. **审查要求**：彻底检查功能性和非[functional requirements](../F/functional-requirements.md) 或用户故事，以了解预期行为。
  2. **了解上下文**：考虑应用程序的上下文，包括用户期望和业务逻辑。
  3. **推导逻辑结果**：根据需求，推导给定输入或操作的逻辑结果。
  4. **与利益相关者协商**：与开发人员、业务分析师或产品所有者合作，以澄清任何歧义。
  5. **使用数据模型**：参考数据模型或模式来预测 [database](../D/database.md) 相关测试的结果。
  6. **考虑边缘情况**：确定边界条件和错误处理场景以定义其预期结果。
  7. **准确记录**：以清晰、明确的方式记录[expected result](../E/expected-result.md)，通常记录在[test case](../T/test-case.md) 本身内。
  8. **验证**：确保[expected result](../E/expected-result.md) 符合验收标准并经过同行评审。

#### 谁通常负责定义“预期结果”？

定义 **[Expected Result](../E/expected-result.md)** 的责任通常落在 **[test case](../T/test-case.md) 作者**身上，他通常是**测试分析师**或**软件测试人员**。在某些情况下，这可能还涉及与**产品所有者**、**业务分析师**或**开发人员**的协作，以确保与需求和功能保持一致。 [test case](../T/test-case.md) 作者必须清楚地了解系统的行为以及测试正在验证的特定需求或用户故事。他们利用这些知识来阐明执行测试时的正确结果应该是什么。
  在**敏捷环境**中，定义[expected results](../E/expected-result.md) 是**团队的努力**，**开发人员**、**测试人员**和**业务利益相关者**共同努力明确验收标准。这种协作方法确保每个人都对该功能的预期行为有共同的理解。
  对于**复杂系统**或需要领域专业知识时，可以咨询**主题专家（SME）**，以深入了解预期结果。这对于具有专业知识的行业（例如金融或医疗保健）尤其重要。
  在 **[automated testing](../A/automated-testing.md)** 中，[expected result](../E/expected-result.md) 必须精确且明确，因为自动化脚本使用它来断言系统响应的正确性。 [Test automation](../T/test-automation.md) 工程师负责将这些[expected results](../E/expected-result.md) 编码到[test scripts](../T/test-script.md) 中，确保它们符合[test case](../T/test-case.md) 规范。

#### 在测试过程中如何使用“预期结果”？

在测试过程中，**[Expected Result](../E/expected-result.md)** 作为验证被测软件行为的基准。它用于**自动比较**与[test execution](../T/test-execution.md) 生成的**[Actual Result](../A/actual-result.md)**。这种比较通常是通过 [test scripts](../T/test-script.md) 中的断言完成的：

  ```
  assert.equal(actualResult, expectedResult, "The actual result does not match the expected result.");
  ```如果比较结果匹配，则测试标记为**通过**；否则，将被标记为**失败**，提示进一步调查。 [Expected Result](../E/expected-result.md) 确保测试**客观**和**可重复**，为每个[test case](../T/test-case.md) 提供明确的成功标准。
  在[automated testing](../A/automated-testing.md)框架中，[Expected Result](../E/expected-result.md)通常嵌入在测试代码或外部数据源中，例如CSV文件、[databases](../D/database.md)或JSON对象，然后在[test execution](../T/test-execution.md)期间加载和使用：

  ```
  const expectedResult = loadData("expectedResult.json");
  ```以这种方式使用 [Expected Results](../E/expected-result.md) 使**持续集成**和**持续部署** (CI/CD) 管道能够自动执行测试并报告应用程序的运行状况，而无需手动干预。这种自动化对于[agile development](../A/agile-development.md) 实践至关重要，可以快速反馈并确保新功能或[bug](../B/bug.md) 修复不会引入回归。

#### 在测试过程中“预期结果”会改变吗？

如果是这样，怎么办？
  是的，**[Expected Result](../E/expected-result.md)** 可能会在测试过程中发生变化。发生这种情况的原因有多种：

- **需求变更**：如果软件需求更新或细化，则预期结果必须相应调整以符合新的期望。
  - **澄清误解**：在测试期间，可能会澄清有关功能的误解，因此需要更改预期结果以反映正确的行为。
  - **软件演化**：随着软件在其开发生命周期中的演化，可能会添加、删除或修改功能，这可能会导致预期结果发生变化。
  - **[Test Case](../T/test-case.md) 细化**：可以对测试用例进行细化以确保准确性或完整性，其中可以包括更新预期结果以确保它们的精确性和相关性。
  当 [expected result](../E/expected-result.md) 发生变化时，至关重要的是：

- **更新[Test Cases](../T/test-case.md)**：修改测试用例以反映新的预期结果。
  - **传达变更**：将变更通知所有相关利益相关者，以确保每个人都掌握最新信息。
  - **版本控制**：使用版本控制进行测试用例管理来跟踪更改并维护修改历史记录。
  - **重新执行测试**：再次运行受影响的测试用例以验证实际结果现在是否与更新的预期结果匹配。
  应谨慎处理对 [expected results](../E/expected-result.md) 的更改，以保持测试过程的完整性并确保软件满足其预期要求。

- **需求变更**：如果软件需求更新或细化，则预期结果必须相应调整以符合新的期望。
  - **澄清误解**：在测试期间，可能会澄清有关功能的误解，因此需要更改预期结果以反映正确的行为。
  - **软件演化**：随着软件在其开发生命周期中的演化，可能会添加、删除或修改功能，这可能会导致预期结果发生变化。
  - **[Test Case](../T/test-case.md) 细化**：可以对测试用例进行细化以确保准确性或完整性，其中可以包括更新预期结果以确保它们的精确性和相关性。
  - **更新[Test Cases](../T/test-case.md)**：修改测试用例以反映新的预期结果。
  - **传达变更**：将变更通知所有相关利益相关者，以确保每个人都掌握最新信息。
  - **版本控制**：使用版本控制进行测试用例管理来跟踪更改并维护修改历史记录。
  - **重新执行测试**：再次运行受影响的测试用例以验证实际结果现在是否与更新的预期结果匹配。

### 比较与分析

#### “预期结果”与“实际结果”相比如何？

在[test automation](../T/test-automation.md) 中，将**[expected result](../E/expected-result.md)** 与**[actual result](../A/actual-result.md)** 进行比较是验证[test case](../T/test-case.md) 结果的关键步骤。这种比较通常在[test script](../T/test-script.md) 内自动进行。其操作方法如下：

1. **断言**：测试框架提供断言方法来比较值，如果比较失败则抛出错误。例如，在 JavaScript 的 [Jest](../J/jest.md) 框架中：

    ```
    expect(actual).toEqual(expected);
    ```

2. **[Verification](../V/verification.md)**：某些框架提供[verification](../V/verification.md) 函数，可以在不停止[test execution](../T/test-execution.md) 的情况下记录失败的比较。
  3. **自定义比较逻辑**：对于复杂对象或非标准比较，可以实现自定义逻辑：

    ```
    if (deepCompare(actual, expected)) {
      // Pass
    } else {
      // Fail and log differences
    }
    ```

4. **视觉验证**：对于[UI testing](../U/ui-testing.md)，可以使用屏幕截图比较工具将UI的当前状态与预期图像进行比较。
  5. **[API](../A/api.md) 响应验证**：测试[APIs](../A/api.md) 时，可以将响应正文、状态代码和标头与预期值进行比较。
  6. **[Database](../D/database.md) 验证**：对于后端测试，可以查询[database](../D/database.md) 的状态并将其与预期数据集进行比较。
  7. **日志和输出**：可以捕获控制台日志、文件和其他输出并将其与预期内容进行比较。
  [test report](../T/test-report.md) 通常会突出显示不匹配的情况，从而促使进一步调查。对于自动化工程师来说，确保比较逻辑准确反映被测应用程序的预期行为至关重要。

1. **断言**：测试框架提供断言方法来比较值，如果比较失败则抛出错误。例如，在 JavaScript 的 [Jest](../J/jest.md) 框架中：

    ```
    expect(actual).toEqual(expected);
    ```

2. **[Verification](../V/verification.md)**：某些框架提供[verification](../V/verification.md) 函数，可以在不停止[test execution](../T/test-execution.md) 的情况下记录失败的比较。
  3. **自定义比较逻辑**：对于复杂对象或非标准比较，可以实现自定义逻辑：

    ```
    if (deepCompare(actual, expected)) {
      // Pass
    } else {
      // Fail and log differences
    }
    ```

4. **视觉验证**：对于[UI testing](../U/ui-testing.md)，可以使用屏幕截图比较工具将UI的当前状态与预期图像进行比较。
  5. **[API](../A/api.md) 响应验证**：测试[APIs](../A/api.md) 时，可以将响应正文、状态代码和标头与预期值进行比较。
  6. **[Database](../D/database.md) 验证**：对于后端测试，可以查询[database](../D/database.md) 的状态并将其与预期数据集进行比较。
  7. **日志和输出**：可以捕获控制台日志、文件和其他输出并将其与预期内容进行比较。

#### 使用哪些工具或技术来比较“预期结果”与“实际结果”？

为了比较 **[Expected Results](../E/expected-result.md)** 与 [test automation](../T/test-automation.md) 中的 **[Actual Results](../A/actual-result.md)**，使用了各种工具和技术：

- **断言库**：JUnit、TestNG 和 NUnit 等框架提供断言方法来验证结果。例如：

    ```
    assertEquals(expectedResult, actualResult);
    ```

- **Matchers** ：像 Hamcrest 或 AssertJ 这样的库提供流畅的 API 来实现更具表现力的断言：

    ```
    assertThat(actualResult, equalTo(expectedResult));
    ```

- **视觉比较工具**：Applitools 或 Percy 等工具捕获屏幕截图并将视觉元素与基线进行比较。
  - **[API Testing](../A/api-testing.md) 工具**：Postman 和 RestAssured 包含内置函数，可根据预期数据验证 API 响应。
  - **自定义验证函数**：有时，编写自定义逻辑来处理复杂的比较，特别是在处理非标准输出时。
  - **快照测试**：Jest 等工具拍摄输出快照，并在后续测试运行中将其与存储的快照进行比较。
  - **[BDD](../B/bdd.md) 框架**：Cucumber 和 SpecFlow 允许使用 Gherkin 语言定义预期结果，并通过步骤定义与实际结果进行匹配。
  这些工具和技术促进了结果比较的自动化，使其成为持续集成和交付管道的关键部分。它们有助于快速识别差异，确保软件按预期运行。

- **断言库**：JUnit、TestNG 和 NUnit 等框架提供断言方法来验证结果。例如：

    ```
    assertEquals(expectedResult, actualResult);
    ```

- **Matchers** ：像 Hamcrest 或 AssertJ 这样的库提供流畅的 API 来实现更具表现力的断言：

    ```
    assertThat(actualResult, equalTo(expectedResult));
    ```

- **视觉比较工具**：Applitools 或 Percy 等工具捕获屏幕截图并将视觉元素与基线进行比较。
  - **[API Testing](../A/api-testing.md) 工具**：Postman 和 RestAssured 包含内置函数，可根据预期数据验证 API 响应。
  - **自定义验证函数**：有时，编写自定义逻辑来处理复杂的比较，特别是在处理非标准输出时。
  - **快照测试**：Jest 等工具拍摄输出快照，并在后续测试运行中将其与存储的快照进行比较。
  - **[BDD](../B/bdd.md) 框架**：Cucumber 和 SpecFlow 允许使用 Gherkin 语言定义预期结果，并通过步骤定义与实际结果进行匹配。

#### 如果“预期结果”与“实际结果”不匹配，这意味着什么？

当 **[Expected Result](../E/expected-result.md)** 与 **[Actual Result](../A/actual-result.md)** 不匹配时，表示存在**差异**，该差异可能是由于各种原因造成的，例如代码中的缺陷、[test case](../T/test-case.md) 中的错误或对需求的误解。这种不匹配会触发以下操作：

1. **调查**：确定差异的原因。这涉及审查测试用例、底层代码和需求。
  2. **[Bug](../B/bug.md) 报告**：如果确认存在缺陷，请将其记录在错误跟踪系统中，并提供不匹配的详细信息和重现步骤。
  3. **沟通**​​：将问题通知相关利益相关者，例如开发人员和产品所有者，以便采取进一步行动。
  4. **解决**：开发团队解决缺陷，解决后，重新执行测试以验证修复。
  5. **[Test Case](../T/test-case.md) 审核**：如果差异是由于不正确的测试用例造成的，请更新测试用例以与正确的预期行为保持一致。
  这种不匹配是[software testing](../S/software-testing.md) 中反馈循环的关键部分，可提高质量并[verification](../V/verification.md) 软件按预期运行。系统地处理这些差异对于保持测试过程的完整性至关重要。

1. **调查**：确定差异的原因。这涉及审查测试用例、底层代码和需求。
  2. **[Bug](../B/bug.md) 报告**：如果确认存在缺陷，请将其记录在错误跟踪系统中，并提供不匹配的详细信息和重现步骤。
  3. **沟通**​​：将问题通知相关利益相关者，例如开发人员和产品所有者，以便采取进一步行动。
  4. **解决**：开发团队解决缺陷，解决后，重新执行测试以验证修复。
  5. **[Test Case](../T/test-case.md) 审核**：如果差异是由于测试用例不正确造成的，请更新测试用例以符合正确的预期行为。

#### 如何分析“预期结果”与“实际结果”之间的差异？

当 **[Expected Result](../E/expected-result.md)** 和 **[Actual Result](../A/actual-result.md)** 之间出现差异时，会通过系统方法进行分析：

1. **[Verification](../V/verification.md)** ：确认实际结果准确，并非由于测试环境问题或测试数据问题。
  2. **重现**：尝试一致地重现问题，以确保它不是侥幸。
  3. **根本原因分析**：通过检查应用程序日志、调试代码或查看可能影响功能的最新更改来调查根本原因。
  4. **影响评估**：评估差异的严重性以及对应用程序功能和用户体验的影响。
  5. **缺陷记录**：如果确认为缺陷，请将其记录在跟踪系统中，并提供详细信息，例如重现步骤、环境和屏幕截图（如果适用）。
  6. **沟通**​​：通知相关利益相关者，例如开发人员和产品所有者，确定问题的优先级并解决问题。
  7. **[Regression Testing](../R/regression-testing.md)** ：修复后，执行回归测试以确保修复不会影响应用程序的其他区域。
  8. **文档**：更新测试用例和文档以反映对功能的任何新理解或对系统所做的更改。
  在整个过程中，使用调试器、版本控制系统和缺陷跟踪软件等工具来促进分析和沟通。目标不仅是解决当前的差异，而且是完善测试策略并防止将来出现类似问题。

1. **[Verification](../V/verification.md)** ：确认实际结果准确，并非由于测试环境问题或测试数据问题。
  2. **重现**：尝试一致地重现问题，以确保它不是侥幸。
  3. **根本原因分析**：通过检查应用程序日志、调试代码或查看可能影响功能的最新更改来调查根本原因。
  4. **影响评估**：评估差异的严重性以及对应用程序功能和用户体验的影响。
  5. **缺陷记录**：如果确认为缺陷，请将其记录在跟踪系统中，并提供详细信息，例如重现步骤、环境和屏幕截图（如果适用）。
  6. **沟通**​​：通知相关利益相关者，例如开发人员和产品所有者，确定问题的优先级并解决问题。
  7. **[Regression Testing](../R/regression-testing.md)** ：修复后，执行回归测试以确保修复不会影响应用程序的其他区域。
  8. **文档**：更新测试用例和文档以反映对功能的任何新理解或对系统所做的更改。

### 最佳实践

#### 定义“预期结果”的最佳实践有哪些？

定义“[Expected Results](../E/expected-result.md)”的最佳实践包括：

- **具体**：清楚地阐明结果，避免含糊不清。使用可以测量或观察的精确值和条件。
  - **参考文档**：与需求、规范或用户故事保持一致，以确保与预期功能的一致性。
  - **考虑边缘情况**：包括边界条件和异常情况的结果，而不仅仅是[happy path](../H/happy-path.md)。
  - **正确使用数据类型**：确保 [expected result](../E/expected-result.md) 与输出的数据类型匹配（例如字符串、整数、布尔值）。
  - **包括时序约束**：如果相关，请指定结果应发生的时间，特别是对于[performance testing](../P/performance-testing.md)。
  - **State the Post-Condition**：描述执行后系统的状态，可能包括[database](../D/database.md)更新、文件生成等。
  - **使其可测试**：结果应该可以手动或通过自动化进行验证。避免主观结果。
  - **版本控制**：跟踪[expected results](../E/expected-result.md) 的更改以维护修改历史记录和基本原理。
  - **同行评审**：让另一位团队成员评审[expected results](../E/expected-result.md) 以发现错误或遗漏。
  - **自动比较**：只要有可能，请使用自动化工具来比较预期和 [actual results](../A/actual-result.md) 以减少人为错误。
  - **维护可追溯性**：将[expected results](../E/expected-result.md)链接到特定的[test cases](../T/test-case.md)以及易于参考和[impact analysis](../I/impact-analysis.md)的要求。
  - **根据需要更新**：当需求发生变化时修改[expected results](../E/expected-result.md)，确保它们保持相关性和准确性。
  通过遵守这些实践，您可以确保[expected results](../E/expected-result.md) 清晰、可靠，并保持测试过程的完整性。

- **具体**：清楚地阐明结果，避免含糊不清。使用可以测量或观察的精确值和条件。
  - **参考文档**：与需求、规范或用户故事保持一致，以确保与预期功能的一致性。
  - **考虑边缘情况**：包括边界条件和异常情况的结果，而不仅仅是[happy path](../H/happy-path.md)。
  - **正确使用数据类型**：确保 [expected result](../E/expected-result.md) 与输出的数据类型匹配（例如字符串、整数、布尔值）。
  - **包括时序约束**：如果相关，请指定结果应发生的时间，特别是对于 [performance testing](../P/performance-testing.md)。
  - **State the Post-Condition**：描述执行后系统的状态，可能包括[database](../D/database.md)更新、文件生成等。
  - **使其可测试**：结果应该可以手动或通过自动化进行验证。避免主观结果。
  - **版本控制**：跟踪[expected results](../E/expected-result.md) 的更改以维护修改历史记录和理由。
  - **同行评审**：让另一位团队成员评审[expected results](../E/expected-result.md) 以发现错误或遗漏。
  - **自动比较**：只要有可能，请使用自动化工具来比较预期和 [actual results](../A/actual-result.md) 以减少人为错误。
  - **维护可追溯性**：将[expected results](../E/expected-result.md)链接到特定的[test cases](../T/test-case.md)以及易于参考和[impact analysis](../I/impact-analysis.md)的要求。
  - **根据需要更新**：当需求发生变化时修改[expected results](../E/expected-result.md)，确保它们保持相关性和准确性。

#### 如何有效地记录“预期结果”？

有效地记录“[Expected Results](../E/expected-result.md)”需要精确和清晰。请遵循以下准则：

- **具体**：明确定义结果，不含糊。例如，指定“系统在 2 秒内将数据保存到 [database](../D/database.md)，并且用户收到‘数据保存成功’消息”，而不是“系统应保存数据”。
  - **使用验收标准**：将 [expected results](../E/expected-result.md) 与用户故事或需求的验收标准保持一致。这确保了与商定的功能的一致性。
  - $

    ```
    - Given a user submits a valid form
    - When the system processes the form
    - Then a confirmation email is sent within 5 minutes
    ```

- **包括边缘情况**：记录系统在异常或极端条件下应如何表现。这有助于覆盖整个测试范围。
  - **利用数据集**：如果适用，请提供输入数据和相应预期输出的示例。这可以在 [test case](../T/test-case.md) 中以表格格式完成。
  - $

    ```
    {
      "input": "ValidEmailAddress@example.com",
      "expectedOutput": "Email is valid"
    }
    ```

- **参考屏幕截图或模型**：处理 UI 元素时，包括视觉参考以阐明 [expected result](../E/expected-result.md)。
  - **版本控制**：维护 [expected results](../E/expected-result.md) 的更改历史记录，以跟踪一段时间内的修改。
  - **协作**：确保 [expected results](../E/expected-result.md) 得到开发人员、测试人员和利益相关者的审查和同意，以避免误解。
  - **自动化[Verification](../V/verification.md)**：如果可能，编写[expected results](../E/expected-result.md) 的[verification](../V/verification.md) 脚本以减少手动工作并提高准确性。
  - **保持最新**：定期审查和更新文档以反映系统或要求的变化。
  通过遵守这些准则，您可以确保 [expected results](../E/expected-result.md) 以对测试团队有用、清晰且可操作的方式记录。

- **具体**：明确定义结果，不含糊。例如，指定“系统在 2 秒内将数据保存到[database](../D/database.md)，并且用户收到‘数据保存成功’消息”，而不是“系统应保存数据”。
  - **使用验收标准**：将 [expected results](../E/expected-result.md) 与用户故事或需求的验收标准保持一致。这确保了与商定的功能的一致性。
  - $

    ```
    - Given a user submits a valid form
    - When the system processes the form
    - Then a confirmation email is sent within 5 minutes
    ```

- **包括边缘情况**：记录系统在异常或极端条件下应如何表现。这有助于覆盖整个测试范围。
  - **利用数据集**：如果适用，请提供输入数据和相应预期输出的示例。这可以在 [test case](../T/test-case.md) 中以表格格式完成。
  - $

    ```
    {
      "input": "ValidEmailAddress@example.com",
      "expectedOutput": "Email is valid"
    }
    ```

- **参考屏幕截图或模型**：处理 UI 元素时，包括视觉参考以阐明 [expected result](../E/expected-result.md)。
  - **版本控制**：维护 [expected results](../E/expected-result.md) 的更改历史记录，以跟踪一段时间内的修改。
  - **协作**：确保 [expected results](../E/expected-result.md) 得到开发人员、测试人员和利益相关者的审查和同意，以避免误解。
  - **自动化[Verification](../V/verification.md)**：如果可能，编写[expected results](../E/expected-result.md) 的[verification](../V/verification.md) 脚本以减少手动工作并提高准确性。
  - **保持最新**：定期审查和更新文档以反映系统或要求的变化。

#### 定义“预期结果”时要避免哪些常见错误？

在 [test automation](../T/test-automation.md) 中定义“[Expected Results](../E/expected-result.md)”时，请避免以下常见错误：

- **模糊性**：确保结果具体且可衡量。歧义可能导致误解和无效的测试。
  - **假设**：在没有适当的文档或理解的情况下，不要假设系统行为。预期结果基于明确的要求或设计规范。
  - **静态定义**：随着新信息的出现或需求的发展，对改进预期结果持开放态度。
  - **俯瞰上下文**：考虑测试环境和先决条件。不同配置的结果可能有所不同。
  - **忽略边缘情况**：包括边界条件和特殊场景的结果，以确保全面覆盖。
  - **不考虑用户视角**：将预期结果与用户需求和体验结合起来，而不仅仅是技术正确性。
  - **缺乏细节**：提供足够的细节以实现精确验证而不会产生歧义。
  - **协作失败**：与开发人员、业务分析师和其他利益相关者合作，以确保预期结果的准确性和相关性。
  - **忽略数据变异性**：考虑可能影响结果的不同数据集。如果适用，请使用数据驱动的测试。
  - **忘记非功能方面**：记住定义性能、安全性和可用性测试的预期结果，而不仅仅是功能行为。
  通过避免这些陷阱，您可以确保“[Expected Results](../E/expected-result.md)”对于验证 [automated testing](../A/automated-testing.md) 期间的软件行为清晰、准确且有用。

- **模糊性**：确保结果具体且可衡量。歧义可能导致误解和无效的测试。
  - **假设**：在没有适当的文档或理解的情况下，不要假设系统行为。预期结果基于明确的要求或设计规范。
  - **静态定义**：随着新信息的出现或需求的发展，对改进预期结果持开放态度。
  - **俯瞰上下文**：考虑测试环境和先决条件。不同配置的结果可能有所不同。
  - **忽略边缘情况**：包括边界条件和特殊场景的结果，以确保全面覆盖。
  - **不考虑用户视角**：将预期结果与用户需求和体验结合起来，而不仅仅是技术正确性。
  - **缺乏细节**：提供足够的细节以实现精确验证而不会产生歧义。
  - **协作失败**：与开发人员、业务分析师和其他利益相关者合作，以确保预期结果的准确性和相关性。
  - **忽略数据变异性**：考虑可能影响结果的不同数据集。如果适用，请使用数据驱动的测试。
  - **忘记非功能方面**：记住定义性能、安全性和可用性测试的预期结果，而不仅仅是功能行为。

#### 如何将“预期结果”有效地传达给测试团队？

可以通过多种方法向测试团队有效传达“[Expected Results](../E/expected-result.md)”：

- **使用清晰简洁的语言**来描述预期结果，避免歧义。
  - **利用结构化格式**，例如用户故事或验收标准，提供上下文和清晰度。

    ```
    Given: <Initial Condition>
    When: <Action Performed>
    Then: <Expected Result>
    ```

- **结合视觉辅助工具**，例如流程图、图表或屏幕截图来说明复杂的场景。
  - **利用[test management](../T/test-management.md) 工具**，支持在团队成员之间追踪和共享[expected results](../E/expected-result.md)。
  - **为[test cases](../T/test-case.md) 实施版本控制**，以跟踪[expected results](../E/expected-result.md) 随时间的变化。
  - **在 [test scripts](../T/test-script.md) 中使用自动断言**，明确说明 [expected result](../E/expected-result.md)。

    ```
    expect(actualResult).toEqual(expectedResult);
    ```

- **与开发人员、业务分析师和其他利益相关者进行评审会议**，以确保达成共识。
  - **提供示例**和边缘案例以涵盖一系列可能的结果。
  - **提供培训课程**，了解如何在被测应用程序的上下文中解释和应用 [expected results](../E/expected-result.md)。
  通过采用这些做法，您可以确保有效地传达[expected results](../E/expected-result.md)，从而实现更准确、更高效的[test automation](../T/test-automation.md) 工作。

- **使用清晰简洁的语言**来描述预期结果，避免歧义。
  - **利用结构化格式**，例如用户故事或验收标准，提供上下文和清晰度。

    ```
    Given: <Initial Condition>
    When: <Action Performed>
    Then: <Expected Result>
    ```

- **结合视觉辅助工具**，例如流程图、图表或屏幕截图来说明复杂的场景。
  - **利用[test management](../T/test-management.md) 工具**，支持在团队成员之间追踪和共享[expected results](../E/expected-result.md)。
  - **为[test cases](../T/test-case.md) 实施版本控制**，以跟踪[expected results](../E/expected-result.md) 随时间的变化。
  - **在 [test scripts](../T/test-script.md) 中使用自动断言**，明确说明 [expected result](../E/expected-result.md)。

    ```
    expect(actualResult).toEqual(expectedResult);
    ```

- **与开发人员、业务分析师和其他利益相关者进行评审会议**，以确保达成共识。
  - **提供示例**和边缘案例以涵盖一系列可能的结果。
  - **提供培训课程**，了解如何在被测应用程序的上下文中解释和应用 [expected results](../E/expected-result.md)。
