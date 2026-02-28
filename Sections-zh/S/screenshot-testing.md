# 截图测试

<!-- TOC START -->
- [有关屏幕截图测试的问题吗？](#有关屏幕截图测试的问题吗？)
  - [基础知识和重要性](#基础知识和重要性)
    - [什么是屏幕截图测试？](#什么是屏幕截图测试？)
    - [为什么屏幕截图测试在软件自动化中很重要？](#为什么屏幕截图测试在软件自动化中很重要？)
    - [屏幕截图测试的主要优点是什么？](#屏幕截图测试的主要优点是什么？)
    - [屏幕截图测试如何提高软件产品的质量？](#屏幕截图测试如何提高软件产品的质量？)
    - [屏幕截图测试有哪些限制？](#屏幕截图测试有哪些限制？)
  - [工具和技术](#工具和技术)
    - [截图测试常用哪些工具？](#截图测试常用哪些工具？)
    - [如何选择合适的截图测试工具？](#如何选择合适的截图测试工具？)
    - [屏幕截图测试工具需要寻找哪些关键功能？](#屏幕截图测试工具需要寻找哪些关键功能？)
    - [屏幕截图测试中使用哪些技术来比较屏幕截图？](#屏幕截图测试中使用哪些技术来比较屏幕截图？)
    - [截图测试中如何处理动态内容？](#截图测试中如何处理动态内容？)
  - [实施和最佳实践](#实施和最佳实践)
    - [屏幕截图测试的最佳实践是什么？](#屏幕截图测试的最佳实践是什么？)
    - [如何管理和组织测试截图？](#如何管理和组织测试截图？)
    - [如何处理截图测试中的误报？](#如何处理截图测试中的误报？)
    - [可以使用哪些策略来自动化屏幕截图测试？](#可以使用哪些策略来自动化屏幕截图测试？)
  - [高级主题](#高级主题)
    - [屏幕截图测试在持续集成/持续部署 (CI/CD) 环境中如何工作？](#屏幕截图测试在持续集成持续部署-cicd-环境中如何工作？)
    - [如何对响应式网页设计进行截图测试？](#如何对响应式网页设计进行截图测试？)
    - [如何处理跨浏览器截图测试？](#如何处理跨浏览器截图测试？)
    - [人工智能 (AI) 在屏幕截图测试中的作用是什么？](#人工智能-ai-在屏幕截图测试中的作用是什么？)
    - [如何对移动应用进行截图测试？](#如何对移动应用进行截图测试？)
<!-- TOC END -->

截图测试

通过将当前视觉效果与基线图像进行比较，识别视觉回归和其他差异，自动评估网页或应用程序的视觉元素。

## 有关屏幕截图测试的问题吗？

### 基础知识和重要性

#### 什么是屏幕截图测试？

[Screenshot testing](../S/screenshot-testing.md) 是一种可视化[verification](../V/verification.md) 方法，其中捕获软件应用程序的用户界面 (UI) 并将其与基线图像进行比较以检测变化或异常。它涉及在应用程序流程的各个阶段对网页、移动应用程序或任何图形用户界面进行屏幕截图，以确保视觉一致性和功能。
  要执行[screenshot testing](../S/screenshot-testing.md)，请按照以下步骤操作：

1. **捕获基线图像**：截取代表应用程序预期状态的 UI 元素或页面的屏幕截图。
  2. **运行测试**：执行与应用程序交互的自动化测试，在拍摄基线图像的同一点捕获屏幕截图。
  3. **比较屏幕截图**：使用图像比较工具或算法来检测基线和新屏幕截图之间的差异。
  4. **分析结果**：检查差异以确定它们是否是有意更改或视觉缺陷。

  ```
  // Example of capturing a screenshot using a test automation tool
  await page.goto('https://example.com');
  await page.screenshot({path: 'example-page.png'});
  ```选择[screenshot testing](../S/screenshot-testing.md) 工具时，请考虑**自动基线管理**、**与 CI/CD 管道集成**以及**支持多种环境和设备**等功能。工具还应该提供一种**忽略动态内容**的方法，并具有**减少[false positives](../F/false-positive.md)**的机制。
  对于动态内容，可以使用**屏蔽**、**等待元素稳定**或**用静态占位符替换动态数据**等策略来确保一致性。
  将 [screenshot testing](../S/screenshot-testing.md) 合并到您的自动化套件中，以捕获仅通过功能测试可能无法检测到的视觉回归，确保跨不同平台和设备的高质量用户体验。

1. **捕获基线图像**：截取代表应用程序预期状态的 UI 元素或页面的屏幕截图。
  2. **运行测试**：执行与应用程序交互的自动化测试，在拍摄基线图像的同一点捕获屏幕截图。
  3. **比较屏幕截图**：使用图像比较工具或算法来检测基线和新屏幕截图之间的差异。
  4. **分析结果**：检查差异以确定它们是否是有意更改或视觉缺陷。

#### 为什么屏幕截图测试在软件自动化中很重要？

[Screenshot testing](../S/screenshot-testing.md) 在软件[test automation](../T/test-automation.md) 中对于**视觉验证**至关重要。它确保 UI 向用户正确显示，捕捉传统功能测试可能错过的**视觉回归**。通过将当前屏幕截图与基线图像进行比较，测试人员可以检测应用程序布局和样式中的意外更改或异常。
  此方法在以下情况下尤其重要：

- **重构**
    或更新 UI，其中代码的更改可能会对视觉呈现产生副作用。

- **验证第三方集成**
    或应用程序代码库可能无法一致控制的内容。

- **在多个设备上测试**
    和屏幕分辨率，以确保跨平台一致的用户体验。
  要有效集成 [screenshot testing](../S/screenshot-testing.md)，请考虑以下事项：

- **自动化捕获和比较过程**
    简化工作流程并减少手动工作量。

- **与您的 CI/CD 管道集成**
    对变化进行持续的视觉反馈。

- **使用智能图像比较工具**
    可以忽略动态内容或动画引起的差异。

- **组织和管理屏幕截图**
    有效地快速访问和审查它们以进行任何必要的调整。
  通过合并 [screenshot testing](../S/screenshot-testing.md)，您可以及早发现视觉问题，维护精美的 UI，并向最终用户提供视觉上一致的高质量产品。

- **重构**
    或更新 UI，其中代码的更改可能会对视觉呈现产生副作用。

- **验证第三方集成**
    或应用程序代码库可能无法一致控制的内容。

- **在多个设备上测试**
    和屏幕分辨率，以确保跨平台一致的用户体验。

- **自动化捕获和比较过程**
    简化工作流程并减少手动工作量。

- **与您的 CI/CD 管道集成**
    对变化进行持续的视觉反馈。

- **使用智能图像比较工具**
    可以忽略动态内容或动画引起的差异。

- **组织和管理屏幕截图**
    有效地快速访问和审查它们以进行任何必要的调整。

#### 屏幕截图测试的主要优点是什么？

[screenshot testing](../S/screenshot-testing.md) 的主要优点包括：

- **视觉回归检测**：快速识别软件版本之间意外的视觉变化。
  - **跨环境的一致性**：确保不同浏览器、设备和屏幕分辨率之间的 UI 一致性。
  - **全面覆盖**：捕获整个页面或特定组件，提供广泛的测试覆盖范围。
  - **历史参考**：维护变化的视觉历史，帮助跟踪和理解 UI 演变。
  - **易于理解**：视觉差异通常比基于代码的错误更直观地识别和传达。
  - **自动验证**：与自动化框架集成，无需手动干预即可验证视觉方面。
  - **时间效率**：减少手动目视检查所花费的时间，特别是对于大规模应用。
  - **改进协作**：可以与利益相关者共享屏幕截图以获取反馈，从而增强协作。
  - **文档**：作为设计和功能文档的一种形式，对于入门和参考很有用。
  实施[screenshot testing](../S/screenshot-testing.md)以获得这些好处，增强[UI testing](../U/ui-testing.md)在您的软件自动化工作中的稳健性和可靠性。

- **视觉回归检测**：快速识别软件版本之间意外的视觉变化。
  - **跨环境的一致性**：确保不同浏览器、设备和屏幕分辨率之间的 UI 一致性。
  - **全面覆盖**：捕获整个页面或特定组件，提供广泛的测试覆盖范围。
  - **历史参考**：维护变化的视觉历史，帮助跟踪和理解 UI 演变。
  - **易于理解**：视觉差异通常比基于代码的错误更直观地识别和传达。
  - **自动验证**：与自动化框架集成，无需手动干预即可验证视觉方面。
  - **时间效率**：减少手动目视检查所花费的时间，特别是对于大规模应用。
  - **改进协作**：可以与利益相关者共享屏幕截图以获取反馈，从而增强协作。
  - **文档**：作为设计和功能文档的一种形式，对于入门和参考很有用。

#### 屏幕截图测试如何提高软件产品的质量？

[Screenshot testing](../S/screenshot-testing.md) 通过在传统[test automation](../T/test-automation.md) 之上提供**可视化[verification](../V/verification.md) 层**来增强[software quality](../S/software-quality.md)。它确保 UI 按最终用户的预期显示，捕获其他自动化测试可能无法检测到的 **样式问题**、**布局问题** 和 **视觉回归**。
  通过将基线图像与当前屏幕截图进行比较，测试人员可以识别 UI 中的意外更改或异常。这对于保持一致的用户体验至关重要，特别是当代码更改频繁时。 [Screenshot testing](../S/screenshot-testing.md) 还有助于验证跨不同浏览器和设备的**像素完美渲染**，这对于**跨平台兼容性**至关重要。
  此外，它还支持**[accessibility testing](../A/accessibility-testing.md)**，允许测试人员根据可访问性标准检查颜色对比度和字体大小等视觉元素。这对于创建可供残疾人使用的包容性软件尤其重要。
  将 [screenshot testing](../S/screenshot-testing.md) 合并到 **CI/CD 管道** 有助于在开发周期的早期发现视觉问题，从而减少以后修复这些问题所需的成本和工作量。它还提供视觉变化的**记录历史**，这对于跟踪和审核目的非常有用。
  通过自动化视觉[verification](../V/verification.md)过程，[screenshot testing](../S/screenshot-testing.md)使人类测试人员能够专注于更复杂的测试场景，从而提高整体[test coverage](../T/test-coverage.md)和产品质量。

#### 屏幕截图测试有哪些限制？

[Screenshot testing](../S/screenshot-testing.md) 虽然很有价值，但有几个限制：

- **对 UI 更改敏感**：对 UI 进行微小且通常不相关的更改可能会导致测试失败，需要手动审核以区分误报和真正问题。
  - **环境依赖性**：测试可能会因环境差异（例如屏幕分辨率、字体渲染和颜色配置文件）而失败，这可能并不表明实际的功能问题。
  - **性能**：屏幕截图测试可能会很慢，因为它们通常需要在捕获屏幕截图之前加载和渲染整个页面，从而导致测试执行时间更长。
  - **资源密集型**：存储、管理和比较屏幕截图会消耗大量磁盘空间和处理能力，特别是对于大型测试套件。
  - **范围有限**：屏幕截图测试仅捕获视觉状态，而不是应用程序的功能或交互行为。
  - **动态内容**：处理动态内容（例如广告、动画或日期和时间值）可能具有挑战性，因为它们可能在测试运行之间发生变化，从而导致漏报。
  - **本地化和国际化**：测试不同的语言和格式可能很麻烦，因为每种变体可能需要自己的一组屏幕截图。
  - **辅助功能**：屏幕截图测试不涵盖辅助功能问题；他们无法确保该应用程序可供残疾人使用。
  为了减轻这些限制，重要的是用其他类型的测试（例如单元测试、集成测试和功能测试）来补充[screenshot testing](../S/screenshot-testing.md)，以确保全面的覆盖范围。

- **对 UI 更改敏感**：对 UI 进行微小且通常不相关的更改可能会导致测试失败，需要手动审核以区分误报和真正问题。
  - **环境依赖性**：测试可能会因环境差异（例如屏幕分辨率、字体渲染和颜色配置文件）而失败，这可能并不表明实际的功能问题。
  - **性能**：屏幕截图测试可能会很慢，因为它们通常需要在捕获屏幕截图之前加载和渲染整个页面，从而导致测试执行时间更长。
  - **资源密集型**：存储、管理和比较屏幕截图会消耗大量磁盘空间和处理能力，特别是对于大型测试套件。
  - **范围有限**：屏幕截图测试仅捕获视觉状态，而不是应用程序的功能或交互行为。
  - **动态内容**：处理动态内容（例如广告、动画或日期和时间值）可能具有挑战性，因为它们可能在测试运行之间发生变化，从而导致漏报。
  - **本地化和国际化**：测试不同的语言和格式可能很麻烦，因为每种变体可能需要自己的一组屏幕截图。
  - **辅助功能**：屏幕截图测试不涵盖辅助功能问题；他们无法确保该应用程序可供残疾人使用。

### 工具和技术

#### 截图测试常用哪些工具？

[screenshot testing](../S/screenshot-testing.md) 的常用工具包括：

- **[Selenium](../S/selenium.md) [WebDriver](../W/webdriver.md)**：与各种编程语言和框架集成，允许自动浏览器控制和屏幕截图捕获。

    ```
    TakesScreenshot ts = (TakesScreenshot)driver;
    File source = ts.getScreenshotAs(OutputType.FILE);
    ```

- **Puppeteer**：一个节点库，提供高级 [API](../A/api.md) 通过 DevTools 协议控制 Chrome 或 Chromium，非常适合 [automated testing](../A/automated-testing.md)。

    ```
    await page.screenshot({path: 'screenshot.png'});
    ```

- **[Cypress](../C/cypress.md)**：一个[end-to-end testing](../E/end-to-end-testing.md) 框架，包括[visual regression testing](../V/visual-regression-testing.md) 的屏幕截图功能。

    ```
    cy.screenshot();
    ```

- **Applitools Eyes**：对 [screenshot testing](../S/screenshot-testing.md) 使用人工智能驱动的视觉比较，提供与多个测试框架集成的 SDK。
  - **Percy**：与 CI/CD 管道集成的可视化测试平台，捕获屏幕截图并突出显示视觉变化。
  - **Playwright**：一个 Node 库，可通过单个 [API](../A/api.md) 实现 Chromium、Firefox 和 WebKit 的自动化，支持跨浏览器的 [screenshot testing](../S/screenshot-testing.md)。

    ```
    await page.screenshot({ path: `screenshot.png` });
    ```

- **Storybook**：主要用于组件测试，它可以与 Chromatic 等视觉回归工具配合使用来捕获和测试 UI 组件。
  - **TestCafe**：一个[Node.js](../N/node-js.md) 工具，用于自动化端到端[web testing](../W/web-testing.md)，包括用于视觉测试的屏幕截图。

    ```
    await t.takeScreenshot();
    ```这些工具可以与断言库和图像比较工具以各种方式组合使用，以创建强大的[screenshot testing](../S/screenshot-testing.md)工作流程。

- **[Selenium](../S/selenium.md) [WebDriver](../W/webdriver.md)**：与各种编程语言和框架集成，允许自动浏览器控制和屏幕截图捕获。

    ```
    TakesScreenshot ts = (TakesScreenshot)driver;
    File source = ts.getScreenshotAs(OutputType.FILE);
    ```

- **Puppeteer**：一个节点库，提供高级 [API](../A/api.md) 通过 DevTools 协议控制 Chrome 或 Chromium，非常适合 [automated testing](../A/automated-testing.md)。

    ```
    await page.screenshot({path: 'screenshot.png'});
    ```

- **[Cypress](../C/cypress.md)**：一个[end-to-end testing](../E/end-to-end-testing.md) 框架，包括[visual regression testing](../V/visual-regression-testing.md) 的屏幕截图功能。

    ```
    cy.screenshot();
    ```

- **Applitools Eyes**：对 [screenshot testing](../S/screenshot-testing.md) 使用人工智能驱动的视觉比较，提供与多个测试框架集成的 SDK。
  - **Percy**：与 CI/CD 管道集成的可视化测试平台，捕获屏幕截图并突出显示视觉变化。
  - **Playwright**：一个 Node 库，可通过单个 [API](../A/api.md) 实现 Chromium、Firefox 和 WebKit 的自动化，支持跨浏览器的 [screenshot testing](../S/screenshot-testing.md)。

    ```
    await page.screenshot({ path: `screenshot.png` });
    ```

- **Storybook**：主要用于组件测试，它可以与 Chromatic 等视觉回归工具配合使用来捕获和测试 UI 组件。
  - **TestCafe**：一个[Node.js](../N/node-js.md) 工具，用于自动化端到端[web testing](../W/web-testing.md)，包括用于视觉测试的屏幕截图。

    ```
    await t.takeScreenshot();
    ```

#### 如何选择合适的截图测试工具？

为[screenshot testing](../S/screenshot-testing.md) 选择正确的工具涉及根据可用工具的功能评估您的特定需求。考虑以下标准：

- **与现有测试框架集成**：确保该工具可以轻松集成到您当前的测试套件中，无论是 Selenium、Cypress 还是其他框架。
  - **平台支持**：验证该工具是否支持您需要测试的所有平台和浏览器，包括移动和桌面环境。
  - **并行测试功能**：寻找提供并行测试的工具，通过同时运行多个测试来加快流程。
  - **版本控制**：选择为屏幕截图提供版本控制的工具，以跟踪随时间的变化和回归。
  - **自定义和灵活性**：该工具应允许自定义比较阈值和区域以忽略动态内容。
  - **报告和分析**：一个好的工具应该提供全面的报告功能，以帮助您快速分析测试结果。
  - **易于使用**：该工具应具有用户友好的界面和清晰的文档，以最大限度地减少学习曲线。
  - **社区和支持**：考虑围绕该工具的社区以及提供商提供的支持，这对于故障排除和改进至关重要。
  - **成本**：评估该工具的定价模型，并确保它符合您的预算，同时满足您的要求。
  考虑这些因素后，建议尝试一系列工具，看看它们在您的特定 [use cases](../U/use-case.md) 上的表现如何。这种实践方法将帮助您做出明智的决定。

- **与现有测试框架集成**：确保该工具可以轻松集成到您当前的测试套件中，无论是 Selenium、Cypress 还是其他框架。
  - **平台支持**：验证该工具是否支持您需要测试的所有平台和浏览器，包括移动和桌面环境。
  - **并行测试功能**：寻找提供并行测试的工具，通过同时运行多个测试来加快流程。
  - **版本控制**：选择为屏幕截图提供版本控制的工具，以跟踪随时间的变化和回归。
  - **自定义和灵活性**：该工具应允许自定义比较阈值和区域以忽略动态内容。
  - **报告和分析**：一个好的工具应该提供全面的报告功能，以帮助您快速分析测试结果。
  - **易于使用**：该工具应具有用户友好的界面和清晰的文档，以最大限度地减少学习曲线。
  - **社区和支持**：考虑围绕该工具的社区以及提供商提供的支持，这对于故障排除和改进至关重要。
  - **成本**：评估该工具的定价模型，并确保它符合您的预算，同时满足您的要求。

#### 屏幕截图测试工具需要寻找哪些关键功能？

评估 **[screenshot testing](../S/screenshot-testing.md) 工具**时，请考虑以下主要功能：

- **高分辨率图像捕获**：确保详细清晰的屏幕截图以进行准确比较。
  - **多视口支持**：捕获各种屏幕尺寸和分辨率的屏幕截图以进行响应测试。
  - **自动基线管理**：能够设置和更新基线图像以轻松进行比较。
  - **逐像素比较**：检测图像之间最小的视觉差异。
  - **区域排除**：忽略动态区域或已知差异以减少误报。
  - **注释和标记工具**：允许用户直接在屏幕截图上突出显示问题。
  - **集成功能**：与流行的测试框架和 CI/CD 管道无缝集成。
  - **并行执行**：支持并发屏幕截图以加快测试过程。
  - **云存储**：为屏幕截图提供安全且可扩展的存储。
  - **版本控制**：跟踪屏幕截图随时间的变化以进行历史比较。
  - **报告和通知**：提供有关测试结果的详细报告和警报。
  - **用户权限和访问控制**：管理团队协作的用户角色。
  - **可自定义阈值**：设置图像比较的敏感度级别以适应项目需求。
  - **[API](../A/api.md) 访问**：通过记录齐全的 API 促进自动化以及与其他工具的集成。
  这些功能共同提高了[automated testing](../A/automated-testing.md) 环境中[screenshot testing](../S/screenshot-testing.md) 的效率、准确性和协作性。

- **高分辨率图像捕获**：确保详细清晰的屏幕截图以进行准确比较。
  - **多视口支持**：捕获各种屏幕尺寸和分辨率的屏幕截图以进行响应测试。
  - **自动基线管理**：能够设置和更新基线图像以轻松进行比较。
  - **逐像素比较**：检测图像之间最小的视觉差异。
  - **区域排除**：忽略动态区域或已知差异以减少误报。
  - **注释和标记工具**：允许用户直接在屏幕截图上突出显示问题。
  - **集成功能**：与流行的测试框架和 CI/CD 管道无缝集成。
  - **并行执行**：支持并发屏幕截图以加快测试过程。
  - **云存储**：为屏幕截图提供安全且可扩展的存储。
  - **版本控制**：跟踪屏幕截图随时间的变化以进行历史比较。
  - **报告和通知**：提供有关测试结果的详细报告和警报。
  - **用户权限和访问控制**：管理团队协作的用户角色。
  - **可自定义阈值**：设置图像比较的敏感度级别以适应项目需求。
  - **[API](../A/api.md) 访问**：通过记录齐全的 API 促进自动化以及与其他工具的集成。

#### 屏幕截图测试中使用哪些技术来比较屏幕截图？

在[screenshot testing](../S/screenshot-testing.md) 中，比较屏幕截图涉及多种技术来检测基线图像和当前图像之间的差异。以下是一些常用的方法：
  **逐像素比较**：此方法涉及比较两个图像的每个对应像素。如果像素颜色值不匹配，则会将其标记为差异。这种方法很简单，但可能对抗锯齿或颜色变化等微小变化过于敏感。

  ```
  compareImages(baselineImage, currentImage) {
    // Loop through each pixel and compare values
  }
  ```**感知哈希 (pHash)**：该技术根据图像的视觉内容将图像转换为哈希值，从而可以比较这些哈希以确定相似性。它对微小变化不太敏感，更关注感知变化。

  ```
  calculateImageHash(image) {
    // Generate a hash based on image content
  }
  ```**结构相似度指数（SSIM）**：SSIM是一种测量两幅图像之间相似度的方法。它考虑纹理、亮度和对比度的变化，提供更人性化的图像差异评估。

  ```
  calculateSSIM(image1, image2) {
    // Calculate similarity index
  }
  ```**基于特征的比较**：这涉及检测图像中的关键特征并比较它们的相对位置和特征。它对于布局保持一致但内容可能发生变化的动态内容很有用。

  ```
  compareImageFeatures(baselineFeatures, currentFeatures) {
    // Match and compare features
  }
  ```**阈值**：为了减少比较中的噪音，可以设置阈值，以便仅报告超过特定水平的差异。这有助于忽略细微的差异。

  ```
  applyThreshold(differenceValue) {
    // Ignore differences below a certain threshold
  }
  ```这些技术可以单独使用或组合使用，以在[screenshot testing](../S/screenshot-testing.md)期间检测有意义的差异时实现灵敏度和特异性之间的平衡。

#### 截图测试中如何处理动态内容？

处理 [screenshot testing](../S/screenshot-testing.md) 中的动态内容需要策略来确保一致性，尽管每次测试运行都会发生变化。以下是一些方法：

- **排除动态区域**：修改屏幕截图测试工具以忽略屏幕的动态区域。这可以通过设置掩码或指定代表动态区域的选择器来完成。

  ```
  excludeSelectors: ['.dynamic-content']
  ```

- **使用稳定的[Test Data](../T/test-data.md)**：将[test environment](../T/test-environment.md) 配置为使用产生可预测输出的静态数据集，从而最大限度地减少 UI 中的更改。
  - **动态内容存根**：在测试期间用静态占位符替换动态内容以确保一致性。
  - **视觉回归阈值**：设置变化的容忍级别，允许动态内容发生微小变化而不会导致测试失败。

  ```
  compareThreshold: 0.01
  ```

- **快照平均**：拍摄多个快照并对它们进行平均，以减轻随机动态内容的影响。
  - **DOM 操作**：在进行屏幕截图之前，操作 DOM 以删除或标准化动态内容。

  ```
  document.querySelector('.timestamp').innerText = '00:00:00';
  ```

- **元素隐藏**：隐藏在测试运行之间容易更改的元素。

  ```
  document.querySelector('.live-feed').style.display = 'none';
  ```

- **智能图像比较**：使用提供人工智能图像比较的工具来区分有意义的变化和动态内容噪音。
  通过结合这些技术，您可以有效地管理[screenshot testing](../S/screenshot-testing.md)中的动态内容，确保测试可靠且有意义。

- **排除动态区域**：修改屏幕截图测试工具以忽略屏幕的动态区域。这可以通过设置掩码或指定代表动态区域的选择器来完成。
  - **使用稳定的[Test Data](../T/test-data.md)**：将[test environment](../T/test-environment.md) 配置为使用产生可预测输出的静态数据集，从而最大限度地减少 UI 中的更改。
  - **动态内容存根**：在测试期间用静态占位符替换动态内容以确保一致性。
  - **视觉回归阈值**：设置变化的容忍级别，允许动态内容发生微小变化而不会导致测试失败。
  - **快照平均**：拍摄多个快照并对它们进行平均，以减轻随机动态内容的影响。
  - **DOM 操作**：在进行屏幕截图之前，操作 DOM 以删除或标准化动态内容。
  - **元素隐藏**：隐藏在测试运行之间容易更改的元素。
  - **智能图像比较**：使用提供人工智能图像比较的工具来区分有意义的变化和动态内容噪音。

### 实施和最佳实践

#### 如何在软件自动化项目中实现截图测试？

要在软件自动化项目中实施[screenshot testing](../S/screenshot-testing.md)，请执行以下步骤：

1. **选择与您现有的测试框架集成并支持您的应用程序平台和浏览器的 [screenshot testing](../S/screenshot-testing.md) 工具**。
  2. **设置环境**以保持一致性。确保测试在相同的屏幕分辨率、浏览器大小和相同的设置上运行，以最大限度地减少差异。
  3. **写入 [test cases](../T/test-case.md)** 以导航到所需的应用程序状态。使用您的[test automation](../T/test-automation.md) 框架与应用程序交互。
  4. 使用该工具的[API](../A/api.md) 在[test cases](../T/test-case.md) 中的关键点**捕获屏幕截图**。例如，在基于 [Selenium](../S/selenium.md) 的项目中，您可以使用：

    ```
    File screenshot = ((TakesScreenshot)driver).getScreenshotAs(OutputType.FILE);
    FileUtils.copyFile(screenshot, new File("path/to/screenshot.png"));
    ```

5. **存储代表应用程序预期状态的基线图像**。将它们保存在版本控制的存储库中或使用 [screenshot testing](../S/screenshot-testing.md) 工具提供的存储。
  6. **使用工具的比较引擎将捕获的屏幕截图**与基线图像进行比较。处理可接受范围内的差异以避免[false positives](../F/false-positive.md)。
  7. **当有意对 UI 进行更改时，根据需要查看和更新​​基线**。
  8. **与 CI/CD 管道集成**以自动触发新构建或部署的屏幕截图测试。
  9. **分析测试结果**并调查任何差异。更新测试和基线图像以适应有意的更改并修复任何发现的问题。
  10. **记录您的流程**并保持清晰的屏幕截图命名约定，以简化协作和维护。
  1. **选择一个 [screenshot testing](../S/screenshot-testing.md) 工具**，它与您现有的测试框架集成并支持您的应用程序的平台和浏览器。
  2. **设置环境**以保持一致性。确保测试在相同的屏幕分辨率、浏览器大小和相同的设置上运行，以最大限度地减少差异。
  3. **写入 [test cases](../T/test-case.md)** 以导航到所需的应用程序状态。使用您的[test automation](../T/test-automation.md) 框架与应用程序交互。
  4. 使用该工具的[API](../A/api.md) 在[test cases](../T/test-case.md) 中的关键点**捕获屏幕截图**。例如，在基于 [Selenium](../S/selenium.md) 的项目中，您可以使用：

    ```
    File screenshot = ((TakesScreenshot)driver).getScreenshotAs(OutputType.FILE);
    FileUtils.copyFile(screenshot, new File("path/to/screenshot.png"));
    ```

5. **存储代表应用程序预期状态的基线图像**。将它们保存在版本控制的存储库中或使用 [screenshot testing](../S/screenshot-testing.md) 工具提供的存储。
  6. **使用工具的比较引擎将捕获的屏幕截图**与基线图像进行比较。处理可接受范围内的差异以避免[false positives](../F/false-positive.md)。
  7. **当有意对 UI 进行更改时，根据需要查看和更新​​基线**。
  8. **与 CI/CD 管道集成**以自动触发新构建或部署的屏幕截图测试。
  9. **分析测试结果**并调查任何差异。更新测试和基线图像以适应有意的更改并修复任何发现的问题。
  10. **记录您的流程**并保持清晰的屏幕截图命名约定，以简化协作和维护。

#### 屏幕截图测试的最佳实践是什么？

[screenshot testing](../S/screenshot-testing.md) 的最佳实践包括：

- **基线管理**：建立一组可靠的基线图像。当发生有意的更改时，明智地更新基线。
  - **选择性测试**：专注于应用程序中视觉变化至关重要的关键区域，而不是捕获整个 UI。
  - **阈值配置**：为图像比较设置适当的阈值，以最大限度地减少由于微小的、不显着的变化而导致的误报。
  - **环境一致性**：确保测试在一致的环境中运行（相同的浏览器版本、屏幕分辨率等）以避免出现差异。
  - **测试隔离**：独立运行屏幕截图测试，以避免从一个测试到另一个测试的级联失败。
  - **使用模拟数据**：利用稳定且可预测的数据来确保屏幕截图在测试运行中具有可比性。
  - **处理动态内容**：屏蔽或删除可能导致不必要的测试失败的动态内容，例如广告或时间戳。
  - **版本控制集成**：将屏幕截图存储在版本控制系统中以跟踪更改并促进协作。
  - **自动清理**：实施一个流程来删除过时的屏幕截图，以保持测试套件最新且易于管理。
  - **文档**：记录每个屏幕截图测试的目的和范围，以实现更好的可维护性。
  - **辅助功能检查**：将辅助功能测试与屏幕截图结合起来，以确保视觉元素符合辅助功能标准。
  - **性能注意事项**：注意对测试套件执行时间的影响并进行优化，以避免减慢 CI/CD 管道的速度。
  - **定期审查**：定期审查屏幕截图测试以消除冗余并确保它们符合当前的 UI 和 UX 期望。
  通过遵循这些做法，您可以在 [test automation](../T/test-automation.md) 策略中最大限度地发挥 [screenshot testing](../S/screenshot-testing.md) 的有效性。

- **基线管理**：建立一组可靠的基线图像。当发生有意的更改时，明智地更新基线。
  - **选择性测试**：专注于应用程序中视觉变化至关重要的关键区域，而不是捕获整个 UI。
  - **阈值配置**：为图像比较设置适当的阈值，以最大限度地减少由于微小的、不显着的变化而导致的误报。
  - **环境一致性**：确保测试在一致的环境中运行（相同的浏览器版本、屏幕分辨率等）以避免出现差异。
  - **测试隔离**：独立运行屏幕截图测试，以避免从一个测试到另一个测试的级联失败。
  - **使用模拟数据**：利用稳定且可预测的数据来确保屏幕截图在测试运行中具有可比性。
  - **处理动态内容**：屏蔽或删除可能导致不必要的测试失败的动态内容，例如广告或时间戳。
  - **版本控制集成**：将屏幕截图存储在版本控制系统中以跟踪更改并促进协作。
  - **自动清理**：实施一个流程来删除过时的屏幕截图，以保持测试套件最新且易于管理。
  - **文档**：记录每个屏幕截图测试的目的和范围，以实现更好的可维护性。
  - **辅助功能检查**：将辅助功能测试与屏幕截图结合起来，以确保视觉元素符合辅助功能标准。
  - **性能注意事项**：注意对测试套件执行时间的影响并进行优化，以避免减慢 CI/CD 管道的速度。
  - **定期审查**：定期审查屏幕截图测试以消除冗余并确保它们符合当前的 UI 和 UX 期望。

#### 如何管理和组织测试截图？

有效管理和组织屏幕截图对于保持 [test automation](../T/test-automation.md) 套件的效率至关重要。以下是一些提示：

- **命名约定**：对屏幕截图使用清晰一致的命名。包括 [test case](../T/test-case.md) ID、日期和屏幕截图用途的简要说明。例如，`TC101_20230315_LoginPage.png`。
  - **目录结构**：以分层文件夹结构组织屏幕截图。按功能、测试运行或日期对它们进行分组。这使得在需要时更容易找到特定的屏幕截图。
  - **版本控制**：将屏幕截图与测试代码一起存储在版本控制系统 (VCS) 中。这允许您跟踪更改并在必要时恢复到以前的版本。
  - **清理策略**：实施保留策略以删除不再相关的旧屏幕截图，以节省存储空间。
  - **云存储**：考虑使用云存储解决方案来轻松共享和备份。确保访问受到控制且安全。
  - **元数据**：将元数据附加到屏幕截图，例如 [test case](../T/test-case.md) 名称、执行时间和结果状态。这对于过滤和搜索很有用。
  - **自动标记**：使用脚本根据[test scenario](../T/test-scenario.md)使用相关关键字来标记屏幕截图。
  - **审核流程**：在工作流程中纳入审核步骤，以评估每个屏幕截图的必要性和相关性。
  - **与[Test Reports](../T/test-report.md)**集成：将屏幕截图嵌入自动[test reports](../T/test-report.md)中以直观地表示测试失败。
  - **工具**：利用提供屏幕截图管理功能的工具，例如自动组织、比较和云集成。
  通过遵循这些实践，您可以维护一个组织良好的屏幕截图存储库，以支持您的测试工作并改进[test automation](../T/test-automation.md)套件的[maintainability](../M/maintainability.md)。

- **命名约定**：对屏幕截图使用清晰一致的命名。包括 [test case](../T/test-case.md) ID、日期和屏幕截图用途的简短说明。例如，`TC101_20230315_LoginPage.png`。
  - **目录结构**：以分层文件夹结构组织屏幕截图。按功能、测试运行或日期对它们进行分组。这使得在需要时更容易找到特定的屏幕截图。
  - **版本控制**：将屏幕截图与测试代码一起存储在版本控制系统 (VCS) 中。这允许您跟踪更改并在必要时恢复到以前的版本。
  - **清理策略**：实施保留策略以删除不再相关的旧屏幕截图，以节省存储空间。
  - **云存储**：考虑使用云存储解决方案来轻松共享和备份。确保访问受到控制且安全。
  - **元数据**：将元数据附加到屏幕截图，例如 [test case](../T/test-case.md) 名称、执行时间和结果状态。这对于过滤和搜索很有用。
  - **自动标记**：使用脚本根据[test scenario](../T/test-scenario.md)使用相关关键字来标记屏幕截图。
  - **审核流程**：在工作流程中纳入审核步骤，以评估每个屏幕截图的必要性和相关性。
  - **与[Test Reports](../T/test-report.md)**集成：将屏幕截图嵌入自动[test reports](../T/test-report.md)中以直观地表示测试失败。
  - **工具**：利用提供屏幕截图管理功能的工具，例如自动组织、比较和云集成。

#### 如何处理截图测试中的误报？

在[screenshot testing](../S/screenshot-testing.md) 中处理[false positives](../F/false-positive.md) 需要结合战略规划和工具配置。以下是缓解[false positives](../F/false-positive.md)的一些步骤：

1. **基线管理**：建立一组可靠的基线图像。仅在有意更改时才更新基线，并定期进行审查。
  2. **选择性区域**：重点关注 UI 中不易发生动态变化的关键区域。使用允许您排除或屏蔽动态内容的工具。
  3. **阈值配置**：调整图像比较工具的灵敏度。设置忽略微小的、不显着的变化的容差水平。
  4. **忽略瞬态元素**：排除广告、弹出窗口等元素或任何经常更改且不影响功能的内容。
  5. **[Test Environment](../T/test-environment.md) 稳定性**：确保稳定的[test environment](../T/test-environment.md)，其中屏幕分辨率和浏览器版本等外部因素保持一致。
  6. **定期维护**：当UI发生变化时及时更新测试和基线，以防止过时的引用。
  7. **人工审核**：纳入人工审核流程，以确认发现的差异是真正的问题还是[false positives](../F/false-positive.md)。
  8. **自动批准**：实施自动化流程来批准不影响应用程序质量的已知差异。
  9. **版本控制集成**：使用版本控制系统跟踪屏幕截图中的更改并有效管理基线。
  10. **视觉降噪**：通过标准化字体和颜色等 UI 元素以及在测试期间避免动画来最小化视觉噪音。
  通过应用这些策略，您可以显着减少 [screenshot testing](../S/screenshot-testing.md) 中 [false positives](../F/false-positive.md) 的出现，使您的自动化工作更加可靠和高效。

1. **基线管理**：建立一组可靠的基线图像。仅在有意更改时才更新基线，并定期进行审查。
  2. **选择性区域**：重点关注 UI 中不易发生动态变化的关键区域。使用允许您排除或屏蔽动态内容的工具。
  3. **阈值配置**：调整图像比较工具的灵敏度。设置忽略微小的、不显着的变化的容差水平。
  4. **忽略瞬态元素**：排除广告、弹出窗口等元素或任何经常更改且不影响功能的内容。
  5. **[Test Environment](../T/test-environment.md) 稳定性**：确保稳定的[test environment](../T/test-environment.md)，其中屏幕分辨率和浏览器版本等外部因素保持一致。
  6. **定期维护**：当UI发生变化时及时更新测试和基线，以防止过时的引用。
  7. **人工审核**：纳入人工审核流程，以确认发现的差异是真正的问题还是[false positives](../F/false-positive.md)。
  8. **自动批准**：实施自动化流程来批准不影响应用程序质量的已知差异。
  9. **版本控制集成**：使用版本控制系统跟踪屏幕截图中的更改并有效管理基线。
  10. **视觉降噪**：通过标准化字体和颜色等 UI 元素以及在测试期间避免动画来最小化视觉噪音。

#### 可以使用哪些策略来自动化屏幕截图测试？

要有效地自动化[screenshot testing](../S/screenshot-testing.md)，请考虑以下策略：

- **基线图像创建**：建立一组基线图像，将来的屏幕截图将与这些图像进行比较。确保这些图像是在受控条件下捕获的，以尽量减少变化。
  - **自动捕获**：使用[Selenium](../S/selenium.md)、Puppeteer 或[Cypress](../C/cypress.md) 等工具将屏幕截图集成到您的[test scripts](../T/test-script.md) 中。在测试流程中的特定点触发捕获。

    ```
    // Example using Puppeteer
    await page.screenshot({ path: 'example.png' });
    ```

- **[Visual Regression Testing](../V/visual-regression-testing.md)**：实施视觉回归工具，例如 BackstopJS、Percy 或 Applitools。这些工具将新的屏幕截图与基线图像进行比较以检测变化。
  - **阈值调整**：设置可接受的变化阈值以区分有意义的差异和噪音。这有助于减少[false positives](../F/false-positive.md)。
  - **选择性测试**：重点关注应用程序中容易发生视觉变化的关键区域。尽可能使用特定于元素或区域的屏幕截图，而不是全页捕获。
  - **并行执行**：并行运行屏幕截图测试以减少执行时间。基于云的服务可以为并行化提供必要的基础设施。
  - **自动审核工作流程**：将 [screenshot testing](../S/screenshot-testing.md) 结果集成到您的审核流程中。 GitHub Actions 或 GitLab CI 等工具可以自动化视觉更改的审批工作流程。
  - **图像版本控制**：将基线和测试图像存储在版本控制系统中。这允许跟踪更改并在必要时恢复到以前的版本。
  - **环境一致性**：确保测试在一致的环境中运行，具有相同的浏览器版本、屏幕分辨率和系统设置，以避免出现差异。
  通过结合这些策略，您可以构建强大且高效的[screenshot testing](../S/screenshot-testing.md) 流程，以补充您的[test automation](../T/test-automation.md) 工作。

- **基线图像创建**：建立一组基线图像，将来的屏幕截图将与这些图像进行比较。确保这些图像是在受控条件下捕获的，以尽量减少变化。
  - **自动捕获**：使用[Selenium](../S/selenium.md)、Puppeteer 或[Cypress](../C/cypress.md) 等工具将屏幕截图集成到[test scripts](../T/test-script.md) 中。在测试流程中的特定点触发捕获。

    ```
    // Example using Puppeteer
    await page.screenshot({ path: 'example.png' });
    ```

- **[Visual Regression Testing](../V/visual-regression-testing.md)**：实施视觉回归工具，例如 BackstopJS、Percy 或 Applitools。这些工具将新的屏幕截图与基线图像进行比较以检测变化。
  - **阈值调整**：设置可接受的变化阈值以区分有意义的差异和噪音。这有助于减少[false positives](../F/false-positive.md)。
  - **选择性测试**：重点关注应用程序中容易发生视觉变化的关键区域。尽可能使用特定于元素或区域的屏幕截图，而不是全页捕获。
  - **并行执行**：并行运行屏幕截图测试以减少执行时间。基于云的服务可以为并行化提供必要的基础设施。
  - **自动审核工作流程**：将 [screenshot testing](../S/screenshot-testing.md) 结果集成到您的审核流程中。 GitHub Actions 或 GitLab CI 等工具可以自动化视觉更改的审批工作流程。
  - **图像版本控制**：将基线和测试图像存储在版本控制系统中。这允许跟踪更改并在必要时恢复到以前的版本。
  - **环境一致性**：确保测试在一致的环境中运行，具有相同的浏览器版本、屏幕分辨率和系统设置，以避免出现差异。

### 高级主题

#### 屏幕截图测试在持续集成/持续部署 (CI/CD) 环境中如何工作？

在**CI/CD 环境**中，[screenshot testing](../S/screenshot-testing.md) 通常是自动化的并集成到部署管道中。它的一般工作原理如下：

1. **代码提交**：开发人员向版本控制系统提交代码，触发 CI/CD 管道。
  2. **构建**：构建应用程序并将其部署到暂存环境。
  3. **[Test Automation](../T/test-automation.md)** ：运行自动化测试，包括屏幕截图测试。
  4. **屏幕截图捕获**：测试工具在应用程序中导航，捕获 UI 元素或页面的屏幕截图。
  5. **比较**：使用图像比较算法将捕获的屏幕截图与基线图像进行比较。
  6. **结果分析**：
    - **匹配**：如果屏幕截图与基线匹配，则测试通过。
    - **不匹配**：如果存在差异，则测试失败，并且团队会收到警报。
    - **匹配**：如果屏幕截图与基线匹配，则测试通过。
    - **不匹配**：如果存在差异，则测试失败，并且团队会收到警报。
  7. **审查**：工程师审查不匹配的情况，以确定它们是否是预期的变化或真正的问题。
  8. **基线更新**：如果有意更改，则更新基线图像以反映 UI 的新状态。
  9. **修复问题**：如果不匹配是错误，开发人员会在继续之前修复它们。
  10. **继续**：如果所有测试都通过，管道将继续执行后续步骤，例如附加测试或部署到生产环境。
  此过程通常由 CI/CD 工具（如 Jenkins、GitLab CI 或 CircleCI）以及 [screenshot testing](../S/screenshot-testing.md) 工具（如 Percy 或 Screener）管理。为了集成[screenshot testing](../S/screenshot-testing.md)，工程师编写[test scripts](../T/test-script.md)并配置CI/CD管道以在适当的阶段包含这些测试。目标是自动捕捉视觉回归，确保任何 UI 更改都不会在代码投入生产之前破坏现有功能。

1. **代码提交**：开发人员向版本控制系统提交代码，触发 CI/CD 管道。
  2. **构建**：构建应用程序并将其部署到暂存环境。
  3. **[Test Automation](../T/test-automation.md)** ：运行自动化测试，包括屏幕截图测试。
  4. **屏幕截图捕获**：测试工具在应用程序中导航，捕获 UI 元素或页面的屏幕截图。
  5. **比较**：使用图像比较算法将捕获的屏幕截图与基线图像进行比较。
  6. **结果分析**：
    - **匹配**：如果屏幕截图与基线匹配，则测试通过。
    - **不匹配**：如果存在差异，则测试失败，并且团队会收到警报。
    - **匹配**：如果屏幕截图与基线匹配，则测试通过。
    - **不匹配**：如果存在差异，则测试失败，并且团队会收到警报。
  7. **审查**：工程师审查不匹配的情况，以确定它们是否是预期的变化或真正的问题。
  8. **基线更新**：如果有意更改，则更新基线图像以反映 UI 的新状态。
  9. **修复问题**：如果不匹配是错误，开发人员会在继续之前修复它们。
  10. **继续**：如果所有测试都通过，管道将继续执行后续步骤，例如附加测试或部署到生产环境。

#### 如何对响应式网页设计进行截图测试？

要执行 [screenshot testing](../S/screenshot-testing.md) 进行响应式网页设计，请按照以下步骤操作：

1. **定义您要测试的屏幕尺寸范围**和分辨率，包括桌面、平板电脑和移动设备尺寸。
  2. **使用支持响应式 [screenshot testing](../S/screenshot-testing.md) 的工具设置您的 [test environment](../T/test-environment.md)**，例如 [Selenium](../S/selenium.md) [WebDriver](../W/webdriver.md)、Puppeteer 或 Playwright。
  3. **编写[test scripts](../T/test-script.md)**，导航到目标网页并将浏览器窗口大小调整为指定尺寸。使用以下伪代码作为参考：

    ```
    // Example using Selenium WebDriver in TypeScript
    import { Builder, By, until } from 'selenium-webdriver';
    async function takeScreenshotAtWidth(width: number) {
      const driver = await new Builder().forBrowser('chrome').build();
      try {
        await driver.manage().window().setRect({ width: width, height: 800 });
        await driver.get('http://yourwebsite.com');
        await driver.wait(until.elementLocated(By.css('body')), 10000);
        const screenshot = await driver.takeScreenshot();
        // Save or process the screenshot
      } finally {
        await driver.quit();
      }
    }
    ```

4. **在每个定义的视口尺寸处捕获屏幕截图**。在进行屏幕截图之前，请确保页面已完全加载且动态内容已稳定。
  5. **使用图像比较工具或 [visual regression testing](../V/visual-regression-testing.md) 服务将屏幕截图与基线图像进行比较。
  6. **分析结果**以找出差异。请特别注意不同屏幕尺寸下可能发生的布局变化、重叠元素和截断。
  7. **记录并报告**任何视觉不一致或[bugs](../B/bug.md)，由开发团队解决。
  8. **在 CI/CD 管道中实现流程自动化**，以确保 [responsive design](../R/responsive-design.md) 在每个构建或部署中得到一致的测试。
  通过执行这些步骤，您可以有效地跨多种设备和屏幕尺寸验证响应式网页设计的视觉外观。

1. **定义您要测试的屏幕尺寸范围**和分辨率，包括桌面、平板电脑和移动设备尺寸。
  2. **使用支持响应式 [screenshot testing](../S/screenshot-testing.md) 的工具（例如 [Selenium](../S/selenium.md) [WebDriver](../W/webdriver.md)、Puppeteer 或 Playwright）设置您的 [test environment](../T/test-environment.md)**。
  3. **编写[test scripts](../T/test-script.md)**，导航到目标网页并将浏览器窗口大小调整为指定尺寸。使用以下伪代码作为参考：

    ```
    // Example using Selenium WebDriver in TypeScript
    import { Builder, By, until } from 'selenium-webdriver';
    async function takeScreenshotAtWidth(width: number) {
      const driver = await new Builder().forBrowser('chrome').build();
      try {
        await driver.manage().window().setRect({ width: width, height: 800 });
        await driver.get('http://yourwebsite.com');
        await driver.wait(until.elementLocated(By.css('body')), 10000);
        const screenshot = await driver.takeScreenshot();
        // Save or process the screenshot
      } finally {
        await driver.quit();
      }
    }
    ```

4. **在每个定义的视口尺寸处捕获屏幕截图**。在进行屏幕截图之前，请确保页面已完全加载且动态内容已稳定。
  5. **使用图像比较工具或 [visual regression testing](../V/visual-regression-testing.md) 服务将屏幕截图与基线图像进行比较。
  6. **分析结果**以找出差异。请特别注意不同屏幕尺寸下可能发生的布局变化、重叠元素和截断。
  7. **记录并报告**任何视觉不一致或[bugs](../B/bug.md)，由开发团队解决。
  8. **在 CI/CD 管道中实现流程自动化**，以确保 [responsive design](../R/responsive-design.md) 在每个构建或部署中得到一致的测试。

#### 如何处理跨浏览器截图测试？

处理跨浏览器[screenshot testing](../S/screenshot-testing.md) 涉及确保应用程序的视觉外观在不同浏览器中保持一致。以下是有效管理此流程的步骤：

1. **使用基于云的服务**或支持多个浏览器和版本的工具，例如[BrowserStack](../B/browserstack.md)或Sauce Labs。这使您可以访问各种浏览器配置而无需维护它们。
  2. **通过根据用户分析定义一组目标浏览器和版本来标准化 [test environments](../T/test-environment.md)**。这有助于集中您的测试工作。
  3. **如有必要，合并特定于浏览器的选择器**。某些浏览器可能以不同的方式解释 CSS，因此请在 [test scripts](../T/test-script.md) 中使用条件逻辑来处理这些情况。
  4. **标准化[test data](../T/test-data.md)**以确保一致性。在所有浏览器测试中使用相同的输入数据，以避免由于动态内容而导致屏幕截图出现差异。
  5. 使用您选择的工具在不同浏览器上**自动捕获屏幕截图**。例如，[Selenium](../S/selenium.md) [WebDriver](../W/webdriver.md) 可用于以编程方式截取屏幕截图：

  ```
  driver.takeScreenshot().then(function(image, err) {
      require('fs').writeFileSync('screenshot.png', image, 'base64');
  });
  ```

1. **实施视觉比较工具**，例如 Percy 或 Applitools，以自动检测视觉差异。这些工具可以逐像素比较屏幕截图或使用人工智能来关注可察觉的变化。
  2. **审查和分类**结果。自动化工具可能会标记需要人工判断才能确定它们是否是真正的 [bugs](../B/bug.md) 或可接受的变体的问题。
  3. **与 CI/CD 管道集成**，在每次提交时运行屏幕截图测试，确保立即反馈视觉回归。
  4. **记录差异**并维护浏览器特定问题的日志，以简化未来的测试工作。
  通过执行这些步骤，您可以创建一个强大的跨浏览器 [screenshot testing](../S/screenshot-testing.md) 流程，帮助在所有受支持的浏览器之间保持视觉一致性。

1. **使用基于云的服务**或支持多个浏览器和版本的工具，例如[BrowserStack](../B/browserstack.md)或Sauce Labs。这使您可以访问各种浏览器配置而无需维护它们。
  2. **通过根据用户分析定义一组目标浏览器和版本来标准化 [test environments](../T/test-environment.md)**。这有助于集中您的测试工作。
  3. **如有必要，合并特定于浏览器的选择器**。某些浏览器可能以不同的方式解释 CSS，因此请在 [test scripts](../T/test-script.md) 中使用条件逻辑来处理这些情况。
  4. **标准化 [test data](../T/test-data.md)** 以确保一致性。在所有浏览器测试中使用相同的输入数据，以避免由于动态内容而导致屏幕截图出现差异。
  5. 使用您选择的工具在不同浏览器上**自动捕获屏幕截图**。例如，[Selenium](../S/selenium.md) [WebDriver](../W/webdriver.md) 可用于以编程方式截取屏幕截图：
  1. **实施视觉比较工具**，例如 Percy 或 Applitools，以自动检测视觉差异。这些工具可以逐像素比较屏幕截图或使用人工智能来关注可察觉的变化。
  2. **审查和分类**结果。自动化工具可能会标记需要人工判断才能确定它们是否是真正的 [bugs](../B/bug.md) 或可接受的变体的问题。
  3. **与 CI/CD 管道集成**，在每次提交时运行屏幕截图测试，确保立即反馈视觉回归。
  4. **记录差异**并维护浏览器特定问题的日志，以简化未来的测试工作。

#### 人工智能 (AI) 在屏幕截图测试中的作用是什么？

人工智能 (AI) 在提高 [screenshot testing](../S/screenshot-testing.md) 的效率和准确性方面发挥着关键作用。通过利用**机器学习算法**，人工智能可以在像素级别分析屏幕截图，以检测人眼可能无法察觉的视觉差异。此功能对于识别可能影响用户体验的细微变化至关重要。
  人工智能驱动的工具还可以根据问题的潜在影响对问题进行“分类和优先排序”，从而简化测试人员的审核流程。这意味着关键的视觉问题 [bugs](../B/bug.md) 会得到及时解决，而次要的视觉问题则可以相应地进行分类。
  此外，人工智能擅长处理**动态内容**。传统的 [screenshot testing](../S/screenshot-testing.md) 可能会难以应对不同的内容，从而导致 [false positives](../F/false-positive.md)。人工智能可以智能地识别动态元素并专注于静态区域，或者它可以理解预期的变化并相应地验证它们。
  另一个显着的优势是人工智能的**自学习方面**。随着时间的推移，人工智能模型可以从应用程序的变化历史中学习并提高其预测能力，减少[false positives](../F/false-positive.md)的数量并增强测试可靠性。
  在 **[visual regression testing](../V/visual-regression-testing.md)** 领域，人工智能不仅可以将屏幕截图与基线图像进行比较，还可以通过了解变化的上下文，提供比简单的像素到像素比较更细致的分析。
  最后，人工智能可以通过在检测到有意更改时更新基线来协助屏幕截图测试的“自动化维护”，从而减少保持测试最新所需的手动工作。
  总之，人工智能通过提供高级分析、动态内容处理、问题优先级、随着时间的推移自我改进和维护自动化来增强[screenshot testing](../S/screenshot-testing.md)。

#### 如何对移动应用进行截图测试？

要对移动应用程序执行[screenshot testing](../S/screenshot-testing.md)，请执行以下步骤：

1. **设置您的[test environment](../T/test-environment.md)**：确保您有权访问具有所需操作系统版本的必要设备或仿真器/模拟器。
  2. **与 [test automation](../T/test-automation.md) 框架集成**：使用支持屏幕截图的框架，如 Appium、Espresso（适用于 Android）或 XCTest（适用于 iOS）。
  3. **编写[test cases](../T/test-case.md)**：开发导航到您要捕获的屏幕的[test cases](../T/test-case.md)。
  4. **捕获屏幕截图**：使用框架的[API](../A/api.md) 在[test cases](../T/test-case.md) 中的所需位置进行屏幕截图。例如，在 Appium 中，您可以使用：

  ```
  File scrFile = ((TakesScreenshot)driver).getScreenshotAs(OutputType.FILE);
  FileUtils.copyFile(scrFile, new File("path/to/screenshot.png"));
  ```

1. **验证屏幕截图**：将捕获的屏幕截图与基线图像进行比较。这可以手动完成，也可以使用提供视觉比较功能的工具完成。
  2. **处理不同的屏幕尺寸和分辨率**：可以通过捕获和比较多组基线图像来确保您的测试考虑到各种设备屏幕尺寸和分辨率。
  3. **自动化流程**：将屏幕截图捕获和比较集成到 CI/CD 管道中，以针对代码更改自动运行测试。
  4. **存储和查看结果**：保存屏幕截图和比较结果以供查看。 Allure 或 ExtentReports 等工具可以帮助组织和显示结果。
  5. **根据需要更新基线**：当有意更改 UI 时，更新基线图像以反映新的预期状态。
  请记住从屏幕截图中**排除瞬态 UI 元素**，例如弹出窗口或 toast，因为这些元素可能会导致 [false positives](../F/false-positive.md)。在捕获屏幕截图之前，使用 **条件等待** 确保 UI 稳定。

1. **设置您的[test environment](../T/test-environment.md)**：确保您可以访问具有所需操作系统版本的必要设备或仿真器/模拟器。
  2. **与 [test automation](../T/test-automation.md) 框架集成**：使用支持屏幕截图的框架，如 Appium、Espresso（适用于 Android）或 XCTest（适用于 iOS）。
  3. **编写[test cases](../T/test-case.md)**：开发[test cases](../T/test-case.md)，导航到您想要捕获的屏幕。
  4. **截取屏幕截图**：使用框架的[API](../A/api.md) 在[test cases](../T/test-case.md) 中的所需位置截取屏幕截图。例如，在 Appium 中，您可以使用：
  1. **验证屏幕截图**：将捕获的屏幕截图与基线图像进行比较。这可以手动完成，也可以使用提供视觉比较功能的工具完成。
  2. **处理不同的屏幕尺寸和分辨率**：可以通过捕获和比较多组基线图像来确保您的测试考虑到各种设备屏幕尺寸和分辨率。
  3. **自动化流程**：将屏幕截图捕获和比较集成到 CI/CD 管道中，以针对代码更改自动运行测试。
  4. **存储和查看结果**：保存屏幕截图和比较结果以供查看。 Allure 或 ExtentReports 等工具可以帮助组织和显示结果。
  5. **根据需要更新基线**：当有意更改 UI 时，更新基线图像以反映新的预期状态。
