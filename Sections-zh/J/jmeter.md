# JMeter

<!-- TOC START -->
- [相关术语：](#相关术语：)
  - [另请参阅：](#另请参阅：)
- [关于 JMeter 有疑问吗？](#关于-jmeter-有疑问吗？)
  - [基础知识和重要性](#基础知识和重要性)
    - [什么是 JMeter？](#什么是-jmeter？)
    - [为什么 JMeter 在软件测试中很重要？](#为什么-jmeter-在软件测试中很重要？)
    - [JMeter 的主要功能是什么？](#jmeter-的主要功能是什么？)
    - [JMeter 与其他性能测试工具有何不同？](#jmeter-与其他性能测试工具有何不同？)
    - [JMeter 在 e2e 测试中的作用是什么？](#jmeter-在-e2e-测试中的作用是什么？)
  - [安装和设置](#安装和设置)
    - [如何安装 JMeter？](#如何安装-jmeter？)
    - [JMeter 有哪些系统要求？](#jmeter-有哪些系统要求？)
    - [第一次如何设置 JMeter？](#第一次如何设置-jmeter？)
    - [如何配置 JMeter 以获得最佳性能？](#如何配置-jmeter-以获得最佳性能？)
    - [将 JMeter 升级到新版本的步骤是什么？](#将-jmeter-升级到新版本的步骤是什么？)
  - [使用 JMeter](#使用-jmeter)
    - [如何在 JMeter 中创建基本测试计划？](#如何在-jmeter-中创建基本测试计划？)
    - [JMeter 测试计划中有哪些不同类型的元素？](#jmeter-测试计划中有哪些不同类型的元素？)
    - [如何使用 JMeter 进行负载测试？](#如何使用-jmeter-进行负载测试？)
    - [如何使用 JMeter 进行压力测试？](#如何使用-jmeter-进行压力测试？)
    - [在 JMeter 中记录测试的步骤是什么？](#在-jmeter-中记录测试的步骤是什么？)
    - [如何分析 JMeter 测试的结果？](#如何分析-jmeter-测试的结果？)
  - [高级主题](#高级主题)
    - [如何使用 JMeter 进行分布式测试？](#如何使用-jmeter-进行分布式测试？)
    - [在 JMeter 中编写脚本的最佳实践是什么？](#在-jmeter-中编写脚本的最佳实践是什么？)
    - [如何将 JMeter 与其他测试工具集成？](#如何将-jmeter-与其他测试工具集成？)
    - [JMeter 有哪些限制以及如何克服它们？](#jmeter-有哪些限制以及如何克服它们？)
    - [如何使用 JMeter 进行 Web 服务的性能测试？](#如何使用-jmeter-进行-web-服务的性能测试？)
<!-- TOC END -->

杰米特

，正式名称为 Apache

杰米特

，是由 Apache 软件基金会开发的开源软件应用程序。它是专为

负载测试

以及 Web 应用程序的性能测量，但其功能超出了 Web 协议的范围。

杰米特

允许用户使用并发线程模拟多个用户，向服务器创建各种请求，并分析应用程序在不同负载条件下的性能。

特点

杰米特

包括使用并发线程模拟多个用户的能力、对各种协议（包括 HTTP、FTP、JDBC 等）的支持以及用于设计和可视化的图形界面

测试计划

。其可扩展性允许开发人员和测试人员集成其他插件或编写自定义代码以增强其功能。和

杰米特

，组织可以验证其软件应用程序和基础设施的可扩展性、响应能力和可靠性。

## 相关术语：

- [Performance Testing tool](../P/performance-testing-tool.md)

### 另请参阅：

- [Official Website](https://jmeter.apache.org/)
- [Wikipedia](https://en.wikipedia.org/wiki/Apache_JMeter)

## 关于 JMeter 有疑问吗？

### 基础知识和重要性

#### 什么是 JMeter？

[JMeter](../J/jmeter.md) 是一个开源 Java 应用程序，旨在加载测试功能行为和测量性能。最初是为 Web 应用程序测试而开发的，后来扩展到其他测试功能。 [JMeter](../J/jmeter.md) 模拟一组用户向目标服务器发送请求并返回显示目标服务器/应用程序的性能/功能的统计信息。
  [JMeter](../J/jmeter.md) 的**可扩展性**使其能够支持各种协议，例如 HTTP、HTTPS、FTP、SOAP、JDBC、JMS 和 LDAP。它还可用于测试静态资源（如 JavaScript 和 HTML）以及动态资源（如 AJAX、JSP、Servlet 和 XML）的性能。
  它提供诸如**线程组**来模拟并发用户、**采样器**来定义发送到服务器的请求、**侦听器**用于查看测试结果以及**计时器**等功能来管理请求节奏。 [JMeter](../J/jmeter.md) 还支持通过测试片段进行**模块化**以及使用变量和函数进行动态输入的**参数化**。
  对于**分布式测试**，[JMeter](../J/jmeter.md)可以从单个主控制器控制多个从机，从而实现大规模测试。它还与其他工具和插件集成以增强功能，并可以通过自定义脚本进行扩展。
  [JMeter](../J/jmeter.md)的GUI模式有利于[test plan](../T/test-plan.md)的创建和调试，而非GUI模式则针对[load testing](../L/load-testing.md)进行了优化。它可以使用 [automated testing](../A/automated-testing.md) 环境的命令行模式集成到 CI/CD 管道中。尽管有这些功能，[JMeter](../J/jmeter.md) 并不是浏览器，因此它无法像真正的浏览器一样呈现 HTML 页面，这可能会影响客户端性能指标。

#### 为什么 JMeter 在软件测试中很重要？

[JMeter](../J/jmeter.md) 在[software testing](../S/software-testing.md) 中很重要，因为它在模拟各种用户场景和负载模式方面具有**多功能性**和**可扩展性**。通过使测试人员能够：

- **模拟重负载**
    在服务器、网络和对象上测试强度并分析不同条件下的整体性能。

- **测量应用程序性能**
    关于响应时间、吞吐量和资源利用率等特定性能指标。

- **识别瓶颈**
    通过提供详细的报告和图表，帮助查明可能阻碍大规模绩效的问题。

- **支持持续集成**
    通过与 Jenkins 等工具集成，可以在 CI/CD 管道中进行自动化性能测试。

- **进行各种类型的测试**
    例如负载、压力、功能和回归测试，无需额外的工具。

- **测试不同的协议和服务器类型**
    包括 HTTP、HTTPS、SOAP、REST、FTP 等，这对于 Web 服务和应用程序的全面测试至关重要。

- **促进协作**
    通过利用其开源特性在团队成员之间共享测试计划和结果，确保测试工作的一致性。
  通过利用[JMeter](../J/jmeter.md)，组织可确保其应用程序能够处理预期的用户负载，从而防止潜在的停机并确保流畅的用户体验。这使得 [JMeter](../J/jmeter.md) 成为专注于性能的 [test automation](../T/test-automation.md) 工程师和 [load testing](../L/load-testing.md) 的工具库中不可或缺的工具。

- **模拟重负载**
    在服务器、网络和对象上测试强度并分析不同条件下的整体性能。

- **测量应用程序性能**
    关于响应时间、吞吐量和资源利用率等特定性能指标。

- **识别瓶颈**
    通过提供详细的报告和图表，帮助查明可能阻碍大规模绩效的问题。

- **支持持续集成**
    通过与 Jenkins 等工具集成，可以在 CI/CD 管道中进行自动化性能测试。

- **进行各种类型的测试**
    例如负载、压力、功能和回归测试，无需额外的工具。

- **测试不同的协议和服务器类型**
    包括 HTTP、HTTPS、SOAP、REST、FTP 等，这对于 Web 服务和应用程序的全面测试至关重要。

- **促进协作**
    通过利用其开源特性在团队成员之间共享测试计划和结果，确保测试工作的一致性。

#### JMeter 的主要功能是什么？

[JMeter](../J/jmeter.md) 的主要功能包括：

- **多协议支持**：JMeter 支持各种协议的测试，例如 HTTP、HTTPS、FTP、SOAP、REST 和 TCP。
  - **Visual [Test Plan](../T/test-plan.md) Building**：用户可以使用 GUI 创建测试计划，从而更轻松地设计和修改测试。
  - **记录功能**：JMeter 可以直接从 Web 浏览器记录操作，这简化了测试脚本的创建。
  - **回放和重播**：可以重播测试计划以模拟用户操作和交互。
  - **参数化**：它允许通过CSV文件或其他方式动态输入数据，从而实现数据驱动的测试。
  - **断言**：用户可以添加断言来根据预期结果验证服务器的响应。
  - **可扩展性**：JMeter 可以使用自定义插件进行扩展，并支持与其他工具集成。
  - **计时器**：这些允许模拟请求之间的真实用户思考时间。
  - **可扩展性**：JMeter 可以有效地使用自己的资源来模拟大量用户，并且可以横向扩展以进行分布式测试。
  - **报告**：它提供全面的报告功能，包括用于分析和可视化测试结果的图形、图表和表格。
  - **脚本支持**：JMeter 支持使用各种语言（例如 JavaScript、Groovy）编写高级测试场景的脚本。
  - **关联**：JMeter 可以通过使用正则表达式提取器和其他后处理器来处理动态服务器响应，例如会话 ID。
  这些功能使 [JMeter](../J/jmeter.md) 成为跨不同应用程序和服务的 [performance testing](../P/performance-testing.md) 的多功能且强大的工具。

- **多协议支持**：JMeter 支持各种协议的测试，例如 HTTP、HTTPS、FTP、SOAP、REST 和 TCP。
  - **Visual [Test Plan](../T/test-plan.md) Building**：用户可以使用 GUI 创建测试计划，从而更轻松地设计和修改测试。
  - **记录功能**：JMeter 可以直接从 Web 浏览器记录操作，这简化了测试脚本的创建。
  - **回放和重播**：可以重播测试计划以模拟用户操作和交互。
  - **参数化**：它允许通过CSV文件或其他方式动态输入数据，从而实现数据驱动的测试。
  - **断言**：用户可以添加断言来根据预期结果验证服务器的响应。
  - **可扩展性**：JMeter 可以使用自定义插件进行扩展，并支持与其他工具集成。
  - **计时器**：这些允许模拟请求之间的真实用户思考时间。
  - **可扩展性**：JMeter 可以有效地使用自己的资源来模拟大量用户，并且可以横向扩展以进行分布式测试。
  - **报告**：它提供全面的报告功能，包括用于分析和可视化测试结果的图形、图表和表格。
  - **脚本支持**：JMeter 支持使用各种语言（例如 JavaScript、Groovy）编写高级测试场景的脚本。
  - **关联**：JMeter 可以通过使用正则表达式提取器和其他后处理器来处理动态服务器响应，例如会话 ID。

#### JMeter 与其他性能测试工具有何不同？

[JMeter](../J/jmeter.md) 与其他[performance testing](../P/performance-testing.md) 工具的不同之处主要在于其**开源性质**和**可扩展性**。与许多商业工具不同，[JMeter](../J/jmeter.md) 可以使用自定义插件进行扩展，并得到为其开发做出贡献的大型社区的支持。它旨在满足从 **[load testing](../L/load-testing.md)**、**[stress testing](../S/stress-testing.md)** 到 **[functional testing](../F/functional-testing.md)** 的各种测试需求。
  [JMeter](../J/jmeter.md) 在**多线程框架**上运行，该框架允许多个线程并发采样并模拟服务器上的重负载。这与一些在协议级别模拟负载或使用浏览器模拟来实现更真实负载的工具不同。
  另一个区别是它的**GUI设计**，与一些基于脚本的工具相比，它对于创建[test plans](../T/test-plan.md)更加**用户友好**。然而，这也可能是一个缺点，因为 GUI 可能会消耗更多资源，因此，[JMeter](../J/jmeter.md) 通常在非 GUI 模式下运行，以实现实际的 [load testing](../L/load-testing.md)。
  [JMeter](../J/jmeter.md) **基于Java**，这意味着它**独立于**并且可以在任何支持Java的系统上运行。这与仅限于特定操作系统的工具形成鲜明对比。
  在**协议支持**方面，[JMeter](../J/jmeter.md) 具有 HTTP、HTTPS、FTP、SOAP 和 JDBC 等内置功能。虽然某些工具专门用于网络协议或 [database](../D/database.md) 测试，但 [JMeter](../J/jmeter.md) 提供了广泛的测试功能，无需额外购买或集成。
  最后，[JMeter](../J/jmeter.md) 通过 HTTP(S) [Test Script](../T/test-script.md) 记录器的 **记录功能** 允许测试人员在 Web 浏览器上记录他们的操作，然后从这些操作创建 [test scripts](../T/test-script.md)，这一功能在其他工具中并不总是可用或简单。

#### JMeter 在 e2e 测试中的作用是什么？

在**端到端 (e2e) 测试**中，[JMeter](../J/jmeter.md) 通过模拟用户从开始到结束的旅程，确保整个应用程序（包括其后端服务和[databases](../D/database.md)）在各种条件下按预期运行，发挥着至关重要的作用。虽然 [JMeter](../J/jmeter.md) 主要以负载和 [performance testing](../P/performance-testing.md) 闻名，但它可以在 e2e 测试中利用，以验证系统在实际场景中是否满足性能基准。
  [JMeter](../J/jmeter.md) 可以模拟具有并发会话的多个用户与 Web 应用程序、[APIs](../A/api.md) 和 Web 服务进行交互，这对于 e2e 测试至关重要。它有助于识别可能影响用户体验的瓶颈和性能问题。通过将 [JMeter](../J/jmeter.md) 与持续集成工具（例如 Jenkins）集成，e2e 测试可以自动化并作为部署管道的一部分运行。
  对于 e2e 测试，[JMeter](../J/jmeter.md) 记录浏览器操作的能力特别有用。测试人员可以记录用户与应用程序的交互，然后通过修改来重播它以模拟各种用户行为。可以添加断言来验证响应，确保应用程序按预期运行。
  [JMeter](../J/jmeter.md) 通过插件和脚本的可扩展性允许自定义测试以覆盖复杂的 e2e 场景。但是，需要注意的是，[JMeter](../J/jmeter.md) 不会渲染用户界面，因此它不能取代为基于 UI 的 e2e 测试设计的工具。相反，它通过提供一种测试应用程序在负载下的性能和行为的方法来补充它们，这是全面的端到端测试策略的一个关键方面。

### 安装和设置

#### 如何安装 JMeter？

要安装[JMeter](../J/jmeter.md)，请按照下列步骤操作：

1. **从 Apache [JMeter](../J/jmeter.md) 网站下载**最新的 [JMeter](../J/jmeter.md) 二进制文件。根据您的操作系统选择相关的 zip 或 tgz 文件。
  2. **解压**下载的存档到您选择的目录。
    在 Windows 上，您可以使用 7-Zip 或 WinRAR 等软件来提取文件。
    在基于 Unix 的系统上，您可以使用终端：
    将`<version>` 替换为下载文件的实际版本号。

    ```
    tar -xzf apache-jmeter-<version>.tgz
    ```

3. **验证 Java 安装**：确保您安装了兼容的 Java 版本。 [JMeter](../J/jmeter.md) 需要 Java 8 或更高版本。通过运行以下命令检查您的 Java 版本：
    如果未安装 Java 或版本已过时，请从 Oracle 网站下载并安装相应的 Java JDK 或使用 OpenJDK。

    ```
    java -version
    ```

4. **设置 JAVA_HOME**（可选）：设置`JAVA_HOME` 环境变量以指向您的 Java 安装目录。此步骤是特定于平台的，如果 Java 已在系统的 PATH 中，则可能不需要。
  5. **运行[JMeter](../J/jmeter.md)**：导航到提取的[JMeter](../J/jmeter.md) 文件夹中的`bin` 目录并启动[JMeter](../J/jmeter.md)：
    在 Windows 上，双击`jmeter.bat`。
    在基于 Unix 的系统上，使 `jmeter` shell 脚本可执行并运行它：

    ```
    chmod +x jmeter.sh
    ./jmeter.sh
    ```[JMeter](../J/jmeter.md) 现在应该启动，您可以开始创建 [test plans](../T/test-plan.md)。

1. **从 Apache [JMeter](../J/jmeter.md) 网站下载**最新的 [JMeter](../J/jmeter.md) 二进制文件。根据您的操作系统选择相关的 zip 或 tgz 文件。
  2. **解压**下载的存档到您选择的目录。
    在 Windows 上，您可以使用 7-Zip 或 WinRAR 等软件来提取文件。
    在基于 Unix 的系统上，您可以使用终端：
    将`<version>` 替换为下载文件的实际版本号。

    ```
    tar -xzf apache-jmeter-<version>.tgz
    ```

3. **验证 Java 安装**：确保您安装了兼容的 Java 版本。 [JMeter](../J/jmeter.md) 需要 Java 8 或更高版本。通过运行以下命令检查您的 Java 版本：
    如果未安装 Java 或版本已过时，请从 Oracle 网站下载并安装相应的 Java JDK 或使用 OpenJDK。

    ```
    java -version
    ```

4. **设置 JAVA_HOME**（可选）：设置`JAVA_HOME` 环境变量以指向您的 Java 安装目录。此步骤是特定于平台的，如果 Java 已在系统的 PATH 中，则可能不需要。
  5. **运行[JMeter](../J/jmeter.md)**：导航到提取的[JMeter](../J/jmeter.md) 文件夹中的`bin` 目录并启动[JMeter](../J/jmeter.md)：
    在 Windows 上，双击`jmeter.bat`。
    在基于 Unix 的系统上，使 `jmeter` shell 脚本可执行并运行它：

    ```
    chmod +x jmeter.sh
    ./jmeter.sh
    ```

#### JMeter 有哪些系统要求？

[JMeter](../J/jmeter.md) 是基于 Java 的应用程序，因此它需要有效的 Java 运行时环境 (JRE) 或 Java 开发工具包 (JDK)。截至 2023 年初我所知，运行 [JMeter](../J/jmeter.md) 的系统要求是：

- **Java**：JMeter 5.x 需要 Java 8 或更高版本。建议使用最新版本的 Java，以便从最新的性能和安全改进中受益。
  - **操作系统**：JMeter 基于 Java，可以在任何支持 Java 的操作系统上运行，包括 Windows、Linux 和 macOS。
  - **内存**：默认堆大小对于小型测试可能足够，但对于较大的测试，您可能需要增加堆大小。这可以通过编辑
    `jmeter.bat`
    （对于 Windows）或
    `jmeter`
    （对于 Unix）文件来调整
    `-Xms`
    和
    `-Xmx`
    参数。

- **磁盘空间**：虽然 JMeter 本身不需要太多磁盘空间，但请确保有足够的空间来存储测试结果和日志，特别是在运行大量测试时。
  - **处理器**：更快的CPU可以提高JMeter的性能，特别是在模拟大量并发用户时。
  要调整内存设置，您可以修改[JMeter](../J/jmeter.md)启动脚本中的`JVM_ARGS`变量：

  ```
  JVM_ARGS="-Xms512m -Xmx512m" jmeter.sh
  ```将 `512m` 替换为所需的堆大小。对于分布式测试，请确保集群中的所有节点都满足这些要求并且已正确联网。

- **Java**：JMeter 5.x 需要 Java 8 或更高版本。建议使用最新版本的 Java，以便从最新的性能和安全改进中受益。
  - **操作系统**：JMeter 基于 Java，可以在任何支持 Java 的操作系统上运行，包括 Windows、Linux 和 macOS。
  - **内存**：默认堆大小对于小型测试可能足够，但对于较大的测试，您可能需要增加堆大小。这可以通过编辑
    `jmeter.bat`
    （对于 Windows）或
    `jmeter`
    （对于 Unix）文件来调整
    `-Xms`
    和
    `-Xmx`
    参数。

- **磁盘空间**：虽然 JMeter 本身不需要太多磁盘空间，但请确保有足够的空间来存储测试结果和日志，特别是在运行大量测试时。
  - **处理器**：更快的CPU可以提高JMeter的性能，特别是在模拟大量并发用户时。

#### 第一次如何设置 JMeter？

安装后首次设置[JMeter](../J/jmeter.md)：

1. **启动[JMeter](../J/jmeter.md)**：双击[JMeter](../J/jmeter.md) 安装文件夹的`bin` 目录中的`jmeter.bat` (Windows) 或`jmeter` (Unix) 文件。
  2. **创建[Test Plan](../T/test-plan.md)**：
    - 在 JMeter GUI 中，右键单击
      **[Test Plan](../T/test-plan.md)**
      节点。

- 选择
      **添加 > 线程（用户）> 线程组**
      添加一个新的线程组。

- 在 JMeter GUI 中，右键单击
      **[Test Plan](../T/test-plan.md)**
      节点。

- 选择
      **添加 > 线程（用户）> 线程组**
      添加一个新的线程组。

3. **配置线程组**：
    - 指定线程（用户）数量、启动周期和循环计数。
    - 指定线程（用户）数量、启动周期和循环计数。
  4. **添加采样器**：
    - 右键单击线程组。
    - 选择
      **添加 > 采样器**
      并选择您要测试的请求类型（例如 HTTP 请求）。

- 右键单击​​线程组。
    - 选择
      **添加 > 采样器**
      并选择您要测试的请求类型（例如 HTTP 请求）。

5. **配置采样器**：
    - 输入请求的详细信息，例如服务器名称、端口号和路径。
    - 输入请求的详细信息，例如服务器名称、端口号和路径。
  6. **添加监听器**：
    - 右键单击线程组。
    - 选择
      **添加 > 侦听器**
      添加用于结果分析的侦听器（例如，查看结果树、摘要报告）。

- 右键单击​​线程组。
    - 选择
      **添加 > 侦听器**
      添加用于结果分析的侦听器（例如，查看结果树、摘要报告）。

7. **保存[Test Plan](../T/test-plan.md)**：
    - 前往
      **文件>另存为**
      并保存您的测试计划
      `.jmx`
      扩展。

- 前往
      **文件>另存为**
      并保存您的测试计划
      `.jmx`
      扩展。

8. **运行[Test Plan](../T/test-plan.md)**：
    - 单击
      **开始**
      按钮（绿色播放箭头）或选择
      **运行>开始**
      执行您的测试计划。

- 单击
      **开始**
      按钮（绿色播放箭头）或选择
      **运行>开始**
      执行您的测试计划。

9. **监控结果**：
    - 在测试运行期间或之后查看配置的侦听器中的结果。
    - 在测试运行期间或之后查看配置的侦听器中的结果。
  请记住经常保存您的工作并关闭所有不必要的应用程序，以确保[JMeter](../J/jmeter.md)有足够的资源。如果遇到内存问题，请调整`jmeter.bat` 或`jmeter.sh` 文件中的[JMeter](../J/jmeter.md) 堆大小。

1. **启动[JMeter](../J/jmeter.md)**：双击[JMeter](../J/jmeter.md) 安装文件夹的`bin` 目录中的`jmeter.bat` (Windows) 或`jmeter` (Unix) 文件。
  2. **创建[Test Plan](../T/test-plan.md)**：
    - 在 JMeter GUI 中，右键单击
      **[Test Plan](../T/test-plan.md)**
      节点。

- 选择
      **添加 > 线程（用户）> 线程组**
      添加一个新的线程组。

- 在 JMeter GUI 中，右键单击
      **[Test Plan](../T/test-plan.md)**
      节点。

- 选择
      **添加 > 线程（用户）> 线程组**
      添加一个新的线程组。

3. **配置线程组**：
    - 指定线程（用户）数量、启动周期和循环计数。
    - 指定线程（用户）数量、启动周期和循环计数。
  4. **添加采样器**：
    - 右键单击线程组。
    - 选择
      **添加 > 采样器**
      并选择您要测试的请求类型（例如 HTTP 请求）。

- 右键单击​​线程组。
    - 选择
      **添加 > 采样器**
      并选择您要测试的请求类型（例如 HTTP 请求）。

5. **配置采样器**：
    - 输入请求的详细信息，例如服务器名称、端口号和路径。
    - 输入请求的详细信息，例如服务器名称、端口号和路径。
  6. **添加监听器**：
    - 右键单击线程组。
    - 选择
      **添加 > 侦听器**
      添加用于结果分析的侦听器（例如，查看结果树、摘要报告）。

- 右键单击​​线程组。
    - 选择
      **添加 > 侦听器**
      添加用于结果分析的侦听器（例如，查看结果树、摘要报告）。

7. **保存[Test Plan](../T/test-plan.md)**：
    - 前往
      **文件>另存为**
      并保存您的测试计划
      `.jmx`
      扩展。

- 前往
      **文件>另存为**
      并保存您的测试计划
      `.jmx`
      扩展。

8. **运行[Test Plan](../T/test-plan.md)**：
    - 单击
      **开始**
      按钮（绿色播放箭头）或选择
      **运行>开始**
      执行您的测试计划。

- 单击
      **开始**
      按钮（绿色播放箭头）或选择
      **运行>开始**
      执行您的测试计划。

9. **监控结果**：
    - 在测试运行期间或之后查看配置的侦听器中的结果。
    - 在测试运行期间或之后查看配置的侦听器中的结果。

#### 如何配置 JMeter 以获得最佳性能？

要配置 [JMeter](../J/jmeter.md) 以获得最佳性能，请遵循以下准则：

- 通过调整`jmeter.bat` (Windows) 或`jmeter.sh` (Linux/Mac) 文件中的JVM 设置，为[JMeter](../J/jmeter.md) **分配足够的内存**。使用`-Xms` 和`-Xmx` 参数增加堆大小。例如：

    ```
    HEAP="-Xms512m -Xmx2048m"
    ```

- **在 [test execution](../T/test-execution.md) 期间禁用不必要的侦听器**，因为它们会消耗内存。仅在脚本调试或结果分析期间使用它们。
  - **使用非GUI模式**运行测试，从而减少资源消耗。从命令行执行测试：

    ```
    jmeter -n -t testplan.jmx -l results.jtl
    ```

- **通过在 `Sample Result Save Configuration` 中设置适当的值来减少收集的样本数量**。
  - **使用`Summary Report` 或`Aggregate Report` 等合适的侦听器而不是`View Results in Table` 或`View Results Tree` 来聚合和总结结果**。
  - **如果可能的话，从服务器级计算机运行 [JMeter](../J/jmeter.md)，因为它们拥有更多资源和网络容量。
  - **在进行大规模测试时，将负载分布在多个[JMeter](../J/jmeter.md) 实例上，以避免单台机器过载。
  - **通过使用最有效的脚本元素并避免不必要或复杂的正则表达式来优化您的[test scripts](../T/test-script.md)**。
  - **在`jmeter.properties` 或`user.properties` 文件中配置[JMeter](../J/jmeter.md) 属性**以进行微调，例如控制DNS 缓存、TCP 套接字设置以及[JMeter](../J/jmeter.md) 对示例错误的行为。
  - **监控运行[JMeter](../J/jmeter.md)的机器的资源使用情况**，以确保它不是瓶颈。
  通过执行这些步骤，您可以确保 [JMeter](../J/jmeter.md) 在 [test execution](../T/test-execution.md) 期间配置为实现最佳性能。

- 通过调整`jmeter.bat` (Windows) 或`jmeter.sh` (Linux/Mac) 文件中的JVM 设置，为[JMeter](../J/jmeter.md) **分配足够的内存**。使用`-Xms` 和`-Xmx` 参数增加堆大小。例如：

    ```
    HEAP="-Xms512m -Xmx2048m"
    ```

- **在 [test execution](../T/test-execution.md) 期间禁用不必要的侦听器**，因为它们会消耗内存。仅在脚本调试或结果分析期间使用它们。
  - **使用非GUI模式**运行测试，从而减少资源消耗。从命令行执行测试：

    ```
    jmeter -n -t testplan.jmx -l results.jtl
    ```

- **通过在 `Sample Result Save Configuration` 中设置适当的值来减少收集的样本数量**。
  - **使用`Summary Report` 或`Aggregate Report` 等合适的侦听器而不是`View Results in Table` 或`View Results Tree` 来聚合和总结结果**。
  - **如果可能的话，从服务器级计算机运行 [JMeter](../J/jmeter.md)，因为它们拥有更多资源和网络容量。
  - **在进行大规模测试时，在多个 [JMeter](../J/jmeter.md) 实例之间分配负载**，以避免单台机器过载。
  - **通过使用最有效的脚本元素并避免不必要或复杂的正则表达式来优化您的[test scripts](../T/test-script.md)**。
  - **在`jmeter.properties` 或`user.properties` 文件中配置[JMeter](../J/jmeter.md) 属性**以进行微调，例如控制DNS 缓存、TCP 套接字设置以及[JMeter](../J/jmeter.md) 对示例错误的行为。
  - **监控运行[JMeter](../J/jmeter.md)的机器的资源使用情况**，以确保它不是瓶颈。

#### 将 JMeter 升级到新版本的步骤是什么？

要将 [JMeter](../J/jmeter.md) 升级到较新版本，请按照以下步骤操作：

1. **备份现有[JMeter](../J/jmeter.md) 安装**，包括任何自定义配置、插件、[test plans](../T/test-plan.md) 和用户属性文件。
  2. **从 Apache [JMeter](../J/jmeter.md) 官方网站下载 [JMeter](../J/jmeter.md) 的最新版本**。
  3. **将下载的存档解压**到新目录。避免覆盖旧的 [JMeter](../J/jmeter.md) 安装，以防止任何潜在的数据丢失。
  4. **将您的自定义配置**从备份复制到新安装。这包括对`jmeter.properties`、`user.properties` 和`system.properties` 文件所做的任何更改。
  5. **重新安装您正在使用的任何其他插件**。使用[JMeter](../J/jmeter.md) 插件管理器可以简化流程，或手动将相关`.jar` 文件复制到`lib/ext` 目录。
  6. **迁移[test plans](../T/test-plan.md)**，方法是在新的[JMeter](../J/jmeter.md) 版本中打开它们并保存它们，以确保它们在发生任何更改时与新格式兼容。
  7. **测试现有脚本**以确认它们在新版本中按预期工作。解决 [JMeter](../J/jmeter.md) 功能中的任何弃用或更改。
  8. **查看新版本的发行说明**，了解可能影响您的 [test plans](../T/test-plan.md) 的新功能和更改。
  9. **一旦您确认新版本满足您的所有要求并且所有[test plans](../T/test-plan.md) 均正常运行，请删除旧的[JMeter](../J/jmeter.md) 版本**。
  请记住始终检查版本之间的兼容性问题，尤其是在使用第三方插件或 [JMeter](../J/jmeter.md) 发生重大更改时。

1. **备份现有[JMeter](../J/jmeter.md) 安装**，包括任何自定义配置、插件、[test plans](../T/test-plan.md) 和用户属性文件。
  2. **从 Apache [JMeter](../J/jmeter.md) 官方网站下载 [JMeter](../J/jmeter.md) 的最新版本**。
  3. **将下载的存档解压**到新目录。避免覆盖旧的 [JMeter](../J/jmeter.md) 安装，以防止任何潜在的数据丢失。
  4. **将您的自定义配置**从备份复制到新安装。这包括对`jmeter.properties`、`user.properties` 和`system.properties` 文件所做的任何更改。
  5. **重新安装您正在使用的任何其他插件**。使用[JMeter](../J/jmeter.md) 插件管理器可以简化流程，或者手动将相关`.jar` 文件复制到`lib/ext` 目录。
  6. **迁移[test plans](../T/test-plan.md)**，方法是在新的[JMeter](../J/jmeter.md) 版本中打开它们并保存它们，以确保它们在发生任何更改时与新格式兼容。
  7. **测试现有脚本**以确认它们在新版本中按预期工作。解决 [JMeter](../J/jmeter.md) 功能中的任何弃用或更改。
  8. **查看新版本的发行说明**，了解可能影响您的 [test plans](../T/test-plan.md) 的新功能和更改。
  9. **一旦您确认新版本满足您的所有要求并且所有[test plans](../T/test-plan.md) 均正常运行，请删除旧的[JMeter](../J/jmeter.md) 版本**。

### 使用 JMeter

#### 如何在 JMeter 中创建基本测试计划？

在 [JMeter](../J/jmeter.md) 中创建基本 [test plan](../T/test-plan.md) 涉及以下步骤：

1. **打开[JMeter](../J/jmeter.md)**
    并选择
    `File > New`
    开始新的测试计划。

2. **添加线程组**
    通过右键单击测试计划并选择来添加到您的测试计划
    `Add > Threads (Users) > Thread Group`
    。

3. 配置
    **线程组**
    包括线程（用户）数量、启动周期和循环计数。

4. **添加采样器**
    到线程组。对于 HTTP 测试，右键单击线程组并选择
    `Add > Sampler > HTTP Request`
    。

5. 配置
    **HTTP 请求**
    包含服务器名称、端口号和路径。如有必要，请填写方法（GET、POST 等）和任何参数。

6. **添加监听器**
    到您的测试计划以查看结果。右键单击线程组并选择
    `Add > Listener`
    。常见的听众有
    `View Results Tree`
    和
    `Summary Report`
    。

7. **保存您的[test plan](../T/test-plan.md)**
    使用
    `File > Save`
    以保留您的设置。

8. **运行测试**
    单击绿色开始按钮或选择
    `Run > Start`
    。
  以下是在 [JMeter](../J/jmeter.md) 中添加线程组和 HTTP 请求的示例：

  ```
  <ThreadGroup guiclass="ThreadGroupGui" testclass="ThreadGroup" testname="Thread Group" enabled="true">
    <stringProp name="ThreadGroup.on_sample_error">continue</stringProp>
    <elementProp name="ThreadGroup.main_controller" elementType="LoopController" guiclass="LoopControlPanel" testclass="LoopController" testname="Loop Controller" enabled="true">
      <boolProp name="LoopController.continue_forever">false</boolProp>
      <stringProp name="LoopController.loops">1</stringProp>
    </elementProp>
    <stringProp name="ThreadGroup.num_threads">1</stringProp>
    <stringProp name="ThreadGroup.ramp_time">1</stringProp>
    <boolProp name="ThreadGroup.scheduler">false</boolProp>
  </ThreadGroup>
  <HTTPSamplerProxy guiclass="HttpTestSampleGui" testclass="HTTPSamplerProxy" testname="HTTP Request" enabled="true">
    <elementProp name="HTTPsampler.Arguments" elementType="Arguments" guiclass="HTTPArgumentsPanel" testclass="Arguments" testname="User Defined Variables" enabled="true">
      <collectionProp name="Arguments.arguments"/>
    </elementProp>
    <stringProp name="HTTPSampler.domain">example.com</stringProp>
    <stringProp name="HTTPSampler.port"></stringProp>
    <stringProp name="HTTPSampler.protocol"></stringProp>
    <stringProp name="HTTPSampler.contentEncoding"></stringProp>
    <stringProp name="HTTPSampler.path">/testpath</stringProp>
    <stringProp name="HTTPSampler.method">GET</stringProp>
  </HTTPSamplerProxy>
  ```请记住根据[test scenario](../T/test-scenario.md) 的具体要求定制您的[test plan](../T/test-plan.md)，包括任何必要的断言、cookie、标头或其他元素。

1. **打开[JMeter](../J/jmeter.md)**
    并选择
    `File > New`
    开始新的测试计划。

2. **添加线程组**
    通过右键单击测试计划并选择来添加到您的测试计划
    `Add > Threads (Users) > Thread Group`
    。

3. 配置
    **线程组**
    包括线程（用户）数量、启动周期和循环计数。

4. **添加采样器**
    到线程组。对于 HTTP 测试，右键单击线程组并选择
    `Add > Sampler > HTTP Request`
    。

5. 配置
    **HTTP 请求**
    包含服务器名称、端口号和路径。如有必要，请填写方法（GET、POST 等）和任何参数。

6. **添加监听器**
    到您的测试计划以查看结果。右键单击线程组并选择
    `Add > Listener`
    。常见的听众有
    `View Results Tree`
    和
    `Summary Report`
    。

7. **保存您的[test plan](../T/test-plan.md)**
    使用
    `File > Save`
    以保留您的设置。

8. **运行测试**
    单击绿色开始按钮或选择
    `Run > Start`
    。

#### JMeter 测试计划中有哪些不同类型的元素？

[JMeter](../J/jmeter.md) [test plans](../T/test-plan.md) 由几个定义测试操作和配置的元素组成：

- **线程组**：通过设置线程数、启动周期和循环计数来模拟用户。
  - **采样器**：向服务器执行特定类型的请求（HTTP、FTP、JDBC 等）。
  - **逻辑控制器**：控制请求流，包括 if-then-else 逻辑和循环。
  - **监听器**：以图形、表格或日志等各种格式收集和可视化测试结果。
  - **计时器**：在请求之间引入延迟以模拟真实的用户思考时间。
  - **断言**：根据预期结果验证服务器的响应。
  - **配置元素**：设置采样器的默认值和变量，例如 HTTP 请求默认值或用户定义的变量。
  - **预处理器**：在采样器请求之前执行操作，例如修改请求属性。
  - **后处理器**：在采样器请求后执行操作，例如从响应中提取数据。
  - **WorkBench**：尚未添加到[test plan](../T/test-plan.md) 的元素的临时工作区。
  每个元素都有不同的用途，当组合起来时，它们会创建一个全面的[test scenario](../T/test-scenario.md)。 [Test plans](../T/test-plan.md) 可以保存为`.jmx` 文件以供重复使用和版本控制。

- **线程组**：通过设置线程数、启动周期和循环计数来模拟用户。
  - **采样器**：向服务器执行特定类型的请求（HTTP、FTP、JDBC 等）。
  - **逻辑控制器**：控制请求流，包括 if-then-else 逻辑和循环。
  - **监听器**：以图形、表格或日志等各种格式收集和可视化测试结果。
  - **计时器**：在请求之间引入延迟以模拟真实的用户思考时间。
  - **断言**：根据预期结果验证服务器的响应。
  - **配置元素**：设置采样器的默认值和变量，例如 HTTP 请求默认值或用户定义的变量。
  - **预处理器**：在采样器请求之前执行操作，例如修改请求属性。
  - **后处理器**：在采样器请求后执行操作，例如从响应中提取数据。
  - **WorkBench**：尚未添加到[test plan](../T/test-plan.md) 的元素的临时工作区。

#### 如何使用 JMeter 进行负载测试？

要将[JMeter](../J/jmeter.md) 用于[load testing](../L/load-testing.md)，请按照下列步骤操作：

1. **设计一个[Test Plan](../T/test-plan.md)**：新建一个[test plan](../T/test-plan.md)，添加一个Thread Group来模拟用户数量。配置线程（用户）数量、启动周期和循环计数。
  2. **添加采样器**：在线程组内，添加 HTTP 请求采样器以定义对服务器的请求。配置请求详细信息，例如服务器名称、端口号、路径和请求方法。
  3. **添加监听器**：要查看结果，请将查看结果树、摘要报告或聚合报告等监听器添加到您的[test plan](../T/test-plan.md)。这些将帮助您分析服务器在负载下的性能。
  4. **使用 CSV 进行参数化**：使用 CSV 数据集配置通过不同的用户数据对您的请求进行参数化，以进行更真实的测试。
  5. **添加断言**：包括断言以验证来自服务器的响应，确保负载不会影响功能。
  6. **配置计时器**：添加恒定计时器或高斯随机计时器等计时器来模拟请求之间的思考时间。
  7. **运行测试**：通过单击“运行”按钮执行[test plan](../T/test-plan.md)。使用添加的监听器实时监控测试。
  8. **分析结果**：测试后，查看监听器数据以了解服务器的性能，查找响应时间、吞吐量和错误率等指标。
  9. **调整和重复**：根据分析，根据需要修改[test plan](../T/test-plan.md)以模拟不同的场景或识别性能瓶颈。
  请记住保存您的[test plan](../T/test-plan.md) 和结果以供将来参考或[regression testing](../R/regression-testing.md)。

1. **设计一个[Test Plan](../T/test-plan.md)**：新建一个[test plan](../T/test-plan.md)，添加一个Thread Group来模拟用户数量。配置线程（用户）数量、启动周期和循环计数。
  2. **添加采样器**：在线程组内，添加 HTTP 请求采样器以定义对服务器的请求。配置请求详细信息，例如服务器名称、端口号、路径和请求方法。
  3. **添加监听器**：要查看结果，请将查看结果树、摘要报告或聚合报告等监听器添加到您的[test plan](../T/test-plan.md)。这些将帮助您分析服务器在负载下的性能。
  4. **使用 CSV 进行参数化**：使用 CSV 数据集配置通过不同的用户数据对您的请求进行参数化，以进行更真实的测试。
  5. **添加断言**：包括断言以验证来自服务器的响应，确保负载不会影响功能。
  6. **配置计时器**：添加恒定计时器或高斯随机计时器等计时器来模拟请求之间的思考时间。
  7. **运行测试**：通过单击“运行”按钮执行[test plan](../T/test-plan.md)。使用添加的监听器实时监控测试。
  8. **分析结果**：测试后，查看监听器数据以了解服务器的性能，查找响应时间、吞吐量和错误率等指标。
  9. **调整和重复**：根据分析，根据需要修改[test plan](../T/test-plan.md)以模拟不同的场景或识别性能瓶颈。

#### 如何使用 JMeter 进行压力测试？

要将[JMeter](../J/jmeter.md) 用于[stress testing](../S/stress-testing.md)，请按照下列步骤操作：

1. **设计[Test Plan](../T/test-plan.md)**：创建为您的应用程序进行压力测试而定制的[test plan](../T/test-plan.md)。这涉及定义要应用的负载和要收集的指标。
  2. **添加线程组**：配置具有大量线程（用户）的线程组来模拟压力负载。设置加速时间和测试持续时间以达到并维持所需的应力水平。
  3. **配置采样器**：添加 HTTP 请求采样器或其他相关采样器来复制会给系统带来压力的用户操作，例如提交表单或执行繁重的查询。
  4. **添加监听器**：包括聚合报告、摘要报告或图形结果等监听器，以监控和可视化压力下的性能。
  5. **参数化输入**：使用 CSV 数据集配置或其他参数化方法来改变输入数据，模拟更真实和多样化的应力条件。
  6. **定义断言**：添加断言以在压力下验证响应，确保应用程序保持功能。
  7. **运行测试**：执行[test plan](../T/test-plan.md)并监视应用程序和服务器资源。
  8. **分析结果**：测试后，使用[JMeter](../J/jmeter.md)监听器和外部监控工具分析结果，以识别瓶颈和阈值。
  9. **微调和重复**：根据分析，微调应用程序或基础设施并重复压力测试以验证改进。
  请记住在压力测试期间监控服务器资源（CPU、内存、磁盘 I/O、网络）以识别基础设施限制。在受控环境中使用 [JMeter](../J/jmeter.md) 以避免影响真实用户。

1. **设计[Test Plan](../T/test-plan.md)**：创建一个专门用于对您的应用程序进行压力测试的[test plan](../T/test-plan.md)。这涉及定义要应用的负载和要收集的指标。
  2. **添加线程组**：配置具有大量线程（用户）的线程组来模拟压力负载。设置加速时间和测试持续时间以达到并维持所需的应力水平。
  3. **配置采样器**：添加 HTTP 请求采样器或其他相关采样器来复制会给系统带来压力的用户操作，例如提交表单或执行繁重的查询。
  4. **添加监听器**：包括聚合报告、摘要报告或图形结果等监听器，以监控和可视化压力下的性能。
  5. **参数化输入**：使用 CSV 数据集配置或其他参数化方法来改变输入数据，模拟更真实和多样化的应力条件。
  6. **定义断言**：添加断言以在压力下验证响应，确保应用程序保持功能。
  7. **运行测试**：执行[test plan](../T/test-plan.md)并监视应用程序和服务器资源。
  8. **分析结果**：测试后，使用[JMeter](../J/jmeter.md)监听器和外部监控工具分析结果，以识别瓶颈和阈值。
  9. **微调和重复**：根据分析，微调应用程序或基础设施并重复压力测试以验证改进。

#### 在 JMeter 中记录测试的步骤是什么？

要在 [JMeter](../J/jmeter.md) 中记录测试，请按照下列步骤操作：

1. **打开[JMeter](../J/jmeter.md)**
    并选择
    **[Test Plan](../T/test-plan.md)**
    在左侧面板上。

2. **右键单击**
    在测试计划上并转至
    **添加 > 线程（用户）> 线程组**
    。

3. 在线程组内部，
    **右键单击**
    并导航至
    **添加 > 逻辑控制器 > 录音控制器**
    。

4. 接下来，添加 HTTP(S) 测试脚本记录器以捕获 HTTP 请求。右键单击测试计划并选择
    **添加 > 非测试元素 > HTTP(S) [Test Script](../T/test-script.md) 记录器**
    。

5. 设置
    **端口号**
    用于 HTTP(S) 测试脚本记录器（默认值为 8888）。

6. 配置您的
    **浏览器或应用程序**
    通过将代理服务器设置为来使用 JMeter 代理
    `localhost`
    使用您在录音机设置中指定的端口。

7. 在 JMeter 中，单击
    **开始**
    HTTP(S) 测试脚本记录器上的按钮。 JMeter 现在已准备好进行记录。

8. **与您的网络应用程序交互**
    使用配置的浏览器/应用程序。 JMeter将记录请求和响应并将它们显示在记录控制器下。

9. 完成您要记录的操作后，
    **停止录音**
    在 JMeter 中。

10.你现在可以
    **保存**
    录制的脚本供以后使用或
    **修改**
    根据您的测试计划的需要。
  请记住在记录之前**清除浏览器缓存**，以确保捕获所有请求，并**禁用代理可能无法捕获的特定于浏览器的功能**，例如预取。

1. **打开[JMeter](../J/jmeter.md)**
    并选择
    **[Test Plan](../T/test-plan.md)**
    在左侧面板上。

2. **右键单击**
    在测试计划上并转至
    **添加 > 线程（用户）> 线程组**
    。

3. 在线程组内部，
    **右键单击**
    并导航至
    **添加 > 逻辑控制器 > 录音控制器**
    。

4. 接下来，添加 HTTP(S) 测试脚本记录器以捕获 HTTP 请求。右键单击测试计划并选择
    **添加 > 非测试元素 > HTTP(S) [Test Script](../T/test-script.md) 记录器**
    。

5. 设置
    **端口号**
    用于 HTTP(S) 测试脚本记录器（默认值为 8888）。

6. 配置您的
    **浏览器或应用程序**
    通过将代理服务器设置为来使用 JMeter 代理
    `localhost`
    使用您在录音机设置中指定的端口。

7. 在 JMeter 中，单击
    **开始**
    HTTP(S) 测试脚本记录器上的按钮。 JMeter 现在已准备好进行记录。

8. **与您的网络应用程序交互**
    使用配置的浏览器/应用程序。 JMeter将记录请求和响应并将它们显示在记录控制器下。

9. 完成您要记录的操作后，
    **停止录音**
    在 JMeter 中。

10.你现在可以
    **保存**
    录制的脚本供以后使用或
    **修改**
    根据您的测试计划的需要。

#### 如何分析 JMeter 测试的结果？

分析[JMeter](../J/jmeter.md) 测试结果涉及检查各种指标以评估性能。运行测试后，[JMeter](../J/jmeter.md) 提供了多种查看和解释数据的方法：

1. **侦听器**：将侦听器添加到您的[test plan](../T/test-plan.md) 以捕获结果。常见的听众包括：
    - 总结报告
    - 综合报告
    - 查看结果树
    - 图表结果
    - 响应时间图
    - 总结报告
    - 综合报告
    - 查看结果树
    - 图表结果
    - 响应时间图
  2. **查看结果树**：要获取详细的请求和响应数据，请使用此侦听器。它有助于调试错误，但会占用大量资源；避免在大负载测试期间使用它。
  3. **聚合报告**：提供一个表格，其中包含平均响应时间、最小/最大、吞吐量、错误百分比等指标。对于快速概览性能很有用。
  4. **图形分析**：使用图形直观地表示随时间变化的响应时间、吞吐量和其他指标。有助于识别趋势和峰值。
  5. **导出结果**：将测试结果保存为 CSV 或 XML 格式，以便使用 Excel 或专用软件等外部工具进行进一步分析。
  6. **插件**：使用[JMeter](../J/jmeter.md) 插件管理器等插件扩展[JMeter](../J/jmeter.md) 的分析功能。插件提供高级图表和报告以获取更深入的见解。
  7. **日志文件**：查看 [JMeter](../J/jmeter.md) 日志文件以了解 [test execution](../T/test-execution.md) 期间发生的任何错误或问题。
  8. **自动分析**：将[JMeter](../J/jmeter.md)与Jenkins等持续集成工具集成，以自动运行测试并生成报告。
  9. **关联指标**：交叉引用不同的指标以了解响应时间、吞吐量和错误率之间的关系。
  10. **比较结果**：比较不同测试运行的结果，以确定性能改进或回归。
  对于经验丰富的工程师来说，分析 [JMeter](../J/jmeter.md) 结果意味着识别瓶颈、了解负载下的系统行为以及做出明智的决策以提高应用程序性能。

1. **侦听器**：将侦听器添加到您的[test plan](../T/test-plan.md) 以捕获结果。常见的听众包括：
    - 总结报告
    - 综合报告
    - 查看结果树
    - 图表结果
    - 响应时间图
    - 总结报告
    - 综合报告
    - 查看结果树
    - 图表结果
    - 响应时间图
  2. **查看结果树**：要获取详细的请求和响应数据，请使用此侦听器。它有助于调试错误，但会占用大量资源；避免在大负载测试期间使用它。
  3. **聚合报告**：提供一个表格，其中包含平均响应时间、最小/最大、吞吐量、错误百分比等指标。对于快速概览性能很有用。
  4. **图形分析**：使用图形直观地表示随时间变化的响应时间、吞吐量和其他指标。有助于识别趋势和峰值。
  5. **导出结果**：将测试结果保存为 CSV 或 XML 格式，以便使用 Excel 或专用软件等外部工具进行进一步分析。
  6. **插件**：使用[JMeter](../J/jmeter.md) 插件管理器等插件扩展[JMeter](../J/jmeter.md) 的分析功能。插件提供高级图表和报告以获取更深入的见解。
  7. **日志文件**：查看 [JMeter](../J/jmeter.md) 日志文件以了解 [test execution](../T/test-execution.md) 期间发生的任何错误或问题。
  8. **自动分析**：将[JMeter](../J/jmeter.md)与Jenkins等持续集成工具集成，以自动运行测试并生成报告。
  9. **关联指标**：交叉引用不同的指标以了解响应时间、吞吐量和错误率之间的关系。
  10. **比较结果**：比较不同测试运行的结果，以确定性能改进或回归。

### 高级主题

#### 如何使用 JMeter 进行分布式测试？

要使用 [JMeter](../J/jmeter.md) 进行分布式测试，请按照下列步骤操作：

1. **在所有将充当负载生成器的计算机（称为从节点）上设置 [JMeter](../J/jmeter.md) 环境**。确保所有机器都在同一网络上并且可以相互通信。
  2. **通过编辑`jmeter.properties` 文件来配置主机**（控制器）。找到 `remote_hosts` 属性并列出所有从属节点的 IP 地址，以逗号分隔。

    ```
    remote_hosts=192.168.0.101,192.168.0.102,192.168.0.103
    ```

3. **在所有从属节点上打开所需的端口**，以允许来自主机的传入连接。默认[JMeter](../J/jmeter.md) 端口是`1099`，但可以在`jmeter.properties` 文件中更改。
  4. **通过从 [JMeter](../J/jmeter.md) `bin` 目录运行以下命令，在每个从属节点上启动 [JMeter](../J/jmeter.md) 服务器**：

    ```
    jmeter-server
    ```

5. **在主计算机上创建[test plan](../T/test-plan.md)**，就像进行本地测试一样。
  6. **从主机上启动分布式测试**，使用GUI模式进行配置，然后使用CLI模式执行，以节省资源。使用`-R` 选项指定远程主机，或使用`-r` 选项来使用`remote_hosts` 属性中列出的主机。

    ```
    jmeter -n -t my_test_plan.jmx -r
    ```

7. **实时监控测试**或等待其完成。收集并分析来自主机的结果，主机将聚合来自所有从节点的数据。
  请记住，如果需要，请同步所有节点的测试开始时间，并确保所有机器都具有同步时钟以获得准确的结果。

1. **在所有将充当负载生成器的计算机（称为从节点）上设置 [JMeter](../J/jmeter.md) 环境**。确保所有机器都在同一网络上并且可以相互通信。
  2. **通过编辑`jmeter.properties` 文件来配置主机**（控制器）。找到 `remote_hosts` 属性并列出所有从属节点的 IP 地址，以逗号分隔。

    ```
    remote_hosts=192.168.0.101,192.168.0.102,192.168.0.103
    ```

3. **在所有从属节点上打开所需的端口**，以允许来自主机的传入连接。默认[JMeter](../J/jmeter.md) 端口是`1099`，但可以在`jmeter.properties` 文件中更改。
  4. **通过从 [JMeter](../J/jmeter.md) `bin` 目录运行以下命令，在每个从属节点上启动 [JMeter](../J/jmeter.md) 服务器**：

    ```
    jmeter-server
    ```

5. **在主计算机上创建[test plan](../T/test-plan.md)**，就像进行本地测试一样。
  6. **从主机上启动分布式测试**，使用GUI模式进行配置，然后使用CLI模式执行，以节省资源。使用`-R` 选项指定远程主机，或使用`-r` 选项来使用`remote_hosts` 属性中列出的主机。

    ```
    jmeter -n -t my_test_plan.jmx -r
    ```

7. **实时监控测试**或等待其完成。收集并分析来自主机的结果，主机将聚合来自所有从节点的数据。

#### 在 JMeter 中编写脚本的最佳实践是什么？

在 [JMeter](../J/jmeter.md) 中编写脚本时，请遵循以下最佳实践以确保高效且可维护的测试：

- **使用命名约定**：清楚地命名您的测试元素以反映其目的，使脚本更易于理解和维护。
  - **模块化您的测试**：使用测试片段将您的[test plans](../T/test-plan.md) 分解为逻辑模块，这些模块可以在不同的[test plans](../T/test-plan.md) 之间重复使用。
  - **参数化输入**：使用 CSV 数据集配置或用户定义变量外部化[test data](../T/test-data.md)，使测试更加灵活和数据驱动。
  - **添加断言**：使用断言验证响应，以确保您的应用程序返回 [expected results](../E/expected-result.md)。
  - **侦听器的有效使用**：侦听器可能会消耗大量内存。谨慎使用它们并在负载测试期间禁用它们以节省资源。
  - **关联**：通过从响应中提取数据并在后续请求中重用来处理会话 ID 等动态数据。
  - **思考时间**：通过在请求之间添加适当的计时器来模拟真实的用户行为。
  - **错误处理**：实施正确的错误处理和日志记录以快速识别问题。
  - **避免不必要的采样器**：仅使用测试所需的采样器，以避免混乱并减少资源使用。
  - **使用[JMeter](../J/jmeter.md) 函数和变量**：利用内置函数和变量来增强您的[test scripts](../T/test-script.md)，而无需硬编码值。
  - **脚本版本控制**：在版本控制系统中维护您的[test scripts](../T/test-script.md)，以跟踪更改并与其他人协作。
  - **正则表达式**：明智地使用正则表达式从响应中提取数据，但要注意它们的性能影响。
  - **优化线程组**：根据您的测试需求配置线程组，避免被测系统或[JMeter](../J/jmeter.md)主机过载。
  通过遵循这些实践，您将创建健壮、可扩展且可维护的 [JMeter](../J/jmeter.md) 脚本，这些脚本可以有效地模拟用户行为并测量应用程序的性能。

- **使用命名约定**：清楚地命名您的测试元素以反映其目的，使脚本更易于理解和维护。
  - **模块化您的测试**：使用测试片段将您的[test plans](../T/test-plan.md) 分解为逻辑模块，这些模块可以在不同的[test plans](../T/test-plan.md) 之间重复使用。
  - **参数化输入**：使用 CSV 数据集配置或用户定义变量外部化[test data](../T/test-data.md)，使测试更加灵活和数据驱动。
  - **添加断言**：使用断言验证响应，以确保您的应用程序返回 [expected results](../E/expected-result.md)。
  - **侦听器的有效使用**：侦听器可能会消耗大量内存。谨慎使用它们并在负载测试期间禁用它们以节省资源。
  - **关联**：通过从响应中提取数据并在后续请求中重用来处理会话 ID 等动态数据。
  - **思考时间**：通过在请求之间添加适当的计时器来模拟真实的用户行为。
  - **错误处理**：实施正确的错误处理和日志记录以快速识别问题。
  - **避免不必要的采样器**：仅使用测试所需的采样器，以避免混乱并减少资源使用。
  - **使用[JMeter](../J/jmeter.md) 函数和变量**：利用内置函数和变量来增强您的[test scripts](../T/test-script.md)，而无需硬编码值。
  - **脚本版本控制**：在版本控制系统中维护您的[test scripts](../T/test-script.md)，以跟踪更改并与其他人协作。
  - **正则表达式**：明智地使用正则表达式从响应中提取数据，但要注意它们的性能影响。
  - **优化线程组**：根据您的测试需求配置线程组，避免被测系统或[JMeter](../J/jmeter.md)主机过载。

#### 如何将 JMeter 与其他测试工具集成？

将[JMeter](../J/jmeter.md) 与其他测试工具集成可以通过将[performance testing](../P/performance-testing.md) 与其他类型的测试相结合来增强您的[test automation](../T/test-automation.md) 套件。以下是实现这一目标的方法：
  **持续集成 (CI) 工具：**
  使用性能插件将 [JMeter](../J/jmeter.md) 与 Jenkins 等 CI 工具集成。从 Jenkins 作业触发 [JMeter](../J/jmeter.md) 测试并收集结果以进行趋势分析和报告。

  ```
  # Example: Execute JMeter test plan in Jenkins job
  jmeter -n -t my_test_plan.jmx -l results.jtl
  ```**[Functional Testing](../F/functional-testing.md) 工具：**
  将[JMeter](../J/jmeter.md) 与[Selenium](../S/selenium.md) 结合起来进行全面的端到端测试。使用[JMeter](../J/jmeter.md) 表示[load testing](../L/load-testing.md)，使用[Selenium](../S/selenium.md) 实现功能自动化。在测试框架内按顺序或并行运行它们。
  **监控工具：**
  将 [JMeter](../J/jmeter.md) 与 Grafana 或 Prometheus 等监控工具链接，以实时可视化性能数据。使用[JMeter](../J/jmeter.md) 的后端侦听器将测试指标发送到这些工具。

  ```
  <!-- Example: Add Backend Listener to JMeter test plan -->
  <BackendListener guiclass="BackendListenerGui" testclass="BackendListener" testname="Backend Listener" enabled="true">
    <elementProp name="arguments" elementType="Arguments" guiclass="ArgumentsPanel" testclass="Arguments" enabled="true">
      <collectionProp name="Arguments.arguments">
        <elementProp name="influxdbMetricsSender" elementType="Argument">
          <stringProp name="Argument.name">influxdbMetricsSender</stringProp>
          <stringProp name="Argument.value">org.apache.jmeter.visualizers.backend.influxdb.HttpMetricsSender</stringProp>
        </elementProp>
        <!-- Additional configuration -->
      </collectionProp>
    </elementProp>
  </BackendListener>
  ```**[API Testing](../A/api-testing.md) 工具：**
  对于[API testing](../A/api-testing.md)，将[JMeter](../J/jmeter.md) 与[Postman](../P/postman.md) 或SoapUI 等工具集成。使用[JMeter](../J/jmeter.md) 来实现[load testing](../L/load-testing.md) [APIs](../A/api.md) 并使用其他工具来实现功能@@PR​​OTECTED_7@@。
  **代码质量工具：**
  通过将测试结果转换为与这些平台兼容的格式，将 [JMeter](../J/jmeter.md) 测试合并到 SonarQube 等代码质量平台中。
  **云服务：**
  利用 BlazeMeter 等云服务实现可扩展的 [JMeter](../J/jmeter.md) [test execution](../T/test-execution.md)。将[JMeter](../J/jmeter.md)脚本导入BlazeMeter并利用云资源进行大规模[performance testing](../P/performance-testing.md)。
  通过将 [JMeter](../J/jmeter.md) 与这些工具集成，您可以创建一个强大的、多方面的 [test automation](../T/test-automation.md) 环境来满足各种测试需求。

#### JMeter 有哪些限制以及如何克服它们？

[JMeter](../J/jmeter.md) 虽然对于 [performance testing](../P/performance-testing.md) 来说很强大，但也有局限性：

- **资源密集型**：[JMeter](../J/jmeter.md) 可能会占用大量资源，尤其是在模拟大量用户时。为了克服这个问题，请将负载分布到集群中的多个[JMeter](../J/jmeter.md) 实例或计算机上。
  - **有限的浏览器模拟**：[JMeter](../J/jmeter.md) 不会像真实浏览器一样执行 JavaScript 或渲染 HTML。使用 [Selenium](../S/selenium.md) 集成进行更准确的浏览器级用户模拟或考虑无头浏览器测试工具。
  - **脚本编写的复杂性**：[JMeter](../J/jmeter.md) 中的高级脚本编写需要 Java 或 BeanShell 知识，这可能是一个障碍。使用[JMeter](../J/jmeter.md) GUI 进行测试创建，并仅在必要时才使用脚本。此外，利用社区插件来扩展功能。
  - **UI 响应**：[JMeter](../J/jmeter.md) GUI 在重负载测试期间可能会变得无响应。使用命令行在非 GUI 模式下运行测试，以减少资源消耗并提高性能。

  ```
  jmeter -n -t testplan.jmx -l testresults.jtl
  ```

- **实时监控**：[JMeter](../J/jmeter.md) 不提供实时性能监控。与 Grafana 和 InfluxDB 等外部监控工具集成，实时可视化测试结果。
  - **移动应用程序测试**：[JMeter](../J/jmeter.md) 并非专为移动应用程序测试而设计。使用第三方库或服务将 [JMeter](../J/jmeter.md) 的功能扩展到移动设备，或使用专门的移动测试工具。
  - **有限协议支持**：[JMeter](../J/jmeter.md) 主要支持 HTTP/HTTPS 协议。为了测试其他协议，您可能需要查找插件或使用更适合这些协议的其他工具。
  通过了解这些限制并利用集成、插件和最佳实践，您可以有效地使用 [JMeter](../J/jmeter.md) 来实现全面的 [performance testing](../P/performance-testing.md)。

- **资源密集型**：[JMeter](../J/jmeter.md) 可能会占用大量资源，尤其是在模拟大量用户时。为了克服这个问题，请将负载分布到集群中的多个[JMeter](../J/jmeter.md) 实例或计算机上。
  - **有限的浏览器模拟**：[JMeter](../J/jmeter.md) 不会像真实浏览器一样执行 JavaScript 或渲染 HTML。使用 [Selenium](../S/selenium.md) 集成进行更准确的浏览器级用户模拟或考虑无头浏览器测试工具。
  - **脚本编写的复杂性**：[JMeter](../J/jmeter.md) 中的高级脚本编写需要 Java 或 BeanShell 知识，这可能是一个障碍。使用[JMeter](../J/jmeter.md) GUI 进行测试创建，并仅在必要时才使用脚本。此外，利用社区插件来扩展功能。
  - **UI 响应性**：[JMeter](../J/jmeter.md) GUI 在重负载测试期间可能会变得无响应。使用命令行在非 GUI 模式下运行测试，以减少资源消耗并提高性能。
  - **实时监控**：[JMeter](../J/jmeter.md) 不提供实时性能监控。与 Grafana 和 InfluxDB 等外部监控工具集成，实时可视化测试结果。
  - **移动应用程序测试**：[JMeter](../J/jmeter.md) 并非专为移动应用程序测试而设计。使用第三方库或服务将 [JMeter](../J/jmeter.md) 的功能扩展到移动设备，或使用专门的移动测试工具。
  - **有限协议支持**：[JMeter](../J/jmeter.md) 主要支持 HTTP/HTTPS 协议。为了测试其他协议，您可能需要查找插件或使用更适合这些协议的其他工具。

#### 如何使用 JMeter 进行 Web 服务的性能测试？

要将 [JMeter](../J/jmeter.md) 用于 Web 服务的 [performance testing](../P/performance-testing.md)，请按照以下步骤操作：

1. **通过在菜单上选择`Test Plan`来创建新的[Test Plan](../T/test-plan.md)**，然后右键单击并选择`Add` > `Threads (Users)` > `Thread Group`。
  2. **配置线程组**，包括测试的线程（用户）数量、启动周期和循环计数。
  3. **将采样器**添加到线程组，方法是右键单击它并导航到 `Add` > `Sampler` > `HTTP Request`。使用 Web 服务的 URL 和请求类型（GET、POST 等）配置 HTTP 请求。
  4. **设置 HTTP 请求默认值**（可选），如果您有多个具有公共参数的 HTTP 请求，可以通过添加 `Config Element` > `HTTP Request Defaults` 来减少冗余。
  5. **添加标头**（如果需要），方法是右键单击 HTTP 请求并选择 `Add` > `Config Element` > `HTTP Header Manager`。输入必要的标头，例如 `Content-Type` 或 `Authorization`。
  6. **添加监听器** 通过右键单击线程组并选择 `Add` > `Listener` 来查看结果。常见的侦听器是`View Results Tree` 和`Summary Report`。
  7. **参数化请求** 使用`CSV Data Set Config` 来测试不同的数据集。
  8. **通过单击工具栏上的 `Start` 按钮运行测试**。
  9. **使用所选侦听器分析结果**，以了解 Web 服务在负载下的性能。
  10. **保存[Test Plan](../T/test-plan.md)**以供将来使用或修改。
  请记住通过单个用户运行来**验证您的测试**，以确保它在扩展之前按预期工作。根据 Web 服务的预期负载和性能目标调整配置。

1. **通过在菜单上选择`Test Plan`来创建新的[Test Plan](../T/test-plan.md)**，然后右键单击并选择`Add` > `Threads (Users)` > `Thread Group`。
  2. **配置线程组**，包括测试的线程（用户）数量、启动周期和循环计数。
  3. **将采样器**添加到线程组，方法是右键单击它并导航到 `Add` > `Sampler` > `HTTP Request`。使用 Web 服务的 URL 和请求类型（GET、POST 等）配置 HTTP 请求。
  4. **设置 HTTP 请求默认值**（可选），如果您有多个具有公共参数的 HTTP 请求，可以通过添加 `Config Element` > `HTTP Request Defaults` 来减少冗余。
  5. **添加标头**（如果需要），方法是右键单击 HTTP 请求并选择 `Add` > `Config Element` > `HTTP Header Manager`。输入必要的标头，例如 `Content-Type` 或 `Authorization`。
  6. **添加监听器** 通过右键单击线程组并选择 `Add` > `Listener` 来查看结果。常见的侦听器是`View Results Tree` 和`Summary Report`。
  7. **参数化请求** 使用`CSV Data Set Config` 来测试不同的数据集。
  8. **通过单击工具栏上的 `Start` 按钮运行测试**。
  9. **使用所选侦听器分析结果**，以了解 Web 服务在负载下的性能。
  10. **保存[Test Plan](../T/test-plan.md)**以供将来使用或修改。
