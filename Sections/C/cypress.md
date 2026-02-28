# Cypress


<!-- TOC START -->
- [Related Terms:](#related-terms)
  - [See also:](#see-also)
- [Questions about Cypress ?](#questions-about-cypress)
  - [Basics and Importance](#basics-and-importance)
    - [What is Cypress?](#what-is-cypress)
    - [Why is Cypress used in testing?](#why-is-cypress-used-in-testing)
    - [What are the key features of Cypress?](#what-are-the-key-features-of-cypress)
    - [How does Cypress differ from other testing tools like Selenium?](#how-does-cypress-differ-from-other-testing-tools-like-selenium)
    - [What types of testing can be performed using Cypress?](#what-types-of-testing-can-be-performed-using-cypress)
  - [Installation and Setup](#installation-and-setup)
    - [How to install Cypress?](#how-to-install-cypress)
    - [What are the system requirements for Cypress?](#what-are-the-system-requirements-for-cypress)
    - [How to set up a project in Cypress?](#how-to-set-up-a-project-in-cypress)
    - [How to configure Cypress for a specific environment?](#how-to-configure-cypress-for-a-specific-environment)
  - [Writing and Running Tests](#writing-and-running-tests)
    - [How to write a basic test in Cypress?](#how-to-write-a-basic-test-in-cypress)
    - [What is the structure of a Cypress test?](#what-is-the-structure-of-a-cypress-test)
    - [How to run a test in Cypress?](#how-to-run-a-test-in-cypress)
    - [How to use assertions in Cypress?](#how-to-use-assertions-in-cypress)
    - [How to handle events in Cypress?](#how-to-handle-events-in-cypress)
    - [How to use fixtures in Cypress?](#how-to-use-fixtures-in-cypress)
  - [Advanced Concepts](#advanced-concepts)
    - [How does Cypress handle asynchronous operations?](#how-does-cypress-handle-asynchronous-operations)
    - [How to use custom commands in Cypress?](#how-to-use-custom-commands-in-cypress)
    - [How to handle network requests in Cypress?](#how-to-handle-network-requests-in-cypress)
    - [How to work with cookies and local storage in Cypress?](#how-to-work-with-cookies-and-local-storage-in-cypress)
    - [How to handle iframes in Cypress?](#how-to-handle-iframes-in-cypress)
    - [How to use plugins in Cypress?](#how-to-use-plugins-in-cypress)
  - [Best Practices and Troubleshooting](#best-practices-and-troubleshooting)
    - [What are some best practices for writing tests in Cypress?](#what-are-some-best-practices-for-writing-tests-in-cypress)
    - [How to debug tests in Cypress?](#how-to-debug-tests-in-cypress)
    - [How to handle common errors in Cypress?](#how-to-handle-common-errors-in-cypress)
    - [How to optimize test execution time in Cypress?](#how-to-optimize-test-execution-time-in-cypress)
<!-- TOC END -->

(aka Cypress.io )

Cypress

is an

end-to-end testing

framework designed for modern web applications. Unlike many other testing solutions,

Cypress

operates directly within the web browser, ensuring more consistent and accurate real-world testing scenarios. It provides a rich set of features and tools for writing tests, debugging in real time, and capturing screenshots or video recordings of test runs.

Cypress

supports both

unit testing

and full

end-to-end testing

, making it a versatile choice for developers and QA professionals. One of its notable features is its interactive

test runner

that allows developers to see commands as they execute while also viewing the application under test. Built on top of technologies like Mocha, Chai, and Sinon,

Cypress

offers a comprehensive and user-friendly environment for web application testing.

## Related Terms:

- [Web Automation tool](../W/web-automation-tool.md)
- [Playwright](../P/playwright.md)

### See also:

- [Official Website](https://www.cypress.io/)
- [Wikipedia](https://en.wikipedia.org/wiki/Cypress_(software))

## Questions about Cypress ?

### Basics and Importance

#### What is Cypress?

  [Cypress](../C/cypress.md) is an **[end-to-end testing](../E/end-to-end-testing.md) framework** designed for modern web applications. It runs tests in a browser and is built on top of technologies like **JavaScript** and **[Node.js](../N/node-js.md)**. Unlike many other testing tools, [Cypress](../C/cypress.md) executes tests in the same run loop as the application, providing native access to every object without the need for a separate driver or server.
  [Cypress](../C/cypress.md) offers a **rich interactive [test runner](../T/test-runner.md)** that allows you to see commands as they execute while also viewing the application under test. The tool provides **real-time reloads** for [test-driven development](../T/test-driven-development.md), with tests rerunning upon file save.
  Tests in [Cypress](../C/cypress.md) are written using a **chainable [API](../A/api.md)** that works with promises, thus simplifying the handling of asynchronous operations. [Cypress](../C/cypress.md) includes **jQuery-like commands** for DOM traversal and manipulation, making it familiar to front-end developers.
  [Cypress](../C/cypress.md) provides **automatic waiting** before performing actions or assertions, eliminating the need for explicit waits or sleeps in most cases. It also offers **spies, stubs, and clocks** to verify and control the behavior of server responses, functions, or timers.
  The tool has a **screenshot and video recording** feature, which is handy for debugging and understanding test failures. [Cypress](../C/cypress.md) tests can be run headlessly in Continuous Integration (CI) environments or interactively during development.
  [Cypress](../C/cypress.md)'s architecture does not use [Selenium](../S/selenium.md) or [WebDriver](../W/webdriver.md), which allows for faster execution and more control but also means it's primarily suited for testing applications that run in a browser. It supports **Chrome-family browsers** (including Electron) and **Firefox**.

#### Why is Cypress used in testing?

  [Cypress](../C/cypress.md) is used in testing primarily for its **simplicity** and **developer-friendly** approach to [end-to-end testing](../E/end-to-end-testing.md). It allows for writing **flakiness-free** tests due to its unique architecture that runs in the same run-loop as the application being tested. This results in more **reliable** and **consistent** tests compared to other tools that operate outside the browser.
  The use of [Cypress](../C/cypress.md) is favored for its **real-time reloads**, which provide instant feedback on test code changes, enhancing productivity and reducing the time spent on writing and maintaining tests. Its **automatic waiting** mechanism eliminates the need for manual sleep or wait commands, thus reducing the complexity of [test scripts](../T/test-script.md).
  Developers and QA engineers opt for [Cypress](../C/cypress.md) when they need **tight integration** with modern development tools and workflows, including continuous integration and version control systems. [Cypress](../C/cypress.md)'s **rich debugging capabilities** make it easier to diagnose and fix issues directly from the browser's developer tools.
  [Cypress](../C/cypress.md)'s **screenshot and video recording** features are crucial for visualizing the state of the application at the time of test failure, facilitating quicker troubleshooting. Its **network traffic control** allows for easy stubbing and testing of edge cases without the need for backend dependencies.
  Overall, [Cypress](../C/cypress.md) is used for its **all-in-one** testing experience, providing a robust set of tools that cater to the needs of modern web application testing, all within a single, coherent framework.

#### What are the key features of Cypress?

  Key features of [Cypress](../C/cypress.md) include:

  - **Real-Time Reloads** : Cypress automatically reloads tests upon detecting changes to the test code, providing immediate feedback.
  - **Time Travel** : Cypress takes snapshots as tests run, allowing you to hover over commands in the Command Log to see exactly what happened at each step.
  - **Automatic Waiting** : Cypress waits for commands and assertions before moving on, eliminating the need for explicit waits or sleeps.
  - **Consistent Results** : Tests in Cypress are less flaky and more reliable as it runs in the same run-loop as the application.
  - **Debuggability** : With readable errors and stack traces, Cypress makes debugging tests easier. You can also use familiar dev tools.
  - **Network Traffic Control** : Intercept and control every network request, enabling you to test edge cases without involving your server.
  - **Screenshots and Videos** : Cypress can capture screenshots automatically on failure, or you can take them manually. It also records a video of the entire test run.
  - **Cross Browser Testing** : Cypress supports testing across multiple browsers, including Chrome, Firefox, Edge, and Electron.
  - **Parallelization** : Tests can be run in parallel across multiple machines to speed up execution time in Continuous Integration (CI).
  - **Dashboard Service** : Provides insights into tests with analytics, parallelization, and history when used with the Cypress Dashboard.
  - **Spies, Stubs, and Clocks** : Verify and control the behavior of functions, server responses, or timers.
  - **[Accessibility Testing](../A/accessibility-testing.md)** : With plugins like
    `cypress-axe`
    , you can incorporate accessibility checks into your test suite.
  These features are designed to streamline the testing process, making it more efficient and effective for [test automation](../T/test-automation.md) engineers.

  - **Real-Time Reloads** : Cypress automatically reloads tests upon detecting changes to the test code, providing immediate feedback.
  - **Time Travel** : Cypress takes snapshots as tests run, allowing you to hover over commands in the Command Log to see exactly what happened at each step.
  - **Automatic Waiting** : Cypress waits for commands and assertions before moving on, eliminating the need for explicit waits or sleeps.
  - **Consistent Results** : Tests in Cypress are less flaky and more reliable as it runs in the same run-loop as the application.
  - **Debuggability** : With readable errors and stack traces, Cypress makes debugging tests easier. You can also use familiar dev tools.
  - **Network Traffic Control** : Intercept and control every network request, enabling you to test edge cases without involving your server.
  - **Screenshots and Videos** : Cypress can capture screenshots automatically on failure, or you can take them manually. It also records a video of the entire test run.
  - **Cross Browser Testing** : Cypress supports testing across multiple browsers, including Chrome, Firefox, Edge, and Electron.
  - **Parallelization** : Tests can be run in parallel across multiple machines to speed up execution time in Continuous Integration (CI).
  - **Dashboard Service** : Provides insights into tests with analytics, parallelization, and history when used with the Cypress Dashboard.
  - **Spies, Stubs, and Clocks** : Verify and control the behavior of functions, server responses, or timers.
  - **[Accessibility Testing](../A/accessibility-testing.md)** : With plugins like
    `cypress-axe`
    , you can incorporate accessibility checks into your test suite.

#### How does Cypress differ from other testing tools like Selenium?

  [Cypress](../C/cypress.md) differs from [Selenium](../S/selenium.md) in several key aspects:

  - **Architecture**: [Cypress](../C/cypress.md) runs in the same run-loop as the application being tested, leading to faster execution and more consistent results. [Selenium](../S/selenium.md) operates outside the browser, which can introduce latency and flakiness.
  - **Language Support**: [Cypress](../C/cypress.md) tests are written in JavaScript, while [Selenium](../S/selenium.md) supports multiple languages like Java, C#, Python, and Ruby.
  - **Direct Access**: [Cypress](../C/cypress.md) has direct access to the DOM and can interact with elements more naturally. [Selenium](../S/selenium.md) requires an intermediary ([WebDriver](../W/webdriver.md)) to communicate with the browser, which can slow down interactions.
  - **[Setup](../S/setup.md) and Configuration**: [Cypress](../C/cypress.md) is easier to set up, with no need for additional drivers or servers. [Selenium](../S/selenium.md) often requires additional [setup](../S/setup.md) for the [WebDriver](../W/webdriver.md) and browser-specific drivers.
  - **Real-time Reloads**: [Cypress](../C/cypress.md) offers a [Test Runner](../T/test-runner.md) that automatically reloads upon test file changes, providing instant feedback. [Selenium](../S/selenium.md) does not have a built-in equivalent.
  - **Automatic Waiting**: [Cypress](../C/cypress.md) automatically waits for commands and assertions before moving on. [Selenium](../S/selenium.md) requires explicit waits or sleep commands to manage timing issues.
  - **[API Testing](../A/api-testing.md)**: [Cypress](../C/cypress.md) includes built-in support for [API testing](../A/api-testing.md), allowing for both front-end and back-end tests in one framework. [Selenium](../S/selenium.md) is primarily focused on browser-based testing.
  - **Screenshots and Videos**: [Cypress](../C/cypress.md) can take screenshots and record videos natively. [Selenium](../S/selenium.md) can capture screenshots, but video recording often requires additional tools or plugins.
  - **Debuggability**: [Cypress](../C/cypress.md) provides more informative error messages and stack traces, making debugging easier. [Selenium](../S/selenium.md)'s error messages can be less clear, making debugging more challenging.
  - **[Cross-browser Testing](../C/cross-browser-testing.md)**: [Selenium](../S/selenium.md) supports a wider range of browsers and versions. [Cypress](../C/cypress.md)'s cross-browser support is improving but has historically been limited to fewer browsers.
  - **Architecture**: [Cypress](../C/cypress.md) runs in the same run-loop as the application being tested, leading to faster execution and more consistent results. [Selenium](../S/selenium.md) operates outside the browser, which can introduce latency and flakiness.
  - **Language Support**: [Cypress](../C/cypress.md) tests are written in JavaScript, while [Selenium](../S/selenium.md) supports multiple languages like Java, C#, Python, and Ruby.
  - **Direct Access**: [Cypress](../C/cypress.md) has direct access to the DOM and can interact with elements more naturally. [Selenium](../S/selenium.md) requires an intermediary ([WebDriver](../W/webdriver.md)) to communicate with the browser, which can slow down interactions.
  - **[Setup](../S/setup.md) and Configuration**: [Cypress](../C/cypress.md) is easier to set up, with no need for additional drivers or servers. [Selenium](../S/selenium.md) often requires additional [setup](../S/setup.md) for the [WebDriver](../W/webdriver.md) and browser-specific drivers.
  - **Real-time Reloads**: [Cypress](../C/cypress.md) offers a [Test Runner](../T/test-runner.md) that automatically reloads upon test file changes, providing instant feedback. [Selenium](../S/selenium.md) does not have a built-in equivalent.
  - **Automatic Waiting**: [Cypress](../C/cypress.md) automatically waits for commands and assertions before moving on. [Selenium](../S/selenium.md) requires explicit waits or sleep commands to manage timing issues.
  - **[API Testing](../A/api-testing.md)**: [Cypress](../C/cypress.md) includes built-in support for [API testing](../A/api-testing.md), allowing for both front-end and back-end tests in one framework. [Selenium](../S/selenium.md) is primarily focused on browser-based testing.
  - **Screenshots and Videos**: [Cypress](../C/cypress.md) can take screenshots and record videos natively. [Selenium](../S/selenium.md) can capture screenshots, but video recording often requires additional tools or plugins.
  - **Debuggability**: [Cypress](../C/cypress.md) provides more informative error messages and stack traces, making debugging easier. [Selenium](../S/selenium.md)'s error messages can be less clear, making debugging more challenging.
  - **[Cross-browser Testing](../C/cross-browser-testing.md)**: [Selenium](../S/selenium.md) supports a wider range of browsers and versions. [Cypress](../C/cypress.md)'s cross-browser support is improving but has historically been limited to fewer browsers.

#### What types of testing can be performed using Cypress?

  Using [Cypress](../C/cypress.md), testers can perform various types of testing, including:

  - **[End-to-End Testing](../E/end-to-end-testing.md) (E2E)** : Simulating real user scenarios from start to finish, ensuring the application behaves as expected in a production-like environment.
  - **[Integration Testing](../I/integration-testing.md)** : Testing the interactions between application layers or between different microservices to verify they work together correctly.
  - **[Unit Testing](../U/unit-testing.md)** : Although not its primary use case, Cypress can be used to test individual functions or components in isolation.
  - **Component Testing** : Verifying the functionality and rendering of individual components, especially useful in modern JavaScript frameworks like React, Angular, or Vue.
  - **[Visual Regression Testing](../V/visual-regression-testing.md)** : By integrating with tools like Percy or Applitools, Cypress can capture screenshots and compare them to baseline images to detect visual changes.
  - **[Accessibility Testing](../A/accessibility-testing.md)** : With plugins like
    `cypress-axe`
    , testers can incorporate accessibility checks into their test suites to ensure compliance with standards like WCAG.

  - **[API Testing](../A/api-testing.md)** : Although Cypress is primarily a browser-based tool, it can be used to test REST or GraphQL APIs by sending HTTP requests and asserting the responses.
  - **[Performance Testing](../P/performance-testing.md)** : While not a full-fledged performance testing tool, Cypress can capture performance metrics like page load times and use assertions to flag performance regressions.
  [Cypress](../C/cypress.md)'s versatility allows it to cover a broad range of testing needs within a single framework, streamlining the development and testing workflow.

  - **[End-to-End Testing](../E/end-to-end-testing.md) (E2E)** : Simulating real user scenarios from start to finish, ensuring the application behaves as expected in a production-like environment.
  - **[Integration Testing](../I/integration-testing.md)** : Testing the interactions between application layers or between different microservices to verify they work together correctly.
  - **[Unit Testing](../U/unit-testing.md)** : Although not its primary use case, Cypress can be used to test individual functions or components in isolation.
  - **Component Testing** : Verifying the functionality and rendering of individual components, especially useful in modern JavaScript frameworks like React, Angular, or Vue.
  - **[Visual Regression Testing](../V/visual-regression-testing.md)** : By integrating with tools like Percy or Applitools, Cypress can capture screenshots and compare them to baseline images to detect visual changes.
  - **[Accessibility Testing](../A/accessibility-testing.md)** : With plugins like
    `cypress-axe`
    , testers can incorporate accessibility checks into their test suites to ensure compliance with standards like WCAG.

  - **[API Testing](../A/api-testing.md)** : Although Cypress is primarily a browser-based tool, it can be used to test REST or GraphQL APIs by sending HTTP requests and asserting the responses.
  - **[Performance Testing](../P/performance-testing.md)** : While not a full-fledged performance testing tool, Cypress can capture performance metrics like page load times and use assertions to flag performance regressions.

### Installation and Setup

#### How to install Cypress?

  To install [Cypress](../C/cypress.md), ensure you have **[Node.js](../N/node-js.md)** (version 12 or above) and **npm** (version 6 or above) installed on your system. Open your terminal or command prompt and follow these steps:

  1. Navigate to your project directory:

    ```
    cd /your/project/path
    ```

  2. Install [Cypress](../C/cypress.md) as a dev dependency using npm:
    Alternatively, you can use `yarn` if you prefer:

    ```
    npm install cypress --save-dev
    ```

    ```
    yarn add cypress --dev
    ```

  3. After installation, you can open [Cypress](../C/cypress.md) for the first time with:
    Or, if you're using yarn:

    ```
    npx cypress open
    ```

    ```
    yarn run cypress open
    ```
  This will open the [Cypress](../C/cypress.md) [Test Runner](../T/test-runner.md) and create a `cypress` folder in your project directory, which contains the default configuration and sample tests.
  For continuous integration systems or to run [Cypress](../C/cypress.md) tests headlessly, use the `cypress run` command:

  ```
  npx cypress run
  ```
  Remember to add [Cypress](../C/cypress.md) commands to the `scripts` section of your `package.json` for easier execution:

  ```
  "scripts": {
    "cypress:open": "cypress open",
    "cypress:run": "cypress run"
  }
  ```
  To execute with these scripts:

  ```
  npm run cypress:open
  ```
  or

  ```
  npm run cypress:run
  ```
  Ensure you have the necessary permissions to install new packages on your system. If you encounter any issues, refer to the official [Cypress](../C/cypress.md) documentation for troubleshooting.

  1. Navigate to your project directory:

    ```
    cd /your/project/path
    ```

  2. Install [Cypress](../C/cypress.md) as a dev dependency using npm:
    Alternatively, you can use `yarn` if you prefer:

    ```
    npm install cypress --save-dev
    ```

    ```
    yarn add cypress --dev
    ```

  3. After installation, you can open [Cypress](../C/cypress.md) for the first time with:
    Or, if you're using yarn:

    ```
    npx cypress open
    ```

    ```
    yarn run cypress open
    ```

#### What are the system requirements for Cypress?

  [Cypress](../C/cypress.md) is compatible with **Windows, macOS, and Linux** operating systems. The specific system requirements include:

  - **[Node.js](../N/node-js.md)** : Version 12 or above.
  - **npm**
    (usually comes with Node.js) or
    **Yarn**
    for package management.

  - A
    **supported browser**
    installed on your machine. Cypress supports:

    - Chrome (including Canary and Chromium)
    - Firefox (including Developer Edition)
    - Edge
    - Electron (bundled with Cypress)
    - Brave
    - Chrome (including Canary and Chromium)
    - Firefox (including Developer Edition)
    - Edge
    - Electron (bundled with Cypress)
    - Brave
  - For
    **CI/CD pipelines**
    , ensure the build agent meets the OS and Node.js requirements.

  - **Memory and CPU** : Sufficient resources to run the Electron browser, especially when running multiple tests in parallel. At least 2GB of RAM is recommended.
  - **Screen resolution** : A minimum screen resolution of 1280x720 is recommended for viewing the Cypress Test Runner.
  Ensure your system has **write permissions** to the directory where [Cypress](../C/cypress.md) is installed and runs tests.
  For **Linux users**, you may need to install additional dependencies if they are not already present on your system. [Cypress](../C/cypress.md) provides a command that can be run to install these dependencies:

  ```
  sudo apt-get install libgtk2.0-0 libgtk-3-0 libgbm-dev libnotify-dev libgconf-2-4 libnss3 libxss1 libasound2 libxtst6 xauth xvfb
  ```
  **Note**: [Cypress](../C/cypress.md) is a desktop application that is installed on your computer, so it requires the above prerequisites to be met for the installation and execution of tests.

  - **[Node.js](../N/node-js.md)** : Version 12 or above.
  - **npm**
    (usually comes with Node.js) or
    **Yarn**
    for package management.

  - A
    **supported browser**
    installed on your machine. Cypress supports:

    - Chrome (including Canary and Chromium)
    - Firefox (including Developer Edition)
    - Edge
    - Electron (bundled with Cypress)
    - Brave
    - Chrome (including Canary and Chromium)
    - Firefox (including Developer Edition)
    - Edge
    - Electron (bundled with Cypress)
    - Brave
  - For
    **CI/CD pipelines**
    , ensure the build agent meets the OS and Node.js requirements.

  - **Memory and CPU** : Sufficient resources to run the Electron browser, especially when running multiple tests in parallel. At least 2GB of RAM is recommended.
  - **Screen resolution** : A minimum screen resolution of 1280x720 is recommended for viewing the Cypress Test Runner.

#### How to set up a project in Cypress?

  To set up a project in [Cypress](../C/cypress.md), follow these steps:

  1. **Create a new directory** for your project if you haven't already, and navigate into it using your terminal or command prompt.

    ```
    mkdir my-cypress-project
    cd my-cypress-project
    ```

  2. **Initialize a new npm project** with `npm init`. You can skip through the prompts by using `npm init -y`.

    ```
    npm init -y
    ```

  3. **Install [Cypress](../C/cypress.md)** via npm by running:

    ```
    npm install cypress --save-dev
    ```

  4. **Open [Cypress](../C/cypress.md)** for the first time to scaffold the default directory structure and files by executing:
    This command generates a `cypress` folder containing example tests and a `cypress.json` file for configuration.

    ```
    npx cypress open
    ```

  5. **Configure your tests** by editing the `cypress.json` file. Set up any required environment variables or base URLs.

    ```
    {
      "baseUrl": "http://yourapp.com",
      "env": {
        "login_url": "/login",
        "products_url": "/products"
      }
    }
    ```

  6. **Organize your test files** within the `cypress/integration` directory. You may create subdirectories to group related tests.
  7. **Write your tests** using the `describe` and `it` functions provided by [Cypress](../C/cypress.md), and save them with a `.spec.js` or `.spec.ts` extension.
  8. **Run your tests** either using `npx cypress open` to open the [Cypress](../C/cypress.md) [Test Runner](../T/test-runner.md) or `npx cypress run` to execute tests in headless mode.
  Remember to **add the `node_modules` directory to your `.gitignore` file** to avoid committing dependencies to version control. Also, consider setting up scripts in your `package.json` for common [Cypress](../C/cypress.md) commands.

  1. **Create a new directory** for your project if you haven't already, and navigate into it using your terminal or command prompt.

    ```
    mkdir my-cypress-project
    cd my-cypress-project
    ```

  2. **Initialize a new npm project** with `npm init`. You can skip through the prompts by using `npm init -y`.

    ```
    npm init -y
    ```

  3. **Install [Cypress](../C/cypress.md)** via npm by running:

    ```
    npm install cypress --save-dev
    ```

  4. **Open [Cypress](../C/cypress.md)** for the first time to scaffold the default directory structure and files by executing:
    This command generates a `cypress` folder containing example tests and a `cypress.json` file for configuration.

    ```
    npx cypress open
    ```

  5. **Configure your tests** by editing the `cypress.json` file. Set up any required environment variables or base URLs.

    ```
    {
      "baseUrl": "http://yourapp.com",
      "env": {
        "login_url": "/login",
        "products_url": "/products"
      }
    }
    ```

  6. **Organize your test files** within the `cypress/integration` directory. You may create subdirectories to group related tests.
  7. **Write your tests** using the `describe` and `it` functions provided by [Cypress](../C/cypress.md), and save them with a `.spec.js` or `.spec.ts` extension.
  8. **Run your tests** either using `npx cypress open` to open the [Cypress](../C/cypress.md) [Test Runner](../T/test-runner.md) or `npx cypress run` to execute tests in headless mode.

#### How to configure Cypress for a specific environment?

  To configure [Cypress](../C/cypress.md) for a specific environment, you'll need to set environment variables and potentially adjust your `cypress.json` configuration file. Here's a succinct guide:

  1. **Environment Variables**: Define environment-specific variables using the `env` key in your `cypress.json` file or by passing them via the command line.
    Alternatively, use the command line to override:

    ```
    {
      "env": {
        "apiUrl": "https://api.staging.example.com"
      }
    }
    ```

    ```
    npx cypress run --env apiUrl=https://api.staging.example.com
    ```

  2. **Configuration Files**: For more complex [setups](../S/setup.md), consider having separate configuration files for each environment, like `cypress.staging.json` and `cypress.production.json`. Use the `--config-file` flag to specify the configuration file when running tests.

    ```
    npx cypress run --config-file cypress.staging.json
    ```

  3. **Dynamic Configuration**: In your `plugins/index.js` file, you can programmatically alter the configuration based on environment variables or other conditions.

    ```
    module.exports = (on, config) => {
      if (process.env.NODE_ENV === 'staging') {
        config.baseUrl = 'https://staging.example.com';
        // Modify other config settings as needed
      }
      return config;
    };
    ```

  4. **[Cypress](../C/cypress.md).env()**: Access environment variables in your tests using `Cypress.env('variableName')`.

    ```
    const apiUrl = Cypress.env('apiUrl');
    ```
  Remember to **never commit sensitive data** to version control. Use environment variables or a secrets management solution for sensitive data.

  1. **Environment Variables**: Define environment-specific variables using the `env` key in your `cypress.json` file or by passing them via the command line.
    Alternatively, use the command line to override:

    ```
    {
      "env": {
        "apiUrl": "https://api.staging.example.com"
      }
    }
    ```

    ```
    npx cypress run --env apiUrl=https://api.staging.example.com
    ```

  2. **Configuration Files**: For more complex [setups](../S/setup.md), consider having separate configuration files for each environment, like `cypress.staging.json` and `cypress.production.json`. Use the `--config-file` flag to specify the configuration file when running tests.

    ```
    npx cypress run --config-file cypress.staging.json
    ```

  3. **Dynamic Configuration**: In your `plugins/index.js` file, you can programmatically alter the configuration based on environment variables or other conditions.

    ```
    module.exports = (on, config) => {
      if (process.env.NODE_ENV === 'staging') {
        config.baseUrl = 'https://staging.example.com';
        // Modify other config settings as needed
      }
      return config;
    };
    ```

  4. **[Cypress](../C/cypress.md).env()**: Access environment variables in your tests using `Cypress.env('variableName')`.

    ```
    const apiUrl = Cypress.env('apiUrl');
    ```

### Writing and Running Tests

#### How to write a basic test in Cypress?

  To write a basic test in [Cypress](../C/cypress.md), follow these steps:

  1. **Create a new test file** in your [Cypress](../C/cypress.md) integration folder, typically with a `.spec.js` extension, for example, `login.spec.js`.
  2. **Start by requiring [Cypress](../C/cypress.md)** at the top of your test file:

  ```
  /// <reference types="cypress" />
  ```

  1. **Describe your [test suite](../T/test-suite.md)**
    using the
    `describe`
    function, providing a title and a callback function to contain your tests:

  ```
  describe('Login Test', () => {
    // Your tests will go here
  });
  ```

  1. **Write individual [test cases](../T/test-case.md)**
    within the
    `describe`
    block using the
    `it`
    function. Each
    `it`
    function takes a title for the test case and a callback function to execute the test steps:

  ```
  it('successfully logs in', () => {
    // Test steps will go here
  });
  ```

  1. **Define the test steps**
    within the
    `it`
    callback. Use Cypress commands to interact with the application:

  ```
  it('successfully logs in', () => {
    cy.visit('/login'); // Navigate to the login page
    cy.get('input[name=username]').type('user@example.com'); // Type the username
    cy.get('input[name=password]').type('password123'); // Type the password
    cy.get('form').submit(); // Submit the login form
    cy.url().should('include', '/dashboard'); // Assert the URL to ensure login was successful
  });
  ```

  1. **Run your test**
    using the Cypress Test Runner or via the command line with
    `cypress open`
    or
    `cypress run`
    .
  Remember to **keep tests isolated** and **independent** for reliability. Use `beforeEach` or `before` hooks if you need to set up state before each test or once before all tests in the suite, respectively.

  1. **Create a new test file** in your [Cypress](../C/cypress.md) integration folder, typically with a `.spec.js` extension, for example, `login.spec.js`.
  2. **Start by requiring [Cypress](../C/cypress.md)** at the top of your test file:
  1. **Describe your [test suite](../T/test-suite.md)**
    using the
    `describe`
    function, providing a title and a callback function to contain your tests:

  1. **Write individual [test cases](../T/test-case.md)**
    within the
    `describe`
    block using the
    `it`
    function. Each
    `it`
    function takes a title for the test case and a callback function to execute the test steps:

  1. **Define the test steps**
    within the
    `it`
    callback. Use Cypress commands to interact with the application:

  1. **Run your test**
    using the Cypress Test Runner or via the command line with
    `cypress open`
    or
    `cypress run`
    .

#### What is the structure of a Cypress test?

  A [Cypress](../C/cypress.md) test typically follows a structure that includes importing necessary dependencies, describing [test suites](../T/test-suite.md), defining [test cases](../T/test-case.md), and implementing test steps with assertions. Here's an example of a basic [Cypress](../C/cypress.md) test structure:

  ```
  // Import the Cypress module
  import cy from 'cypress';
  // Describe the test suite
  describe('User Login', () => {
    // Before each test, do some common setup (optional)
    beforeEach(() => {
      // Visit the login page
      cy.visit('/login');
    });
    // Define a test case
    it('should login with valid credentials', () => {
      // Test steps
      cy.get('input[name="username"]').type('user');
      cy.get('input[name="password"]').type('password');
      cy.get('form').submit();
      // Assertions
      cy.url().should('include', '/dashboard');
      cy.get('.welcome-message').should('contain', 'Welcome, user');
    });
    // Define another test case
    it('should display an error for invalid credentials', () => {
      // Test steps
      cy.get('input[name="username"]').type('wronguser');
      cy.get('input[name="password"]').type('wrongpassword');
      cy.get('form').submit();
      // Assertions
      cy.get('.error-message').should('be.visible');
    });
  });
  ```
  In this structure:

  - **describe**
    blocks group related tests, known as a test suite.

  - **it**
    blocks define individual test cases.

  - **beforeEach**
    is a hook for setting up conditions before each test runs.

  - **cy.visit**
    navigates to a URL.

  - **cy.get**
    selects DOM elements.

  - **type**
    and
    **submit**
    simulate user actions.

  - **should**
    is used for assertions to verify the desired state.

  - **describe**
    blocks group related tests, known as a test suite.

  - **it**
    blocks define individual test cases.

  - **beforeEach**
    is a hook for setting up conditions before each test runs.

  - **cy.visit**
    navigates to a URL.

  - **cy.get**
    selects DOM elements.

  - **type**
    and
    **submit**
    simulate user actions.

  - **should**
    is used for assertions to verify the desired state.

#### How to run a test in Cypress?

  To run a test in [Cypress](../C/cypress.md), follow these steps:

  1. Open your terminal or command prompt.
  2. Navigate to your project directory where Cypress is installed.
  3. Execute the following command to open the Cypress Test Runner:

  ```
  npx cypress open
  ```

  1. The Cypress Test Runner GUI will launch, displaying a list of your test files.
  2. Click on the test file you want to run. Cypress will execute the tests in that file and display the results in real-time.
  Alternatively, to run tests headlessly without opening the [Test Runner](../T/test-runner.md) GUI:

  1. Use the following command in your terminal:

  ```
  npx cypress run
  ```

  1. This will run all test files in the default headless browser (Electron).
  For running tests in a specific browser, use the `--browser` flag:

  ```
  npx cypress run --browser chrome
  ```
  To run a specific test file, append the `--spec` flag followed by the path to the test file:

  ```
  npx cypress run --spec "cypress/integration/example.spec.js"
  ```
  To run tests with additional configuration options, use the `--config` flag:

  ```
  npx cypress run --config video=false
  ```
  This command will run tests without recording a video.
  For parallel [test execution](../T/test-execution.md) and load balancing across multiple machines or CI containers, use the [Cypress](../C/cypress.md) Dashboard service, which requires additional [setup](../S/setup.md) and configuration.

  1. Open your terminal or command prompt.
  2. Navigate to your project directory where Cypress is installed.
  3. Execute the following command to open the Cypress Test Runner:
  1. The Cypress Test Runner GUI will launch, displaying a list of your test files.
  2. Click on the test file you want to run. Cypress will execute the tests in that file and display the results in real-time.
  1. Use the following command in your terminal:
  1. This will run all test files in the default headless browser (Electron).

#### How to use assertions in Cypress?

  Using assertions in [Cypress](../C/cypress.md) is crucial for verifying that the application under test behaves as expected. [Cypress](../C/cypress.md) uses Chai for assertions, which provides `expect`, `assert`, and `should` syntax.
  **Expect** and **should** are [BDD](../B/bdd.md) (Behavior-Driven Development) style assertions, while **assert** is TDD ([Test-Driven Development](../T/test-driven-development.md)) style. Here's how you can use them:
  **Expect:**

  ```
  expect(variable).to.equal(value);
  expect(element).to.have.class(className);
  ```
  **Should:**

  ```
  cy.get(selector).should('have.class', className);
  cy.get(selector).should('contain', text);
  ```
  **Assert:**

  ```
  assert.equal(variable, value, 'Optional message');
  assert.isTrue(condition, 'Optional message');
  ```
  [Cypress](../C/cypress.md) assertions are automatically retried until they pass or time out, which is defined by the `defaultCommandTimeout` configuration.
  Chain assertions for more complex checks:

  ```
  cy.get(selector).should('be.visible').and('contain', text);
  ```
  Use `.and` to chain multiple assertions on the same subject.
  For assertions on network requests:

  ```
  cy.request('GET', '/api/data').then((response) => {
    expect(response.status).to.eq(200);
    expect(response.body).to.have.property('data');
  });
  ```
  Remember to leverage [Cypress](../C/cypress.md)'s built-in assertions for common conditions, such as visibility or existence of elements, which simplifies the syntax and improves readability:

  ```
  cy.get(selector).should('be.visible');
  cy.get(selector).should('exist');
  ```
  By using assertions effectively, you ensure that your tests accurately validate the behavior of your application.

#### How to handle events in Cypress?

  Handling events in [Cypress](../C/cypress.md) is straightforward due to its jQuery-like syntax. To interact with elements and handle events, you can use [Cypress](../C/cypress.md) commands that simulate user actions.
  For example, to handle a click event, you would use the `.click()` command:

  ```
  cy.get('button').click();
  ```
  To handle form submission, you can use the `.submit()` command:

  ```
  cy.get('form').submit();
  ```
  For keyboard events, such as typing into an input field, use the `.type()` command:

  ```
  cy.get('input').type('Hello, World!');
  ```
  To handle more complex events like hover, [Cypress](../C/cypress.md) does not natively support the `hover` event as a user would experience it. Instead, you can trigger the same functionality using the `.trigger()` command:

  ```
  cy.get('div').trigger('mouseover');
  ```
  For events that require waiting for a specific condition, you can use `.wait()` in combination with other commands:

  ```
  cy.wait(1000); // Waits for 1 second
  cy.get('button').click();
  ```
  Remember that [Cypress](../C/cypress.md) automatically waits for elements to exist and will retry commands until the elements are actionable. This means you often don't need to manually handle events that depend on previous actions or asynchronous operations.
  For custom events or more complex scenarios, you can define custom commands using `Cypress.Commands.add()` to encapsulate reusable event handling logic:

  ```
  Cypress.Commands.add('customEvent', (selector, event) => {
    cy.get(selector).trigger(event);
  });
  // Usage
  cy.customEvent('button', 'customEventName');
  ```
  Always ensure you understand the application's behavior to correctly simulate events and achieve reliable test results.

#### How to use fixtures in Cypress?

  Using fixtures in [Cypress](../C/cypress.md) is a way to manage [test data](../T/test-data.md) separately from [test scripts](../T/test-script.md), allowing you to load static data that can be used across multiple tests. Here's how to use fixtures in [Cypress](../C/cypress.md):

  1. **Create a fixture file** : Place a JSON file inside the
    `cypress/fixtures`
    directory. For example,
    `user.json`
    could contain:

  ```
  {
    "id": 1,
    "name": "Jane Doe",
    "email": "jane.doe@example.com"
  }
  ```

  1. **Load a fixture** : Use the
    `cy.fixture()`
    function to load the fixture data. You can then use this data within your test.

  ```
  describe('Test with fixtures', () => {
    it('Loads data from a fixture', () => {
      cy.fixture('user').then((user) => {
        // user now contains the fixture data
      });
    });
  });
  ```

  1. **Use fixture data in tests** : Once the fixture is loaded, you can use the data in your test logic, such as filling out forms or comparing against expected values.

  ```
  cy.get('input[name="name"]').type(user.name);
  cy.get('input[name="email"]').type(user.email);
  ```

  1. **Shortcut for loading fixtures** : You can also pass the fixture file directly to commands like
    `cy.get()`
    or
    `cy.route()`
    using the
    `@`
    prefix.

  ```
  cy.get('input[name="name"]').type('@user.name');
  ```

  1. **Alias fixture data** : To make fixtures easier to manage within a test, you can assign an alias to the fixture using
    `as()`
    .

  ```
  cy.fixture('user').as('userData');
  cy.get('@userData').then((user) => {
    // use user data here
  });
  ```
  Remember to keep your fixture data up-to-date and relevant to the tests you are performing. This will ensure your tests remain reliable and maintainable.

  1. **Create a fixture file** : Place a JSON file inside the
    `cypress/fixtures`
    directory. For example,
    `user.json`
    could contain:

  1. **Load a fixture** : Use the
    `cy.fixture()`
    function to load the fixture data. You can then use this data within your test.

  1. **Use fixture data in tests** : Once the fixture is loaded, you can use the data in your test logic, such as filling out forms or comparing against expected values.
  1. **Shortcut for loading fixtures** : You can also pass the fixture file directly to commands like
    `cy.get()`
    or
    `cy.route()`
    using the
    `@`
    prefix.

  1. **Alias fixture data** : To make fixtures easier to manage within a test, you can assign an alias to the fixture using
    `as()`
    .

### Advanced Concepts

#### How does Cypress handle asynchronous operations?

  [Cypress](../C/cypress.md) handles asynchronous operations by automatically waiting for commands and assertions before moving on to the next step. This means that it will wait for elements to become visible, for animations to complete, and for network requests to finish before executing the next command. There's no need to add explicit waits or sleeps in your tests.
  For example, when you use a command to get an element, [Cypress](../C/cypress.md) will continuously retry this command until the element is found or a timeout is reached. This applies to most commands in [Cypress](../C/cypress.md):

  ```
  cy.get('.some-element') // Cypress will wait for this element to exist
  ```
  When dealing with network requests, [Cypress](../C/cypress.md) provides `cy.wait()` to wait for a specific request to complete:

  ```
  cy.wait('@yourRequestAlias')
  ```
  You can also handle the response of asynchronous requests using `.then()`:

  ```
  cy.request('POST', '/yourEndpoint', yourRequestBody)
    .then((response) => {
      expect(response.body).to.have.property('success', true);
    });
  ```
  [Cypress](../C/cypress.md) ensures that the test does not proceed until the asynchronous operation inside `.then()` is completed.
  For assertions, [Cypress](../C/cypress.md) uses a retry-and-timeout mechanism. Assertions will re-run until they pass or until a specified timeout is reached:

  ```
  cy.get('.list-item').should('have.length', 5) // Retries until the condition is met or timeout
  ```
  This approach simplifies handling asynchronous operations, making tests more readable and less flaky.

#### How to use custom commands in Cypress?

  Using custom commands in [Cypress](../C/cypress.md) can enhance your [test suite](../T/test-suite.md) by encapsulating repetitive tasks. To define a custom command, add a function to the `Cypress.Commands.add` method in the `commands.js` file located in the `cypress/support` directory.

  ```
  Cypress.Commands.add('login', (email, password) => {
    cy.get('input[name=email]').type(email);
    cy.get('input[name=password]').type(password);
    cy.get('form').submit();
  });
  ```
  Invoke custom commands in your tests using `cy` followed by the command name:

  ```
  cy.login('user@example.com', 'password123');
  ```
  **Parameters** can be passed to custom commands just like any other function. In the example above, `email` and `password` are the parameters.
  **Chaining** is supported by custom commands. Return `cy` from your custom command to continue chaining [Cypress](../C/cypress.md) commands:

  ```
  Cypress.Commands.add('fillForm', data => {
    return cy.get('form').within(() => {
      cy.get('input[name=firstName]').type(data.firstName);
      cy.get('input[name=lastName]').type(data.lastName);
    });
  });
  ```
  **Overwriting** existing commands is possible by using the same `Cypress.Commands.add` method with the name of an existing command:

  ```
  Cypress.Commands.overwrite('visit', (originalFn, url, options) => {
    // Custom logic before visit
    return originalFn(url, options);
  });
  ```
  Remember to **document** your custom commands to ensure team members understand their purpose and usage. Keep custom commands **maintainable** by limiting their scope and complexity.

#### How to handle network requests in Cypress?

  Handling network requests in [Cypress](../C/cypress.md) can be achieved using the `cy.intercept()` method. This allows you to listen to, modify, or mock network requests and responses.
  **Intercepting a GET request:**

  ```
  cy.intercept('GET', '/api/todos').as('getTodos')
  ```
  After setting up an intercept, you can wait for the request to complete using `cy.wait()`:

  ```
  cy.wait('@getTodos').its('response.statusCode').should('eq', 200)
  ```
  **Modifying a response:**
  You can modify the response by providing a static response:

  ```
  cy.intercept('GET', '/api/todos', { fixture: 'todos.json' })
  ```
  **Stubbing a response:**
  To stub a response, you can provide the response directly:

  ```
  cy.intercept('POST', '/api/todos', {
    statusCode: 201,
    body: { id: 123, title: 'Stubbed task' },
  }).as('createTodo')
  ```
  **Accessing request and response:**
  You can access the request and response objects in the intercept callback:

  ```
  cy.intercept('POST', '/api/todos', (req) => {
    req.body.title = 'Modified title'
  }).as('createTodo')
  ```
  **Chaining assertions:**
  You can chain assertions to the intercepted request:

  ```
  cy.wait('@createTodo').then(({ request, response }) => {
    expect(request.body).to.have.property('title', 'Modified title')
    expect(response.statusCode).to.eq(201)
  })
  ```
  Use `cy.intercept()` to gain full control over network requests and responses, enabling you to test your application's behavior under various scenarios.

#### How to work with cookies and local storage in Cypress?

  Working with cookies and local storage in [Cypress](../C/cypress.md) is straightforward due to its built-in commands.
  **Cookies:**
  To get a cookie by name:

  ```
  cy.getCookie('session_id').should('exist')
  ```
  To get all cookies:

  ```
  cy.getCookies().should('have.length', 1)
  ```
  To set a cookie:

  ```
  cy.setCookie('session_id', 'abc123')
  ```
  To clear a specific cookie:

  ```
  cy.clearCookie('session_id')
  ```
  To clear all cookies:

  ```
  cy.clearCookies()
  ```
  **Local Storage:**
  To set an item in local storage:

  ```
  cy.setLocalStorage('cart', JSON.stringify({ items: 1 }))
  ```
  To get an item from local storage:

  ```
  cy.getLocalStorage('cart').should('equal', '{"items":1}')
  ```
  To clear specific item from local storage:

  ```
  cy.removeLocalStorage('cart')
  ```
  To clear all local storage data:

  ```
  cy.clearLocalStorage()
  ```
  Or to clear local storage with a specific key pattern:

  ```
  cy.clearLocalStorage(/cart/)
  ```
  Remember, these commands are asynchronous and return promises, so they should be used with [Cypress](../C/cypress.md)'s chaining mechanism. Also, local storage operations are typically performed in the context of the application under test, so ensure the correct page is loaded before attempting to interact with local storage.

#### How to handle iframes in Cypress?

  Handling iframes in [Cypress](../C/cypress.md) requires a few additional steps because [Cypress](../C/cypress.md) commands are designed to operate within the same-origin context. Here's a succinct guide:

  1. **Target the iframe**
    - Use
    `cy.get()`
    to grab the iframe element.

  ```
  cy.get('iframe')
  ```

  1. **Access the iframe's content**
    - Use
    `.its('contentDocument.body')`
    to get the body of the iframe, which is subject to same-origin policy restrictions.

  ```
  cy.get('iframe').its('contentDocument.body').should('not.be.empty').then(cy.wrap)
  ```

  1. **Interact with elements**
    - Once wrapped, you can interact with the elements inside the iframe as you would with any other element in Cypress.

  ```
  cy.get('iframe').its('contentDocument.body').should('not.be.empty').then(cy.wrap).find('selector').click()
  ```
  Remember that for cross-origin iframes, you'll need to set `"chromeWebSecurity": false` in your `cypress.json` configuration file to bypass these restrictions. However, this is not recommended for security reasons and should only be used when absolutely necessary.
  If you're dealing with multiple nested iframes, you'll need to repeat the process for each level of iframe nesting, ensuring that you target the correct iframe at each level.
  Keep in mind that [Cypress](../C/cypress.md) best practices recommend avoiding iframes when possible, as they add complexity to your tests. If you have control over the application, consider alternatives to iframes that are more test-friendly.

  1. **Target the iframe**
    - Use
    `cy.get()`
    to grab the iframe element.

  1. **Access the iframe's content**
    - Use
    `.its('contentDocument.body')`
    to get the body of the iframe, which is subject to same-origin policy restrictions.

  1. **Interact with elements**
    - Once wrapped, you can interact with the elements inside the iframe as you would with any other element in Cypress.

#### How to use plugins in Cypress?

  Using plugins in [Cypress](../C/cypress.md) enhances its capabilities by extending its core functionality. To use a plugin, follow these steps:

  1. **Install the plugin** via npm. For example, to install the `cypress-file-upload` plugin, run:

    ```
    npm install --save-dev cypress-file-upload
    ```

  2. **Include the plugin** in your project's `cypress/plugins/index.js` file. This is where you modify or extend the internal behavior of [Cypress](../C/cypress.md). For instance:

    ```
    module.exports = (on, config) => {
      // your plugin code here
    }
    ```

  3. **Import and use the plugin** in your test files as needed. For example, with `cypress-file-upload`, you would add the following to your test file:

    ```
    import 'cypress-file-upload';
    ```

  4. **Utilize the plugin's features** in your tests. For the `cypress-file-upload` plugin, you can now use the `.attachFile()` command:

    ```
    cy.get('input[type="file"]').attachFile('file.json');
    ```
  Remember to **check the plugin's documentation** for specific usage instructions and compatibility with your version of [Cypress](../C/cypress.md). Some plugins may require additional configuration or initialization steps.
  Plugins can provide a variety of functionalities, such as custom commands, improved reporting, or integration with other tools. Always **ensure that the plugin is actively maintained** and well-suited for your needs before adding it to your project.

  1. **Install the plugin** via npm. For example, to install the `cypress-file-upload` plugin, run:

    ```
    npm install --save-dev cypress-file-upload
    ```

  2. **Include the plugin** in your project's `cypress/plugins/index.js` file. This is where you modify or extend the internal behavior of [Cypress](../C/cypress.md). For instance:

    ```
    module.exports = (on, config) => {
      // your plugin code here
    }
    ```

  3. **Import and use the plugin** in your test files as needed. For example, with `cypress-file-upload`, you would add the following to your test file:

    ```
    import 'cypress-file-upload';
    ```

  4. **Utilize the plugin's features** in your tests. For the `cypress-file-upload` plugin, you can now use the `.attachFile()` command:

    ```
    cy.get('input[type="file"]').attachFile('file.json');
    ```

### Best Practices and Troubleshooting

#### What are some best practices for writing tests in Cypress?

  When writing tests in [Cypress](../C/cypress.md), consider the following best practices:

  - **Organize tests logically**
    using
    `describe`
    and
    `context`
    blocks for better readability and structure.

  - **Use `it` blocks**
    for individual test cases, ensuring they are descriptive and reflect the user behavior you're testing.

  - **Keep tests isolated and independent**
    to avoid inter-test dependencies that can cause flakiness.

  - **Employ [Page Object Model](../P/page-object-model.md)**
    or similar patterns to abstract element selectors and page interactions, enhancing maintainability.

  - **Utilize [Cypress](../C/cypress.md)'s built-in retry-ability**
    for commands and assertions to handle dynamic content and reduce flakiness.

  - **Avoid using arbitrary waits**
    (
    `cy.wait()`
    with a fixed time); instead, rely on Cypress's automatic waiting for elements to exist, be visible, be clickable, etc.

  - **Leverage [Cypress](../C/cypress.md) aliases**
    with
    `cy.as()`
    for reusing elements or responses in a chain of commands.

  - **Write custom commands**
    for reusable sequences of actions, but use them judiciously to keep the clarity of the tests.

  - **Assert on real user interactions**
    and outcomes, not implementation details, to ensure tests remain valid with code changes.

  - **Test the critical user journeys**
    first to provide immediate value and catch significant regressions early.

  - **Use environment variables**
    for configuration to keep sensitive data out of the test code and allow flexibility across different environments.

  - **Implement Continuous Integration**
    to run tests automatically on code changes, ensuring immediate feedback on the health of the application.

  ```
  // Example of a descriptive test case
  describe('User Profile', () => {
    it('should allow a user to update their profile picture', () => {
      cy.get('.profile-pic').click();
      cy.get('input[type="file"]').attachFile('new-pic.jpg');
      cy.get('.save-btn').click();
      cy.get('.profile-pic').should('have.attr', 'src', 'path/to/new-pic.jpg');
    });
  });
  ```
  Remember to **review and refactor tests regularly** to adapt to application changes and improve [test suite](../T/test-suite.md) reliability and performance.

  - **Organize tests logically**
    using
    `describe`
    and
    `context`
    blocks for better readability and structure.

  - **Use `it` blocks**
    for individual test cases, ensuring they are descriptive and reflect the user behavior you're testing.

  - **Keep tests isolated and independent**
    to avoid inter-test dependencies that can cause flakiness.

  - **Employ [Page Object Model](../P/page-object-model.md)**
    or similar patterns to abstract element selectors and page interactions, enhancing maintainability.

  - **Utilize [Cypress](../C/cypress.md)'s built-in retry-ability**
    for commands and assertions to handle dynamic content and reduce flakiness.

  - **Avoid using arbitrary waits**
    (
    `cy.wait()`
    with a fixed time); instead, rely on Cypress's automatic waiting for elements to exist, be visible, be clickable, etc.

  - **Leverage [Cypress](../C/cypress.md) aliases**
    with
    `cy.as()`
    for reusing elements or responses in a chain of commands.

  - **Write custom commands**
    for reusable sequences of actions, but use them judiciously to keep the clarity of the tests.

  - **Assert on real user interactions**
    and outcomes, not implementation details, to ensure tests remain valid with code changes.

  - **Test the critical user journeys**
    first to provide immediate value and catch significant regressions early.

  - **Use environment variables**
    for configuration to keep sensitive data out of the test code and allow flexibility across different environments.

  - **Implement Continuous Integration**
    to run tests automatically on code changes, ensuring immediate feedback on the health of the application.

#### How to debug tests in Cypress?

  Debugging tests in [Cypress](../C/cypress.md) can be approached systematically:

  1. **Use the [Cypress](../C/cypress.md) [Test Runner](../T/test-runner.md)**: It provides a visual representation of [test execution](../T/test-execution.md). You can see commands as they run and inspect the state of the application at each step.
  2. **Time Travel**: [Cypress](../C/cypress.md) takes snapshots as your tests run. Hover over commands in the Command Log to see exactly what happened at each step.
  3. **Real-Time Reloads**: [Cypress](../C/cypress.md) automatically reloads whenever you make changes to your tests. You can see test results instantly.
  4. **Console Output**: Check the browser's developer console for logs. [Cypress](../C/cypress.md) commands log additional information here, which can be useful for debugging.
  5. **`.debug()` Command**: Insert `.debug()` into your chain of commands to inspect the state of the DOM at that point. It will cause the browser's debugger to kick in.

    ```
    cy.get('.selector').debug().should('have.text', 'expected text');
    ```

  6. **Breakpoints**: Use `debugger` statements in your test code to pause execution at a specific line.

    ```
    cy.get('.selector').then(($el) => {
      debugger; // Execution will pause here
    });
    ```

  7. **Network Requests**: Inspect network requests in the [Test Runner](../T/test-runner.md)'s Command Log to ensure [API](../A/api.md) calls are being made as expected and with the correct data.
  8. **Error Messages**: Read error messages carefully. [Cypress](../C/cypress.md) provides descriptive error messages that can guide you to the source of the problem.
  9. **[Cypress](../C/cypress.md) Logs**: Enable verbose logging by setting `Cypress.config('log', true)` to get more detailed information about the [test execution](../T/test-execution.md).
  10. **Retry-ability**: Understand that [Cypress](../C/cypress.md) commands automatically retry until they succeed or time out. If a test is failing because an assertion is running before the application is ready, consider adding waits or assertions for intermediate states.
  By combining these tools and techniques, you can effectively debug your [Cypress](../C/cypress.md) tests and resolve issues more quickly.

  1. **Use the [Cypress](../C/cypress.md) [Test Runner](../T/test-runner.md)**: It provides a visual representation of [test execution](../T/test-execution.md). You can see commands as they run and inspect the state of the application at each step.
  2. **Time Travel**: [Cypress](../C/cypress.md) takes snapshots as your tests run. Hover over commands in the Command Log to see exactly what happened at each step.
  3. **Real-Time Reloads**: [Cypress](../C/cypress.md) automatically reloads whenever you make changes to your tests. You can see test results instantly.
  4. **Console Output**: Check the browser's developer console for logs. [Cypress](../C/cypress.md) commands log additional information here, which can be useful for debugging.
  5. **`.debug()` Command**: Insert `.debug()` into your chain of commands to inspect the state of the DOM at that point. It will cause the browser's debugger to kick in.

    ```
    cy.get('.selector').debug().should('have.text', 'expected text');
    ```

  6. **Breakpoints**: Use `debugger` statements in your test code to pause execution at a specific line.

    ```
    cy.get('.selector').then(($el) => {
      debugger; // Execution will pause here
    });
    ```

  7. **Network Requests**: Inspect network requests in the [Test Runner](../T/test-runner.md)'s Command Log to ensure [API](../A/api.md) calls are being made as expected and with the correct data.
  8. **Error Messages**: Read error messages carefully. [Cypress](../C/cypress.md) provides descriptive error messages that can guide you to the source of the problem.
  9. **[Cypress](../C/cypress.md) Logs**: Enable verbose logging by setting `Cypress.config('log', true)` to get more detailed information about the [test execution](../T/test-execution.md).
  10. **Retry-ability**: Understand that [Cypress](../C/cypress.md) commands automatically retry until they succeed or time out. If a test is failing because an assertion is running before the application is ready, consider adding waits or assertions for intermediate states.

#### How to handle common errors in Cypress?

  Handling common errors in [Cypress](../C/cypress.md) involves understanding the error messages and applying appropriate fixes or workarounds. Here are some strategies:
  **Timeout Errors**: Increase default timeout settings using `cy.wait()` or globally in `cypress.json` if elements take longer to load.

  ```
  cy.get('.some-element', { timeout: 10000 }) // waits for 10 seconds
  ```
  **Element Not Found**: Ensure elements are available in the DOM before interacting with them. Use `.should('be.visible')` to wait for elements to appear.

  ```
  cy.get('.some-element').should('be.visible').click()
  ```
  **Cross-Origin Errors**: Configure `chromeWebSecurity` to `false` in `cypress.json` if you need to bypass the same-origin policy.

  ```
  {
    "chromeWebSecurity": false
  }
  ```
  **[Flaky Tests](../F/flaky-test.md)**: Address flakiness by using `.retry()` for assertions or commands that might fail due to timing issues.

  ```
  cy.get('.some-element').should('exist').retry()
  ```
  **Assertion Failures**: Review the expected conditions and ensure the assertions match the actual application state. Use explicit assertions like `.should('have.text', 'expected text')`.

  ```
  cy.get('.some-element').should('have.text', 'expected text')
  ```
  **Network Errors**: Stub network requests using `cy.intercept()` to control the response and avoid external dependencies.

  ```
  cy.intercept('GET', '/api/data', { fixture: 'data.json' })
  ```
  **Unhandled Promise Rejections**: Use `.catch()` to handle promise rejections within tests and avoid uncaught exceptions.

  ```
  cy.task('mightFail').catch((error) => {
    // handle error
  })
  ```
  **[Cypress](../C/cypress.md) Command Queue Errors**: Remember that [Cypress](../C/cypress.md) commands are asynchronous and queued. Avoid using traditional async/await with [Cypress](../C/cypress.md) commands.
  For more complex or persistent errors, consult the [Cypress](../C/cypress.md) documentation or community forums for specific solutions and troubleshooting tips.

#### How to optimize test execution time in Cypress?

  To optimize [test execution](../T/test-execution.md) time in [Cypress](../C/cypress.md), consider the following strategies:

  - **Run tests in parallel**: Utilize [Cypress](../C/cypress.md) Dashboard Service to run tests simultaneously across multiple machines. This can significantly reduce the overall [test suite](../T/test-suite.md) execution time.

    ```
    cypress run --record --key <record_key> --parallel
    ```

  - **Selective [test execution](../T/test-execution.md)**: Use `.only` to run specific tests or [test suites](../T/test-suite.md) during development to avoid running the entire suite.

    ```
    describe.only('My Test Suite', () => {
      // Only this suite will run
    });
    it.only('My Test', () => {
      // Only this test will run
    });
    ```

  - **Test retries**: Implement test retries to handle [flaky tests](../F/flaky-test.md) without rerunning the entire suite.

    ```
    // Global level
    Cypress.config('retries', 2);
    // Test-specific level
    it('retries test', { retries: 2 }, () => {
      // Test code here
    });
    ```

  - **Smart waiting**: Use [Cypress](../C/cypress.md)'s automatic waiting for elements and assertions to avoid unnecessary waits and timeouts.
  - **Stubbing and intercepting**: Replace actual network calls with stubs using `cy.intercept()` to save time spent on real network requests.

    ```
    cy.intercept('GET', '/users', { fixture: 'users.json' });
    ```

  - **Avoid unnecessary UI actions**: Use direct [API](../A/api.md) calls to set up application state instead of going through UI workflows.

    ```
    cy.request('POST', '/login', { username: 'user', password: 'pass' });
    ```

  - **Cache resources**: Cache data that doesn't change often between tests to avoid reloading.
  - **Optimize selectors**: Use efficient selectors to reduce the time [Cypress](../C/cypress.md) spends querying the DOM.
  - **Batch actions**: Group actions or commands that can be executed together to minimize the number of yieldable [Cypress](../C/cypress.md) commands.
  By implementing these strategies, you can achieve faster feedback cycles and more efficient [test execution](../T/test-execution.md) in [Cypress](../C/cypress.md).

  - **Run tests in parallel**: Utilize [Cypress](../C/cypress.md) Dashboard Service to run tests simultaneously across multiple machines. This can significantly reduce the overall [test suite](../T/test-suite.md) execution time.

    ```
    cypress run --record --key <record_key> --parallel
    ```

  - **Selective [test execution](../T/test-execution.md)**: Use `.only` to run specific tests or [test suites](../T/test-suite.md) during development to avoid running the entire suite.

    ```
    describe.only('My Test Suite', () => {
      // Only this suite will run
    });
    it.only('My Test', () => {
      // Only this test will run
    });
    ```

  - **Test retries**: Implement test retries to handle [flaky tests](../F/flaky-test.md) without rerunning the entire suite.

    ```
    // Global level
    Cypress.config('retries', 2);
    // Test-specific level
    it('retries test', { retries: 2 }, () => {
      // Test code here
    });
    ```

  - **Smart waiting**: Use [Cypress](../C/cypress.md)'s automatic waiting for elements and assertions to avoid unnecessary waits and timeouts.
  - **Stubbing and intercepting**: Replace actual network calls with stubs using `cy.intercept()` to save time spent on real network requests.

    ```
    cy.intercept('GET', '/users', { fixture: 'users.json' });
    ```

  - **Avoid unnecessary UI actions**: Use direct [API](../A/api.md) calls to set up application state instead of going through UI workflows.

    ```
    cy.request('POST', '/login', { username: 'user', password: 'pass' });
    ```

  - **Cache resources**: Cache data that doesn't change often between tests to avoid reloading.
  - **Optimize selectors**: Use efficient selectors to reduce the time [Cypress](../C/cypress.md) spends querying the DOM.
  - **Batch actions**: Group actions or commands that can be executed together to minimize the number of yieldable [Cypress](../C/cypress.md) commands.
