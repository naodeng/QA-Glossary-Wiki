# Cypress




<!-- TOC START -->
- [# 另请参阅：](##-另请参阅：)
- [# 基础知识和重要性](##-基础知识和重要性)
  - [# Cypress 是什么？](##-cypress-是什么？)
  - [# 为什么在测试中使用Cypress？](##-为什么在测试中使用cypress？)
  - [# Cypress 的主要功能是什么？](##-cypress-的主要功能是什么？)
  - [# Cypress 与 Selenium 等其他测试工具有何不同？](##-cypress-与-selenium-等其他测试工具有何不同？)
  - [# 使用Cypress 可以执行哪些类型的测试？](##-使用cypress-可以执行哪些类型的测试？)
- [# 安装和设置](##-安装和设置)
  - [# 如何安装Cypress？](##-如何安装cypress？)
  - [# Cypress 的系统要求是什么？](##-cypress-的系统要求是什么？)
  - [# 如何在Cypress 中建立项目？](##-如何在cypress-中建立项目？)
  - [# 如何为特定环境配置Cypress？](##-如何为特定环境配置cypress？)
- [# 编写和运行测试](##-编写和运行测试)
  - [# 如何在Cypress 中编写基本测试？](##-如何在cypress-中编写基本测试？)
  - [# Cypress 测试的结构是什么？](##-cypress-测试的结构是什么？)
  - [# 如何在Cypress 中运行测试？](##-如何在cypress-中运行测试？)
  - [# 如何在Cypress 中使用断言？](##-如何在cypress-中使用断言？)
  - [# 如何处理Cypress 中的事件？](##-如何处理cypress-中的事件？)
  - [# 如何在Cypress 中使用灯具？](##-如何在cypress-中使用灯具？)
- [# 高级概念](##-高级概念)
  - [# Cypress 如何处理异步操作？](##-cypress-如何处理异步操作？)
  - [# 如何在Cypress 中使用自定义命令？](##-如何在cypress-中使用自定义命令？)
  - [# 如何处理Cypress 中的网络请求？](##-如何处理cypress-中的网络请求？)
  - [# 如何使用 Cypress 中的 cookie 和本地存储？](##-如何使用-cypress-中的-cookie-和本地存储？)
  - [# 如何处理 Cypress 中的 iframe？](##-如何处理-cypress-中的-iframe？)
  - [# 如何使用Cypress中的插件？](##-如何使用cypress中的插件？)
- [# 最佳实践和故障排除](##-最佳实践和故障排除)
  - [# 在 Cypress 中编写测试的最佳实践有哪些？](##-在-cypress-中编写测试的最佳实践有哪些？)
  - [# 如何在Cypress 中调试测试？](##-如何在cypress-中调试测试？)
  - [# 如何处理Cypress 中的常见错误？](##-如何处理cypress-中的常见错误？)
  - [# 如何优化 Cypress 中的测试执行时间？](##-如何优化-cypress-中的测试执行时间？)
<!-- TOC END -->

（又名 Cypress.io ）

Cypress

是一个

端到端测试

专为现代 Web 应用程序设计的框架。与许多其他测试解决方案不同，

Cypress

直接在网络浏览器中运行，确保更加一致和准确的真实测试场景。它提供了一组丰富的功能和工具，用于编写测试、实时调试以及捕获测试运行的屏幕截图或视频记录。

Cypress

两者都支持

单元测试

和完整的

端到端测试

，使其成为开发人员和 QA 专业人员的多功能选择。其显着特点之一是其互动性

测试运行者

它允许开发人员在执行命令时查看命令，同时还可以查看正在测试的应用程序。基于 Mocha、Chai 和 Sinon 等技术构建，

Cypress

为 Web 应用程序测试提供全面且用户友好的环境。

# # 相关术语：

- [Web Automation tool](../W/web-automation-tool.md)
- [Playwright](../P/playwright.md)

## # 另请参阅：

- [Official Website](https://www.cypress.io/)
- [Wikipedia](https://en.wikipedia.org/wiki/Cypress_(software))

# # 关于Cypress 有疑问吗？

## # 基础知识和重要性

### # Cypress 是什么？

[Cypress](../C/cypress.md) 是一个专为现代 Web 应用程序设计的 **[end-to-end testing](../E/end-to-end-testing.md) 框架**。它在浏览器中运行测试，并基于 **JavaScript** 和 **[Node.js](../N/node-js.md)** 等技术构建。与许多其他测试工具不同，[Cypress](../C/cypress.md) 在与应用程序相同的运行循环中执行测试，提供对每个对象的本机访问，而不需要单独的驱动程序或服务器。
  [Cypress](../C/cypress.md) 提供了**丰富的交互式[test runner](../T/test-runner.md)**，允许您在命令执行时查看命令，同时还可以查看正在测试的应用程序。该工具为 [test-driven development](../T/test-driven-development.md) 提供**实时重新加载**，并在文件保存时重新运行测试。
  [Cypress](../C/cypress.md) 中的测试是使用 **可链接的 [API](../A/api.md)** 编写的，它与 Promise 一起使用，从而简化了异步操作的处理。 [Cypress](../C/cypress.md) 包含**类似 jQuery 的命令**，用于 DOM 遍历和操作，使其为前端开发人员所熟悉。
  [Cypress](../C/cypress.md) 在执行操作或断言之前提供**自动等待**，从而在大多数情况下无需显式等待或睡眠。它还提供**间谍、存根和时钟**来验证和控制服务器响应、函数或计时器的行为。
  该工具具有**屏幕截图和视频录制**功能，可以方便地调试和理解测试失败。 [Cypress](../C/cypress.md) 测试可以在持续集成 (CI) 环境中无头运行，也可以在开发过程中以交互方式运行。
  [Cypress](../C/cypress.md) 的体系结构不使用[Selenium](../S/selenium.md) 或[WebDriver](../W/webdriver.md)，这允许更快的执行和更多的控制，但也意味着它主要适合测试在浏览器中运行的应用程序。它支持**Chrome系列浏览器**（包括Electron）和**Firefox**。

### # 为什么在测试中使用Cypress？

[Cypress](../C/cypress.md) 用于测试主要是因为其**简单**和**开发人员友好**方法[end-to-end testing](../E/end-to-end-testing.md)。由于其独特的架构与被测试的应用程序在同一运行循环中运行，因此它允许编写**无片断**测试。与在浏览器之外运行的其他工具相比，这会产生更可靠的测试和一致的测试。
  [Cypress](../C/cypress.md) 的使用因其**实时重新加载**而受到青睐，它可以提供有关测试代码更改的即时反馈，从而提高生产力并减少编写和维护测试所花费的时间。它的**自动等待**机制消除了手动睡眠或等待命令的需要，从而降低了[test scripts](../T/test-script.md)的复杂性。
  当开发人员和 QA 工程师需要与现代开发工具和工作流程（包括持续集成和版本控制系统）**紧密集成**时，他们会选择[Cypress](../C/cypress.md)。 [Cypress](../C/cypress.md) 的**丰富的调试功能**使得直接从浏览器的开发人员工具诊断和修复问题变得更加容易。
  [Cypress](../C/cypress.md) 的**屏幕截图和视频录制**功能对于可视化测试失败时应用程序的状态至关重要，有助于更快地排除故障。它的**网络流量控制**允许轻松地对边缘情况进行存根和测试，而无需后端依赖项。
  总的来说，[Cypress](../C/cypress.md) 用于其**一体化**测试体验，提供了一组强大的工具来满足现代 Web 应用程序测试的需求，所有这些都在一个单一的、连贯的框架内。

### # Cypress 的主要功能是什么？

[Cypress](../C/cypress.md) 的主要功能包括：

- **实时重新加载**：Cypress 在检测到测试代码的更改后自动重新加载测试，提供即时反馈。
  - **时间旅行**：Cypress 在测试运行时拍摄快照，允许您将鼠标悬停在命令日志中的命令上以准确查看每个步骤发生的情况。
  - **自动等待**：Cypress 在继续之前等待命令和断言，消除了显式等待或睡眠的需要。
  - **一致的结果**：Cypress 中的测试不那么不稳定且更可靠，因为它与应用程序在同一运行循环中运行。
  - **可调试性**：通过可读错误和堆栈跟踪，Cypress 使调试测试变得更加容易。您还可以使用熟悉的开发工具。
  - **网络流量控制**：拦截和控制每个网络请求，使您能够在不涉及服务器的情况下测试边缘情况。
  - **屏幕截图和视频**：Cypress 可以在失败时自动捕获屏幕截图，也可以手动捕获它们。它还记录了整个测试运行的视频。
  - **跨浏览器测试**：Cypress 支持跨多个浏览器进行测试，包括Chrome、Firefox、Edge 和Electron。
  - **并行化**：测试可以在多台机器上并行运行，以加快持续集成（CI）中的执行时间。
  - **仪表板服务**：与 Cypress 仪表板一起使用时，通过分析、并行化和历史记录提供对测试的深入了解。
  - **间谍、存根和时钟**：验证和控制函数、服务器响应或计时器的行为。
  - **[Accessibility Testing](../A/accessibility-testing.md)** ：使用诸如
    `cypress-axe`
    ，您可以将可访问性检查合并到您的测试套件中。
  这些功能旨在简化测试过程，使 [test automation](../T/test-automation.md) 工程师更加高效和有效。

- **实时重新加载**：Cypress 在检测到测试代码的更改后自动重新加载测试，提供即时反馈。
  - **时间旅行**：Cypress 在测试运行时拍摄快照，允许您将鼠标悬停在命令日志中的命令上以准确查看每个步骤发生的情况。
  - **自动等待**：Cypress 在继续之前等待命令和断言，消除了显式等待或睡眠的需要。
  - **一致的结果**：Cypress 中的测试不那么不稳定且更可靠，因为它与应用程序在同一运行循环中运行。
  - **可调试性**：通过可读错误和堆栈跟踪，Cypress 使调试测试变得更加容易。您还可以使用熟悉的开发工具。
  - **网络流量控制**：拦截和控制每个网络请求，使您能够在不涉及服务器的情况下测试边缘情况。
  - **屏幕截图和视频**：Cypress 可以在失败时自动捕获屏幕截图，也可以手动捕获它们。它还记录了整个测试运行的视频。
  - **跨浏览器测试**：Cypress 支持跨多个浏览器进行测试，包括Chrome、Firefox、Edge 和Electron。
  - **并行化**：测试可以在多台机器上并行运行，以加快持续集成（CI）中的执行时间。
  - **仪表板服务**：与 Cypress 仪表板一起使用时，通过分析、并行化和历史记录提供对测试的深入了解。
  - **间谍、存根和时钟**：验证和控制函数、服务器响应或计时器的行为。
  - **[Accessibility Testing](../A/accessibility-testing.md)** ：使用诸如
    `cypress-axe`
    ，您可以将可访问性检查合并到您的测试套件中。

### # Cypress 与 Selenium 等其他测试工具有何不同？

[Cypress](../C/cypress.md) 与 [Selenium](../S/selenium.md) 在几个关键方面有所不同：

- **架构**：[Cypress](../C/cypress.md) 与正在测试的应用程序在同一运行循环中运行，从而实现更快的执行和更一致的结果。 [Selenium](../S/selenium.md) 在浏览器外部运行，这可能会导致延迟和不稳定。
  - **语言支持**：[Cypress](../C/cypress.md) 测试以JavaScript 编写，而[Selenium](../S/selenium.md) 支持多种语言，例如Java、C#、Python 和Ruby。
  - **直接访问**：[Cypress](../C/cypress.md) 可以直接访问DOM，并且可以更自然地与元素交互。 [Selenium](../S/selenium.md) 需要中介 ([WebDriver](../W/webdriver.md)) 与浏览器通信，这会减慢交互速度。
  - **[Setup](../S/setup.md) 和配置**：[Cypress](../C/cypress.md) 更易于设置，无需额外的驱动程序或服务器。 [Selenium](../S/selenium.md) 通常需要额外的[setup](../S/setup.md) 用于[WebDriver](../W/webdriver.md) 和浏览器特定的驱动程序。
  - **实时重新加载**：[Cypress](../C/cypress.md) 提供[Test Runner](../T/test-runner.md)，可在测试文件更改时自动重新加载，提供即时反馈。 [Selenium](../S/selenium.md) 没有内置等效项。
  - **自动等待**：[Cypress](../C/cypress.md) 在继续之前自动等待命令和断言。 [Selenium](../S/selenium.md) 需要显式等待或睡眠命令来管理计时问题。
  - **[API Testing](../A/api-testing.md)**：[Cypress](../C/cypress.md) 包含对 [API testing](../A/api-testing.md) 的内置支持，允许在一个框架中进行前端和后端测试。 [Selenium](../S/selenium.md) 主要专注于基于浏览器的测试。
  - **屏幕截图和视频**：[Cypress](../C/cypress.md) 可以本地截图和录制视频。 [Selenium](../S/selenium.md)可以捕获屏幕截图，但视频录制通常需要额外的工具或插件。
  - **可调试性**：[Cypress](../C/cypress.md) 提供更多信息性错误消息和堆栈跟踪，使调试更容易。 [Selenium](../S/selenium.md) 的错误消息可能不太清晰，使调试更具挑战性。
  - **[Cross-browser Testing](../C/cross-browser-testing.md)**：[Selenium](../S/selenium.md) 支持更广泛的浏览器和版本。 [Cypress](../C/cypress.md) 的跨浏览器支持正在改进，但历史上仅限于较少的浏览器。
  - **架构**：[Cypress](../C/cypress.md) 与正在测试的应用程序在同一运行循环中运行，从而实现更快的执行和更一致的结果。 [Selenium](../S/selenium.md) 在浏览器外部运行，这可能会导致延迟和不稳定。
  - **语言支持**：[Cypress](../C/cypress.md) 测试以JavaScript 编写，而[Selenium](../S/selenium.md) 支持多种语言，例如Java、C#、Python 和Ruby。
  - **直接访问**：[Cypress](../C/cypress.md) 可以直接访问DOM，并且可以更自然地与元素交互。 [Selenium](../S/selenium.md) 需要中介 ([WebDriver](../W/webdriver.md)) 与浏览器通信，这会减慢交互速度。
  - **[Setup](../S/setup.md) 和配置**：[Cypress](../C/cypress.md) 更易于设置，无需额外的驱动程序或服务器。 [Selenium](../S/selenium.md) 通常需要额外的[setup](../S/setup.md) 用于[WebDriver](../W/webdriver.md) 和浏览器特定的驱动程序。
  - **实时重新加载**：[Cypress](../C/cypress.md) 提供了 [Test Runner](../T/test-runner.md)，可在测试文件更改时自动重新加载，提供即时反馈。 [Selenium](../S/selenium.md) 没有内置等效项。
  - **自动等待**：[Cypress](../C/cypress.md) 在继续之前自动等待命令和断言。 [Selenium](../S/selenium.md) 需要显式等待或睡眠命令来管理计时问题。
  - **[API Testing](../A/api-testing.md)**：[Cypress](../C/cypress.md) 包含对 [API testing](../A/api-testing.md) 的内置支持，允许在一个框架中进行前端和后端测试。 [Selenium](../S/selenium.md) 主要专注于基于浏览器的测试。
  - **屏幕截图和视频**：[Cypress](../C/cypress.md) 可以本地截图和录制视频。 [Selenium](../S/selenium.md)可以捕获屏幕截图，但视频录制通常需要额外的工具或插件。
  - **可调试性**：[Cypress](../C/cypress.md) 提供更多信息性错误消息和堆栈跟踪，使调试更容易。 [Selenium](../S/selenium.md) 的错误消息可能不太清晰，使调试更具挑战性。
  - **[Cross-browser Testing](../C/cross-browser-testing.md)**：[Selenium](../S/selenium.md) 支持更广泛的浏览器和版本。 [Cypress](../C/cypress.md) 的跨浏览器支持正在改进，但历史上仅限于较少的浏览器。

### # 使用Cypress 可以执行哪些类型的测试？

使用[Cypress](../C/cypress.md)，测试人员可以执行各种类型的测试，包括：

- **[End-to-End Testing](../E/end-to-end-testing.md) (E2E)** ：从头到尾模拟真实的用户场景，确保应用程序在类似生产的环境中按预期运行。
  - **[Integration Testing](../I/integration-testing.md)** ：测试应用程序层之间或不同微服务之间的交互，以验证它们正确地协同工作。
  - **[Unit Testing](../U/unit-testing.md)** ：虽然不是其主要用例，但 Cypress 可用于单独测试各个功能或组件。
  - **组件测试**：验证各个组件的功能和渲染，在现代 JavaScript 框架（如 React、Angular 或 Vue）中特别有用。
  - **[Visual Regression Testing](../V/visual-regression-testing.md)** ：通过与 Percy 或 Applitools 等工具集成，Cypress 可以捕获屏幕截图并将其与基线图像进行比较以检测视觉变化。
  - **[Accessibility Testing](../A/accessibility-testing.md)** ：使用诸如
    `cypress-axe`
    ，测试人员可以将可访问性检查合并到他们的测试套件中，以确保符合 WCAG 等标准。

- **[API Testing](../A/api-testing.md)** ：虽然 Cypress 主要是一个基于浏览器的工具，但它可用于通过发送 HTTP 请求并断言响应来测试 REST 或 GraphQL API。
  - **[Performance Testing](../P/performance-testing.md)** ：虽然不是成熟的性能测试工具，Cypress 可以捕获页面加载时间等性能指标，并使用断言来标记性能回归。
  [Cypress](../C/cypress.md) 的多功能性使其能够在单个框架内涵盖广泛的测试需求，从而简化开发和测试工作流程。

- **[End-to-End Testing](../E/end-to-end-testing.md) (E2E)** ：从头到尾模拟真实的用户场景，确保应用程序在类似生产的环境中按预期运行。
  - **[Integration Testing](../I/integration-testing.md)** ：测试应用程序层之间或不同微服务之间的交互，以验证它们正确地协同工作。
  - **[Unit Testing](../U/unit-testing.md)** ：虽然不是其主要用例，但 Cypress 可用于单独测试各个功能或组件。
  - **组件测试**：验证各个组件的功能和渲染，在现代 JavaScript 框架（如 React、Angular 或 Vue）中特别有用。
  - **[Visual Regression Testing](../V/visual-regression-testing.md)** ：通过与 Percy 或 Applitools 等工具集成，Cypress 可以捕获屏幕截图并将其与基线图像进行比较以检测视觉变化。
  - **[Accessibility Testing](../A/accessibility-testing.md)** ：使用诸如
    `cypress-axe`
    ，测试人员可以将可访问性检查合并到他们的测试套件中，以确保符合 WCAG 等标准。

- **[API Testing](../A/api-testing.md)** ：虽然 Cypress 主要是一个基于浏览器的工具，但它可用于通过发送 HTTP 请求并断言响应来测试 REST 或 GraphQL API。
  - **[Performance Testing](../P/performance-testing.md)** ：虽然不是成熟的性能测试工具，Cypress 可以捕获页面加载时间等性能指标，并使用断言来标记性能回归。

## # 安装和设置

### # 如何安装Cypress？

要安装 [Cypress](../C/cypress.md)，请确保您的系统上安装了 **[Node.js](../N/node-js.md)**（版本 12 或更高版本）和 **npm**（版本 6 或更高版本）。打开终端或命令提示符并按照以下步骤操作：

1. 导航到您的项目目录：

    ```
    cd /your/project/path
    ```
2. 使用npm 将[Cypress](../C/cypress.md) 安装为开发依赖项：
    或者，如果您愿意，也可以使用`yarn`：

    ```
    npm install cypress --save-dev
    ```

    ```
    yarn add cypress --dev
    ```
3. 安装后，您可以使用以下命令首次打开[Cypress](../C/cypress.md)：
    或者，如果您使用的是纱线：

    ```
    npx cypress open
    ```

    ```
    yarn run cypress open
    ```
这将打开 [Cypress](../C/cypress.md) [Test Runner](../T/test-runner.md) 并在项目目录中创建 `cypress` 文件夹，其中包含默认配置和示例测试。
  对于持续集成系统或无头运行 [Cypress](../C/cypress.md) 测试，请使用 `cypress run` 命令：

  ```
  npx cypress run
  ```
请记住将 [Cypress](../C/cypress.md) 命令添加到 `package.json` 的 `scripts` 部分，以便于执行：

  ```
  "scripts": {
    "cypress:open": "cypress open",
    "cypress:run": "cypress run"
  }
  ```
要使用这些脚本执行：

  ```
  npm run cypress:open
  ```
或者

  ```
  npm run cypress:run
  ```
确保您拥有在系统上安装新软件包所需的权限。如果您遇到任何问题，请参阅官方[Cypress](../C/cypress.md)文档进行故障排除。

1. 导航到您的项目目录：

    ```
    cd /your/project/path
    ```
2. 使用npm 将[Cypress](../C/cypress.md) 安装为开发依赖项：
    或者，如果您愿意，也可以使用`yarn`：

    ```
    npm install cypress --save-dev
    ```

    ```
    yarn add cypress --dev
    ```
3. 安装后，您可以使用以下命令首次打开[Cypress](../C/cypress.md)：
    或者，如果您使用的是纱线：

    ```
    npx cypress open
    ```

    ```
    yarn run cypress open
    ```
### # Cypress 的系统要求是什么？

[Cypress](../C/cypress.md) 与 **Windows、macOS 和 Linux** 操作系统兼容。具体的系统要求包括：

- **[Node.js](../N/node-js.md)** ：版本 12 或更高版本。
  - **npm**
    （通常带有Node.js）或
    **纱线**
    用于包管理。

- A
    **支持的浏览器**
    安装在您的机器上。 Cypress 支持：

- Chrome（包括 Canary 和 Chromium）
    - Firefox（包括开发者版）
    - Edge
    - Electron（与Cypress 捆绑在一起）
    - 勇敢
    - Chrome（包括 Canary 和 Chromium）
    - Firefox（包括开发者版）
    - Edge
    - Electron（与Cypress 捆绑在一起）
    - 勇敢
  - 对于
    **CI/CD 管道**
    ，确保构建代理满足操作系统和Node.js 要求。

- **内存和CPU**：有足够的资源来运行Electron浏览器，特别是在并行运行多个测试时。建议至少 2GB RAM。
  - **屏幕分辨率**：建议使用最小屏幕分辨率 1280x720 查看 Cypress 测试运行程序。
  确保您的系统对安装[Cypress](../C/cypress.md) 并运行测试的目录具有**写入权限**。
  对于 **Linux 用户**，如果您的系统上尚不存在其他依赖项，您可能需要安装它们。 [Cypress](../C/cypress.md) 提供了一个可以运行来安装这些依赖项的命令：

  ```
  sudo apt-get install libgtk2.0-0 libgtk-3-0 libgbm-dev libnotify-dev libgconf-2-4 libnss3 libxss1 libasound2 libxtst6 xauth xvfb
  ```
**注意**：[Cypress](../C/cypress.md) 是安装在您的计算机上的桌面应用程序，因此需要满足上述先决条件才能安装和执行测试。

- **[Node.js](../N/node-js.md)** ：版本 12 或更高版本。
  - **npm**
    （通常带有Node.js）或
    **纱线**
    用于包管理。

- A
    **支持的浏览器**
    安装在您的机器上。 Cypress 支持：

- Chrome（包括 Canary 和 Chromium）
    - Firefox（包括开发者版）
    - Edge
    - Electron（与Cypress 捆绑在一起）
    - 勇敢
    - Chrome（包括 Canary 和 Chromium）
    - Firefox（包括开发者版）
    - Edge
    - Electron（与Cypress 捆绑在一起）
    - 勇敢
  - 对于
    **CI/CD 管道**
    ，确保构建代理满足操作系统和Node.js 要求。

- **内存和CPU**：有足够的资源来运行Electron浏览器，特别是在并行运行多个测试时。建议至少 2GB RAM。
  - **屏幕分辨率**：建议查看 Cypress 测试运行程序时的最小屏幕分辨率为 1280x720。

### # 如何在Cypress 中建立项目？

要在 [Cypress](../C/cypress.md) 中设置项目，请执行以下步骤：

1. **为您的项目创建一个新目录**（如果尚未创建），然后使用终端或命令提示符导航到该目录。

    ```
    mkdir my-cypress-project
    cd my-cypress-project
    ```
2. **使用`npm init` 初始化新的npm 项目**。您可以使用`npm init -y` 跳过提示。

    ```
    npm init -y
    ```
3. **通过npm安装[Cypress](../C/cypress.md)**，运行：

    ```
    npm install cypress --save-dev
    ```
4. **首次打开[Cypress](../C/cypress.md)**，通过执行以下命令搭建默认目录结构和文件：
    此命令生成一个 `cypress` 文件夹，其中包含示例测试和一个用于配置的 `cypress.json` 文件。

    ```
    npx cypress open
    ```
5. **通过编辑`cypress.json` 文件来配置您的测试**。设置任何所需的环境变量或基本 URL。

    ```
    {
      "baseUrl": "http://yourapp.com",
      "env": {
        "login_url": "/login",
        "products_url": "/products"
      }
    }
    ```
6. **在 `cypress/integration` 目录中组织测试文件**。您可以创建子目录来对相关测试进行分组。
  7. **使用[Cypress](../C/cypress.md) 提供的`describe` 和`it` 函数编写测试**，并使用`.spec.js` 或`.spec.ts` 扩展名保存它们。
  8. **运行测试** 使用 `npx cypress open` 打开 [Cypress](../C/cypress.md) [Test Runner](../T/test-runner.md) 或 `npx cypress run` 在无头模式下执行测试。
  请记住**将 `node_modules` 目录添加到 `.gitignore` 文件**以避免将依赖项提交到版本控制。另外，请考虑在 `package.json` 中为常见的 [Cypress](../C/cypress.md) 命令设置脚本。

1. **为您的项目创建一个新目录**（如果尚未创建），然后使用终端或命令提示符导航到该目录。

    ```
    mkdir my-cypress-project
    cd my-cypress-project
    ```
2. **使用`npm init` 初始化新的npm 项目**。您可以使用`npm init -y` 跳过提示。

    ```
    npm init -y
    ```
3. **通过npm安装[Cypress](../C/cypress.md)**，运行：

    ```
    npm install cypress --save-dev
    ```
4. **首次打开[Cypress](../C/cypress.md)**，通过执行以下命令搭建默认目录结构和文件：
    此命令生成一个 `cypress` 文件夹，其中包含示例测试和一个用于配置的 `cypress.json` 文件。

    ```
    npx cypress open
    ```
5. **通过编辑`cypress.json` 文件来配置您的测试**。设置任何所需的环境变量或基本 URL。

    ```
    {
      "baseUrl": "http://yourapp.com",
      "env": {
        "login_url": "/login",
        "products_url": "/products"
      }
    }
    ```
6. **在 `cypress/integration` 目录中组织测试文件**。您可以创建子目录来对相关测试进行分组。
  7. **使用[Cypress](../C/cypress.md) 提供的`describe` 和`it` 函数编写测试**，并使用`.spec.js` 或`.spec.ts` 扩展名保存它们。
  8. **运行测试** 使用 `npx cypress open` 打开 [Cypress](../C/cypress.md) [Test Runner](../T/test-runner.md) 或 `npx cypress run` 在无头模式下执行测试。

### # 如何为特定环境配置Cypress？

要为特定环境配置[Cypress](../C/cypress.md)，您需要设置环境变量并可能调整您的`cypress.json` 配置文件。这是一个简洁的指南：

1. **环境变量**：使用 `cypress.json` 文件中的 `env` 键或通过命令行传递它们来定义特定于环境的变量。
    或者，使用命令行覆盖：

    ```
    {
      "env": {
        "apiUrl": "https://api.staging.example.com"
      }
    }
    ```

    ```
    npx cypress run --env apiUrl=https://api.staging.example.com
    ```
2. **配置文件**：对于更复杂的[setups](../S/setup.md)，请考虑为每个环境使用单独的配置文件，例如`cypress.staging.json` 和`cypress.production.json`。运行测试时使用 `--config-file` 标志指定配置文件。

    ```
    npx cypress run --config-file cypress.staging.json
    ```
3. **动态配置**：在`plugins/index.js` 文件中，您可以根据环境变量或其他条件以编程方式更改配置。

    ```
    module.exports = (on, config) => {
      if (process.env.NODE_ENV === 'staging') {
        config.baseUrl = 'https://staging.example.com';
        // Modify other config settings as needed
      }
      return config;
    };
    ```
4. **[Cypress](../C/cypress.md).env()**：使用`Cypress.env('variableName')` 访问测试中的环境变量。

    ```
    const apiUrl = Cypress.env('apiUrl');
    ```
请记住，**永远不要将敏感数据**提交给版本控制。对敏感数据使用环境变量或秘密管理解决方案。

1. **环境变量**：使用 `cypress.json` 文件中的 `env` 键或通过命令行传递它们来定义特定于环境的变量。
    或者，使用命令行覆盖：

    ```
    {
      "env": {
        "apiUrl": "https://api.staging.example.com"
      }
    }
    ```

    ```
    npx cypress run --env apiUrl=https://api.staging.example.com
    ```
2. **配置文件**：对于更复杂的[setups](../S/setup.md)，请考虑为每个环境使用单独的配置文件，例如`cypress.staging.json` 和`cypress.production.json`。运行测试时使用 `--config-file` 标志指定配置文件。

    ```
    npx cypress run --config-file cypress.staging.json
    ```
3. **动态配置**：在`plugins/index.js` 文件中，您可以根据环境变量或其他条件以编程方式更改配置。

    ```
    module.exports = (on, config) => {
      if (process.env.NODE_ENV === 'staging') {
        config.baseUrl = 'https://staging.example.com';
        // Modify other config settings as needed
      }
      return config;
    };
    ```
4. **[Cypress](../C/cypress.md).env()**：使用`Cypress.env('variableName')` 访问测试中的环境变量。

    ```
    const apiUrl = Cypress.env('apiUrl');
    ```
## # 编写和运行测试

### # 如何在Cypress 中编写基本测试？

要在 [Cypress](../C/cypress.md) 中编写基本测试，请按照以下步骤操作：

1. **在[Cypress](../C/cypress.md) 集成文件夹中创建一个新的测试文件**，通常带有`.spec.js` 扩展名，例如`login.spec.js`。
  2. **首先在测试文件顶部要求[Cypress](../C/cypress.md)**：

  ```
  /// <reference types="cypress" />
  ```
1. **描述您的[test suite](../T/test-suite.md)**
    使用
    `describe`
    函数，提供标题和回调函数来包含您的测试：

  ```
  describe('Login Test', () => {
    // Your tests will go here
  });
  ```
1. **写单独的[test cases](../T/test-case.md)**
    内
    `describe`
    块使用
    `it`
    功能。每个
    `it`
    函数采用测试用例的标题和执行测试步骤的回调函数：

  ```
  it('successfully logs in', () => {
    // Test steps will go here
  });
  ```
1. **定义测试步骤**
    内
    `it`
    回调。使用 Cypress 命令与应用程序交互：

  ```
  it('successfully logs in', () => {
    cy.visit('/login'); // Navigate to the login page
    cy.get('input[name=username]').type('user@example.com'); // Type the username
    cy.get('input[name=password]').type('password123'); // Type the password
    cy.get('form').submit(); // Submit the login form
    cy.url().should('include', '/dashboard'); // Assert the URL to ensure login was successful
  });
  ```
1. **运行测试**
    使用 Cypress 测试运行程序或通过命令行
    `cypress open`
    或
    `cypress run`
    。
  请记住**保持测试隔离**和**独立**以确保可靠性。如果您需要在每次测试之前或在套件中的所有测试之前分别设置一次状态，请使用 `beforeEach` 或 `before` 挂钩。

1. **在[Cypress](../C/cypress.md) 集成文件夹中创建一个新的测试文件**，通常带有`.spec.js` 扩展名，例如`login.spec.js`。
  2. **首先在测试文件顶部要求[Cypress](../C/cypress.md)**：
  1. **描述您的[test suite](../T/test-suite.md)**
    使用
    `describe`
    函数，提供标题和回调函数来包含您的测试：

1. **写个人[test cases](../T/test-case.md)**
    内
    `describe`
    块使用
    `it`
    功能。每个
    `it`
    函数采用测试用例的标题和执行测试步骤的回调函数：

1. **定义测试步骤**
    内
    `it`
    回调。使用 Cypress 命令与应用程序交互：

1. **运行测试**
    使用Cypress测试运行器或通过命令行
    `cypress open`
    或
    `cypress run`
    。

### # Cypress 测试的结构是什么？

[Cypress](../C/cypress.md) 测试通常遵循的结构包括导入必要的依赖项、描述[test suites](../T/test-suite.md)、定义[test cases](../T/test-case.md) 以及使用断言实现测试步骤。以下是基本 [Cypress](../C/cypress.md) 测试结构的示例：

  ```
  // Import the Cypress module
  import cy from 'cypress';
  // Describe the test suite
  describe('User Login', () => {
    // Before each test, do some common setup (optional)
    beforeEach(() => {
      // Visit the login page
      cy.visit('/login');
    });
    // Define a test case
    it('should login with valid credentials', () => {
      // Test steps
      cy.get('input[name="username"]').type('user');
      cy.get('input[name="password"]').type('password');
      cy.get('form').submit();
      // Assertions
      cy.url().should('include', '/dashboard');
      cy.get('.welcome-message').should('contain', 'Welcome, user');
    });
    // Define another test case
    it('should display an error for invalid credentials', () => {
      // Test steps
      cy.get('input[name="username"]').type('wronguser');
      cy.get('input[name="password"]').type('wrongpassword');
      cy.get('form').submit();
      // Assertions
      cy.get('.error-message').should('be.visible');
    });
  });
  ```
在这个结构中：

- **描述**
    块将相关测试分组，称为测试套件。

- **它**
    块定义单独的测试用例。

- **在每个之前**
    是一个用于在每次测试运行之前设置条件的钩子。

- **cy.visit**
    导航到URL。

- **cy.get**
    选择DOM 元素。

- **类型**
    和
    **提交**
    模拟用户操作。

- **应该**
    用于断言以验证所需的状态。

- **描述**
    块将相关测试分组，称为测试套件。

- **它**
    块定义单独的测试用例。

- **在每个之前**
    是一个用于在每次测试运行之前设置条件的钩子。

- **cy.visit**
    导航到URL。

- **cy.get**
    选择DOM 元素。

- **类型**
    和
    **提交**
    模拟用户操作。

- **应该**
    用于断言以验证所需的状态。

### # 如何在Cypress 中运行测试？

要在 [Cypress](../C/cypress.md) 中运行测试，请按照以下步骤操作：

1. 打开终端或命令提示符。
  2. 导航到安装Cypress 的项目目录。
  3. 执行以下命令打开Cypress测试运行程序：

  ```
  npx cypress open
  ```
1. Cypress Test Runner GUI 将启动，显示测试文件列表。
  2. 单击要运行的测试文件。 Cypress 将执行该文件中的测试并实时显示结果。
  或者，在不打开 [Test Runner](../T/test-runner.md) GUI 的情况下无头运行测试：

1. 在终端中使用以下命令：

  ```
  npx cypress run
  ```
1. 这将在默认的无头浏览器 (Electron) 中运行所有测试文件。
  要在特定浏览器中运行测试，请使用 `--browser` 标志：

  ```
  npx cypress run --browser chrome
  ```
要运行特定的测试文件，请附加 `--spec` 标志，后跟测试文件的路径：

  ```
  npx cypress run --spec "cypress/integration/example.spec.js"
  ```
要使用其他配置选项运行测试，请使用 `--config` 标志：

  ```
  npx cypress run --config video=false
  ```
此命令将运行测试而不录制视频。
  对于并行 [test execution](../T/test-execution.md) 以及跨多台计算机或 CI 容器的负载平衡，请使用 [Cypress](../C/cypress.md) 仪表板服务，这需要额外的 [setup](../S/setup.md) 和配置。

1. 打开终端或命令提示符。
  2. 导航到安装Cypress 的项目目录。
  3. 执行以下命令打开Cypress测试运行器：
  1. Cypress Test Runner GUI 将启动，显示测试文件列表。
  2. 单击要运行的测试文件。 Cypress 将执行该文件中的测试并实时显示结果。
  1. 在终端中使用以下命令：
  1. 这将在默认的无头浏览器 (Electron) 中运行所有测试文件。

### # 如何在Cypress 中使用断言？

在 [Cypress](../C/cypress.md) 中使用断言对于验证被测应用程序是否按预期运行至关重要。 [Cypress](../C/cypress.md) 使用 Chai 进行断言，它提供 `expect`、`assert` 和 `should` 语法。
  **Expect** 和 **should** 是 [BDD](../B/bdd.md)（行为驱动开发）风格的断言，而 **assert** 是 TDD ([Test-Driven Development](../T/test-driven-development.md)) 风格。以下是如何使用它们：
  **预期：**

  ```
  expect(variable).to.equal(value);
  expect(element).to.have.class(className);
  ```
**应该：**

  ```
  cy.get(selector).should('have.class', className);
  cy.get(selector).should('contain', text);
  ```
**断言：**

  ```
  assert.equal(variable, value, 'Optional message');
  assert.isTrue(condition, 'Optional message');
  ```
[Cypress](../C/cypress.md) 断言会自动重试，直到通过或超时（这是由 `defaultCommandTimeout` 配置定义的）。
  用于更复杂检查的链断言：

  ```
  cy.get(selector).should('be.visible').and('contain', text);
  ```
使用 `.and` 链接同一主题的多个断言。
  对于网络请求的断言：

  ```
  cy.request('GET', '/api/data').then((response) => {
    expect(response.status).to.eq(200);
    expect(response.body).to.have.property('data');
  });
  ```
请记住利用 [Cypress](../C/cypress.md) 的内置断言来处理常见条件，例如元素的可见性或存在，这可以简化语法并提高可读性：

  ```
  cy.get(selector).should('be.visible');
  cy.get(selector).should('exist');
  ```
通过有效地使用断言，您可以确保您的测试准确地验证应用程序的行为。

### # 如何处理Cypress 中的事件？

由于其类似于 jQuery 的语法，在 [Cypress](../C/cypress.md) 中处理事件非常简单。要与元素交互并处理事件，您可以使用模拟用户操作的 [Cypress](../C/cypress.md) 命令。
  例如，要处理单击事件，您可以使用 `.click()` 命令：

  ```
  cy.get('button').click();
  ```
要处理表单提交，您可以使用 `.submit()` 命令：

  ```
  cy.get('form').submit();
  ```
对于键盘事件，例如在输入字段中键入内容，请使用 `.type()` 命令：

  ```
  cy.get('input').type('Hello, World!');
  ```
为了处理更复杂的事件（例如悬停），[Cypress](../C/cypress.md) 本身并不支持用户体验到的 `hover` 事件。相反，您可以使用 `.trigger()` 命令触发相同的功能：

  ```
  cy.get('div').trigger('mouseover');
  ```
对于需要等待特定条件的事件，可以将`.wait()`与其他命令结合使用：

  ```
  cy.wait(1000); // Waits for 1 second
  cy.get('button').click();
  ```
请记住，[Cypress](../C/cypress.md) 会自动等待元素存在，并重试命令，直到元素可操作。这意味着您通常不需要手动处理依赖于先前操作或异步操作的事件。
  对于自定义事件或更复杂的场景，您可以使用`Cypress.Commands.add()`定义自定义命令来封装可重用的事件处理逻辑：

  ```
  Cypress.Commands.add('customEvent', (selector, event) => {
    cy.get(selector).trigger(event);
  });
  // Usage
  cy.customEvent('button', 'customEventName');
  ```
始终确保您了解应用程序的行为，以正确模拟事件并获得可靠的测试结果。

### # 如何在Cypress 中使用灯具？

在[Cypress](../C/cypress.md) 中使用固定装置是一种与[test scripts](../T/test-script.md) 分开管理[test data](../T/test-data.md) 的方法，允许您加载可在多个测试中使用的静态数据。以下是在 [Cypress](../C/cypress.md) 中使用灯具的方法：

1. **创建一个fixture文件** : 将一个JSON文件放入
    `cypress/fixtures`
    目录。例如，
    `user.json`
    可能包含：

  ```
  {
    "id": 1,
    "name": "Jane Doe",
    "email": "jane.doe@example.com"
  }
  ```
1. **加载夹具**：使用
    `cy.fixture()`
    函数加载夹具数据。然后您可以在测试中使用这些数据。

  ```
  describe('Test with fixtures', () => {
    it('Loads data from a fixture', () => {
      cy.fixture('user').then((user) => {
        // user now contains the fixture data
      });
    });
  });
  ```
1. **在测试中使用夹具数据**：加载夹具后，您可以在测试逻辑中使用数据，例如填写表格或与预期值进行比较。

  ```
  cy.get('input[name="name"]').type(user.name);
  cy.get('input[name="email"]').type(user.email);
  ```
1. **加载fixtures的快捷方式** ：您还可以将fixture文件直接传递给命令，例如
    `cy.get()`
    或
    `cy.route()`
    使用
    `@`
    前缀。

  ```
  cy.get('input[name="name"]').type('@user.name');
  ```
1. **别名夹具数据**：为了使测试中的夹具更易于管理，您可以使用以下命令为夹具分配别名
    `as()`
    。

  ```
  cy.fixture('user').as('userData');
  cy.get('@userData').then((user) => {
    // use user data here
  });
  ```
请记住使您的夹具数据保持最新并与您正在执行的测试相关。这将确保您的测试保持可靠和可维护。

1. **创建一个fixture文件** : 将一个JSON文件放入
    `cypress/fixtures`
    目录。例如，
    `user.json`
    可能包含：

1. **加载夹具**：使用
    `cy.fixture()`
    函数加载夹具数据。然后您可以在测试中使用这些数据。

1. **在测试中使用夹具数据**：加载夹具后，您可以在测试逻辑中使用数据，例如填写表格或与预期值进行比较。
  1. **加载fixtures的快捷方式** ：您还可以将fixture文件直接传递给命令，例如
    `cy.get()`
    或
    `cy.route()`
    使用
    `@`
    前缀。

1. **别名夹具数据**：为了使测试中的夹具更易于管理，您可以使用以下命令为夹具分配别名
    `as()`
    。

## # 高级概念

### # Cypress 如何处理异步操作？

[Cypress](../C/cypress.md) 通过在继续下一步之前自动等待命令和断言来处理异步操作。这意味着它将等待元素变得可见、动画完成以及网络请求完成，然后再执行下一个命令。无需在测试中添加显式等待或睡眠。
  例如，当您使用命令获取元素时，[Cypress](../C/cypress.md)将不断重试该命令，直到找到该元素或达到超时。这适用于 [Cypress](../C/cypress.md) 中的大多数命令：

  ```
  cy.get('.some-element') // Cypress will wait for this element to exist
  ```
在处理网络请求时，[Cypress](../C/cypress.md) 提供`cy.wait()` 来等待特定请求完成：

  ```
  cy.wait('@yourRequestAlias')
  ```
您还可以使用`.then()`处理异步请求的响应：

  ```
  cy.request('POST', '/yourEndpoint', yourRequestBody)
    .then((response) => {
      expect(response.body).to.have.property('success', true);
    });
  ```
[Cypress](../C/cypress.md) 确保在 `.then()` 内部的异步操作完成之前测试不会继续。
  对于断言，[Cypress](../C/cypress.md) 使用重试和超时机制。断言将重新运行，直到通过或达到指定的超时：

  ```
  cy.get('.list-item').should('have.length', 5) // Retries until the condition is met or timeout
  ```
这种方法简化了异步操作的处理，使测试更具可读性且不那么不稳定。

### # 如何在Cypress 中使用自定义命令？

在[Cypress](../C/cypress.md) 中使用自定义命令可以通过封装重复任务来增强您的[test suite](../T/test-suite.md)。要定义自定义命令，请将函数添加到`cypress/support` 目录中`commands.js` 文件中的`Cypress.Commands.add` 方法。

  ```
  Cypress.Commands.add('login', (email, password) => {
    cy.get('input[name=email]').type(email);
    cy.get('input[name=password]').type(password);
    cy.get('form').submit();
  });
  ```
使用 `cy` 后跟命令名称来调用测试中的自定义命令：

  ```
  cy.login('user@example.com', 'password123');
  ```
**参数** 可以像任何其他函数一样传递给自定义命令。在上面的示例中，`email` 和`password` 是参数。
  **链接**由自定义命令支持。从自定义命令返回 `cy` 以继续链接 [Cypress](../C/cypress.md) 命令：

  ```
  Cypress.Commands.add('fillForm', data => {
    return cy.get('form').within(() => {
      cy.get('input[name=firstName]').type(data.firstName);
      cy.get('input[name=lastName]').type(data.lastName);
    });
  });
  ```
通过使用相同的 `Cypress.Commands.add` 方法和现有命令的名称，可以**覆盖**现有命令：

  ```
  Cypress.Commands.overwrite('visit', (originalFn, url, options) => {
    // Custom logic before visit
    return originalFn(url, options);
  });
  ```
请记住**记录**您的自定义命令，以确保团队成员了解其目的和用法。通过限制自定义命令的范围和复杂性来保持自定义命令的**可维护性**。

### # 如何处理Cypress 中的网络请求？

可以使用`cy.intercept()` 方法来处理[Cypress](../C/cypress.md) 中的网络请求。这允许您监听、修改或模拟网络请求和响应。
  **拦截GET请求：**

  ```
  cy.intercept('GET', '/api/todos').as('getTodos')
  ```
设置拦截后，您可以使用 `cy.wait()` 等待请求完成：

  ```
  cy.wait('@getTodos').its('response.statusCode').should('eq', 200)
  ```
**修改回复：**
  您可以通过提供静态响应来修改响应：

  ```
  cy.intercept('GET', '/api/todos', { fixture: 'todos.json' })
  ```
**存根回复：**
  要存根响应，您可以直接提供响应：

  ```
  cy.intercept('POST', '/api/todos', {
    statusCode: 201,
    body: { id: 123, title: 'Stubbed task' },
  }).as('createTodo')
  ```
**访问请求和响应：**
  您可以在拦截回调中访问请求和响应对象：

  ```
  cy.intercept('POST', '/api/todos', (req) => {
    req.body.title = 'Modified title'
  }).as('createTodo')
  ```
**链接断言：**
  您可以将断言链接到拦截的请求：

  ```
  cy.wait('@createTodo').then(({ request, response }) => {
    expect(request.body).to.have.property('title', 'Modified title')
    expect(response.statusCode).to.eq(201)
  })
  ```
使用`cy.intercept()` 获得对网络请求和响应的完全控制，使您能够测试应用程序在各种场景下的行为。

### # 如何使用 Cypress 中的 cookie 和本地存储？

由于其内置命令，[Cypress](../C/cypress.md) 中的 cookie 和本地存储的使用非常简单。
  **饼干：**
  要按名称获取 cookie：

  ```
  cy.getCookie('session_id').should('exist')
  ```
获取所有cookie：

  ```
  cy.getCookies().should('have.length', 1)
  ```
设置 cookie：

  ```
  cy.setCookie('session_id', 'abc123')
  ```
要清除特定的 cookie：

  ```
  cy.clearCookie('session_id')
  ```
要清除所有 cookie：

  ```
  cy.clearCookies()
  ```
**本地存储：**
  要在本地存储中设置项目：

  ```
  cy.setLocalStorage('cart', JSON.stringify({ items: 1 }))
  ```
要从本地存储获取项目：

  ```
  cy.getLocalStorage('cart').should('equal', '{"items":1}')
  ```
要从本地存储中清除特定项目：

  ```
  cy.removeLocalStorage('cart')
  ```
清除所有本地存储数据：

  ```
  cy.clearLocalStorage()
  ```
或者使用特定的键模式清除本地存储：

  ```
  cy.clearLocalStorage(/cart/)
  ```
请记住，这些命令是异步的并返回承诺，因此它们应该与 [Cypress](../C/cypress.md) 的链接机制一起使用。此外，本地存储操作通常在被测应用程序的上下文中执行，因此请确保在尝试与本地存储交互之前加载正确的页面。

### # 如何处理 Cypress 中的 iframe？

处理 [Cypress](../C/cypress.md) 中的 iframe 需要一些额外的步骤，因为 [Cypress](../C/cypress.md) 命令被设计为在同源上下文中操作。这是一个简洁的指南：

1. **定位 iframe**
    - 使用
    `cy.get()`
    抓取 iframe 元素。

  ```
  cy.get('iframe')
  ```
1. **访问iframe的内容**
    - 使用
    `.its('contentDocument.body')`
    获取iframe的body，该iframe受同源策略限制。

  ```
  cy.get('iframe').its('contentDocument.body').should('not.be.empty').then(cy.wrap)
  ```
1. **与元素交互**
    - 包装后，您可以与 iframe 内的元素进行交互，就像与 Cypress 中的任何其他元素进行交互一样。

  ```
  cy.get('iframe').its('contentDocument.body').should('not.be.empty').then(cy.wrap).find('selector').click()
  ```
请记住，对于跨源 iframe，您需要在 `cypress.json` 配置文件中设置 `"chromeWebSecurity": false` 以绕过这些限制。但是，出于安全原因，不建议这样做，并且仅应在绝对必要时使用。
  如果您正在处理多个嵌套 iframe，则需要对每个级别的 iframe 嵌套重复该过程，以确保您在每个级别都定位正确的 iframe。
  请记住，[Cypress](../C/cypress.md) 最佳实践建议尽可能避免使用 iframe，因为它们会增加测试的复杂性。如果您可以控制应用程序，请考虑更适合测试的 iframe 替代方案。

1. **定位 iframe**
    - 使用
    `cy.get()`
    抓取 iframe 元素。

1. **访问iframe的内容**
    - 使用
    `.its('contentDocument.body')`
    获取iframe的body，该iframe受同源策略限制。

1. **与元素交互**
    - 包装后，您可以与 iframe 内的元素进行交互，就像与 Cypress 中的任何其他元素进行交互一样。

### # 如何使用Cypress中的插件？

在[Cypress](../C/cypress.md) 中使用插件可以通过扩展其核心功能来增强其功能。要使用插件，请按照下列步骤操作：

1. **通过npm安装插件**。例如，要安装 `cypress-file-upload` 插件，请运行：

    ```
    npm install --save-dev cypress-file-upload
    ```
2. **将插件包含在项目的 `cypress/plugins/index.js` 文件中。您可以在此处修改或扩展[Cypress](../C/cypress.md) 的内部行为。例如：

    ```
    module.exports = (on, config) => {
      // your plugin code here
    }
    ```
3. **根据需要在测试文件中导入并使用插件**。例如，使用`cypress-file-upload`，您可以将以下内容添加到测试文件中：

    ```
    import 'cypress-file-upload';
    ```
4. **在测试中利用插件的功能**。对于 `cypress-file-upload` 插件，您现在可以使用 `.attachFile()` 命令：

    ```
    cy.get('input[type="file"]').attachFile('file.json');
    ```
请记住**检查插件的文档**以获取具体的使用说明以及与您的 [Cypress](../C/cypress.md) 版本的兼容性。某些插件可能需要额外的配置或初始化步骤。
  插件可以提供各种功能，例如自定义命令、改进的报告或与其他工具的集成。在将插件添加到您的项目之前，始终**确保该插件得到积极维护**并且非常适合您的需求。

1. **通过npm安装插件**。例如，要安装 `cypress-file-upload` 插件，请运行：

    ```
    npm install --save-dev cypress-file-upload
    ```
2. **将插件包含在项目的 `cypress/plugins/index.js` 文件中。您可以在此处修改或扩展[Cypress](../C/cypress.md) 的内部行为。例如：

    ```
    module.exports = (on, config) => {
      // your plugin code here
    }
    ```
3. **根据需要在测试文件中导入并使用插件**。例如，使用`cypress-file-upload`，您可以将以下内容添加到测试文件中：

    ```
    import 'cypress-file-upload';
    ```
4. **在测试中利用插件的功能**。对于 `cypress-file-upload` 插件，您现在可以使用 `.attachFile()` 命令：

    ```
    cy.get('input[type="file"]').attachFile('file.json');
    ```
## # 最佳实践和故障排除

### # 在 Cypress 中编写测试的最佳实践有哪些？

在 [Cypress](../C/cypress.md) 中编写测试时，请考虑以下最佳实践：

- **逻辑地组织测试**
    使用
    `describe`
    和
    `context`
    块以获得更好的可读性和结构。

- **使用`it`块**
    对于单个测试用例，确保它们具有描述性并反映您正在测试的用户行为。

- **保持测试隔离和独立**
    以避免可能导致不稳定的测试间依赖性。

- **使用[Page Object Model](../P/page-object-model.md)**
    或类似的模式来抽象元素选择器和页面交互，从而增强可维护性。

- **利用[Cypress](../C/cypress.md)的内置重试能力**
    用于处理动态内容并减少不稳定的命令和断言。

- **避免使用任意等待**
    （
    `cy.wait()`
    有固定时间）；相反，依赖 Cypress 自动等待元素存在、可见、可点击等。

- **利用[Cypress](../C/cypress.md)别名**
    与
    `cy.as()`
    用于重用命令链中的元素或响应。

- **编写自定义命令**
    用于可重复使用的操作序列，但要明智地使用它们以保持测试的清晰度。

- **对真实用户交互进行断言**
    和结果，而不是实现细节，以确保测试在代码更改时仍然有效。

- **测试关键用户旅程**
    首先提供即时价值并尽早发现重大回归。

- **使用环境变量**
    用于配置以将敏感数据排除在测试代码之外，并允许跨不同环境的灵活性。

- **实施持续集成**
    自动对代码更改运行测试，确保立即反馈应用程序的运行状况。

  ```
  // Example of a descriptive test case
  describe('User Profile', () => {
    it('should allow a user to update their profile picture', () => {
      cy.get('.profile-pic').click();
      cy.get('input[type="file"]').attachFile('new-pic.jpg');
      cy.get('.save-btn').click();
      cy.get('.profile-pic').should('have.attr', 'src', 'path/to/new-pic.jpg');
    });
  });
  ```
请记住**定期审查和重构测试**以适应应用程序更改并提高[test suite](../T/test-suite.md)可靠性和性能。

- **逻辑地组织测试**
    使用
    `describe`
    和
    `context`
    块以获得更好的可读性和结构。

- **使用`it`块**
    对于单个测试用例，确保它们具有描述性并反映您正在测试的用户行为。

- **保持测试隔离和独立**
    以避免可能导致不稳定的测试间依赖性。

- **使用[Page Object Model](../P/page-object-model.md)**
    或类似的模式来抽象元素选择器和页面交互，从而增强可维护性。

- **利用[Cypress](../C/cypress.md)的内置重试能力**
    用于处理动态内容并减少不稳定的命令和断言。

- **避免使用任意等待**
    （
    `cy.wait()`
    有固定时间）；相反，依赖Cypress自动等待元素存在、可见、可点击等。

- **利用[Cypress](../C/cypress.md)别名**
    与
    `cy.as()`
    用于重用命令链中的元素或响应。

- **编写自定义命令**
    用于可重复使用的操作序列，但要明智地使用它们以保持测试的清晰度。

- **对真实用户交互进行断言**
    和结果，而不是实现细节，以确保测试在代码更改时仍然有效。

- **测试关键用户旅程**
    首先提供即时价值并尽早发现重大回归。

- **使用环境变量**
    用于配置以将敏感数据排除在测试代码之外，并允许跨不同环境的灵活性。

- **实施持续集成**
    自动对代码更改运行测试，确保立即反馈应用程序的运行状况。

### # 如何在Cypress 中调试测试？

可以系统地进行[Cypress](../C/cypress.md) 中的调试测试：

1. **使用[Cypress](../C/cypress.md) [Test Runner](../T/test-runner.md)**：它提供[test execution](../T/test-execution.md) 的视觉表示。您可以在命令运行时查看命令，并在每个步骤检查应用程序的状态。
  2. **时间旅行**：[Cypress](../C/cypress.md) 在测试运行时拍摄快照。将鼠标悬停在命令日志中的命令上可准确查看每个步骤发生的情况。
  3. **实时重新加载**：只要您对测试进行更改，[Cypress](../C/cypress.md)就会自动重新加载。您可以立即看到测试结果。
  4. **控制台输出**：检查浏览器的开发者控制台的日志。 [Cypress](../C/cypress.md) 命令在此处记录附加信息，这对于调试很有用。
  5. **`.debug()` 命令**：将 `.debug()` 插入命令链以检查 DOM 此时的状态。它将导致浏览器的调试器启动。

    ```
    cy.get('.selector').debug().should('have.text', 'expected text');
    ```
6. **断点**：在测试代码中使用 `debugger` 语句在特定行暂停执行。

    ```
    cy.get('.selector').then(($el) => {
      debugger; // Execution will pause here
    });
    ```
7. **网络请求**：检查 [Test Runner](../T/test-runner.md) 的命令日志中的网络请求，以确保 [API](../A/api.md) 调用按预期进行且数据正确。
  8. **错误消息**：仔细阅读错误消息。 [Cypress](../C/cypress.md) 提供描述性错误消息，可以指导您找到问题的根源。
  9. **[Cypress](../C/cypress.md) 日志**：通过设置`Cypress.config('log', true)` 启用详细日志记录，以获取有关[test execution](../T/test-execution.md) 的更多详细信息。
  10. **重试能力**：了解 [Cypress](../C/cypress.md) 命令会自动重试，直到成功或超时。如果测试因应用程序准备就绪之前运行断言而失败，请考虑为中间状态添加等待或断言。
  通过结合这些工具和技术，您可以有效地调试 [Cypress](../C/cypress.md) 测试并更快地解决问题。

1. **使用[Cypress](../C/cypress.md) [Test Runner](../T/test-runner.md)**：它提供[test execution](../T/test-execution.md) 的视觉表示。您可以在命令运行时查看命令，并在每个步骤检查应用程序的状态。
  2. **时间旅行**：[Cypress](../C/cypress.md) 在测试运行时拍摄快照。将鼠标悬停在命令日志中的命令上可准确查看每个步骤发生的情况。
  3. **实时重新加载**：只要您对测试进行更改，[Cypress](../C/cypress.md)就会自动重新加载。您可以立即看到测试结果。
  4. **控制台输出**：检查浏览器的开发者控制台的日志。 [Cypress](../C/cypress.md) 命令在此处记录附加信息，这对于调试很有用。
  5. **`.debug()` 命令**：将 `.debug()` 插入命令链以检查 DOM 此时的状态。它将导致浏览器的调试器启动。

    ```
    cy.get('.selector').debug().should('have.text', 'expected text');
    ```
6. **断点**：在测试代码中使用 `debugger` 语句在特定行暂停执行。

    ```
    cy.get('.selector').then(($el) => {
      debugger; // Execution will pause here
    });
    ```
7. **网络请求**：检查 [Test Runner](../T/test-runner.md) 的命令日志中的网络请求，以确保 [API](../A/api.md) 调用按预期进行且数据正确。
  8. **错误消息**：仔细阅读错误消息。 [Cypress](../C/cypress.md) 提供描述性错误消息，可以指导您找到问题的根源。
  9. **[Cypress](../C/cypress.md) 日志**：通过设置`Cypress.config('log', true)` 启用详细日志记录，以获取有关[test execution](../T/test-execution.md) 的更多详细信息。
  10. **重试能力**：了解 [Cypress](../C/cypress.md) 命令会自动重试，直到成功或超时。如果测试因应用程序准备就绪之前运行断言而失败，请考虑为中间状态添加等待或断言。

### # 如何处理Cypress 中的常见错误？

处理 [Cypress](../C/cypress.md) 中的常见错误涉及了解错误消息并应用适当的修复或解决方法。以下是一些策略：
  **超时错误**：如果元素加载时间较长，请使用 `cy.wait()` 或在 `cypress.json` 中全局增加默认超时设置。

  ```
  cy.get('.some-element', { timeout: 10000 }) // waits for 10 seconds
  ```
**未找到元素**：在与元素交互之前，确保DOM 中元素可用。使用 `.should('be.visible')` 等待元素出现。

  ```
  cy.get('.some-element').should('be.visible').click()
  ```
**跨源错误**：如果需要绕过同源策略，请在`cypress.json`中配置`chromeWebSecurity`到`false`。

  ```
  {
    "chromeWebSecurity": false
  }
  ```
**[Flaky Tests](../F/flaky-test.md)**：通过使用 `.retry()` 来解决可能因计时问题而失败的断言或命令的不稳定问题。

  ```
  cy.get('.some-element').should('exist').retry()
  ```
**断言失败**：检查预期条件并确保断言与实际应用程序状态匹配。使用显式断言，如 `.should('have.text', 'expected text')`。

  ```
  cy.get('.some-element').should('have.text', 'expected text')
  ```
**网络错误**：使用 `cy.intercept()` 存根网络请求来控制响应并避免外部依赖。

  ```
  cy.intercept('GET', '/api/data', { fixture: 'data.json' })
  ```
**未处理的 Promise 拒绝**：使用 `.catch()` 处理测试中的 Promise 拒绝并避免未捕获的异常。

  ```
  cy.task('mightFail').catch((error) => {
    // handle error
  })
  ```
**[Cypress](../C/cypress.md) 命令队列错误**：请记住，[Cypress](../C/cypress.md) 命令是异步且排队的。避免将传统的 async/await 与 [Cypress](../C/cypress.md) 命令一起使用。
  对于更复杂或持续存在的错误，请参阅[Cypress](../C/cypress.md) 文档或社区论坛以获取特定的解决方案和故障排除提示。

### # 如何优化 Cypress 中的测试执行时间？

要优化 [Cypress](../C/cypress.md) 中的 [test execution](../T/test-execution.md) 时间，请考虑以下策略：

- **并行运行测试**：利用[Cypress](../C/cypress.md) Dashboard Service 在多台机器上同时运行测试。这可以显着减少[test suite](../T/test-suite.md) 的总体执行时间。

    ```
    cypress run --record --key <record_key> --parallel
    ```
- **选择性[test execution](../T/test-execution.md)**：使用`.only` 运行特定测试或在开发期间使用[test suites](../T/test-suite.md) 以避免运行整个套件。

    ```
    describe.only('My Test Suite', () => {
      // Only this suite will run
    });
    it.only('My Test', () => {
      // Only this test will run
    });
    ```
- **测试重试**：实施测试重试来处理[flaky tests](../F/flaky-test.md)，而无需重新运行整个套件。

    ```
    // Global level
    Cypress.config('retries', 2);
    // Test-specific level
    it('retries test', { retries: 2 }, () => {
      // Test code here
    });
    ```
- **智能等待**：使用[Cypress](../C/cypress.md)的自动等待元素和断言，以避免不必要的等待和超时。
  - **存根和拦截**：使用 `cy.intercept()` 将实际的网络调用替换为存根，以节省花费在实际网络请求上的时间。

    ```
    cy.intercept('GET', '/users', { fixture: 'users.json' });
    ```
- **避免不必要的 UI 操作**：使用直接 [API](../A/api.md) 调用来设置应用程序状态，而不是通过 UI 工作流程。

    ```
    cy.request('POST', '/login', { username: 'user', password: 'pass' });
    ```
- **缓存资源**：缓存测试之间不经常更改的数据，以避免重新加载。
  - **优化选择器**：使用高效的选择器来减少[Cypress](../C/cypress.md) 查询DOM 所花费的时间。
  - **批量操作**：对可以一起执行的操作或命令进行分组，以最大程度地减少可生成的 [Cypress](../C/cypress.md) 命令的数量。
  通过实施这些策略，您可以在[Cypress](../C/cypress.md) 中实现更快的反馈周期和更高效的[test execution](../T/test-execution.md)。

- **并行运行测试**：利用[Cypress](../C/cypress.md) Dashboard Service 在多台机器上同时运行测试。这可以显着减少[test suite](../T/test-suite.md) 的总体执行时间。

    ```
    cypress run --record --key <record_key> --parallel
    ```
- **选择性[test execution](../T/test-execution.md)**：使用`.only` 运行特定测试或在开发期间使用[test suites](../T/test-suite.md) 以避免运行整个套件。

    ```
    describe.only('My Test Suite', () => {
      // Only this suite will run
    });
    it.only('My Test', () => {
      // Only this test will run
    });
    ```
- **测试重试**：实施测试重试来处理[flaky tests](../F/flaky-test.md)，而无需重新运行整个套件。

    ```
    // Global level
    Cypress.config('retries', 2);
    // Test-specific level
    it('retries test', { retries: 2 }, () => {
      // Test code here
    });
    ```
- **智能等待**：使用[Cypress](../C/cypress.md)的自动等待元素和断言，以避免不必要的等待和超时。
  - **存根和拦截**：使用 `cy.intercept()` 将实际的网络调用替换为存根，以节省花费在实际网络请求上的时间。

    ```
    cy.intercept('GET', '/users', { fixture: 'users.json' });
    ```
- **避免不必要的 UI 操作**：使用直接 [API](../A/api.md) 调用来设置应用程序状态，而不是通过 UI 工作流程。

    ```
    cy.request('POST', '/login', { username: 'user', password: 'pass' });
    ```
- **缓存资源**：缓存测试之间不经常更改的数据，以避免重新加载。
  - **优化选择器**：使用高效的选择器来减少[Cypress](../C/cypress.md) 查询DOM 所花费的时间。
  - **批量操作**：对可以一起执行的操作或命令进行分组，以最大程度地减少可生成的 [Cypress](../C/cypress.md) 命令的数量。
