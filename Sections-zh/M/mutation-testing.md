# 突变测试

<!-- TOC START -->
- [关于突变测试的问题吗？](#关于突变测试的问题吗？)
  - [基础知识和重要性](#基础知识和重要性)
    - [软件测试中的突变测试是什么？](#软件测试中的突变测试是什么？)
    - [为什么突变测试很重要？](#为什么突变测试很重要？)
    - [突变测试与其他类型的测试有何不同？](#突变测试与其他类型的测试有何不同？)
    - [突变测试有什么好处？](#突变测试有什么好处？)
    - [突变测试有哪些局限性？](#突变测试有哪些局限性？)
  - [概念和技术](#概念和技术)
    - [突变测试的关键概念是什么？](#突变测试的关键概念是什么？)
    - [突变测试中的突变体是什么？](#突变测试中的突变体是什么？)
    - [什么是突变分数以及它是如何计算的？](#什么是突变分数以及它是如何计算的？)
    - [变异算子有哪些不同类型？](#变异算子有哪些不同类型？)
    - [使用哪些技术来降低突变测试的成本？](#使用哪些技术来降低突变测试的成本？)
  - [实施和工具](#实施和工具)
    - [执行突变测试涉及哪些步骤？](#执行突变测试涉及哪些步骤？)
    - [有哪些工具可用于突变测试？](#有哪些工具可用于突变测试？)
    - [如何在持续集成环境中实现变异测试？](#如何在持续集成环境中实现变异测试？)
    - [实施突变测试的最佳实践有哪些？](#实施突变测试的最佳实践有哪些？)
    - [如何解读突变检测结果？](#如何解读突变检测结果？)
  - [高级主题](#高级主题)
    - [什么是高阶突变测试？](#什么是高阶突变测试？)
    - [突变测试如何帮助测试套件改进？](#突变测试如何帮助测试套件改进？)
    - [突变测试在测试用例生成中的作用是什么？](#突变测试在测试用例生成中的作用是什么？)
    - [扩展大型代码库的突变测试有哪些挑战？](#扩展大型代码库的突变测试有哪些挑战？)
    - [突变测试的最新进展是什么？](#突变测试的最新进展是什么？)
<!-- TOC END -->

突变测试

评估软件测试的质量。它涉及对程序进行轻微修改并检查现有测试是否可以检测到这些更改。

## 关于突变测试的问题吗？

### 基础知识和重要性

#### 软件测试中的突变测试是什么？

[Mutation testing](../M/mutation-testing.md) 是一种通过向程序源代码引入微小更改或突变并检查现有[test suite](../T/test-suite.md) 是否可以检测到这些修改来评估软件测试质量的技术。前提是，当使用 [bugs](../B/bug.md) 故意更改代码时，健壮的 [test suite](../T/test-suite.md) 应该会失败。突变体是代码的修改版本，每个版本都针对原始[test suite](../T/test-suite.md)进行测试。如果测试失败，突变体就会被杀死；如果所有测试都通过，突变体就会存活，表明存在潜在的[test suite](../T/test-suite.md)缺陷。
  [Mutation testing](../M/mutation-testing.md) 在细粒度级别上运行，通常会修改单行代码甚至单个运算符。此方法提供了对[test suite](../T/test-suite.md) 在捕获错误方面的有效性的详细了解。突变分数，即被杀死的突变体与突变体总数的比率，可作为 [test suite](../T/test-suite.md) 强度的定量测量。
  虽然[mutation testing](../M/mutation-testing.md) 可以显着提高[test suite](../T/test-suite.md) 质量，但它的计算成本很高并且可能非常耗时。为了缓解这种情况，采用选择性突变、并行执行和突变图式等各种策略来减少突变体的数量或优化测试过程。
  [Mutation testing](../M/mutation-testing.md) 对于确保 [test cases](../T/test-case.md) 的彻底性和指导其他测试的开发特别有用。它通过提供关于测试有效性的不同视角来补充其他测试方法，重点关注测试检测小型系统故障的能力，否则这些故障可能会被忽视。

#### 为什么突变测试很重要？

[Mutation testing](../M/mutation-testing.md) 至关重要，因为它提供了对[test suite](../T/test-suite.md) 有效性的**深入而严格的评估**。通过向代码库引入小的更改或“突变”并检查 [test suite](../T/test-suite.md) 是否检测到这些更改，[mutation testing](../M/mutation-testing.md) 暴露了 [test coverage](../T/test-coverage.md) 中其他测试方法可能会错过的弱点。它有效地**衡量测试本身的质量**，而不仅仅是测试所覆盖的代码数量。
  这种形式的测试将[test suite](../T/test-suite.md)推向极限，确保测试不仅通过，而且对潜在缺陷敏感。它有助于制作**高质量的[test cases](../T/test-case.md)**，它们对代码更改具有鲁棒性，并且可以捕获意外行为。 [Mutation testing](../M/mutation-testing.md) 的重要性在于它能够**验证[test suite](../T/test-suite.md) 的故障检测能力**，使其成为维护和提高软件系统可靠性的强大工具。
  此外，[mutation testing](../M/mutation-testing.md) 可以通过突出显示未测试或根本未测试的代码区域来指导开发人员**提高测试有效性**。这种反馈循环对于测试开发过程中的**持续改进**至关重要，从而产生更易于维护和防错的软件。
  本质上，[mutation testing](../M/mutation-testing.md) 不仅仅是寻找[bugs](../B/bug.md)；这是关于**评估和提高发现[bugs](../B/bug.md) 的测试的质量**，这是交付强大软件的关键方面。

#### 突变测试与其他类型的测试有何不同？

[Mutation testing](../M/mutation-testing.md) 与其他类型的测试不同，它通过显式地向程序源代码引入更改或**突变**来评估[test cases](../T/test-case.md) 的有效性。与关注[test cases](../T/test-case.md) 是否能够检测到现有故障的传统测试方法不同，[mutation testing](../M/mutation-testing.md) 旨在评估[test suite](../T/test-suite.md) 识别新的人为故障的能力。
  例如，在 **[unit testing](../U/unit-testing.md)** 中，目标是验证源代码的各个单元是否按预期工作。 **[Integration testing](../I/integration-testing.md)** 检查不同的模块或服务是否正确协同工作。 **[System testing](../S/system-testing.md)** 根据需求查看整个系统的行为，而 **[acceptance testing](../A/acceptance-testing.md)** 验证端到端业务流程。
  另一方面，[Mutation testing](../M/mutation-testing.md) 采用了不同的方法。它通过引入小的变化来系统地改变代码，创建程序的许多版本，每个版本都有一个错误。然后针对这些变异版本运行[test suite](../T/test-suite.md)。如果测试失败，则意味着检测到了突变；如果所有测试都通过，则突变未被检测到，表明[test suite](../T/test-suite.md)中存在潜在的弱点。
  此方法提供了一种方法来衡量 [test suite](../T/test-suite.md) 在查找错误方面的**真实有效性**，而不仅仅是确认软件在已知条件下的行为符合预期。它是**白盒测试**的一种形式，提供测试质量的定量测量并鼓励开发更全面的[test cases](../T/test-case.md)。

#### 突变测试有什么好处？

[Mutation testing](../M/mutation-testing.md) 具有多种优势，可以提高 [test suites](../T/test-suite.md) 的质量和有效性：

- **检测弱点**：它通过识别测试可能无法捕获错误的特定条件来暴露测试套件中的弱点。
  - **提高测试质量**：鼓励创建更彻底的测试用例，从而形成更强大、更可靠的测试套件。
  - **定量测量**：通过突变分数提供测试套件有效性的定量测量，可用于基准测试和改进测试工作。
  - **针对极端情况**：有助于针对标准测试过程中经常被忽视的极端情况和边缘条件。
  - **驱动开发**：可以通过突出显示未经过充分测试的代码区域来驱动开发，这在测试驱动开发 (TDD) 环境中特别有用。
  - **完善代码理解**：增强对代码库的理解，因为测试人员必须批判性地思考代码如何工作才能生成有意义的突变体。
  - **鼓励重构**：当杀死突变体的过程揭示出难以测试的复杂或编写不良的代码时，可能会导致代码重构。
  - **与 CI 集成**：可以集成到持续集成 (CI) 管道中，以随着代码更改不断提高测试套件的质量。
  通过专注于突变体的产生和随后的消除，[mutation testing](../M/mutation-testing.md) 推动了一种超越传统测试方法的更全面、更有弹性的测试策略。

- **检测弱点**：它通过识别测试可能无法捕获错误的特定条件来暴露测试套件中的弱点。
  - **提高测试质量**：鼓励创建更彻底的测试用例，从而形成更强大、更可靠的测试套件。
  - **定量测量**：通过突变分数提供测试套件有效性的定量测量，可用于基准测试和改进测试工作。
  - **针对极端情况**：有助于针对标准测试过程中经常被忽视的极端情况和边缘条件。
  - **驱动开发**：可以通过突出显示未经过充分测试的代码区域来驱动开发，这在测试驱动开发 (TDD) 环境中特别有用。
  - **完善代码理解**：增强对代码库的理解，因为测试人员必须批判性地思考代码如何工作才能生成有意义的突变体。
  - **鼓励重构**：当杀死突变体的过程揭示出难以测试的复杂或编写不良的代码时，可能会导致代码重构。
  - **与 CI 集成**：可以集成到持续集成 (CI) 管道中，以随着代码更改不断提高测试套件的质量。

#### 突变测试有哪些局限性？

[Mutation testing](../M/mutation-testing.md) 虽然功能强大，但有几个限制：

- **高计算成本**：生成和测试大量突变体可能会占用资源，特别是对于大型代码库。
  - **等效突变体**：某些突变体可能在功能上与原始程序相同，因此无法通过测试杀死它们。识别这些等效突变体通常是不可判定的，需要手动检查。
  - **琐碎的突变体**：一些突变体可能会导致微不足道的变化，而这些变化无助于有意义的测试用例改进。
  - **有限变异算子**：变异测试的有效性取决于所使用的变异算子。如果操作员不反映现实世界的错误，测试的价值就会降低。
  - **[Test suite](../T/test-suite.md) 质量**：突变测试假设存在良好的初始测试套件。如果没有它，突变分数可能无法准确反映代码的质量。
  - **耗时**：该过程可能很慢，对于持续集成或没有优化技术的频繁部署场景来说是不切实际的。
  - **[False positives](../F/false-positive.md)** ：突变测试可能会将经过良好测试的代码标记为未充分测试，因为存在不代表可能错误的幸存突变体。
  - **学习曲线**：理解和解释突变测试结果可能具有挑战性，需要深入了解代码和突变测试过程本身。
  尽管存在这些限制，[mutation testing](../M/mutation-testing.md) 仍然是评估和提高[test suites](../T/test-suite.md) 质量的宝贵工具，只要它的使用根据项目的背景及其限制进行定制。

- **高计算成本**：生成和测试大量突变体可能会占用资源，特别是对于大型代码库。
  - **等效突变体**：某些突变体可能在功能上与原始程序相同，因此无法通过测试杀死它们。识别这些等效突变体通常是不可判定的，需要手动检查。
  - **琐碎的突变体**：一些突变体可能会导致微不足道的变化，而这些变化无助于有意义的测试用例改进。
  - **有限变异算子**：变异测试的有效性取决于所使用的变异算子。如果操作员不反映现实世界的错误，测试的价值就会降低。
  - **[Test suite](../T/test-suite.md) 质量**：突变测试假设存在良好的初始测试套件。如果没有它，突变分数可能无法准确反映代码的质量。
  - **耗时**：该过程可能很慢，对于持续集成或没有优化技术的频繁部署场景来说是不切实际的。
  - **[False positives](../F/false-positive.md)** ：突变测试可能会将经过充分测试的代码标记为未充分测试，因为存在不代表可能的故障的幸存突变体。
  - **学习曲线**：理解和解释突变测试结果可能具有挑战性，需要深入了解代码和突变测试过程本身。

### 概念和技术

#### 突变测试的关键概念是什么？

[Mutation testing](../M/mutation-testing.md) 涉及通过进行小的更改（通常通过预定义的**突变运算符**）来创建代码的**突变体**。这些运算符可能会更改算术运算、逻辑连接器或代码的其他部分以引入错误。目标是通过检查 [test suite](../T/test-suite.md) 是否可以检测到这些故意故障来评估它的有效性。
  **突变分数**是评估 [test suite](../T/test-suite.md) 质量的指标，通过检测到的突变体与非等效突变体总数的比率计算。高分表示强大的[test suite](../T/test-suite.md)。
  为了降低成本，采用了**选择性突变**、**突变体采样**和**并行执行**等技术。这些策略旨在最大限度地减少突变体的数量和测试所需的时间，而不显着损害[mutation testing](../M/mutation-testing.md)过程的有效性。
  在**持续集成**环境中，[mutation testing](../M/mutation-testing.md) 可以集成为作为构建过程的一部分自动运行。这可确保持续评估[test suite](../T/test-suite.md) 针对代码更改的有效性。
  解释结果涉及分析哪些突变体被杀死，哪些存活下来。幸存的突变体指出了[test suite](../T/test-suite.md) 的潜在弱点，从而指导改进。
  最佳实践包括从突变运算符的子集开始，重点关注代码的关键部分，并在完善 [test suite](../T/test-suite.md) 时逐渐扩展。
  [Mutation testing](../M/mutation-testing.md) 诸如 **Stryker**、**PIT** 和 **MutPy** 之类的工具可以帮助自动化该过程，提供对各种编程语言的支持以及与构建工具的集成。
  高阶[mutation testing](../M/mutation-testing.md)和[test case](../T/test-case.md)生成是高级主题，涉及创建具有多个变化的突变体并分别使用[mutation testing](../M/mutation-testing.md)来通知新[test cases](../T/test-case.md)的创建。

#### 突变测试中的突变体是什么？

[mutation testing](../M/mutation-testing.md) 中的突变体是原始代码的修改版本，是通过使用**突变运算符**进行小的更改而创建的。这些更改旨在模仿常见的编程错误或强制执行特定条件。每个突变体都是原始代码的副本，并应用了这样的更改。
  创建突变体的目的是评估[test cases](../T/test-case.md)的有效性。如果 [test suite](../T/test-suite.md) 能够检测并“杀死”这些突变体，则被认为是稳健的，这意味着针对更改的代码执行测试时会失败。如果[test suite](../T/test-suite.md) 没有让突变体失效，则称该突变体“幸存”，表明[test coverage](../T/test-coverage.md) 中存在潜在弱点。
  这是 TypeScript 中的一个简单示例：
  原始代码：

  ```
  function isEven(number: number): boolean {
    return number % 2 === 0;
  }
  ```变异例子：

  ```
  function isEven(number: number): boolean {
    return number % 2 !== 0; // Mutated line
  }
  ```在这种情况下，突变将相等运算符从`===`更改为`!==`。当针对这个突变体运行时，全面的[test suite](../T/test-suite.md)应该会失败，表明检测到了突变（以及它所代表的故障类型）。

#### 什么是突变分数以及它是如何计算的？

**突变分数**是 [test suite](../T/test-suite.md) 在识别 [mutation testing](../M/mutation-testing.md) 引入的故障方面的有效性的定量测量。它的计算方法是将**检测到的突变体**（导致测试失败的突变体）的数量除以**非等效突变体**（导致程序行为发生变化并可以被[test case](../T/test-case.md)检测到的突变体）的总数。
  突变得分的计算公式为：

  ```
  Mutation Score = (Detected Mutants / (Total Mutants - Equivalent Mutants)) * 100
  ```

- **检测到的突变体**：被杀死的突变体数量（即导致至少一项测试失败）。
  - **突变体总数**：通过应用突变算子生成的突变体总数。
  - **等效突变体**：尽管代码发生变化，但不会改变程序的外部行为，因此无法被任何测试捕获的突变体。
  突变得分以百分比表示，百分比越高表示[test suite](../T/test-suite.md)越有效。 100% 的分数意味着[test suite](../T/test-suite.md) 检测到了所有非等价突变体，表明测试有效性较高。然而，由于等效突变体的存在以及实现这种彻底性的成本，实现 100% 突变评分通常是不切实际的。因此，团队通常会寻求一个突变分数，以平衡彻底性和实现它所需的努力。

- **检测到的突变体**：被杀死的突变体数量（即导致至少一项测试失败）。
  - **突变体总数**：通过应用突变算子生成的突变体总数。
  - **等效突变体**：尽管代码发生变化，但不会改变程序的外部行为，因此无法被任何测试捕获的突变体。

#### 变异算子有哪些不同类型？

突变运算符是定义如何修改程序源代码以创建突变体的规则。不同类型的变异运算符针对代码的各个方面：

- **算术运算符替换 (AOR)** ：更改算术运算符（例如，
    `+`
    到
    `-`
    ）。

- **关系运算符替换 (ROR)** ：更改关系运算符（例如，
    `>`
    到
    `>=`
    ）。

- **逻辑运算符替换 (LOR)** ：修改逻辑运算符（例如，
    `&&`
    到
    `||`
    ）。

- **绝对值插入 (ABS)**：在表达式周围插入绝对值函数。
  - **条件运算符替换 (COR)** ：切换条件运算符（例如，
    `?:`
    ）。

- **语句删除 (STD)** ：从代码中删除语句。
  - **变量替换 (VR)** ：用相同范围和类型的其他变量替换变量。
  - **常量替换 (CR)** ：更改表达式中的常量。
  - **函数调用替换 (FCR)** ：用具有相同签名的其他函数替换函数调用。
  - **否定插入 (NEG)** ：在布尔表达式中插入否定。
  - **边界值更改 (BVC)**：修改条件和表达式中的边界值。
  每个操作符的目的是模拟常见的编程错误或强制[test suite](../T/test-suite.md)考虑不同的执行路径。通过评估[test suite](../T/test-suite.md) 检测这些故意注入的故障的能力，[mutation testing](../M/mutation-testing.md) 提供了对[test cases](../T/test-case.md) 的有效性和覆盖范围的见解。

- **算术运算符替换 (AOR)** ：更改算术运算符（例如，
    `+`
    到
    `-`
    ）。

- **关系运算符替换 (ROR)** ：更改关系运算符（例如，
    `>`
    到
    `>=`
    ）。

- **逻辑运算符替换 (LOR)** ：修改逻辑运算符（例如，
    `&&`
    到
    `||`
    ）。

- **绝对值插入 (ABS)**：在表达式周围插入绝对值函数。
  - **条件运算符替换 (COR)** ：切换条件运算符（例如，
    `?:`
    ）。

- **语句删除 (STD)** ：从代码中删除语句。
  - **变量替换 (VR)** ：用相同范围和类型的其他变量替换变量。
  - **常量替换 (CR)** ：更改表达式中的常量。
  - **函数调用替换 (FCR)** ：用具有相同签名的其他函数替换函数调用。
  - **否定插入 (NEG)** ：在布尔表达式中插入否定。
  - **边界值更改 (BVC)**：修改条件和表达式中的边界值。

#### 使用哪些技术来降低突变测试的成本？

要降低 [mutation testing](../M/mutation-testing.md) 的成本，请考虑以下技术：

- **选择性变异**：重点关注在检测故障方面最有效的变异算子子集。这减少了生成和测试的突变体的数量。
  - **突变采样**：不是生成所有可能的突变体，而是随机选择一个代表性样本。这可以显着减少突变体的数量，同时仍然保持测试有效性。
  - **等效突变体检测**：开发识别和排除等效突变体的方法，这些突变体不会改变程序的外部行为，以避免在其上浪费资源。
  - **高阶突变体**：谨慎使用高阶突变体（具有多个变化的突变体），因为它们更复杂并且不太可能代表现实世界的错误。
  - **[Test Case](../T/test-case.md) 优先级**：根据 [test cases](../T/test-case.md) 杀死突变体的有效性确定优先级。尽早运行最有效的测试，以便更快地发现故障。
  - **并行执行**：利用并行计算资源同时执行[mutation testing](../M/mutation-testing.md)任务，减少整体执行时间。
  - **增量[Mutation Testing](../M/mutation-testing.md)**：仅将[mutation testing](../M/mutation-testing.md)应用于修改后的代码或新功能，而不是整个代码库，以节省时间和资源。
  - **工具优化**：选择并配置[mutation testing](../M/mutation-testing.md) 提供性能优化的工具，例如代码检测和即时编译。
  - CI 中的 **[Mutation Testing](../M/mutation-testing.md)**：将 [mutation testing](../M/mutation-testing.md) 集成到您的持续集成 (CI) 管道中，以分摊整个开发周期的成本并及早发现问题。
  通过应用这些策略，您可以使[mutation testing](../M/mutation-testing.md) 更具成本效益，同时仍然获得[test suite](../T/test-suite.md) 改进的好处。

- **选择性变异**：重点关注在检测故障方面最有效的变异算子子集。这减少了生成和测试的突变体的数量。
  - **突变采样**：不是生成所有可能的突变体，而是随机选择一个代表性样本。这可以显着减少突变体的数量，同时仍然保持测试有效性。
  - **等效突变体检测**：开发识别和排除等效突变体的方法，这些突变体不会改变程序的外部行为，以避免在其上浪费资源。
  - **高阶突变体**：谨慎使用高阶突变体（具有多个变化的突变体），因为它们更复杂并且不太可能代表现实世界的错误。
  - **[Test Case](../T/test-case.md) 优先级**：根据 [test cases](../T/test-case.md) 杀死突变体的有效性确定优先级。尽早运行最有效的测试，以便更快地发现故障。
  - **并行执行**：利用并行计算资源同时执行[mutation testing](../M/mutation-testing.md)任务，减少整体执行时间。
  - **增量[Mutation Testing](../M/mutation-testing.md)**：仅将[mutation testing](../M/mutation-testing.md)应用于修改后的代码或新功能，而不是整个代码库，以节省时间和资源。
  - **工具优化**：选择并配置提供性能优化的[mutation testing](../M/mutation-testing.md) 工具，例如代码检测和即时编译。
  - CI 中的 **[Mutation Testing](../M/mutation-testing.md)**：将 [mutation testing](../M/mutation-testing.md) 集成到您的持续集成 (CI) 管道中，以分摊整个开发周期的成本并及早发现问题。

### 实施和工具

#### 执行突变测试涉及哪些步骤？

要执行[mutation testing](../M/mutation-testing.md)，请执行以下步骤：

1. **选择目标**：选择您要测试的代码段。
  2. **生成突变体**：将突变运算符应用于原始代码以创建更改的版本，称为突变体。
  3. **运行[test suite](../T/test-suite.md)** ：针对每个突变体执行现有的测试套件。
  4. **确定存活**：检查哪些突变体被测试“杀死”（即测试失败）以及哪些“存活”（即测试通过）。
  5. **分析结果**：检查幸存的突变体以识别测试套件中的弱点。
  6. **改进测试**：增强您的测试套件以杀死幸存的突变体，确保它可以捕获更多类型的错误。
  7. **重复**：迭代该过程，完善测试套件，直到达到令人满意的突变分数或直到观察到收益递减。
  使用 [mutation testing](../M/mutation-testing.md) 工具自动执行步骤 2 到 4。改进 [test suite](../T/test-suite.md) 后，重新运行 [mutation testing](../M/mutation-testing.md) 以验证新测试是否有效。请记住，[mutation testing](../M/mutation-testing.md) 可能会占用大量资源，因此请考虑优化流程的策略，例如使用突变运算符的子集或并行执行。

1. **选择目标**：选择您要测试的代码段。
  2. **生成突变体**：将突变运算符应用于原始代码以创建更改的版本，称为突变体。
  3. **运行[test suite](../T/test-suite.md)** ：针对每个突变体执行现有的测试套件。
  4. **确定存活**：检查哪些突变体被测试“杀死”（即测试失败）以及哪些“存活”（即测试通过）。
  5. **分析结果**：检查幸存的突变体以识别测试套件中的弱点。
  6. **改进测试**：增强您的测试套件以杀死幸存的突变体，确保它可以捕获更多类型的错误。
  7. **重复**：迭代该过程，完善测试套件，直到达到令人满意的突变分数或直到观察到收益递减。

#### 有哪些工具可用于突变测试？

有多种工具可用于跨不同编程语言的[mutation testing](../M/mutation-testing.md)：

- **PIT (Pitest)** ：与 Maven 和 Ant 集成的流行 Java 工具。它速度很快并且可以与持续集成系统一起使用。

    ```
    <plugin>
      <groupId>org.pitest</groupId>
      <artifactId>pitest-maven</artifactId>
      <version>LATEST</version>
    </plugin>
    ```

- **Stryker**：JavaScript、TypeScript 和 .NET 的突变测试框架。它被设计为健壮且与框架无关。

    ```
    npm install --save-dev @stryker-mutator/core
    ```

- **MutPy** ：Python程序的突变测试工具，支持unittest和pytest测试套件。

    ```
    pip install MutPy
    ```

- **Infection**：PHP 突变测试工具，支持 PHPUnit。

    ```
    composer require --dev infection/infection
    ```

- **Humbug**：另一个 PHP 突变测试工具，设计简单易用。
  - **Cosmic Ray**：Python 的突变测试工具，注重简单性和易用性。
  - **Mull** ：基于 LLVM 的 C 和 C++ 突变测试工具，支持各种测试框架。
  - **主要**：Java 程序的突变测试框架，可以用作命令行工具或集成到 Ant/Maven 构建中。
  这些工具自动生成突变体并针对它们运行 [test suites](../T/test-suite.md)、计算突变分数并提供报告以帮助提高测试质量。与流行的构建工具和测试框架的集成使它们适合包含在 CI/CD 管道中。

- **PIT (Pitest)** ：与 Maven 和 Ant 集成的流行 Java 工具。它速度很快并且可以与持续集成系统一起使用。

    ```
    <plugin>
      <groupId>org.pitest</groupId>
      <artifactId>pitest-maven</artifactId>
      <version>LATEST</version>
    </plugin>
    ```

- **Stryker**：JavaScript、TypeScript 和 .NET 的突变测试框架。它被设计为健壮且与框架无关。

    ```
    npm install --save-dev @stryker-mutator/core
    ```

- **MutPy** ：Python程序的突变测试工具，支持unittest和pytest测试套件。

    ```
    pip install MutPy
    ```

- **Infection**：PHP 突变测试工具，支持 PHPUnit。

    ```
    composer require --dev infection/infection
    ```

- **Humbug**：另一个 PHP 突变测试工具，设计简单易用。
  - **Cosmic Ray**：Python 的突变测试工具，注重简单性和易用性。
  - **Mull** ：基于 LLVM 的 C 和 C++ 突变测试工具，支持各种测试框架。
  - **主要**：Java 程序的突变测试框架，可以用作命令行工具或集成到 Ant/Maven 构建中。

#### 如何在持续集成环境中实现变异测试？

要在持续集成 (CI) 环境中实施[mutation testing](../M/mutation-testing.md)，请执行以下步骤：

1. **选择与您的技术堆栈和 CI 系统兼容的 [mutation testing](../M/mutation-testing.md) 工具**。流行的工具包括用于 JavaScript 的 Stryker、用于 Java 的 PIT 和用于 Python 的 MutPy。
  2. **将该工具集成到您的构建管道中**。在 CI 配置中添加一个步骤来运行 [mutation testing](../M/mutation-testing.md) 工具。例如，在 Jenkins 管道中，您可以添加一个阶段：

    ```
    stage('Mutation Test') {
        steps {
            sh 'mvn org.pitest:pitest-maven:mutationCoverage'
        }
    }
    ```

3. **配置[mutation testing](../M/mutation-testing.md) 工具**以针对代码库中最关键的部分来管理执行时间。使用配置文件或命令行参数来指定包含和排除的类、方法或文件。
  4. **设置突变分数的阈值**以确定构建的通过/失败标准。如果分数低于阈值，则构建应该失败。

    ```
    failWhenScoreLessThan: 75
    ```

5. **通过并行或在非高峰时段运行突变测试来优化流程**，以尽量减少对开发人员生产力的影响。
  6. **审查结果并采取行动**。应检查[Mutation testing](../M/mutation-testing.md) 报告，以确定[test suite](../T/test-suite.md) 中的薄弱环节并改进[test cases](../T/test-case.md)。
  7. **自动结果跟踪**。集成报告工具以可视化突变分数随时间变化的趋势，帮助您监控 [test suite](../T/test-suite.md) 的有效性。
  8. **根据 CI 流程的反馈定期完善您的 [mutation testing](../M/mutation-testing.md) 策略**，调整范围和配置以保持彻底性和构建时间之间的平衡。
  1. **选择与您的技术堆栈和 CI 系统兼容的 [mutation testing](../M/mutation-testing.md) 工具**。流行的工具包括用于 JavaScript 的 Stryker、用于 Java 的 PIT 和用于 Python 的 MutPy。
  2. **将该工具集成到您的构建管道中**。在 CI 配置中添加一个步骤来运行 [mutation testing](../M/mutation-testing.md) 工具。例如，在 Jenkins 管道中，您可以添加一个阶段：

    ```
    stage('Mutation Test') {
        steps {
            sh 'mvn org.pitest:pitest-maven:mutationCoverage'
        }
    }
    ```

3. **配置[mutation testing](../M/mutation-testing.md) 工具**以针对代码库中最关键的部分来管理执行时间。使用配置文件或命令行参数来指定包含和排除的类、方法或文件。
  4. **设置突变分数的阈值**以确定构建的通过/失败标准。如果分数低于阈值，则构建应该失败。

    ```
    failWhenScoreLessThan: 75
    ```

5. **通过并行或在非高峰时段运行突变测试来优化流程**，以尽量减少对开发人员生产力的影响。
  6. **审查结果并采取行动**。应检查[Mutation testing](../M/mutation-testing.md) 报告，以确定[test suite](../T/test-suite.md) 中的薄弱环节并改进[test cases](../T/test-case.md)。
  7. **自动结果跟踪**。集成报告工具以可视化突变分数随时间变化的趋势，帮助您监控 [test suite](../T/test-suite.md) 的有效性。
  8. **根据 CI 流程的反馈定期完善您的 [mutation testing](../M/mutation-testing.md) 策略**，调整范围和配置以保持彻底性和构建时间之间的平衡。

#### 实施突变测试的最佳实践有哪些？

实施 [mutation testing](../M/mutation-testing.md) 的最佳实践包括：

- **优先考虑关键代码**：重点关注对应用程序功能至关重要的代码库部分。
  - **从小处开始**：从一组有限的变异算子开始，在扩展之前了解它们的影响。
  - **与现有测试集成**：使用突变测试来评估和提高当前测试套件的质量。
  - **自动化该过程**：将突变测试纳入您的构建管道以定期运行它。
  - **使用增量分析**：对代码更改应用突变测试以有效管理流程。
  - **设置现实的阈值**：建立可实现的突变评分目标，以避免争取不切实际的 100% 突变覆盖率。
  - **分析结果并采取行动**：审查突变测试结果，以识别测试中的薄弱点并相应地增强它们。
  - **平衡[test suite](../T/test-suite.md) 大小和质量**：目标是建立一个能够有效检测突变体而又不会变得笨重的测试套件。
  - **教育您的团队**：确保所有团队成员了解突变测试的目的和好处，以促进其采用。
  - **监控性能**：密切关注突变测试所消耗的时间和资源，并根据需要进行优化。
  通过遵循这些实践，您可以有效地利用 [mutation testing](../M/mutation-testing.md) 来提高软件 [test automation](../T/test-automation.md) 工作的稳健性。

- **优先考虑关键代码**：重点关注对应用程序功能至关重要的代码库部分。
  - **从小处开始**：从一组有限的变异算子开始，在扩展之前了解它们的影响。
  - **与现有测试集成**：使用突变测试来评估和提高当前测试套件的质量。
  - **自动化该过程**：将突变测试纳入您的构建管道以定期运行它。
  - **使用增量分析**：对代码更改应用突变测试以有效管理流程。
  - **设置现实的阈值**：建立可实现的突变评分目标，以避免争取不切实际的 100% 突变覆盖率。
  - **分析结果并采取行动**：审查突变测试结果，以识别测试中的薄弱点并相应地增强它们。
  - **平衡[test suite](../T/test-suite.md) 大小和质量**：目标是建立一个能够有效检测突变体而又不会变得笨拙的测试套件。
  - **教育您的团队**：确保所有团队成员了解突变测试的目的和好处，以促进其采用。
  - **监控性能**：密切关注突变测试所消耗的时间和资源，并根据需要进行优化。

#### 如何解读突变检测结果？

解释[mutation testing](../M/mutation-testing.md) 的结果涉及分析**突变得分**和**杀死和存活的突变体**。突变得分通常以百分比表示，表示被杀死（即由 [test suite](../T/test-suite.md) 检测到）的突变体占生成的突变体总数的比例。
  **高突变分数**表明[test suite](../T/test-suite.md)能够有效检测注入的故障并且具有良好的覆盖率。然而，检查突变体的背景至关重要：

- **幸存的突变体**表明[test suite](../T/test-suite.md)中存在潜在的弱点。分析每个幸存的突变体，了解其未被杀死的原因，并考虑添加或改进 [test cases](../T/test-case.md) 以涵盖这些场景。
  - **等效突变体**，在语法上不同但在功能上与原始代码相同，可以夸大突变分数。这些应该被识别出来，并可能从分数计算中排除，以获得更准确的评估。
  - **被杀死的突变体**验证了现有[test cases](../T/test-case.md)的有效性，但也需要审查以确保它们代表现实且有价值的[test scenarios](../T/test-scenario.md)。
  在审查结果时，优先考虑代表可能的故障或关键功能的突变体。利用获得的见解来完善和加强[test suite](../T/test-suite.md)，重点关注[mutation testing](../M/mutation-testing.md) 表明覆盖或检测能力不足的领域。
  请记住，我们的目标不是获得完美分数，而是提高[test suite](../T/test-suite.md) 捕获回归和错误的能力，从而提高软件的可靠性。

- **幸存的突变体**表明[test suite](../T/test-suite.md)中的潜在弱点。分析每个幸存的突变体，了解其未被杀死的原因，并考虑添加或改进 [test cases](../T/test-case.md) 以涵盖这些场景。
  - **等效突变体**，在语法上不同但在功能上与原始代码相同，可以夸大突变分数。这些应该被识别出来，并可能从分数计算中排除，以获得更准确的评估。
  - **被杀死的突变体**验证了现有[test cases](../T/test-case.md)的有效性，但也需要审查以确保它们代表现实且有价值的[test scenarios](../T/test-scenario.md)。

### 高级主题

#### 什么是高阶突变测试？

高阶[mutation testing](../M/mutation-testing.md) 是[mutation testing](../M/mutation-testing.md) 的高级形式，其中**突变被组合**以生成更复杂的突变体，通常称为**高阶突变体（HOM）**。与传统的 [mutation testing](../M/mutation-testing.md) 不同，传统的 [mutation testing](../M/mutation-testing.md) 专注于一阶突变体（每个突变体单个突变），高阶 [mutation testing](../M/mutation-testing.md) 会同时将多个突变算子应用于原始程序。
  高阶 [mutation testing](../M/mutation-testing.md) 背后的基本原理是，它可以通过引入实际编码场景中可能发生的多个相关错误来**模拟更真实的故障**。它还旨在通过创建更细微的更改来解决**等效突变体**和**琐碎突变体**的问题，这些更改在语义上不太可能与原始程序等效或太琐碎而无用。
  高阶突变体是通过组合两个或多个一级突变体而产生的。该过程包括选择通过现有[test suite](../T/test-suite.md)的一阶突变体，然后以各种方式将它们组合起来生成HOM。然后针对 [test suite](../T/test-suite.md) 测试这些 HOM，看看是否可以检测到它们。

  ```
  // Example of creating a higher order mutant by combining two first order mutations
  original_code = "if (a && b) { doSomething(); }"
  first_order_mutant1 = "if (a || b) { doSomething(); }"
  first_order_mutant2 = "if (a && !b) { doSomething(); }"
  higher_order_mutant = "if (a || !b) { doSomething(); }" // Combination of the two
  ```由于可能的突变体组合呈指数增长，高阶[mutation testing](../M/mutation-testing.md)被认为比一阶[mutation testing](../M/mutation-testing.md)更具挑战性且计算成本更高。然而，它可以对[test suite](../T/test-suite.md) 检测复杂故障的能力进行更彻底的检查。

#### 突变测试如何帮助测试套件改进？

[Mutation testing](../M/mutation-testing.md) 通过**识别弱点**和**增强[test coverage](../T/test-coverage.md)** 帮助改进[test suites](../T/test-suite.md)。它通过生成突变体来实现这一点，这些突变体是原始代码的细微变化，然后针对这些突变体运行现有的[test suite](../T/test-suite.md)。如果[test suite](../T/test-suite.md) 未能检测并杀死这些突变体，则表明[test coverage](../T/test-coverage.md)** 中存在**缺口。
  通过分析[mutation testing](../M/mutation-testing.md)的结果，工程师可以：

- **确定具体条件**
    未经过测试的部分，例如边界条件或错误处理路径。

- **完善现有测试**
    使它们更加稳健并对潜在缺陷更加敏感。

- **添加新测试**
    覆盖幸存的突变体揭示的未经测试的代码路径。

- **删除或改进冗余测试**
    这不会有助于杀死突变体，从而优化测试套件以提高效率。
  [Mutation testing](../M/mutation-testing.md) 因此充当反馈机制，引导工程师**关注需要更彻底测试的领域**。这会导致更有效和更全面的[test suite](../T/test-suite.md)，从而增加在软件发布之前捕获[bugs](../B/bug.md)的可能性。随着代码库的不断发展，它还有助于保持高质量的[test suite](../T/test-suite.md)。
  通过持续应用[mutation testing](../M/mutation-testing.md)，团队可以确保他们的[test suites](../T/test-suite.md)不仅广泛，而且具有针对性和高效性，从而**提高[software quality](../S/software-quality.md)**和**可靠性**。

- **确定具体条件**
    未经过测试的部分，例如边界条件或错误处理路径。

- **完善现有测试**
    使它们更加稳健并对潜在缺陷更加敏感。

- **添加新测试**
    覆盖幸存的突变体揭示的未经测试的代码路径。

- **删除或改进冗余测试**
    这不会有助于杀死突变体，从而优化测试套件以提高效率。

#### 突变测试在测试用例生成中的作用是什么？

[Mutation testing](../M/mutation-testing.md) 通过提供评估和提高[test cases](../T/test-case.md) 质量的方法，在**[test case](../T/test-case.md) 生成**中发挥着至关重要的作用。通过对代码进行微小的更改（称为**突变体**），它会挑战现有的[test suite](../T/test-suite.md)来检测这些修改。如果 [test case](../T/test-case.md) 由于突变而失败，则表明 [test case](../T/test-case.md) 可以有效捕获与原始代码行为的偏差。
  在[test case](../T/test-case.md)生成的背景下，[mutation testing](../M/mutation-testing.md)帮助识别[test suite](../T/test-suite.md)中的弱点，指导测试人员创建新的[test cases](../T/test-case.md)来覆盖以前未检测到的路径或条件。此过程导致开发出一组更强大的[test cases](../T/test-case.md)，它们能够更好地确保代码的正确性。
  [Mutation testing](../M/mutation-testing.md) 也可以自动系统地生成突变体并针对它们运行[test suite](../T/test-suite.md)。然后可以分析结果以确定代码的哪些部分没有经过充分测试。这个反馈循环对于[test cases](../T/test-case.md)的**持续改进**非常宝贵，确保它们随着代码库的发展而保持有效。
  通过努力获得高**突变分数**，团队有动力生成全面的[test cases](../T/test-case.md)，不仅断言预期结果，而且还考虑边缘情况和潜在错误。这种严格的 [test case](../T/test-case.md) 生成方法有助于提高 [software quality](../S/software-quality.md) 和可靠性。

#### 扩展大型代码库的突变测试有哪些挑战？

为大型代码库扩展 [mutation testing](../M/mutation-testing.md) 会带来一些挑战：

- **资源密集性**：[Mutation testing](../M/mutation-testing.md) 需要大量的计算资源，因为它会生成大量突变体并对每个突变体运行 [test suite](../T/test-suite.md)。对于大型代码库来说，这可能特别要求。
  - **时间消耗**：该过程非常耗时，因为测试每个突变体可能需要与运行整个[test suite](../T/test-suite.md)一样长的时间。对于大型项目，这可能会导致执行时间不切实际。
  - **等效突变体**：随着代码库的增长，识别和处理等效突变体（不改变程序外部行为的突变体）变得更加困难，导致浪费精力和潜在的[false positives](../F/false-positive.md)。
  - **突变爆炸**：可能突变的数量随着代码大小呈指数增长。这种“突变爆炸”可能会让人很难专注于最有意义的突变。
  - **[Test Suite](../T/test-suite.md) 质量**：[Mutation testing](../M/mutation-testing.md) 假定为高质量[test suite](../T/test-suite.md)。在大型代码库中，确保 [test suite](../T/test-suite.md) 在所有组件中的有效性可能具有挑战性。
  - **并行执行**：虽然并行执行可以缓解一些性能问题，但它需要仔细编排来管理跨多个机器或处理器的测试分布和结果收集。
  - **数据管理**：处理和分析大型代码库中[mutation testing](../M/mutation-testing.md) 生成的大量数据可能会令人难以承受，并且可能需要专门的工具或[databases](../D/database.md)。
  为了应对这些挑战，通常采用**选择性突变**、**突变体采样**和**增量[mutation testing](../M/mutation-testing.md)**等策略。这些方法旨在减少突变体的数量，并优先考虑那些最有可能发现故障的突变体，从而使[mutation testing](../M/mutation-testing.md) 对于大型项目来说更加可行。

- **资源密集性**：[Mutation testing](../M/mutation-testing.md) 需要大量的计算资源，因为它会生成大量突变体并对每个突变体运行 [test suite](../T/test-suite.md)。对于大型代码库来说，这可能特别要求。
  - **时间消耗**：该过程非常耗时，因为测试每个突变体可能需要与运行整个[test suite](../T/test-suite.md)一样长的时间。对于大型项目，这可能会导致执行时间不切实际。
  - **等效突变体**：随着代码库的增长，识别和处理等效突变体（不改变程序外部行为的突变体）变得更加困难，导致浪费精力和潜在的[false positives](../F/false-positive.md)。
  - **突变爆炸**：可能突变的数量随着代码大小呈指数增长。这种“突变爆炸”可能会让人很难专注于最有意义的突变。
  - **[Test Suite](../T/test-suite.md) 质量**：[Mutation testing](../M/mutation-testing.md) 假定为高质量 [test suite](../T/test-suite.md)。在大型代码库中，确保 [test suite](../T/test-suite.md) 在所有组件中的有效性可能具有挑战性。
  - **并行执行**：虽然并行执行可以缓解一些性能问题，但它需要仔细编排来管理跨多个机器或处理器的测试分布和结果收集。
  - **数据管理**：处理和分析大型代码库中[mutation testing](../M/mutation-testing.md) 生成的大量数据可能会令人难以承受，并且可能需要专门的工具或[databases](../D/database.md)。

#### 突变测试的最新进展是什么？

[mutation testing](../M/mutation-testing.md) 的最新进展包括：

- **与现代开发工具集成**：[Mutation testing](../M/mutation-testing.md) 工具现在可以更好地与流行的 IDE 和构建系统集成，从而可以无缝包含在开发工作流程中。
  - **性能优化**：引入了*增量突变测试*和*并行执行*等技术来减少[mutation testing](../M/mutation-testing.md)所需的计算成本和时间。
  - **高级变异运算符**：已经开发了针对特定语言功能或常见编程错误的新运算符，提高了检测到的错误的相关性和有效性。
  - **[Mutation testing](../M/mutation-testing.md) 用于非功能属性**：正在努力扩展 [mutation testing](../M/mutation-testing.md) 以评估性能、安全性和并发问题，从而扩大其适用性。
  - **智能突变生成**：利用机器学习和启发式方法来确定优先级并生成更有可能发现真正故障的突变，从而提高效率。
  - **[Mutation testing](../M/mutation-testing.md) 新语言框架**：为以前缺乏支持的语言（例如 Go、Rust 和 Swift）开发 [mutation testing](../M/mutation-testing.md) 工具，正在扩大 [mutation testing](../M/mutation-testing.md) 的范围。
  - **突变体包容研究**：识别并专注于“包容突变体”，可以用更少的[test cases](../T/test-case.md)提供相同或更好的测试信息，从而减少所需突变体的数量。
  - **增强的报告和可视化**：改进的报告工具和仪表板有助于更好地理解[mutation testing](../M/mutation-testing.md)结果并采取行动。
  - **基于云的[mutation testing](../M/mutation-testing.md) 服务**：提供[mutation testing](../M/mutation-testing.md) 作为服务的云平台正在兴起，无需本地计算资源即可提供可扩展性和易用性。
  - **与现代开发工具集成**：[Mutation testing](../M/mutation-testing.md) 工具现在可以更好地与流行的 IDE 和构建系统集成，从而可以无缝包含在开发工作流程中。
  - **性能优化**：引入了*增量突变测试*和*并行执行*等技术来减少[mutation testing](../M/mutation-testing.md)所需的计算成本和时间。
  - **高级变异运算符**：已经开发了针对特定语言功能或常见编程错误的新运算符，提高了检测到的错误的相关性和有效性。
  - **[Mutation testing](../M/mutation-testing.md) 用于非功能属性**：正在努力扩展 [mutation testing](../M/mutation-testing.md) 以评估性能、安全性和并发问题，从而扩大其适用性。
  - **智能突变生成**：利用机器学习和启发式方法来确定优先级并生成更有可能发现真正故障的突变，从而提高效率。
  - **[Mutation testing](../M/mutation-testing.md) 新语言框架**：为以前缺乏支持的语言（例如 Go、Rust 和 Swift）开发 [mutation testing](../M/mutation-testing.md) 工具，正在扩大 [mutation testing](../M/mutation-testing.md) 的范围。
  - **突变体包容研究**：识别并关注“包容突变体”，可以用更少的[test cases](../T/test-case.md)提供相同或更好的测试信息，从而减少所需突变体的数量。
  - **增强的报告和可视化**：改进的报告工具和仪表板有助于更好地理解[mutation testing](../M/mutation-testing.md)结果并采取行动。
  - **基于云的[mutation testing](../M/mutation-testing.md) 服务**：提供[mutation testing](../M/mutation-testing.md) 作为服务的云平台正在兴起，无需本地计算资源即可提供可扩展性和易用性。
