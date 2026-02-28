# 错误猜测

<!-- TOC START -->
- [相关术语：](#相关术语：)
  - [另请参阅：](#另请参阅：)
- [关于错误猜测的问题？](#关于错误猜测的问题？)
  - [基础知识和重要性](#基础知识和重要性)
    - [软件测试中的错误猜测是什么？](#软件测试中的错误猜测是什么？)
    - [为什么错误猜测被认为是软件测试中的一项重要技术？](#为什么错误猜测被认为是软件测试中的一项重要技术？)
    - [错误猜测和其他测试技术有什么区别？](#错误猜测和其他测试技术有什么区别？)
    - [错误猜测的优点和缺点是什么？](#错误猜测的优点和缺点是什么？)
  - [技术和策略](#技术和策略)
    - [错误猜测中常用的策略有哪些？](#错误猜测中常用的策略有哪些？)
    - [测试人员如何培养错误猜测能力？](#测试人员如何培养错误猜测能力？)
    - [经验在错误猜测中起什么作用？](#经验在错误猜测中起什么作用？)
    - [错误猜测如何与其他测试技术结合起来？](#错误猜测如何与其他测试技术结合起来？)
  - [实际应用](#实际应用)
    - [您能否提供错误猜测特别有用的情况示例？](#您能否提供错误猜测特别有用的情况示例？)
    - [错误猜测如何应用于自动化测试？](#错误猜测如何应用于自动化测试？)
    - [通常使用错误猜测来识别哪些类型的错误？](#通常使用错误猜测来识别哪些类型的错误？)
    - [如何衡量错误猜测的有效性？](#如何衡量错误猜测的有效性？)
<!-- TOC END -->

错误猜测

是一个

软件测试

测试人员依靠他们的经验、直觉和系统知识尝试预测缺陷可能出现的位置的技术。而不是遵循系统的测试方法或预定义的

测试用例

，测试人员进行有根据的猜测，以确定软件可能出现故障的潜在问题区域或场景。该技术基于测试人员对常见错误、过去缺陷或特定系统行为的熟悉程度。

错误猜测

通常用作补充测试方法，补充更结构化的技术，并且在识别独特或意外问题方面特别有效。

## 相关术语：

- [Heuristic Testing](../H/heuristic-testing.md)

### 另请参阅：

- [Wikipedia](https://en.wikipedia.org/wiki/Error_guessing)

## 关于错误猜测的问题？

### 基础知识和重要性

#### 软件测试中的错误猜测是什么？

[Error guessing](../E/error-guessing.md) 是一种 **[test case](../T/test-case.md) 设计技术**，测试人员可以利用他们的直觉、经验和对系统的理解来预测 [bugs](../B/bug.md) 可能发生的位置，而不需要遵循任何正式的方法。测试人员利用他们对常见陷阱和特定系统怪癖的了解来识别潜在的错误情况。
  在实践中，[error guessing](../E/error-guessing.md) 涉及根据类似应用程序的**预感**或**过去的经验**创建测试。测试人员可能会考虑边界条件、无效输入和可能导致错误的复杂用户场景等因素。
  为了增强[error guessing](../E/error-guessing.md)，测试人员可以保留通用[bugs](../B/bug.md)**的**存储库，并使用从历史缺陷数据派生的**清单**。定期回顾过去的缺陷并从中学习可以增强测试人员的直觉。
  In [automated testing](../A/automated-testing.md), [error guessing](../E/error-guessing.md) can inform the creation of **[test scripts](../T/test-script.md)** that target likely failure points.例如，如果测试人员怀疑表单可能无法正确处理特殊字符，他们可能会编写一个自动测试，将这些字符输入到表单字段中。
  虽然[error guessing](../E/error-guessing.md) 的结构不如其他技术，但它可以**互补**。它通常会填补更正式方法留下的空白，提供一个安全网来捕获否则可能会被遗漏的问题。
  为了衡量其有效性，与其他方法相比，团队可以通过 [error guessing](../E/error-guessing.md) 跟踪**发现的缺陷数量**。如果[error guessing](../E/error-guessing.md) 始终如一地发现重大问题，则它验证了该技术在测试策略中的价值。

#### 为什么错误猜测被认为是软件测试中的一项重要技术？

[Error guessing](../E/error-guessing.md) 在[software testing](../S/software-testing.md) 中至关重要，因为它利用**测试人员的直觉和经验**来预测和模拟正式测试技术可能无法涵盖的非常规或边缘情况场景。它充当**系统方法的补充**，填补结构化方法可能遗漏的空白。测试人员运用他们对常见故障的理解和领域知识来假设潜在的错误情况。
  这项技术特别有价值，因为它可以**识别独特且意外的[bugs](../B/bug.md)**。虽然结构化测试基于规范和预定义的标准，但 [error guessing](../E/error-guessing.md) 是动​​态的，可以适应对应用程序及其环境不断发展的理解。
  将[error guessing](../E/error-guessing.md) 合并到[test automation](../T/test-automation.md) 涉及根据**测试人员对潜在错误的假设**创建脚本。这些脚本可以与常规自动化测试一起运行，以发现可能漏掉的问题。
  为了提高[error guessing](../E/error-guessing.md) 的有效性，测试人员应该**不断地从过去的缺陷中学习**，及时了解类似应用程序中的常见问题，并与同行分享知识。缺陷检测率等指标可以帮助衡量其影响。
  总之，[error guessing](../E/error-guessing.md) 是一项**重要的技术**，它为测试过程添加了一层人类洞察力，使其更加强大和全面。当与其他测试方法结合使用时，它是最有效的，可确保彻底探索应用程序的潜在弱点。

#### 错误猜测和其他测试技术有什么区别？

[Error guessing](../E/error-guessing.md) differs from other testing techniques primarily in its **lack of formal structure** and reliance on the tester's intuition and experience. While methods like **boundary value analysis** or **[equivalence partitioning](../E/equivalence-partitioning.md)** are systematic and based on specific rules or models, [error guessing](../E/error-guessing.md) is more **ad-hoc** and **heuristic-based**.它不遵循一组预定义的[test cases](../T/test-case.md)，而是依赖于测试人员预测可能的错误源的能力。
  其他技术通常需要详细的文档，并且可以**轻松地实现自动化**或**外包**。 In contrast, [error guessing](../E/error-guessing.md) is highly **subjective** and **personal**, making it harder to automate or transfer between testers without loss of effectiveness.
  **基于模型的测试**等正式方法根据正式规范生成[test cases](../T/test-case.md)，确保覆盖所有定义的场景。 [Error guessing](../E/error-guessing.md), however, targets areas that might be overlooked by formal methods, often based on past experiences with similar applications or common failure patterns.
  While structured methods can be more **comprehensive** and **repeatable**, [error guessing](../E/error-guessing.md) can quickly identify critical issues without the need for extensive preparation.它通常用作**补充方法**，填补更系统的技术留下的空白。
  In summary, [error guessing](../E/error-guessing.md) is a **flexible**, **experience-driven** approach that contrasts with the **rigorous**, **rule-based** nature of other testing techniques.它对于识别更正式的方法可能无法捕获的异常或被忽视的错误特别有用。

#### 错误猜测的优点和缺点是什么？

[Error Guessing](../E/error-guessing.md) 的优点：

- **直观**：利用测试人员的直觉和经验来识别潜在的弱点。
  - **灵活**：适应不同的环境和应用，无需正式程序。
  - **高效**：快速定位可能失败的区域，节省测试过程的时间。
  - **补充**：通过解决预定义测试可能遗漏的情况来增强结构化测试方法。
  [Error Guessing](../E/error-guessing.md) 的缺点：

- **主观**：严重依赖个人技能和经验，导致结果存在差异。
  - **不可重现**：缺乏正式的方法，使得难以在团队之间复制测试或共享技术。
  - **不完整**：可能无法涵盖所有​​可能的错误场景，尤其是在复杂的系统中。
  - **不可预测**：有效性难以衡量，如果忽视关键错误，可能会导致错误的安全感。
  - **直观**：利用测试人员的直觉和经验来识别潜在的弱点。
  - **灵活**：适应不同的环境和应用，无需正式程序。
  - **高效**：快速定位可能失败的区域，节省测试过程的时间。
  - **补充**：通过解决预定义测试可能遗漏的情况来增强结构化测试方法。
  - **主观**：严重依赖个人技能和经验，导致结果存在差异。
  - **不可重现**：缺乏正式的方法，使得难以在团队之间复制测试或共享技术。
  - **不完整**：可能无法涵盖所有​​可能的错误场景，尤其是在复杂的系统中。
  - **不可预测**：有效性难以衡量，如果忽视关键错误，可能会导致错误的安全感。

### 技术和策略

#### 错误猜测中常用的策略有哪些？

[Error guessing](../E/error-guessing.md) 策略通常取决于测试人员的直觉和经验。常见策略包括：

- **边界值分析**：猜测输入范围边缘的错误。
  - **[Stress Testing](../S/stress-testing.md)** ：预测高负载或极端条件下的故障。
  - **无效输入**：尝试超出有效范围或格式的输入。
  - **资源耗尽**：当系统资源不足或耗尽时猜测错误。
  - **状态转换错误**：预测系统从一种状态转移到另一种状态时的故障。
  - **与外部系统的交互**：猜测与数据库、API 或其他服务交互期间可能发生的错误。
  - **并发问题**：寻找多线程应用程序中的竞争条件和死锁。
  - **用户行为**：模拟异常或意外的用户操作。
  通过编写反映这些猜测的脚本，将这些策略合并到自动化测试中。例如：

  ```
  // Boundary Value Analysis Example
  test('should handle maximum input length', () => {
    const input = 'a'.repeat(MAX_INPUT_LENGTH);
    expect(() => processInput(input)).not.toThrow();
  });
  ```要衡量有效性，请对照其他方法发现的缺陷数量跟踪使用 [error guessing](../E/error-guessing.md) 发现的缺陷数量。根据缺陷趋势和过去的经验调整策略。请记住，[error guessing](../E/error-guessing.md) 是对系统技术的补充，应用作平衡测试方法的一部分。

- **边界值分析**：猜测输入范围边缘的错误。
  - **[Stress Testing](../S/stress-testing.md)** ：预测高负载或极端条件下的故障。
  - **无效输入**：尝试超出有效范围或格式的输入。
  - **资源耗尽**：当系统资源不足或耗尽时猜测错误。
  - **状态转换错误**：预测系统从一种状态转移到另一种状态时的故障。
  - **与外部系统的交互**：猜测与数据库、API 或其他服务交互期间可能发生的错误。
  - **并发问题**：寻找多线程应用程序中的竞争条件和死锁。
  - **用户行为**：模拟异常或意外的用户操作。

#### 测试人员如何培养错误猜测能力？

为了培养 [error guessing](../E/error-guessing.md) 技能，测试人员应该：

- **定期练习**：参与不同的测试场景，遇到各种错误。
  - **从过去的缺陷中学习**：分析历史错误数据以识别模式和常见故障点。
  - **研究应用程序领域**：深入了解软件领域，以预测复杂的用户行为和潜在错误。
  - **与他人合作**：与同行分享知识，从他们的见解和经验中学习。
  - **使用检查表**：根据已知的错误类型创建和完善检查表，以系统地猜测潜在的错误。
  - **保持更新**：及时了解新技术、工具和测试方法，以预测现代错误类型。
  - **像最终用户一样思考**：采用用户的视角来发现实际使用中可能发生的错误。
  - **实验**：尝试非常规的测试用例和场景，以发现不太明显的错误。
  - **查看代码更改**：了解最近对目标区域进行的代码修改可能会引入新的错误。
  通过磨练这些技能，测试人员可以提高他们的直觉并更加精通[error guessing](../E/error-guessing.md)，从而使[test automation](../T/test-automation.md)更加有效和高效。

- **定期练习**：参与不同的测试场景，遇到各种错误。
  - **从过去的缺陷中学习**：分析历史错误数据以识别模式和常见故障点。
  - **研究应用程序领域**：深入了解软件领域，以预测复杂的用户行为和潜在错误。
  - **与他人合作**：与同行分享知识，从他们的见解和经验中学习。
  - **使用检查表**：根据已知的错误类型创建和完善检查表，以系统地猜测潜在的错误。
  - **保持更新**：及时了解新技术、工具和测试方法，以预测现代错误类型。
  - **像最终用户一样思考**：采用用户的视角来发现实际使用中可能发生的错误。
  - **实验**：尝试非常规的测试用例和场景，以发现不太明显的错误。
  - **查看代码更改**：了解最近对目标区域进行的代码修改可能会引入新的错误。

#### 经验在错误猜测中起什么作用？

经验在 **[error guessing](../E/error-guessing.md)** 中起着至关重要的作用，因为它在很大程度上依赖于测试人员的直觉和知识来预测可能出现缺陷的位置。经验丰富的测试人员根据对常见故障模式、过去的[bugs](../B/bug.md)、系统行为和领域知识的理解，对潜在错误做出有根据的猜测。
  凭借经验，测试人员会对代码和系统异常产生“直觉”。他们通常可以根据以前遇到的类似问题来预测边界条件、数据流、复杂算法和集成等领域的错误。
  此外，经验丰富的测试人员善于识别“微妙的线索”，这些线索可能表明更深层次的问题，例如不一致的行为或性能问题，而这些问题对于经验不足的测试人员来说可能不会立即显现出来。
  为了提高[error guessing](../E/error-guessing.md) 的有效性，测试人员应该不断**反思过去的测试经验**，分析缺陷，并及时了解类似应用程序或技术中报告的常见问题。这种回顾性分析有助于构建潜在问题领域的“心理存储库”，可应用于未来的测试场景。
  总之，经验在[error guessing](../E/error-guessing.md)中的作用是利用过去的见解和知识来**预测和识别更正式的测试技术可能无法捕获的错误**。它通过添加一层**人类判断**和**启发式分析**来识别潜在缺陷，从而丰富了测试过程。

#### 错误猜测如何与其他测试技术结合起来？

[Error guessing](../E/error-guessing.md)可以与其他测试技术有效结合，以增强整体测试过程。方法如下：

- **边界值分析 (BVA)**：使用错误猜测来识别潜在的相差一错误和 BVA 未涵盖的其他边缘情况。
  - **[Equivalence Partitioning](../E/equivalence-partitioning.md)** ：对输入数据进行分区后，应用错误猜测来假设每个分区中的错误，尤其是那些看起来更容易出现问题的错误。
  - **[Decision Table Testing](../D/decision-table-testing.md)** ：结合错误猜测来探索决策表中未表示的条件和操作。
  - **[State Transition Testing](../S/state-transition-testing.md)** ：使用错误猜测来预测状态机中的非法状态转换或意外行为。
  - **[Exploratory Testing](../E/exploratory-testing.md)** ：在执行探索性测试时，利用错误猜测将探索引导至疑似高风险的区域。
  - **自动化[Regression Testing](../R/regression-testing.md)**：将错误猜测集成为附加测试用例，以捕获已知脆弱区域的回归。
  在[automated testing](../A/automated-testing.md)中，错误猜测可以转换为特定的[test cases](../T/test-case.md)或断言。例如：

  ```
  // Hypothetical error guess: Negative quantity leads to incorrect inventory count
  test('Inventory count should not decrease on negative quantity input', () => {
    const initialCount = getInventoryCount();
    addInventory(-5);
    expect(getInventoryCount()).toEqual(initialCount);
  });
  ```要衡量 [error guessing](../E/error-guessing.md) 的有效性，请跟踪使用此技术发现的缺陷数量与发现的缺陷总数。此外，分析[severity](../S/severity.md) 和[error guessing](../E/error-guessing.md) 捕获的缺陷的影响，以评估其在测试策略中的价值。

- **边界值分析 (BVA)**：使用错误猜测来识别潜在的相差一错误和 BVA 未涵盖的其他边缘情况。
  - **[Equivalence Partitioning](../E/equivalence-partitioning.md)** ：对输入数据进行分区后，应用错误猜测来假设每个分区中的错误，尤其是那些看起来更容易出现问题的错误。
  - **[Decision Table Testing](../D/decision-table-testing.md)** ：结合错误猜测来探索决策表中未表示的条件和操作。
  - **[State Transition Testing](../S/state-transition-testing.md)** ：使用错误猜测来预测状态机中的非法状态转换或意外行为。
  - **[Exploratory Testing](../E/exploratory-testing.md)** ：在执行探索性测试时，利用错误猜测将探索引导至疑似高风险的区域。
  - **自动化[Regression Testing](../R/regression-testing.md)**：将错误猜测集成为附加测试用例，以捕获已知脆弱区域的回归。

### 实际应用

#### 您能否提供错误猜测特别有用的情况示例？

[Error guessing](../E/error-guessing.md) 在以下情况下特别有用：

- **复杂的用户输入**
    是预期的，例如自由格式的文本字段，其中输入模式是不可预测的，并可能导致意外的行为。

- **边界条件**
    没有明确定义，测试人员必须依靠直觉来识别潜在的边缘情况。

- **历史数据**
    表示某些区域频繁出现问题，表明这些或相关组件中可能会再次出现类似的问题。

- **间歇性问题**
    被报告，这可能很难系统地重现，但可以根据测试人员对可能导致问题的原因的预感来触发。

- **第三方集成**
    涉及，并且测试人员必须预测外部系统不可预测的行为可能引起的问题。

- **新功能**
    引入时没有详细的要求，测试人员必须根据自己的经验来猜测哪里可能会出现错误。

- **旧系统**
    被更新或修改，并且缺乏全面的文档或对系统复杂性的理解。
  在这些情况下，[error guessing](../E/error-guessing.md) 可以指导创建针对不太明显的故障点的[test cases](../T/test-case.md)，从而补充更结构化的测试方法。这是一种利用测试人员的直觉和经验来预见和测试通过正式测试策略可能不会立即显现出来的潜在错误的技术。

- **复杂的用户输入**
    是预期的，例如自由格式的文本字段，其中输入模式是不可预测的，并可能导致意外的行为。

- **边界条件**
    没有明确定义，测试人员必须依靠直觉来识别潜在的边缘情况。

- **历史数据**
    表示某些区域频繁出现问题，表明这些或相关组件中可能会再次出现类似的问题。

- **间歇性问题**
    被报告，这可能很难系统地重现，但可以根据测试人员对可能导致问题的原因的预感来触发。

- **第三方集成**
    涉及，并且测试人员必须预测外部系统不可预测的行为可能引起的问题。

- **新功能**
    引入时没有详细的要求，测试人员必须根据自己的经验来猜测哪里可能会出现错误。

- **旧系统**
    被更新或修改，并且缺乏全面的文档或对系统复杂性的理解。

#### 错误猜测如何应用于自动化测试？

通过将**基于启发式的检查**合并到[test scripts](../T/test-script.md)中，[Error guessing](../E/error-guessing.md)可以有效地应用在[automated testing](../A/automated-testing.md)中。经验丰富的测试人员可以利用直觉来预测潜在的错误情况，然后编写自动化测试来验证这些场景。
  例如，如果测试人员怀疑应用程序可能无法正确处理意外的文件格式，他们可以编写一个自动化测试，尝试上传各种不正确的文件格式并断言应用程序会适当响应。

  ```
  describe('File Upload Error Handling', () => {
    const invalidFormats = ['invalidimage.bmp', 'randomtext.txt', 'corruptedfile.jpg'];
    invalidFormats.forEach((format) => {
      it(`should reject the ${format} file format`, () => {
        const response = uploadFile(format);
        expect(response).to.have.status(400);
        expect(response).to.have.error('Unsupported file format');
      });
    });
  });
  ```使用基于属性的测试框架等工具，可以**随机**基于[error guessing](../E/error-guessing.md) 的自动化测试，以覆盖更广泛的输入或场景。这种方法可以发现通过正式[test case](../T/test-case.md) 设计不容易预见到的错误。
  为了最大限度地提高有效性，[error guessing](../E/error-guessing.md) 应根据自动化测试结果的反馈**不断完善**。随着系统的发展和新见解的获得，自动化测试应该更新以反映对潜在错误条件的最新理解。
  将[error guessing](../E/error-guessing.md) 合并到[automated testing](../A/automated-testing.md) 需要在**探索性洞察力**和**系统执行**之间取得平衡，利用自动化的速度和可重复性，同时利用测试人员的经验和直觉。

#### 通常使用错误猜测来识别哪些类型的错误？

[Error guessing](../E/error-guessing.md) 通常可以识别正式测试方法不易捕获的错误。这些包括：

- **与边界相关的错误**：猜测等价划分或边界值分析可能无法覆盖的输入范围最末端的值。
  - **用户行为错误**：预测用户可能犯的错误，例如输入不正确的数据类型或可能导致系统失败的操作序列。
  - **并发问题**：识别多个进程访问共享资源时可能发生的竞争条件和死锁。
  - **资源耗尽**：猜测系统可能耗尽内存、磁盘空间或其他资源的情况。
  - **错误处理路径**：识别系统遇到错误情况时出现的未经测试的路径。
  - **集成错误**：猜测组件如何无法正确交互，特别是当它们之前没有集成过时。
  - **安全漏洞**：预测攻击者可能利用系统的方式，例如 SQL 注入或缓冲区溢出。
  经验丰富的测试人员利用他们对系统、系统环境和潜在用户行为的了解，对这些类型的错误可能发生的位置做出有根据的猜测。虽然[error guessing](../E/error-guessing.md) 不如其他测试技术系统化，但它可以发现可能会被遗漏的问题。

- **与边界相关的错误**：猜测等价划分或边界值分析可能无法覆盖的输入范围最末端的值。
  - **用户行为错误**：预测用户可能犯的错误，例如输入不正确的数据类型或可能导致系统失败的操作序列。
  - **并发问题**：识别多个进程访问共享资源时可能发生的竞争条件和死锁。
  - **资源耗尽**：猜测系统可能耗尽内存、磁盘空间或其他资源的情况。
  - **错误处理路径**：识别系统遇到错误情况时出现的未经测试的路径。
  - **集成错误**：猜测组件如何无法正确交互，特别是当它们之前没有集成过时。
  - **安全漏洞**：预测攻击者可能利用系统的方式，例如 SQL 注入或缓冲区溢出。

#### 如何衡量错误猜测的有效性？

由于其主观性，衡量 **[error guessing](../E/error-guessing.md)** 的有效性可能具有挑战性。但是，您可以通过几个指标来衡量其成功：

- **缺陷检测率 (DDR)**：将通过 [error guessing](../E/error-guessing.md) 发现的缺陷数量与发现的缺陷总数进行比较。比率越高表明效率越高。

    ```
    DDR = (Defects found by error guessing / Total defects found) * 100
    ```

- **缺陷检测效率 (DDE)**：与其他方法相比，评估 [error guessing](../E/error-guessing.md) 识别缺陷的速度。更快的检测可以表明更高的效率。

    ```
    DDE = (Defects found by error guessing / Time spent on error guessing)
    ```

- **[Severity](../S/severity.md) 缺陷**：评估[error guessing](../E/error-guessing.md) 捕获的缺陷的[severity](../S/severity.md)。发现关键缺陷可以体现该技术的价值。
  - **[Test Coverage](../T/test-coverage.md)**：分析[error guessing](../E/error-guessing.md)是否会导致识别现有[test cases](../T/test-case.md)未覆盖的区域。
  - **来自回顾的反馈**：从团队回顾中收集有关 [error guessing](../E/error-guessing.md) 对测试过程的影响的定性数据。
  - **历史比较**：将当前项目指标与未使用 [error guessing](../E/error-guessing.md) 的过去项目进行比较。
  为了确保更客观的评估，请将这些指标与其他测试技术的数据结合起来。此方法有助于了解[error guessing](../E/error-guessing.md) 对[test strategy](../T/test-strategy.md) 的总体贡献。请记住，我们的目标是通过 [error guessing](../E/error-guessing.md) 见解来补充而不是取代系统测试方法。

- **缺陷检测率 (DDR)**：将通过 [error guessing](../E/error-guessing.md) 发现的缺陷数量与发现的缺陷总数进行比较。比率越高表明效率越高。

    ```
    DDR = (Defects found by error guessing / Total defects found) * 100
    ```

- **缺陷检测效率 (DDE)**：与其他方法相比，评估 [error guessing](../E/error-guessing.md) 识别缺陷的速度。更快的检测可以表明更高的效率。

    ```
    DDE = (Defects found by error guessing / Time spent on error guessing)
    ```

- **[Severity](../S/severity.md) 缺陷**：评估[error guessing](../E/error-guessing.md) 捕获的缺陷的[severity](../S/severity.md)。发现关键缺陷可以体现该技术的价值。
  - **[Test Coverage](../T/test-coverage.md)**：分析[error guessing](../E/error-guessing.md)是否会导致识别现有[test cases](../T/test-case.md)未覆盖的区域。
  - **来自回顾的反馈**：从团队回顾中收集有关 [error guessing](../E/error-guessing.md) 对测试过程的影响的定性数据。
  - **历史比较**：将当前项目指标与未使用 [error guessing](../E/error-guessing.md) 的过去项目进行比较。
