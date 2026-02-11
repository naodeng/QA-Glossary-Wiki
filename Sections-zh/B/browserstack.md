# BrowserStack

[BrowserStack](#browserstack)

### 相关术语：
- [跨浏览器测试工具](/glossary/cross-browser-testing-tool)

### 另请参阅：
- [官方网站](https://www.browserstack.com/)
- [维基百科](https://en.wikipedia.org/wiki/BrowserStack)

## 关于 BrowserStack 的问题？

#### 基础知识与重要性

- **什么是 BrowserStack？**

**BrowserStack** 是一个基于云的**跨浏览器测试平台**，它使开发人员和 QA 专业人员能够在各种浏览器、操作系统和真实移动设备上测试其网站和移动应用程序。它提供了对庞大浏览器和设备库的访问，从而消除了维护内部测试基础设施的需要。

使用 BrowserStack，你可以进行**交互式手动测试**，或使用 **Selenium**、**Appium** 和 **Cypress** 等流行框架运行**自动化测试**。它支持多种编程语言，包括 Java、Python 和 Ruby，允许无缝集成到现有的**测试套件**中。

设置 BrowserStack 涉及创建帐户、使用提供的访问凭据配置**测试脚本**，以及通过平台的云基础设施运行测试。你可以直接从 CI/CD 流水线启动测试，因为 BrowserStack 提供了与 Jenkins、Travis CI 和 CircleCI 等工具的集成。

对于移动端测试，BrowserStack 的 **App Live** 和 **App Automate** 功能支持对原生和混合移动应用进行测试。你可以上传应用构建版本并在真实设备上与其交互，或自动化测试过程。

BrowserStack 的**屏幕截图 (Screenshots)** 功能允许你捕获并比较多个浏览器和设备上的截图，从而促进**视觉回归测试**。

平台的 **Automate Pro** 计划提供了高级功能，如并行测试、IP 白名单和**优先级**支持，这可以显著加快测试过程并增强安全性。

总的来说，BrowserStack 简化了测试工作流，确保应用程序在所有用户触点上都能完美运行。

- **为什么 BrowserStack 对软件测试很重要？**

BrowserStack 对于**软件测试**至关重要，因为它具备**跨浏览器兼容性测试**能力。它允许测试人员在不需要内部设备实验室的情况下，验证应用程序是否能在众多浏览器和设备上无缝运行。随着用户环境多样性的不断增长（各种版本的浏览器和操作系统），这一点尤为重要。

通过提供对**真实设备和浏览器**的访问，BrowserStack 确保测试反映了实际的用户条件，与模拟器或仿真器相比，这能产生更准确的结果。这种真实的测试环境有助于发现那些仅在特定条件下出现、且无法通过仿真器重现的边缘情况和**缺陷 (bugs)**。

此外，BrowserStack 基于云的基础设施提供了可扩展性和灵活性。测试人员可以并行运行多个测试，显著减少了大型**测试套件**所需的时间。这对于追求快速**迭代**和持续交付的敏捷及 DevOps 团队至关重要。

该服务与 **CI/CD 流水线**及 Selenium 等流行自动化框架的集成能力增强了其重要性。它允许自动化回归测试成为构建过程的一部分，确保新的代码更改不会破坏现有功能。

最后，BrowserStack 的**安全特性**确保测试在安全的环境中进行，这对于处理敏感数据的企业来说是一个关键考量。这使其不仅成为功能测试的可靠工具，也适用于需要遵守严格安全标准的应用测试。

- **BrowserStack 的关键特性有哪些？**

BrowserStack 的关键特性包括：
- **跨浏览器测试**：在各种真实浏览器和操作系统上进行测试，无需维护内部实验室。
- **真实设备云**：访问大量真实移动设备，以获得更准确的测试结果。
- **本地测试**：通过本地测试功能安全地测试开发和分发（staging）环境。
- **并行测试**：同时运行多个测试以减少执行时间。
- **集成**：与 Jenkins、Travis CI 和 CircleCI 等流行 CI/CD 工具无缝集成。
- **交互式测试**：在桌面和移动设备上进行手动测试和调试。
- **自动化截图和视频**：自动捕获测试的截图和视频，用于视觉回归和文档记录。
- **地理位置测试**：模拟和测试基于地理位置的场景。
- **响应式测试**：评估 Web 应用程序在不同设备上的响应能力。
- **开发者工具 (DevTools)**：在桌面浏览器上使用 Chrome DevTools 进行调试和分析。
- **网络节流 (Network Throttling)**：在不同网络条件下测试应用程序。
- **企业级特性**：为企业需求提供 SSO、优先级支持、团队管理和使用分析。

```javascript
// 使用 Selenium WebDriver 在 BrowserStack 中启动并行测试会话的示例
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
    // 此处编写你的测试代码
  } finally {
    await driver.quit();
  }
}
runTest();
```

这些特性使 BrowserStack 成为 Web 和移动应用程序测试的多功能平台。

- **BrowserStack 如何提高软件测试质量？**

BrowserStack 通过提供**访问大量真实设备和浏览器**的机会，提升了**软件测试**质量。这种多样性确保了应用程序在紧密模拟最终用户环境的条件下进行测试，从而能够检测出测试模拟器或有限设备集时可能会遗漏的**边缘情况问题**。

借助**并行测试能力**，**测试套件**可以在多个环境中同时执行，显著减少了全面测试所需的时间，并加快了开发团队的反馈循环。

**本地测试**允许安全地测试开发和分发环境，确保应用程序在发布到生产环境前经过彻底审核。此特性对于识别环境特定的**缺陷 (bugs)** 至关重要。

BrowserStack 与 Jenkins 等流行 **CI/CD 工具的集成**以及对 Selenium 等框架的兼容性，使其能够无缝纳入自动化流水线。这种集成支持了对敏捷和 DevOps 工作流至关重要的**持续测试实践**。

该平台的**可靠性和可扩展性**确保了自动化测试的一致运行，减少了可能破坏对**自动化测试**流程信任的**误报 (false positives)**。此外，BrowserStack 诸如地理位置测试和多样化网络条件等**高级特性**，支持更细腻的测试场景，进一步提高了**测试覆盖率**和**质量保证**。

总之，BrowserStack 全面的设备和浏览器覆盖方案、并行测试、本地测试能力以及无缝集成，促成了一个更稳健、高效且可靠的测试过程，最终实现了更高质量软件的交付。

- **使用 BrowserStack 可以执行哪些类型的测试？**

使用 BrowserStack，**测试自动化**工程师可以执行各种测试，以确保不同设备和平台上的应用程序质量：
- **跨浏览器测试**：验证 Web 应用程序在多种浏览器及其版本上的功能和设计。
- **响应式设计测试**：检查 Web 应用程序如何适应不同的屏幕尺寸和分辨率。
- **回归测试**：在应用程序更改后自动重新运行**测试用例**，以确保现有功能不受影响。
- **性能测试**：使用 BrowserStack 的性能工具测量应用程序在各种条件下的响应能力和稳定性。
- **本地化测试**：在不同的地理设置中测试应用程序，以确保其在各种区域设置下表现正确。
- **无障碍测试**：使用 BrowserStack 确保残障用户能够访问应用程序，符合 WCAG 等标准。
- **交互式测试**：在大量真实设备上进行手动交互，以进行**探索性测试**。
- **视觉测试**：比较应用程序在不同设备和浏览器上的截图，以发现 UI 不一致。
- **自动化截图测试**：大规模捕获并比较截图，以验证应用程序的视觉方面。
- **移动应用测试**：在大量真实 iOS 和 Android 设备上测试原生和混合移动应用程序。
- **集成测试**：将 BrowserStack 与 CI/CD 流水线相结合，作为开发过程的一部分运行测试。

这些测试可以使用 Selenium、Appium、**Cypress** 等流行框架和工具执行，BrowserStack 支持这些工具与现有**测试套件**的无缝集成。

#### 功能与用法

- **BrowserStack 是如何工作的？**

BrowserStack 通过提供一个基于云的平台运作，用户可以在该平台上访问各种**真实设备**、**浏览器**和**操作系统**进行测试。当启动测试时，BrowserStack 会根据测试要求从其设备农场中分配一个虚拟机或真实设备。

对于**自动化测试**，你通常会使用 Selenium 或 Appium 等框架编写**测试脚本**，然后配置这些脚本使用提供的 **API** 和**访问密钥**与 BrowserStack 服务器通信。以下是一个使用 JavaScript 配合 WebDriverIO 和 Selenium 的简化示例：

```javascript
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
  // 在此处编写你的测试步骤
  await driver.deleteSession();
}

runTestOnBrowserStack();
```

脚本连接到 BrowserStack，后者随后启动指定的环境。测试运行起来就像在本地执行一样，但实际上是在 BrowserStack 服务器上运行的。这允许跨不同环境进行**并行测试**，显著加快了测试过程。

BrowserStack 的基础设施旨在处理测试环境的**设置、维护**和**清理 (teardown)**，这简化了测试工作流，使你能够专注于编写和执行测试。测试完成后，BrowserStack 会提供**详细日志**、**屏幕截图**和**视频录制**以帮助调试任何问题。

- **我该如何设置并开始使用 BrowserStack？**

要设置并开始使用 BrowserStack 进行**测试自动化**，请遵循以下步骤：
1. 如果还没有帐户，请**注册** BrowserStack 帐户。
2. 登录后，导航到 **Automate** 部分以访问自动化仪表板。
3. **配置你的测试脚本**以连接到 BrowserStack 的远程服务器。你需要在测试代码中设置 BrowserStack 的 URL 和访问凭据。使用 BrowserStack 帐户提供的用户名和访问密钥。

```javascript
const capabilities = {
  'browserName' : 'Chrome',
  'browserstack.user' : 'YOUR_USERNAME',
  'browserstack.key' : 'YOUR_ACCESS_KEY'
}
```

4. **选择所需的浏览器和操作系统**配置，在测试 capability 中指定它们。
5. 使用你偏好的**测试运行器**运行**测试脚本**。你的测试现在将在 BrowserStack 的远程浏览器/设备上执行。
6. 通过 BrowserStack Automate 仪表板实时**监控你的测试**，你可以在其中查看测试进度、视频录制、日志和截图。
7. 使用 BrowserStack 提供的详细报告**分析测试结果**并调试问题。

请记住保护好你的 BrowserStack 访问凭据，不要公开分享。对于持续集成，请使用环境变量存储 BrowserStack 用户名和访问密钥。与 Jenkins 等 CI 工具集成时，请添加 BrowserStack 插件或使用提供的 **API** 在构建过程中触发测试。

- **在 BrowserStack 上执行测试的步骤是什么？**

要在 BrowserStack 上执行测试，请遵循以下步骤：
1. **登录**你的 BrowserStack 帐户。
2. **选择**测试类型：Live、Automate、App Live 或 Screenshots & Responsive。
3. 对于 **Automate**：
   - **配置**你的测试脚本以使用 BrowserStack 的中心 (hub) URL 和所需的 capability。

```javascript
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

   - 从 IDE 或命令行**运行**测试脚本。
4. 对于 **Live 测试 (Live Testing)**：
   - **选择**浏览器、版本和操作系统。
   - **导航**到托管 Web 应用程序的 URL。
   - 手动与其**交互**以执行测试。
5. 对于 **App Live**：
   - **上传**移动应用或提供应用的公开 URL。
   - **选择**设备和操作系统版本。
   - 在所选设备上与应用**交互**。
6. 对于 **Screenshots & Responsive**：
   - **输入** Web 应用程序的 URL。
   - **选择**用于截图的浏览器和设备。
   - **生成**截图以审查不同设备和浏览器上的布局。

测试完成后，**审查**结果，根据测试类型可能包括视频录制、日志和截图。**分析**结果以识别任何问题或**缺陷 (bugs)**。

- **如何使用 BrowserStack 进行移动端测试？**

要使用 BrowserStack 进行移动端测试，请遵循以下步骤：
1. **登录**你的 BrowserStack 帐户。
2. 导航到 **App Live** 或 **App Automate** 部分，具体取决于你要进行手动还是**自动化测试**。
3. 对于 **App Live**：
   - 上传移动应用或提供公开 URL。
   - 选择要测试的设备和操作系统版本。
   - 通过浏览器在所选设备上与应用交互。
4. 对于 **App Automate**：
   - 确保你已准备好使用 Appium 或 Espresso 等框架编写的自动化脚本。
   - 配置测试脚本，使用提供的**访问密钥**和**用户名**连接到 BrowserStack。
   - 指定所需的 capability，包括设备和操作系统版本。
   - 运行测试脚本。它将在 BrowserStack 云端执行。

以下是 Appium 测试的示例代码片段：

```java
DesiredCapabilities capabilities = new DesiredCapabilities();
capabilities.setCapability("device", "iPhone 11 Pro Max");
capabilities.setCapability("os_version", "13");
capabilities.setCapability("realMobile", "true");
capabilities.setCapability("browserstack.user", "YOUR_USERNAME");
capabilities.setCapability("browserstack.key", "YOUR_ACCESS_KEY");

AppiumDriver driver = new AppiumDriver(new URL("http://hub.browserstack.com/wd/hub"), capabilities);
```

通过 **BrowserStack 仪表板 (BrowserStack Dashboard)** 监控测试结果，你可以在其中查看视频录制、日志和截图。

请记得将 `"YOUR_USERNAME"` 和 `"YOUR_ACCESS_KEY"` 替换为你真实的 BrowserStack 凭据。

- **BrowserStack 如何处理不同的浏览器和操作系统？**

BrowserStack 通过维护**庞大的真实设备和浏览器版本库存**来管理各种环境。当发起测试时，BrowserStack 会**分配**一个符合指定标准（如浏览器版本、操作系统和屏幕分辨率）的虚拟机或真实设备。

对于浏览器，BrowserStack 支持 **Chrome**、**Firefox**、**Safari**、**Internet Explorer** 和 **Edge** 的广泛版本。它还提供各类移动浏览器版本，以便在不同设备上进行测试。

对于操作系统，它包含 **Windows**、**macOS**、**iOS** 和 **Android** 平台，覆盖多个版本以确保跨不同环境的兼容性。

BrowserStack 利用**基于云的基础设施**提供对这些环境的访问，这意味着可以在浏览器和操作系统的多种组合中并行运行测试，而无需本地**设置**或维护。

为了指定所需的环境，测试人员在**测试脚本**中使用 capability。以下是 JavaScript 中使用 Selenium **WebDriver** 的示例：

```javascript
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

这种方法确保了应用程序在**紧密模拟用户条件的测试环境**中运行，从而产生更可靠的测试结果。

- **我可以使用 BrowserStack 进行自动化测试吗？**

当然可以，BrowserStack 可用于运行**自动化测试**。它提供一个云平台，允许你在多种浏览器和真实移动设备上运行自动化测试。首先，你需要配置你的**测试自动化**框架以连接 BrowserStack 远程服务器。

以下是一个在 JavaScript 中使用 Selenium **WebDriver** 的基础示例：

```javascript
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
    // 在此处添加你的测试逻辑
  } finally {
    await driver.quit();
  }
}

runTestOnBrowserStack();
```

将 `YOUR_USERNAME` 和 `YOUR_ACCESS_KEY` 替换为你的 BrowserStack 凭据。此代码设置了一个在 BrowserStack 基础设施上运行的 Selenium WebDriver 测试。

对于**持续集成**，你可以将 BrowserStack 与 **Jenkins**、**Travis CI** 或 **CircleCI** 等工具集成，以便在每次提交或拉取请求时自动运行测试。

BrowserStack 还支持其他测试框架，如用于**移动应用测试**的 Appium，以及用于更专门测试场景的 **Cypress**、Playwright 或 Espresso。与这些工具的集成遵循类似的模式：配置你的测试以与 BrowserStack 远程服务器通信。

#### 集成与兼容性

- **BrowserStack 如何与其他测试工具集成？**

BrowserStack 可以与各种测试工具集成，以增强自动化并简化工作流。以下是与一些常用工具集成的方法：

- **Appium**：使用 BrowserStack 的 Appium 服务器进行**移动应用测试**。在 Appium 客户端中将 `remote_url` 设置为带有访问凭据的 BrowserStack 端点。

```java
DesiredCapabilities caps = new DesiredCapabilities();
caps.setCapability("browserstack.user", "YOUR_USERNAME");
caps.setCapability("browserstack.key", "YOUR_ACCESS_KEY");
// 其他 capability
AppiumDriver driver = new AppiumDriver(new URL("http://hub-cloud.browserstack.com/wd/hub"), caps);
```

- **Cypress**：对于 **Cypress** 集成，安装 BrowserStack 的 CLI 工具并使用 `browserstack-cypress` 命令在 BrowserStack 上运行测试。

```bash
npm install -g browserstack-cypress-cli
browserstack-cypress run
```

- **TestCafe**：通过使用 BrowserStack 插件集成 TestCafe。在 `.testcaferc.json` 文件中配置你的 BrowserStack 凭据和所需的 capability。

```json
{
  "browsers": "browserstack:chrome",
  "browserstack": {
    "username": "YOUR_USERNAME",
    "accessKey": "YOUR_ACCESS_KEY"
  }
}
```

- **JUnit**：对于 JUnit 集成，配置你的测试连接到 BrowserStack 的 Selenium 网格，使用 `RemoteWebDriver` 和所需的 capability。

```java
DesiredCapabilities caps = new DesiredCapabilities();
caps.setCapability("browserstack.user", "YOUR_USERNAME");
caps.setCapability("browserstack.key", "YOUR_ACCESS_KEY");
// 其他 capability
WebDriver driver = new RemoteWebDriver(new URL("http://hub-cloud.browserstack.com/wd/hub"), caps);
```

- **GitHub Actions**：使用 BrowserStack 的 GitHub Action 设置 CI/CD 流水线。将该 Action 添加到工作流文件中并配置 BrowserStack 凭据。

```yaml
- name: BrowserStack Action
  uses: browserstack/github-actions@master
  with:
    username: ${{ secrets.BROWSERSTACK_USERNAME }}
    access-key: ${{ secrets.BROWSERSTACK_ACCESS_KEY }}
```

这些集成允许你在现有的**测试自动化**生态系统中使用 BrowserStack 的基础设施，从而促进跨浏览器和跨平台的测试。

- **BrowserStack 是否兼容持续集成工具？**

是的，**BrowserStack** 兼容器各种**持续集成 (CI)** 工具。它提供的插件和集成支持与 CI 系统的无缝协作，使自动化测试能够作为构建过程的一部分运行。这种兼容性确保了测试是开发周期中不可或缺的一部分，有助于及早发现问题并维持**软件质量**。

例如，BrowserStack 通过插件与 **Jenkins** 集成，允许你直接从 Jenkins 构建过程中触发 BrowserStack 测试。同样，它通过可用插件或在 CI 配置中使用自定义脚本，支持 **Travis CI**、**CircleCI**、**GitLab CI** 和 **Bitbucket Pipelines** 等其他 CI 工具。

要将 BrowserStack 与 CI 工具集成，你通常需要添加 BrowserStack 访问凭据并配置**测试脚本**以与 BrowserStack **API** 通信。以下是如何使用环境变量进行身份验证，配合 CI 工具设置 BrowserStack 的示例：

```bash
export BROWSERSTACK_USERNAME="your_username"
export BROWSERSTACK_ACCESS_KEY="your_access_key"
```

然后，你可以运行包含 BrowserStack capability 的测试命令。此命令的具体形式取决于你使用的测试框架和语言。

通过将 BrowserStack 与 CI 工具集成，你可以实现跨浏览器和跨平台测试的自动化，确保每次提交或构建都经过验证，从而以最小的手动干预维持高质量标准。

- **我可以在 Selenium 中使用 BrowserStack 吗？**

当然可以，**BrowserStack** 可以与 **Selenium** 配合运行自动化浏览器测试。要在 Selenium 中集成 BrowserStack，请遵循以下步骤：
1. **设置环境**：
   - 确保为你喜欢的编程语言安装了 Selenium **WebDriver**。
   - 安装必要的语言特定绑定。
2. **配置测试脚本**：
   - 从 Selenium 导入 WebDriver 和 `DesiredCapabilities` 模块。
   - 定义你的 BrowserStack 凭据和所需的 capability，包括要测试的浏览器、浏览器版本和操作系统。
3. **初始化远程 WebDriver**：
   - 将 WebDriver 指向包含访问凭据的 BrowserStack 远程 URL。
4. **编写测试用例**：
   - 使用与本地浏览器测试相同的 Selenium 命令。

以下是 Java 中的一个基础示例：

```java
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
    // 此处编写你的测试代码
    driver.quit();
  }
}
```

将 `your_browserstack_username` 和 `your_browserstack_accesskey` 替换为你的 BrowserStack 凭据。根据你的测试需求调整 capability。

- **BrowserStack 如何与 Jenkins 集成？**

BrowserStack 通过其 **BrowserStack Jenkins Plugin** 与 Jenkins 集成。该插件允许你直接从 Jenkins 界面在 BrowserStack 的基础设施上运行自动化测试。要设置集成，请遵循以下步骤：
1. 从 Jenkins 插件管理器安装 **BrowserStack Jenkins Plugin**。
2. 通过导航到 Jenkins 系统配置页面，配置插件的 **Access Key** 和 **Username**。
3. 在你的 Job 配置中，添加一个构建步骤或构建后操作来**在 BrowserStack 上运行自动化测试**。
4. 定义你的测试配置，包括要测试的浏览器和设备。
5. 使用 **BrowserStackLocal** 二进制文件，通过安全隧道测试内部、私有或分发环境。
6. 启动 Jenkins 构建，插件将自动在 BrowserStack 上触发测试。

以下是你可能配置 Jenkins Job 使用 BrowserStack 的示例：

```groovy
pipeline {
    agent any
    stages {
        stage('Test') {
            steps {
                script {
                    // 设置 BrowserStack 凭据
                    def browserStackCredentials = withCredentials([usernamePassword(credentialsId: 'BROWSERSTACK_CREDENTIALS', passwordVariable: 'BROWSERSTACK_ACCESS_KEY', usernameVariable: 'BROWSERSTACK_USERNAME')]) {
                        // 在 BrowserStack 上运行测试
                        sh 'mvn test -DBrowserStack_Username=$BROWSERSTACK_USERNAME -DBrowserStack_AccessKey=$BROWSERSTACK_ACCESS_KEY'
                    }
                }
            }
        }
    }
}
```

该插件还为 BrowserStack 凭据提供**环境变量**，可在**测试脚本**中使用。测试执行后，可在 BrowserStack Automate 仪表板上看到结果和视频录制。Jenkins 也将显示结果，方便直接从 CI 流水线追踪测试的成功与失败。

- **还有哪些其他工具和框架可以与 BrowserStack 配合使用？**

BrowserStack 可以集成多种**测试自动化工具和框架**。以下是一些值得关注的：
- **Appium**：对于移动应用程序测试，你可以配合 BrowserStack 使用 Appium 在各种真实设备上运行自动化测试。

```java
browserstackUser = "YOUR_USER";
browserstackKey = "YOUR_KEY";

desiredCapabilities.setCapability("browserstack.user", browserstackUser);
desiredCapabilities.setCapability("browserstack.key", browserstackKey);
```

- **Cypress**：BrowserStack 支持 **Cypress** 测试，允许你跨多个浏览器和操作系统运行它们。
- **TestCafe**：你可以在 BrowserStack 上运行 TestCafe 脚本，利用其**跨浏览器测试**能力。
- **Espresso**：对于 Android 应用测试，Espresso 测试可以在 BrowserStack 的真实设备云中执行。
- **XCTest**：同样支持针对 iOS 应用的 XCTest 框架，支持在各类 Apple 设备上进行测试。
- **Puppeteer**：BrowserStack 支持使用 Puppeteer 进行无头（headless）浏览器测试，适用于快速反馈。
- **Playwright**：集成 Playwright 测试在 BrowserStack 上运行，从而跨所有浏览器测试现代 Web 应用。
- **GitHub Actions**：通过集成 BrowserStack 与 GitHub Actions 实现工作流自动化，进行持续测试。
- **Bitbucket Pipelines**：在 Bitbucket Pipelines CI/CD 过程中将测试在 BrowserStack 中运行。
- **TeamCity**：与 TeamCity 集成，随构建自动触发 BrowserStack 测试。
- **Visual Studio Team Services**：将 VSTS 流水线连接到 BrowserStack，作为发布过程的一部分运行自动化测试。

这些集成有助于利用 BrowserStack 的设备和浏览器覆盖方案，使其成为全面**自动化测试**的多功能选择。

#### 高级特性

- **BrowserStack 的高级特性有哪些？**

BrowserStack 为资深**测试自动化**工程师提供了一系列高级特性：
- **本地测试**：通过在 BrowserStack 和本地机器之间建立安全隧道，安全地测试受防火墙保护或位于 localhost 的开发和分发环境。
- **并行测试**：通过在不同浏览器、设备和操作系统上同时运行多个测试来加快**测试执行**速度。
- **地理位置测试**：模拟不同地理位置的网站和应用性能，确保全球用户获得一致体验。
- **真实设备云**：访问大量真实移动设备以获得更准确的测试结果，而非使用仿真器或模拟器。
- **视觉回归测试**：通过比较不同时间的截图，自动检测视觉回归。
- **网络节流**：在 3G、4G、LTE 和 Wi-Fi 等各种网络条件下测试应用，了解其性能和用户体验。
- **交互式调试**：在 Live 测试会话期间使用断点和控制台日志等工具，实时识别并解决问题。
- **集成开发者工具**：在远程设备上访问浏览器开发者工具进行深度调试。
- **自动化移动端应用测试**：使用 Appium、Espresso 和 XCUITest 框架在原生和混合移动端应用上运行自动化测试。
- **企业级特性**：针对大型组织的定制解决方案，包括单点登录 (SSO)、团队管理和**优先级**支持。

要利用这些特性，工程师可以将相关的 BrowserStack capability 纳入现有的**测试自动化**框架中，使用提供的 **API** 和 CLI 工具。例如，要启用本地测试，请使用 BrowserStackLocal 二进制文件：

```bash
BrowserStackLocal --key YOUR_ACCESS_KEY
```

对于并行测试，配置**测试脚本**以启动具有不同配置的多个会话：

```json
"browsers": [
  { "browser": "chrome", "browser_version": "latest", "os": "Windows", "os_version": "10" },
  { "browser": "firefox", "browser_version": "latest", "os": "OS X", "os_version": "Catalina" }
]
```

这些特性旨在提高测试效率、准确性和覆盖范围，确保应用程序在所有用户触点上都能表现最优。

- **BrowserStack 中的“Live 测试”特性是如何运作的？**

BrowserStack 中的 **Live 测试**特性允许你在不同的浏览器和设备上交互式地测试你的网站或应用，而无需搭建实际的服务端**测试环境**。它在平台的云基础设施上提供实时浏览器会话，使你能够像使用本地设备或浏览器一样，手动导航并测试 Web 应用程序的功能。

要使用 Live 测试：
1. 登录你的 BrowserStack 帐户。
2. 导航到 **Live** 部分。
3. 选择所需的**浏览器**、**浏览器版本**和**操作系统**。
4. 输入你要测试的网站或 Web 应用的 **URL**。
5. 点击**开始会话 (Start Session)** 以发起 Live 测试会话。

在会话期间，你可以与网站或应用交互，测试布局、功能并实时调试问题。你还可以在不同浏览器和设备之间快速切换，测试跨浏览器兼容性。

Live 测试还提供了调试工具，如**控制台日志**、**网络分析日志**，以及在会话期间进行**屏幕截图**或**视频录制**的能力。这些特性有助于在测试过程中识别并记录出现的问题。

请记住，Live 测试是专为**手动测试**设计的。对于**自动化测试**，你应该使用 BrowserStack 的 Automate 特性或其他**自动化测试**集成方案。

- **BrowserStack 中的“Automate Pro”是什么？**

Automate Pro 是 BrowserStack 的高级产品，专为**企业级测试自动化**需求量身定制。与标准 Automate 计划相比，它提供了**高级特性**和**增强能力**。

通过 Automate Pro，用户可以访问**无限制的并行测试运行**，这显著减少了运行大型**测试套件**所需的时间。对于具有高测试需求且需要扩展自动化工作的组织来说，这尤其有益。

此外，Automate Pro 还包含**优先级支持**，以确保任何问题都能得到及时处理，最大限度地减少停机时间。用户还受益于**独家特性**，如用于增加安全性和便利性的**单点登录 (SSO)**，以及用于控制访问并遵守公司网络策略的 **IP 白名单**。

对于专注于**测试覆盖率**的团队，Automate Pro 提供**真实设备测试**，以确保应用程序在实际移动设备（而不仅仅是模拟器或仿真器）上无缝运行。这对于在当今以移动设备为中心的世界中提供高质量的用户体验至关重要。

为了满足大型组织的需求，Automate Pro 还提供**团队管理能力**，允许分布式测试团队之间更好的协调与协作。这包括**基于角色的访问控制**和用于有效管理资源的**团队使用洞察**等功能。

简而言之，Automate Pro 旨在通过在 BrowserStack 中提供更稳健、特性更丰富的**测试自动化**环境，支持大型企业复杂且广泛的测试需求。

- **我该如何使用 BrowserStack 中的“App Live”特性？**

要使用 BrowserStack 中的 **App Live** 特性，请遵循以下步骤：
1. 登录你的 BrowserStack 帐户。
2. 导航到 **App Live** 部分。
3. **上传**移动应用二进制文件：
   - 对于 iOS，上传 `.ipa` 文件。
   - 对于 Android，上传 `.apk` 文件。
4. 上传后，从可用 iOS 和 Android 设备列表中选择**所需的设备**。
5. 在所选设备上**启动**应用。BrowserStack 将实例化一个真实设备会话。
6. 在浏览器窗口中实时与应用**交互**。
7. 使用**工具栏**执行旋转、摇晃、截屏和设置地理位置等操作。
8. 通过查看日志、视频录制和其他数据**调试**你的应用。
9. 如果需要测试内部服务器或开发环境，配合**本地测试**功能集成你的本地开发环境。

对于应用的**自动化测试**，请切换到 BrowserStack 的 **Automate** 部分，并按照你所选框架（如 Appium 或 Espresso）的相关步骤操作。

请记住，App Live 是专为**手动交互测试**设计的。对于自动化测试，请使用 BrowserStack 的 Automate 或 Automate Pro 特性。

- **BrowserStack 中的“Screenshots”特性是什么？**

BrowserStack 中的 **Screenshots** 特性是一个工具，允许用户跨不同浏览器和操作系统捕获并保存网页图像。这对于**视觉回归测试**特别有用，在这种测试中，你需要确保你的 Web 应用程序在多个浏览器环境中外观和功能都正确。

要使用 Screenshots 特性，你需要指定要测试网页的 URL，以及一组浏览器和系统组合。BrowserStack 随后会生成该页面在所选浏览器和设备上的外观截图。这些截图可以手动审查，或使用第三方工具以编程方式进行比较，以检测视觉差异。

以下是如何使用 JavaScript 触发 Screenshots **API** 的基础示例：

```javascript
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
      // 根据需要添加更多浏览器/系统组合
    ]
  })
};

request(options, function (error, response, body) {
  if (error) throw new Error(error);
  console.log(body);
});
```

此特性对于快速识别 UI 问题至关重要，无需进行手动的**跨浏览器测试**，从而节省了时间和资源。截图也可以分享给团队成员或利益相关者，以提供测试结果的视觉证据。
