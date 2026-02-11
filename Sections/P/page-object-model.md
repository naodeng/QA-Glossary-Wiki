# Page Object Model
[Page Object Model](#page-object-model)[Page Object Model](/wiki/page-object-model)
### Related Terms:
- Web Automation
- Selenium IDE
- WebDriver
[Web Automation](/glossary/web-automation)[Selenium IDE](/glossary/selenium-ide)[WebDriver](/glossary/webdriver)
## Questions aboutPage Object Model?

#### Basics and Importance
- What is the Page Object Model in automation testing?ThePage Object Model(POM)is a design pattern in automation testing that encapsulates the properties and behaviors of a web page within a class. Each page class serves as an interface to a web page, and all interactions with that page go through the page object, hiding the underlyingSeleniumcalls.Here's a basic example in Java usingSelenium:public class LoginPage {
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
}In this model, tests interact with the page objects rather than directly with the web elements. This abstraction reduces code duplication and improvesmaintainability. When a page changes, only the page object needs to be updated, not the tests that interact with it.To interact with a page object, a test would instantiate the page object with a reference to theWebDriverand use its methods to perform actions:LoginPage loginPage = new LoginPage(driver);
loginPage.enterUsername("user");
loginPage.enterPassword("pass");
loginPage.clickLoginButton();By following this pattern, tests become more readable and resilient to changes in the web application's UI.
- Why is the Page Object Model considered a good practice in automation testing?ThePage Object Model(POM) is considered a good practice in automation testing due to itsenhancement of test maintenanceandreduction in code duplication. By encapsulating page information away from the actual tests, it allows for aclear separation of concerns. This means that changes to the UI only require updates in the page object classes, not in the tests themselves, making the tests moreresilient to changesin the application UI.Moreover, POM promotesbetter organizationof code andimproves readability, as the model encourages a modular approach to scripting.Test casesbecome moreunderstandableandeasier to navigatebecause they interact with methods that represent the page, rather than directly with the UI elements.Using POM also facilitatesteam collaboration. As the model provides a single repository for the services or operations offered by the page, multiple test engineers can work on the automation scripts without stepping on each other's toes.Lastly, POM can be easilyintegrated with other design patterns, such as Singleton or Factory, to further enhance the efficiency and scalability of thetest automationframework. This integration can lead to morerobust and flexibletest architectures that can handle complextest scenarioswith ease.In essence, POM is a cornerstone of moderntest automationstrategies, offering a structured and maintainable approach that aligns with good software design principles.
- What are the benefits of using the Page Object Model?ThePage Object Model(POM)offers several benefits fortest automation:Maintainability: By encapsulating page details, POM reduces the maintenance effort. Changes in UI only require updates in page object classes, not in tests.Readability: Tests become more readable due to the clear separation of page actions and assertions. This makes it easier for new team members to understand the code.Reusability: Page methods can be reused across multiple tests, reducing code duplication.Reduced Flakiness: Centralizing element locators and interactions can lead to more stable tests as changes to these elements only need to be updated in one place.Better Collaboration: Clear structure allows developers and testers to work more efficiently together on the test codebase.Ease of Reporting: With methods representing page actions, it's simpler to generate meaningful test reports and logs.Scalability: POM supports scaling the test suite by adding new page objects and tests without a significant increase in complexity.By leveraging POM,test automationengineers can build a robust, scalable, and maintainabletest suitethat can adapt to changes in the application's UI with minimal impact on the existing tests.
- How does the Page Object Model improve the maintainability of test code?ThePage Object Model(POM) enhancesmaintainabilityof test code byencapsulatingthe UI structure and behaviors within page objects. This separation means changes to the UI only require updates in one place, reducing the risk of duplicating code and making it easier to manage.By abstracting page details, POM allows tests to bereadableandunderstandable, resembling domain-specific language. This clarity makes it straightforward for anyone to update tests when necessary.POM promotesreusability. Common elements and functionalities shared across pages can be abstracted into base or utility classes, from which page objects can inherit or consume. This approach minimizes the effort needed to write and maintain tests for similar UI components.With POM, tests are less brittle to changes in the UI. Since locators and interactions with the UI are confined to page objects, any modifications in the page structure require changes only in the page object classes, not in the tests themselves. Thisdecouplingensures that the test logic remains stable and unaffected by UI changes.Lastly, POM supportsparallel development.Test automationengineers can develop and maintain page objects simultaneously with the development of the application's UI, allowing for continuous integration and testing.In summary, POM improvesmaintainabilityby centralizing changes, enhancing readability, promoting reusability, reducing brittleness, and supporting parallel development efforts.

ThePage Object Model(POM)is a design pattern in automation testing that encapsulates the properties and behaviors of a web page within a class. Each page class serves as an interface to a web page, and all interactions with that page go through the page object, hiding the underlyingSeleniumcalls.
**Page Object Model(POM)**[Page Object Model](/wiki/page-object-model)[Selenium](/wiki/selenium)
Here's a basic example in Java usingSelenium:
[Selenium](/wiki/selenium)
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
`public class LoginPage {
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
}`
In this model, tests interact with the page objects rather than directly with the web elements. This abstraction reduces code duplication and improvesmaintainability. When a page changes, only the page object needs to be updated, not the tests that interact with it.
[maintainability](/wiki/maintainability)
To interact with a page object, a test would instantiate the page object with a reference to theWebDriverand use its methods to perform actions:
[WebDriver](/wiki/webdriver)
```
LoginPage loginPage = new LoginPage(driver);
loginPage.enterUsername("user");
loginPage.enterPassword("pass");
loginPage.clickLoginButton();
```
`LoginPage loginPage = new LoginPage(driver);
loginPage.enterUsername("user");
loginPage.enterPassword("pass");
loginPage.clickLoginButton();`
By following this pattern, tests become more readable and resilient to changes in the web application's UI.

ThePage Object Model(POM) is considered a good practice in automation testing due to itsenhancement of test maintenanceandreduction in code duplication. By encapsulating page information away from the actual tests, it allows for aclear separation of concerns. This means that changes to the UI only require updates in the page object classes, not in the tests themselves, making the tests moreresilient to changesin the application UI.
[Page Object Model](/wiki/page-object-model)**enhancement of test maintenance****reduction in code duplication****clear separation of concerns****resilient to changes**
Moreover, POM promotesbetter organizationof code andimproves readability, as the model encourages a modular approach to scripting.Test casesbecome moreunderstandableandeasier to navigatebecause they interact with methods that represent the page, rather than directly with the UI elements.
**better organization****improves readability**[Test cases](/wiki/test-case)**understandable****easier to navigate**
Using POM also facilitatesteam collaboration. As the model provides a single repository for the services or operations offered by the page, multiple test engineers can work on the automation scripts without stepping on each other's toes.
**team collaboration**
Lastly, POM can be easilyintegrated with other design patterns, such as Singleton or Factory, to further enhance the efficiency and scalability of thetest automationframework. This integration can lead to morerobust and flexibletest architectures that can handle complextest scenarioswith ease.
**integrated with other design patterns**[test automation](/wiki/test-automation)**robust and flexible**[test scenarios](/wiki/test-scenario)
In essence, POM is a cornerstone of moderntest automationstrategies, offering a structured and maintainable approach that aligns with good software design principles.
[test automation](/wiki/test-automation)
ThePage Object Model(POM)offers several benefits fortest automation:
**Page Object Model(POM)**[Page Object Model](/wiki/page-object-model)[test automation](/wiki/test-automation)- Maintainability: By encapsulating page details, POM reduces the maintenance effort. Changes in UI only require updates in page object classes, not in tests.
- Readability: Tests become more readable due to the clear separation of page actions and assertions. This makes it easier for new team members to understand the code.
- Reusability: Page methods can be reused across multiple tests, reducing code duplication.
- Reduced Flakiness: Centralizing element locators and interactions can lead to more stable tests as changes to these elements only need to be updated in one place.
- Better Collaboration: Clear structure allows developers and testers to work more efficiently together on the test codebase.
- Ease of Reporting: With methods representing page actions, it's simpler to generate meaningful test reports and logs.
- Scalability: POM supports scaling the test suite by adding new page objects and tests without a significant increase in complexity.
**Maintainability**[Maintainability](/wiki/maintainability)**Readability****Reusability****Reduced Flakiness****Better Collaboration****Ease of Reporting****Scalability**
By leveraging POM,test automationengineers can build a robust, scalable, and maintainabletest suitethat can adapt to changes in the application's UI with minimal impact on the existing tests.
[test automation](/wiki/test-automation)[test suite](/wiki/test-suite)
ThePage Object Model(POM) enhancesmaintainabilityof test code byencapsulatingthe UI structure and behaviors within page objects. This separation means changes to the UI only require updates in one place, reducing the risk of duplicating code and making it easier to manage.
[Page Object Model](/wiki/page-object-model)[maintainability](/wiki/maintainability)**encapsulating**
By abstracting page details, POM allows tests to bereadableandunderstandable, resembling domain-specific language. This clarity makes it straightforward for anyone to update tests when necessary.
**readable****understandable**
POM promotesreusability. Common elements and functionalities shared across pages can be abstracted into base or utility classes, from which page objects can inherit or consume. This approach minimizes the effort needed to write and maintain tests for similar UI components.
**reusability**
With POM, tests are less brittle to changes in the UI. Since locators and interactions with the UI are confined to page objects, any modifications in the page structure require changes only in the page object classes, not in the tests themselves. Thisdecouplingensures that the test logic remains stable and unaffected by UI changes.
**decoupling**
Lastly, POM supportsparallel development.Test automationengineers can develop and maintain page objects simultaneously with the development of the application's UI, allowing for continuous integration and testing.
**parallel development**[Test automation](/wiki/test-automation)
In summary, POM improvesmaintainabilityby centralizing changes, enhancing readability, promoting reusability, reducing brittleness, and supporting parallel development efforts.
[maintainability](/wiki/maintainability)
#### Implementation
- How is the Page Object Model implemented in Selenium?Implementing thePage Object Model(POM) inSeleniuminvolves creating a separate class file for each web page. Each class encapsulates the web page's structure and behaviors, providing methods to interact with its elements.Here's a step-by-step guide:Identify the elementson the web page using locators such as ID, name, CSS selector, or XPath.Create a classrepresenting the web page. The class name should reflect the page's purpose, making it easily identifiable.Declare private variablesfor each element you want to interact with. These variables represent the web page's elements.Initialize elementswithin the constructor of the class using thePageFactory.initElements()method if you're using PageFactory.Write public methodsto perform actions on the elements, such as click, setText, or getText. These methods abstract the interactions and can be reused in multiple tests.Return a new instanceof the relevant page object from methods that result in navigation to a different page.Here's a simple example in Java:import org.openqa.selenium.WebDriver;
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
}In this example,LoginPageis a page object class that provides a methodloginto perform a login action, returning a new instance ofHomePageupon successful login.
- What are the key components of a Page Object class?Key components of aPage Objectclass include:Locators: Variables that store the ways to find elements on the page, often as private members. Use strategies like ID, name, CSS selector, or XPath.private By loginButton = By.id("login");Constructor: Initializes the page object, often ensuring the page is in the expected state. May useWebDriveras a parameter.public LoginPage(WebDriver driver) {
    this.driver = driver;
}WebElements: Representations of the elements on the page, typically defined using locators. Avoid public WebElements to maintain encapsulation.private WebElement getLoginButton() {
    return driver.findElement(loginButton);
}Actions: Methods that simulate user interactions with the page, such as clicking a button or entering text. They provide an interface for the tests to interact with the page.public void clickLogin() {
    getLoginButton().click();
}Assertions: Methods that allowverificationof the state of the page or certain elements, ensuring the page behaves as expected after an action.public boolean isLoginButtonVisible() {
    return getLoginButton().isDisplayed();
}Navigation Methods: Functions that handle the transition to other pages, often returning a new instance of the next page object.public HomePage login(String user, String pass) {
    enterUsername(user);
    enterPassword(pass);
    clickLogin();
    return new HomePage(driver);
}These components work together to create a robust, maintainable, and reusable interface for automating interactions with a specific page.
- How do you handle dynamic elements in a Page Object Model?Handling dynamic elements in aPage Object Model(POM) involves strategies that allow your tests to interact with elements that may not have consistent identifiers or that may change state between test runs. Here are some approaches:Use of Waits: Implement explicit waits to handle elements that appear after a certain condition or time. This ensures that the elements are interactable when your test tries to access them.WebDriverWait wait = new WebDriverWait(driver, Duration.ofSeconds(10));
WebElement dynamicElement = wait.until(ExpectedConditions.visibilityOfElementLocated(By.id("dynamicId")));Dynamic Selectors: Craft XPath or CSS selectors that can locate elements based on their relative position or other attributes that do not change.WebElement dynamicElement = driver.findElement(By.xpath("//div[contains(@class, 'dynamic-class')]"));Regular Expressions: Use regex with selectors to match patterns if part of an element's identifier is dynamic.WebElement dynamicElement = driver.findElement(By.xpath("//input[contains(@id, 'regexPattern')]"));JavaScript Execution: Execute JavaScript to interact with elements that are difficult to handle with standard Selenium methods.JavascriptExecutor js = (JavascriptExecutor) driver;
WebElement dynamicElement = (WebElement) js.executeScript("return document.querySelector('.dynamic-class');");Custom Methods: Create custom methods within your Page Objects that encapsulate the logic for handling dynamic elements, making your tests cleaner and more readable.public WebElement getDynamicElement() {
    WebDriverWait wait = new WebDriverWait(driver, Duration.ofSeconds(10));
    return wait.until(ExpectedConditions.visibilityOfElementLocated(By.id("dynamicId")));
}By employing these strategies within your Page Object classes, you can effectively manage dynamic elements and maintain stable, reliable automated tests.
- How can you use the Page Factory class in the Page Object Model?Using thePage Factoryclass in thePage Object Model(POM) involves initializing elements in a manner that supports the POM's design principles. Page Factory provides aninitElementsmethod to initialize all WebElement fields annotated with@FindBy,@FindBys, or@FindAllannotations.Here's a basic example in Java usingSelenium's PageFactory:import org.openqa.selenium.WebDriver;
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
}In this example, theLoginPageclass represents a page object. The constructor takes aWebDriverinstance and callsPageFactory.initElementsto initialize the fields. The@FindByannotations define how the elements are located on the web page.Page Factoryis particularly useful for:Readability: It clearly separates the page structure from the test logic.Maintainability: Changes to element locators only require updates in one place.Reusability: Commonly used elements and interactions can be encapsulated in methods for reuse across tests.

Implementing thePage Object Model(POM) inSeleniuminvolves creating a separate class file for each web page. Each class encapsulates the web page's structure and behaviors, providing methods to interact with its elements.
[Page Object Model](/wiki/page-object-model)[Selenium](/wiki/selenium)
Here's a step-by-step guide:
1. Identify the elementson the web page using locators such as ID, name, CSS selector, or XPath.
2. Create a classrepresenting the web page. The class name should reflect the page's purpose, making it easily identifiable.
3. Declare private variablesfor each element you want to interact with. These variables represent the web page's elements.
4. Initialize elementswithin the constructor of the class using thePageFactory.initElements()method if you're using PageFactory.
5. Write public methodsto perform actions on the elements, such as click, setText, or getText. These methods abstract the interactions and can be reused in multiple tests.
6. Return a new instanceof the relevant page object from methods that result in navigation to a different page.

Identify the elementson the web page using locators such as ID, name, CSS selector, or XPath.
**Identify the elements**
Create a classrepresenting the web page. The class name should reflect the page's purpose, making it easily identifiable.
**Create a class**
Declare private variablesfor each element you want to interact with. These variables represent the web page's elements.
**Declare private variables**
Initialize elementswithin the constructor of the class using thePageFactory.initElements()method if you're using PageFactory.
**Initialize elements**`PageFactory.initElements()`
Write public methodsto perform actions on the elements, such as click, setText, or getText. These methods abstract the interactions and can be reused in multiple tests.
**Write public methods**
Return a new instanceof the relevant page object from methods that result in navigation to a different page.
**Return a new instance**
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
`import org.openqa.selenium.WebDriver;
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
}`
In this example,LoginPageis a page object class that provides a methodloginto perform a login action, returning a new instance ofHomePageupon successful login.
`LoginPage``login``HomePage`
Key components of aPage Objectclass include:
**Page Object**- Locators: Variables that store the ways to find elements on the page, often as private members. Use strategies like ID, name, CSS selector, or XPath.private By loginButton = By.id("login");
- Constructor: Initializes the page object, often ensuring the page is in the expected state. May useWebDriveras a parameter.public LoginPage(WebDriver driver) {
    this.driver = driver;
}
- WebElements: Representations of the elements on the page, typically defined using locators. Avoid public WebElements to maintain encapsulation.private WebElement getLoginButton() {
    return driver.findElement(loginButton);
}
- Actions: Methods that simulate user interactions with the page, such as clicking a button or entering text. They provide an interface for the tests to interact with the page.public void clickLogin() {
    getLoginButton().click();
}
- Assertions: Methods that allowverificationof the state of the page or certain elements, ensuring the page behaves as expected after an action.public boolean isLoginButtonVisible() {
    return getLoginButton().isDisplayed();
}
- Navigation Methods: Functions that handle the transition to other pages, often returning a new instance of the next page object.public HomePage login(String user, String pass) {
    enterUsername(user);
    enterPassword(pass);
    clickLogin();
    return new HomePage(driver);
}

Locators: Variables that store the ways to find elements on the page, often as private members. Use strategies like ID, name, CSS selector, or XPath.
**Locators**
```
private By loginButton = By.id("login");
```
`private By loginButton = By.id("login");`
Constructor: Initializes the page object, often ensuring the page is in the expected state. May useWebDriveras a parameter.
**Constructor****WebDriver**[WebDriver](/wiki/webdriver)
```
public LoginPage(WebDriver driver) {
    this.driver = driver;
}
```
`public LoginPage(WebDriver driver) {
    this.driver = driver;
}`
WebElements: Representations of the elements on the page, typically defined using locators. Avoid public WebElements to maintain encapsulation.
**WebElements**
```
private WebElement getLoginButton() {
    return driver.findElement(loginButton);
}
```
`private WebElement getLoginButton() {
    return driver.findElement(loginButton);
}`
Actions: Methods that simulate user interactions with the page, such as clicking a button or entering text. They provide an interface for the tests to interact with the page.
**Actions**
```
public void clickLogin() {
    getLoginButton().click();
}
```
`public void clickLogin() {
    getLoginButton().click();
}`
Assertions: Methods that allowverificationof the state of the page or certain elements, ensuring the page behaves as expected after an action.
**Assertions**[verification](/wiki/verification)
```
public boolean isLoginButtonVisible() {
    return getLoginButton().isDisplayed();
}
```
`public boolean isLoginButtonVisible() {
    return getLoginButton().isDisplayed();
}`
Navigation Methods: Functions that handle the transition to other pages, often returning a new instance of the next page object.
**Navigation Methods**
```
public HomePage login(String user, String pass) {
    enterUsername(user);
    enterPassword(pass);
    clickLogin();
    return new HomePage(driver);
}
```
`public HomePage login(String user, String pass) {
    enterUsername(user);
    enterPassword(pass);
    clickLogin();
    return new HomePage(driver);
}`
These components work together to create a robust, maintainable, and reusable interface for automating interactions with a specific page.

Handling dynamic elements in aPage Object Model(POM) involves strategies that allow your tests to interact with elements that may not have consistent identifiers or that may change state between test runs. Here are some approaches:
[Page Object Model](/wiki/page-object-model)- Use of Waits: Implement explicit waits to handle elements that appear after a certain condition or time. This ensures that the elements are interactable when your test tries to access them.
**Use of Waits**
```
WebDriverWait wait = new WebDriverWait(driver, Duration.ofSeconds(10));
WebElement dynamicElement = wait.until(ExpectedConditions.visibilityOfElementLocated(By.id("dynamicId")));
```
`WebDriverWait wait = new WebDriverWait(driver, Duration.ofSeconds(10));
WebElement dynamicElement = wait.until(ExpectedConditions.visibilityOfElementLocated(By.id("dynamicId")));`- Dynamic Selectors: Craft XPath or CSS selectors that can locate elements based on their relative position or other attributes that do not change.
**Dynamic Selectors**
```
WebElement dynamicElement = driver.findElement(By.xpath("//div[contains(@class, 'dynamic-class')]"));
```
`WebElement dynamicElement = driver.findElement(By.xpath("//div[contains(@class, 'dynamic-class')]"));`- Regular Expressions: Use regex with selectors to match patterns if part of an element's identifier is dynamic.
**Regular Expressions**
```
WebElement dynamicElement = driver.findElement(By.xpath("//input[contains(@id, 'regexPattern')]"));
```
`WebElement dynamicElement = driver.findElement(By.xpath("//input[contains(@id, 'regexPattern')]"));`- JavaScript Execution: Execute JavaScript to interact with elements that are difficult to handle with standard Selenium methods.
**JavaScript Execution**
```
JavascriptExecutor js = (JavascriptExecutor) driver;
WebElement dynamicElement = (WebElement) js.executeScript("return document.querySelector('.dynamic-class');");
```
`JavascriptExecutor js = (JavascriptExecutor) driver;
WebElement dynamicElement = (WebElement) js.executeScript("return document.querySelector('.dynamic-class');");`- Custom Methods: Create custom methods within your Page Objects that encapsulate the logic for handling dynamic elements, making your tests cleaner and more readable.
**Custom Methods**
```
public WebElement getDynamicElement() {
    WebDriverWait wait = new WebDriverWait(driver, Duration.ofSeconds(10));
    return wait.until(ExpectedConditions.visibilityOfElementLocated(By.id("dynamicId")));
}
```
`public WebElement getDynamicElement() {
    WebDriverWait wait = new WebDriverWait(driver, Duration.ofSeconds(10));
    return wait.until(ExpectedConditions.visibilityOfElementLocated(By.id("dynamicId")));
}`
By employing these strategies within your Page Object classes, you can effectively manage dynamic elements and maintain stable, reliable automated tests.

Using thePage Factoryclass in thePage Object Model(POM) involves initializing elements in a manner that supports the POM's design principles. Page Factory provides aninitElementsmethod to initialize all WebElement fields annotated with@FindBy,@FindBys, or@FindAllannotations.
**Page Factory**[Page Object Model](/wiki/page-object-model)`initElements``@FindBy``@FindBys``@FindAll`
Here's a basic example in Java usingSelenium's PageFactory:
[Selenium](/wiki/selenium)
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
`import org.openqa.selenium.WebDriver;
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
}`
In this example, theLoginPageclass represents a page object. The constructor takes aWebDriverinstance and callsPageFactory.initElementsto initialize the fields. The@FindByannotations define how the elements are located on the web page.
`LoginPage``WebDriver``PageFactory.initElements``@FindBy`
Page Factoryis particularly useful for:
**Page Factory**- Readability: It clearly separates the page structure from the test logic.
- Maintainability: Changes to element locators only require updates in one place.
- Reusability: Commonly used elements and interactions can be encapsulated in methods for reuse across tests.
**Readability****Maintainability**[Maintainability](/wiki/maintainability)**Reusability**
#### Advanced Concepts
- How can the Page Object Model be used with other design patterns like Singleton or Factory?ThePage Object Model(POM)can be enhanced by integrating it with other design patterns likeSingletonandFactoryto improve test maintenance and scalability.Singletonensures a class has only one instance and provides a global point of access to it. In POM, Singleton can manage the instantiation of browser sessions. By using Singleton for browser instances, you ensure that tests do not inadvertently spawn multiple browser windows.public class DriverSingleton {
    private static WebDriver driver;

    private DriverSingleton() {}

    public static WebDriver getDriver() {
        if (driver == null) {
            driver = new ChromeDriver();
        }
        return driver;
    }
}Factorypattern is used to create objects without specifying the exact class of object that will be created. This is useful in POM when you have multiple page classes and want to instantiate them without exposing the instantiation logic.public class PageFactory {
    public static <T extends BasePage> T getPage(Class<T> pageClass) {
        try {
            return pageClass.getDeclaredConstructor(WebDriver.class)
                            .newInstance(DriverSingleton.getDriver());
        } catch (Exception e) {
            throw new RuntimeException("Error creating page instance", e);
        }
    }
}By combining POM with Factory, you can dynamically create page objects during runtime, which is particularly useful when dealing with multiple pages that share similar features. Singleton, when used with POM, ensures that theWebDriverinstance is reused efficiently, reducing resource consumption and speeding uptest execution. Together, these patterns contribute to a more robust, maintainable, and scalabletest automationframework.
- How can you handle page navigation in the Page Object Model?Handling page navigation in thePage Object Model(POM)involves encapsulating the navigation logic within the page objects themselves. This approach maintains the separation of concerns and keeps tests clean and readable.Here's a general strategy:Define methodsfor navigation in the page object classes. These methods perform actions that cause a page transition, such as clicking a link or submitting a form.Return a new page objectinstance that represents the destination page. This allows for a fluent interface and chaining of actions in your tests.For example, in aSelenium-basedtest automationframework:public class HomePage {
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
}In your tests, you can chain these methods to navigate through the application:HomePage homePage = new HomePage(driver);
DashboardPage dashboard = homePage.clickSignIn().login("user", "pass");By following this pattern, you ensure thatpage transitions are predictableand that your tests remaindecoupledfrom the navigation logic. This makes your tests moremaintainableandscalable, as changes to navigation only require updates in the page object methods, not in the tests themselves.
- What is the role of abstraction in the Page Object Model?Abstraction in thePage Object Model(POM) serves to separate theimplementation detailsof web pages from the tests that use them. By abstracting web page interactions intohigh-level methods, POM allowstest scriptsto interact with page elements without knowing about the underlying HTML or CSS. This encapsulation means that changes to the page structure require updates only in the page object classes, not in the tests themselves.For example, consider a login page with username and password fields. Instead of writing code to interact with these fields directly in the test, you would create a method in the page object:public HomePage login(String username, String password) {
    usernameField.sendKeys(username);
    passwordField.sendKeys(password);
    submitButton.click();
    return new HomePage();
}Tests can then call this method without concern for how the login action is performed:LoginPage loginPage = new LoginPage(driver);
HomePage homePage = loginPage.login("user", "pass");This abstraction makes testseasier to read and maintain, as they focus on thebehaviorbeing tested rather than themechanicsof the user interface. It also reducescode duplication, as common interactions are centralized in page object methods. When UI changes occur, you only need to update the page object, not the tests, ensuringrobustnessandscalabilityof yourtest suite.
- How can you handle multiple windows or frames using the Page Object Model?Handling multiple windows or frames in thePage Object Model(POM) involves creating separate page objects for each window or frame. This encapsulates the interactions within each context, maintaining the POM's principles of modularity and reusability.Forswitching between windows, you can useWebDriver'sswitchTo().window()method. Store the window handles and switch to the desired window before interacting with elements within that window.Set<String> windowHandles = driver.getWindowHandles();
for (String windowHandle : windowHandles) {
    if (!windowHandle.equals(originalWindow)) {
        driver.switchTo().window(windowHandle);
        // Interact with the new window using its page object
    }
}Forhandling frames or iframes, useWebDriver'sswitchTo().frame()method. You can switch to a frame by index, name, or WebElement. After switching, interact with the frame's contents through its dedicated page object.driver.switchTo().frame("frameName");
// Interact with the frame using its page object
driver.switchTo().defaultContent(); // Switch back to the main pageRemember to switch back to the main content or the original window after the interactions are complete to maintain a stable state for subsequent actions. This can be done usingdriver.switchTo().defaultContent()for frames or by switching to the original window handle for windows.By encapsulating window and frame handling within page objects, you maintain a clean separation of concerns and improve themaintainabilityof your test code.

ThePage Object Model(POM)can be enhanced by integrating it with other design patterns likeSingletonandFactoryto improve test maintenance and scalability.
**Page Object Model(POM)**[Page Object Model](/wiki/page-object-model)**Singleton****Factory**
Singletonensures a class has only one instance and provides a global point of access to it. In POM, Singleton can manage the instantiation of browser sessions. By using Singleton for browser instances, you ensure that tests do not inadvertently spawn multiple browser windows.
**Singleton**
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
`public class DriverSingleton {
    private static WebDriver driver;

    private DriverSingleton() {}

    public static WebDriver getDriver() {
        if (driver == null) {
            driver = new ChromeDriver();
        }
        return driver;
    }
}`
Factorypattern is used to create objects without specifying the exact class of object that will be created. This is useful in POM when you have multiple page classes and want to instantiate them without exposing the instantiation logic.
**Factory**
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
`public class PageFactory {
    public static <T extends BasePage> T getPage(Class<T> pageClass) {
        try {
            return pageClass.getDeclaredConstructor(WebDriver.class)
                            .newInstance(DriverSingleton.getDriver());
        } catch (Exception e) {
            throw new RuntimeException("Error creating page instance", e);
        }
    }
}`
By combining POM with Factory, you can dynamically create page objects during runtime, which is particularly useful when dealing with multiple pages that share similar features. Singleton, when used with POM, ensures that theWebDriverinstance is reused efficiently, reducing resource consumption and speeding uptest execution. Together, these patterns contribute to a more robust, maintainable, and scalabletest automationframework.
[WebDriver](/wiki/webdriver)[test execution](/wiki/test-execution)[test automation](/wiki/test-automation)
Handling page navigation in thePage Object Model(POM)involves encapsulating the navigation logic within the page objects themselves. This approach maintains the separation of concerns and keeps tests clean and readable.
**Page Object Model(POM)**[Page Object Model](/wiki/page-object-model)
Here's a general strategy:
- Define methodsfor navigation in the page object classes. These methods perform actions that cause a page transition, such as clicking a link or submitting a form.
- Return a new page objectinstance that represents the destination page. This allows for a fluent interface and chaining of actions in your tests.
**Define methods****Return a new page object**
For example, in aSelenium-basedtest automationframework:
[Selenium](/wiki/selenium)[test automation](/wiki/test-automation)
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
`public class HomePage {
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
}`
In your tests, you can chain these methods to navigate through the application:

```
HomePage homePage = new HomePage(driver);
DashboardPage dashboard = homePage.clickSignIn().login("user", "pass");
```
`HomePage homePage = new HomePage(driver);
DashboardPage dashboard = homePage.clickSignIn().login("user", "pass");`
By following this pattern, you ensure thatpage transitions are predictableand that your tests remaindecoupledfrom the navigation logic. This makes your tests moremaintainableandscalable, as changes to navigation only require updates in the page object methods, not in the tests themselves.
**page transitions are predictable****decoupled****maintainable****scalable**
Abstraction in thePage Object Model(POM) serves to separate theimplementation detailsof web pages from the tests that use them. By abstracting web page interactions intohigh-level methods, POM allowstest scriptsto interact with page elements without knowing about the underlying HTML or CSS. This encapsulation means that changes to the page structure require updates only in the page object classes, not in the tests themselves.
[Page Object Model](/wiki/page-object-model)**implementation details****high-level methods**[test scripts](/wiki/test-script)
For example, consider a login page with username and password fields. Instead of writing code to interact with these fields directly in the test, you would create a method in the page object:

```
public HomePage login(String username, String password) {
    usernameField.sendKeys(username);
    passwordField.sendKeys(password);
    submitButton.click();
    return new HomePage();
}
```
`public HomePage login(String username, String password) {
    usernameField.sendKeys(username);
    passwordField.sendKeys(password);
    submitButton.click();
    return new HomePage();
}`
Tests can then call this method without concern for how the login action is performed:

```
LoginPage loginPage = new LoginPage(driver);
HomePage homePage = loginPage.login("user", "pass");
```
`LoginPage loginPage = new LoginPage(driver);
HomePage homePage = loginPage.login("user", "pass");`
This abstraction makes testseasier to read and maintain, as they focus on thebehaviorbeing tested rather than themechanicsof the user interface. It also reducescode duplication, as common interactions are centralized in page object methods. When UI changes occur, you only need to update the page object, not the tests, ensuringrobustnessandscalabilityof yourtest suite.
**easier to read and maintain****behavior****mechanics****code duplication****robustness****scalability**[test suite](/wiki/test-suite)
Handling multiple windows or frames in thePage Object Model(POM) involves creating separate page objects for each window or frame. This encapsulates the interactions within each context, maintaining the POM's principles of modularity and reusability.
[Page Object Model](/wiki/page-object-model)
Forswitching between windows, you can useWebDriver'sswitchTo().window()method. Store the window handles and switch to the desired window before interacting with elements within that window.
**switching between windows**[WebDriver](/wiki/webdriver)`switchTo().window()`
```
Set<String> windowHandles = driver.getWindowHandles();
for (String windowHandle : windowHandles) {
    if (!windowHandle.equals(originalWindow)) {
        driver.switchTo().window(windowHandle);
        // Interact with the new window using its page object
    }
}
```
`Set<String> windowHandles = driver.getWindowHandles();
for (String windowHandle : windowHandles) {
    if (!windowHandle.equals(originalWindow)) {
        driver.switchTo().window(windowHandle);
        // Interact with the new window using its page object
    }
}`
Forhandling frames or iframes, useWebDriver'sswitchTo().frame()method. You can switch to a frame by index, name, or WebElement. After switching, interact with the frame's contents through its dedicated page object.
**handling frames or iframes**[WebDriver](/wiki/webdriver)`switchTo().frame()`
```
driver.switchTo().frame("frameName");
// Interact with the frame using its page object
driver.switchTo().defaultContent(); // Switch back to the main page
```
`driver.switchTo().frame("frameName");
// Interact with the frame using its page object
driver.switchTo().defaultContent(); // Switch back to the main page`
Remember to switch back to the main content or the original window after the interactions are complete to maintain a stable state for subsequent actions. This can be done usingdriver.switchTo().defaultContent()for frames or by switching to the original window handle for windows.
`driver.switchTo().defaultContent()`
By encapsulating window and frame handling within page objects, you maintain a clean separation of concerns and improve themaintainabilityof your test code.
[maintainability](/wiki/maintainability)
