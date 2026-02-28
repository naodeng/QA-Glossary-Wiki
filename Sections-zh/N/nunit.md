# NUnit

<!-- TOC START -->
- [相关术语：](#相关术语：)
  - [另请参阅：](#另请参阅：)
- [关于 NUnit 有疑问吗？](#关于-nunit-有疑问吗？)
  - [基础知识和重要性](#基础知识和重要性)
    - [NUnit 是什么？](#nunit-是什么？)
    - [为什么 NUnit 在软件测试中很重要？](#为什么-nunit-在软件测试中很重要？)
    - [NUnit 的主要特性是什么？](#nunit-的主要特性是什么？)
    - [NUnit 与其他测试框架相比如何？](#nunit-与其他测试框架相比如何？)
  - [安装和设置](#安装和设置)
    - [如何安装 NUnit？](#如何安装-nunit？)
    - [NUnit 有哪些系统要求？](#nunit-有哪些系统要求？)
    - [如何为新项目设置 NUnit？](#如何为新项目设置-nunit？)
    - [NUnit 安装过程中常见的问题有哪些以及如何解决？](#nunit-安装过程中常见的问题有哪些以及如何解决？)
  - [用法和实现](#用法和实现)
    - [如何在 NUnit 中编写基本测试用例？](#如何在-nunit-中编写基本测试用例？)
    - [NUnit 中的断言有哪些不同类型？](#nunit-中的断言有哪些不同类型？)
    - [在 NUnit 中如何对测试进行分组？](#在-nunit-中如何对测试进行分组？)
    - [如何在 NUnit 中运行一组特定的测试？](#如何在-nunit-中运行一组特定的测试？)
    - [NUnit 中的 SetUp 和 TearDown 有什么用？](#nunit-中的-setup-和-teardown-有什么用？)
  - [高级概念](#高级概念)
    - [NUnit 如何处理异常？](#nunit-如何处理异常？)
    - [NUnit 中的参数化测试是什么？](#nunit-中的参数化测试是什么？)
    - [如何在 NUnit 中实现数据驱动测试？](#如何在-nunit-中实现数据驱动测试？)
    - [TestFixture 在 NUnit 中的作用是什么？](#testfixture-在-nunit-中的作用是什么？)
    - [如何将 NUnit 与 Selenium 等其他工具集成以进行 e2e 测试？](#如何将-nunit-与-selenium-等其他工具集成以进行-e2e-测试？)
<!-- TOC END -->

单位

是一个开源的

单元测试

源自 JUnit 的 C# 框架。它有助于在 .NET 中编写和执行测试，例如

单位

-console.exe 用于批处理

测试执行

。

## 相关术语：

- [JUnit Testing](../J/junit-testing.md)
- [Test Framework](../T/test-framework.md)

### 另请参阅：

- [Official Website](https://nunit.org/)
- [Wikipedia](https://en.wikipedia.org/wiki/NUnit)

## 关于 NUnit 有疑问吗？

### 基础知识和重要性

#### NUnit 是什么？

[NUnit](../N/nunit.md) 是一个用于 .NET 语言的开源 **[unit testing](../U/unit-testing.md) 框架**，旨在成为用于编写和运行测试的灵活且用户友好的工具。它是 .NET 基金会的一部分，并因其创建简单和复杂[test cases](../T/test-case.md) 的能力而被广泛使用。
  [NUnit](../N/nunit.md) 中的测试是通过使用属性注释方法来创建的，例如 `[Test]` 表示测试方法，`[TestFixture]` 表示测试类，`[SetUp]` 和 `[TearDown]` 分别表示在每个测试之前和之后运行的方法。 [NUnit](../N/nunit.md) 提供了一组丰富的断言，例如`Assert.AreEqual` 和`Assert.IsTrue`，以验证测试结果。
  要运行一组特定的测试，您可以使用[NUnit](../N/nunit.md) 控制台运行程序中的`--where` 选项，或使用`[Category]` 属性对测试进行分类并相应地过滤它们。 [NUnit](../N/nunit.md) 中的异常处理很简单；您可以使用`Assert.Throws` 方法或`ExpectedException` 属性来预期异常。
  [Parameterized testing](../P/parameterized-testing.md) 通过`[TestCase]` 和`[TestCaseSource]` 等属性得到支持，从而实现数据驱动测试。为了与 [Selenium](../S/selenium.md) 等工具集成，[NUnit](../N/nunit.md) 可以无缝工作，从而允许 [end-to-end testing](../E/end-to-end-testing.md) 场景。
  [NUnit](../N/nunit.md) 的 `[TestFixture]` 属性在指示类包含测试方面起着至关重要的作用，并且还可以用于传递用于使用不同输入运行测试的参数。
  总而言之，[NUnit](../N/nunit.md) 是 .NET 测试生态系统中强大而重要的工具，为有效的[test automation](../T/test-automation.md) 提供了一套全面的功能。

#### 为什么 NUnit 在软件测试中很重要？

[NUnit](../N/nunit.md) 通过提供**灵活且高效的**框架来编写和执行测试，在[software testing](../S/software-testing.md) 中发挥着至关重要的作用。作为 [unit testing](../U/unit-testing.md) 框架，它有助于促进**[Test-Driven Development](../T/test-driven-development.md) (TDD)**，其中测试是在实际代码之前编写的，确保软件组件从一开始就按预期工作。 [NUnit](../N/nunit.md) 的重要性还源于它与**持续集成 (CI)** 系统集成的能力，允许自动构建和测试，从而尽早检测到缺陷和回归。
  此外，[NUnit](../N/nunit.md) 支持**并行[test execution](../T/test-execution.md)**，显着减少运行大量[test suites](../T/test-suite.md) 所需的时间，并向开发人员提供快速反馈。其**可扩展性**允许通过插件进行定制和添加新功能，使其能够适应各种测试需求。 [NUnit](../N/nunit.md) 的 **断言库** 非常全面，使测试人员能够验证各种条件，这对于确保代码质量和功能至关重要。
  在涉及多个开发人员或团队的环境中，[NUnit](../N/nunit.md) 凭借其定义明确的结构和约定，有助于保持测试方法的**一致性**。这种一致性对于理解和维护不同团队成员编写的测试至关重要。通过实施良好的测试实践并提供强大的测试创建平台，[NUnit](../N/nunit.md) 为软件开发中的整体 **[quality assurance](../Q/quality-assurance.md)** 流程做出了重大贡献。

#### NUnit 的主要特性是什么？

[NUnit](../N/nunit.md) 提供了一系列关键功能，使其成为[test automation](../T/test-automation.md) 的强大工具：

- **基于属性的测试配置**：使用 `[Test]`、`[TestCase]` 和 `[TestFixture]` 等属性来表示测试方法和类，可以轻松配置测试。
  - **[Test Cases](../T/test-case.md) 和 [Test Suites](../T/test-suite.md)**：将测试组织到案例和套件中，以实现更好的管理和结构。
  - **断言类**：一套全面的 `Assert` 方法，用于验证测试结果，包括针对不同数据类型和条件的多个重载。
  - **测试[Setup](../S/setup.md) 和拆卸**：在每次测试之前和之后，利用`[SetUp]` 和`[TearDown]` 属性准备和清理[test environment](../T/test-environment.md)。
  - **参数化测试**：使用 `[TestCase]` 和 `[TestCaseSource]` 属性创建使用不同数据集运行的测试。
  - **并行[Test Execution](../T/test-execution.md)**：使用`[Parallelizable]` 属性并行运行测试以减少执行时间。
  - **类别**：使用`[Category]` 属性对测试进行分组，允许根据类别运行选择性测试。
  - **测试过滤**：使用[NUnit](../N/nunit.md) 强大的测试选择语言执行测试子集，该语言允许按名称、类别、属性或其他条件进行过滤。
  - **结果报告**：生成各种格式的详细测试结果报告，包括 XML，可用于进一步分析或与 CI/CD 工具集成。
  - **平台和运行时支持**：兼容多个平台和运行时，包括.NET Core和Mono，支持跨平台测试。
  - **可扩展性**：通过自定义属性、约束和事件侦听器扩展[NUnit](../N/nunit.md)，以根据特定的测试需求进行定制。
  - **与各种 IDE 和 CI 工具集成**：与流行的开发环境和持续集成服务器无缝协作，增强开发工作流程。
  这些功能共同使[test automation](../T/test-automation.md) 工程师能够高效地编写、组织和执行测试，使[NUnit](../N/nunit.md) 成为许多测试场景的多功能选择。

- **基于属性的测试配置**：使用 `[Test]`、`[TestCase]` 和 `[TestFixture]` 等属性来表示测试方法和类，可以轻松配置测试。
  - **[Test Cases](../T/test-case.md) 和 [Test Suites](../T/test-suite.md)**：将测试组织到案例和套件中，以实现更好的管理和结构。
  - **断言类**：一套全面的 `Assert` 方法，用于验证测试结果，包括针对不同数据类型和条件的多个重载。
  - **测试[Setup](../S/setup.md) 和拆卸**：在每次测试之前和之后，利用`[SetUp]` 和`[TearDown]` 属性准备和清理[test environment](../T/test-environment.md)。
  - **参数化测试**：使用 `[TestCase]` 和 `[TestCaseSource]` 属性创建使用不同数据集运行的测试。
  - **并行[Test Execution](../T/test-execution.md)**：使用`[Parallelizable]` 属性并行运行测试以减少执行时间。
  - **类别**：使用`[Category]` 属性对测试进行分组，允许根据类别运行选择性测试。
  - **测试过滤**：使用[NUnit](../N/nunit.md) 强大的测试选择语言执行测试子集，该语言允许按名称、类别、属性或其他标准进行过滤。
  - **结果报告**：生成各种格式的详细测试结果报告，包括 XML，可用于进一步分析或与 CI/CD 工具集成。
  - **平台和运行时支持**：兼容多个平台和运行时，包括.NET Core和Mono，支持跨平台测试。
  - **可扩展性**：通过自定义属性、约束和事件侦听器扩展[NUnit](../N/nunit.md)，以根据特定的测试需求进行定制。
  - **与各种 IDE 和 CI 工具集成**：与流行的开发环境和持续集成服务器无缝协作，增强开发工作流程。

#### NUnit 与其他测试框架相比如何？

[NUnit](../N/nunit.md) 是 .NET 生态系统中流行的测试框架，通常与 **MSTest** 和 **xUnit** 等其他框架进行比较。
  **MSTest** 是 Microsoft 的官方测试框架，与 Visual Studio 紧密集成，为在此 IDE 中工作的开发人员提供流畅的体验。然而，[NUnit](../N/nunit.md) 往往更灵活、功能更丰富，[test cases](../T/test-case.md) 具有更广泛的属性，并且更好地支持参数化测试。 [NUnit](../N/nunit.md)的断言库也被认为更强大。随着时间的推移，MSTest 不断得到改进，但通常被选择是因为它与 Microsoft 堆栈的无缝集成，而不是高级功能。
  **xUnit** 是另一个开源框架，被 .NET 社区中的一些人视为 [NUnit](../N/nunit.md) 的继承者。它引入了一种更现代的测试方法，取消了 [setup](../S/setup.md) 和拆卸，转而使用构造函数和处置方法来进行测试初始化​​和清理。 xUnit 还拥有对异步测试的更好支持，并为[test case](../T/test-case.md) 发现和执行提供了更可扩展的模型。然而，[NUnit](../N/nunit.md) 的广泛使用和熟悉度仍然是许多团队的优势，特别是那些现有 [NUnit](../N/nunit.md) [test suites](../T/test-suite.md) 的团队。
  总之，[NUnit](../N/nunit.md) 在 MSTest 提供的易用性和 xUnit 的现代测试方法之间提供了平衡。它以其灵活性、广泛的断言库以及对数据驱动测试的强大支持而脱颖而出，使其成为许多 .NET 开发人员的可靠选择。然而，这些框架之间的选择通常取决于特定的项目需求、团队熟悉程度和集成要求。

### 安装和设置

#### 如何安装 NUnit？

要安装[NUnit](../N/nunit.md)，您可以使用NuGet Package Manager，这是.NET项目最简单且最常用的方法。请按照下列步骤操作：

1. 在 Visual Studio 中打开您的项目。
  2. 前往
    **解决方案浏览器**
    。

3. 右键单击​​要添加 NUnit 的项目。
  4. 选择
    **管理 NuGet 包**
    。

5. 在 NuGet 包管理器中，单击
    **浏览**
    选项卡。

6. 搜索
    `NUnit`
    。

7. 选择
    `NUnit`
    列表中的包。

8. 单击
    **安装**
    按钮将 NUnit 添加到您的项目中。
  或者，您可以使用程序包管理器控制台安装[NUnit](../N/nunit.md)：

  ```
  Install-Package NUnit -Version 3.x.x
  ```将 `3.x.x` 替换为所需的版本号。
  对于 .NET Core 或 .NET Standard 项目，您还可以使用 `dotnet` CLI：

  ```
  dotnet add package NUnit --version 3.x.x
  ```再次将 `3.x.x` 替换为您要安装的特定版本。
  确保您的项目的目标框架与您正在安装的[NUnit](../N/nunit.md) 版本兼容。安装后，您可以开始使用 [NUnit](../N/nunit.md) 框架编写测试。如果您想在 Visual Studio 的测试资源管理器中运行测试，请记住还安装`NUnit3TestAdapter`。

1. 在 Visual Studio 中打开您的项目。
  2. 前往
    **解决方案浏览器**
    。

3. 右键单击​​要添加 NUnit 的项目。
  4. 选择
    **管理 NuGet 包**
    。

5. 在 NuGet 包管理器中，单击
    **浏览**
    选项卡。

6. 搜索
    `NUnit`
    。

7. 选择
    `NUnit`
    列表中的包。

8. 单击
    **安装**
    按钮将 NUnit 添加到您的项目中。

#### NUnit 有哪些系统要求？

[NUnit](../N/nunit.md) 的系统要求因您使用的版本而异。对于 **[NUnit](../N/nunit.md) 3**，要求如下：

- **.NET Framework**：NUnit 与 .NET Framework 2.0 及更高版本兼容。但是，为了使用最新功能并获得最佳体验，建议使用 .NET Framework 4.5 或更高版本。
  - **.NET Core**：NUnit 支持 .NET Core 1.1 及更高版本，包括用于跨平台测试的 .NET 5 和 6。
  - **Mono** ：要在支持 Mono 的平台上运行，需要 4.6 或更高版本。
  - **操作系统**：NUnit 是跨平台的，可以在 Windows、macOS 和 Linux 上运行。
  - **IDE 支持**：NUnit 可与各种集成开发环境 (IDE) 配合使用，例如 Visual Studio，这需要 NUnit 3 测试适配器进行集成。
  在安装 [NUnit](../N/nunit.md) 之前，请确保您的系统上安装了适当版本的 .NET 平台。对于针对多个框架的项目，请确保所有目标框架都满足最低要求。

  ```
  <ItemGroup>
    <PackageReference Include="NUnit" Version="3.x.x" />
    <PackageReference Include="Microsoft.NET.Test.Sdk" Version="x.x.x" />
    <PackageReference Include="NUnit3TestAdapter" Version="x.x.x" />
  </ItemGroup>
  ```将 `3.x.x` 替换为您要使用的 [NUnit](../N/nunit.md) 的特定版本，并将 `x.x.x` 替换为与您的开发环境兼容的测试 SDK 和测试适配器的版本。

- **.NET Framework**：NUnit 与 .NET Framework 2.0 及更高版本兼容。但是，为了使用最新功能并获得最佳体验，建议使用 .NET Framework 4.5 或更高版本。
  - **.NET Core**：NUnit 支持 .NET Core 1.1 及更高版本，包括用于跨平台测试的 .NET 5 和 6。
  - **Mono** ：要在支持 Mono 的平台上运行，需要 4.6 或更高版本。
  - **操作系统**：NUnit 是跨平台的，可以在 Windows、macOS 和 Linux 上运行。
  - **IDE 支持**：NUnit 可与各种集成开发环境 (IDE) 配合使用，例如 Visual Studio，这需要 NUnit 3 测试适配器进行集成。

#### 如何为新项目设置 NUnit？

要为新项目设置[NUnit](../N/nunit.md)，请执行以下步骤：

1. **在您首选的 IDE（例如 Visual Studio）中创建一个新项目**。
  2. **使用项目的包管理器安装 [NUnit](../N/nunit.md) 框架**。对于 .NET Core 或 .NET 5+ 项目，请在包管理器控制台中使用以下命令：
    或者，对于 .NET Framework 项目或者如果您更喜欢使用 .NET CLI，请使用：

    ```
    Install-Package NUnit
    ```

    ```
    dotnet add package NUnit
    ```

3. **安装[NUnit](../N/nunit.md) 测试适配器**，它允许[test runner](../T/test-runner.md) 执行您的测试。使用以下命令：
    或者，对于 .NET CLI：

    ```
    Install-Package NUnit3TestAdapter
    ```

    ```
    dotnet add package NUnit3TestAdapter
    ```

4. **通过在测试文件顶部添加`using NUnit.Framework;` 指令来引用测试项目中的[NUnit](../N/nunit.md) 框架**。
  5. **创建一个[test class](../T/test-class.md)**并用`[TestFixture]`装饰它。在类内部，定义测试方法并用`[Test]`对其进行注释。
  6. **构建项目**来编译[test cases](../T/test-case.md)。
  7. **使用 IDE 中的测试资源管理器或通过命令行运行测试。对于命令行，导航到您的项目目录并运行：

    ```
    dotnet test
    ```确保您的项目针对 [NUnit](../N/nunit.md) 的兼容框架版本。如果遇到问题，请验证 [NUnit](../N/nunit.md) 和测试适配器版本是否与项目的目标框架兼容。

1. **在您首选的 IDE（例如 Visual Studio）中创建一个新项目**。
  2. **使用项目的包管理器安装 [NUnit](../N/nunit.md) 框架**。对于 .NET Core 或 .NET 5+ 项目，请在包管理器控制台中使用以下命令：
    或者，对于 .NET Framework 项目或者如果您更喜欢使用 .NET CLI，请使用：

    ```
    Install-Package NUnit
    ```

    ```
    dotnet add package NUnit
    ```

3. **安装[NUnit](../N/nunit.md) 测试适配器**，它允许[test runner](../T/test-runner.md) 执行您的测试。使用以下命令：
    或者，对于 .NET CLI：

    ```
    Install-Package NUnit3TestAdapter
    ```

    ```
    dotnet add package NUnit3TestAdapter
    ```

4. **通过在测试文件顶部添加`using NUnit.Framework;` 指令来引用测试项目中的[NUnit](../N/nunit.md) 框架**。
  5. **创建一个[test class](../T/test-class.md)**并用`[TestFixture]`装饰它。在类内部，定义测试方法并用`[Test]`对其进行注释。
  6. **构建项目**来编译[test cases](../T/test-case.md)。
  7. **使用 IDE 中的测试资源管理器或通过命令行运行测试。对于命令行，导航到您的项目目录并运行：

    ```
    dotnet test
    ```

#### NUnit 安装过程中常见的问题有哪些以及如何解决？

[NUnit](../N/nunit.md) 安装过程中的常见问题及其解决方案包括：

- **兼容性问题**：确保[NUnit](../N/nunit.md) 版本与项目中的.NET Framework 版本兼容。如果不匹配，请更新项目的框架或选择兼容的 [NUnit](../N/nunit.md) 版本。
  - **NuGet 包管理器问题**：有时，NuGet 包管理器可能无法按预期工作。尝试使用以下命令清除 NuGet 缓存：
    或重新安装[NUnit](../N/nunit.md) 软件包。

    ```
    nuget locals all -clear
    ```

- **不正确的安装**：[NUnit](../N/nunit.md) 应作为 NuGet 包安装在测试项目中，而不是作为独立应用程序。使用包管理器控制台：
    或 Visual Studio 中的 NuGet 包管理器 GUI。

    ```
    Install-Package NUnit
    ```

- **缺少[NUnit](../N/nunit.md) 测试适配器**：如果没有[NUnit](../N/nunit.md) 测试适配器，Visual Studio 将无法识别或运行您的测试。通过 NuGet 安装它：

    ```
    Install-Package NUnit3TestAdapter
    ```

- **路径问题**：如果全局安装[NUnit](../N/nunit.md)，请确保将[NUnit](../N/nunit.md) 控制台运行程序的路径添加到系统的 PATH 环境变量中。
  - **访问权限**：缺乏适当的访问权限可能会导致安装失败。以管理员身份运行 IDE 或确保您的用户具有必要的权限。
  - **防火墙或防病毒干扰**：有时，防火墙或防病毒设置可能会阻止 [NUnit](../N/nunit.md) 正确安装。暂时禁用这些或为 [NUnit](../N/nunit.md) 添加例外。
  - **安装文件损坏**：如果安装文件损坏，请重新下载 [NUnit](../N/nunit.md) 软件包或使用其他源。
  如果问题仍然存在，请参阅 [NUnit](../N/nunit.md) 文档或社区论坛以获取特定错误消息或故障排除步骤。

- **兼容性问题**：确保[NUnit](../N/nunit.md) 版本与项目中的.NET Framework 版本兼容。如果不匹配，请更新项目的框架或选择兼容的 [NUnit](../N/nunit.md) 版本。
  - **NuGet 包管理器问题**：有时，NuGet 包管理器可能无法按预期工作。尝试使用以下命令清除 NuGet 缓存：
    或重新安装[NUnit](../N/nunit.md) 软件包。

    ```
    nuget locals all -clear
    ```

- **不正确的安装**：[NUnit](../N/nunit.md) 应作为 NuGet 包安装在测试项目中，而不是作为独立应用程序。使用包管理器控制台：
    或 Visual Studio 中的 NuGet 包管理器 GUI。

    ```
    Install-Package NUnit
    ```

- **缺少[NUnit](../N/nunit.md) 测试适配器**：如果没有[NUnit](../N/nunit.md) 测试适配器，Visual Studio 将无法识别或运行您的测试。通过 NuGet 安装它：

    ```
    Install-Package NUnit3TestAdapter
    ```

- **路径问题**：如果全局安装[NUnit](../N/nunit.md)，请确保将[NUnit](../N/nunit.md) 控制台运行程序的路径添加到系统的 PATH 环境变量中。
  - **访问权限**：缺乏适当的访问权限可能会导致安装失败。以管理员身份运行 IDE 或确保您的用户具有必要的权限。
  - **防火墙或防病毒干扰**：有时，防火墙或防病毒设置可能会阻止 [NUnit](../N/nunit.md) 正确安装。暂时禁用这些或为 [NUnit](../N/nunit.md) 添加例外。
  - **安装文件损坏**：如果安装文件损坏，请重新下载 [NUnit](../N/nunit.md) 软件包或使用其他来源。

### 用法和实现

#### 如何在 NUnit 中编写基本测试用例？

要在 [NUnit](../N/nunit.md) 中编写基本的 [test case](../T/test-case.md)，请按照下列步骤操作：

1. **通过使用 `[TestFixture]` 属性标记类来创建 [test class](../T/test-class.md)**。此类将包含您的测试方法。

    ```
    [TestFixture]
    public class CalculatorTests
    {
    }
    ```

2. 通过使用`[Test]` 属性标记方法，在[test class](../T/test-class.md) 中**定义测试方法**。该方法将代表一个单独的[test case](../T/test-case.md)。

    ```
    [Test]
    public void Add_TwoNumbers_ReturnsSum()
    {
    }
    ```

3. **在测试方法内实现测试逻辑**。实例化被测类、执行操作并使用断言来验证预期结果。

    ```
    [Test]
    public void Add_TwoNumbers_ReturnsSum()
    {
        // Arrange
        var calculator = new Calculator();
        int number1 = 5;
        int number2 = 7;
        // Act
        int result = calculator.Add(number1, number2);
        // Assert
        Assert.AreEqual(12, result);
    }
    ```

4. **使用[NUnit](../N/nunit.md) 的[test runner](../T/test-runner.md) 或支持[NUnit](../N/nunit.md) 的集成开发环境(IDE) 运行测试**。 [test runner](../T/test-runner.md) 将执行测试方法并报告结果。
  请记住**保持测试相互隔离**和**独立**。每个测试都应该关注单个行为或场景。如果您需要为每个测试执行常见的[setup](../S/setup.md) 或清理任务，请使用`[SetUp]` 和`[TearDown]` 方法。

1. **通过使用 `[TestFixture]` 属性标记类来创建 [test class](../T/test-class.md)**。此类将包含您的测试方法。

    ```
    [TestFixture]
    public class CalculatorTests
    {
    }
    ```

2. 通过使用`[Test]` 属性标记方法，在[test class](../T/test-class.md) 中**定义测试方法**。该方法将代表一个单独的[test case](../T/test-case.md)。

    ```
    [Test]
    public void Add_TwoNumbers_ReturnsSum()
    {
    }
    ```

3. **在测试方法内实现测试逻辑**。实例化被测类、执行操作并使用断言来验证预期结果。

    ```
    [Test]
    public void Add_TwoNumbers_ReturnsSum()
    {
        // Arrange
        var calculator = new Calculator();
        int number1 = 5;
        int number2 = 7;
        // Act
        int result = calculator.Add(number1, number2);
        // Assert
        Assert.AreEqual(12, result);
    }
    ```

4. **使用[NUnit](../N/nunit.md) 的[test runner](../T/test-runner.md) 或支持[NUnit](../N/nunit.md) 的集成开发环境(IDE) 运行测试**。 [test runner](../T/test-runner.md) 将执行测试方法并报告结果。

#### NUnit 中的断言有哪些不同类型？

[NUnit](../N/nunit.md) 提供各种断言来验证测试结果。这些断言分为：

- **相等断言**：验证两个值是否相等。

    ```
    Assert.AreEqual(expected, actual);
    Assert.AreNotEqual(notExpected, actual);
    ```

- **身份断言**：检查两个对象实例是否相同。

    ```
    Assert.AreSame(expected, actual);
    Assert.AreNotSame(notExpected, actual);
    ```

- **布尔断言**：测试 `true` 或 `false` 条件。

    ```
    Assert.IsTrue(condition);
    Assert.IsFalse(condition);
    ```

- **可为空断言**：确定对象是否为`null`。

    ```
    Assert.IsNull(object);
    Assert.IsNotNull(object);
    ```

- **比较断言**：比较值以确定相对大小。

    ```
    Assert.Greater(value1, value2);
    Assert.GreaterOrEqual(value1, value2);
    Assert.Less(value1, value2);
    Assert.LessOrEqual(value1, value2);
    ```

- **字符串断言**：特定于字符串操作，如包含、匹配等。

    ```
    Assert.AreEqual(expected, actual, ignoreCase, message);
    Assert.Contains(substring, string);
    Assert.StartsWith(substring, string);
    Assert.EndsWith(substring, string);
    Assert.IsMatch(regex, string);
    ```

- **集合断言**：验证集合的各个方面，例如相等性、子集等。

    ```
    Assert.AreEqual(expected, actual, comparer);
    Assert.Contains(object, collection);
    Assert.AllItemsAreInstancesOfType(collection, expectedType);
    Assert.IsSubsetOf(subset, superset);
    ```

- **异常断言**：断言抛出特定类型的异常。

    ```
    Assert.Throws<ExceptionType>(() => { /* code that throws exception */ });
    Assert.DoesNotThrow(() => { /* code that should not throw exception */ });
    ```

- **约束模型**：使用流畅的界面编写断言的更具表现力的方式。

    ```
    Assert.That(actual, Is.EqualTo(expected));
    Assert.That(actual, Is.Not.Null);
    Assert.That(collection, Has.No.Member(item));
    Assert.That(() => { /* code */ }, Throws.TypeOf<ExceptionType>());
    ```这些断言有助于验证被测代码的行为，确保软件按预期运行。

- **相等断言**：验证两个值是否相等。

    ```
    Assert.AreEqual(expected, actual);
    Assert.AreNotEqual(notExpected, actual);
    ```

- **身份断言**：检查两个对象实例是否相同。

    ```
    Assert.AreSame(expected, actual);
    Assert.AreNotSame(notExpected, actual);
    ```

- **布尔断言**：测试 `true` 或 `false` 条件。

    ```
    Assert.IsTrue(condition);
    Assert.IsFalse(condition);
    ```

- **可为空断言**：确定对象是否为`null`。

    ```
    Assert.IsNull(object);
    Assert.IsNotNull(object);
    ```

- **比较断言**：比较值以确定相对大小。

    ```
    Assert.Greater(value1, value2);
    Assert.GreaterOrEqual(value1, value2);
    Assert.Less(value1, value2);
    Assert.LessOrEqual(value1, value2);
    ```

- **字符串断言**：特定于字符串操作，如包含、匹配等。

    ```
    Assert.AreEqual(expected, actual, ignoreCase, message);
    Assert.Contains(substring, string);
    Assert.StartsWith(substring, string);
    Assert.EndsWith(substring, string);
    Assert.IsMatch(regex, string);
    ```

- **集合断言**：验证集合的各个方面，例如相等性、子集等。

    ```
    Assert.AreEqual(expected, actual, comparer);
    Assert.Contains(object, collection);
    Assert.AllItemsAreInstancesOfType(collection, expectedType);
    Assert.IsSubsetOf(subset, superset);
    ```

- **异常断言**：断言抛出特定类型的异常。

    ```
    Assert.Throws<ExceptionType>(() => { /* code that throws exception */ });
    Assert.DoesNotThrow(() => { /* code that should not throw exception */ });
    ```

- **约束模型**：使用流畅的界面编写断言的更具表现力的方式。

    ```
    Assert.That(actual, Is.EqualTo(expected));
    Assert.That(actual, Is.Not.Null);
    Assert.That(collection, Has.No.Member(item));
    Assert.That(() => { /* code */ }, Throws.TypeOf<ExceptionType>());
    ```

#### 在 NUnit 中如何对测试进行分组？

在[NUnit](../N/nunit.md) 中，可以使用**属性** 对测试进行分组，以有效地组织和管理它们。用于分组的主要属性是`[TestFixture]`，它表示包含测试方法的类。在测试装置中，您可以使用 `[Category]` 属性进一步对测试进行分组。
  以下是使用 `[Category]` 对测试进行分组的示例：

  ```
  [TestFixture]
  public class MathTests
  {
      [Test]
      [Category("Addition")]
      public void Add_PositiveNumbers_ReturnsCorrectSum()
      {
          // Test code here
      }
      [Test]
      [Category("Subtraction")]
      public void Subtract_PositiveNumbers_ReturnsCorrectDifference()
      {
          // Test code here
      }
  }
  ```您还可以将多个类别应用于单个测试：

  ```
  [Test]
  [Category("Addition")]
  [Category("Boundary")]
  public void Add_MaxIntValues_ReturnsOverflow()
  {
      // Test code here
  }
  ```要运行特定组的测试，请使用 `--where` 命令行选项以及 `cat` 关键字，后跟类别名称：

  ```
  nunit-console --where "cat == Addition" MyTests.dll
  ```对于更复杂的分组，您可以使用**[NUnit](../N/nunit.md) 的测试选择语言**来包含或排除基于多个类别或其他属性的测试。
  请记住，对测试进行分组有助于根据其类别执行测试子集，这对于在测试期间定位应用程序的特定区域非常有用。它还有助于维护组织良好的[test suite](../T/test-suite.md)。

#### 如何在 NUnit 中运行一组特定的测试？

要在 [NUnit](../N/nunit.md) 中运行一组特定的测试，您可以使用 [NUnit](../N/nunit.md) Console Runner 或适用于 Visual Studio 等 IDE 的 [NUnit](../N/nunit.md) 测试适配器提供的 **测试选择语言** 或 **命令行选项**。
  **使用测试选择语言：**
  [NUnit](../N/nunit.md) 的测试选择语言允许您根据测试的属性（例如名称、类别或自定义属性）选择测试。例如，要按名称运行测试：

  ```
  nunit3-console.exe --where "test==MyNamespace.MyTestClass.MyTestMethod" path\to\test\assembly.dll
  ```要运行属于特定类别的测试：

  ```
  nunit3-console.exe --where "cat==Urgent" path\to\test\assembly.dll
  ```**使用命令行选项：**
  使用 [NUnit](../N/nunit.md) Console Runner 时，您可以通过其完全限定名称指定要运行的测试：

  ```
  nunit3-console.exe --test=MyNamespace.MyTestClass.MyTestMethod path\to\test\assembly.dll
  ```您还可以通过用逗号分隔来运行多个测试：

  ```
  nunit3-console.exe --test=MyNamespace.MyTestClass.MyTestMethod1,MyNamespace.MyTestClass.MyTestMethod2 path\to\test\assembly.dll
  ```**在 Visual Studio 中使用 [NUnit](../N/nunit.md) 测试适配器：**
  如果您使用的是 Visual Studio，则可以使用 **测试资源管理器** 运行一组特定的测试。您可以按名称、结果、持续时间和特征过滤测试。右键单击要运行的测试或测试组，然后选择“**运行**”。
  **注意：** 确保使用 `[Category]` 等属性对您的测试进行正确分组，以便在运行特定测试集时更轻松地进行选择。

#### NUnit 中的 SetUp 和 TearDown 有什么用？

在[NUnit](../N/nunit.md) 中，`SetUp` 和`TearDown` 是定义在`TestFixture` 内每个测试之前和之后运行的方法的属性。
  **`SetUp`** 用于在每次测试运行之前初始化对象或设置状态。这确保每个测试都从已知环境开始，从而潜在地减少测试之间依赖的可能性。

  ```
  [SetUp]
  public void Initialize()
  {
      // Code to set up test environment
  }
  ```另一方面，**`TearDown`** 用于在测试运行后进行清理。这可能涉及释放资源，例如关闭[database](../D/database.md)连接或删除[test data](../T/test-data.md)，以确保不会留下可能影响后续测试的副作用。

  ```
  [TearDown]
  public void Cleanup()
  {
      // Code to clean up after the test
  }
  ```使用`SetUp` 和`TearDown` 有助于保持干净的[test environment](../T/test-environment.md) 并可以防止测试相互干扰，这对于获得准确可靠的测试结果至关重要。当测试不是独立的、共享必须重置的资源或状态时，它们特别有用。但是，重要的是使这些方法尽可能轻量，以尽量减少对整体 [test suite](../T/test-suite.md) 执行时间的影响。

### 高级概念

#### NUnit 如何处理异常？

[NUnit](../N/nunit.md) 使用其内置断言模型处理异常，允许[test automation](../T/test-automation.md) 工程师断言在[test execution](../T/test-execution.md) 期间按预期抛出异常。要验证是否引发了特定异常，可以使用 `Assert.Throws` 方法或其通用对应方法 `Assert.Throws<T>`，其中 `T` 是预期异常的类型。这是一个例子：

  ```
  [Test]
  public void ShouldThrowException()
  {
      Assert.Throws<InvalidOperationException>(() =>
      {
          // Code that should throw the InvalidOperationException
      });
  }
  ```对于需要进一步检查异常的情况，可以通过如下方式捕获：

  ```
  [Test]
  public void ShouldThrowExceptionWithSpecificProperties()
  {
      var ex = Assert.Throws<InvalidOperationException>(() =>
      {
          // Code that should throw the InvalidOperationException
      });
      Assert.That(ex.Message, Is.EqualTo("Expected message"));
  }
  ```如果您希望不会引发异常，可以使用`Assert.DoesNotThrow`：

  ```
  [Test]
  public void ShouldNotThrowException()
  {
      Assert.DoesNotThrow(() =>
      {
          // Code that should not throw any exceptions
      });
  }
  ```[NUnit](../N/nunit.md) 还提供 `ExpectedException` 属性，但它被认为已过时，有利于 `Assert.Throws` 方法，该方法提供更多控制和更好的可读性。通过使用这些断言，您可以确保您的代码不仅在正常条件下正确运行，而且还可以按预期处理错误状态。

#### NUnit 中的参数化测试是什么？

[NUnit](../N/nunit.md) 中的[Parameterized testing](../P/parameterized-testing.md) 允许您使用不同的输入数据集多次运行相同的测试。这种方法对于覆盖广泛的输入组合非常有用，而无需编写多个测试方法。要实现参数化测试，您可以使用`[TestCase]`、`[TestCaseSource]` 或`[ValueSource]` 等属性。
  使用`[TestCase]` 属性，您可以直接在测试方法上指定内联参数。例如：

  ```
  [Test]
  [TestCase(1, 2, 3)]
  [TestCase(3, 3, 6)]
  [TestCase(2, -2, 0)]
  public void AddTest(int a, int b, int expectedSum)
  {
      Assert.AreEqual(expectedSum, Add(a, b));
  }
  ````[TestCaseSource]` 属性允许您定义返回[test cases](../T/test-case.md) 的`IEnumerable` 的单独方法、属性或字段。当您有复杂的数据或需要在多个测试方法之间共享[test data](../T/test-data.md)时，这特别有用。

  ```
  public static IEnumerable<TestCaseData> AddCases
  {
      get
      {
          yield return new TestCaseData(1, 2).Returns(3);
          yield return new TestCaseData(3, 3).Returns(6);
          // More test cases
      }
  }
  [Test, TestCaseSource(nameof(AddCases))]
  public int AddTest(int a, int b)
  {
      return Add(a, b);
  }
  ````[ValueSource]` 属性与`[TestCaseSource]` 类似，但用于向测试方法提供单个参数。
  参数化测试增强了[test coverage](../T/test-coverage.md) 和[maintainability](../M/maintainability.md)，因为它们将测试逻辑与[test data](../T/test-data.md) 分开，从而可以轻松更新和添加[test scenarios](../T/test-scenario.md)。

#### 如何在 NUnit 中实现数据驱动测试？

要在[NUnit](../N/nunit.md) 中实现数据驱动测试，您可以使用`TestCaseSource` 属性来指定[test data](../T/test-data.md) 的源。此源可以是返回 `IEnumerable` 的属性、字段或方法。
  这是一个简洁的例子：

  ```
  [TestFixture]
  public class DataDrivenTests
  {
      public static IEnumerable<TestCaseData> TestData
      {
          get
          {
              yield return new TestCaseData("input1", "expected1");
              yield return new TestCaseData("input2", "expected2");
              // Add more test cases as needed
          }
      }
      [Test, TestCaseSource(nameof(TestData))]
      public void TestMethod(string input, string expected)
      {
          // Arrange & Act
          var actual = SomeFunction(input);
          // Assert
          Assert.AreEqual(expected, actual);
      }
  }
  ```在此示例中，`TestData` 是一个生成 [test cases](../T/test-case.md) 的 `IEnumerable<TestCaseData>`。每个`TestCaseData` 实例代表一组要传递给`TestMethod` 的参数。
  **注意**：确保数据源返回与您的测试方法的参数兼容的对象。 [NUnit](../N/nunit.md) 将使用数据源提供的每组参数调用测试方法。
  对于更复杂的场景，您还可以使用外部数据源，例如 CSV 文件、[databases](../D/database.md) 或 XML 文件。您需要编写一个方法来读取数据并将其转换为 `TestCaseData` 对象。
  请记住保持数据源可维护且易于理解，因为复杂的数据源会使您的测试更难以阅读和调试。

#### TestFixture 在 NUnit 中的作用是什么？

在[NUnit](../N/nunit.md) 中，**TestFixture** 是一个属性，它将类标记为包含测试以及（可选）[setup](../S/setup.md) 或拆卸方法。它充当一组相关测试的容器，并允许在执行测试之前或之后运行任何初始化或清理代码。
  这是 TestFixture 的示例：

  ```
  [TestFixture]
  public class CalculatorTests
  {
      private Calculator _calculator;
      [SetUp]
      public void Init()
      {
          // This code runs before each test
          _calculator = new Calculator();
      }
      [TearDown]
      public void Cleanup()
      {
          // This code runs after each test
          _calculator = null;
      }
      [Test]
      public void Add_WhenCalled_ReturnsSum()
      {
          // Arrange is done in SetUp
          // Act
          int result = _calculator.Add(1, 2);
          // Assert
          Assert.AreEqual(3, result);
      }
      // More tests...
  }
  ```使用**TestFixture**，您可以：

- 按逻辑对测试进行分组。
  - 在多个测试中共享设置和清理代码，减少冗余。
  - 将公共上下文应用于一组测试，这在数据驱动测试中特别有用。
  **TestFixture** 还可以采用参数，允许使用不同的输入运行同一组测试，从而促进[parameterized testing](../P/parameterized-testing.md)。当您想要在各种条件下测试相同的逻辑时，这特别有用。

- 按逻辑对测试进行分组。
  - 在多个测试中共享设置和清理代码，减少冗余。
  - 将公共上下文应用于一组测试，这在数据驱动测试中特别有用。

#### 如何将 NUnit 与 Selenium 等其他工具集成以进行 e2e 测试？

将 **[NUnit](../N/nunit.md)** 与 **[Selenium](../S/selenium.md)** 集成以进行端到端 (e2e) 测试涉及使用 [NUnit](../N/nunit.md) 作为浏览器自动化的 [test runner](../T/test-runner.md) 和 [Selenium](../S/selenium.md)。以下是实现此集成的简明指南：

1. **引用[Selenium](../S/selenium.md) [WebDriver](../W/webdriver.md)**：确保您的项目引用[Selenium](../S/selenium.md) [WebDriver](../W/webdriver.md)。这可以通过 NuGet 包管理器来完成。

    ```
    Install-Package Selenium.WebDriver
    ```

2. **创建[Test Cases](../T/test-case.md)**：使用[NUnit](../N/nunit.md)的注解编写[test cases](../T/test-case.md)。在这些测试中使用 [Selenium](../S/selenium.md) [API](../A/api.md) 与 Web 浏览器进行交互。

    ```
    [TestFixture]
    public class SeleniumTests
    {
        private IWebDriver driver;
        [SetUp]
        public void SetUp()
        {
            // Initialize WebDriver, e.g., ChromeDriver
            driver = new ChromeDriver();
        }
        [Test]
        public void TestExample()
        {
            // Use Selenium to navigate and interact with the browser
            driver.Navigate().GoToUrl("http://example.com");
            Assert.IsTrue(driver.Title.Contains("Example Domain"));
        }
        [TearDown]
        public void TearDown()
        {
            // Cleanup: Close the browser after each test
            driver.Quit();
        }
    }
    ```

3. **运行测试**：使用[NUnit](../N/nunit.md) 的[test runner](../T/test-runner.md) 执行测试。这可以通过命令行、持续集成 (CI) 服务器或支持 [NUnit](../N/nunit.md) 的 IDE 来完成。
  通过执行这些步骤，您可以利用 [NUnit](../N/nunit.md) 的测试功能和 [Selenium](../S/selenium.md) 的浏览器自动化来创建强大的 e2e 测试。请记住正确管理[WebDriver](../W/webdriver.md)实例以避免资源泄漏，并考虑在测试完成后使用`TearDown`属性关闭浏览器。

1. **引用[Selenium](../S/selenium.md) [WebDriver](../W/webdriver.md)**：确保您的项目引用[Selenium](../S/selenium.md) [WebDriver](../W/webdriver.md)。这可以通过 NuGet 包管理器来完成。

    ```
    Install-Package Selenium.WebDriver
    ```

2. **创建[Test Cases](../T/test-case.md)**：使用[NUnit](../N/nunit.md)的注解编写[test cases](../T/test-case.md)。在这些测试中使用 [Selenium](../S/selenium.md) [API](../A/api.md) 与 Web 浏览器进行交互。

    ```
    [TestFixture]
    public class SeleniumTests
    {
        private IWebDriver driver;
        [SetUp]
        public void SetUp()
        {
            // Initialize WebDriver, e.g., ChromeDriver
            driver = new ChromeDriver();
        }
        [Test]
        public void TestExample()
        {
            // Use Selenium to navigate and interact with the browser
            driver.Navigate().GoToUrl("http://example.com");
            Assert.IsTrue(driver.Title.Contains("Example Domain"));
        }
        [TearDown]
        public void TearDown()
        {
            // Cleanup: Close the browser after each test
            driver.Quit();
        }
    }
    ```

3. **运行测试**：使用[NUnit](../N/nunit.md) 的[test runner](../T/test-runner.md) 执行测试。这可以通过命令行、持续集成 (CI) 服务器或支持 [NUnit](../N/nunit.md) 的 IDE 来完成。
