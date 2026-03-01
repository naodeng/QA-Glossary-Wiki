# BrowserStack




<!-- TOC START -->
- [# 另请参阅：](##-另请参阅：)
- [# 基础知识和重要性](##-基础知识和重要性)
  - [# BrowserStack 是什么？](##-browserstack-是什么？)
  - [# 为什么BrowserStack 对于软件测试很重要？](##-为什么browserstack-对于软件测试很重要？)
  - [# BrowserStack 的主要功能是什么？](##-browserstack-的主要功能是什么？)
  - [# BrowserStack 如何提高软件测试的质量？](##-browserstack-如何提高软件测试的质量？)
  - [# 使用BrowserStack 可以执行哪些类型的测试？](##-使用browserstack-可以执行哪些类型的测试？)
- [# 功能和用法](##-功能和用法)
  - [# BrowserStack 如何工作？](##-browserstack-如何工作？)
  - [# 如何设置并开始使用BrowserStack？](##-如何设置并开始使用browserstack？)
  - [# 对BrowserStack 执行测试的步骤是什么？](##-对browserstack-执行测试的步骤是什么？)
  - [# 如何使用 BrowserStack 进行移动测试？](##-如何使用-browserstack-进行移动测试？)
  - [# BrowserStack 如何处理不同的浏览器和操作系统？](##-browserstack-如何处理不同的浏览器和操作系统？)
  - [# 我可以使用 BrowserStack 进行自动化测试吗？](##-我可以使用-browserstack-进行自动化测试吗？)
- [# 集成和兼容性](##-集成和兼容性)
  - [# BrowserStack 如何与其他测试工具集成？](##-browserstack-如何与其他测试工具集成？)
  - [# BrowserStack 与持续集成工具兼容吗？](##-browserstack-与持续集成工具兼容吗？)
  - [# 我可以将BrowserStack 与Selenium 一起使用吗？](##-我可以将browserstack-与selenium-一起使用吗？)
  - [# BrowserStack 如何与 Jenkins 集成？](##-browserstack-如何与-jenkins-集成？)
  - [# 还有哪些其他工具和框架可以与 BrowserStack 一起使用？](##-还有哪些其他工具和框架可以与-browserstack-一起使用？)
- [# 高级功能](##-高级功能)
  - [# BrowserStack 有哪些高级功能？](##-browserstack-有哪些高级功能？)
  - [# BrowserStack 中的“实时测试”功能如何工作？](##-browserstack-中的实时测试功能如何工作？)
  - [# BrowserStack 中的“Automate Pro”是什么？](##-browserstack-中的automate-pro是什么？)
  - [# 如何使用 BrowserStack 中的“App Live”功能？](##-如何使用-browserstack-中的app-live功能？)
  - [# BrowserStack 中的“屏幕截图”功能是什么？](##-browserstack-中的屏幕截图功能是什么？)
<!-- TOC END -->

BrowserStack

是一个基于云的 Web 和移动测试平台，允许开发人员和测试人员跨多个浏览器、操作系统和真实移动设备查看其网站和应用程序并与之交互，而无需虚拟机或设备的内部实验室。它提供对各种浏览器和操作系统组合的即时访问，确保开发人员可以在现实条件下测试他们的产品。这有助于识别和解决在单个平台或浏览器上可能不明显的兼容性问题。

BrowserStack

特别有利于确保跨浏览器和跨平台兼容性，并且它与许多流行的持续集成工具集成以简化测试过程。

# # 相关术语：

- [Cross-Browser Testing tool](../C/cross-browser-testing-tool.md)

## # 另请参阅：

- [Official Website](https://www.browserstack.com/)
- [Wikipedia](https://en.wikipedia.org/wiki/BrowserStack)

# # 关于BrowserStack 有疑问吗？

## # 基础知识和重要性

### # BrowserStack 是什么？

[BrowserStack](../B/browserstack.md) 是一个基于云的 **[cross-browser testing](../C/cross-browser-testing.md) 平台**，使开发人员和 QA 专业人员能够在各种浏览器、操作系统和真实移动设备上测试他们的网站和移动应用程序。它提供对大量浏览器和设备的访问，无需维护内部测试基础设施。
  借助[BrowserStack](../B/browserstack.md)，您可以使用[Selenium](../S/selenium.md)、Appium 和[Cypress](../C/cypress.md) 等流行框架进行**交互式[manual testing](../M/manual-testing.md)** 或运行**自动化测试**。它支持各种编程语言，包括Java、Python和Ruby，允许无缝集成到现有[test suites](../T/test-suite.md)。
  设置[BrowserStack](../B/browserstack.md) 涉及创建帐户、使用提供的访问凭据配置您的[test scripts](../T/test-script.md)，以及通过平台的云基础设施运行测试。您可以直接从 CI/CD 管道启动测试，因为 [BrowserStack](../B/browserstack.md) 提供与 Jenkins、Travis CI 和 CircleCI 等工具的集成。
  对于移动测试，[BrowserStack](../B/browserstack.md) 的 **App Live** 和 **App Automate** 功能支持测试本机和混合移动应用程序。您可以上传应用程序版本并在真实设备上与它们交互或自动化测试过程。
  [BrowserStack](../B/browserstack.md) 的 **屏幕截图** 功能允许您跨多个浏览器和设备捕获和比较屏幕截图，从而促进 [visual regression testing](../V/visual-regression-testing.md)。
  该平台的 **Automate Pro** 计划提供并行测试、IP 白名单和 [priority](../P/priority.md) 支持等高级功能，可以显着加快测试过程并增强安全性。
  总体而言，[BrowserStack](../B/browserstack.md) 简化了测试工作流程，确保应用程序在所有用户接触点上完美运行。

### # 为什么BrowserStack 对于软件测试很重要？

[BrowserStack](../B/browserstack.md) 对于[software testing](../S/software-testing.md) 至关重要，因为它具有**跨浏览器[compatibility testing](../C/compatibility-testing.md)** 功能。它允许测试人员验证应用程序是否可以在多种浏览器和设备上无缝运行，而无需内部设备实验室。随着用户环境的多样性不断增长，浏览器和操作系统版本不断变化，这一点尤其重要。
  通过提供对**真实设备和浏览器**的访问，[BrowserStack](../B/browserstack.md) 确保测试反映实际用户条件，从而获得比仿真器或模拟器更准确的结果。这个真实世界的测试环境有助于发现边缘情况和[bugs](../B/bug.md)，这些情况可能仅在模拟器无法复制的特定条件下出现。
  此外，[BrowserStack](../B/browserstack.md) 的 **基于云的基础设施** 提供可扩展性和灵活性。测试人员可以并行运行多个测试，从而显着减少大量 [test suites](../T/test-suite.md) 所需的时间。这对于旨在快速 [iteration](../I/iteration.md) 和持续交付的敏捷和 DevOps 团队至关重要。
  该服务与**CI/CD 管道**和[Selenium](../S/selenium.md) 等流行自动化框架的集成功能增强了其重要性。它允许自动回归测试成为构建过程的一部分，确保新的代码更改不会破坏现有功能。
  最后，[BrowserStack](../B/browserstack.md) 的**安全功能**确保测试在安全的环境中完成，这是处理敏感数据的企业的关键考虑因素。这使其成为一个值得信赖的工具，不仅可以用于功能测试，还可以用于测试需要遵守严格安全标准的应用程序。

### # BrowserStack 的主要功能是什么？

[BrowserStack](../B/browserstack.md) 的主要功能包括：

- **[Cross-browser Testing](../C/cross-browser-testing.md)** ：在一系列真实的浏览器和操作系统上进行测试，无需维护内部实验室。
  - **真实设备云**：访问大量真实移动设备，以获得更准确的测试结果。
  - **本地测试**：使用本地测试功能安全地测试开发和登台环境。
  - **并行测试**：同时运行多个测试以减少执行时间。
  - **集成**：与流行的 CI/CD 工具（如 Jenkins、Travis CI 和 CircleCI）无缝集成。
  - **交互式测试**：在桌面和移动设备上手动测试和调试。
  - **自动屏幕截图和视频**：自动捕获测试的屏幕截图和视频以进行视觉回归和文档记录。
  - **地理位置测试**：模拟和测试基于地理位置的场景。
  - **响应测试**：评估不同设备上 Web 应用程序的响应能力。
  - **DevTools** ：Chrome 用于在桌面浏览器上进行调试和分析的 DevTools。
  - **网络节流**：在不同网络条件下测试应用程序。
  - **企业功能**：SSO、优先级支持、团队管理和满足企业需求的使用情况分析。

  ```
  // Example of initiating a parallel test session in BrowserStack using Selenium WebDriver
  const { Builder } = require('selenium-webdriver');
  const capabilities = {
    'browserName': 'chrome',
    'browserstack.user': 'YOUR_USERNAME',
    'browserstack.key': 'YOUR_ACCESS_KEY'
  };
  async function runTest() {
    let driver = new Builder()
      .usingServer('http://hub-cloud.browserstack.com/wd/hub')
      .withCapabilities(capabilities)
      .build();
    try {
      await driver.get('http://www.google.com');
      // Your test code here
    } finally {
      await driver.quit();
    }
  }
  runTest();
  ```
除其他功能外，这些功能使 [BrowserStack](../B/browserstack.md) 成为用于 Web 和移动应用程序测试的多功能平台。

- **[Cross-browser Testing](../C/cross-browser-testing.md)** ：在一系列真实的浏览器和操作系统上进行测试，无需维护内部实验室。
  - **真实设备云**：访问大量真实移动设备，以获得更准确的测试结果。
  - **本地测试**：使用本地测试功能安全地测试开发和登台环境。
  - **并行测试**：同时运行多个测试以减少执行时间。
  - **集成**：与流行的 CI/CD 工具（如 Jenkins、Travis CI 和 CircleCI）无缝集成。
  - **交互式测试**：在桌面和移动设备上手动测试和调试。
  - **自动屏幕截图和视频**：自动捕获测试的屏幕截图和视频以进行视觉回归和文档记录。
  - **地理位置测试**：模拟和测试基于地理位置的场景。
  - **响应测试**：评估不同设备上 Web 应用程序的响应能力。
  - **DevTools** ：Chrome DevTools，用于在桌面浏览器上进行调试和分析。
  - **网络节流**：在不同网络条件下测试应用程序。
  - **企业功能**：SSO、优先级支持、团队管理和满足企业需求的使用情况分析。

### # BrowserStack 如何提高软件测试的质量？

[BrowserStack](../B/browserstack.md) 通过提供**对各种真实设备和浏览器的访问**来增强[software testing](../S/software-testing.md) 质量。这种多样性确保应用程序在密切反映最终用户环境的条件下进行测试，从而检测到在模拟器或有限设备上进行测试时可能会错过的**边缘情况问题**。
  凭借**并行测试功能**，[test suites](../T/test-suite.md)可以在多个环境中同时执行，从而显着减少全面测试所需的时间并加快开发团队的反馈循环。
  **本地测试**允许对开发和登台环境进行安全测试，确保应用程序在发布到生产环境之前经过彻底审查。此功能对于识别特定于环境的 [bugs](../B/bug.md) 至关重要。
  [BrowserStack](../B/browserstack.md) **与 Jenkins 等流行的 CI/CD 工具**集成，以及与 [Selenium](../S/selenium.md) 等框架的兼容性，可以无缝包含在自动化管道中。此集成支持**持续测试实践**，这对于敏捷和 DevOps 工作流程至关重要。
  该平台的**可靠性和可扩展性**确保自动化测试一致运行，减少可能破坏[automated testing](../A/automated-testing.md)进程信任的[false positives](../F/false-positive.md)。此外，[BrowserStack](../B/browserstack.md) 的**高级功能**（如地理位置测试和各种网络条件）允许更细致的测试场景，进一步改进[test coverage](../T/test-coverage.md) 和[quality assurance](../Q/quality-assurance.md)。
  总之，[BrowserStack](../B/browserstack.md) 全面的设备和浏览器覆盖、并行测试、本地测试功能和无缝集成有助于实现更稳健、高效和可靠的测试流程，最终交付更高质量的软件。

### # 使用BrowserStack 可以执行哪些类型的测试？

使用[BrowserStack](../B/browserstack.md)，[test automation](../T/test-automation.md) 工程师可以执行各种测试，以确保跨不同设备和平台的应用程序质量：

- **[Cross-browser Testing](../C/cross-browser-testing.md)**：跨多个浏览器及其版本验证您的 Web 应用程序的功能和设计。
  - **[Responsive Design](../R/responsive-design.md) 测试**：检查您的 Web 应用程序如何适应不同的屏幕尺寸和分辨率。
  - **[Regression Testing](../R/regression-testing.md)**：应用程序更改后自动重新运行[test cases](../T/test-case.md)，以确保现有功能不受影响。
  - **[Performance Testing](../P/performance-testing.md)**：使用[BrowserStack](../B/browserstack.md) 的性能工具测量应用程序在各种条件下的响应能力和稳定性。
  - **[Localization Testing](../L/localization-testing.md)**：在不同的地理设置中测试您的应用程序，以确保它在不同的区域设置中正常运行。
  - **[Accessibility Testing](../A/accessibility-testing.md)**：使用[BrowserStack](../B/browserstack.md) 确保残障用户可以访问您的应用程序，并符合 WCAG 等标准。
  - **交互式测试**：出于 [exploratory testing](../E/exploratory-testing.md) 目的，在各种真实设备上手动与您的应用程序进行交互。
  - **视觉测试**：比较不同设备和浏览器上的应用程序屏幕截图，以发现 UI 不一致的地方。
  - **自动化[Screenshot Testing](../S/screenshot-testing.md)**：大规模捕获和比较屏幕截图以验证应用程序的视觉方面。
  - **[Mobile App Testing](../M/mobile-app-testing.md)**：在大量精选的真实iOS 和 Android 设备上测试本机和混合移动应用程序。
  - **[Integration Testing](../I/integration-testing.md)**：将 [BrowserStack](../B/browserstack.md) 与 CI/CD 管道结合起来，作为开发过程的一部分运行测试。
  这些测试可以使用[Selenium](../S/selenium.md)、Appium、[Cypress](../C/cypress.md) 等流行的框架和工具来执行，[BrowserStack](../B/browserstack.md) 支持这些框架和工具，以便无缝集成到现有的[test suites](../T/test-suite.md) 中。

- **[Cross-browser Testing](../C/cross-browser-testing.md)**：跨多个浏览器及其版本验证您的 Web 应用程序的功能和设计。
  - **[Responsive Design](../R/responsive-design.md) 测试**：检查您的 Web 应用程序如何适应不同的屏幕尺寸和分辨率。
  - **[Regression Testing](../R/regression-testing.md)**：应用程序更改后自动重新运行[test cases](../T/test-case.md)，以确保现有功能不受影响。
  - **[Performance Testing](../P/performance-testing.md)**：使用[BrowserStack](../B/browserstack.md) 的性能工具测量应用程序在各种条件下的响应能力和稳定性。
  - **[Localization Testing](../L/localization-testing.md)**：在不同的地理设置中测试您的应用程序，以确保它在不同的区域设置中正常运行。
  - **[Accessibility Testing](../A/accessibility-testing.md)**：使用[BrowserStack](../B/browserstack.md) 确保残障用户可以访问您的应用程序，并符合 WCAG 等标准。
  - **交互式测试**：出于 [exploratory testing](../E/exploratory-testing.md) 目的，在各种真实设备上手动与您的应用程序进行交互。
  - **视觉测试**：比较不同设备和浏览器上的应用程序屏幕截图，以发现 UI 不一致的地方。
  - **自动化[Screenshot Testing](../S/screenshot-testing.md)**：大规模捕获和比较屏幕截图以验证应用程序的视觉方面。
  - **[Mobile App Testing](../M/mobile-app-testing.md)**：在大量精选的真实iOS 和 Android 设备上测试本机和混合移动应用程序。
  - **[Integration Testing](../I/integration-testing.md)**：将 [BrowserStack](../B/browserstack.md) 与 CI/CD 管道结合起来，作为开发过程的一部分运行测试。

## # 功能和用法

### # BrowserStack 如何工作？

[BrowserStack](../B/browserstack.md) 通过提供基于云的平台来运行，用户可以在该平台上访问各种**真实设备**、**浏览器**和**操作系统**以进行测试。启动测试时，[BrowserStack](../B/browserstack.md) 根据测试要求从其设备场分配虚拟机或真实设备。
  对于 [automated testing](../A/automated-testing.md)，您通常会使用 **[Selenium](../S/selenium.md)** 或 **Appium** 等框架编写 [test scripts](../T/test-script.md)，然后配置这些脚本以使用提供的 **[APIs](../A/api.md)** 和 **访问密钥** 与 [BrowserStack](../B/browserstack.md) 服务器进行通信。以下是 JavaScript 中使用 WebDriverIO 和 [Selenium](../S/selenium.md) 的简化示例：

  ```
  const { remote } = require('webdriverio');
  async function runTestOnBrowserStack() {
    const browserStackOptions = {
      os: 'Windows',
      os_version: '10',
      browserName: 'Chrome',
      browser_version: 'latest',
      'browserstack.user': 'YOUR_USERNAME',
      'browserstack.key': 'YOUR_ACCESS_KEY'
    };
    const driver = await remote({
      capabilities: browserStackOptions,
      host: 'hub.browserstack.com',
      port: 80
    });
    await driver.url('https://www.yourwebsite.com');
    // Your test steps go here
    await driver.deleteSession();
  }
  runTestOnBrowserStack();
  ```
该脚本连接到[BrowserStack](../B/browserstack.md)，然后启动指定的环境。该测试的运行就像在本地执行一样，但它实际上是在 [BrowserStack](../B/browserstack.md) 服务器上运行。这允许跨不同环境进行**并行测试**，从而显着加快测试过程。
  [BrowserStack](../B/browserstack.md) 的基础设施旨在处理测试环境的**[setup](../S/setup.md)、维护**和**拆卸**，这简化了测试工作流程，让您能够专注于编写和执行测试。测试完成后，[BrowserStack](../B/browserstack.md) 会提供**详细日志**、**屏幕截图**和**视频录制**来帮助调试任何问题。

### # 如何设置并开始使用BrowserStack？

要为 [test automation](../T/test-automation.md) 设置并开始使用 [BrowserStack](../B/browserstack.md)，请按照以下步骤操作：

1. **注册** [BrowserStack](../B/browserstack.md) 帐户（如果您尚未注册）。
  2. 登录后，导航至 **自动化** 部分以访问您的自动化仪表板。
  3. **配置您的[test scripts](../T/test-script.md)** 以连接到[BrowserStack](../B/browserstack.md) 的远程服务器。您需要在测试代码中设置[BrowserStack](../B/browserstack.md) 的URL 并访问凭据。使用[BrowserStack](../B/browserstack.md) 帐户中提供的用户名和访问密钥。

    ```
    const capabilities = {
      'browserName' : 'Chrome',
      'browserstack.user' : 'YOUR_USERNAME',
      'browserstack.key' : 'YOUR_ACCESS_KEY'
    }
    ```
4. **通过在测试功能中指定来选择测试所需的浏览器和操作系统**配置。
  5. **使用您首选的[test runner](../T/test-runner.md) 运行您的[test scripts](../T/test-script.md)**。您的测试现在将在[BrowserStack](../B/browserstack.md) 的远程浏览器/设备上执行。
  6. 通过[BrowserStack](../B/browserstack.md) Automate 仪表板实时监控您的测试，您可以在其中查看测试进度、视频记录、日志和屏幕截图。
  7. **分析测试结果**并使用[BrowserStack](../B/browserstack.md) 提供的详细报告调试问题。
  请记住保护您的[BrowserStack](../B/browserstack.md) 访问凭据，并且不要公开共享它们。为了持续集成，请使用环境变量来存储您的[BrowserStack](../B/browserstack.md) 用户名和访问密钥。与 Jenkins 等 CI 工具集成时，添加 [BrowserStack](../B/browserstack.md) 插件或使用提供的 [API](../A/api.md) 来触发测试作为构建过程的一部分。

1. **注册** [BrowserStack](../B/browserstack.md) 帐户（如果您尚未注册）。
  2. 登录后，导航至 **自动化** 部分以访问您的自动化仪表板。
  3. **配置您的[test scripts](../T/test-script.md)** 以连接到[BrowserStack](../B/browserstack.md) 的远程服务器。您需要在测试代码中设置 [BrowserStack](../B/browserstack.md) 的 URL 和访问凭据。使用[BrowserStack](../B/browserstack.md) 帐户中提供的用户名和访问密钥。

    ```
    const capabilities = {
      'browserName' : 'Chrome',
      'browserstack.user' : 'YOUR_USERNAME',
      'browserstack.key' : 'YOUR_ACCESS_KEY'
    }
    ```
4. **通过在测试功能中指定来选择测试所需的浏览器和操作系统**配置。
  5. **使用您首选的[test runner](../T/test-runner.md) 运行您的[test scripts](../T/test-script.md)**。您的测试现在将在[BrowserStack](../B/browserstack.md) 的远程浏览器/设备上执行。
  6. 通过[BrowserStack](../B/browserstack.md) Automate 仪表板实时监控您的测试，您可以在其中查看测试进度、视频记录、日志和屏幕截图。
  7. **分析测试结果**并使用[BrowserStack](../B/browserstack.md) 提供的详细报告调试问题。

### # 对BrowserStack 执行测试的步骤是什么？

要对 [BrowserStack](../B/browserstack.md) 执行测试，请执行以下步骤：

1. **登录**
    到您的BrowserStack 帐户。

2. **选择**
    测试类型：实时、自动化、应用程序实时或屏幕截图和响应式。

3.为了
    **自动化**：

    ```
    const capabilities = {
      'browserName': 'Chrome',
      'browser_version': 'latest',
      'os': 'Windows',
      'os_version': '10',
      'resolution': '1024x768',
      'browserstack.user': 'YOUR_USERNAME',
      'browserstack.key': 'YOUR_ACCESS_KEY'
    };
    ```
- **配置**
      您的测试脚本使用 BrowserStack 的中心 URL 和所需的功能。

- **运行**
      来自 IDE 或命令行的测试脚本。

- **配置**
      您的测试脚本使用 BrowserStack 的中心 URL 和所需的功能。

- **运行**
      来自 IDE 或命令行的测试脚本。

4. 对于
    **实时测试**：

- **选择**
      浏览器、版本和操作系统。

- **导航**
      到托管您的 Web 应用程序的URL。

- **互动**
      手动与您的网站一起执行测试。

- **选择**
      浏览器、版本和操作系统。

- **导航**
      到托管您的 Web 应用程序的URL。

- **互动**
      手动与您的网站一起执行测试。

5. 对于
    **应用直播**：

- **上传**
      您的移动应用程序或向该应用程序提供公共URL。

- **选择**
      设备和操作系统版本。

- **互动**
      在所选设备上使用您的应用程序。

- **上传**
      您的移动应用程序或向该应用程序提供公共URL。

- **选择**
      设备和操作系统版本。

- **互动**
      在所选设备上使用您的应用程序。

6. 对于
    **屏幕截图和响应式**：

- **输入**
      您的网络应用程序的URL。

- **选择**
      用于截图的浏览器和设备。

- **生成**
      屏幕截图以查看不同设备和浏览器的布局。

- **输入**
      您的网络应用程序的URL。

- **选择**
      用于截图的浏览器和设备。

- **生成**
      屏幕截图以查看不同设备和浏览器的布局。
  测试后，**查看**结果，其中可能包括视频记录、日志和屏幕截图，具体取决于所执行的测试类型。 **分析**结果以识别任何问题或[bugs](../B/bug.md)。

1. **登录**
    到您的BrowserStack 帐户。

2. **选择**
    测试类型：实时、自动化、应用程序实时或屏幕截图和响应式。

3.为了
    **自动化**：

    ```
    const capabilities = {
      'browserName': 'Chrome',
      'browser_version': 'latest',
      'os': 'Windows',
      'os_version': '10',
      'resolution': '1024x768',
      'browserstack.user': 'YOUR_USERNAME',
      'browserstack.key': 'YOUR_ACCESS_KEY'
    };
    ```
- **配置**
      您的测试脚本使用 BrowserStack 的中心 URL 和所需的功能。

- **运行**
      来自 IDE 或命令行的测试脚本。

- **配置**
      您的测试脚本使用 BrowserStack 的中心 URL 和所需的功能。

- **运行**
      来自 IDE 或命令行的测试脚本。

4. 对于
    **实时测试**：

- **选择**
      浏览器、版本和操作系统。

- **导航**
      到托管您的 Web 应用程序的URL。

- **互动**
      手动与您的网站一起执行测试。

- **选择**
      浏览器、版本和操作系统。

- **导航**
      到托管您的 Web 应用程序的URL。

- **互动**
      手动与您的网站一起执行测试。

5. 对于
    **应用直播**：

- **上传**
      您的移动应用程序或向该应用程序提供公共URL。

- **选择**
      设备和操作系统版本。

- **互动**
      在所选设备上使用您的应用程序。

- **上传**
      您的移动应用程序或向该应用程序提供公共URL。

- **选择**
      设备和操作系统版本。

- **互动**
      在所选设备上使用您的应用程序。

6. 对于
    **屏幕截图和响应式**：

- **输入**
      您的网络应用程序的URL。

- **选择**
      用于截图的浏览器和设备。

- **生成**
      屏幕截图以查看不同设备和浏览器的布局。

- **输入**
      您的网络应用程序的URL。

- **选择**
      用于截图的浏览器和设备。

- **生成**
      屏幕截图以查看不同设备和浏览器的布局。

### # 如何使用 BrowserStack 进行移动测试？

要使用 [BrowserStack](../B/browserstack.md) 进行移动测试，请按照以下步骤操作：

1. **登录**您的[BrowserStack](../B/browserstack.md) 帐户。
  2. 导航至 **App Live** 或 **App Automate** 部分，具体取决于您要执行手动操作还是[automated testing](../A/automated-testing.md)。
  3. 对于**应用直播**：
    - 上传您的移动应用程序或提供公共URL。
    - 选择您要测试的设备和操作系统版本。
    - 通过浏览器与所选设备上的应用程序交互。
    - 上传您的移动应用程序或提供公共URL。
    - 选择您要测试的设备和操作系统版本。
    - 通过浏览器与所选设备上的应用程序交互。
  4. 对于**应用程序自动化**：
    - 确保您准备好使用 Appium 或 Espresso 等框架的自动化脚本。
    - 配置您的测试脚本以使用提供的连接到BrowserStack
      **访问密钥**
      和
      **用户名**
      。

- 指定所需的功能，包括设备和操作系统版本。
    - 运行您的测试脚本。它将在BrowserStack云上执行。
    - 确保您准备好使用 Appium 或 Espresso 等框架的自动化脚本。
    - 配置您的测试脚本以使用提供的连接到BrowserStack
      **访问密钥**
      和
      **用户名**
      。

- 指定所需的功能，包括设备和操作系统版本。
    - 运行您的测试脚本。它将在BrowserStack 云上执行。
  以下是 Appium 测试的示例代码片段：

  ```
  DesiredCapabilities capabilities = new DesiredCapabilities();
  capabilities.setCapability("device", "iPhone 11 Pro Max");
  capabilities.setCapability("os_version", "13");
  capabilities.setCapability("realMobile", "true");
  capabilities.setCapability("browserstack.user", "YOUR_USERNAME");
  capabilities.setCapability("browserstack.key", "YOUR_ACCESS_KEY");
  AppiumDriver driver = new AppiumDriver(new URL("http://hub.browserstack.com/wd/hub"), capabilities);
  ```
1. 通过以下方式监控测试结果
    **[BrowserStack](../B/browserstack.md) 仪表板**
    您可以在其中查看视频记录、日志和屏幕截图。
  请记住将 `"YOUR_USERNAME"` 和 `"YOUR_ACCESS_KEY"` 替换为您的实际 [BrowserStack](../B/browserstack.md) 凭据。

1. **登录**您的[BrowserStack](../B/browserstack.md) 帐户。
  2. 导航到 **App Live** 或 **App Automate** 部分，具体取决于您要执行手动操作还是 [automated testing](../A/automated-testing.md)。
  3. 对于**应用直播**：
    - 上传您的移动应用程序或提供公共URL。
    - 选择您要测试的设备和操作系统版本。
    - 通过浏览器与所选设备上的应用程序交互。
    - 上传您的移动应用程序或提供公共URL。
    - 选择您要测试的设备和操作系统版本。
    - 通过浏览器与所选设备上的应用程序交互。
  4. 对于**应用程序自动化**：
    - 确保您准备好使用 Appium 或 Espresso 等框架的自动化脚本。
    - 配置您的测试脚本以使用提供的连接到BrowserStack
      **访问密钥**
      和
      **用户名**
      。

- 指定所需的功能，包括设备和操作系统版本。
    - 运行您的测试脚本。它将在BrowserStack云上执行。
    - 确保您准备好使用 Appium 或 Espresso 等框架的自动化脚本。
    - 配置您的测试脚本以使用提供的连接到BrowserStack
      **访问密钥**
      和
      **用户名**
      。

- 指定所需的功能，包括设备和操作系统版本。
    - 运行您的测试脚本。它将在BrowserStack云上执行。
  1. 通过以下方式监控测试结果
    **[BrowserStack](../B/browserstack.md) 仪表板**
    您可以在其中查看视频记录、日志和屏幕截图。

### # BrowserStack 如何处理不同的浏览器和操作系统？

[BrowserStack](../B/browserstack.md) 通过维护真实设备和浏览器版本的**大量库存**来管理各种浏览器和操作系统。启动测试时，[BrowserStack](../B/browserstack.md) **分配**符合指定条件（例如浏览器版本、操作系统和屏幕分辨率）的虚拟机或真实设备。
  对于浏览器，[BrowserStack](../B/browserstack.md) 支持 **Chrome**、**Firefox**、**Safari**、**Internet Explorer** 和 **Edge** 等多种版本。它还提供各种版本的移动浏览器，以便在不同设备上进行测试。
  操作系统方面，包括**Windows**、**macOS**、**iOS**、**Android**平台，覆盖多个版本，保证不同环境下的兼容性。
  [BrowserStack](../B/browserstack.md) 使用**基于云的基础设施**来提供对这些环境的访问，这意味着测试可以跨浏览器和操作系统的多种组合并行运行，而不需要本地[setup](../S/setup.md) 或维护。
  为了指定所需的环境，测试人员使用[test scripts](../T/test-script.md) 中的功能。以下是在 JavaScript 中使用 [Selenium](../S/selenium.md) [WebDriver](../W/webdriver.md) 的示例：

  ```
  const capabilities = {
    'browserName' : 'Chrome',
    'browser_version' : 'latest',
    'os' : 'Windows',
    'os_version' : '10',
    'resolution' : '1024x768'
  };
  const driver = new webdriver.Builder().
    usingServer('http://hub-cloud.browserstack.com/wd/hub').
    withCapabilities(capabilities).
    build();
  ```
这种方法可确保应用程序在**接近模仿用户条件**的环境中进行测试，从而获得更可靠的测试结果。

### # 我可以使用 BrowserStack 进行自动化测试吗？

当然，**[BrowserStack](../B/browserstack.md)** 可用于[automated testing](../A/automated-testing.md)。它提供了一个基于云的平台，使您能够在各种浏览器和真实的移动设备上运行自动化测试。首先，您需要配置[test automation](../T/test-automation.md) 框架以与[BrowserStack](../B/browserstack.md) 的远程服务器连接。
  下面是使用 **[Selenium](../S/selenium.md) [WebDriver](../W/webdriver.md)** 和 **JavaScript** 的基本示例：

  ```
  const { Builder } = require('selenium-webdriver');
  require('chromedriver');
  async function runTestOnBrowserStack() {
    const capabilities = {
      'bstack:options' : {
        "os" : "Windows",
        "osVersion" : "10",
        "local" : "false",
        "seleniumVersion" : "3.14.0",
        "userName" : "YOUR_USERNAME",
        "accessKey" : "YOUR_ACCESS_KEY",
      },
      "browserName" : "Chrome",
      "browserVersion" : "latest",
    };
    let driver = new Builder()
      .usingServer('http://hub-cloud.browserstack.com/wd/hub')
      .withCapabilities(capabilities)
      .build();
    try {
      await driver.get('http://www.google.com');
      // Add your test logic here
    } finally {
      await driver.quit();
    }
  }
  runTestOnBrowserStack();
  ```
将`YOUR_USERNAME` 和`YOUR_ACCESS_KEY` 替换为您的[BrowserStack](../B/browserstack.md) 凭据。此代码设置[Selenium](../S/selenium.md) [WebDriver](../W/webdriver.md) 测试以在[BrowserStack](../B/browserstack.md) 的基础结构上运行。
  对于**持续集成**，您可以将 [BrowserStack](../B/browserstack.md) 与 **Jenkins**、**Travis CI** 或 **CircleCI** 等工具集成，以在每次提交或拉取请求时自动运行测试。
  [BrowserStack](../B/browserstack.md) 还支持其他测试框架，例如用于 [mobile app testing](../M/mobile-app-testing.md) 的 **Appium**，以及用于更专业测试场景的 **[Cypress](../C/cypress.md)**、**Playwright** 或 **Espresso**。与这些工具的集成遵循配置测试以与 [BrowserStack](../B/browserstack.md) 的远程服务器进行通信的类似模式。

## # 集成和兼容性

### # BrowserStack 如何与其他测试工具集成？

[BrowserStack](../B/browserstack.md) 可以与各种测试工具集成，以增强自动化并简化工作流程。以下是如何将其与一些常用工具集成：
  **Appium**：将[BrowserStack](../B/browserstack.md) 的Appium 服务器用于[mobile app testing](../M/mobile-app-testing.md)。使用您的访问凭据将Appium 客户端中的`remote_url` 设置为[BrowserStack](../B/browserstack.md) 的端点。

  ```
  DesiredCapabilities caps = new DesiredCapabilities();
  caps.setCapability("browserstack.user", "YOUR_USERNAME");
  caps.setCapability("browserstack.key", "YOUR_ACCESS_KEY");
  // Additional capabilities
  AppiumDriver driver = new AppiumDriver(new URL("http://hub.browserstack.com/wd/hub"), caps);
  ```
**[Cypress](../C/cypress.md)**：对于[Cypress](../C/cypress.md) 集成，请安装[BrowserStack](../B/browserstack.md) 的CLI 工具并使用`browserstack-cypress` 命令在[BrowserStack](../B/browserstack.md) 上运行测试。

  ```
  npm install -g browserstack-cypress-cli
  browserstack-cypress run
  ```
**TestCafe**：使用[BrowserStack](../B/browserstack.md) 插件集成TestCafe。在`.testcaferc.json` 文件中配置您的[BrowserStack](../B/browserstack.md) 凭据和所需的功能。

  ```
  {
    "browsers": "browserstack:chrome",
    "browserstack": {
      "username": "YOUR_USERNAME",
      "accessKey": "YOUR_ACCESS_KEY"
    }
  }
  ```
**JUnit**：对于JUnit 集成，将您的测试配置为使用`RemoteWebDriver` 和所需功能连接到[BrowserStack](../B/browserstack.md) 的[Selenium](../S/selenium.md) 网格。

  ```
  DesiredCapabilities caps = new DesiredCapabilities();
  caps.setCapability("browserstack.user", "YOUR_USERNAME");
  caps.setCapability("browserstack.key", "YOUR_ACCESS_KEY");
  // Additional capabilities
  WebDriver driver = new RemoteWebDriver(new URL("http://hub.browserstack.com/wd/hub"), caps);
  ```
**GitHub 操作**：使用 [BrowserStack](../B/browserstack.md) 的 GitHub 操作来设置 CI/CD 管道。将操作添加到您的工作流程文件并使用您的 [BrowserStack](../B/browserstack.md) 凭据进行配置。

  ```
  - name: BrowserStack Action
    uses: browserstack/github-actions@master
    with:
      username: ${{ secrets.BROWSERSTACK_USERNAME }}
      access-key: ${{ secrets.BROWSERSTACK_ACCESS_KEY }}
  ```
这些集成允许您在现有的[test automation](../T/test-automation.md) 生态系统中利用[BrowserStack](../B/browserstack.md) 的基础设施，从而促进跨浏览器和跨平台测试。

### # BrowserStack 与持续集成工具兼容吗？

是的，**[BrowserStack](../B/browserstack.md)** 与各种**持续集成 (CI)** 工具兼容。它提供了与 CI 系统无缝工作流程的插件和集成，使自动化测试能够作为构建过程的一部分运行。这种兼容性确保测试成为开发周期不可或缺的一部分，从而尽早发现问题并维护[software quality](../S/software-quality.md)。
  例如，[BrowserStack](../B/browserstack.md) 通过插件与 **Jenkins** 集成，允许您直接从 Jenkins 构建过程触发 [BrowserStack](../B/browserstack.md) 测试。同样，它通过可用插件或在 CI 配置中使用自定义脚本来支持其他 CI 工具，例如 **Travis CI**、**CircleCI**、**GitLab CI** 和 **Bitbucket Pipelines**。
  要将 [BrowserStack](../B/browserstack.md) 与 CI 工具集成，您通常需要添加 [BrowserStack](../B/browserstack.md) 访问凭据并配置 [test scripts](../T/test-script.md) 以与 [BrowserStack](../B/browserstack.md) [API](../A/api.md) 进行通信。以下示例说明了如何使用 CI 工具使用环境变量进行身份验证来设置 [BrowserStack](../B/browserstack.md)：

  ```
  export BROWSERSTACK_USERNAME="your_username"
  export BROWSERSTACK_ACCESS_KEY="your_access_key"
  ```
然后，您将运行包含 [BrowserStack](../B/browserstack.md) 功能的测试命令。此命令的具体细节取决于您使用的测试框架和语言。
  通过将 [BrowserStack](../B/browserstack.md) 与 CI 工具集成，您可以自动化跨浏览器和跨平台测试，确保每次提交或构建都得到验证，从而以最少的手动干预保持高标准的质量。

### # 我可以将BrowserStack 与Selenium 一起使用吗？

当然，**[BrowserStack](../B/browserstack.md)** 可以与 **[Selenium](../S/selenium.md)** 一起使用来运行自动化浏览器测试。要将[Selenium](../S/selenium.md) 与[BrowserStack](../B/browserstack.md) 集成，请执行以下步骤：

1. **设置您的环境**：
    - 确保您有
      **[Selenium](../S/selenium.md) [WebDriver](../W/webdriver.md)**
      为您首选的编程语言安装。

- 安装必要的特定于语言的绑定。
    - 确保您有
      **[Selenium](../S/selenium.md) [WebDriver](../W/webdriver.md)**
      为您首选的编程语言安装。

- 安装必要的特定于语言的绑定。
  2. **配置您的[test script](../T/test-script.md)**：
    - 从Selenium 导入WebDriver 和
      `DesiredCapabilities`
      模块。

- 定义您的 BrowserStack 凭据和所需的功能，包括您要测试的浏览器、浏览器版本和操作系统。
    - 从Selenium 导入WebDriver 和
      `DesiredCapabilities`
      模块。

- 定义您的 BrowserStack 凭据和所需的功能，包括您要测试的浏览器、浏览器版本和操作系统。
  3. **初始化远程[WebDriver](../W/webdriver.md)**：
    - 将WebDriver 指向BrowserStack 远程URL，包括您的访问凭据。
    - 将WebDriver 指向BrowserStack 远程URL，包括您的访问凭据。
  4. **写下您的[test cases](../T/test-case.md)**：
    - 使用与本地浏览器测试相同的 Selenium 命令。
    - 使用与本地浏览器测试相同的 Selenium 命令。
  这是 Java 中的一个基本示例：

  ```
  import org.openqa.selenium.WebDriver;
  import org.openqa.selenium.remote.DesiredCapabilities;
  import org.openqa.selenium.remote.RemoteWebDriver;
  import java.net.URL;
  public class BrowserStackSeleniumTest {
    public static final String USERNAME = "your_browserstack_username";
    public static final String AUTOMATE_KEY = "your_browserstack_accesskey";
    public static final String URL = "https://" + USERNAME + ":" + AUTOMATE_KEY +
                                     "@hub-cloud.browserstack.com/wd/hub";
    public static void main(String[] args) throws Exception {
      DesiredCapabilities caps = new DesiredCapabilities();
      caps.setCapability("browserName", "chrome");
      caps.setCapability("browserVersion", "latest");
      caps.setCapability("os", "Windows");
      caps.setCapability("os_version", "10");
      caps.setCapability("name", "BrowserStackTest");
      WebDriver driver = new RemoteWebDriver(new URL(URL), caps);
      driver.get("http://www.google.com");
      // Your test code here
      driver.quit();
    }
  }
  ```
将`your_browserstack_username` 和`your_browserstack_accesskey` 替换为您的[BrowserStack](../B/browserstack.md) 凭据。调整功能以满足您的测试要求。

1. **设置您的环境**：
    - 确保您有
      **[Selenium](../S/selenium.md) [WebDriver](../W/webdriver.md)**
      为您首选的编程语言安装。

- 安装必要的特定于语言的绑定。
    - 确保您有
      **[Selenium](../S/selenium.md) [WebDriver](../W/webdriver.md)**
      为您首选的编程语言安装。

- 安装必要的特定于语言的绑定。
  2. **配置您的[test script](../T/test-script.md)**：
    - 从Selenium 导入WebDriver 和
      `DesiredCapabilities`
      模块。

- 定义您的 BrowserStack 凭据和所需的功能，包括您要测试的浏览器、浏览器版本和操作系统。
    - 从Selenium 导入WebDriver 和
      `DesiredCapabilities`
      模块。

- 定义您的 BrowserStack 凭据和所需的功能，包括您要测试的浏览器、浏览器版本和操作系统。
  3. **初始化远程[WebDriver](../W/webdriver.md)**：
    - 将WebDriver 指向BrowserStack 远程URL，包括您的访问凭据。
    - 将WebDriver 指向BrowserStack 远程URL，包括您的访问凭据。
  4. **写下您的[test cases](../T/test-case.md)**：
    - 使用与本地浏览器测试相同的 Selenium 命令。
    - 使用与本地浏览器测试相同的 Selenium 命令。

### # BrowserStack 如何与 Jenkins 集成？

[BrowserStack](../B/browserstack.md) 通过其 **[BrowserStack](../B/browserstack.md) Jenkins 插件** 与 Jenkins 集成。该插件允许您直接从 Jenkins 界面轻松地在 [BrowserStack](../B/browserstack.md) 的基础设施上运行自动化测试。要设置集成，请执行以下步骤：

1. 安装
    **[BrowserStack](../B/browserstack.md) Jenkins 插件**
    来自 Jenkins 插件管理器。

2. 使用您的BrowserStack 配置插件
    **访问密钥**
    和
    **用户名**
    导航到 Jenkins 系统配置页面。

3. 在作业配置中，添加构建步骤或构建后操作
    **在[BrowserStack](../B/browserstack.md)上运行自动化测试**
    。

4. 定义您的测试配置，包括您要测试的浏览器和设备。
  5. 使用
    **BrowserStack Local**
    用于通过安全隧道测试内部、私有或临时环境的二进制文件。

6. 启动 Jenkins 构建，插件将自动触发 BrowserStack 上的测试。
  以下是如何配置 Jenkins 作业以使用 [BrowserStack](../B/browserstack.md) 的示例：

  ```
  pipeline {
      agent any
      stages {
          stage('Test') {
              steps {
                  script {
                      // Set up BrowserStack credentials
                      def browserStackCredentials = withCredentials([usernamePassword(credentialsId: 'BROWSERSTACK_CREDENTIALS', passwordVariable: 'BROWSERSTACK_ACCESS_KEY', usernameVariable: 'BROWSERSTACK_USERNAME')]) {
                          // Run tests on BrowserStack
                          sh 'mvn test -DBrowserStack_Username=$BROWSERSTACK_USERNAME -DBrowserStack_AccessKey=$BROWSERSTACK_ACCESS_KEY'
                      }
                  }
              }
          }
      }
  }
  ```
该插件还为[BrowserStack](../B/browserstack.md) 凭据提供**环境变量**，可在您的[test scripts](../T/test-script.md) 中使用。执行测试后，结果和视频记录可在 [BrowserStack](../B/browserstack.md) Automate 仪表板上查看。 Jenkins 还将显示结果，从而可以轻松地直接从 CI 管道跟踪测试成功和失败。

1. 安装
    **[BrowserStack](../B/browserstack.md) Jenkins 插件**
    来自 Jenkins 插件管理器。

2. 使用您的BrowserStack 配置插件
    **访问密钥**
    和
    **用户名**
    导航到 Jenkins 系统配置页面。

3. 在作业配置中，添加构建步骤或构建后操作
    **在[BrowserStack](../B/browserstack.md)上运行自动化测试**
    。

4. 定义您的测试配置，包括您要测试的浏览器和设备。
  5. 使用
    **BrowserStack Local**
    用于通过安全隧道测试内部、私有或临时环境的二进制文件。

6. 启动 Jenkins 构建，插件将自动触发 BrowserStack 上的测试。

### # 还有哪些其他工具和框架可以与 BrowserStack 一起使用？

[BrowserStack](../B/browserstack.md)可以与各种**[test automation](../T/test-automation.md)工具和框架**集成，以增强测试能力。以下是一些值得注意的：

- **Appium**：对于移动应用程序测试，您可以使用Appium 和[BrowserStack](../B/browserstack.md) 在各种真实设备上运行自动化测试。

    ```
    browserstackUser = "YOUR_USER";
    browserstackKey = "YOUR_KEY";
    desiredCapabilities.setCapability("browserstack.user", browserstackUser);
    desiredCapabilities.setCapability("browserstack.key", browserstackKey);
    ```
- **[Cypress](../C/cypress.md)**：[BrowserStack](../B/browserstack.md) 支持[Cypress](../C/cypress.md) 测试，允许您跨多个浏览器和操作系统运行它们。
  - **TestCafe**：您可以在[BrowserStack](../B/browserstack.md) 上运行TestCafe 脚本以利用其[cross-browser testing](../C/cross-browser-testing.md) 功能。
  - **Espresso**：对于Android应用程序测试，可以在[BrowserStack](../B/browserstack.md)的真实设备云上执行Espresso测试。
  - **XCTest**：同样，支持 iOS 应用程序的 XCTest 框架，可以在一系列 Apple 设备上进行测试。
  - **Puppeteer**：[BrowserStack](../B/browserstack.md) 使用Puppeteer 提供对无头浏览器测试的支持，这对于快速反馈非常有用。
  - **Playwright**：集成 Playwright 测试以在 [BrowserStack](../B/browserstack.md) 上运行，以测试跨所有浏览器的现代 Web 应用程序。
  - **GitHub 操作**：通过将[BrowserStack](../B/browserstack.md) 与GitHub 操作集成以实现连续测试，自动化您的工作流程。
  - **Bitbucket Pipelines**：在 [BrowserStack](../B/browserstack.md) 中运行测试，作为 Bitbucket Pipelines CI/CD 进程的一部分。
  - **TeamCity**：与 TeamCity 集成，自动在您的构建中触发 [BrowserStack](../B/browserstack.md) 测试。
  - **Visual Studio Team Services**：将 VSTS 管道与 [BrowserStack](../B/browserstack.md) 连接，以在发布过程中运行自动化测试。
  这些集成有助于利用 [BrowserStack](../B/browserstack.md) 的设备和浏览器覆盖范围，使其成为全面 [automated testing](../A/automated-testing.md) 的多功能选择。

- **Appium**：对于移动应用程序测试，您可以使用Appium 和[BrowserStack](../B/browserstack.md) 在各种真实设备上运行自动化测试。

    ```
    browserstackUser = "YOUR_USER";
    browserstackKey = "YOUR_KEY";
    desiredCapabilities.setCapability("browserstack.user", browserstackUser);
    desiredCapabilities.setCapability("browserstack.key", browserstackKey);
    ```
- **[Cypress](../C/cypress.md)**：[BrowserStack](../B/browserstack.md) 支持[Cypress](../C/cypress.md) 测试，允许您跨多个浏览器和操作系统运行它们。
  - **TestCafe**：您可以在[BrowserStack](../B/browserstack.md) 上运行TestCafe 脚本以利用其[cross-browser testing](../C/cross-browser-testing.md) 功能。
  - **Espresso**：对于Android应用程序测试，可以在[BrowserStack](../B/browserstack.md)的真实设备云上执行Espresso测试。
  - **XCTest**：同样，支持 iOS 应用程序的 XCTest 框架，可以在一系列 Apple 设备上进行测试。
  - **Puppeteer**：[BrowserStack](../B/browserstack.md) 使用Puppeteer 提供无头浏览器测试支持，这对于快速反馈非常有用。
  - **Playwright**：集成 Playwright 测试以在 [BrowserStack](../B/browserstack.md) 上运行，以测试跨所有浏览器的现代 Web 应用程序。
  - **GitHub 操作**：通过将[BrowserStack](../B/browserstack.md) 与GitHub 操作集成以实现连续测试，自动化您的工作流程。
  - **Bitbucket Pipelines**：在 [BrowserStack](../B/browserstack.md) 中运行测试，作为 Bitbucket Pipelines CI/CD 进程的一部分。
  - **TeamCity**：与 TeamCity 集成，自动在您的构建中触发 [BrowserStack](../B/browserstack.md) 测试。
  - **Visual Studio Team Services**：将 VSTS 管道与 [BrowserStack](../B/browserstack.md) 连接，以在发布过程中运行自动化测试。

## # 高级功能

### # BrowserStack 有哪些高级功能？

[BrowserStack](../B/browserstack.md) 提供了多种高级功能，可以满足经验丰富的 [test automation](../T/test-automation.md) 工程师的需求：

- **本地测试**：通过在 [BrowserStack](../B/browserstack.md) 和本地计算机之间建立安全隧道，在防火墙后面或本地主机上安全地测试开发和登台环境。
  - **并行测试**：通过在不同的浏览器、设备和操作系统上同时运行多个测试来加速[test execution](../T/test-execution.md)。
  - **地理位置测试**：模拟不同地理位置的网站和应用程序性能，以确保全球用户获得一致的体验。
  - **真实设备云**：访问各种真实的移动设备，以获得更准确的测试结果，而不是仿真器或模拟器。
  - **[Visual Regression Testing](../V/visual-regression-testing.md)**：通过比较一段时间内的屏幕截图来自动检测视觉回归。
  - **网络节流**：在各种网络条件下测试应用程序，包括 3G、4G、LTE 和 Wi-Fi，以了解性能和用户体验。
  - **交互式调试**：在实时测试会话期间使用断点和控制台日志等工具来实时识别和解决问题。
  - **集成开发人员工具**：访问远程设备上的浏览器开发工具以进行深入调试。
  - **自动化[Mobile App Testing](../M/mobile-app-testing.md)**：使用Appium、Espresso 和 XCUITest 框架在本机和混合移动应用程序上运行自动化测试。
  - **企业功能**：为大型组织定制的解决方案，包括单点登录 (SSO)、团队管理和[priority](../P/priority.md) 支持。
  为了利用这些功能，工程师可以使用提供的[APIs](../A/api.md)和CLI工具将相关的[BrowserStack](../B/browserstack.md)功能合并到现有的[test automation](../T/test-automation.md)框架中。例如，要启用本地测试，请使用 BrowserStackLocal 二进制文件：

  ```
  BrowserStackLocal --key YOUR_ACCESS_KEY
  ```
对于并行测试，配置您的 [test scripts](../T/test-script.md) 以使用不同的配置启动多个会话：

  ```
  "browsers": [
    { "browser": "chrome", "browser_version": "latest", "os": "Windows", "os_version": "10" },
    { "browser": "firefox", "browser_version": "latest", "os": "OS X", "os_version": "Catalina" }
  ]
  ```
这些功能旨在提高测试效率、准确性和覆盖范围，确保应用程序在所有用户接触点上以最佳性能运行。

- **本地测试**：通过在 [BrowserStack](../B/browserstack.md) 和本地计算机之间建立安全隧道，在防火墙后面或本地主机上安全地测试开发和登台环境。
  - **并行测试**：通过在不同的浏览器、设备和操作系统上同时运行多个测试来加速[test execution](../T/test-execution.md)。
  - **地理位置测试**：模拟不同地理位置的网站和应用程序性能，以确保全球用户获得一致的体验。
  - **真实设备云**：访问各种真实的移动设备，以获得更准确的测试结果，而不是仿真器或模拟器。
  - **[Visual Regression Testing](../V/visual-regression-testing.md)**：通过比较一段时间内的屏幕截图来自动检测视觉回归。
  - **网络节流**：在各种网络条件下测试应用程序，包括 3G、4G、LTE 和 Wi-Fi，以了解性能和用户体验。
  - **交互式调试**：在实时测试会话期间使用断点和控制台日志等工具来实时识别和解决问题。
  - **集成开发人员工具**：访问远程设备上的浏览器开发工具以进行深入调试。
  - **自动化[Mobile App Testing](../M/mobile-app-testing.md)**：使用Appium、Espresso 和 XCUITest 框架在本机和混合移动应用程序上运行自动化测试。
  - **企业功能**：为大型组织定制的解决方案，包括单点登录 (SSO)、团队管理和 [priority](../P/priority.md) 支持。

### # BrowserStack 中的“实时测试”功能如何工作？

[BrowserStack](../B/browserstack.md) 中的**实时测试**功能允许您在不同的浏览器和设备上以交互方式测试您的网站或应用程序，而无需设置实际的[test environment](../T/test-environment.md)。它在平台的云基础设施上提供实时浏览器会话，使您能够手动导航和测试 Web 应用程序的功能，就像使用本地设备或浏览器一样。
  要使用实时测试：

1. 登录您的BrowserStack 帐户。
  2. 导航至
    **直播**
    部分。

3. 选择所需的
    **浏览器**
    ,
    **浏览器版本**
    , 和
    **操作系统**
    。

4. 输入
    **URL**
    您要测试的网站或 Web 应用程序的名称。

5. 单击
    **开始会话**
    启动实时测试会话。
  在会议期间，您可以与网站或应用程序交互，实时测试布局、功能并调试问题。您还可以在不同浏览器和设备之间快速切换，测试跨浏览器兼容性。
  实时测试还提供调试工具，例如**控制台日志**、**网络日志**，以及拍摄会话的**屏幕截图**或**视频录制**的功能。这些功能有助于识别和记录测试过程中可能出现的问题。
  请记住，实时测试适用于[manual testing](../M/manual-testing.md)。对于[automated testing](../A/automated-testing.md)，您将使用[BrowserStack](../B/browserstack.md) 的自动化功能或其他[automated testing](../A/automated-testing.md) 集成。

1. 登录您的BrowserStack 帐户。
  2. 导航至
    **直播**
    部分。

3. 选择所需的
    **浏览器**
    ,
    **浏览器版本**
    , 和
    **操作系统**
    。

4. 输入
    **URL**
    您要测试的网站或 Web 应用程序的名称。

5. 单击
    **开始会话**
    启动实时测试会话。

### # BrowserStack 中的“Automate Pro”是什么？

Automate Pro 是[BrowserStack](../B/browserstack.md) 的高级产品，专为**企业级** [test automation](../T/test-automation.md) 需求而定制。与标准自动化计划相比，它提供**高级功能**和**增强功能**。借助 Automate Pro，用户可以访问**无限并行测试运行**，这显着减少了运行大型 [test suites](../T/test-suite.md) 所需的时间。这对于测试要求高、需要扩展自动化工作的组织来说尤其有利。
  此外，Automate Pro 还包括 **[priority](../P/priority.md) 支持**，以确保及时解决任何问题，从而最大限度地减少停机时间。用户还可以受益于**独有的功能**，例如**单点登录 (SSO)** 可提高安全性和便利性，以及 **IP 白名单** 可控制访问并保持对公司网络策略的合规性。
  对于专注于 **[test coverage](../T/test-coverage.md)** 的团队，Automate Pro 提供**真实设备测试**，以确保应用程序能够在实际移动设备上无缝运行，而不仅仅是仿真器或模拟器。这对于在当今以移动为中心的世界中提供高质量的用户体验至关重要。
  为了满足大型组织的需求，Automate Pro还提供**团队管理功能**，允许分布式测试团队之间更好的协调和协作。这包括用于有效管理资源的**基于角色的访问控制**和**团队使用情况洞察**等功能。
  总之，Automate Pro 旨在通过在[BrowserStack](../B/browserstack.md) 内提供更强大且功能丰富的[test automation](../T/test-automation.md) 环境来支持大型企业复杂而广泛的测试需求。

### # 如何使用 BrowserStack 中的“App Live”功能？

要使用 [BrowserStack](../B/browserstack.md) 中的 **App Live** 功能，请按照以下步骤操作：

1. **登录**
    到您的BrowserStack 帐户。

2. 导航至
    **应用直播**
    部分。

3. **上传**
    您的移动应用程序二进制文件：

- 对于iOS，上传
      `.ipa`
      文件。

- 对于 Android，请上传
      `.apk`
      文件。

- 对于iOS，上传
      `.ipa`
      文件。

- 对于 Android，请上传
      `.apk`
      文件。

4. 上传后，选择
    **所需设备**
    从可用iOS 和 Android 设备列表中。

5. **启动**
    所选设备上的应用程序。 BrowserStack 将实例化真实设备会话。

6. **互动**
    在浏览器窗口中实时使用您的应用程序。

7. 使用
    **工具栏**
    执行旋转、摇动、截屏和设置地理位置等操作。

8. **调试**
    通过查看日志、视频记录和其他数据来访问您的应用程序。

9. **整合**
    与您本地的开发环境一起使用
    **本地测试**
    如果需要测试内部服务器或开发环境，则可以使用此功能。
  对于您的应用程序的 **[automated testing](../A/automated-testing.md)**，请切换到 [BrowserStack](../B/browserstack.md) 中的 **自动化** 部分，并按照您选择的框架（例如 Appium 或 Espresso）的相关步骤进行操作。
  请记住，App Live 用于**手动交互测试**。对于自动化测试，请使用[BrowserStack](../B/browserstack.md) 的 **Automate** 或 **Automate Pro** 功能。

1. **登录**
    到您的BrowserStack 帐户。

2. 导航至
    **应用直播**
    部分。

3. **上传**
    您的移动应用程序二进制文件：

- 对于iOS，上传
      `.ipa`
      文件。

- 对于 Android，请上传
      `.apk`
      文件。

- 对于iOS，上传
      `.ipa`
      文件。

- 对于 Android，请上传
      `.apk`
      文件。

4. 上传后，选择
    **所需设备**
    从可用iOS 和 Android 设备列表中。

5. **启动**
    所选设备上的应用程序。 BrowserStack 将实例化一个真实的设备会话。

6. **互动**
    在浏览器窗口中实时使用您的应用程序。

7. 使用
    **工具栏**
    执行旋转、摇动、截屏和设置地理位置等操作。

8. **调试**
    通过查看日志、视频记录和其他数据来访问您的应用程序。

9. **整合**
    与您本地的开发环境一起使用
    **本地测试**
    如果需要测试内部服务器或开发环境，则可以使用此功能。

### # BrowserStack 中的“屏幕截图”功能是什么？

[BrowserStack](../B/browserstack.md) 中的 **屏幕截图** 功能是一个允许用户跨不同浏览器和操作系统捕获和保存网页图像的工具。这对于 [visual regression testing](../V/visual-regression-testing.md) 特别有用，您需要确保您的 Web 应用程序在多个浏览器环境中外观和功能正常。
  要使用屏幕截图功能，您需要指定要测试的网页的URL，以及浏览器和操作系统组合的列表。 [BrowserStack](../B/browserstack.md) 然后生成该页面的屏幕截图，就像它显示在所选浏览器和设备上一样。这些屏幕截图可以手动查看，也可以使用第三方工具以编程方式进行比较，以检测视觉差异。
  以下是如何使用 JavaScript 触发屏幕截图 [API](../A/api.md) 的基本示例：

  ```
  const request = require('request');
  const options = {
    method: 'POST',
    url: 'https://www.browserstack.com/screenshots',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': 'Basic ' + Buffer.from('your_username:your_access_key').toString('base64')
    },
    body: JSON.stringify({
      url: 'http://www.yourwebsite.com',
      browsers: [
        {os: 'Windows', os_version: '10', browser: 'chrome', browser_version: 'latest'},
        {os: 'OS X', os_version: 'Big Sur', browser: 'safari', browser_version: 'latest'}
        // Add more browsers/OS combinations as needed
      ]
    })
  };
  request(options, function (error, response, body) {
    if (error) throw new Error(error);
    console.log(body);
  });
  ```
此功能对于快速识别 UI 问题至关重要，无需手动[cross-browser testing](../C/cross-browser-testing.md)，从而节省时间和资源。屏幕截图还可以与团队成员或利益相关者共享，以提供测试结果的视觉证据。
