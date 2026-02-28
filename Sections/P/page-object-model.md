# Page Object Model


<!-- TOC START -->
- [Related Terms:](#related-terms)
- [Questions about Page Object Model ?](#questions-about-page-object-model)
  - [Basics and Importance](#basics-and-importance)
    - [What is the Page Object Model in automation testing?](#what-is-the-page-object-model-in-automation-testing)
    - [Why is the Page Object Model considered a good practice in automation testing?](#why-is-the-page-object-model-considered-a-good-practice-in-automation-testing)
    - [What are the benefits of using the Page Object Model?](#what-are-the-benefits-of-using-the-page-object-model)
    - [How does the Page Object Model improve the maintainability of test code?](#how-does-the-page-object-model-improve-the-maintainability-of-test-code)
  - [Implementation](#implementation)
    - [How is the Page Object Model implemented in Selenium?](#how-is-the-page-object-model-implemented-in-selenium)
    - [What are the key components of a Page Object class?](#what-are-the-key-components-of-a-page-object-class)
    - [How do you handle dynamic elements in a Page Object Model?](#how-do-you-handle-dynamic-elements-in-a-page-object-model)
    - [How can you use the Page Factory class in the Page Object Model?](#how-can-you-use-the-page-factory-class-in-the-page-object-model)
  - [Advanced Concepts](#advanced-concepts)
    - [How can the Page Object Model be used with other design patterns like Singleton or Factory?](#how-can-the-page-object-model-be-used-with-other-design-patterns-like-singleton-or-factory)
    - [How can you handle page navigation in the Page Object Model?](#how-can-you-handle-page-navigation-in-the-page-object-model)
    - [What is the role of abstraction in the Page Object Model?](#what-is-the-role-of-abstraction-in-the-page-object-model)
    - [How can you handle multiple windows or frames using the Page Object Model?](#how-can-you-handle-multiple-windows-or-frames-using-the-page-object-model)
<!-- TOC END -->

The

Page Object Model

(POM) is a design pattern that consolidates web elements into an object repository, promoting code reusability and simplifying test maintenance.

## Related Terms:

- [Web Automation](../W/web-automation.md)
- [Selenium IDE](../S/selenium-ide.md)
- [WebDriver](../W/webdriver.md)

## Questions about Page Object Model ?

### Basics and Importance

#### What is the Page Object Model in automation testing?

  The **[Page Object Model](../P/page-object-model.md) (POM)** is a design pattern in automation testing that encapsulates the properties and behaviors of a web page within a class. Each page class serves as an interface to a web page, and all interactions with that page go through the page object, hiding the underlying [Selenium](../S/selenium.md) calls.
  Here's a basic example in Java using [Selenium](../S/selenium.md):

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
  ```
  In this model, tests interact with the page objects rather than directly with the web elements. This abstraction reduces code duplication and improves [maintainability](../M/maintainability.md). When a page changes, only the page object needs to be updated, not the tests that interact with it.
  To interact with a page object, a test would instantiate the page object with a reference to the [WebDriver](../W/webdriver.md) and use its methods to perform actions:

  ```
  LoginPage loginPage = new LoginPage(driver);
  loginPage.enterUsername("user");
  loginPage.enterPassword("pass");
  loginPage.clickLoginButton();
  ```
  By following this pattern, tests become more readable and resilient to changes in the web application's UI.

#### Why is the Page Object Model considered a good practice in automation testing?

  The [Page Object Model](../P/page-object-model.md) (POM) is considered a good practice in automation testing due to its **enhancement of test maintenance** and **reduction in code duplication**. By encapsulating page information away from the actual tests, it allows for a **clear separation of concerns**. This means that changes to the UI only require updates in the page object classes, not in the tests themselves, making the tests more **resilient to changes** in the application UI.
  Moreover, POM promotes **better organization** of code and **improves readability**, as the model encourages a modular approach to scripting. [Test cases](../T/test-case.md) become more **understandable** and **easier to navigate** because they interact with methods that represent the page, rather than directly with the UI elements.
  Using POM also facilitates **team collaboration**. As the model provides a single repository for the services or operations offered by the page, multiple test engineers can work on the automation scripts without stepping on each other's toes.
  Lastly, POM can be easily **integrated with other design patterns**, such as Singleton or Factory, to further enhance the efficiency and scalability of the [test automation](../T/test-automation.md) framework. This integration can lead to more **robust and flexible** test architectures that can handle complex [test scenarios](../T/test-scenario.md) with ease.
  In essence, POM is a cornerstone of modern [test automation](../T/test-automation.md) strategies, offering a structured and maintainable approach that aligns with good software design principles.

#### What are the benefits of using the Page Object Model?

  The **[Page Object Model](../P/page-object-model.md) (POM)** offers several benefits for [test automation](../T/test-automation.md):

  - **[Maintainability](../M/maintainability.md)** : By encapsulating page details, POM reduces the maintenance effort. Changes in UI only require updates in page object classes, not in tests.
  - **Readability** : Tests become more readable due to the clear separation of page actions and assertions. This makes it easier for new team members to understand the code.
  - **Reusability** : Page methods can be reused across multiple tests, reducing code duplication.
  - **Reduced Flakiness** : Centralizing element locators and interactions can lead to more stable tests as changes to these elements only need to be updated in one place.
  - **Better Collaboration** : Clear structure allows developers and testers to work more efficiently together on the test codebase.
  - **Ease of Reporting** : With methods representing page actions, it's simpler to generate meaningful test reports and logs.
  - **Scalability** : POM supports scaling the test suite by adding new page objects and tests without a significant increase in complexity.
  By leveraging POM, [test automation](../T/test-automation.md) engineers can build a robust, scalable, and maintainable [test suite](../T/test-suite.md) that can adapt to changes in the application's UI with minimal impact on the existing tests.

  - **[Maintainability](../M/maintainability.md)** : By encapsulating page details, POM reduces the maintenance effort. Changes in UI only require updates in page object classes, not in tests.
  - **Readability** : Tests become more readable due to the clear separation of page actions and assertions. This makes it easier for new team members to understand the code.
  - **Reusability** : Page methods can be reused across multiple tests, reducing code duplication.
  - **Reduced Flakiness** : Centralizing element locators and interactions can lead to more stable tests as changes to these elements only need to be updated in one place.
  - **Better Collaboration** : Clear structure allows developers and testers to work more efficiently together on the test codebase.
  - **Ease of Reporting** : With methods representing page actions, it's simpler to generate meaningful test reports and logs.
  - **Scalability** : POM supports scaling the test suite by adding new page objects and tests without a significant increase in complexity.

#### How does the Page Object Model improve the maintainability of test code?

  The [Page Object Model](../P/page-object-model.md) (POM) enhances [maintainability](../M/maintainability.md) of test code by **encapsulating** the UI structure and behaviors within page objects. This separation means changes to the UI only require updates in one place, reducing the risk of duplicating code and making it easier to manage.
  By abstracting page details, POM allows tests to be **readable** and **understandable**, resembling domain-specific language. This clarity makes it straightforward for anyone to update tests when necessary.
  POM promotes **reusability**. Common elements and functionalities shared across pages can be abstracted into base or utility classes, from which page objects can inherit or consume. This approach minimizes the effort needed to write and maintain tests for similar UI components.
  With POM, tests are less brittle to changes in the UI. Since locators and interactions with the UI are confined to page objects, any modifications in the page structure require changes only in the page object classes, not in the tests themselves. This **decoupling** ensures that the test logic remains stable and unaffected by UI changes.
  Lastly, POM supports **parallel development**. [Test automation](../T/test-automation.md) engineers can develop and maintain page objects simultaneously with the development of the application's UI, allowing for continuous integration and testing.
  In summary, POM improves [maintainability](../M/maintainability.md) by centralizing changes, enhancing readability, promoting reusability, reducing brittleness, and supporting parallel development efforts.

### Implementation

#### How is the Page Object Model implemented in Selenium?

  Implementing the [Page Object Model](../P/page-object-model.md) (POM) in [Selenium](../S/selenium.md) involves creating a separate class file for each web page. Each class encapsulates the web page's structure and behaviors, providing methods to interact with its elements.
  Here's a step-by-step guide:

  1. **Identify the elements** on the web page using locators such as ID, name, CSS selector, or XPath.
  2. **Create a class** representing the web page. The class name should reflect the page's purpose, making it easily identifiable.
  3. **Declare private variables** for each element you want to interact with. These variables represent the web page's elements.
  4. **Initialize elements** within the constructor of the class using the `PageFactory.initElements()` method if you're using PageFactory.
  5. **Write public methods** to perform actions on the elements, such as click, setText, or getText. These methods abstract the interactions and can be reused in multiple tests.
  6. **Return a new instance** of the relevant page object from methods that result in navigation to a different page.
  Here's a simple example in Java:

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
  ```
  In this example, `LoginPage` is a page object class that provides a method `login` to perform a login action, returning a new instance of `HomePage` upon successful login.

  1. **Identify the elements** on the web page using locators such as ID, name, CSS selector, or XPath.
  2. **Create a class** representing the web page. The class name should reflect the page's purpose, making it easily identifiable.
  3. **Declare private variables** for each element you want to interact with. These variables represent the web page's elements.
  4. **Initialize elements** within the constructor of the class using the `PageFactory.initElements()` method if you're using PageFactory.
  5. **Write public methods** to perform actions on the elements, such as click, setText, or getText. These methods abstract the interactions and can be reused in multiple tests.
  6. **Return a new instance** of the relevant page object from methods that result in navigation to a different page.

#### What are the key components of a Page Object class?

  Key components of a **Page Object** class include:

  - **Locators**: Variables that store the ways to find elements on the page, often as private members. Use strategies like ID, name, CSS selector, or XPath.

    ```
    private By loginButton = By.id("login");
    ```

  - **Constructor**: Initializes the page object, often ensuring the page is in the expected state. May use **[WebDriver](../W/webdriver.md)** as a parameter.

    ```
    public LoginPage(WebDriver driver) {
        this.driver = driver;
    }
    ```

  - **WebElements**: Representations of the elements on the page, typically defined using locators. Avoid public WebElements to maintain encapsulation.

    ```
    private WebElement getLoginButton() {
        return driver.findElement(loginButton);
    }
    ```

  - **Actions**: Methods that simulate user interactions with the page, such as clicking a button or entering text. They provide an interface for the tests to interact with the page.

    ```
    public void clickLogin() {
        getLoginButton().click();
    }
    ```

  - **Assertions**: Methods that allow [verification](../V/verification.md) of the state of the page or certain elements, ensuring the page behaves as expected after an action.

    ```
    public boolean isLoginButtonVisible() {
        return getLoginButton().isDisplayed();
    }
    ```

  - **Navigation Methods**: Functions that handle the transition to other pages, often returning a new instance of the next page object.

    ```
    public HomePage login(String user, String pass) {
        enterUsername(user);
        enterPassword(pass);
        clickLogin();
        return new HomePage(driver);
    }
    ```
  These components work together to create a robust, maintainable, and reusable interface for automating interactions with a specific page.

  - **Locators**: Variables that store the ways to find elements on the page, often as private members. Use strategies like ID, name, CSS selector, or XPath.

    ```
    private By loginButton = By.id("login");
    ```

  - **Constructor**: Initializes the page object, often ensuring the page is in the expected state. May use **[WebDriver](../W/webdriver.md)** as a parameter.

    ```
    public LoginPage(WebDriver driver) {
        this.driver = driver;
    }
    ```

  - **WebElements**: Representations of the elements on the page, typically defined using locators. Avoid public WebElements to maintain encapsulation.

    ```
    private WebElement getLoginButton() {
        return driver.findElement(loginButton);
    }
    ```

  - **Actions**: Methods that simulate user interactions with the page, such as clicking a button or entering text. They provide an interface for the tests to interact with the page.

    ```
    public void clickLogin() {
        getLoginButton().click();
    }
    ```

  - **Assertions**: Methods that allow [verification](../V/verification.md) of the state of the page or certain elements, ensuring the page behaves as expected after an action.

    ```
    public boolean isLoginButtonVisible() {
        return getLoginButton().isDisplayed();
    }
    ```

  - **Navigation Methods**: Functions that handle the transition to other pages, often returning a new instance of the next page object.

    ```
    public HomePage login(String user, String pass) {
        enterUsername(user);
        enterPassword(pass);
        clickLogin();
        return new HomePage(driver);
    }
    ```

#### How do you handle dynamic elements in a Page Object Model?

  Handling dynamic elements in a [Page Object Model](../P/page-object-model.md) (POM) involves strategies that allow your tests to interact with elements that may not have consistent identifiers or that may change state between test runs. Here are some approaches:

  - **Use of Waits** : Implement explicit waits to handle elements that appear after a certain condition or time. This ensures that the elements are interactable when your test tries to access them.

  ```
  WebDriverWait wait = new WebDriverWait(driver, Duration.ofSeconds(10));
  WebElement dynamicElement = wait.until(ExpectedConditions.visibilityOfElementLocated(By.id("dynamicId")));
  ```

  - **Dynamic Selectors** : Craft XPath or CSS selectors that can locate elements based on their relative position or other attributes that do not change.

  ```
  WebElement dynamicElement = driver.findElement(By.xpath("//div[contains(@class, 'dynamic-class')]"));
  ```

  - **Regular Expressions** : Use regex with selectors to match patterns if part of an element's identifier is dynamic.

  ```
  WebElement dynamicElement = driver.findElement(By.xpath("//input[contains(@id, 'regexPattern')]"));
  ```

  - **JavaScript Execution** : Execute JavaScript to interact with elements that are difficult to handle with standard Selenium methods.

  ```
  JavascriptExecutor js = (JavascriptExecutor) driver;
  WebElement dynamicElement = (WebElement) js.executeScript("return document.querySelector('.dynamic-class');");
  ```

  - **Custom Methods** : Create custom methods within your Page Objects that encapsulate the logic for handling dynamic elements, making your tests cleaner and more readable.

  ```
  public WebElement getDynamicElement() {
      WebDriverWait wait = new WebDriverWait(driver, Duration.ofSeconds(10));
      return wait.until(ExpectedConditions.visibilityOfElementLocated(By.id("dynamicId")));
  }
  ```
  By employing these strategies within your Page Object classes, you can effectively manage dynamic elements and maintain stable, reliable automated tests.

  - **Use of Waits** : Implement explicit waits to handle elements that appear after a certain condition or time. This ensures that the elements are interactable when your test tries to access them.
  - **Dynamic Selectors** : Craft XPath or CSS selectors that can locate elements based on their relative position or other attributes that do not change.
  - **Regular Expressions** : Use regex with selectors to match patterns if part of an element's identifier is dynamic.
  - **JavaScript Execution** : Execute JavaScript to interact with elements that are difficult to handle with standard Selenium methods.
  - **Custom Methods** : Create custom methods within your Page Objects that encapsulate the logic for handling dynamic elements, making your tests cleaner and more readable.

#### How can you use the Page Factory class in the Page Object Model?

  Using the **Page Factory** class in the [Page Object Model](../P/page-object-model.md) (POM) involves initializing elements in a manner that supports the POM's design principles. Page Factory provides an `initElements` method to initialize all WebElement fields annotated with `@FindBy`, `@FindBys`, or `@FindAll` annotations.
  Here's a basic example in Java using [Selenium](../S/selenium.md)'s PageFactory:

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
  ```
  In this example, the `LoginPage` class represents a page object. The constructor takes a `WebDriver` instance and calls `PageFactory.initElements` to initialize the fields. The `@FindBy` annotations define how the elements are located on the web page.
  **Page Factory** is particularly useful for:

  - **Readability** : It clearly separates the page structure from the test logic.
  - **[Maintainability](../M/maintainability.md)** : Changes to element locators only require updates in one place.
  - **Reusability** : Commonly used elements and interactions can be encapsulated in methods for reuse across tests.
  - **Readability** : It clearly separates the page structure from the test logic.
  - **[Maintainability](../M/maintainability.md)** : Changes to element locators only require updates in one place.
  - **Reusability** : Commonly used elements and interactions can be encapsulated in methods for reuse across tests.

### Advanced Concepts

#### How can the Page Object Model be used with other design patterns like Singleton or Factory?

  The **[Page Object Model](../P/page-object-model.md) (POM)** can be enhanced by integrating it with other design patterns like **Singleton** and **Factory** to improve test maintenance and scalability.
  **Singleton** ensures a class has only one instance and provides a global point of access to it. In POM, Singleton can manage the instantiation of browser sessions. By using Singleton for browser instances, you ensure that tests do not inadvertently spawn multiple browser windows.

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
  ```
  **Factory** pattern is used to create objects without specifying the exact class of object that will be created. This is useful in POM when you have multiple page classes and want to instantiate them without exposing the instantiation logic.

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
  ```
  By combining POM with Factory, you can dynamically create page objects during runtime, which is particularly useful when dealing with multiple pages that share similar features. Singleton, when used with POM, ensures that the [WebDriver](../W/webdriver.md) instance is reused efficiently, reducing resource consumption and speeding up [test execution](../T/test-execution.md). Together, these patterns contribute to a more robust, maintainable, and scalable [test automation](../T/test-automation.md) framework.

#### How can you handle page navigation in the Page Object Model?

  Handling page navigation in the **[Page Object Model](../P/page-object-model.md) (POM)** involves encapsulating the navigation logic within the page objects themselves. This approach maintains the separation of concerns and keeps tests clean and readable.
  Here's a general strategy:

  - **Define methods**
    for navigation in the page object classes. These methods perform actions that cause a page transition, such as clicking a link or submitting a form.

  - **Return a new page object**
    instance that represents the destination page. This allows for a fluent interface and chaining of actions in your tests.
  For example, in a [Selenium](../S/selenium.md)-based [test automation](../T/test-automation.md) framework:

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
  ```
  In your tests, you can chain these methods to navigate through the application:

  ```
  HomePage homePage = new HomePage(driver);
  DashboardPage dashboard = homePage.clickSignIn().login("user", "pass");
  ```
  By following this pattern, you ensure that **page transitions are predictable** and that your tests remain **decoupled** from the navigation logic. This makes your tests more **maintainable** and **scalable**, as changes to navigation only require updates in the page object methods, not in the tests themselves.

  - **Define methods**
    for navigation in the page object classes. These methods perform actions that cause a page transition, such as clicking a link or submitting a form.

  - **Return a new page object**
    instance that represents the destination page. This allows for a fluent interface and chaining of actions in your tests.

#### What is the role of abstraction in the Page Object Model?

  Abstraction in the [Page Object Model](../P/page-object-model.md) (POM) serves to separate the **implementation details** of web pages from the tests that use them. By abstracting web page interactions into **high-level methods**, POM allows [test scripts](../T/test-script.md) to interact with page elements without knowing about the underlying HTML or CSS. This encapsulation means that changes to the page structure require updates only in the page object classes, not in the tests themselves.
  For example, consider a login page with username and password fields. Instead of writing code to interact with these fields directly in the test, you would create a method in the page object:

  ```
  public HomePage login(String username, String password) {
      usernameField.sendKeys(username);
      passwordField.sendKeys(password);
      submitButton.click();
      return new HomePage();
  }
  ```
  Tests can then call this method without concern for how the login action is performed:

  ```
  LoginPage loginPage = new LoginPage(driver);
  HomePage homePage = loginPage.login("user", "pass");
  ```
  This abstraction makes tests **easier to read and maintain**, as they focus on the **behavior** being tested rather than the **mechanics** of the user interface. It also reduces **code duplication**, as common interactions are centralized in page object methods. When UI changes occur, you only need to update the page object, not the tests, ensuring **robustness** and **scalability** of your [test suite](../T/test-suite.md).

#### How can you handle multiple windows or frames using the Page Object Model?

  Handling multiple windows or frames in the [Page Object Model](../P/page-object-model.md) (POM) involves creating separate page objects for each window or frame. This encapsulates the interactions within each context, maintaining the POM's principles of modularity and reusability.
  For **switching between windows**, you can use [WebDriver](../W/webdriver.md)'s `switchTo().window()` method. Store the window handles and switch to the desired window before interacting with elements within that window.

  ```
  Set<String> windowHandles = driver.getWindowHandles();
  for (String windowHandle : windowHandles) {
      if (!windowHandle.equals(originalWindow)) {
          driver.switchTo().window(windowHandle);
          // Interact with the new window using its page object
      }
  }
  ```
  For **handling frames or iframes**, use [WebDriver](../W/webdriver.md)'s `switchTo().frame()` method. You can switch to a frame by index, name, or WebElement. After switching, interact with the frame's contents through its dedicated page object.

  ```
  driver.switchTo().frame("frameName");
  // Interact with the frame using its page object
  driver.switchTo().defaultContent(); // Switch back to the main page
  ```
  Remember to switch back to the main content or the original window after the interactions are complete to maintain a stable state for subsequent actions. This can be done using `driver.switchTo().defaultContent()` for frames or by switching to the original window handle for windows.
  By encapsulating window and frame handling within page objects, you maintain a clean separation of concerns and improve the [maintainability](../M/maintainability.md) of your test code.
