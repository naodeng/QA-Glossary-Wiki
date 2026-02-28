# 页面对象模型

<!-- TOC START -->
- [相关术语：](#相关术语：)
- [有关页面对象模型的问题吗？](#有关页面对象模型的问题吗？)
  - [基础知识和重要性](#基础知识和重要性)
    - [自动化测试中的页面对象模型是什么？](#自动化测试中的页面对象模型是什么？)
    - [为什么页面对象模型被认为是自动化测试中的良好实践？](#为什么页面对象模型被认为是自动化测试中的良好实践？)
    - [使用页面对象模型有哪些好处？](#使用页面对象模型有哪些好处？)
    - [页面对象模型如何提高测试代码的可维护性？](#页面对象模型如何提高测试代码的可维护性？)
    - [Selenium 中的页面对象模型是如何实现的？](#selenium-中的页面对象模型是如何实现的？)
    - [页面对象类的关键组件是什么？](#页面对象类的关键组件是什么？)
    - [如何处理页面对象模型中的动态元素？](#如何处理页面对象模型中的动态元素？)
    - [如何在页面对象模型中使用页面工厂类？](#如何在页面对象模型中使用页面工厂类？)
  - [高级概念](#高级概念)
    - [页面对象模型如何与单例或工厂等其他设计模式一起使用？](#页面对象模型如何与单例或工厂等其他设计模式一起使用？)
    - [如何在页面对象模型中处理页面导航？](#如何在页面对象模型中处理页面导航？)
    - [页面对象模型中抽象的作用是什么？](#页面对象模型中抽象的作用是什么？)
    - [如何使用页面对象模型处理多个窗口或框架？](#如何使用页面对象模型处理多个窗口或框架？)
<!-- TOC END -->

这

页面对象模型

(POM) 是一种设计模式，它将 Web 元素合并到对象存储库中，从而提高代码可重用性并简化测试维护。

## 相关术语：

- [Web Automation](../W/web-automation.md)
- [Selenium IDE](../S/selenium-ide.md)
- [WebDriver](../W/webdriver.md)

## 有关页面对象模型的问题吗？

### 基础知识和重要性

#### 自动化测试中的页面对象模型是什么？

**[Page Object Model](../P/page-object-model.md) (POM)** 是自动化测试中的一种设计模式，它将网页的属性和行为封装在一个类中。每个页面类都充当网页的接口，与该页面的所有交互都通过页面对象，隐藏底层的 [Selenium](../S/selenium.md) 调用。
  下面是使用 [Selenium](../S/selenium.md) 的 Java 基本示例：

  ```
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
  ```在此模型中，测试与页面对象交互，而不是直接与 Web 元素交互。这种抽象减少了代码重复并改进了[maintainability](../M/maintainability.md)。当页面更改时，仅需要更新页面对象，而不需要更新与其交互的测试。
  要与页面对象交互，测试将使用对 [WebDriver](../W/webdriver.md) 的引用来实例化页面对象，并使用其方法来执行操作：

  ```
  LoginPage loginPage = new LoginPage(driver);
  loginPage.enterUsername("user");
  loginPage.enterPassword("pass");
  loginPage.clickLoginButton();
  ```通过遵循此模式，测试变得更具可读性，并且能够适应 Web 应用程序 UI 中的更改。

#### 为什么页面对象模型被认为是自动化测试中的良好实践？

[Page Object Model](../P/page-object-model.md) (POM) 被认为是自动化测试中的良好实践，因为它**增强了测试维护**并**减少了代码重复**。通过将页面信息与实际测试分开，它可以实现**清晰的关注点分离**。这意味着对 UI 的更改只需要在页面对象类中进行更新，而不需要在测试本身中进行更新，从而使测试对应用程序 UI 中的更改更具**弹性**。
  此外，POM 促进了代码的**更好的组织**并**提高了可读性**，因为该模型鼓励采用模块化的脚本编写方法。 [Test cases](../T/test-case.md) 变得更**易于理解**和**更易于导航**，因为它们与表示页面的方法交互，而不是直接与 UI 元素交互。
  使用 POM 还可以促进**团队协作**。由于该模型为页面提供的服务或操作提供了一个存储库，因此多个测试工程师可以处理自动化脚本，而不会互相干扰。
  最后，POM可以轻松地**与其他设计模式集成**，例如Singleton或Factory，以进一步提高[test automation](../T/test-automation.md)框架的效率和可扩展性。这种集成可以带来更**强大和灵活的**测试架构，可以轻松处理复杂的[test scenarios](../T/test-scenario.md)。
  从本质上讲，POM 是现代 [test automation](../T/test-automation.md) 策略的基石，提供了一种符合良好软件设计原则的结构化且可维护的方法。

#### 使用页面对象模型有哪些好处？

**[Page Object Model](../P/page-object-model.md) (POM)** 为 [test automation](../T/test-automation.md) 提供了多项优势：

- **[Maintainability](../M/maintainability.md)** ：通过封装页面详细信息，POM 减少了维护工作。 UI 的更改只需要更新页面对象类，而不需要更新测试。
  - **可读性**：由于页面操作和断言的清晰分离，测试变得更具可读性。这使得新团队成员更容易理解代码。
  - **可重用性**：页面方法可以在多个测试中重用，减少代码重复。
  - **减少不稳定**：集中元素定位器和交互可以带来更稳定的测试，因为对这些元素的更改只需要在一处更新。
  - **更好的协作**：清晰的结构允许开发人员和测试人员在测试代码库上更有效地合作。
  - **易于报告**：使用表示页面操作的方法，可以更简单地生成有意义的测试报告和日志。
  - **可扩展性**：POM 支持通过添加新的页面对象和测试来扩展测试套件，而不会显着增加复杂性。
  通过利用 POM，[test automation](../T/test-automation.md) 工程师可以构建一个健壮、可扩展且可维护的[test suite](../T/test-suite.md)，它可以适应应用程序 UI 的变化，同时对现有测试的影响最小。

- **[Maintainability](../M/maintainability.md)** ：通过封装页面详细信息，POM 减少了维护工作。 UI 的更改只需要更新页面对象类，而不需要更新测试。
  - **可读性**：由于页面操作和断言的清晰分离，测试变得更具可读性。这使得新团队成员更容易理解代码。
  - **可重用性**：页面方法可以在多个测试中重用，减少代码重复。
  - **减少不稳定**：集中元素定位器和交互可以带来更稳定的测试，因为对这些元素的更改只需要在一处更新。
  - **更好的协作**：清晰的结构允许开发人员和测试人员在测试代码库上更有效地合作。
  - **易于报告**：使用表示页面操作的方法，可以更简单地生成有意义的测试报告和日志。
  - **可扩展性**：POM 支持通过添加新的页面对象和测试来扩展测试套件，而不会显着增加复杂性。

#### 页面对象模型如何提高测试代码的可维护性？

[Page Object Model](../P/page-object-model.md) (POM) 通过**封装**页面对象中的 UI 结构和行为来增强测试代码的[maintainability](../M/maintainability.md)。这种分离意味着对 UI 的更改只需要在一处进行更新，从而降低了重复代码的风险并使其更易于管理。
  通过抽象页面细节，POM 允许测试**可读**和**可理解**，类似于特定于领域的语言。这种清晰度使任何人都可以在必要时轻松更新测试。
  POM 促进**可重用性**。跨页面共享的公共元素和功能可以抽象为基类或实用程序类，页面对象可以从中继承或使用。这种方法最大限度地减少了为类似 UI 组件编写和维护测试所需的工作量。
  使用 POM，测试对于 UI 中的更改不会那么脆弱。由于定位器和与 UI 的交互仅限于页面对象，因此页面结构中的任何修改仅需要在页面对象类中进行更改，而不是在测试本身中进行更改。这种**解耦**确保测试逻辑保持稳定并且不受 UI 更改的影响。
  最后，POM 支持**并行开发**。 [Test automation](../T/test-automation.md) 工程师可以在开发应用程序 UI 的同时开发和维护页面对象，从而实现持续集成和测试。
  总之，POM 通过集中更改、增强可读性、促进可重用性、降低脆弱性和支持并行开发工作来改进[maintainability](../M/maintainability.md)。

＃＃＃ 执行

#### Selenium 中的页面对象模型是如何实现的？

在[Selenium](../S/selenium.md) 中实现[Page Object Model](../P/page-object-model.md) (POM) 需要为每个网页创建一个单独的类文件。每个类都封装了网页的结构和行为，提供与其元素交互的方法。
  这是分步指南：

1. **使用 ID、名称、CSS 选择器或 XPath 等定位器识别网页上的元素**。
  2. **创建一个代表网页的类**。类名应该反映页面的用途，使其易于识别。
  3. **为您想要交互的每个元素声明私有变量**。这些变量代表网页的元素。
  4. 如果您使用的是 PageFactory，请使用 `PageFactory.initElements()` 方法在类的构造函数中**初始化元素**。
  5. **编写公共方法**以对元素执行操作，例如 click、setText 或 getText。这些方法抽象了交互并且可以在多个测试中重用。
  6. **从导致导航到不同页面的方法返回相关页面对象的新实例**。
  下面是一个简单的 Java 示例：

  ```
  import org.openqa.selenium.WebDriver;
  import org.openqa.selenium.WebElement;
  import org.openqa.selenium.support.FindBy;
  import org.openqa.selenium.support.PageFactory;
  public class LoginPage {
      private WebDriver driver;
      @FindBy(id = "username")
      private WebElement usernameField;
      @FindBy(id = "password")
      private WebElement passwordField;
      @FindBy(id = "loginButton")
      private WebElement loginButton;
      public LoginPage(WebDriver driver) {
          this.driver = driver;
          PageFactory.initElements(driver, this);
      }
      public HomePage login(String username, String password) {
          usernameField.sendKeys(username);
          passwordField.sendKeys(password);
          loginButton.click();
          return new HomePage(driver);
      }
  }
  ```在此示例中，`LoginPage` 是一个页面对象类，它提供方法`login` 来执行登录操作，并在成功登录后返回`HomePage` 的新实例。

1. **使用 ID、名称、CSS 选择器或 XPath 等定位器识别网页上的元素**。
  2. **创建一个代表网页的类**。类名应该反映页面的用途，使其易于识别。
  3. **为您想要交互的每个元素声明私有变量**。这些变量代表网页的元素。
  4. 如果您使用的是 PageFactory，请使用 `PageFactory.initElements()` 方法在类的构造函数中**初始化元素**。
  5. **编写公共方法**以对元素执行操作，例如 click、setText 或 getText。这些方法抽象了交互并且可以在多个测试中重用。
  6. **从导致导航到不同页面的方法返回相关页面对象的新实例**。

#### 页面对象类的关键组件是什么？

**页面对象** 类的关键组件包括：

- **定位器**：存储在页面上查找元素的方式的变量，通常作为私有成员。使用 ID、名称、CSS 选择器或 XPath 等策略。

    ```
    private By loginButton = By.id("login");
    ```

- **构造函数**：初始化页面对象，通常确保页面处于预期状态。可以使用 **[WebDriver](../W/webdriver.md)** 作为参数。

    ```
    public LoginPage(WebDriver driver) {
        this.driver = driver;
    }
    ```

- **WebElements**：页面上元素的表示，通常使用定位器定义。避免公共 WebElements 以维护封装。

    ```
    private WebElement getLoginButton() {
        return driver.findElement(loginButton);
    }
    ```

- **操作**：模拟用户与页面交互的方法，例如单击按钮或输入文本。它们为测试提供与页面交互的接口。

    ```
    public void clickLogin() {
        getLoginButton().click();
    }
    ```

- **断言**：允许 [verification](../V/verification.md) 页面或某些元素的状态的方法，确保页面在操作后按预期运行。

    ```
    public boolean isLoginButtonVisible() {
        return getLoginButton().isDisplayed();
    }
    ```

- **导航方法**：处理到其他页面的转换的函数，通常返回下一页对象的新实例。

    ```
    public HomePage login(String user, String pass) {
        enterUsername(user);
        enterPassword(pass);
        clickLogin();
        return new HomePage(driver);
    }
    ```这些组件协同工作，创建一个健壮、可维护且可重用的界面，用于自动与特定页面进行交互。

- **定位器**：存储在页面上查找元素的方式的变量，通常作为私有成员。使用 ID、名称、CSS 选择器或 XPath 等策略。

    ```
    private By loginButton = By.id("login");
    ```

- **构造函数**：初始化页面对象，通常确保页面处于预期状态。可以使用 **[WebDriver](../W/webdriver.md)** 作为参数。

    ```
    public LoginPage(WebDriver driver) {
        this.driver = driver;
    }
    ```

- **WebElements**：页面上元素的表示，通常使用定位器定义。避免公共 WebElements 以维护封装。

    ```
    private WebElement getLoginButton() {
        return driver.findElement(loginButton);
    }
    ```

- **操作**：模拟用户与页面交互的方法，例如单击按钮或输入文本。它们为测试提供与页面交互的接口。

    ```
    public void clickLogin() {
        getLoginButton().click();
    }
    ```

- **断言**：允许 [verification](../V/verification.md) 页面或某些元素的状态的方法，确保页面在操作后按预期运行。

    ```
    public boolean isLoginButtonVisible() {
        return getLoginButton().isDisplayed();
    }
    ```

- **导航方法**：处理到其他页面的转换的函数，通常返回下一页对象的新实例。

    ```
    public HomePage login(String user, String pass) {
        enterUsername(user);
        enterPassword(pass);
        clickLogin();
        return new HomePage(driver);
    }
    ```

#### 如何处理页面对象模型中的动态元素？

处理 [Page Object Model](../P/page-object-model.md) (POM) 中的动态元素涉及允许您的测试与可能具有不一致标识符或可能在测试运行之间更改状态的元素进行交互的策略。以下是一些方法：

- **使用等待**：实现显式等待来处理在特定条件或时间后出现的元素。这确保了当您的测试尝试访问这些元素时，这些元素是可交互的。

  ```
  WebDriverWait wait = new WebDriverWait(driver, Duration.ofSeconds(10));
  WebElement dynamicElement = wait.until(ExpectedConditions.visibilityOfElementLocated(By.id("dynamicId")));
  ```

- **动态选择器**：制作 XPath 或 CSS 选择器，可以根据元素的相对位置或其他不变的属性来定位元素。

  ```
  WebElement dynamicElement = driver.findElement(By.xpath("//div[contains(@class, 'dynamic-class')]"));
  ```

- **正则表达式**：如果元素标识符的一部分是动态的，则使用带有选择器的正则表达式来匹配模式。

  ```
  WebElement dynamicElement = driver.findElement(By.xpath("//input[contains(@id, 'regexPattern')]"));
  ```

- **JavaScript 执行**：执行 JavaScript 来与标准 Selenium 方法难以处理的元素进行交互。

  ```
  JavascriptExecutor js = (JavascriptExecutor) driver;
  WebElement dynamicElement = (WebElement) js.executeScript("return document.querySelector('.dynamic-class');");
  ```

- **自定义方法**：在页面对象中创建自定义方法，封装处理动态元素的逻辑，使您的测试更清晰、更具可读性。

  ```
  public WebElement getDynamicElement() {
      WebDriverWait wait = new WebDriverWait(driver, Duration.ofSeconds(10));
      return wait.until(ExpectedConditions.visibilityOfElementLocated(By.id("dynamicId")));
  }
  ```通过在页面对象类中采用这些策略，您可以有效地管理动态元素并维护稳定、可靠的自动化测试。

- **使用等待**：实现显式等待来处理在特定条件或时间后出现的元素。这确保了当您的测试尝试访问这些元素时，这些元素是可交互的。
  - **动态选择器**：制作 XPath 或 CSS 选择器，可以根据元素的相对位置或其他不变的属性来定位元素。
  - **正则表达式**：如果元素标识符的一部分是动态的，则使用带有选择器的正则表达式来匹配模式。
  - **JavaScript 执行**：执行 JavaScript 来与标准 Selenium 方法难以处理的元素进行交互。
  - **自定义方法**：在页面对象中创建自定义方法，封装处理动态元素的逻辑，使您的测试更清晰、更具可读性。

#### 如何在页面对象模型中使用页面工厂类？

在 [Page Object Model](../P/page-object-model.md) (POM) 中使用 **Page Factory** 类涉及以支持 POM 设计原则的方式初始化元素。 Page Factory 提供了 `initElements` 方法来初始化所有使用 `@FindBy`、`@FindBys` 或 `@FindAll` 注释进行注释的 WebElement 字段。
  下面是使用 [Selenium](../S/selenium.md) 的 PageFactory 的 Java 基本示例：

  ```
  import org.openqa.selenium.WebDriver;
  import org.openqa.selenium.WebElement;
  import org.openqa.selenium.support.FindBy;
  import org.openqa.selenium.support.PageFactory;
  public class LoginPage {
      private WebDriver driver;
      @FindBy(id = "username")
      private WebElement usernameField;
      @FindBy(id = "password")
      private WebElement passwordField;
      @FindBy(id = "loginButton")
      private WebElement loginButton;
      public LoginPage(WebDriver driver) {
          this.driver = driver;
          PageFactory.initElements(driver, this);
      }
      public void enterUsername(String username) {
          usernameField.sendKeys(username);
      }
      public void enterPassword(String password) {
          passwordField.sendKeys(password);
      }
      public void clickLogin() {
          loginButton.click();
      }
  }
  ```在此示例中，`LoginPage` 类表示页面对象。构造函数采用 `WebDriver` 实例并调用 `PageFactory.initElements` 来初始化字段。 `@FindBy` 注释定义元素在网页上的位置。
  **页面工厂** 特别适用于：

- **可读性**：它清楚地将页面结构与测试逻辑分开。
  - **[Maintainability](../M/maintainability.md)** ：对元素定位器的更改仅需要在一处更新。
  - **可重用性**：常用的元素和交互可以封装在方法中以便在测试中重用。
  - **可读性**：它清楚地将页面结构与测试逻辑分开。
  - **[Maintainability](../M/maintainability.md)** ：对元素定位器的更改仅需要在一处更新。
  - **可重用性**：常用的元素和交互可以封装在方法中以便在测试中重用。

### 高级概念

#### 页面对象模型如何与单例或工厂等其他设计模式一起使用？

**[Page Object Model](../P/page-object-model.md) (POM)** 可以通过与 **Singleton** 和 **Factory** 等其他设计模式集成来增强，以提高测试维护和可扩展性。
  **单例**确保一个类只有一个实例并提供对其的全局访问点。在POM中，Singleton可以管理浏览器会话的实例化。通过对浏览器实例使用 Singleton，您可以确保测试不会无意中生成多个浏览器窗口。

  ```
  public class DriverSingleton {
      private static WebDriver driver;
      private DriverSingleton() {}
      public static WebDriver getDriver() {
          if (driver == null) {
              driver = new ChromeDriver();
          }
          return driver;
      }
  }
  ```**工厂**模式用于创建对象，而不指定将创建的对象的确切类。当您有多个页面类并且想要实例化它们而不暴露实例化逻辑时，这在 POM 中非常有用。

  ```
  public class PageFactory {
      public static <T extends BasePage> T getPage(Class<T> pageClass) {
          try {
              return pageClass.getDeclaredConstructor(WebDriver.class)
                              .newInstance(DriverSingleton.getDriver());
          } catch (Exception e) {
              throw new RuntimeException("Error creating page instance", e);
          }
      }
  }
  ```通过将 POM 与 Factory 相结合，您可以在运行时动态创建页面对象，这在处理共享相似功能的多个页面时特别有用。 Singleton与POM一起使用时，可以确保[WebDriver](../W/webdriver.md)实例被有效地重用，从而减少资源消耗并加快[test execution](../T/test-execution.md)的速度。这些模式共同构建了一个更健壮、可维护和可扩展的 [test automation](../T/test-automation.md) 框架。

#### 如何在页面对象模型中处理页面导航？

处理 **[Page Object Model](../P/page-object-model.md) (POM)** 中的页面导航涉及将导航逻辑封装在页面对象本身内。这种方法保持了关注点的分离，并使测试保持干净和可读。
  这是一个总体策略：

- **定义方法**
    用于在页面对象类中导航。这些方法执行导致页面转换的操作，例如单击链接或提交表单。

- **返回一个新的页面对象**
    代表目标页面的实例。这允许在测试中提供流畅的界面和链接操作。
  例如，在基于 [Selenium](../S/selenium.md) 的 [test automation](../T/test-automation.md) 框架中：

  ```
  public class HomePage {
      // Elements and methods for the home page
      public LoginPage clickSignIn() {
          // Code to click on the sign-in link
          return new LoginPage(driver);
      }
  }
  public class LoginPage {
      // Elements and methods for the login page
      public DashboardPage login(String username, String password) {
          // Code to enter login credentials and submit
          return new DashboardPage(driver);
      }
  }
  ```在测试中，您可以链接这些方法来浏览应用程序：

  ```
  HomePage homePage = new HomePage(driver);
  DashboardPage dashboard = homePage.clickSignIn().login("user", "pass");
  ```通过遵循此模式，您可以确保**页面转换是可预测的**，并且您的测试与导航逻辑保持**解耦**。这使得您的测试更加**可维护**和**可扩展**，因为导航的更改只需要在页面对象方法中进行更新，而不是在测试本身中进行更新。

- **定义方法**
    用于在页面对象类中导航。这些方法执行导致页面转换的操作，例如单击链接或提交表单。

- **返回一个新的页面对象**
    代表目标页面的实例。这允许在测试中提供流畅的界面和链接操作。

#### 页面对象模型中抽象的作用是什么？

[Page Object Model](../P/page-object-model.md) (POM) 中的抽象用于将网页的**实现细节**与使用它们的测试分开。通过将网页交互抽象为**高级方法**，POM 允许 [test scripts](../T/test-script.md) 与页面元素交互，而无需了解底层 HTML 或 CSS。这种封装意味着页面结构的更改仅需要在页面对象类中进行更新，而不是在测试本身中进行更新。
  例如，考虑带有用户名和密码字段的登录页面。您无需在测试中直接编写代码与这些字段进行交互，而是在页面对象中创建一个方法：

  ```
  public HomePage login(String username, String password) {
      usernameField.sendKeys(username);
      passwordField.sendKeys(password);
      submitButton.click();
      return new HomePage();
  }
  ```然后测试可以调用此方法，而无需关心登录操作的执行方式：

  ```
  LoginPage loginPage = new LoginPage(driver);
  HomePage homePage = loginPage.login("user", "pass");
  ```这种抽象使得测试**更易于阅读和维护**，因为它们专注于正在测试的**行为**，而不是用户界面的**机制**。它还减少了**代码重复**，因为常见的交互集中在页面对象方法中。当 UI 发生更改时，您只需更新页面对象，而不需要更新测试，从而确保 [test suite](../T/test-suite.md) 的**稳健性**和**可扩展性**。

#### 如何使用页面对象模型处理多个窗口或框架？

处理 [Page Object Model](../P/page-object-model.md) (POM) 中的多个窗口或框架涉及为每个窗口或框架创建单独的页面对象。这封装了每个上下文中的交互，维护了 POM 的模块化和可重用性原则。
  对于**窗口之间的切换**，可以使用[WebDriver](../W/webdriver.md) 的`switchTo().window()` 方法。在与窗口中的元素交互之前，存储窗口句柄并切换到所需的窗口。

  ```
  Set<String> windowHandles = driver.getWindowHandles();
  for (String windowHandle : windowHandles) {
      if (!windowHandle.equals(originalWindow)) {
          driver.switchTo().window(windowHandle);
          // Interact with the new window using its page object
      }
  }
  ```对于**处理框架或 iframe**，请使用 [WebDriver](../W/webdriver.md) 的 `switchTo().frame()` 方法。您可以按索引、名称或 WebElement 切换到框架。切换后，通过其专用的页面对象与框架的内容进行交互。

  ```
  driver.switchTo().frame("frameName");
  // Interact with the frame using its page object
  driver.switchTo().defaultContent(); // Switch back to the main page
  ```请记住在交互完成后切换回主要内容或原始窗口，以保持后续操作的稳定状态。这可以通过对框架使用 `driver.switchTo().defaultContent()` 或通过切换到窗口的原始窗口句柄来完成。
  通过将窗口和框架处理封装在页面对象中，您可以保持关注点的清晰分离并改进测试代码的[maintainability](../M/maintainability.md)。
