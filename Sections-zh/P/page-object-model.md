# 页面对象模型 (Page Object Model)
[Page Object Model](#page-object-model) [页面对象模型 (Page Object Model)](/wiki/page-object-model)

### 相关术语：
- Web 自动化 (Web Automation)
- Selenium IDE
- WebDriver

## 关于页面对象模型的常见问题？

#### 基础与重要性
- **什么是自动化测试中的页面对象模型 (POM)？**
  页面对象模型 (Page Object Model, POM) 是自动化测试中的一种设计模式，它将 Web 页面的属性和行为封装在一个类中。每个页面类作为 Web 页面的接口，所有与该页面的交互都通过页面对象进行，从而隐藏了底层的 Selenium 调用。
  **Java 示例（使用 Selenium）**：
  ```java
  public class LoginPage {
      private WebDriver driver;
      private By usernameLocator = By.id("username");
      private By passwordLocator = By.id("password");
      private By loginButtonLocator = By.id("login");

      public LoginPage(WebDriver driver) {
          this.driver = driver;
      }

      public void enterUsername(String username) {
          driver.findElement(usernameLocator).sendKeys(username);
      }

      public void enterPassword(String password) {
          driver.findElement(passwordLocator).sendKeys(password);
      }

      public void clickLoginButton() {
          driver.findElement(loginButtonLocator).click();
      }
  }
  ```
  在此模型中，测试脚本与页面对象交互，而不是直接操作 Web 元素。这种抽象减少了代码重复并提高了**可维护性**。当页面发生变化时，只需更新页面对象，而无需修改与其交互的所有测试用例。

- **为什么页面对象模型被认为是自动化测试的最佳实践？**
  它显著提升了**测试维护效率**并**减少了代码冗余**。通过将页面信息与实际测试分离，它实现了**关注点分离**。此外，POM 促进了代码的**组织性**和**可读性**，使测试用例更易于理解。它还便于团队协作，并能与 Singleton（单例）或 Factory（工厂）模式集成，增强框架的扩展性。

- **使用 POM 的好处有哪些？**
  - **可维护性**：UI 变化只需在页面类中修改一次。
  - **可读性**：动作与断言分离，逻辑清晰。
  - **复用性**：页面方法可在多个测试中重复使用。
  - **稳定性**：通过集中管理定位器减少了测试的脆弱性（Flakiness）。
  - **易于报告**：页面动作对应的方法名使生成的日志更具语义化。
  - **扩展性**：支持在大规模测试套件中轻松添加新页面。

#### 实施步骤
- **如何在 Selenium 中实施 POM？**
  1. **识别元素**：使用 ID、Name、XPath 等定位器。
  2. **创建类**：每个页面对应一个类。
  3. **声明变量**：将元素定位器设为类私有成员。
  4. **初始化**：通过构造函数或 `PageFactory.initElements()` 初始化。
  5. **编写公共方法**：封装点击、输入、获取文本等操作。
  6. **返回实例**：涉及页面跳转的方法应返回新页面的对象实例。

#### 关键组件
- **定位器 (Locators)**：存储查找元素的方式。
- **构造函数 (Constructor)**：初始化对象并确保页面处于预期状态。
- **Web 元素 (WebElements)**：页面的元素表示（建议私有，确保封装）。
- **动作 (Actions)**：模拟用户交互的方法。
- **断言 (Assertions)**：验证页面状态的方法。
- **导航方法 (Navigation Methods)**：处理页面间的转场。

#### 进阶概念
- **动态元素处理**：使用显示等待 (Explicit Waits)、动态选择器、正则表达式或 JavaScript 执行来处理不规则元素。
- **Page Factory**：使用 `@FindBy` 注解简化元素定义，并提供延迟加载特性。
- **模式集成**：
  - **Singleton**：管理浏览器会话（WebDriver 实例）。
  - **Factory**：根据需要动态生成不同类型的页面对象。
- **多窗口/框架处理**：为每个窗口或 `iframe` 创建独立的页面对象，并在操作前通过 `driver.switchTo()` 切换上下文。
- **抽象 (Abstraction) 的作用**：将复杂的 UI 机械操作（如何定位）与高层业务逻辑（做什么）分离，使测试通过“领域特定语言”风格进行编写。
