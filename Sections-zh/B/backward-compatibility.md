# 向后兼容性

<!-- TOC START -->
- [有关向后兼容性的问题吗？](#有关向后兼容性的问题吗？)
  - [基础知识和重要性](#基础知识和重要性)
    - [什么是软件向后兼容性？](#什么是软件向后兼容性？)
    - [为什么向后兼容性在软件开发中很重要？](#为什么向后兼容性在软件开发中很重要？)
    - [不保持向后兼容性的潜在后果是什么？](#不保持向后兼容性的潜在后果是什么？)
    - [向后兼容性如何影响用户体验？](#向后兼容性如何影响用户体验？)
    - [流行软件中向后兼容的一些例子有哪些？](#流行软件中向后兼容的一些例子有哪些？)
  - [实施和挑战](#实施和挑战)
    - [开发软件时确保向后兼容性的步骤有哪些？](#开发软件时确保向后兼容性的步骤有哪些？)
    - [保持向后兼容性时面临哪些常见挑战？](#保持向后兼容性时面临哪些常见挑战？)
    - [软件开发人员如何在引入新功能和保持向后兼容性之间取得平衡？](#软件开发人员如何在引入新功能和保持向后兼容性之间取得平衡？)
    - [保持向后兼容性的最佳实践是什么？](#保持向后兼容性的最佳实践是什么？)
    - [自动化测试如何帮助确保向后兼容性？](#自动化测试如何帮助确保向后兼容性？)
  - [案例研究和现实世界的例子](#案例研究和现实世界的例子)
    - [您能否提供一个因缺乏向后兼容性而导致用户不满意的案例研究？](#您能否提供一个因缺乏向后兼容性而导致用户不满意的案例研究？)
    - [Microsoft 或 Apple 等主要软件公司如何处理向后兼容性？](#microsoft-或-apple-等主要软件公司如何处理向后兼容性？)
    - [成功实现向后兼容性的一些实际示例有哪些？](#成功实现向后兼容性的一些实际示例有哪些？)
    - [您能否提供一个示例，说明软件必须在新功能上做出妥协才能保持向后兼容性？](#您能否提供一个示例，说明软件必须在新功能上做出妥协才能保持向后兼容性？)
    - [具有强大的向后兼容性策略的软件示例有哪些？](#具有强大的向后兼容性策略的软件示例有哪些？)
<!-- TOC END -->

向后兼容性

，在上下文中

软件测试

，是指软件应用程序或系统与其早期版本有效运行或与较旧的输入数据格式、配置或硬件正确连接的能力。本质上，当软件产品向后兼容时，它可以确保使用旧版本的用户在与新版本交互时不会遇到意外问题或故障

迭代

。测试

向后兼容性

在软件升级或发布过程中，确保引入的更改不会对现有用户产生负面影响或破坏既定功能至关重要。这种做法优先考虑用户体验，确保软件各代之间的无缝过渡和交互。

## 有关向后兼容性的问题吗？

### 基础知识和重要性

#### 什么是软件向后兼容性？

软件中的[Backward compatibility](../B/backward-compatibility.md) 是指系统**与自身的旧版本**交互或与为此类版本设计的输入交互的能力。它确保较新版本的软件可以接受、执行或解释旧版本生成的数据或代码，而不会出现错误或功能丢失。
  对于[test automation](../T/test-automation.md) 工程师来说，[backward compatibility](../B/backward-compatibility.md) 意味着为以前版本设计的自动化测试应该继续适用于新版本。这很重要，因为它允许**连续测试**，而不需要不断更新[test scripts](../T/test-script.md)。
  为了维护[backward compatibility](../B/backward-compatibility.md)，工程师经常：

- 使用
    **版本化[APIs](../A/api.md)**
    以防止更改影响老客户。

- 实施
    **功能切换**
    在不破坏现有功能的情况下逐步引入更改。

- 申请
    **弃用政策**
    给用户和开发人员时间来适应新版本。
  [Automated testing](../A/automated-testing.md) 对于 [backward compatibility](../B/backward-compatibility.md) 通常涉及：

- 运行一个
    **回归测试套件**
    反对新版本。

- 使用
    **虚拟机或容器**
    跨不同环境和版本进行测试。

- 纳入
    **[backward compatibility](../B/backward-compatibility.md) 检查**
    进入 CI/CD 管道。

  ```
  // Example of a simple backward compatibility check in an automated test
  function testBackwardCompatibility(newVersionFunction) {
    const oldVersionResult = oldVersionFunction(input);
    const newVersionResult = newVersionFunction(input);
    assert.equal(newVersionResult, oldVersionResult, 'The function is not backward compatible');
  }
  ```维护[backward compatibility](../B/backward-compatibility.md) 是创新与稳定性之间的**微妙平衡**，需要仔细规划和测试以确保进步不会扰乱现有用户的工作流程。

- 使用
    **版本化[APIs](../A/api.md)**
    以防止更改影响老客户。

- 实施
    **功能切换**
    在不破坏现有功能的情况下逐步引入更改。

- 申请
    **弃用政策**
    给用户和开发人员时间来适应新版本。

- 运行一个
    **回归测试套件**
    反对新版本。

- 使用
    **虚拟机或容器**
    跨不同环境和版本进行测试。

- 纳入
    **[backward compatibility](../B/backward-compatibility.md) 检查**
    进入 CI/CD 管道。

#### 为什么向后兼容性在软件开发中很重要？

[Backward compatibility](../B/backward-compatibility.md) 对于软件开发中的**无缝集成**和**连续性**至关重要。它确保新版本的软件可以与为旧版本设计的数据、接口或系统配合使用，防止用户工作流程中断并保护现有基础设施的投资。
  维护[backward compatibility](../B/backward-compatibility.md) 是对**用户信任**和**产品可靠性**的承诺。它允许用户按照自己的节奏升级软件，而不必担心失去对关键功能或数据的访问。对于企业而言，这意味着避免成本高昂的迁移和再培训，并确保第三方集成和定制解决方案继续发挥作用。
  在[test automation](../T/test-automation.md) 上下文中，[backward compatibility](../B/backward-compatibility.md) 表示[test scripts](../T/test-script.md) 和框架在软件更新后仍保持功能。这对于**持续测试**和**交付管道**至关重要，任何破损都可能导致延误和成本增加。
  开发人员必须仔细管理新功能的引入和旧功能的弃用，通常使用**版本控制**和**弃用警告**来表示更改。 [Automated testing](../A/automated-testing.md)，包括**单元测试**、**集成测试**和**回归测试**，在验证新更新不会破坏现有功能方面发挥着关键作用。
  最终，[backward compatibility](../B/backward-compatibility.md) 是尊重用户现有的环境，同时继续创新。这是一种微妙的平衡，如果处理得当，可以带来**长期用户满意度**和**产品成功**。

#### 不保持向后兼容性的潜在后果是什么？

不维护 [backward compatibility](../B/backward-compatibility.md) 可能会导致一些负面结果：

- **支持成本增加**：使用旧版本的用户可能会遇到需要支持的问题，从而增加帮助台和支持团队的工作量。
  - **碎片**：用户群可能会在不同版本之间变得碎片化，从而使更新和安全补丁的部署变得复杂。
  - **强制升级**：用户可能被迫升级其系统或硬件以运行最新的软件版本，这可能既昂贵又耗时。
  - **集成问题**：第三方集成或依赖系统如果依赖于较旧的 API 或软件版本，则可能会失败，从而可能会中断工作流程和业务运营。
  - **失去信任**：无法升级或选择不升级的用户如果感到被抛弃或被迫进行更改，可能会失去对软件的信任。
  - **数据不兼容性**：新软件版本可能使用不同的数据格式，从而在尝试访问旧数据时导致潜在的数据丢失或损坏。
  - **市场份额减少**：潜在客户可能会选择与其现有基础设施具有更好兼容性的竞争对手的产品。
  - **法律和合规风险**：在某些行业中，由于兼容性问题而无法访问或使用数据可能会导致不遵守监管标准。
  [Automated testing](../A/automated-testing.md) 可以通过验证新软件版本是否与以前版本保持兼容性来减轻这些风险，确保现有功能不受更新影响。

- **支持成本增加**：使用旧版本的用户可能会遇到需要支持的问题，从而增加帮助台和支持团队的工作量。
  - **碎片**：用户群可能会在不同版本之间变得碎片化，从而使更新和安全补丁的部署变得复杂。
  - **强制升级**：用户可能被迫升级其系统或硬件以运行最新的软件版本，这可能既昂贵又耗时。
  - **集成问题**：第三方集成或依赖系统如果依赖于较旧的 API 或软件版本，则可能会失败，从而可能会中断工作流程和业务运营。
  - **失去信任**：无法升级或选择不升级的用户如果感到被抛弃或被迫进行更改，可能会失去对软件的信任。
  - **数据不兼容性**：新软件版本可能使用不同的数据格式，从而在尝试访问旧数据时导致潜在的数据丢失或损坏。
  - **市场份额减少**：潜在客户可能会选择与其现有基础设施具有更好兼容性的竞争对手的产品。
  - **法律和合规风险**：在某些行业中，由于兼容性问题而无法访问或使用数据可能会导致不遵守监管标准。

#### 向后兼容性如何影响用户体验？

[Backward compatibility](../B/backward-compatibility.md) 通过确保软件版本之间的无缝过渡直接影响**用户体验 (UX)**。用户希望他们现有的工作流程、脚本和工具在更新后能够继续运行。当维护[backward compatibility](../B/backward-compatibility.md)时，用户在日常操作中享受**一致性**，避免重新学习或适应不必要的更改的挫败感。
  对于[test automation](../T/test-automation.md) 工程师来说，[backward compatibility](../B/backward-compatibility.md) 意味着[test scripts](../T/test-script.md) 在多个软件版本上保持**有效**和**可靠**。这种稳定性减少了对持续脚本维护的需求，使工程师能够专注于增强[test coverage](../T/test-coverage.md)或探索新功能。
  但是，当[backward compatibility](../B/backward-compatibility.md) 未保留时，用户可能会面临**中断**。他们可能需要**更新**或**重写**脚本、配置或集成，从而导致**停机**并降低生产力。在极端情况下，用户甚至可能被迫**放弃**该软件，寻求替代方案来兑现他们在[setup](../S/setup.md)和培训方面的现有投资。
  维护[backward compatibility](../B/backward-compatibility.md) 是对用户信任和满意度的**承诺**，确保新功能的引入不会以牺牲现有功能为代价。这是一种微妙的平衡，一旦实现，就会产生积极的用户体验，培养软件的**忠诚度**和**长期采用**。

#### 流行软件中向后兼容的一些例子有哪些？

流行软件中[backward compatibility](../B/backward-compatibility.md)的示例：

- **Microsoft Windows**：新版本通常支持为旧版本设计的应用程序。例如，Windows 10 无需修改即可运行许多 Windows 7 应用程序。
  - **Java 运行时环境 (JRE)**：在旧版本上编译的 Java 应用程序通常在较新的 JRE 上运行，因为 Java 的发展遵循 [backward compatibility](../B/backward-compatibility.md)。
  - **Python 2 到 Python 3**：虽然 Python 3 引入了重大更改，但 `2to3` 等工具和 `six` 等兼容性库有助于维护两个版本之间的桥梁。
  - **Adobe Photoshop**：新版本通常可以打开旧版本创建的文件，保留用户工作流程。
  - **Apple macOS**：尽管架构发生了变化，macOS 仍包含 Rosetta 2 等功能，允许为英特尔处理器编译的软件在 Apple Silicon 上运行。
  - **[SQL](../S/sql.md) 服务器**：Microsoft 的[database](../D/database.md) 服务器保持兼容性级别，允许旧版本的[databases](../D/database.md) 恢复或附加到较新版本的[SQL](../S/sql.md) 服务器。
  - **WordPress**：CMS 确保插件和主题通常与新版本兼容，从而在更新后保护用户的网站功能。
  - **HTTP/2**：设计为向后兼容 HTTP/1.1，使客户端和服务器能够支持这两种协议。
  - **USB 标准**：较新的 USB 版本通常设计用于与以前的 [iterations](../I/iteration.md) 中的设备和电缆配合使用，确保用户硬件投资保持有效。
  - **游戏机**：某些游戏机（例如 PlayStation 5）提供 [backward compatibility](../B/backward-compatibility.md) 前几代游戏，保护用户的游戏库投资。
  - **Microsoft Windows**：新版本通常支持为旧版本设计的应用程序。例如，Windows 10 无需修改即可运行许多 Windows 7 应用程序。
  - **Java 运行时环境 (JRE)**：在旧版本上编译的 Java 应用程序通常在较新的 JRE 上运行，因为 Java 的发展遵循 [backward compatibility](../B/backward-compatibility.md)。
  - **Python 2 到 Python 3**：虽然 Python 3 引入了重大更改，但 `2to3` 等工具和 `six` 等兼容性库有助于维护两个版本之间的桥梁。
  - **Adobe Photoshop**：新版本通常可以打开旧版本创建的文件，保留用户工作流程。
  - **Apple macOS**：尽管架构发生了变化，macOS 仍包含 Rosetta 2 等功能，允许为英特尔处理器编译的软件在 Apple Silicon 上运行。
  - **[SQL](../S/sql.md) 服务器**：Microsoft 的[database](../D/database.md) 服务器保持兼容性级别，允许将旧版本的[databases](../D/database.md) 恢复或附加到较新版本的[SQL](../S/sql.md) 服务器。
  - **WordPress**：CMS 确保插件和主题通常与新版本兼容，从而在更新后保护用户的网站功能。
  - **HTTP/2**：设计为向后兼容 HTTP/1.1，使客户端和服务器能够支持这两种协议。
  - **USB 标准**：较新的 USB 版本通常设计用于与以前的[iterations](../I/iteration.md) 中的设备和电缆配合使用，确保用户硬件投资保持有效。
  - **游戏机**：某些游戏机（例如 PlayStation 5）提供 [backward compatibility](../B/backward-compatibility.md) 前几代游戏，保护用户的游戏库投资。

### 实施和挑战

#### 开发软件时确保向后兼容性的步骤有哪些？

要在开发软件时确保 [backward compatibility](../B/backward-compatibility.md)，请按照以下步骤操作：

1. **定义兼容性规则**：清楚地概述您的项目的[backward compatibility](../B/backward-compatibility.md)的构成，包括[API](../A/api.md)合约、数据格式和配置文件。
  2. **版本控制**：使用语义版本控制来传达更改。增量主要版本用于重大更改，次要版本用于向后兼容的新功能，以及 [bug](../B/bug.md) 修复的补丁。
  3. **弃用政策**：在引入影响兼容性的更改时，提供弃用时间表并将其传达给用户。
  4. **[Automated Testing](../A/automated-testing.md)**：实施针对旧版本软件运行的自动回归测试，以确保新更改不会破坏现有功能。
  5. **持续集成 (CI)**：将 [backward compatibility](../B/backward-compatibility.md) 测试集成到 CI 管道中以尽早发现问题。
  6. **功能标志**：使用功能切换逐步推出新功能，允许您在不影响现有功能的情况下禁用它们。
  7. **文档**：保留所有更改的完整文档，包括用户从旧版本过渡的迁移指南。
  8. **用户反馈**：与您的用户社区互动，了解他们的需求以及更改可能如何影响他们。
  9. **旧系统支持**：维护镜像旧系统的[test environment](../T/test-environment.md)以确保兼容性。
  10. **代码审查**：进行彻底的代码审查，重点关注潜在的[backward compatibility](../B/backward-compatibility.md)问题。
  通过遵循这些步骤，您可以最大限度地降低引入重大更改的风险，并为用户维护稳定可靠的软件产品。

1. **定义兼容性规则**：清楚地概述您的项目的[backward compatibility](../B/backward-compatibility.md)的构成，包括[API](../A/api.md)合约、数据格式和配置文件。
  2. **版本控制**：使用语义版本控制来传达更改。增量主要版本用于重大更改，次要版本用于向后兼容的新功能，以及 [bug](../B/bug.md) 修复的补丁。
  3. **弃用政策**：在引入影响兼容性的更改时，提供弃用时间表并将其传达给用户。
  4. **[Automated Testing](../A/automated-testing.md)**：实施针对旧版本软件运行的自动回归测试，以确保新更改不会破坏现有功能。
  5. **持续集成 (CI)**：将 [backward compatibility](../B/backward-compatibility.md) 测试集成到 CI 管道中以尽早发现问题。
  6. **功能标志**：使用功能切换逐步推出新功能，允许您在不影响现有功能的情况下禁用它们。
  7. **文档**：保留所有更改的完整文档，包括用户从旧版本过渡的迁移指南。
  8. **用户反馈**：与您的用户社区互动，了解他们的需求以及更改可能如何影响他们。
  9. **旧系统支持**：维护镜像旧系统的[test environment](../T/test-environment.md)以确保兼容性。
  10. **代码审查**：进行彻底的代码审查，重点关注潜在的[backward compatibility](../B/backward-compatibility.md)问题。

#### 保持向后兼容性时面临哪些常见挑战？

维护[backward compatibility](../B/backward-compatibility.md) 面临着一些挑战：

- **复杂性**：随着软件的发展，代码库变得越来越复杂，使得预测更改将如何与旧版本交互变得更加困难。
  - **测试开销**：确保兼容性需要跨多个版本进行广泛的测试，这可能非常耗时且占用资源。
  - $

    ```
    ```// 示例：多个版本的自动 [test script](../T/test-script.md) 片段
  const 版本 = ['v1.0', 'v1.1', 'v2.0'];
  版本.forEach(版本 => {
  测试(`Ensure feature X works on ${version}`, () => {
  // 测试实现
  });
  });

  ```
  - **Dependency Management**: External libraries or APIs may not maintain their own backward compatibility, forcing updates that could break existing functionality.
  - **Performance**: Backward compatibility layers can introduce performance bottlenecks, as legacy support code may not be optimized for current hardware.
  - **Code Bloat**: Maintaining legacy code can lead to bloated software, as deprecated features must coexist with new ones.
  - **Resource Allocation**: Balancing current development with maintaining old versions can strain resources, potentially slowing down new feature rollouts.
  - **Documentation**: Keeping documentation up-to-date for multiple versions is challenging and can lead to confusion if not managed properly.
  Experienced test automation engineers must navigate these challenges carefully, often employing strategies like feature flags, versioned APIs, and modular architecture to mitigate the risks while ensuring a seamless user experience.
  ```

- **复杂性**：随着软件的发展，代码库变得越来越复杂，使得预测更改将如何与旧版本交互变得更加困难。
  - **测试开销**：确保兼容性需要跨多个版本进行广泛的测试，这可能非常耗时且占用资源。
  - $

    ```
    ```

#### 软件开发人员如何在引入新功能和保持向后兼容性之间取得平衡？

平衡新功能的引入与维护[backward compatibility](../B/backward-compatibility.md) 是软件开发人员的一项关键任务。为了实现这一点，开发人员通常采用**版本控制策略**。语义版本控制 (SemVer) 是一种流行的方法，其中版本号传达有关底层更改的含义。主要版本中的更改表示重大更改，而次要版本和补丁版本分别表示向后兼容的改进和[bug](../B/bug.md)修复。
  开发人员还依靠**弃用政策**来逐步淘汰旧功能。他们将过时的功能标记为已弃用，但在过渡期内保持其功能。这让用户有时间适应新的 [APIs](../A/api.md) 或功能，然后再在未来的主要版本中删除旧的功能。
  **功能标志**或切换开关允许开发人员引入新功能，同时保持旧功能的运行。用户可以在新功能准备就绪时选择加入，从而提供灵活性并保持兼容性。
  **模块化架构**是另一个关键方面。通过将新功能隔离到单独的模块或服务中，核心系统保持稳定，并且兼容性不太可能受到影响。
  **[Automated testing](../A/automated-testing.md)**，包括回归和集成测试，至关重要。它确保新的更改不会破坏现有功能。持续集成 (CI) 系统可以在每次代码提交时自动运行这些测试。
  最后，与用户就变更（尤其是破坏性变更）进行**清晰的沟通**至关重要。提供详细的发行说明和迁移指南可以帮助用户了解更新的影响以及如何相应地调整其系统。
  通过结合这些策略，开发人员可以引入新功能，同时尊重 [backward compatibility](../B/backward-compatibility.md) 的需求。

#### 保持向后兼容性的最佳实践是什么？

维护 [backward compatibility](../B/backward-compatibility.md) 对于最大限度地减少中断并确保用户在软件版本之间顺利过渡至关重要。以下是实现这一目标的最佳实践：

- **遵守语义版本控制**：在进行不兼容的 API 更改时增加主要版本号，以向后兼容的方式添加功能的次要版本，以及向后兼容的错误修复的补丁版本。
  - **使用弃用策略**：逐步淘汰功能。对已弃用的 API 提供警告，并在删除前将其维护一段合理的时间。
  - **利用功能切换**：引入新功能，同时保持旧功能运行，允许用户根据需要进行切换。
  - **维护全面的[test suites](../T/test-suite.md)** ：包括覆盖旧功能的回归测试以捕获重大更改。
  - **细致地记录变更**：保留详细的变更日志，以便用户了解版本之间的修改。
  - **采用强大的[API](../A/api.md)策略**：设计API时考虑到可扩展性，使用开放/封闭原则等原则，其中软件实体应该对扩展开放，但对修改关闭。
  - **隔离遗留系统**：必要时，封装旧代码，防止其干扰新的开发。
  - **利用抽象层**：引入抽象层将新实现与旧接口分开，使它们能够独立发展。
  - **执行[impact analysis](../I/impact-analysis.md)** ：在更改现有功能之前，分析对当前用户的影响以了解更改的范围。
  - **收集用户反馈**：与您的用户社区互动，了解他们对兼容性的需求和担忧。
  通过遵循这些实践，您可以确保您的软件即使在不断发展时仍然可靠且用户友好。

- **遵守语义版本控制**：在进行不兼容的 API 更改时增加主要版本号，以向后兼容的方式添加功能的次要版本，以及向后兼容的错误修复的补丁版本。
  - **使用弃用策略**：逐步淘汰功能。对已弃用的 API 提供警告，并在删除前将其维护一段合理的时间。
  - **利用功能切换**：引入新功能，同时保持旧功能运行，允许用户根据需要进行切换。
  - **维护全面的[test suites](../T/test-suite.md)** ：包括覆盖旧功能的回归测试以捕获重大更改。
  - **细致地记录变更**：保留详细的变更日志，以便用户了解版本之间的修改。
  - **采用强大的[API](../A/api.md)策略**：设计API时考虑到可扩展性，使用开放/封闭原则等原则，其中软件实体应该对扩展开放，但对修改关闭。
  - **隔离遗留系统**：必要时，封装旧代码，防止其干扰新的开发。
  - **利用抽象层**：引入抽象层将新实现与旧接口分开，使它们能够独立发展。
  - **执行[impact analysis](../I/impact-analysis.md)** ：在更改现有功能之前，分析对当前用户的影响以了解更改的范围。
  - **收集用户反馈**：与您的用户社区互动，了解他们对兼容性的需求和担忧。

#### 自动化测试如何帮助确保向后兼容性？

[Automated testing](../A/automated-testing.md) 通过提供系统方法来验证新代码更改不会破坏现有功能，在确保 **[backward compatibility](../B/backward-compatibility.md)** 方面发挥着至关重要的作用。通过实施一整套自动化回归测试，开发人员可以快速识别并解决开发过程中出现的任何兼容性问题。

  ```
  // Example of an automated regression test
  describe('Backward Compatibility Tests', () => {
    it('should work with legacy data formats', () => {
      const legacyData = getLegacyData();
      const result = newSoftwareFunction(legacyData);
      expect(result).toBeCompatibleWithLegacySystems();
    });
  });
  ```可以针对软件的多个版本运行自动化测试，确保新更新与旧版本保持兼容。当处理[APIs](../A/api.md)、数据格式或外部系统依赖一致行为的协议时，这一点尤其重要。
  通过将 [automated testing](../A/automated-testing.md) 集成到 CI/CD 管道中，团队可以在每次构建时持续验证 [backward compatibility](../B/backward-compatibility.md)，使其成为开发工作流程中不可或缺的一部分。这种方法降低了引入重大更改的风险，并有助于维持与依赖软件稳定性的用户的信任。
  此外，可以使用以前软件版本的实际数据和工作流程来设计自动化测试来模拟现实场景。这可确保测试代表用户环境，从而确保[backward compatibility](../B/backward-compatibility.md) 保留在实际[use cases](../U/use-case.md) 中。
  总之，[automated testing](../A/automated-testing.md) 对于维护 [backward compatibility](../B/backward-compatibility.md) 至关重要，它提供了一种主动且有效的方法来防止回归并确保用户在软件更新过程中获得无缝体验。

### 案例研究和现实世界的例子

#### 您能否提供一个因缺乏向后兼容性而导致用户不满意的案例研究？

2018年，**Adobe Photoshop CC 2019**（版本20.0）的发布因**缺少[backward compatibility](../B/backward-compatibility.md)**而引起了用户的极大不满。 Adobe 推出了新功能和改进的 UI，但删除了许多用户依赖的多项旧功能，例如 **保存为 Web** 选项。
  此更改影响了将 Photoshop 集成到其**自动化工作流程**中的用户。依赖于已删除功能的脚本和操作**失败**，导致自动化流程中断。围绕这些功能构建了自定义自动化例程的专业用户发现他们的效率受到了影响。
  立即遭到强烈反对。用户在 Adob​​e 论坛和社交媒体上纷纷抱怨，称工作流程被破坏，需要恢复到旧版本。在这种情况下，Adobe 决定优先考虑新功能而不是[backward compatibility](../B/backward-compatibility.md)，这导致了严重的**用户体验**问题，许多人质疑订阅模式的价值，如果这意味着失去对基本工具的访问权限。
  该事件对软件开发人员来说是一个警示，让他们考虑删除功能的全面影响，特别是当这些功能是用户工作流程不可或缺的一部分时。它还强调了[automated testing](../A/automated-testing.md) 的重要性，其中包括对[backward compatibility](../B/backward-compatibility.md) 的检查，以确保更新不会破坏现有功能。

#### Microsoft 或 Apple 等主要软件公司如何处理向后兼容性？

**微软**和**苹果**等主要软件公司已采取多种策略来接触[backward compatibility](../B/backward-compatibility.md)，通常优先考虑维持稳定的用户群并确保软件版本之间的无缝过渡。
  **Microsoft** 历来非常重视[backward compatibility](../B/backward-compatibility.md)，尤其是其 Windows 操作系统。他们提供广泛的文档和工具，例如**应用程序兼容性工具包 (ACT)**，以帮助开发人员针对新的 Windows 版本测试其应用程序。 Microsoft 还使用 **shims** 或小段代码来拦截 [API](../A/api.md) 调用并重定向或修改它们以与旧软件兼容。
  另一方面，**苹果**采取了更进步的方法，有时牺牲[backward compatibility](../B/backward-compatibility.md)来推动现代化和新技术的采用。例如，在 macOS 中，Apple 引入了**应用程序传输安全性 (ATS)** 作为默认设置，该设置强制执行更严格的安全协议，并破坏了一些不使用安全网络连接的旧应用程序。然而，Apple 提供了详细的指南和工具（如 **Xcode**）来帮助开发人员更新他们的应用程序。
  两家公司都利用**版本控制**和**弃用政策**来通知开发人员即将发生的可能影响[backward compatibility](../B/backward-compatibility.md)的更改。他们还提供一段时期的**旧版支持**，允许用户和开发人员逐渐过渡到新版本。
  [Automated testing](../A/automated-testing.md) 框架对于这些公司测试[backward compatibility](../B/backward-compatibility.md) 至关重要。他们对新软件版本运行一套自动化测试，以确保现有功能不受影响。

#### 成功实现向后兼容性的一些实际示例有哪些？

[backward compatibility](../B/backward-compatibility.md) 的成功案例包括：

- **Java**：Oracle 的 Java 平台以其对 [backward compatibility](../B/backward-compatibility.md) 的坚定承诺而闻名。 Java 运行时环境 (JRE) 允许用旧版本编写的应用程序无需修改即可在最新的 JRE 上运行。
  - **Python 2 到 3**：虽然从 Python 2 到 3 的过渡很重要，但提供了 `2to3` 等工具和 `six` 等兼容性库来帮助维护 [backward compatibility](../B/backward-compatibility.md) 并简化迁移过程。
  - **Windows 操作系统**：Microsoft 确保为旧版本 Windows 开发的应用程序可以继续在新版本上运行。他们使用垫片和兼容模式来实现这一点。
  - **PlayStation 游戏机**：索尼的 PlayStation 2 与 PlayStation 1 游戏兼容，PlayStation 3 最初为 PS1 和 PS2 游戏提供[backward compatibility](../B/backward-compatibility.md)。
  - **HTTP/2**：较新的 HTTP/2 协议使用 HTTP/1.1 维护 [backward compatibility](../B/backward-compatibility.md)。客户端和服务器可以协商要使用的协议版本，确保 Web 服务在不同的 HTTP 版本上继续运行。
  - **[SQL](../S/sql.md) 服务器**：Microsoft [SQL](../S/sql.md) 服务器通过允许在较新版本的[SQL](../S/sql.md) 服务器上恢复旧版本的[databases](../D/database.md) 来维护[backward compatibility](../B/backward-compatibility.md)。
  - **WordPress**：WordPress CMS 通过插件和主题维护[backward compatibility](../B/backward-compatibility.md)，确保核心软件的更新不会破坏现有功能。
  这些示例展示了公司如何优先考虑 [backward compatibility](../B/backward-compatibility.md) 以保护用户投资并确保无缝过渡到较新的软件版本。

- **Java**：Oracle 的 Java 平台以其对 [backward compatibility](../B/backward-compatibility.md) 的坚定承诺而闻名。 Java 运行时环境 (JRE) 允许用旧版本编写的应用程序无需修改即可在最新的 JRE 上运行。
  - **Python 2 到 3**：虽然从 Python 2 到 3 的过渡很重要，但提供了 `2to3` 等工具和 `six` 等兼容性库来帮助维护 [backward compatibility](../B/backward-compatibility.md) 并简化迁移过程。
  - **Windows 操作系统**：Microsoft 确保为旧版本 Windows 开发的应用程序可以继续在新版本上运行。他们使用垫片和兼容模式来实现这一点。
  - **PlayStation 游戏机**：索尼的 PlayStation 2 与 PlayStation 1 游戏兼容，PlayStation 3 最初为 PS1 和 PS2 游戏提供[backward compatibility](../B/backward-compatibility.md)。
  - **HTTP/2**：较新的 HTTP/2 协议使用 HTTP/1.1 维护 [backward compatibility](../B/backward-compatibility.md)。客户端和服务器可以协商要使用的协议版本，确保 Web 服务在不同的 HTTP 版本上继续运行。
  - **[SQL](../S/sql.md) 服务器**：Microsoft [SQL](../S/sql.md) 服务器通过允许在较新版本的[SQL](../S/sql.md) 服务器上恢复旧版本的[databases](../D/database.md) 来维护[backward compatibility](../B/backward-compatibility.md)。
  - **WordPress**：WordPress CMS 通过插件和主题维护[backward compatibility](../B/backward-compatibility.md)，确保核心软件的更新不会破坏现有功能。

#### 您能否提供一个示例，说明软件必须在新功能上做出妥协才能保持向后兼容性？

当然！这是按要求格式化的示例：
  ---
  在**Python 3**的开发过程中，核心团队面临着[backward compatibility](../B/backward-compatibility.md)的重大挑战。 Python 3 引入了许多新功能和改进，但它并不完全向后兼容 Python 2。这是一个经过深思熟虑的决定，旨在清理语言语法并删除冗余的操作方式，这意味着一些较旧的 Python 2 代码将无法在未经修改的情况下在 Python 3 上运行。
  例如，`print` 语句成为一个函数：

  ```
  # Python 2 code
  print "Hello, world!"
  # Python 3 code
  print("Hello, world!")
  ```这一更改提高了语言的一致性和清晰度，但要求开发人员修改现有的 Python 2 代码以保持兼容性。因此，Python 社区不得不在立即采用 Python 3 中的新功能方面做出妥协，以维护现有的代码库。这导致了 Python 2 和 Python 3 都在使用的过渡期延长，Python 2 的生命周期终止日期多次延长，以便有更多的时间进行迁移。
  Python 增强提案 (PEP) 404 正式声明 Python 2.8 永远不会发布，确保不会抱有向后兼容新版本的错误希望。这个例子强调了语言现代化和维护[backward compatibility](../B/backward-compatibility.md)之间的权衡，Python核心团队选择彻底决裂，为未来的创新铺平道路。

#### 具有强大的向后兼容性策略的软件示例有哪些？

多种软件产品以其强大的 [backward compatibility](../B/backward-compatibility.md) 策略而闻名：

- **Microsoft Windows**：Windows 操作系统以保持与旧应用程序的兼容性而闻名，通常允许为早期版本编写的软件在最新的 Windows 版本上运行。
  - **Java 运行时环境 (JRE)**：为旧版本 JRE 编写的 Java 应用程序通常无需修改即可在较新版本上运行，这要归功于 Java 平台对 [backward compatibility](../B/backward-compatibility.md) 的承诺。
  - **Ubuntu LTS 版本**：Ubuntu 的长期支持 (LTS) 版本提供五年更新，并确保针对 LTS 版本的软件在此期间保持兼容。
  - **PostgreSQL**：此[database](../D/database.md) 管理系统因确保较新版本与旧版本创建的[databases](../D/database.md) 保持兼容性而享有盛誉，从而实现无缝升级。
  - **Python 2.7**：尽管Python 3引入了许多更改，但Python 2.7仍保留了较长一段时间，以便为现有Python 2应用程序提供稳定且兼容的平台。
  - **企业软件（SAP、Oracle）**：企业软件供应商经常强调[backward compatibility](../B/backward-compatibility.md)，以确保其大型企业客户可以在不中断业务运营的情况下升级系统。
  这些示例说明了对[backward compatibility](../B/backward-compatibility.md)的承诺，使用户能够从新功能和改进中受益，而无需牺牲运行现有软件的能力。

- **Microsoft Windows**：Windows 操作系统以保持与旧应用程序的兼容性而闻名，通常允许为早期版本编写的软件在最新的 Windows 版本上运行。
  - **Java 运行时环境 (JRE)**：为旧版本 JRE 编写的 Java 应用程序通常无需修改即可在较新版本上运行，这要归功于 Java 平台对 [backward compatibility](../B/backward-compatibility.md) 的承诺。
  - **Ubuntu LTS 版本**：Ubuntu 的长期支持 (LTS) 版本提供五年更新，并确保针对 LTS 版本的软件在此期间保持兼容。
  - **PostgreSQL**：此[database](../D/database.md) 管理系统因确保较新版本与旧版本创建的[databases](../D/database.md) 保持兼容性而享有盛誉，从而实现无缝升级。
  - **Python 2.7**：尽管Python 3引入了许多更改，但Python 2.7仍保留了较长一段时间，以便为现有Python 2应用程序提供稳定且兼容的平台。
  - **企业软件（SAP、Oracle）**：企业软件供应商经常强调[backward compatibility](../B/backward-compatibility.md)，以确保其大型企业客户可以在不中断业务运营的情况下升级系统。
