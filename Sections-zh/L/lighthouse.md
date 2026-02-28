# 灯塔

<!-- TOC START -->
- [另请参阅：](#另请参阅：)
- [关于 灯塔 的问题吗？](#关于-灯塔-的问题吗？)
  - [基础知识和重要性](#基础知识和重要性)
    - [灯塔是什么？](#灯塔是什么？)
    - [为什么 Lighthouse 在软件自动化中很重要？](#为什么-lighthouse-在软件自动化中很重要？)
    - [Lighthouse 的主要特点是什么？](#lighthouse-的主要特点是什么？)
    - [Lighthouse 与其他性能审核工具有何不同？](#lighthouse-与其他性能审核工具有何不同？)
    - [Lighthouse 执行哪些类型的审核？](#lighthouse-执行哪些类型的审核？)
  - [用法和实现](#用法和实现)
    - [如何在 Chrome 中使用 Lighthouse？](#如何在-chrome-中使用-lighthouse？)
    - [Lighthouse 如何用于自动化测试？](#lighthouse-如何用于自动化测试？)
    - [运行 Lighthouse 审核的步骤是什么？](#运行-lighthouse-审核的步骤是什么？)
    - [如何在持续集成流程中使用 Lighthouse？](#如何在持续集成流程中使用-lighthouse？)
    - [如何配置 Lighthouse 进行自定义审核？](#如何配置-lighthouse-进行自定义审核？)
  - [结果和解释](#结果和解释)
    - [Lighthouse 分数是如何计算的？](#lighthouse-分数是如何计算的？)
    - [不同的 Lighthouse 审核类别有何含义？](#不同的-lighthouse-审核类别有何含义？)
    - [您如何解读 Lighthouse 报告？](#您如何解读-lighthouse-报告？)
    - [根据 Lighthouse 审核结果可以采取哪些行动？](#根据-lighthouse-审核结果可以采取哪些行动？)
    - [如何提高低 Lighthouse 分数？](#如何提高低-lighthouse-分数？)
  - [高级概念](#高级概念)
    - [Lighthouse CI 是什么以及它是如何工作的？](#lighthouse-ci-是什么以及它是如何工作的？)
    - [如何使用 Lighthouse 进行绩效预算？](#如何使用-lighthouse-进行绩效预算？)
    - [Lighthouse 在渐进式 Web 应用程序 (PWA) 中的作用是什么？](#lighthouse-在渐进式-web-应用程序-pwa-中的作用是什么？)
    - [Lighthouse 如何处理 JavaScript 执行？](#lighthouse-如何处理-javascript-执行？)
    - [使用 Lighthouse 时有哪些常见问题和解决方案？](#使用-lighthouse-时有哪些常见问题和解决方案？)
<!-- TOC END -->

灯塔

是 Google 开发的一款开源自动化工具，用于提高网页质量。它提供对性能、可访问性、渐进式 Web 应用程序、SEO 和网页质量其他方面的审核。通过跑步

灯塔

针对网页，开发人员和测试人员可以获得一组可操作的建议和见解，有助于优化网站的用户体验和整体有效性。

## 另请参阅：

- [Wikipedia](https://en.wikipedia.org/wiki/Google_Lighthouse)

## 关于 灯塔 的问题吗？

### 基础知识和重要性

#### 灯塔是什么？

[Lighthouse](../L/lighthouse.md) 是一个**开源**、**自动化工具**，用于提高网页质量。它可以针对任何公共网页或需要身份验证的网页运行。 [Lighthouse](../L/lighthouse.md) 对性能、可访问性、渐进式 Web 应用程序、SEO 等进行审核，提供网页质量和有效性的全面视图。
  要在 **Chrome** 中使用 [Lighthouse](../L/lighthouse.md)，请导航到要审核的页面，打开 **DevTools**，然后单击 **[Lighthouse](../L/lighthouse.md)** 选项卡。选择要运行的审核，然后单击 **生成报告** 按钮。 [Lighthouse](../L/lighthouse.md) 将对页面运行选定的审核，然后生成有关页面执行情况的报告。
  对于**[automated testing](../A/automated-testing.md)**，[Lighthouse](../L/lighthouse.md) 可以集成到**持续集成**系统中。它可以作为 Node 模块、命令行工具运行，也可以作为自定义构建过程的一部分以编程方式运行。 [Lighthouse](../L/lighthouse.md) CI 是一组命令，可以更轻松地使用[Lighthouse](../L/lighthouse.md) 进行持续集成。
  分数是根据性能指标和启发法计算的。每个指标单独评分，然后将分数合并为总分。
  提高低[Lighthouse](../L/lighthouse.md) 分数涉及解决报告中提供的具体反馈。这可能包括优化图像、缩小 CSS 和 JavaScript、实现延迟加载、改进辅助功能等等。
  对于 **JavaScript 执行**，[Lighthouse](../L/lighthouse.md) 会模拟中间层设备，即使在功能强大的桌面计算机上运行时也是如此，以创建一致的真实条件。
  使用 [Lighthouse](../L/lighthouse.md) 时的常见问题包括不稳定的性能指标，可以通过多次运行审核并考虑中值来缓解这些问题。

#### 为什么 Lighthouse 在软件自动化中很重要？

[Lighthouse](../L/lighthouse.md) 在软件[test automation](../T/test-automation.md) 中至关重要，因为它能够**将性能和质量检查**集成到开发和部署管道中。它为性能、可访问性、渐进式 Web 应用程序、SEO 和最佳实践提供**自动审核**，这对于维护高质量的 Web 应用程序至关重要。
  通过将 [Lighthouse](../L/lighthouse.md) 合并到 [automated testing](../A/automated-testing.md) 中，工程师可以确保根据这些指标评估任何代码更改，从而在开发周期的早期捕获回归或问题。这对于**持续集成（CI）**和**持续部署（CD）**环境尤其重要，其中自动化测试必须提供有关代码更改的潜在影响的快速反馈。
  [Lighthouse](../L/lighthouse.md) 的作用扩展到**绩效预算**，帮助团队设定并遵守绩效目标。它可以无头运行，使其适合**服务器端自动化**并集成到 CI/CD 管道中。该工具的**可配置性**允许根据特定需求进行定制审核，其**评分系统**提供了站点质量属性的可量化衡量标准。
  此外，[Lighthouse](../L/lighthouse.md) 的**报告**提供了可操作的见解，这对于寻求优化其 Web 应用程序的工程师来说非常宝贵。自动执行这些审核并将其集成到开发工作流程中的能力使 [Lighthouse](../L/lighthouse.md) 成为以自动化和高效的方式维护和改进 Web 应用程序的质量和用户体验的重要工具。

#### Lighthouse 的主要特点是什么？

**[Lighthouse](../L/lighthouse.md)** 的主要功能包括：

- **性能指标**：[Lighthouse](../L/lighthouse.md) 提供详细指标，例如首次内容绘制 (FCP)、速度指数、最大内容绘制 (LCP)、交互时间 (TTI)、总阻塞时间 (TBT) 和累积布局偏移 (CLS)。
  - **可访问性审核**：它根据网页内容可访问性指南 (WCAG) 评估网页的可访问性并提出改进建议。
  - **最佳实践**：[Lighthouse](../L/lighthouse.md) 检查是否遵守 Web 开发中的最佳实践，例如 HTTPS 使用、正确的图像长宽比以及避免弃用的 [APIs](../A/api.md)。
  - **SEO 审核**：它评估影响页面搜索引擎排名的元素，包括元标记、hreflang 标记和描述性链接文本。
  - **渐进式 Web 应用程序 (PWA) 评估**：[Lighthouse](../L/lighthouse.md) 可以验证 PWA 的各个方面，确保它们满足可靠性、性能和参与度的某些标准。
  - **自定义审核**：开发人员可以通过编写自定义审核来扩展[Lighthouse](../L/lighthouse.md)，以检查与其项目相关的特定要求或标准。
  - **CLI 和可编程 [API](../A/api.md)**：[Lighthouse](../L/lighthouse.md) 可以通过命令行运行，也可以通过其 [API](../A/api.md) 以编程方式运行，从而允许集成到自动化工作流程和 CI/CD 管道中。
  - **可配置性**：用户可以通过指定要审核的类别、限制设置和其他运行时选项来配置 [Lighthouse](../L/lighthouse.md) 运行。
  - **报告**：审核后，[Lighthouse](../L/lighthouse.md) 生成一份报告，其中包含每个类别的分数、详细解释以及可行的改进建议。
  - **可扩展性**：[Lighthouse](../L/lighthouse.md) 是开源的，可以扩展或定制以满足特定的测试需求，并且它与 [Lighthouse](../L/lighthouse.md) CI 等其他工具集成以进行连续测试。
  这些功能使 [Lighthouse](../L/lighthouse.md) 成为专注于提高 Web 应用程序质量的 Web 开发人员和 [test automation](../T/test-automation.md) 工程师的多功能工具。

- **性能指标**：[Lighthouse](../L/lighthouse.md) 提供详细指标，例如首次内容绘制 (FCP)、速度指数、最大内容绘制 (LCP)、交互时间 (TTI)、总阻塞时间 (TBT) 和累积布局偏移 (CLS)。
  - **可访问性审核**：它根据网页内容可访问性指南 (WCAG) 评估网页的可访问性并提出改进建议。
  - **最佳实践**：[Lighthouse](../L/lighthouse.md) 检查是否遵守 Web 开发中的最佳实践，例如 HTTPS 使用、正确的图像长宽比以及避免弃用的 [APIs](../A/api.md)。
  - **SEO 审核**：它评估影响页面搜索引擎排名的元素，包括元标记、hreflang 标记和描述性链接文本。
  - **渐进式 Web 应用程序 (PWA) 评估**：[Lighthouse](../L/lighthouse.md) 可以验证 PWA 的各个方面，确保它们满足可靠性、性能和参与度的某些标准。
  - **自定义审核**：开发人员可以通过编写自定义审核来扩展[Lighthouse](../L/lighthouse.md)，以检查与其项目相关的特定要求或标准。
  - **CLI 和可编程 [API](../A/api.md)**：[Lighthouse](../L/lighthouse.md) 可以通过命令行运行，也可以通过其 [API](../A/api.md) 以编程方式运行，从而允许集成到自动化工作流程和 CI/CD 管道中。
  - **可配置性**：用户可以通过指定要审核的类别、限制设置和其他运行时选项来配置 [Lighthouse](../L/lighthouse.md) 运行。
  - **报告**：审核后，[Lighthouse](../L/lighthouse.md) 生成一份报告，其中包含每个类别的分数、详细解释以及可行的改进建议。
  - **可扩展性**：[Lighthouse](../L/lighthouse.md) 是开源的，可以扩展或定制以满足特定的测试需求，并且它与 [Lighthouse](../L/lighthouse.md) CI 等其他工具集成以进行连续测试。

#### Lighthouse 与其他性能审核工具有何不同？

[Lighthouse](../L/lighthouse.md) 与其他性能审核工具的区别在于它**与 Chrome 开发人员工具集成**以及**强调用户体验**指标，例如 Core Web Vitals。虽然 WebPageTest 等工具提供详细的瀑布和网络信息，但 [Lighthouse](../L/lighthouse.md) 专注于提供 Web 性能、可访问性、最佳实践、SEO 和渐进式 Web 应用程序指标的**全面视图**。
  与某些需要复杂 [setup](../S/setup.md) 或服务器端集成的工具不同，[Lighthouse](../L/lighthouse.md) **易于访问**，并且可以从命令行、作为 Node 模块运行，或直接在浏览器中运行，使其适用于不同的工作流程。它还通过其灵活的配置选项提供**自定义审核功能**。
  [Lighthouse](../L/lighthouse.md) 的 **可操作报告** 具有清晰的评分和建议，能够指导开发人员如何提高性能和用户体验。它对于模拟移动网络和中间层设备上的页面加载特别有用，这是一种常见的[use case](../U/use-case.md)，并不总是被其他工具覆盖。
  此外，[Lighthouse](../L/lighthouse.md) 是**开源**并由 Google 维护，确保定期更新反映最新的 Web 开发最佳实践和标准。这与一些专有工具形成鲜明对比，这些工具可能不那么透明或不符合网络标准。
  最后，[Lighthouse](../L/lighthouse.md) 通过 [Lighthouse](../L/lighthouse.md) CI 集成到 **CI/CD 管道** 的能力使其成为自动化性能检查并确保部署前满足性能标准的强大选项。

#### Lighthouse 执行哪些类型的审核？

[Lighthouse](../L/lighthouse.md) 跨**五个类别**执行审核：**性能**、**可访问性**、**最佳实践**、**SEO** 和 **渐进式 Web 应用程序 (PWA)**。每个类别都包含各种检查：

- **性能**：评估首次内容绘制、速度指数和交互时间等指标，重点关注用户感知的加载体验和交互性。
  - **辅助功能**：检查可能阻止用户访问内容的常见问题，例如缺少图像替代文本、不正确的 ARIA 属性以及不正确的语义 HTML 元素。
  - **最佳实践**：寻找现代 Web 开发实践，包括 HTTPS 使用、正确的图像长宽比以及避免已弃用的[APIs](../A/api.md)。
  - **SEO**：评估影响页面对搜索引擎可见性的元素，例如元描述、hreflang 链接和清晰的字体大小。
  - **PWA**：验证是否存在 Service Worker、Web 应用程序清单以及使 Web 应用程序能够安装在设备主屏幕上并离线运行的其他标准。
  每次审核都会提供具体的、可操作的反馈，并单独评分，从而得出总体类别得分。 [Lighthouse](../L/lighthouse.md) 还提供**机会**和**诊断**来帮助确定需要改进的领域并了解根本问题。可以通过 [Lighthouse](../L/lighthouse.md) 配置针对特定 [use cases](../U/use-case.md) 扩展或自定义这些审核。

- **性能**：评估首次内容绘制、速度指数和交互时间等指标，重点关注用户感知的加载体验和交互性。
  - **辅助功能**：检查可能阻止用户访问内容的常见问题，例如缺少图像替代文本、不正确的 ARIA 属性以及不正确的语义 HTML 元素。
  - **最佳实践**：寻找现代 Web 开发实践，包括 HTTPS 使用、正确的图像长宽比以及避免已弃用的 [APIs](../A/api.md)。
  - **SEO**：评估影响页面对搜索引擎可见性的元素，例如元描述、hreflang 链接和清晰的字体大小。
  - **PWA**：验证是否存在 Service Worker、Web 应用程序清单以及使 Web 应用程序能够安装在设备主屏幕上并离线运行的其他标准。

### 用法和实现

#### 如何在 Chrome 中使用 Lighthouse？

要在 Chrome 中将 **[Lighthouse](../L/lighthouse.md)** 用于 [test automation](../T/test-automation.md)，请按照以下步骤操作：

1. 按 打开 Chrome 开发者工具
    `Ctrl+Shift+I`
    （或
    `Cmd+Option+I`
    在 Mac 上）。

2. 导航至
    **[Lighthouse](../L/lighthouse.md)**
    选项卡。

3. 选择所需的审核类别（性能、可访问性、最佳实践、SEO 和渐进式 Web 应用程序）。
  4. 选择适合模拟的设备类型（移动设备或桌面设备）。
  5. 单击
    **生成报告**
    开始审核。
  出于自动化目的，您可以使用命令行或作为节点模块以编程方式运行 [Lighthouse](../L/lighthouse.md)。这是使用 [Node.js](../N/node-js.md) 的基本示例：

  ```
  const lighthouse = require('lighthouse');
  const chromeLauncher = require('chrome-launcher');
  async function runLighthouse(url, options, config = null) {
    const chrome = await chromeLauncher.launch({ chromeFlags: options.chromeFlags });
    options.port = chrome.port;
    const results = await lighthouse(url, options, config);
    await chrome.kill();
    return results.lhr;
  }
  const options = {
    chromeFlags: ['--headless'],
    // Add more options here
  };
  // Usage
  runLighthouse('https://example.com', options)
    .then(results => console.log(results))
    .catch(err => console.error(err));
  ```对于持续集成，您可以使用**[Lighthouse](../L/lighthouse.md) CI**，它提供了对网站运行审核的命令并断言分数是否满足您的要求。它可以使用配置文件和 CLI 命令集成到您的 CI 管道中。
  请记住查看审核结果并进行必要的代码或配置更改以提高分数。通过将其集成到构建和部署管道中来实现流程自动化，以确保持续的性能监控。

1. 按 打开 Chrome 开发者工具
    `Ctrl+Shift+I`
    （或
    `Cmd+Option+I`
    在 Mac 上）。

2. 导航至
    **[Lighthouse](../L/lighthouse.md)**
    选项卡。

3. 选择所需的审核类别（性能、可访问性、最佳实践、SEO 和渐进式 Web 应用程序）。
  4. 选择适合模拟的设备类型（移动设备或桌面设备）。
  5. 单击
    **生成报告**
    开始审核。

#### Lighthouse 如何用于自动化测试？

[Lighthouse](../L/lighthouse.md) 可以集成到[automated testing](../A/automated-testing.md) 工作流程中，以确保 Web 应用程序满足性能、可访问性、最佳实践和 SEO 标准。要自动执行[Lighthouse](../L/lighthouse.md) 测试，您可以使用[Lighthouse](../L/lighthouse.md) CLI 或[Lighthouse](../L/lighthouse.md) 节点模块。
  **CLI 方法：**
  通过 npm 全局安装[Lighthouse](../L/lighthouse.md)：

  ```
  npm install -g lighthouse
  ```在无头模式下运行 [Lighthouse](../L/lighthouse.md) 以测试 URL 并将结果输出到 JSON 文件：

  ```
  lighthouse https://example.com --output=json --output-path=./report.json --chrome-flags="--headless"
  ```**节点模块方法：**
  安装 [Lighthouse](../L/lighthouse.md) 作为开发依赖项：

  ```
  npm install --save-dev lighthouse
  ```创建一个脚本来启动 Chrome 并以编程方式运行[Lighthouse](../L/lighthouse.md)：

  ```
  const lighthouse = require('lighthouse');
  const chromeLauncher = require('chrome-launcher');
  async function runLighthouse(url, opts, config = null) {
    const chrome = await chromeLauncher.launch({ chromeFlags: opts.chromeFlags });
    opts.port = chrome.port;
    const results = await lighthouse(url, opts, config);
    await chrome.kill();
    return results.lhr;
  }
  const options = {
    chromeFlags: ['--headless'],
    output: 'json'
  };
  runLighthouse('https://example.com', options)
    .then(results => {
      // Process Lighthouse results here
    });
  ```**持续集成：**
  使用[Lighthouse](../L/lighthouse.md) CI 将[Lighthouse](../L/lighthouse.md) 合并到CI 管道中。设置 `.lighthouserc.js` 配置文件并将 [Lighthouse](../L/lighthouse.md) CI 命令添加到 CI 配置中：

  ```
  lhci autorun --config=.lighthouserc.js
  ```这将在每次提交或拉取请求期间针对指定的 URL 运行审核，确保代码更改不会降低应用程序的质量。使用[Lighthouse](../L/lighthouse.md) CI 服务器进行历史跟踪和断言性能预算。

#### 运行 Lighthouse 审核的步骤是什么？

要运行 [Lighthouse](../L/lighthouse.md) 审核：

1. **打开谷歌浏览器**
    并导航至您要审核的页面。

2. **访问开发者工具**
    通过按
    `Ctrl+Shift+I`
    （或
    `Cmd+Option+I`
    在 Mac 上），或右键单击页面并选择“检查”。

3. 单击
    **[Lighthouse](../L/lighthouse.md)**
    开发人员工具面板中的选项卡。如果它不可见，您可能需要单击
    `>>`
    图标来找到它。

4. **选择类别**
    您希望审核（性能、可访问性、最佳实践、SEO 和渐进式 Web 应用程序）。

5. 选择
    **设备类型**
    （移动或桌面）进行模拟。

6.（可选）单击
    **高级设置**
    在审核期间调整限制选项或阻止某些 URL。

7. 单击
    **“生成报告”**
    按钮开始审核。
  [Lighthouse](../L/lighthouse.md) 现在将对页面运行一系列测试并生成报告。审核完成后，您将收到一份详细的报告，概述页面的性能和质量。您可以使用此报告来确定需要改进的领域。
  对于 [automated testing](../A/automated-testing.md) 或持续集成，您可以通过 npm 安装 [Lighthouse](../L/lighthouse.md) CLI 来使用它：

  ```
  npm install -g lighthouse
  ```然后运行审计：

  ```
  lighthouse https://example.com --output json --output-path ./report.json
  ```将 `https://example.com` 替换为您的 URL，并根据需要调整输出格式和路径。此命令将生成可集成到 CI/CD 管道中的 JSON 报告。

1. **打开谷歌浏览器**
    并导航至您要审核的页面。

2. **访问开发者工具**
    通过按
    `Ctrl+Shift+I`
    （或
    `Cmd+Option+I`
    在 Mac 上），或右键单击页面并选择“检查”。

3. 单击
    **[Lighthouse](../L/lighthouse.md)**
    开发人员工具面板中的选项卡。如果它不可见，您可能需要单击
    `>>`
    图标来找到它。

4. **选择类别**
    您希望审核（性能、可访问性、最佳实践、SEO 和渐进式 Web 应用程序）。

5. 选择
    **设备类型**
    （移动或桌面）进行模拟。

6.（可选）单击
    **高级设置**
    在审核期间调整限制选项或阻止某些 URL。

7. 单击
    **“生成报告”**
    按钮开始审核。

#### 如何在持续集成流程中使用 Lighthouse？

将 **[Lighthouse](../L/lighthouse.md)** 集成到持续集成 (CI) 流程中可确保每次代码提交都遵守性能、可访问性和 SEO 标准。要在 CI 中使用 [Lighthouse](../L/lighthouse.md)，请按照以下步骤操作：

1. **安装[Lighthouse](../L/lighthouse.md) CI**：

    ```
    npm install -g @lhci/cli
    ```

2. **通过在项目根目录中创建 `.lighthouserc.js` 或 `.lighthouserc.json` 文件来配置 [Lighthouse](../L/lighthouse.md) CI**。定义要审核的 URL、运行次数以及任何其他配置。
  3. **在 CI 管道中添加 [Lighthouse](../L/lighthouse.md) CI 步骤**。例如，在 GitHub Actions 工作流程中，添加运行 [Lighthouse](../L/lighthouse.md) CI 的作业：

    ```
    - name: Run Lighthouse CI
      run: lhci autorun
    ```

4. **设置断言**以执行绩效预算或特定审计阈值。如果不满足这些条件，则 CI 构建失败：

    ```
    "assertions": {
      "categories:performance": ["error", { "minScore": 0.9 }],
      "categories:accessibility": ["error", { "minScore": 0.9 }]
    }
    ```

5. **存储报告**以进行历史比较和跟踪回归。使用`--upload.target` 选项上传到[Lighthouse](../L/lighthouse.md) CI 服务器或其他存储解决方案。
  6. **自动化流程**以在每个拉取请求上运行或推送到特定分支，确保新代码满足定义的质量标准。
  通过将 [Lighthouse](../L/lighthouse.md) 集成到 CI 中，您可以创建一个**反馈循环**，尽早提醒开发人员潜在的问题，从而保持 Web 应用程序用户体验的高标准。

1. **安装[Lighthouse](../L/lighthouse.md) CI**：

    ```
    npm install -g @lhci/cli
    ```

2. **通过在项目根目录中创建 `.lighthouserc.js` 或 `.lighthouserc.json` 文件来配置 [Lighthouse](../L/lighthouse.md) CI**。定义要审核的 URL、运行次数以及任何其他配置。
  3. **在 CI 管道中添加 [Lighthouse](../L/lighthouse.md) CI 步骤**。例如，在 GitHub Actions 工作流程中，添加运行 [Lighthouse](../L/lighthouse.md) CI 的作业：

    ```
    - name: Run Lighthouse CI
      run: lhci autorun
    ```

4. **设置断言**以执行绩效预算或特定审计阈值。如果不满足这些条件，则 CI 构建失败：

    ```
    "assertions": {
      "categories:performance": ["error", { "minScore": 0.9 }],
      "categories:accessibility": ["error", { "minScore": 0.9 }]
    }
    ```

5. **存储报告**以进行历史比较和跟踪回归。使用`--upload.target` 选项上传到[Lighthouse](../L/lighthouse.md) CI 服务器或其他存储解决方案。
  6. **自动化流程**以在每个拉取请求上运行或推送到特定分支，确保新代码满足定义的质量标准。

#### 如何配置 Lighthouse 进行自定义审核？

要为自定义审核配置**[Lighthouse](../L/lighthouse.md)**，您需要创建自定义审核定义和收集器。这是一个简洁的指南：

1. **创建自定义收集器**：

    ```
    const { Gatherer } = require('lighthouse');
    class CustomGatherer extends Gatherer {
      afterPass(options) {
        // Collect data and return it
      }
    }
    module.exports = CustomGatherer;
    ```

- 收集器从页面收集信息。延长
      `Gatherer`
      来自灯塔的课程。

- 收集器从页面收集信息。延长
      `Gatherer`
      来自灯塔的课程。

2. **制定自定义审核**：

    ```
    const { Audit } = require('lighthouse');
    class CustomAudit extends Audit {
      static get meta() {
        return {
          id: 'custom-audit-id',
          title: 'Custom Audit',
          failureTitle: 'Custom Audit Failed',
          description: 'Description of your custom audit',
          requiredArtifacts: ['CustomGatherer'],
        };
      }
      static audit(artifacts) {
        const loadMetrics = artifacts.CustomGatherer;
        // Perform audit logic and return a score
        return {
          score: Number(loadMetrics < threshold),
        };
      }
    }
    module.exports = CustomAudit;
    ```

- 审计使用收集者收集的数据。延长
      `Audit`
      类。

- 审计使用收集者收集的数据。延长
      `Audit`
      类。

3. **添加到[Lighthouse](../L/lighthouse.md)配置**：

    ```
    module.exports = {
      passes: [{
        passName: 'defaultPass',
        gatherers: [
          'path/to/customgatherer',
        ],
      }],
      audits: [
        'path/to/customaudit',
      ],
      categories: {
        customCategory: {
          title: 'Custom Category',
          description: 'Includes custom audits',
          auditRefs: [
            { id: 'custom-audit-id', weight: 1 },
          ],
        },
      },
    };
    ```

- 在 Lighthouse 配置中包含您的自定义收集器和审核。
    - 在 Lighthouse 配置中包含您的自定义收集器和审核。
  4. **使用您的自定义配置运行[Lighthouse](../L/lighthouse.md)**：

    ```
    lighthouse https://example.com --config-path=path/to/custom-config.js
    ```请记住处理收集器和审核逻辑中的异常和边缘情况，以确保稳健性。

1. **创建自定义收集器**：

    ```
    const { Gatherer } = require('lighthouse');
    class CustomGatherer extends Gatherer {
      afterPass(options) {
        // Collect data and return it
      }
    }
    module.exports = CustomGatherer;
    ```

- 收集器从页面收集信息。延长
      `Gatherer`
      来自灯塔的课程。

- 收集器从页面收集信息。延长
      `Gatherer`
      来自灯塔的课程。

2. **制定自定义审核**：

    ```
    const { Audit } = require('lighthouse');
    class CustomAudit extends Audit {
      static get meta() {
        return {
          id: 'custom-audit-id',
          title: 'Custom Audit',
          failureTitle: 'Custom Audit Failed',
          description: 'Description of your custom audit',
          requiredArtifacts: ['CustomGatherer'],
        };
      }
      static audit(artifacts) {
        const loadMetrics = artifacts.CustomGatherer;
        // Perform audit logic and return a score
        return {
          score: Number(loadMetrics < threshold),
        };
      }
    }
    module.exports = CustomAudit;
    ```

- 审计使用收集者收集的数据。延长
      `Audit`
      类。

- 审计使用收集者收集的数据。延长
      `Audit`
      类。

3. **添加到[Lighthouse](../L/lighthouse.md)配置**：

    ```
    module.exports = {
      passes: [{
        passName: 'defaultPass',
        gatherers: [
          'path/to/customgatherer',
        ],
      }],
      audits: [
        'path/to/customaudit',
      ],
      categories: {
        customCategory: {
          title: 'Custom Category',
          description: 'Includes custom audits',
          auditRefs: [
            { id: 'custom-audit-id', weight: 1 },
          ],
        },
      },
    };
    ```

- 在 Lighthouse 配置中包含您的自定义收集器和审核。
    - 在 Lighthouse 配置中包含您的自定义收集器和审核。
  4. **使用您的自定义配置运行[Lighthouse](../L/lighthouse.md)**：

    ```
    lighthouse https://example.com --config-path=path/to/custom-config.js
    ```

### 结果和解释

#### Lighthouse 分数是如何计算的？

[Lighthouse](../L/lighthouse.md) 分数是根据一系列审核计算得出的，分为五个类别：**性能**、**可访问性**、**最佳实践**、**SEO** 和 **渐进式 Web 应用程序**。每个类别都有一组包含单独测试的审核。然后将这些测试的分数汇总为每个类别的分数。
  **性能** 分数很大程度上取决于速度指标，例如首次内容绘制 (FCP)、速度指数、最大内容绘制 (LCP)、交互时间 (TTI)、总阻塞时间 (TBT) 和累积布局偏移 (CLS)。这些指标反映了用户在加载、交互性和视觉稳定性方面的体验。
  **可访问性**审核检查可能阻止用户因残疾而访问内容的常见问题。这包括正确使用 HTML 元素、ARIA 属性、颜色对比度和导航。
  **最佳实践**分数源自检查现代 Web 开发标准的测试，包括 HTTPS 使用、正确的图像长宽比以及避免弃用的[APIs](../A/api.md)。
  **SEO** 分数评估影响网站对搜索引擎可见性的元素，例如元标记、hreflang 标记和描述性链接文本。
  **渐进式 Web 应用程序** 分数评估 Web 应用程序是否准备好提供类似应用程序的体验，并考虑 Service Worker 注册、Web 应用程序清单以及对不同屏幕尺寸的响应等因素。
  每个类别分数都是其审核分数的加权平均值。 [Lighthouse](../L/lighthouse.md) 总体得分是五个类别得分的加权平均值，其中 **性能** 通常具有最大权重。分数范围从 0 到 100，分数越高表示更好地遵守 Web 开发最佳实践。

#### 不同的 Lighthouse 审核类别有何含义？

[Lighthouse](../L/lighthouse.md) 审核类别是评估网络应用程序质量各个方面的基准。每个类别代表用户体验和技术性能的核心领域：

- **性能**：衡量网站的速度和效率。指标包括首次内容绘制、速度指数和交互时间。
  - **辅助功能**：评估残障人士使用网站的情况。它检查 ARIA 属性、屏幕阅读器支持和导航可访问性的正确使用。
  - **最佳实践**：评估现代 Web 开发实践的使用。这包括检查 HTTPS 使用情况、正确的图像长宽比以及避免已弃用的 [APIs](../A/api.md)。
  - **SEO**：分析网站被搜索引擎索引的潜力。它着眼于移动友好性、内容最佳实践和元数据存在。
  - **渐进式 Web 应用程序 (PWA)**：确定网站是否遵守 PWA 标准。它检查 Service Worker 注册、有效的 Web 应用清单和 [responsive design](../R/responsive-design.md)。
  每个类别都提供了具体的、可操作的见解。例如，**性能**类别可以突出显示延迟加载屏幕外图像的机会，而**辅助功能**可能会建议屏幕阅读器用户进行改进。这些见解指导工程师优化其 Web 应用程序，以获得更好的用户体验和技术稳健性。

- **性能**：衡量网站的速度和效率。指标包括首次内容绘制、速度指数和交互时间。
  - **辅助功能**：评估残障人士使用网站的情况。它检查 ARIA 属性、屏幕阅读器支持和导航可访问性的正确使用。
  - **最佳实践**：评估现代 Web 开发实践的使用。这包括检查 HTTPS 使用情况、正确的图像长宽比以及避免已弃用的 [APIs](../A/api.md)。
  - **SEO**：分析网站被搜索引擎索引的潜力。它着眼于移动友好性、内容最佳实践和元数据存在。
  - **渐进式 Web 应用程序 (PWA)**：确定网站是否遵守 PWA 标准。它检查 Service Worker 注册、有效的 Web 应用程序清单和 [responsive design](../R/responsive-design.md)。

#### 您如何解读 Lighthouse 报告？

解释 [Lighthouse](../L/lighthouse.md) 报告涉及分析每个审核类别中提供的数据，以确定 Web 应用程序中需要改进的领域。运行 [Lighthouse](../L/lighthouse.md) 审核后，您将收到一份报告，其中包含 **性能**、**可访问性**、**最佳实践**、**SEO** 和 **渐进式 Web 应用程序** 的分数。
  **性能**：查看诸如**首次内容绘制 (FCP)**、**速度指数**、**最大内容绘制 (LCP)**、**交互时间 (TTI)**、**总阻塞时间 (TBT)** 和 **累积布局偏移 (CLS)** 等指标。这些指标可以深入了解用户感知的加载体验和交互性。
  **辅助功能**：查看可能阻止残障用户访问内容的问题。这包括缺少替代文本、不正确的 ARIA 属性以及不正确的语义 HTML 使用。
  **最佳实践**：检查可能影响应用程序可靠性和安全性的警告和错误，例如使用 HTTPS、避免弃用的 [APIs](../A/api.md) 以及确保正确的图像长宽比。
  **SEO**：检查可能影响网站搜索引擎排名的因素，包括移动设备友好性、内容最佳实践和元数据存在。
  **渐进式 Web 应用程序**：根据 PWA 标准评估您的应用程序，重点关注快速加载时间、[responsive design](../R/responsive-design.md) 和离线工作模式等方面。
  对于每次审核，[Lighthouse](../L/lighthouse.md) 提供：

- A
    **分数**
    (0-100) 指示该类别页面的质量。

- **颜色编码指标**
    （绿色表示良好，橙色表示需要改进，红色表示较差）。

- **可行的建议**
    为了提高你的分数。
  使用详细的建议来确定修复和增强的优先级。首先解决**红色**项目，因为它们代表最关键的问题，然后解决**橙色**，然后解决**绿色**以微调性能。实施更改，重新运行[Lighthouse](../L/lighthouse.md)，并比较报告以跟踪进度。

- A
    **分数**
    (0-100) 指示该类别页面的质量。

- **颜色编码指标**
    （绿色表示良好，橙色表示需要改进，红色表示较差）。

- **可行的建议**
    为了提高你的分数。

#### 根据 Lighthouse 审核结果可以采取哪些行动？

根据[Lighthouse](../L/lighthouse.md) 审核结果，可以采取多种措施来提高 Web 应用程序的质量和性能：

- **优化图像**：压缩并正确格式化图像以减少加载时间。
  - **缩小 CSS、JavaScript 和 HTML**：删除不必要的字符而不更改功能以减小文件大小。
  - **利用浏览器缓存**：设置适当的缓存标头以最大程度地减少返回用户的重复加载时间。
  - **消除渲染阻塞资源**：推迟非关键 CSS 和 JavaScript 以加快首次绘制速度。
  - **使用延迟加载**：按需加载图像和 iframe 以减少初始加载时间。
  - **提高服务器响应时间**：优化服务器配置，使用内容交付网络 (CDN)，或在必要时升级托管。
  - **删除未使用的代码**：检测并清除死代码以减少文件大小和复杂性。
  - **启用压缩**：使用 Gzip 或 Brotli 压缩基于文本的资源。
  - **实施 H​​TTP/2** ：利用多路复用和服务器推送功能来加快加载时间。
  - **优先考虑首屏内容**：构建 HTML 以首先加载最重要的内容。
  - **辅助功能增强**：解决影响残障用户的问题，例如颜色对比度和键盘导航。
  - **SEO 改进**：确保元标记存在且具有描述性，并且内容可抓取。
  迭代应用这些操作，将它们集成到您的 CI/CD 管道中以实现持续改进。定期使用[Lighthouse](../L/lighthouse.md) 进行重新审核，以衡量进度并发现新的优化机会。

- **优化图像**：压缩并正确格式化图像以减少加载时间。
  - **缩小 CSS、JavaScript 和 HTML**：删除不必要的字符而不更改功能以减小文件大小。
  - **利用浏览器缓存**：设置适当的缓存标头以最大程度地减少返回用户的重复加载时间。
  - **消除渲染阻塞资源**：推迟非关键 CSS 和 JavaScript 以加快首次绘制速度。
  - **使用延迟加载**：按需加载图像和 iframe 以减少初始加载时间。
  - **提高服务器响应时间**：优化服务器配置，使用内容交付网络 (CDN)，或在必要时升级托管。
  - **删除未使用的代码**：检测并清除死代码以减少文件大小和复杂性。
  - **启用压缩**：使用 Gzip 或 Brotli 压缩基于文本的资源。
  - **实施 H​​TTP/2** ：利用多路复用和服务器推送功能来加快加载时间。
  - **优先考虑首屏内容**：构建 HTML 以首先加载最重要的内容。
  - **辅助功能增强**：解决影响残障用户的问题，例如颜色对比度和键盘导航。
  - **SEO 改进**：确保元标记存在且具有描述性，并且内容可抓取。

#### 如何提高低 Lighthouse 分数？

提高低 [Lighthouse](../L/lighthouse.md) 分数涉及优化 Web 应用程序的各个方面。以下是一些策略：

- **优化图像**：使用 ImageOptim 等工具或 TinyPNG 等服务压缩图像而不损失质量。
  - **缩小 CSS、JavaScript 和 HTML**：使用 UglifyJS、cssnano 或 HTMLMinifier 等工具来减小文件大小。
  - **启用压缩** ：在服务器上使用 Gzip 或 Brotli 来压缩资源。
  - **利用浏览器缓存**：设置适当
    `Cache-Control`
    资产的标题。

- **删除渲染阻塞资源**：内联关键 CSS，推迟非关键 JavaScript，或使用
    `async`
    属性。

- **使用高效的 CSS 选择器**：避免使用会减慢页面渲染速度的复杂选择器。
  - **最小化主线程工作**：分析您的 JavaScript 并优化阻塞主线程的长任务。
  - **减少 JavaScript 有效负载**：使用动态导入拆分代码，并通过 Tree Shaking 删除未使用的代码。
  - **实施延迟加载**：仅在需要时加载图像或模块。
  - **优化网页字体**：使用
    `font-display: swap`
    最大限度地减少渲染阻塞，并考虑对字体进行子集化。

- **预连接到所需的来源**：使用
    `<link rel="preconnect">`
    尽早建立与重要第三方域的连接。

- **使用 HTTP/2** ：通过 HTTP/2 提供资源以实现更好的多路复用和并行性。
  - **优先内容**：使用
    `Priority Hints`
    或
    `loading`
    属性来优先加载关键资源。

- **审核第三方代码**：删除或优化不重要的第三方脚本。
  迭代应用这些优化，并在每次更改后监控 [Lighthouse](../L/lighthouse.md) 分数以了解其影响。

- **优化图像**：使用 ImageOptim 等工具或 TinyPNG 等服务压缩图像而不损失质量。
  - **缩小 CSS、JavaScript 和 HTML**：使用 UglifyJS、cssnano 或 HTMLMinifier 等工具来减小文件大小。
  - **启用压缩** ：在服务器上使用 Gzip 或 Brotli 来压缩资源。
  - **利用浏览器缓存**：设置适当
    `Cache-Control`
    资产的标题。

- **删除渲染阻塞资源**：内联关键 CSS，推迟非关键 JavaScript，或使用
    `async`
    属性。

- **使用高效的 CSS 选择器**：避免使用会减慢页面渲染速度的复杂选择器。
  - **最小化主线程工作**：分析您的 JavaScript 并优化阻塞主线程的长任务。
  - **减少 JavaScript 有效负载**：使用动态导入拆分代码，并通过 Tree Shaking 删除未使用的代码。
  - **实施延迟加载**：仅在需要时加载图像或模块。
  - **优化网页字体**：使用
    `font-display: swap`
    最大限度地减少渲染阻塞，并考虑对字体进行子集化。

- **预连接到所需的来源**：使用
    `<link rel="preconnect">`
    尽早建立与重要第三方域的连接。

- **使用 HTTP/2** ：通过 HTTP/2 提供资源以实现更好的多路复用和并行性。
  - **优先内容**：使用
    `Priority Hints`
    或
    `loading`
    属性来优先加载关键资源。

- **审核第三方代码**：删除或优化不重要的第三方脚本。

### 高级概念

#### Lighthouse CI 是什么以及它是如何工作的？

[Lighthouse](../L/lighthouse.md) CI 是一种开源自动化工具，用于提高网页和应用程序的质量。它与持续集成 (CI) 系统集成，对每次提交运行 [Lighthouse](../L/lighthouse.md) 审核，提供有关性能、可访问性、SEO 和最佳实践方面潜在回归的即时反馈。
  **它是如何工作的：**

1. **安装**：[Lighthouse](../L/lighthouse.md) CI 作为 npm 包安装。

    ```
    npm install -g @lhci/cli
    ```

2. **配置**：创建 `.lighthouserc.js` 或 `.lighthouserc.json` 文件来配置审核。

    ```
    module.exports = {
      ci: {
        collect: {
          /* ... */
        },
        assert: {
          /* ... */
        },
        upload: {
          /* ... */
        },
      },
    };
    ```

3. **运行审核**：使用[Lighthouse](../L/lighthouse.md) CI CLI 针对应用程序的构建版本运行审核。

    ```
    lhci autorun
    ```

4. **断言**：定义性能指标和其他审核分数的断言。如果断言不满足指定的阈值，[Lighthouse](../L/lighthouse.md) CI 将使 CI 构建失败。
  5. **报告**：结果显示在 CI 输出中，详细报告可以上传到[Lighthouse](../L/lighthouse.md) CI 服务器或其他托管解决方案以进行进一步分析。
  6. **集成**：[Lighthouse](../L/lighthouse.md) CI 可以集成到流行的 CI 服务中，例如 GitHub Actions、Travis CI 和 Jenkins，确保性能和质量检查成为开发工作流程的一部分。
  [Lighthouse](../L/lighthouse.md) CI 确保持续监控性能和质量，有助于防止回归并在更新过程中保持高标准。

1. **安装**：[Lighthouse](../L/lighthouse.md) CI 作为 npm 包安装。

    ```
    npm install -g @lhci/cli
    ```

2. **配置**：创建 `.lighthouserc.js` 或 `.lighthouserc.json` 文件来配置审核。

    ```
    module.exports = {
      ci: {
        collect: {
          /* ... */
        },
        assert: {
          /* ... */
        },
        upload: {
          /* ... */
        },
      },
    };
    ```

3. **运行审核**：使用[Lighthouse](../L/lighthouse.md) CI CLI 针对应用程序的构建版本运行审核。

    ```
    lhci autorun
    ```

4. **断言**：定义性能指标和其他审核分数的断言。如果断言不满足指定的阈值，[Lighthouse](../L/lighthouse.md) CI 将使 CI 构建失败。
  5. **报告**：结果显示在 CI 输出中，详细报告可以上传到[Lighthouse](../L/lighthouse.md) CI 服务器或其他托管解决方案以进行进一步分析。
  6. **集成**：[Lighthouse](../L/lighthouse.md) CI 可以集成到流行的 CI 服务中，例如 GitHub Actions、Travis CI 和 Jenkins，确保性能和质量检查成为开发工作流程的一部分。

#### 如何使用 Lighthouse 进行绩效预算？

[Lighthouse](../L/lighthouse.md) 有助于为您的 Web 应用程序实施和执行 **性能预算**。性能预算是对影响站点性能的某些指标（例如图像、脚本和 CSS 文件的大小）的一组限制。
  要使用 [Lighthouse](../L/lighthouse.md) 进行性能预算，请执行以下步骤：

1. **定义您的绩效预算**。确定要实施的指标和阈值，例如最大页面加载时间、图像总大小或 HTTP 请求数。
  2. **创建[Lighthouse](../L/lighthouse.md)配置文件**。在 JSON 文件中，指定您的性能预算限制。例如：

  ```
  {
    "extends": "lighthouse:default",
    "settings": {
      "budgets": [{
        "resourceSizes": [
          {
            "resourceType": "script",
            "budget": 125
          },
          {
            "resourceType": "total",
            "budget": 300
          }
        ],
        "resourceCounts": [
          {
            "resourceType": "third-party",
            "budget": 10
          }
        ]
      }]
    }
  }
  ```

1. **使用您的配置运行[Lighthouse](../L/lighthouse.md)**
    。使用 CLI 通过您的配置文件运行 Lighthouse：

  ```
  lighthouse https://example.com --budget-path=./path-to-your-budget.json
  ```

1. **查看输出**
    。 Lighthouse 将在报告中包含一个部分，指示您的网站是否保持在定义的预算范围内。如果超出任何预算，Lighthouse 会提供超出部分的详细信息。
  通过将此流程集成到您的**CI/CD 管道**中，您可以自动检查每个构建是否符合您的性能预算，确保在开发过程的早期发现并解决性能回归问题。

1. **定义您的绩效预算**。确定要实施的指标和阈值，例如最大页面加载时间、图像总大小或 HTTP 请求数。
  2. **创建[Lighthouse](../L/lighthouse.md) 配置文件**。在 JSON 文件中，指定您的性能预算限制。例如：
  1. **使用您的配置运行[Lighthouse](../L/lighthouse.md)**
    。使用 CLI 通过您的配置文件运行 Lighthouse：

1. **查看输出**
    。 Lighthouse 将在报告中包含一个部分，指示您的网站是否保持在定义的预算范围内。如果超出任何预算，Lighthouse 会提供超出部分的详细信息。

#### Lighthouse 在渐进式 Web 应用程序 (PWA) 中的作用是什么？

[Lighthouse](../L/lighthouse.md) 通过提供一组专门针对 PWA 功能和最佳实践的审核，在评估和提高渐进式 Web 应用程序 (PWA) 的质量方面发挥着至关重要的作用。它根据现代 Web 应用程序的预期基线来评估 PWA，确保它们快速、可靠且有吸引力。
  对于 PWA，[Lighthouse](../L/lighthouse.md) 检查：

- **Service Worker** ：验证 Service Worker 是否已注册以及是否允许离线使用。
  - **Web 应用程序清单**：确保清单文件存在，并具有适当的图标、主题颜色和显示设置，以实现全屏、独立的用户体验。
  - **HTTPS**：确认应用程序通过安全连接提供服务，这是许多 PWA 功能的先决条件。
  - **重定向**：检查导航是否未重定向，这可能会减慢应用程序的速度。
  - **启动画面**：评估加载期间是否提供自定义启动画面，以改善用户体验。
  - **主题**：评估地址栏和启动画面主题颜色的一致性。
  - **视口配置**：确保视口正确设置为响应式设计。
  - **用户参与度**：衡量提示用户将网络应用程序安装到主屏幕的能力。
  通过将 [Lighthouse](../L/lighthouse.md) 集成到 [test automation](../T/test-automation.md) 流程中，工程师可以自动评估这些 PWA 特定标准、确定需要改进的领域并跟踪一段时间内的进度。这可确保 PWA 满足性能、可访问性和用户体验的高标准，这对于用户保留和满意度至关重要。

- **Service Worker** ：验证 Service Worker 是否已注册以及是否允许离线使用。
  - **Web 应用程序清单**：确保清单文件存在，并具有适当的图标、主题颜色和显示设置，以实现全屏、独立的用户体验。
  - **HTTPS**：确认应用程序通过安全连接提供服务，这是许多 PWA 功能的先决条件。
  - **重定向**：检查导航是否未重定向，这可能会减慢应用程序的速度。
  - **启动画面**：评估加载期间是否提供自定义启动画面，以改善用户体验。
  - **主题**：评估地址栏和启动画面主题颜色的一致性。
  - **视口配置**：确保视口正确设置为响应式设计。
  - **用户参与度**：衡量提示用户将网络应用程序安装到主屏幕的能力。

#### Lighthouse 如何处理 JavaScript 执行？

[Lighthouse](../L/lighthouse.md) 通过 **无头 Chrome 浏览器** 处理 JavaScript 执行。当[Lighthouse](../L/lighthouse.md)审核启动时，它会以无头模式启动Chrome，这允许它像用户一样以编程方式与页面交互。 [Lighthouse](../L/lighthouse.md) 然后导航到目标 URL 并等待页面加载。
  在加载过程中，[Lighthouse](../L/lighthouse.md)**记录了页面上JavaScript的执行情况。这包括脚本的解析和执行时间，以及异步 JavaScript 任务完成所需的时间。 [Lighthouse](../L/lighthouse.md) 使用 Chrome DevTools 协议收集有关 JavaScript 执行的信息，其中包括：

- **脚本评估**：解析和编译脚本所花费的时间。
  - **任务执行**：执行脚本任务所花费的时间。
  - **JavaScript 启动时间**：页面变为交互式所需的时间，这对于理解用户体验至关重要。
  [Lighthouse](../L/lighthouse.md) 还会在必要时模拟用户交互，以触发可能与用户事件相关的 JavaScript 执行。这可确保审核捕获仅在交互时执行的脚本的性能影响。
  JavaScript 执行过程中收集的数据将用于多个 [Lighthouse](../L/lighthouse.md) 审计，例如：

- **首次内容绘制 (FCP)**
  - **交互时间 (TTI)**
  - **总阻塞时间 (TBT)**
  这些指标有助于评估 JavaScript 对页面加载性能和交互性的影响，这对于理解和改善用户体验至关重要。

- **脚本评估**：解析和编译脚本所花费的时间。
  - **任务执行**：执行脚本任务所花费的时间。
  - **JavaScript 启动时间**：页面变为交互式所需的时间，这对于理解用户体验至关重要。
  - **首次内容绘制 (FCP)**
  - **交互时间 (TTI)**
  - **总阻塞时间 (TBT)**

#### 使用 Lighthouse 时有哪些常见问题和解决方案？

[Lighthouse](../L/lighthouse.md) 的常见问题及其解决方案：

- **波动的分数**：由于网络条件、缓存状态或 CPU 限制，运行之间的分数可能会有所不同。 **解决方案**：多次运行 [Lighthouse](../L/lighthouse.md) 并取平均分数以确保一致性。
  - **大型资产**：未优化的图像或庞大的脚本可能会对性能产生负面影响。 **解决方案**：压缩图像，缩小CSS/JS，并使用延迟加载。
  - **第三方脚本**：外部脚本可能会降低您网站的速度。 **解决方案**：对已知主机使用`rel="preconnect"` 属性，推迟非关键脚本，或删除不必要的第三方脚本。
  - **缓存配置**：缓存配置不当可能会导致冗余数据获取。 **解决方案**：为静态资产设置适当的 `Cache-Control` 标头。
  - **可访问性问题**：[Lighthouse](../L/lighthouse.md) 可能会报告并非立即显而易见的可访问性问题。 **解决方案**：查看每个问题，查阅 WCAG 指南，并进行必要的 HTML/ARIA 调整。
  - **SEO 缺点**：缺少元标记或不正确的语义可能会影响 SEO 审核。 **解决方案**：确保正确使用语义 HTML 和元标记，例如 `description`、`viewport` 和结构化数据。
  - **渐进式 Web 应用程序标准**：[Lighthouse](../L/lighthouse.md) 可能表示缺少 PWA 功能。 **解决方案**：实施 Service Worker，创建 Web 应用程序清单，并确保您的应用程序通过 HTTPS 提供服务。
  - **超时或错误**：[Lighthouse](../L/lighthouse.md) 审核时可能会超时或遇到错误。 **解决方案**：检查服务器问题，确保没有浏览器扩展干扰，并以隐身模式运行审核。
  使用以下命令无头运行[Lighthouse](../L/lighthouse.md)，这有助于自动化环境中的一致性：

  ```
  lighthouse <url> --chrome-flags="--headless"
  ```请记住保持您的[Lighthouse](../L/lighthouse.md) 版本更新，以便从最新检查和[bug](../B/bug.md) 修复中受益。

- **波动的分数**：由于网络条件、缓存状态或 CPU 限制，运行之间的分数可能会有所不同。 **解决方案**：多次运行 [Lighthouse](../L/lighthouse.md) 并取平均分数以确保一致性。
  - **大型资产**：未优化的图像或庞大的脚本可能会对性能产生负面影响。 **解决方案**：压缩图像，缩小CSS/JS，并使用延迟加载。
  - **第三方脚本**：外部脚本可能会降低您网站的速度。 **解决方案**：对已知主机使用`rel="preconnect"` 属性，推迟非关键脚本，或删除不必要的第三方脚本。
  - **缓存配置**：缓存配置不当可能会导致冗余数据获取。 **解决方案**：为静态资产设置适当的 `Cache-Control` 标头。
  - **可访问性问题**：[Lighthouse](../L/lighthouse.md) 可能会报告并非立即显而易见的可访问性问题。 **解决方案**：查看每个问题，查阅 WCAG 指南，并进行必要的 HTML/ARIA 调整。
  - **SEO 缺点**：缺少元标记或不正确的语义可能会影响 SEO 审核。 **解决方案**：确保正确使用语义 HTML 和元标记，例如 `description`、`viewport` 和结构化数据。
  - **渐进式 Web 应用程序标准**：[Lighthouse](../L/lighthouse.md) 可能表示缺少 PWA 功能。 **解决方案**：实施 Service Worker，创建 Web 应用程序清单，并确保您的应用程序通过 HTTPS 提供服务。
  - **超时或错误**：[Lighthouse](../L/lighthouse.md) 在审核时可能会超时或遇到错误。 **解决方案**：检查服务器问题，确保没有浏览器扩展干扰，并以隐身模式运行审核。
