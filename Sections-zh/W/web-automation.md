# 网络自动化

<!-- TOC START -->
- [有关 Web 自动化的问题吗？](#有关-web-自动化的问题吗？)
  - [基础知识和重要性](#基础知识和重要性)
    - [什么是网络自动化？](#什么是网络自动化？)
    - [为什么网络自动化很重要？](#为什么网络自动化很重要？)
    - [Web 自动化的关键组件是什么？](#web-自动化的关键组件是什么？)
    - [自动化 Web 任务有哪些好处？](#自动化-web-任务有哪些好处？)
    - [Web 自动化的潜在缺点或挑战是什么？](#web-自动化的潜在缺点或挑战是什么？)
  - [工具和技术](#工具和技术)
    - [用于网络自动化的一些流行工具有哪些？](#用于网络自动化的一些流行工具有哪些？)
    - [Selenium 是什么以及它如何在 Web 自动化中使用？](#selenium-是什么以及它如何在-web-自动化中使用？)
    - [JavaScript 在 Web 自动化中的作用是什么？](#javascript-在-web-自动化中的作用是什么？)
    - [Puppeteer 或 WebDriver 这样的工具如何帮助实现 Web 自动化？](#puppeteer-或-webdriver-这样的工具如何帮助实现-web-自动化？)
    - [Selenium、Puppeteer 和 Cypress 等工具之间有什么区别？](#selenium、puppeteer-和-cypress-等工具之间有什么区别？)
  - [流程和技术](#流程和技术)
    - [设置 Web 自动化测试的过程是怎样的？](#设置-web-自动化测试的过程是怎样的？)
    - [Web 自动化中有哪些常用技术？](#web-自动化中有哪些常用技术？)
    - [如何处理 Web 自动化中的动态内容？](#如何处理-web-自动化中的动态内容？)
    - [编写自动化脚本的最佳实践是什么？](#编写自动化脚本的最佳实践是什么？)
    - [如何在网站上自动提交表单或进行用户交互？](#如何在网站上自动提交表单或进行用户交互？)
  - [高级概念](#高级概念)
    - [如何在 Web 自动化中处理 CAPTCHA 或双因素身份验证？](#如何在-web-自动化中处理-captcha-或双因素身份验证？)
    - [什么是无头浏览器自动化以及它为什么有用？](#什么是无头浏览器自动化以及它为什么有用？)
    - [如何确保您的 Web 自动化测试可靠且稳健？](#如何确保您的-web-自动化测试可靠且稳健？)
    - [如何使用 Web 自动化进行性能测试？](#如何使用-web-自动化进行性能测试？)
    - [人工智能在网络自动化中的作用是什么？](#人工智能在网络自动化中的作用是什么？)
<!-- TOC END -->

网站的程序化操作通过

测试脚本

和工具，取代手动任务以节省时间并降低成本。

## 有关 Web 自动化的问题吗？

### 基础知识和重要性

#### 什么是网络自动化？

[Web automation](../W/web-automation.md) 是指使用软件模拟用户与网络浏览器和网络应用程序交互的过程。它涉及执行脚本来执行诸如单击按钮、将数据输入表单、浏览网站和提取信息等任务。这样做通常是为了测试 Web 应用程序的功能和性能，以确保它们在不同的浏览器和设备上按预期工作。
  **[Web automation](../W/web-automation.md)** 是通过专门的工具和框架实现的，这些工具和框架根据 HTML 结构与 Web 元素进行交互。这些工具可以以编程方式控制浏览器，模仿用户操作，无需手动干预。它们可以集成到 [automated testing](../A/automated-testing.md) 和部署的持续集成管道中。
  为了实现[web automation](../W/web-automation.md)，工程师使用JavaScript、Python或Java等语言编写脚本，这些语言利用自动化工具提供的[APIs](../A/api.md)。这些脚本可以很简单，执行单个操作，也可以很复杂，涵盖用户旅程的多个步骤。
  例如，自动化登录过程可能涉及：

  ```
  const { By, Key, until } = require('selenium-webdriver');
  (async function example() {
    let driver = await new Builder().forBrowser('firefox').build();
    try {
      await driver.get('http://www.example.com');
      await driver.findElement(By.name('username')).sendKeys('yourUsername');
      await driver.findElement(By.name('password')).sendKeys('yourPassword', Key.RETURN);
      await driver.wait(until.titleIs('Dashboard'), 1000);
    } finally {
      await driver.quit();
    }
  })();
  ```此脚本使用 **[Selenium](../S/selenium.md) [WebDriver](../W/webdriver.md)** 导航到网站，填写登录表单，然后等待仪表板页面加载。它说明了基本的 [web automation](../W/web-automation.md) 任务，该任务可以扩展为包括错误处理、数据验证和其他复杂的交互。

#### 为什么网络自动化很重要？

[Web automation](../W/web-automation.md) 至关重要，原因如下：

- **可扩展性**：它能够以手动测试无法比拟的规模测试复杂的 Web 应用程序。
  - **一致性**：自动化测试每次都精确执行相同的步骤，确保测试结果一致。
  - **速度**：自动化显着减少了重复测试所需的时间，从而缩短了开发周期。
  - **覆盖范围**：它允许广泛的测试覆盖范围，包括多个浏览器、版本和设备。
  - **效率**：将人力资源从重复性任务中解放出来，使他们能够专注于更具创造性的测试场景和探索性测试。
  - **早期[Bug](../B/bug.md) 检测**：自动化测试可以集成到 CI/CD 管道中，在开发过程的早期发现问题。
  - **成本降低**：虽然存在初始设置成本，但随着时间的推移，自动化可以通过减少手动测试所花费的时间和资源来节省成本。
  - **[Performance Testing](../P/performance-testing.md)** ：启用难以手动执行的压力、负载和性能测试。
  - **反馈循环**：向开发人员提供即时反馈，提高 Web 应用程序的质量和可靠性。
  总之，[web automation](../W/web-automation.md) 是维持 Web 应用程序的**质量**、**可靠性**和**性能**，同时优化开发和测试生命周期的关键因素。

- **可扩展性**：它能够以手动测试无法比拟的规模测试复杂的 Web 应用程序。
  - **一致性**：自动化测试每次都精确执行相同的步骤，确保测试结果一致。
  - **速度**：自动化显着减少了重复测试所需的时间，从而缩短了开发周期。
  - **覆盖范围**：它允许广泛的测试覆盖范围，包括多个浏览器、版本和设备。
  - **效率**：将人力资源从重复性任务中解放出来，使他们能够专注于更具创造性的测试场景和探索性测试。
  - **早期[Bug](../B/bug.md) 检测**：自动化测试可以集成到 CI/CD 管道中，在开发过程的早期发现问题。
  - **成本降低**：虽然存在初始设置成本，但随着时间的推移，自动化可以通过减少手动测试所花费的时间和资源来节省成本。
  - **[Performance Testing](../P/performance-testing.md)** ：启用难以手动执行的压力、负载和性能测试。
  - **反馈循环**：向开发人员提供即时反馈，提高 Web 应用程序的质量和可靠性。

#### Web 自动化的关键组件是什么？

[web automation](../W/web-automation.md) 的关键组件包括：

- **测试框架**：提供编写和组织测试的结构，例如 Mocha、Jest 或 Jasmine。
  - **驱动程序和浏览器**：与浏览器的接口；用于跨浏览器测试的WebDriver、用于Chrome的ChromeDriver等。
  - **选择器**：识别网页元素； CSS、XPath 或 jQuery 等特定库。
  - **[APIs](../A/api.md)** ：与网页交互； WebDriver API、Puppeteer API。
  - **断言库**：检查条件； Chai、Expect 或测试框架中的内置断言。
  - **[Test Runners](../T/test-runner.md)** ：执行测试；内置框架或像 Karma 这样的独立框架。
  - **报告工具**：生成测试报告；魅力，摩卡威。
  - **持续集成 (CI) 系统**：与 CI/CD 管道集成；詹金斯、特拉维斯 CI、GitHub 操作。
  - **版本控制系统**：管理测试代码；吉特、SVN。
  - **数据管理**：处理测试数据；固定装置、工厂或数据驱动的测试方法。
  - **Mocking 和 Stubbing** ：模拟后端响应或复杂的用户交互；西农，诺克。
  - **错误处理**：管理异常和不稳定的测试；尝试/捕获，重试。
  - **日志记录**：跟踪测试执行细节；温斯顿，Log4js。
  - **环境管理**：配置测试环境；码头工人，库伯内斯。
  - **[Performance Testing](../P/performance-testing.md) 工具**：评估速度和可扩展性；灯塔，网页测试。
  - **[Security Testing](../S/security-testing.md) 工具**：检查漏洞； OWASP ZAP、Burp Suite。

  ```
  // Example of a simple assertion using Chai
  const expect = require('chai').expect;
  expect(true).to.be.true;
  ```这些组件共同创建一个全面的[web automation](../W/web-automation.md) [setup](../S/setup.md)，使工程师能够有效地编写、运行和维护测试。

- **测试框架**：提供编写和组织测试的结构，例如 Mocha、Jest 或 Jasmine。
  - **驱动程序和浏览器**：与浏览器的接口；用于跨浏览器测试的WebDriver、用于Chrome的ChromeDriver等。
  - **选择器**：识别网页元素； CSS、XPath 或 jQuery 等特定库。
  - **[APIs](../A/api.md)** ：与网页交互； WebDriver API、Puppeteer API。
  - **断言库**：检查条件； Chai、Expect 或测试框架中的内置断言。
  - **[Test Runners](../T/test-runner.md)** ：执行测试；内置框架或像 Karma 这样的独立框架。
  - **报告工具**：生成测试报告；魅力，摩卡威。
  - **持续集成 (CI) 系统**：与 CI/CD 管道集成；詹金斯、特拉维斯 CI、GitHub 操作。
  - **版本控制系统**：管理测试代码；吉特、SVN。
  - **数据管理**：处理测试数据；固定装置、工厂或数据驱动的测试方法。
  - **Mocking 和 Stubbing** ：模拟后端响应或复杂的用户交互；西农，诺克。
  - **错误处理**：管理异常和不稳定的测试；尝试/捕获，重试。
  - **日志记录**：跟踪测试执行细节；温斯顿，Log4js。
  - **环境管理**：配置测试环境；码头工人，库伯内斯。
  - **[Performance Testing](../P/performance-testing.md) 工具**：评估速度和可扩展性；灯塔，网页测试。
  - **[Security Testing](../S/security-testing.md) 工具**：检查漏洞； OWASP ZAP、Burp Suite。

#### 自动化 Web 任务有哪些好处？

自动化 Web 任务有几个好处：

- **效率**：自动化执行任务的速度比手动流程更快，显着减少重复任务所需的时间。
  - **一致性**：自动化任务每次都以相同的方式执行操作，消除人为错误并确保结果一致。
  - **可扩展性**：自动化可以处理工作量的增加，无需额外的人力资源，从而可以轻松扩展操作。
  - **降低成本**：随着时间的推移，自动化可以节省劳动力成本，并释放人力资源来执行需要批判性思维的更复杂的任务。
  - **24/7 运行**：自动化系统可以全天候运行，不间断，从而提高生产率。
  - **改进[Test Coverage](../T/test-coverage.md)**：自动化允许更广泛的测试覆盖范围，包括可能耗时或难以手动执行的复杂场景。
  - **快速反馈**：自动化测试为开发人员提供即时反馈，加快开发周期和错误修复过程。
  - **可靠性**：自动化测试比手动测试更可靠，因为它们不易产生人为疲劳和监督。
  - **文档**：自动化测试作为测试程序和预期结果的文档，这对于入职和知识转移非常有用。
  - **集成**：自动化可以与其他工具和系统集成，例如持续集成/持续部署（CI/CD）管道，从而增强整体开发工作流程。
  通过利用自动化，测试工程师可以专注于设计更好的测试和提高软件质量，而不是执行单调的任务。

- **效率**：自动化执行任务的速度比手动流程更快，显着减少重复任务所需的时间。
  - **一致性**：自动化任务每次都以相同的方式执行操作，消除人为错误并确保结果一致。
  - **可扩展性**：自动化可以处理工作量的增加，无需额外的人力资源，从而可以轻松扩展操作。
  - **降低成本**：随着时间的推移，自动化可以节省劳动力成本，并释放人力资源来执行需要批判性思维的更复杂的任务。
  - **24/7 运行**：自动化系统可以全天候运行，不间断，从而提高生产率。
  - **改进[Test Coverage](../T/test-coverage.md)**：自动化允许更广泛的测试覆盖范围，包括可能耗时或难以手动执行的复杂场景。
  - **快速反馈**：自动化测试为开发人员提供即时反馈，加快开发周期和错误修复过程。
  - **可靠性**：自动化测试比手动测试更可靠，因为它们不易产生人为疲劳和监督。
  - **文档**：自动化测试作为测试程序和预期结果的文档，这对于入职和知识转移非常有用。
  - **集成**：自动化可以与其他工具和系统集成，例如持续集成/持续部署（CI/CD）管道，从而增强整体开发工作流程。

#### Web 自动化的潜在缺点或挑战是什么？

[Web automation](../W/web-automation.md) 虽然功能强大，但也有自己的一系列**挑战**：

- **[Maintainability](../M/maintainability.md)** ：随着频繁的 UI 更改，自动化测试可能会变得脆弱，从而导致高昂的维护成本。
  - **复杂性**：处理复杂的场景（例如文件上传、下载或与非 HTML 元素的交互）可能很棘手。
  - **不稳定**：由于计时问题、网络延迟或外部依赖性，测试可能会间歇性地通过或失败。
  - **资源密集型**：运行大量测试可能会消耗大量计算资源。
  - **跨浏览器不一致**：确保不同浏览器和版本之间的行为一致可能很困难。
  - **有限交互**：可能不完全支持模拟复杂的用户行为，例如拖放或多点触控手势。
  - **安全限制**：Web 自动化工具在与具有严格安全措施的网站交互时可能会面临限制。
  - **异步操作**：处理 AJAX 调用并等待元素变得可用而不诉诸任意睡眠调用需要仔细设计。
  - **环境差异**：本地、临时和生产环境之间的差异可能会导致误报或漏报。
  - **学习曲线**：掌握网络自动化工具和最佳实践需要时间和精力。
  - **开销**：自动化框架和基础设施的初始设置和配置可能非常耗时。
  - **虚假信心**：通过测试并不能保证应用程序没有错误；他们只断言经过明确测试的内容。
  为了缓解这些挑战，工程师应专注于创建**弹性**和**灵活**[test suites](../T/test-suite.md)，使用**显式等待**而不是隐式等待，维护**可扩展的[test environment](../T/test-environment.md)**，并持续**重构**测试以适应应用程序更改。

- **[Maintainability](../M/maintainability.md)** ：随着频繁的 UI 更改，自动化测试可能会变得脆弱，从而导致高昂的维护成本。
  - **复杂性**：处理复杂的场景（例如文件上传、下载或与非 HTML 元素的交互）可能很棘手。
  - **不稳定**：由于计时问题、网络延迟或外部依赖性，测试可能会间歇性地通过或失败。
  - **资源密集型**：运行大量测试可能会消耗大量计算资源。
  - **跨浏览器不一致**：确保不同浏览器和版本之间的行为一致可能很困难。
  - **有限交互**：可能不完全支持模拟复杂的用户行为，例如拖放或多点触控手势。
  - **安全限制**：Web 自动化工具在与具有严格安全措施的网站交互时可能会面临限制。
  - **异步操作**：处理 AJAX 调用并等待元素变得可用而不诉诸任意睡眠调用需要仔细设计。
  - **环境差异**：本地、临时和生产环境之间的差异可能会导致误报或漏报。
  - **学习曲线**：掌握网络自动化工具和最佳实践需要时间和精力。
  - **开销**：自动化框架和基础设施的初始设置和配置可能非常耗时。
  - **虚假信心**：通过测试并不能保证应用程序没有错误；他们只断言经过明确测试的内容。

### 工具和技术

#### 用于网络自动化的一些流行工具有哪些？

[web automation](../W/web-automation.md) 的热门工具包括：

- **TestComplete**：为 Web、移动和桌面应用程序提供强大且多功能的测试环境。支持多种脚本语言，如 JavaScript、Python 和 VBScript。
  - **Katalon Studio**：一种一体化自动化解决方案，具有用户友好的界面，用于为 Web、[API](../A/api.md)、移动和桌面应用程序创建自动化测试。
  - **UFT（统一[Functional Testing](../F/functional-testing.md)）**：以前称为 QTP，UFT 为功能性和[regression testing](../R/regression-testing.md) 提供了全面的[test automation](../T/test-automation.md) 解决方案以及可视化脚本界面。
  - **Protractor**：专为 Angular 和 AngularJS 应用程序设计的端到端测试框架，它在真实的浏览器中针对您的应用程序运行测试。
  - **Watir**：一个用于自动化 Web 浏览器的 Ruby 库，它允许您编写易于阅读和维护的测试。
  - **Playwright**：一个 Node 库，可通过单个 [API](../A/api.md) 实现 Chromium、Firefox 和 WebKit 的自动化。它使跨浏览器[web automation](../W/web-automation.md)成为常青、强大、可靠和快速的。
  - **Appium**：一种开源工具，用于在 iOS 和 Android 平台上自动化本机、移动 Web 和混合应用程序。
  - **Nightwatch.js**：使用 W3C [WebDriver](../W/webdriver.md) [API](../A/api.md) 为基于浏览器的应用程序和网站提供 [Node.js](../N/node-js.md) 驱动的 [end-to-end testing](../E/end-to-end-testing.md) 解决方案。
  - **CodeceptJS**：一个现代的 [end-to-end testing](../E/end-to-end-testing.md) 框架，具有 [BDD](../B/bdd.md) 风格的语法，它包装了 WebDriverIO 或 Protractor。
  - **TestCafe**：一个[node.js](../N/node-js.md) 工具，用于自动化端到端[web testing](../W/web-testing.md)。它不需要[WebDriver](../W/webdriver.md)或任何其他测试软件。
  每个工具都有其独特的功能，可能更适合特定的场景或偏好。根据项目的需求评估它们非常重要。

- **TestComplete**：为 Web、移动和桌面应用程序提供强大且多功能的测试环境。支持多种脚本语言，如 JavaScript、Python 和 VBScript。
  - **Katalon Studio**：一种一体化自动化解决方案，具有用户友好的界面，用于为 Web、[API](../A/api.md)、移动和桌面应用程序创建自动化测试。
  - **UFT（统一[Functional Testing](../F/functional-testing.md)）**：以前称为 QTP，UFT 为功能性和[regression testing](../R/regression-testing.md) 提供了全面的[test automation](../T/test-automation.md) 解决方案以及可视化脚本界面。
  - **Protractor**：专为 Angular 和 AngularJS 应用程序设计的端到端测试框架，它在真实的浏览器中针对您的应用程序运行测试。
  - **Watir**：一个用于自动化 Web 浏览器的 Ruby 库，它允许您编写易于阅读和维护的测试。
  - **Playwright**：一个 Node 库，可通过单个 [API](../A/api.md) 实现 Chromium、Firefox 和 WebKit 的自动化。它使跨浏览器 [web automation](../W/web-automation.md) 成为常​​绿、强大、可靠且快速的。
  - **Appium**：一种开源工具，用于在 iOS 和 Android 平台上自动化本机、移动 Web 和混合应用程序。
  - **Nightwatch.js**：使用 W3C [WebDriver](../W/webdriver.md) [API](../A/api.md)，为基于浏览器的应用程序和网站提供 [Node.js](../N/node-js.md) 驱动的 [end-to-end testing](../E/end-to-end-testing.md) 解决方案。
  - **CodeceptJS**：一个现代的 [end-to-end testing](../E/end-to-end-testing.md) 框架，具有 [BDD](../B/bdd.md) 风格的语法，它包装了 WebDriverIO 或 Protractor。
  - **TestCafe**：一个[node.js](../N/node-js.md) 工具，用于自动化端到端[web testing](../W/web-testing.md)。它不需要[WebDriver](../W/webdriver.md)或任何其他测试软件。

#### Selenium 是什么以及它如何在 Web 自动化中使用？

[Selenium](../S/selenium.md) 是一个开源 **[test automation](../T/test-automation.md) 框架**，主要用于自动化 Web 浏览器。它支持多种编程语言，包括 Java、C#、Python、Ruby 和 JavaScript，允许工程师用他们选择的语言编写[test scripts](../T/test-script.md)。
  [Selenium](../S/selenium.md) 的核心是 **[WebDriver](../W/webdriver.md) [API](../A/api.md)**，它提供了一个独立于平台的接口来控制浏览器。工程师使用[WebDriver](../W/webdriver.md) 来模拟用户交互，例如单击按钮、输入文本和浏览网页。
  以下是用 Python 编写的 [Selenium](../S/selenium.md) [WebDriver](../W/webdriver.md) 脚本的基本示例：

  ```
  from selenium import webdriver
  # Initialize the WebDriver instance using a specific browser driver
  driver = webdriver.Chrome()
  # Navigate to a web page
  driver.get("https://www.example.com")
  # Interact with elements on the page
  search_box = driver.find_element_by_name('q')
  search_box.send_keys('Selenium')
  search_box.submit()
  # Close the browser
  driver.quit()
  ```[Selenium](../S/selenium.md) 支持各种**浏览器驱动程序**（Google Chrome 的 ChromeDriver、Firefox 的 GeckoDriver 等），它们充当 [Selenium](../S/selenium.md) [WebDriver](../W/webdriver.md) 和浏览器本身之间的桥梁。
  对于复杂的场景，**[Selenium](../S/selenium.md) Grid**可用于在不同的机器和浏览器上同时运行测试，这增强了[test coverage](../T/test-coverage.md)并加快了执行速度。
  [Selenium](../S/selenium.md) 的多功能性以及与众多测试框架和 CI/CD 工具的兼容性使其成为[web automation](../W/web-automation.md) 的首选。然而，它需要对编程和网络技术有深入的了解才能有效地创建和维护[test scripts](../T/test-script.md)。

#### JavaScript 在 Web 自动化中的作用是什么？

由于 JavaScript 在 Web 浏览器中的本机支持以及与网页元素交互的能力，因此 JavaScript 在 [web automation](../W/web-automation.md) 中发挥着**核心作用**。它是网络的**脚本语言**，使自动化工具能够执行以下任务：

- **操作 DOM**：JavaScript 可以创建、修改或删除网页上的元素，这对于模拟用户交互至关重要。
  - **事件处理**：它可以触发并响应点击、表单提交和键盘输入等事件，从而实现真实的用户场景模拟。
  - **异步操作**：借助 Promise 和 async/await 等功能，JavaScript 可以处理异步操作，例如等待页面加载或 AJAX 请求，这在现代 Web 应用程序中很常见。
  - **浏览器控制**：使用 JavaScript 的自动化框架可以以编程方式控制浏览器会话、在页面之间导航以及管理 cookie 或本地存储。
  - **与[APIs](../A/api.md)**集成：JavaScript可以轻松地与各种API集成，从而可以扩展自动化功能或与外部服务交互。
  **Puppeteer** 和 **[Cypress](../C/cypress.md)** 等框架基于 JavaScript 构建，并提供丰富的 [APIs](../A/api.md) 集，以在 [Node.js](../N/node-js.md) 环境中自动化 Chrome 和其他浏览器。下面是一个简单的 Puppeteer 脚本示例：

  ```
  const puppeteer = require('puppeteer');
  (async () => {
    const browser = await puppeteer.launch();
    const page = await browser.newPage();
    await page.goto('https://example.com');
    // More automation code here
    await browser.close();
  })();
  ```综上所述，JavaScript 在 Web 开发中的普遍存在及其强大的功能使其成为[web automation](../W/web-automation.md) 不可或缺的工具。

- **操作 DOM**：JavaScript 可以创建、修改或删除网页上的元素，这对于模拟用户交互至关重要。
  - **事件处理**：它可以触发并响应点击、表单提交和键盘输入等事件，从而实现真实的用户场景模拟。
  - **异步操作**：借助 Promise 和 async/await 等功能，JavaScript 可以处理异步操作，例如等待页面加载或 AJAX 请求，这在现代 Web 应用程序中很常见。
  - **浏览器控制**：使用 JavaScript 的自动化框架可以以编程方式控制浏览器会话、在页面之间导航以及管理 cookie 或本地存储。
  - **与[APIs](../A/api.md)**集成：JavaScript可以轻松地与各种API集成，从而可以扩展自动化功能或与外部服务交互。

#### Puppeteer 或 WebDriver 这样的工具如何帮助实现 Web 自动化？

Puppeteer 和[WebDriver](../W/webdriver.md) 通过提供[APIs](../A/api.md) 以编程方式控制网络浏览器来促进[web automation](../W/web-automation.md)。 **Puppeteer** 仅适用于 Google Chrome 或 Chromium，而 **[WebDriver](../W/webdriver.md)** 是一种与浏览器无关的协议，被各种工具（包括 [Selenium](../S/selenium.md)）使用，与不同的浏览器进行交互。
  Puppeteer 允许通过 DevTools 协议**直接操作** Chrome/Chromium。它对于需要高级别的浏览器控制的任务特别有用，例如生成 PDF、截取屏幕截图或测试 Chrome 扩展。 Puppeteer 脚本通常用 JavaScript 或 TypeScript 编写，可以在 **无头** 模式下执行，这种模式速度更快，需要的资源更少，因为不显示 UI。

  ```
  const puppeteer = require('puppeteer');
  (async () => {
    const browser = await puppeteer.launch();
    const page = await browser.newPage();
    await page.goto('https://example.com');
    await page.screenshot({ path: 'example.png' });
    await browser.close();
  })();
  ```另一方面，[WebDriver](../W/webdriver.md) 通过 **[WebDriver](../W/webdriver.md) 协议**与浏览器进行通信，该协议由 W3C 标准化。这允许 [cross-browser testing](../C/cross-browser-testing.md)，并且对于确保 Web 应用程序在不同环境中一致工作至关重要。 [WebDriver](../W/webdriver.md) 实现适用于各种编程语言，可以与不同的技术堆栈进行更广泛的集成。

  ```
  WebDriver driver = new ChromeDriver();
  driver.get("https://example.com");
  WebElement element = driver.findElement(By.name("q"));
  element.sendKeys("WebDriver");
  element.submit();
  driver.quit();
  ```这两种工具都是自动化浏览器任务不可或缺的一部分，从简单的页面交互到复杂的端到端测试，提高了测试过程的效率和可靠性。

#### Selenium、Puppeteer 和 Cypress 等工具之间有什么区别？

[Selenium](../S/selenium.md)、Puppeteer 和[Cypress](../C/cypress.md) 都是流行的[web automation](../W/web-automation.md) 工具，每个工具都具有独特的功能和[use cases](../U/use-case.md)。
  **[Selenium](../S/selenium.md)** 是一款多功能工具，支持多种语言（Java、C#、Python 等）和浏览器（Chrome、Firefox、IE 等）。它使用特定于每个浏览器的驱动程序来实现自动化，并且可以集成到各种测试框架和 CI/CD 管道中。 [Selenium](../S/selenium.md) 是[cross-browser testing](../C/cross-browser-testing.md) 的理想选择，并在业界得到广泛采用。
  另一方面，**Puppeteer** 是由 Google 开发的 Node 库，专门与 Chrome 或 Chromium 配合使用。它提供了一个高级 [API](../A/api.md) 来控制无头 Chrome 或 Chromium，使其对于生成页面屏幕截图、PDF 和自动表单提交等任务非常有用。 Puppeteer 在处理严重依赖 JavaScript 的现代 Web 应用程序时以其易用性而闻名。
  **[Cypress](../C/cypress.md)** 也是[Node.js](../N/node-js.md) 工具，但不同之处在于它是专门为[end-to-end testing](../E/end-to-end-testing.md) 构建的。与远程控制浏览器的[Selenium](../S/selenium.md) 不同，[Cypress](../C/cypress.md) 与应用程序在同一运行循环中运行。这种架构允许更快的执行和更容易的调试。 [Cypress](../C/cypress.md) 带有内置的 [test runner](../T/test-runner.md) 和断言库，使其成为一个更加一体化的解决方案。然而，它目前仅支持有限数量的浏览器，并且主要用于在开发过程中测试应用程序。
  每个工具都有其优点，并根据项目要求进行选择，例如浏览器支持、语言偏好以及[test automation](../T/test-automation.md) 策略的特定需求。

### 流程和技术

#### 设置 Web 自动化测试的过程是怎样的？

设置 [web automation](../W/web-automation.md) 测试涉及几个关键步骤：

1. **选择与您首选的 [web automation](../W/web-automation.md) 工具集成的测试框架**，例如 Mocha、[Jest](../J/jest.md) 或 [Jasmine](../J/jasmine.md)。
  2. **搭建环境**：
    - 安装必要的
      **网络驱动程序**
      对于您正在测试的浏览器。

- 确保
      **语言绑定**
      （例如，Java、Python、JavaScript）适用于所选工具。

- 安装必要的
      **网络驱动程序**
      对于您正在测试的浏览器。

- 确保
      **语言绑定**
      （例如，Java、Python、JavaScript）适用于所选工具。

3. **配置[test runner](../T/test-runner.md)**：
    - 定义
      **[test suites](../T/test-suite.md)**
      和
      **[test cases](../T/test-case.md)**
      。

- 设置
      **测试参数**
      ，例如超时和重试。

- 定义
      **[test suites](../T/test-suite.md)**
      和
      **[test cases](../T/test-case.md)**
      。

- 设置
      **测试参数**
      ，例如超时和重试。

4. **写[test scripts](../T/test-script.md)**：
    - 使用
      **[Page Object Model](../P/page-object-model.md) (POM)**
      为了可维护性。

- 实施
      **断言**
      检查预期结果。

- 使用
      **[Page Object Model](../P/page-object-model.md) (POM)**
      为了可维护性。

- 实施
      **断言**
      检查预期结果。

5. **管理[test data](../T/test-data.md)**：
    - 使用
      **外部数据源**
      （例如，JSON、CSV）用于输入数据。

- 实施
      **数据驱动测试**
      如果需要的话。

- 使用
      **外部数据源**
      （例如，JSON、CSV）用于输入数据。

- 实施
      **数据驱动测试**
      如果需要的话。

6. **处理浏览器会话**：
    - 启动一个新的浏览器实例。
    - 导航至
      **目标网址**
      。

- 启动一个新的浏览器实例。
    - 导航至
      **目标网址**
      。

7. **与网页元素交互**：
    - 使用定位元素
      **选择器**
      （例如 CSS、XPath）。

- 执行单击、输入文本和获取数据等操作。
    - 使用定位元素
      **选择器**
      （例如 CSS、XPath）。

- 执行单击、输入文本和获取数据等操作。
  8. **实现同步**：
    - 使用
      **显式等待**
      处理动态内容。

- 使用
      **显式等待**
      处理动态内容。

9. **运行测试**：
    - 通过命令行或 CI/CD 管道执行测试。
    - 使用
      **并行执行**
      以获得更快的反馈。

- 通过命令行或 CI/CD 管道执行测试。
    - 使用
      **并行执行**
      以获得更快的反馈。

10. **分析测试结果**：
    - 回顾
      **日志**
      和
      **截图**
      对于失败。

- 与集成
      **报告工具**
      为了更好的可见性。

- 回顾
      **日志**
      和
      **截图**
      对于失败。

- 与集成
      **报告工具**
      为了更好的可见性。

11. **维护测试**：
    - 定期
      **重构**
      和
      **更新测试**
      随着应用程序的发展。

- 定期
      **重构**
      和
      **更新测试**
      随着应用程序的发展。

  ```
  // Example of a simple test script using Selenium WebDriver in JavaScript
  const { Builder, By, Key, until } = require('selenium-webdriver');
  (async function example() {
      let driver = await new Builder().forBrowser('firefox').build();
      try {
          await driver.get('http://www.example.com');
          await driver.findElement(By.name('q')).sendKeys('webdriver', Key.RETURN);
          await driver.wait(until.titleIs('webdriver - Google Search'), 1000);
      } finally {
          await driver.quit();
      }
  })();
  ```请记住随着工具和最佳实践的发展，**审查并调整**您的[setup](../S/setup.md)。

1. **选择与您首选的 [web automation](../W/web-automation.md) 工具集成的测试框架**，例如 Mocha、[Jest](../J/jest.md) 或 [Jasmine](../J/jasmine.md)。
  2. **搭建环境**：
    - 安装必要的
      **网络驱动程序**
      对于您正在测试的浏览器。

- 确保
      **语言绑定**
      （例如，Java、Python、JavaScript）适用于所选工具。

- 安装必要的
      **网络驱动程序**
      对于您正在测试的浏览器。

- 确保
      **语言绑定**
      （例如，Java、Python、JavaScript）适用于所选工具。

3. **配置[test runner](../T/test-runner.md)**：
    - 定义
      **[test suites](../T/test-suite.md)**
      和
      **[test cases](../T/test-case.md)**
      。

- 设置
      **测试参数**
      ，例如超时和重试。

- 定义
      **[test suites](../T/test-suite.md)**
      和
      **[test cases](../T/test-case.md)**
      。

- 设置
      **测试参数**
      ，例如超时和重试。

4. **写[test scripts](../T/test-script.md)**：
    - 使用
      **[Page Object Model](../P/page-object-model.md) (POM)**
      为了可维护性。

- 实施
      **断言**
      检查预期结果。

- 使用
      **[Page Object Model](../P/page-object-model.md) (POM)**
      为了可维护性。

- 实施
      **断言**
      检查预期结果。

5. **管理[test data](../T/test-data.md)**：
    - 使用
      **外部数据源**
      （例如，JSON、CSV）用于输入数据。

- 实施
      **数据驱动测试**
      如果需要的话。

- 使用
      **外部数据源**
      （例如，JSON、CSV）用于输入数据。

- 实施
      **数据驱动测试**
      如果需要的话。

6. **处理浏览器会话**：
    - 启动一个新的浏览器实例。
    - 导航至
      **目标网址**
      。

- 启动一个新的浏览器实例。
    - 导航至
      **目标网址**
      。

7. **与网页元素交互**：
    - 使用定位元素
      **选择器**
      （例如 CSS、XPath）。

- 执行单击、输入文本和获取数据等操作。
    - 使用定位元素
      **选择器**
      （例如 CSS、XPath）。

- 执行单击、输入文本和获取数据等操作。
  8. **实现同步**：
    - 使用
      **显式等待**
      处理动态内容。

- 使用
      **显式等待**
      处理动态内容。

9. **运行测试**：
    - 通过命令行或 CI/CD 管道执行测试。
    - 使用
      **并行执行**
      以获得更快的反馈。

- 通过命令行或 CI/CD 管道执行测试。
    - 使用
      **并行执行**
      以获得更快的反馈。

10. **分析测试结果**：
    - 回顾
      **日志**
      和
      **截图**
      对于失败。

- 与集成
      **报告工具**
      为了更好的可见性。

- 回顾
      **日志**
      和
      **截图**
      对于失败。

- 与集成
      **报告工具**
      为了更好的可见性。

11. **维护测试**：
    - 定期
      **重构**
      和
      **更新测试**
      随着应用程序的发展。

- 定期
      **重构**
      和
      **更新测试**
      随着应用程序的发展。

#### Web 自动化中有哪些常用技术？

[web automation](../W/web-automation.md) 中的常用技术包括：

- **数据驱动测试**：外部数据源（如 CSV、Excel 或[databases](../D/database.md)）驱动[test scripts](../T/test-script.md)，允许测试多个场景和输入组合。
  - **关键字驱动测试**：使用关键字定义测试，关键字描述要在 Web 应用程序上执行的操作，使测试更易于阅读和编写。
  - **[Page Object Model](../P/page-object-model.md) (POM)**：用于为 Web UI 元素创建对象存储库的设计模式。每个页面都由一个类表示，该类封装了页面的元素和行为，从而增强了[maintainability](../M/maintainability.md)。
  - **行为驱动开发 ([BDD](../B/bdd.md))**：将 TDD 的通用技术和原理与领域驱动设计和面向对象分析的思想相结合，为软件开发和管理团队提供共享工具和共享流程来协作进行软件开发。
  - **[Cross-Browser Testing](../C/cross-browser-testing.md)**：确保 Web 应用程序在不同浏览器和版本上正常运行，通常使用基于云的工具来提供对多个浏览器环境的访问。
  - **持续集成 (CI) 和持续部署 (CD)**：将 [web automation](../W/web-automation.md) 测试集成到 CI/CD 管道中，以便及早发现问题并自信地进行部署。
  - **[Visual Regression Testing](../V/visual-regression-testing.md)**：将网页的视觉效果与基线进行比较，以检测意外的更改。
  - **[API Testing](../A/api-testing.md)**：验证应用程序的[API](../A/api.md) 层的功能、可靠性、性能和安全性，该层通常是 Web 应用程序的关键组件。
  - **[Load Testing](../L/load-testing.md)**：模拟大量用户来测试应用程序在预期负载和峰值负载条件下的性能。
  - **[Accessibility Testing](../A/accessibility-testing.md)**：确保 Web 应用程序可供残疾人使用，符合 WCAG 等标准。
  - **移动[Web Testing](../W/web-testing.md)**：在移动设备或模拟器/仿真器上测试 Web 应用程序，以确保移动平台上的功能和可用性。
  - **数据驱动测试**：外部数据源（如 CSV、Excel 或[databases](../D/database.md)）驱动[test scripts](../T/test-script.md)，允许测试多个场景和输入组合。
  - **关键字驱动测试**：使用关键字定义测试，关键字描述要在 Web 应用程序上执行的操作，使测试更易于阅读和编写。
  - **[Page Object Model](../P/page-object-model.md) (POM)**：用于为 Web UI 元素创建对象存储库的设计模式。每个页面都由一个类表示，该类封装了页面的元素和行为，从而增强了[maintainability](../M/maintainability.md)。
  - **行为驱动开发 ([BDD](../B/bdd.md))**：将 TDD 的通用技术和原理与领域驱动设计和面向对象分析的思想相结合，为软件开发和管理团队提供共享工具和共享流程来协作进行软件开发。
  - **[Cross-Browser Testing](../C/cross-browser-testing.md)**：确保 Web 应用程序在不同浏览器和版本上正常运行，通常使用基于云的工具来提供对多个浏览器环境的访问。
  - **持续集成 (CI) 和持续部署 (CD)**：将 [web automation](../W/web-automation.md) 测试集成到 CI/CD 管道中，以便及早发现问题并自信地进行部署。
  - **[Visual Regression Testing](../V/visual-regression-testing.md)**：将网页的视觉效果与基线进行比较，以检测意外的更改。
  - **[API Testing](../A/api-testing.md)**：验证应用程序 [API](../A/api.md) 层的功能、可靠性、性能和安全性，该层通常是 Web 应用程序的关键组件。
  - **[Load Testing](../L/load-testing.md)**：模拟大量用户来测试应用程序在预期负载和峰值负载条件下的性能。
  - **[Accessibility Testing](../A/accessibility-testing.md)**：确保 Web 应用程序可供残疾人使用，符合 WCAG 等标准。
  - **移动[Web Testing](../W/web-testing.md)**：在移动设备或模拟器/仿真器上测试 Web 应用程序，以确保移动平台上的功能和可用性。

#### 如何处理 Web 自动化中的动态内容？

处理[web automation](../W/web-automation.md) 中的动态内容需要能够适应网页元素或数据变化的策略。以下是一些技巧：

- **CSS 选择器和 XPath** ：使用灵活的定位器，可以根据部分属性值或模式匹配元素。例如，XPath 的功能如下
    `contains()`
    可以帮助定位具有动态 ID 的元素。

  ```
  driver.findElement(By.xpath("//div[contains(@id,'dynamic-id-')]"));
  ```

- **等待命令**：实现显式等待以处理 AJAX 调用或 JavaScript 执行后出现的元素。 Selenium 等工具提供
    `WebDriverWait`
    等待某些条件。

  ```
  new WebDriverWait(driver, Duration.ofSeconds(10))
      .until(ExpectedConditions.visibilityOfElementLocated(By.id("dynamic-element")));
  ```

- **JavaScript执行**：执行JavaScript以与标准API方法难以处理的元素进行交互。

  ```
  ((JavascriptExecutor)driver).executeScript("arguments[0].click();", element);
  ```

- **[Page Object Model](../P/page-object-model.md) (POM)**：使用 POM 设计您的测试来封装与动态元素的交互，使您的测试更加可维护和灵活。
  - **数据驱动测试**：从[test scripts](../T/test-script.md) 外部化[test data](../T/test-data.md)。使用 CSV 文件或 [databases](../D/database.md) 等数据源将动态值输入到您的测试中。
  - **正则表达式**：使用正则表达式处理动态文本内容。它们可以匹配字符串中的模式，从而允许您验证或提取数据。
  - **[API](../A/api.md) 调用**：有时，通过 [API](../A/api.md) 调用直接与后端交互可能比处理 UI 更改更可靠。
  请记住**避免测试和 UI 之间的紧密耦合**。目标是**定位策略**能够适应变化和**抽象复杂性**，以使您的自动化脚本不那么脆弱。

- **CSS 选择器和 XPath** ：使用灵活的定位器，可以根据部分属性值或模式匹配元素。例如，XPath 的功能如下
    `contains()`
    可以帮助定位具有动态 ID 的元素。

- **等待命令**：实现显式等待以处理 AJAX 调用或 JavaScript 执行后出现的元素。 Selenium 等工具提供
    `WebDriverWait`
    等待某些条件。

- **JavaScript执行**：执行JavaScript以与标准API方法难以处理的元素进行交互。
  - **[Page Object Model](../P/page-object-model.md) (POM)**：使用 POM 设计您的测试来封装与动态元素的交互，使您的测试更加可维护和灵活。
  - **数据驱动测试**：从[test scripts](../T/test-script.md) 外部化[test data](../T/test-data.md)。使用 CSV 文件或 [databases](../D/database.md) 等数据源将动态值输入到您的测试中。
  - **正则表达式**：使用正则表达式处理动态文本内容。它们可以匹配字符串中的模式，从而允许您验证或提取数据。
  - **[API](../A/api.md) 调用**：有时，通过 [API](../A/api.md) 调用直接与后端交互可能比处理 UI 更改更可靠。

#### 编写自动化脚本的最佳实践是什么？

编写自动化脚本的最佳实践包括：

- **[Maintainability](../M/maintainability.md)** ：编写干净、可读且可维护的代码。使用页面对象模型将测试逻辑与特定于页面的代码分开。
  - **可重用性**：创建可重用的函数和类以避免代码重复。
  - **模块化**：将测试分解为更小的独立模块，以便于维护和更好的可重用性。
  - **版本控制**：使用 Git 等版本控制系统来跟踪更改并与团队成员协作。
  - **注释和文档**：在必要时注释您的代码并维护复杂逻辑的最新文档。
  - **数据驱动测试**：实施数据驱动测试，将测试逻辑与测试数据分开，从而实现轻松更新和可扩展性。
  - **错误处理**：实施强大的错误处理来管理测试执行流程并提供清晰的错误消息。
  - **断言**：使用清晰且适当的断言来验证测试结果。
  - **持续集成**：将您的测试与 CI/CD 管道集成，以确保它们在每个构建中运行。
  - **[Test Environment](../T/test-environment.md)** ：确保测试在稳定一致的环境中运行，以避免不稳定的结果。
  - **并行执行**：利用并行测试执行来减少运行时间并提供更快的反馈。
  - **报告**：生成详细且可操作的报告以有效分析测试结果。
  - **代码审查**：定期进行代码审查，以确保遵守最佳实践并提高代码质量。
  - **重构**：定期重构测试以提高性能和可维护性。
  - **等待策略**：实施智能等待策略而不是硬编码的睡眠来处理动态内容。

  ```
  // Example of a reusable function in a page object model
  class LoginPage {
    async login(username, password) {
      await this.enterUsername(username);
      await this.enterPassword(password);
      await this.submit();
    }
  }
  ```请记住，目标是创建高效、易于理解且快速适应变化的脚本。

- **[Maintainability](../M/maintainability.md)** ：编写干净、可读且可维护的代码。使用页面对象模型将测试逻辑与特定于页面的代码分开。
  - **可重用性**：创建可重用的函数和类以避免代码重复。
  - **模块化**：将测试分解为更小的独立模块，以便于维护和更好的可重用性。
  - **版本控制**：使用 Git 等版本控制系统来跟踪更改并与团队成员协作。
  - **注释和文档**：在必要时注释您的代码并维护复杂逻辑的最新文档。
  - **数据驱动测试**：实施数据驱动测试，将测试逻辑与测试数据分开，从而实现轻松更新和可扩展性。
  - **错误处理**：实施强大的错误处理来管理测试执行流程并提供清晰的错误消息。
  - **断言**：使用清晰且适当的断言来验证测试结果。
  - **持续集成**：将您的测试与 CI/CD 管道集成，以确保它们在每个构建中运行。
  - **[Test Environment](../T/test-environment.md)** ：确保测试在稳定一致的环境中运行，以避免不稳定的结果。
  - **并行执行**：利用并行测试执行来减少运行时间并提供更快的反馈。
  - **报告**：生成详细且可操作的报告以有效分析测试结果。
  - **代码审查**：定期进行代码审查，以确保遵守最佳实践并提高代码质量。
  - **重构**：定期重构测试以提高性能和可维护性。
  - **等待策略**：实施智能等待策略而不是硬编码的睡眠来处理动态内容。

#### 如何在网站上自动提交表单或进行用户交互？

要自动在网站上提交表单或进行用户交互，请按照以下步骤操作：

1. **识别元素**
    在网页上使用其唯一标识符（例如 ID、名称、CSS 选择器或 XPath）。

2. **实例化驱动程序**
    您正在自动化的浏览器的对象。

3. **导航至 URL**
    使用驱动程序的表格所在的位置
    `get`
    方法。

4. **与元素互动**
    使用类似的方法
    `click()`
    ,
    `sendKeys()`
    , 和
    `submit()`
    执行输入文本、选择选项或单击按钮等操作。

5. **断言预期行为**
    表单提交后，例如检查成功消息或页面重定向。
  以下是在 Python 中使用 [Selenium](../S/selenium.md) 的基本示例：

  ```
  from selenium import webdriver
  from selenium.webdriver.common.keys import Keys
  # Instantiate a browser driver
  driver = webdriver.Chrome()
  # Navigate to the form page
  driver.get("http://example.com/form")
  # Interact with form elements
  username = driver.find_element_by_id("username")
  password = driver.find_element_by_id("password")
  submit_button = driver.find_element_by_id("submit")
  username.send_keys("testuser")
  password.send_keys("password123")
  submit_button.click()
  # Assert the expected outcome
  assert "Success" in driver.page_source
  # Close the browser
  driver.quit()
  ```请记住在与元素交互之前**等待元素**出现或可见，必要时使用显式等待来处理动态内容。另外，请考虑**错误处理**以优雅地管理意外行为或故障。最后，在测试后通过关闭浏览器和任何其他使用的资源进行清理。

1. **识别元素**
    在网页上使用其唯一标识符（例如 ID、名称、CSS 选择器或 XPath）。

2. **实例化驱动程序**
    您正在自动化的浏览器的对象。

3. **导航至 URL**
    使用驱动程序的表格所在的位置
    `get`
    方法。

4. **与元素互动**
    使用类似的方法
    `click()`
    ,
    `sendKeys()`
    , 和
    `submit()`
    执行输入文本、选择选项或单击按钮等操作。

5. **断言预期行为**
    表单提交后，例如检查成功消息或页面重定向。

### 高级概念

#### 如何在 Web 自动化中处理 CAPTCHA 或双因素身份验证？

在 [web automation](../W/web-automation.md) 中处理 **CAPTCHA** 或 **双因素身份验证 (2FA)** 可能具有挑战性，因为它们的目的是将人类用户与机器人区分开来。以下是一些策略：

1. **验证码绕过选项**：
    - **[Test Environment](../T/test-environment.md)** ：与开发团队合作在测试环境中禁用验证码。
    - **[API](../A/api.md) Key** ：一些 CAPTCHA 提供商提供测试 API 密钥，这些密钥始终返回可预测的响应。
    - **白名单**：将自动化服务器的 IP 地址列入白名单以绕过验证码。
    - **[Test Environment](../T/test-environment.md)** ：与开发团队合作在测试环境中禁用验证码。
    - **[API](../A/api.md) Key** ：一些 CAPTCHA 提供商提供测试 API 密钥，这些密钥始终返回可预测的响应。
    - **白名单**：将自动化服务器的 IP 地址列入白名单以绕过验证码。
  2. **2FA 旁路选项**：
    - **静态代码**：使用为测试目的提供的静态备份代码。
    - **2FA 自动化**：使用 API 或电子邮件/短信自动化工具自动从电子邮件或短信中检索 2FA 代码。
    - **基于时间的一次性密码 (TOTP)** ：使用类似的库
      `pyotp`
      如果密钥可用，则在 Python 中生成 TOTP 代码。

- **静态代码**：使用为测试目的提供的静态备份代码。
    - **2FA 自动化**：使用 API 或电子邮件/短信自动化工具自动从电子邮件或短信中检索 2FA 代码。
    - **基于时间的一次性密码 (TOTP)** ：使用类似的库
      `pyotp`
      如果密钥可用，则在 Python 中生成 TOTP 代码。

3. **外部服务**：
    - **验证码解决服务**：使用付费的第三方服务来解决验证码。应谨慎且合乎道德地使用这种方法。
    - **验证码解决服务**：使用付费的第三方服务来解决验证码。应谨慎且合乎道德地使用这种方法。
  4. **手动干预**：
    - **手动输入**：暂停自动化并允许人类手动解决验证码或输入 2FA 代码。
    - **手动输入**：暂停自动化并允许人类手动解决验证码或输入 2FA 代码。
  5. **与安全策略的协调**：
    - **策略例外**：与安全团队协调以创建用于自动化目的的策略例外。
    - **策略例外**：与安全团队协调以创建用于自动化目的的策略例外。
  请记住，绕过验证码和 2FA 等安全功能应以尊重用户安全和隐私的方式进行，并且仅在法律和道德上可接受的环境中进行。始终优先考虑安全和负责任的测试实践。

1. **验证码绕过选项**：
    - **[Test Environment](../T/test-environment.md)** ：与开发团队合作在测试环境中禁用验证码。
    - **[API](../A/api.md) Key** ：一些 CAPTCHA 提供商提供测试 API 密钥，这些密钥始终返回可预测的响应。
    - **白名单**：将自动化服务器的 IP 地址列入白名单以绕过验证码。
    - **[Test Environment](../T/test-environment.md)** ：与开发团队合作在测试环境中禁用验证码。
    - **[API](../A/api.md) Key** ：一些 CAPTCHA 提供商提供测试 API 密钥，这些密钥始终返回可预测的响应。
    - **白名单**：将自动化服务器的 IP 地址列入白名单以绕过验证码。
  2. **2FA 旁路选项**：
    - **静态代码**：使用为测试目的提供的静态备份代码。
    - **2FA 自动化**：使用 API 或电子邮件/短信自动化工具自动从电子邮件或短信中检索 2FA 代码。
    - **基于时间的一次性密码 (TOTP)** ：使用类似的库
      `pyotp`
      如果密钥可用，则在 Python 中生成 TOTP 代码。

- **静态代码**：使用为测试目的提供的静态备份代码。
    - **2FA 自动化**：使用 API 或电子邮件/短信自动化工具自动从电子邮件或短信中检索 2FA 代码。
    - **基于时间的一次性密码 (TOTP)** ：使用类似的库
      `pyotp`
      如果密钥可用，则在 Python 中生成 TOTP 代码。

3. **外部服务**：
    - **验证码解决服务**：使用付费的第三方服务来解决验证码。应谨慎且合乎道德地使用这种方法。
    - **验证码解决服务**：使用付费的第三方服务来解决验证码。应谨慎且合乎道德地使用这种方法。
  4. **手动干预**：
    - **手动输入**：暂停自动化并允许人类手动解决验证码或输入 2FA 代码。
    - **手动输入**：暂停自动化并允许人类手动解决验证码或输入 2FA 代码。
  5. **与安全策略的协调**：
    - **策略例外**：与安全团队协调以创建用于自动化目的的策略例外。
    - **策略例外**：与安全团队协调以创建用于自动化目的的策略例外。

#### 什么是无头浏览器自动化以及它为什么有用？

无头浏览器自动化是指在没有图形用户界面 (GUI) 的情况下运行浏览器驱动的测试的做法。这是通过使用无头浏览器来实现的，无头浏览器是屏幕上没有可见窗口的网络浏览器。无头浏览器可以执行常规浏览器可以执行的所有任务，例如渲染 HTML、执行 JavaScript 和处理用户事件，但它们是在后台执行的。
  **无头浏览器自动化的用处：**

- **速度**：没有渲染 UI 的开销，无头浏览器运行速度更快，使测试执行更高效。
  - **资源效率**：它们消耗更少的内存和CPU，这在并行运行多个测试时特别有益。
  - **持续集成 (CI) 兼容性**：无头浏览器非常适合 CI 管道，因为它们可以在没有显示环境的服务器上运行。
  - **跨平台**：它们可以在各种操作系统上运行，而无需担心 GUI 差异。
  - **屏幕捕获和 DOM [Inspection](../I/inspection.md)** ：尽管缺少 GUI，无头浏览器可以捕获屏幕截图并提供用于调试的 DOM 访问。
  **Puppeteer 示例**：

  ```
  const puppeteer = require('puppeteer');
  (async () => {
    const browser = await puppeteer.launch({ headless: true });
    const page = await browser.newPage();
    await page.goto('https://example.com');
    // Perform automation tasks...
    await browser.close();
  })();
  ```在此代码片段中，Puppeteer 启动无头浏览器，导航到 URL，然后在执行自动化任务后关闭浏览器。这种方法对于[test automation](../T/test-automation.md) 来说是精简且高效的，特别是在开发或 CI/CD 环境中。

- **速度**：没有渲染 UI 的开销，无头浏览器运行速度更快，使测试执行更高效。
  - **资源效率**：它们消耗更少的内存和CPU，这在并行运行多个测试时特别有益。
  - **持续集成 (CI) 兼容性**：无头浏览器非常适合 CI 管道，因为它们可以在没有显示环境的服务器上运行。
  - **跨平台**：它们可以在各种操作系统上运行，而无需担心 GUI 差异。
  - **屏幕捕获和 DOM [Inspection](../I/inspection.md)** ：尽管缺乏 GUI，无头浏览器可以捕获屏幕截图并提供 DOM 访问以进行调试。

#### 如何确保您的 Web 自动化测试可靠且稳健？

为了确保 [web automation](../W/web-automation.md) 测试**可靠且稳健**，请遵循以下准则：

- **可重用性设计**：使用可重用组件创建模块化脚本，以最大限度地减少冗余并促进维护。
  - **实现显式等待**：使用显式等待来处理异步操作并确保元素在交互之前可用。
  - **使用[Page Object Model](../P/page-object-model.md) (POM)** ：将页面详细信息抽象为对象，将测试逻辑与UI结构分开，增强可维护性。
  - **优先选择选择器**：根据位置选择稳定且独特的选择器（例如 ID 或数据属性），而不是脆弱的选择器（例如 XPath）。
  - **处理异常**：实施强大的异常处理来管理意外事件并记录有用的错误信息。
  - **数据驱动测试**：外部化测试数据以允许参数化测试和轻松更新，而无需更改测试代码。
  - **版本控制**：使用版本控制系统来跟踪更改、协作并在必要时恢复到稳定状态。
  - **持续集成 (CI)**：将测试集成到 CI 管道中，以便尽早发现问题并确保测试在一致的环境中运行。
  - **[Cross-Browser Testing](../C/cross-browser-testing.md)** ：跨多个浏览器验证测试以确保兼容性并捕获特定于浏览器的问题。
  - **定期重构**：定期审查和重构测试，以提高效率、可读性并适应应用程序的变化。
  - **[Test Environment](../T/test-environment.md) 稳定性**：确保测试环境密切反映生产情况并且稳定以避免误报/漏报。
  - **监控和报告**：实施全面的报告和监控，以快速识别和解决测试失败。
  通过遵循这些实践，您可以显着提高 [web automation](../W/web-automation.md) 测试的可靠性和稳健性。

- **可重用性设计**：使用可重用组件创建模块化脚本，以最大限度地减少冗余并促进维护。
  - **实现显式等待**：使用显式等待来处理异步操作并确保元素在交互之前可用。
  - **使用[Page Object Model](../P/page-object-model.md) (POM)** ：将页面详细信息抽象为对象，将测试逻辑与UI结构分开，增强可维护性。
  - **优先选择选择器**：根据位置选择稳定且独特的选择器（例如 ID 或数据属性），而不是脆弱的选择器（例如 XPath）。
  - **处理异常**：实施强大的异常处理来管理意外事件并记录有用的错误信息。
  - **数据驱动测试**：外部化测试数据以允许参数化测试和轻松更新，而无需更改测试代码。
  - **版本控制**：使用版本控制系统来跟踪更改、协作并在必要时恢复到稳定状态。
  - **持续集成 (CI)**：将测试集成到 CI 管道中，以便尽早发现问题并确保测试在一致的环境中运行。
  - **[Cross-Browser Testing](../C/cross-browser-testing.md)** ：跨多个浏览器验证测试以确保兼容性并捕获特定于浏览器的问题。
  - **定期重构**：定期审查和重构测试，以提高效率、可读性并适应应用程序的变化。
  - **[Test Environment](../T/test-environment.md) 稳定性**：确保测试环境密切反映生产情况并且稳定以避免误报/漏报。
  - **监控和报告**：实施全面的报告和监控，以快速识别和解决测试失败。

#### 如何使用 Web 自动化进行性能测试？

[Web automation](../W/web-automation.md) 可用于 [performance testing](../P/performance-testing.md)，通过模拟多个用户或操作来测试 Web 应用程序的负载能力和响应能力。这涉及创建模仿用户行为的自动化脚本，例如单击、输入数据、导航页面和其他交互。
  要使用 [web automation](../W/web-automation.md) 执行 [performance testing](../P/performance-testing.md)：

1. **确定关键场景**
    对于测试，重点关注用户在使用应用程序时可能采取的关键路径。

2. **创建自动化[test scripts](../T/test-script.md)**
    复制这些用户操作。这些脚本应设计为同时运行以模拟多个用户。

3. **使用[performance testing](../P/performance-testing.md)工具**
    像 JMeter 或 LoadRunner，它们可以与 Web 自动化框架集成来生成和管理负载。

4. **配置测试**
    逐渐增加虚拟用户的数量，以了解应用程序在不同负载条件下的行为方式。

5. **监控应用程序性能**
    响应时间、错误率和系统资源利用率等指标。

6. **分析结果**
    识别瓶颈、性能下降和系统的最大容量。
  以下示例展示了如何使用 [JMeter](../J/jmeter.md) 和 Web 驱动程序来设置简单的负载测试：

  ```
  <ThreadGroup guiclass="ThreadGroupGui" testclass="ThreadGroup" testname="Simulate Users" enabled="true">
    <stringProp name="ThreadGroup.num_threads">50</stringProp>
    <stringProp name="ThreadGroup.ramp_time">10</stringProp>
    <stringProp name="ThreadGroup.duration"></stringProp>
    <boolProp name="ThreadGroup.scheduler">false</boolProp>
  </ThreadGroup>
  ```此 XML 片段配置 [JMeter](../J/jmeter.md) 以在 10 秒的启动期内模拟 50 个用户。将此与 Web 驱动程序脚本结合起来，在测试的 Web 应用程序上执行特定操作。

1. **确定关键场景**
    对于测试，重点关注用户在使用应用程序时可能采取的关键路径。

2. **创建自动化[test scripts](../T/test-script.md)**
    复制这些用户操作。这些脚本应设计为同时运行以模拟多个用户。

3. **使用[performance testing](../P/performance-testing.md)工具**
    像 JMeter 或 LoadRunner，它们可以与 Web 自动化框架集成来生成和管理负载。

4. **配置测试**
    逐渐增加虚拟用户的数量，以了解应用程序在不同负载条件下的行为方式。

5. **监控应用程序性能**
    响应时间、错误率和系统资源利用率等指标。

6. **分析结果**
    识别瓶颈、性能下降和系统的最大容量。

#### 人工智能在网络自动化中的作用是什么？

通过引入**自适应学习**和**预测分析**，人工智能在增强[web automation](../W/web-automation.md)方面发挥着**关键作用**。它有助于创建更加**智能**和**弹性** [test scripts](../T/test-script.md)，可以适应 Web 应用程序 UI 或功能的变化，而无需持续的人工干预。
  [web automation](../W/web-automation.md) 中人工智能的关键应用之一是**自我修复测试**。人工智能算法可以检测到测试何时由于应用程序中的微小变化而中断，并且可以**自动更新**选择器或交互模式以保持测试通过，从而减少维护开销。
  人工智能还支持**视觉测试**，机器学习模型可以比较网页的屏幕截图以检测视觉回归。这对于确保不同设备和浏览器之间的一致用户体验特别有用。
  此外，人工智能还可用于**智能测试生成**，它分析用户与 Web 应用程序的交互，以自动生成更能反映真实用户行为的 [test cases](../T/test-case.md)。
  AI 驱动的分析可以提供对 [test coverage](../T/test-coverage.md) 和缺陷模式的见解，帮助团队优先考虑更容易出现问题的领域的测试工作。

  ```
  // Example of an AI-powered function to update selectors
  async function updateSelector(oldSelector, newHint) {
    // AI logic to find the new selector based on the provided hint
    const newSelector = AI.findNewSelector(oldSelector, newHint);
    return newSelector;
  }
  ```通过整合人工智能，[test automation](../T/test-automation.md) 变得更加**高效**和**有效**，显着减少测试所需的时间和资源，同时提高 Web 应用程序的质量和可靠性。
