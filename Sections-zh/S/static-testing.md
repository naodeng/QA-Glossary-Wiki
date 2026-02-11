# 静态测试 (Static Testing)
[静态测试 (Static Testing)](#static-testing) [静态测试 (Static Testing)](/wiki/static-testing)

### 相关术语：
- 动态测试 (Dynamic Testing)
[动态测试 (Dynamic Testing)](/glossary/dynamic-testing)

## 关于静态测试的常见问题？

#### 基础与重要性
- **什么是静态测试？**
  **[静态测试 (Static testing)](/wiki/static-testing)** 是指在不执行代码的情况下对软件制品进行检查。它涉及 **分析** 文档和源代码以查找错误，其中可能包括语法错误、代码标准违规和设计问题。此类测试通常通过 **人工** 努力（如同行评审）和执行静态代码分析的 **自动化工具** 结合完成。
  用于 **[静态测试 (static testing)](/wiki/static-testing)** 的自动化工具会扫描代码库，查找指示潜在问题的预定义模式。这些工具可以集成到开发环境或持续集成流水线中，为开发人员提供即时反馈。它们的范围从执行编码标准的简单 Linter 到可以检测更微妙问题（如潜在安全漏洞或性能瓶颈）的复杂静态分析工具。
  **[静态测试 (Static testing)](/wiki/static-testing)** 不仅仅是为了寻找 **[Bug (bugs)](/wiki/bug)**，还关乎 **代码质量** 和 **可维护性**。它有助于确保代码符合标准，并且是可理解且可修改的。通过在开发过程的早期识别问题，**[静态测试 (static testing)](/wiki/static-testing)** 有助于降低修复缺陷的成本，因为越早发现的问题通常解决成本越低。
  为了有效实施 **[静态测试 (static testing)](/wiki/static-testing)**，选择与项目的语言和框架相一致的合适工具和技术至关重要。此外，建立一种重视代码质量和定期评审的文化可以增强 **[静态测试 (static testing)](/wiki/static-testing)** 的益处。

- **为什么静态测试在软件开发过程中很重要？**
  **[静态测试 (Static testing)](/wiki/static-testing)** 在软件开发过程中至关重要，因为它允许在 **[动态测试 (dynamic testing)](/wiki/dynamic-testing)** 开始之前进行 **缺陷的早期检测**。通过在不执行代码的情况下检查代码、需求和设计文档，它有助于在修复成本 **较低** 的阶段识别错误。这种前瞻性的方法通过确保在初始阶段解决问题，提高了 **最终产品的质量**，降低了开发生命周期后期复合错误的风险。
  此外，**[静态测试 (static testing)](/wiki/static-testing)** 有助于对代码库和系统架构有 **更好的理解**，这可以带来更具可维护性和更稳健的软件。它还支持对编码标准的 **合规性**，并能突出潜在的 **安全漏洞**。通过捕捉文档和代码中的歧义和不一致，**[静态测试 (static testing)](/wiki/static-testing)** 增强了软件需求和设计的清晰度，从而实现更准确和可靠的实施。
  本质上，**[静态测试 (static testing)](/wiki/static-testing)** 是一种 **预防性措施**，它通过确保代码库在运行任何功能测试之前具有高质量，来补充 **[动态测试 (dynamic testing)](/wiki/dynamic-testing)**。它是全面 **[质量保证 (quality assurance)](/wiki/quality-assurance)** 战略中不可或缺的一部分，有助于简化开发过程并有助于交付更可靠的软件产品。

- **静态测试与动态测试有何不同？**
  **[静态测试 (Static testing)](/wiki/static-testing)** 涉及在不执行程序的情况下检查代码、需求或文档。这是一种 **[验证 (verification)](/wiki/verification)** 形式，在开发过程的早期检查问题。另一方面，**[动态测试 (Dynamic testing)](/wiki/dynamic-testing)** 需要执行代码，并根据定义的需求验证软件运行。这是一种确认形式，通常涉及单元测试、集成测试、系统测试和验收测试。
  - **静态测试 (Static Testing)**：
    - 在不运行程序的情况下分析代码结构、语法和用法。
    - 包括评审、检查和静态代码分析。
    - 旨在在代码执行之前及早发现缺陷。
  - **动态测试 (Dynamic Testing)**：
    - 涉及执行代码并在各种条件下检查系统行为。
    - 包括功能和非功能测试方法。
    - 旨在发现仅在软件运行时才会浮现的缺陷。
  虽然 **[静态测试 (static testing)](/wiki/static-testing)** 侧重于预防缺陷，但 **[动态测试 (dynamic testing)](/wiki/dynamic-testing)** 侧重于发现缺陷。由于 **[静态测试 (Static testing)](/wiki/static-testing)** 无需运行环境即可识别错误，因此更具成本效益。然而，**[动态测试 (Dynamic testing)](/wiki/dynamic-testing)** 对于确保软件在真实场景中按预期工作必不可少。两种测试类型是互补的，结合使用时，可为软件质量保证提供全面的方法。

- **静态测试的益处有哪些？**
  **[静态测试 (static testing)](/wiki/static-testing)** 的益处包括：
  - **早期缺陷检测**：在代码执行前识别问题，减少后期修复 Bug 的成本和工作量。
  - **提高代码质量**：鼓励遵循编码标准和最佳实践，从而产生更整洁、更易于维护的代码。
  - **文档 [验证 (Verification)](/wiki/verification)**：确保文档准确反映了软件的预期功能和设计。
  - **效率**：无需运行环境或创建测试用例即可捕捉错误，节省时间和资源。
  - **全面分析**：一次性分析整个代码库和文档，对软件质量进行彻底评估。
  - **非侵入式**：不改变程序行为，因为它不需要执行代码。
  - **风险缓解**：及早识别潜在的安全漏洞和合规性问题。
  - **团队协作**：通过评审和检查促进团队成员之间的讨论和知识共享。
  - **过程改进**：提供对开发过程的见解，突出待改进区域并确保项目的一致性。
  **[静态测试 (Static testing)](/wiki/static-testing)** 通过提供不同的质量和可靠性视角来补充 **[动态测试 (dynamic testing)](/wiki/dynamic-testing)**，最终有助于打造更稳健且无错的软件产品。

- **静态测试的关键目标是什么？**
  **[静态测试 (static testing)](/wiki/static-testing)** 的关键目标是：
  - **及早发现缺陷**：在动态测试开始前，检测文档、代码或设计中的问题。
  - **提高质量**：通过捕捉后期更难发现的错误，提升软件的整体质量。
  - **降低成本**：在执行代码前捕捉缺陷，降低修复成本，因为后期修复通常更贵。
  - **确保合规**：验证代码是否符合编码标准、指南和监管要求。
  - **促进代码理解**：通过彻底检查帮助开发人员和测试人员理解代码库和设计。
  - **防止缺陷蔓延**：防止缺陷进入后续开发阶段或最终产品。
  - **优化代码**：识别代码优化和重构的机会，以提高性能和可维护性。
  - **增强安全性**：发现可能被利用的安全漏洞。
  - **促进团队合作**：通过评审和检查鼓励协作，实现知识共享。
  - **文档验证**：确保所有必需的文档准确、完整且无歧义。
  通过关注这些目标，**[静态测试 (static testing)](/wiki/static-testing)** 有助于建立更稳健可靠的软件开发生命周期。

#### 技术与方法
- **静态测试中常用的技术有哪些？**
  **[静态测试 (static testing)](/wiki/static-testing)** 中常用的技术包括：
  - **语法检查 (Syntax Checking)**：自动化工具根据编程语言规范检查代码语法。
  - **代码评审 (Code Reviews)**：同行手动检查源码，识别缺陷、执行编码标准并共享知识。
  - **结对编程 (Pair Programming)**：两名开发人员在一台工作站工作，一人写代码，另一人实时评审。
  - **模型 [验证 (Verification)](/wiki/verification)**：确保系统模型遵循规则和约定。
  - **文档评审 (Document Reviews)**：检查需求规范、设计文档、**[测试计划 (test plans)](/wiki/test-plan)** 和用户手册。
  - **静态分析工具 (Static Analysis Tools)**：分析代码而不执行，查找安全漏洞、死代码和内存泄漏。
  - **Linter 工具**：检查源代码的风格错误、编程错误和可疑结构。
  - **形式化方法 (Formal Methods)**：用于指定和验证不同抽象层级软件的数学方法。
  - **桌面检查 (Desk Checking)**：开发人员通过模拟执行来手动检查自己的代码。
  - **控制流分析 (Control Flow Analysis)**：检查程序流程，确保控制结构被正确使用。
  - **数据流分析 (Data Flow Analysis)**：分析代码中的数据流，检测未初始化变量或不可达代码。
  - **接口分析 (Interface Analysis)**：确保模块、函数或系统间的接口定义和使用正确。
  - **合规性检查 (Compliance Checking)**：验证代码是否遵循行业标准和法规。
  每种技术针对 **[软件质量 (software quality)](/wiki/software-quality)** 的不同方面，结合使用可实现全面的 **[静态测试 (static testing)](/wiki/static-testing)** 覆盖。

- **静态测试中的走查、检查和评审有何区别？**
  **走查 (Walkthroughs)**、**[检查 (inspections)](/wiki/inspection)** 和评审都是 **[静态测试 (static testing)](/wiki/static-testing)** 的方法：
  - **走查 (Walkthroughs)**：非正式会议，由制品（代码或设计）作者向同行展示以获取反馈，旨在增进理解并发现异常。
  - **检查 (Inspections)**：比走查更正式，涉及彻底检查。由主持人（非作者）领导，遵循定义的过程（包括读者、检查员等角色），重点在于缺陷检测，通常有后续跟进会议。
  - **评审 (Reviews)**：广义术语，涵盖走查和 **[检查 (inspections)](/wiki/inspection)**。可以是正式或非正式的，旨在查找缺陷、确保符合标准并评估质量。
  本质上，走查是教育和头脑风暴，而 **[检查 (inspections)](/wiki/inspection)** 是正式的寻错会议。这些方法在 **[静态测试 (static testing)](/wiki/static-testing)** 中都起着提升 **[软件质量 (software quality)](/wiki/software-quality)** 的作用，防止问题进入 **[动态测试 (dynamic testing)](/wiki/dynamic-testing)**。

- **什么是静态代码分析？**
  **静态代码分析** 是在执行前对源代码进行的自动化检查，以识别潜在漏洞、**[Bug (bugs)](/wiki/bug)** 和违背编码标准的情况。与需要执行代码的 **[动态测试 (dynamic testing)](/wiki/dynamic-testing)** 不同，它不运行程序。它是白盒测试的一种形式，工具扫描整个代码库以检测安全漏洞、内存泄漏、并发问题和其他可能导致性能差、崩溃或被入侵的问题。
  工具通常集成到 IDE 或构建环境中。
  **关键益处**：
  - **早期 [Bug (bug)](/wiki/bug) 检测**：在运行时前识别问题。
  - **改进代码质量**：确保遵循标准。
  - **安全性保证**：揭示安全漏洞。
  - **降低成本**：及早捕捉 Bug 降低修复成本。
  **示例工具**：
  - **SonarQube**：扫描 Bug、漏洞和异味 (Code Smells)。
  - **Fortify**：专注于安全问题。
  - **ESLint**：JavaScript 的插件化 Lint 工具。
  应通过 CI 流水线自动运行以提供即时反馈。

- **如何在软件开发的早期阶段执行静态测试？**
  早期阶段的 **[静态测试 (Static testing)](/wiki/static-testing)** 不涉及代码执行。执行方式如下：
  - **评审需求**：确保清晰、完整和可测试，识别歧义。
  - **进行同行评审**：开发人员相互查看代码提交，捕捉缺陷。
  - **使用静态分析工具**：自动扫描源码，查找安全漏洞和代码异味。
  - **执行模型检查**：使用形式化方法验证系统设计。
  - **校对文档**：查找拼写、语法错误和不一致。
  这种主动的方法有助于在问题变得昂贵且耗时之前解决它们。

- **用于静态测试的工具有哪些？**
  **[静态测试 (Static testing)](/wiki/static-testing)** 工具分类如下：
  - **代码 Linter 和格式化工具**：`ESLint`, `JSHint`, `Pylint`, `StyleCop`（识别编程错误、Bug 和可疑结构）。
  - **静态分析工具**：`SonarQube`, `Coverity`, `Fortify`, `Checkmarx`（检测漏洞、异味和 Bug）。
  - **IDE 插件**：`Eclipse`, `Visual Studio`, `IntelliJ IDEA` 及其内置分析功能。
  - **代码评审工具**：`Gerrit`, `Review Board`, `Phabricator`, `Crucible`。
  - **文档工具**：`Doxygen`, `Javadoc`, `Sphinx`。
  - **度量和复杂度分析器**：`CodeClimate`, `NDepend`。
  这些工具常集成到 `Jenkins`, `Travis CI`, `GitHub Actions` 等 CI 流水线中，使 **[静态测试 (static testing)](/wiki/static-testing)** 自动化。

#### 实施与执行
- **静态测试过程涉及哪些步骤？**
  **[静态测试 (Static testing)](/wiki/static-testing)** 包含以下步骤，确保制品在 **[动态测试 (dynamic testing)](/wiki/dynamic-testing)** 前达标：
  1. **计划 (Planning)**：定义范围、目标和策略。识别待评审制品（需求、代码、**[测试用例 (test cases)](/wiki/test-case)** 等）。
  2. **准备 (Preparation)**：收集文档和工具，创建核对表 (Checklists)。
  3. **检查 (Examination)**：通过人工会议、走查或自动分析来评审制品。
  4. **报告 (Reporting)**：记录发现的缺陷、偏差和改进建议。
  5. **修复 (Fixing)**：开发人员纠正检查阶段识别的缺陷。
  6. **再检查 (Re-examination)**：验证问题是否已解决，可能需要重新评审或运行工具。
  7. **跟进 (Follow-up)**：实施过程改进以预防类似问题。
  8. **结束 (Closure)**：制品达标后结束过程，记录成果和教训。
  协作与沟通在整个 **[静态测试 (static testing)](/wiki/static-testing)** 过程中至关重要。

- **如何准备静态测试？**
  准备 **[静态测试 (static testing)](/wiki/static-testing)** 的步骤：
  - **定义范围**：确定待检查的各部分。
  - **收集文档**：包括需求、设计规范、用户故事。
  - **选择技术**：基于项目需求选择代码评审或静态分析等技术。
  - **选择工具**：确定辅助工具。
  - **创建核对表**：引导评审过程，确保一致性。
  - **设置环境**：准备好工具和权限。
  - **培训参与者**：提供准则和工具使用培训。
  - **安排会议/时间**。
  - **沟通预期目标**。
  - **评审以往缺陷**：分析历史数据以调整重点。
  通过周密准备，可以最大化 **[静态测试 (static testing)](/wiki/static-testing)** 的有效性。

- **静态测试参与者的角色和职责是什么？**
  **[静态测试 (static testing)](/wiki/static-testing)** 参与者的角色：
  - **测试人员/分析师**：准备 **[测试用例 (test cases)](/wiki/test-case)** 和核对表，执行测试并查找不一致之处。
  - **开发人员**：参与同行评审，确保代码符合标准和最佳实践。
  - **评审员 (Peers)**：由 **[评审员 (Reviewers)](/wiki/reviewer)** 检查代码、设计、需求中的缺陷，提供反馈。
  - **主持人 (Moderator)**：在正式 **[检查 (inspections)](/wiki/inspection)** 中负责领导系统化评审。
  - **作者 (Authors)**：制品的创建者，负责澄清疑问并在识别问题后进行修改。
  - **[质量保证 (Quality Assurance)](/wiki/quality-assurance) 团队**：确保过程符合标准，对结果进行审计。
  所有参与者间的协作是 **[静态测试 (static testing)](/wiki/static-testing)** 成功的关键。

- **静态测试中面临的常见挑战及如何克服？**
  常见挑战包括：
  - **覆盖范围有限**：可能无法覆盖所有路径。应结合 **[静态测试 (static testing)](/wiki/static-testing)** 与 **[动态测试 (dynamic testing)](/wiki/dynamic-testing)**。
  - **误报/漏报**：工具可能会产生 **[误报 (False Positives)](/wiki/false-positive)** 或漏报。需精炼工具配置并定期评审规则。
  - **代码复杂性**：鼓励编写简洁代码，对复杂部分采用结对编程评审。
  - **工具局限性**：选择合适的工具组合。
  - **抵触情绪**：通过培训展示 **[静态测试 (static testing)](/wiki/static-testing)** 在节省时间和提高质量方面的价值。
  - **与过程集成**：将 **[静态测试 (static testing)](/wiki/static-testing)** 集成到 CI 流水线实现无缝衔接。
  - **理解并处理结果**：需要专业知识解析工具报告。
  - **维护测试套件**：随着代码演进及时更新 **[测试套件 (Test Suites)](/wiki/test-suite)** 和 **[测试用例 (test cases)](/wiki/test-case)**。

- **如何衡量静态测试的有效性？**
  衡量 **[静态测试 (static testing)](/wiki/static-testing)** 有效性的关键指标：
  - **缺陷密度 (Defect Density)**：`defectDensity = numberOfDefects / sizeOfCode`。较低的密度通常指示更高质量。
  - **缺陷检测率 (Defect Detection Rate)**：`defectDetectionRate = (defectsFoundInStaticTesting / totalDefectsFound) * 100`。
  - **质量成本 (Cost of Quality)**：有效的 **[静态测试 (static testing)](/wiki/static-testing)** 应降低因缺陷导致的失败成本。
  - **上市时间 (Time to Market)**：及早抓捕 Bug 可缩短周期。
  - **代码复杂度**：降低复杂度可提高 **[可维护性 (maintainability)](/wiki/maintainability)**。
  - **评审效率 (Review Efficiency)**：`reviewEfficiency = numberOfDefectsFound / hoursSpentReviewing`。
  - **重做百分比**：静态测试后需要重做的代码量。

#### 最佳实践
- **静态测试的最佳实践有哪些？**
  **[静态测试 (static testing)](/wiki/static-testing)** 的最佳实践：
  - **早期集成**：尽早开始以防缺陷蔓延。
  - **定期执行**：伴随每次代码提交运行测试。
  - **全面的规则集**：涵盖从风格到复杂 **[Bug (bugs)](/wiki/bug)** 的各种问题。
  - **定制化分析**：根据项目特定需求调整工具规则和严重性。
  - **同行评审**：结对编程和评审带来不同视角。
  - **文档化**：维护知识库以防问题重复，提升团队学习。
  - **代码标准**：坚持规范以保持一致性。
  - **培训**：让团队掌握工具使用和结果解读。
  - **持续改进**：基于反馈和指标完善过程。
  - **CI/CD 集成**：使之成为构建流水线中不可跳过的一环。
  - **提供可操作的报告**：确保结果明确，协助开发人员决策。

- **如何提高静态测试的效率？**
  提升 **[静态测试 (static testing)](/wiki/static-testing)** 效率的策略：
  - **优先级排序**：针对关键且高风险的代码区域。
  - **实施自动化静态分析工具**：提供连续反馈。
  - **定制分析规则**：减少误报。
  - **集成到 CI/CD**：实现自动检查。
  - **建立知识库**：积累常见问题和方案。
  - **紧密协作**：协助开发人员快速响应报告。
  - **定期完善过程**。
  - **开展团队教育**。
  - **利用同行评审**。
  - **跟踪并分析指标**。

- **静态测试中应避免的常见错误？**
  应避免：
  - **忽视早期介入**：**[静态测试 (Static testing)](/wiki/static-testing)** 越晚开始，代价越大。
  - **覆盖不足**：确保全待评审物料（不只是代码）都得到检查。
  - **团队多样性不足**：不同背景的人能发现不同类型的问题。
  - **跳过准备工作**：核对表和标准是必须的。
  - **忽略非代码制品**：如需求、设计文档。
  - **过度依赖工具**：工具无法捕捉逻辑错误，需结合人工。
  - **缺少跟进**：识别缺陷后必须确保其被解决。
  - **沟通不畅**：反馈应是建设性的。
  - **抵触发现的问题**：关注改进而非批评。

- **如何将静态测试集成到软件开发生命周期？**
  在 SDLC 各阶段集成 **[静态测试 (static testing)](/wiki/static-testing)**：
  1. **需求分析**：评审文档，验证完整性、一致性和可测试性。
  2. **设计阶段**：评审设计规范，使用 UML 检查工具。
  3. **编码阶段**：实施自动分析工具，集成到 IDE。
  4. **代码评审**：正式化同行评审。
  5. **构建与部署**：在 CI/CD 流水线中包含静态检测，不通过则阻止构建。
  6. **测试计划**：评审测试策略、计划和用例。
  7. **维护**：对任何变更持续应用 **[静态测试 (static testing)](/wiki/static-testing)**，确保持续的 **[软件质量 (software quality)](/wiki/software-quality)**。

- **静态测试的行业标准有哪些？**
  **[静态测试 (static testing)](/wiki/static-testing)** 的相关行业标准包括：
  - **ISO/IEC 20246:2019**：提供制品评审的需求和过程指南。
  - **IEEE 1028**：定义评审和审计的标准实践，包括 **[检查 (inspections)](/wiki/inspection)**、走查和技术评审。
  - **MISRA 准则**：适用于嵌入式系统，通过静态分析确保软件安全可靠。
  - **CERT 编码标准**：提供规避常见安全编程错误的规则。
  - **OWASP**：提供 Web 应用安全的静态分析最佳实践和工具。
  - **SANS Top 25**：针对最常见安全 **[Bug (bugs)](/wiki/bug)** 的静态分析建议。
  遵循这些标准有助于维持质量、降低缺陷并确保合规。
