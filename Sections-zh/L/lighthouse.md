# Lighthouse
[Lighthouse](#lighthouse) [Lighthouse](/wiki/lighthouse) [Lighthouse](/wiki/lighthouse)
### 参见 (See also):
- Wikipedia
[Wikipedia](https://en.wikipedia.org/wiki/Google_Lighthouse)
## 关于 Lighthouse 的常见问题

#### 基础与重要性
- **什么是 Lighthouse？**
  **Lighthouse** 是一款**开源、自动化**的网页质量提升工具。它可以运行在任何网页上，无论是公开页面还是需要身份验证的页面。Lighthouse 针对性能、无障碍性 (Accessibility)、渐进式网页应用 (PWA)、SEO 等进行审计，提供对网页质量和有效性的全面评估。
  在 **Chrome** 中使用 Lighthouse：导航到要审计的页面，打开 **DevTools (开发者工具)**，点击 **Lighthouse** 标签。选择要运行的审计项，然后点击 **Generate report (生成报告)** 按钮。Lighthouse 对页面运行选定的审计，然后生成一份关于页面表现的报告。
  对于**自动化测试**，Lighthouse 可以集成到**持续集成 (CI)** 系统中。它可以作为 Node 模块、命令行工具或以编程方式作为自定义构建流程的一部分运行。**Lighthouse CI** 是一组专门的命令，使在持续集成中使用 Lighthouse 变得更加容易。
  得分是基于性能指标和启发式算法计算的。每个指标独立评分，然后组合成总分。提升较低的 Lighthouse 分数需要根据报告提供的具体反馈进行优化，这可能包括优化图像、压缩 CSS 和 JavaScript、实现延迟加载、改进无障碍功能等。
  在 **JavaScript 执行**方面，即使在高性能桌面机器上运行，Lighthouse 也会模拟中端设备，以创建一致的真实环境条件。使用 Lighthouse 时的常见问题包括性能指标波动，这可以通过多次运行审计并取中值来缓解。

- **为什么 Lighthouse 在软件自动化中很重要？**
  Lighthouse 在软件**测试自动化**中至关重要，因为它能够将**性能和质量检查集成**到开发和部署流水线中。它通过提供针对性能、无障碍、PWA、SEO 和最佳实践的**自动化审计**，确保维护高质量的 Web 应用。
  通过将 Lighthouse 纳入**自动化测试**，工程师可以确保任何代码更改都经过这些指标的评估，从而在开发周期早期发现性能退化或问题。这对于**持续集成 (CI)** 和**持续部署 (CD)** 环境尤为重要，因为自动化测试必须对代码更改的潜在影响提供快速反馈。
  Lighthouse 的作用还延伸到**性能预算 (Performance Budgeting)**，帮助团队设定并遵守性能目标。它可以**无头 (Headless)** 运行，适用于**服务端自动化**和 CI/CD 流水线集成。其**可配置性**允许针对特定需求自定义审计，其**评分系统**为站点的质量属性提供了量化衡量。
  此外，Lighthouse 的报告提供了可操作的建议，这对寻求优化 Web 应用的工程师极具价值。自动化这些审计并将其集成到开发工作流中，使 Lighthouse 成为高效改进 Web 应用质量和用户体验的重要工具。

- **Lighthouse 的主要功能有哪些？**
  - **性能指标 (Performance Metrics)**：提供详细指标，如 First Contentful Paint (FCP)、Speed Index、Largest Contentful Paint (LCP)、Time to Interactive (TTI)、Total Blocking Time (TBT) 和 Cumulative Layout Shift (CLS)。
  - **无障碍审计 (Accessibility Audits)**：根据 Web 内容无障碍指南 (WCAG) 评估页面，并建议改进措施。
  - **最佳实践 (Best Practices)**：检查开发是否遵循最佳实践，如 HTTPS 使用、正确的图像宽高比、避免使用已废弃的 **API** 等。
  - **SEO 审计**：评估影响搜索引擎排名的元素，包括 meta 标签、hreflang 标签和描述性链接文本。
  - **PWA 评估**：验证 PWA 的各个方面，确保满足可靠性、性能和参与度标准。
  - **自定义审计 (Custom Audits)**：开发人员可以编写自定义审计来检查特定的项目要求或标准。
  - **命令行 (CLI) 和编程 API**：可通过命令行或 **API** 运行，便于集成到自动化工作流中。
  - **可配置性**：可配置审计类别、节流 (Throttling) 设置和其他运行选项。
  - **报告功能**：生成包含分类评分、详细说明和改进建议的报告。
  - **扩展性**：开源且可定制，与 Lighthouse CI 等工具集成进行持续测试。

- **Lighthouse 与其他性能审计工具有何不同？**
  Lighthouse 的独特之处在于其与 **Chrome 开发者工具的深度集成**，以及对核心网页指标 (**Core Web Vitals**) 等用户体验指标的强调。虽然像 WebPageTest 这样的工具提供了详细的瀑布图和网络信息，但 Lighthouse 更侧重于提供涵盖性能、无障碍、最佳实践、SEO 和 PWA 指标的**全方位视角**。
  与一些需要复杂**设置 (Setup)** 或服务端集成的工具不同，Lighthouse **易于访问**，可以在命令行、Node 模块或直接在浏览器中运行，非常灵活。
  Lighthouse 提供包含清晰评分和建议的**操作报告**，指引开发人员改进性能。特别是在模拟移动网络和中端设备加载页面方面表现出色，这是许多其他工具未涵盖的**用例 (Use case)**。
  作为由 Google 维护的**开源**项目，它能定期更新以反映最新的 Web 标准，不像某些私有工具可能透明度不足。
  最后，其通过 Lighthouse CI 集成到 **CI/CD 流水线**的能力，使其成为发布前确保性能达标的强大工具。

- **Lighthouse 执行哪些类型的审计？**
  Lighthouse 在**五个类别**中执行审计：**性能 (Performance)**、**无障碍 (Accessibility)**、**最佳实践 (Best Practices)**、**SEO** 和 **PWA**。
  - **性能**：评估 FCP、Speed Index 等指标，关注用户感知的加载体验和交互性。
  - **无障碍**：检查可能阻碍用户访问内容的问题，如图像缺失 alt 文本、不当的 ARIA 属性和非语义化 HTML。
  - **最佳实践**：寻找现代开发实践，包括 HTTPS、正确的图像比例、避免废弃 **API**。
  - **SEO**：评估影响搜索可见性的元素，如 meta 描述、hreflang 链接、字体大小。
  - **PWA**：验证 Service Worker、Web App Manifest 以及离线功能等 PWA 标准。
  每个审计都提供反馈和分值，并可通过配置进行扩展或自定义。

#### 使用与实现
- **如何在 Chrome 中使用 Lighthouse 进行自动化测试？**
  1. 按 `Ctrl+Shift+I` (Mac 为 `Cmd+Option+I`) 打开 Chrome 开发者工具。
  2. 导航到 **Lighthouse** 标签。
  3. 选择审计类别（性能、无障碍等）。
  4. 选择设备类型（移动或桌面）。
  5. 点击 **Generate report (生成报告)**。
  以编程方式使用 **Node.js** 的示例：
  ```javascript
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
  };

  runLighthouse('https://example.com', options)
    .then(results => console.log(results))
    .catch(err => console.error(err));
  ```
  对于持续集成，可以使用 **Lighthouse CI** 运行审计并进行断言。

- **如何将 Lighthouse 用于自动化测试？**
  通过 **CLI** 或 **Node 模块**集成。
  **CLI 方式：**
  ```bash
  npm install -g lighthouse
  lighthouse https://example.com --output=json --output-path=./report.json --chrome-flags="--headless"
  ```
  **持续集成：**
  使用 **Lighthouse CI**。设置 `.lighthouserc.js` 配置文件并运行：
  ```bash
  lhci autorun --config=.lighthouserc.js
  ```
  这确保了代码提交或 PR 不会降低应用质量。

#### 结果与解读
- **Lighthouse 分数是如何计算的？**
  分数基于五个类别的审计。**性能**分数受 FCP、LCP、TTI、TBT 和 CLS 等速度指标的加权影响，反映加载、交互和视觉稳定性。**无障碍**检查 HTML 元素、ARIA、对比度。**最佳实践**来自 HTTPS、API 废弃检查。**SEO** 评估 meta 标签、字体大小。**PWA** 评估 Service Worker 和响应式设置。每个类别分数是审计项的加权平均值，由于性能在用户体验中占比大，通常具有最高权重。

- **如何解读 Lighthouse 报告？**
  - **性能**：关注 FCP、LCP、TTI、TBT 和 CLS。
  - **无障碍**：审查 alt 文本、ARIA、语义化 HTML。
  - **最佳实践**：检查安全性、HTTPS 和废弃 API。
  - **SEO**：检查移动端友好度、元数据。
  - **PWA**：评估响应式设计和离线模式。
  报告提供 0-100 的**得分**、**颜色编码指标**（绿色为优，橙色待改进，红色为差）以及**可操作建议**。建议优先处理**红色**项，再处理**橙色**，最后是**绿色**以微调性能。

#### 高级概念
- **什么是 Lighthouse CI？**
  它是一个开源自动化工具，可与 CI 系统集成，在每次 commit 时运行审计，针对性能、SEO 等提供即时反馈。工作流程包括：安装 `@lhci/cli`、配置 `.lighthouserc.js`、运行 `lhci autorun`、定义断言（若不达标则使构建失败）以及上传报告。

- **如何使用 Lighthouse 进行性能预算？**
  性能预算是对影响性能的指标（如图像、脚本大小）设定的限制。
  步骤：
  1. **定义预算**：确定最大加载时间、脚本大小等。
  2. **创建配置**：在 JSON 中指定约束。
  ```json
  {
    "extends": "lighthouse:default",
    "settings": {
      "budgets": [{
        "resourceSizes": [
          { "resourceType": "script", "budget": 125 },
          { "resourceType": "total", "budget": 300 }
        ]
      }]
    }
  }
  ```
  3. **运行审计**：`lighthouse https://example.com --budget-path=./budget.json`。
  报告中会指示站点是否符合预算。

- **Lighthouse 如何处理 JavaScript 执行？**
  它通过运行在**无头 (Headless) 模式**下的 Chrome 浏览器来处理。Lighthouse 记录脚本解析、编译和执行的时间。利用 Chrome DevTools Protocol，它收集脚本评估、任务执行和 JS 启动时间。它还会模拟用户交互以触发特定脚本，这些数据直接影响 FCP、TTI 和 TBT 等核心指标。

#### 常见问题与解决方案
- **分数波动**：受网络和 CPU 节流影响。**方案**：多次运行并取平均值。
- **资源过大**：图像或脚本臃肿。**方案**：压缩图像、Minify CSS/JS、延迟加载。
- **第三方脚本慢**：**方案**：使用 `rel="preconnect"`，异步加载或移除不必要的脚本。
- **缓存配置不当**：导致重复获取。**方案**：设置 `Cache-Control` 响应头。
- **超时或报错**：检查服务器、禁用扩展、使用隐身模式运行。建议使用 `--chrome-flags="--headless"`。
