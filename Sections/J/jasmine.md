# Jasmine


<!-- TOC START -->
- [Related Terms:](#related-terms)
  - [See also:](#see-also)
- [Questions about Jasmine ?](#questions-about-jasmine)
  - [Basics and Importance](#basics-and-importance)
    - [What is Jasmine in the context of software testing?](#what-is-jasmine-in-the-context-of-software-testing)
    - [Why is Jasmine considered important in e2e testing?](#why-is-jasmine-considered-important-in-e2e-testing)
    - [What are the key features of Jasmine?](#what-are-the-key-features-of-jasmine)
    - [How does Jasmine compare to other testing frameworks?](#how-does-jasmine-compare-to-other-testing-frameworks)
  - [Installation and Setup](#installation-and-setup)
    - [How do you install Jasmine for JavaScript testing?](#how-do-you-install-jasmine-for-javascript-testing)
    - [What are the prerequisites for installing Jasmine?](#what-are-the-prerequisites-for-installing-jasmine)
    - [How do you set up a basic Jasmine test environment?](#how-do-you-set-up-a-basic-jasmine-test-environment)
  - [Test Writing](#test-writing)
    - [How do you write a basic test in Jasmine?](#how-do-you-write-a-basic-test-in-jasmine)
    - [What is the structure of a Jasmine test?](#what-is-the-structure-of-a-jasmine-test)
    - [How do you use 'describe' and 'it' functions in Jasmine?](#how-do-you-use-describe-and-it-functions-in-jasmine)
    - [What are 'beforeEach' and 'afterEach' functions in Jasmine and how are they used?](#what-are-beforeeach-and-aftereach-functions-in-jasmine-and-how-are-they-used)
  - [Assertions and Matchers](#assertions-and-matchers)
    - [What are Jasmine matchers and how are they used?](#what-are-jasmine-matchers-and-how-are-they-used)
    - [How do you create custom matchers in Jasmine?](#how-do-you-create-custom-matchers-in-jasmine)
    - [What are the different types of assertions in Jasmine?](#what-are-the-different-types-of-assertions-in-jasmine)
  - [Spies and Mocking](#spies-and-mocking)
    - [What are Jasmine spies and how are they used?](#what-are-jasmine-spies-and-how-are-they-used)
    - [How do you create a mock in Jasmine?](#how-do-you-create-a-mock-in-jasmine)
    - [What is the difference between a spy and a mock in Jasmine?](#what-is-the-difference-between-a-spy-and-a-mock-in-jasmine)
  - [Advanced Concepts](#advanced-concepts)
    - [How do you handle asynchronous testing in Jasmine?](#how-do-you-handle-asynchronous-testing-in-jasmine)
    - [How do you use Jasmine with other libraries or frameworks like Angular or React?](#how-do-you-use-jasmine-with-other-libraries-or-frameworks-like-angular-or-react)
    - [What are some best practices for writing tests in Jasmine?](#what-are-some-best-practices-for-writing-tests-in-jasmine)
<!-- TOC END -->

Jasmine

is an open-source testing framework for JavaScript. It is designed to be behavior-driven, allowing developers to write tests in a way that describes the expected behavior of the software in clear, human-readable terms.

Jasmine

provides functions to structure your tests, set up preconditions, and define assertions.

## Related Terms:

- [Testing framework](../T/testing-framework.md)
- [Jest](../J/jest.md)
- [Chai.js](../C/chaijs.md)

### See also:

- [Official Website](https://jasmine.github.io/)
- [Wikipedia](https://en.wikipedia.org/wiki/Jasmine_(software))

## Questions about Jasmine ?

### Basics and Importance

#### What is Jasmine in the context of software testing?

  [Jasmine](../J/jasmine.md) is a **behavior-driven development ([BDD](../B/bdd.md))** framework for testing JavaScript code. It does not rely on browsers, DOM, or any JavaScript framework, making it suitable for testing any JavaScript application. [Jasmine](../J/jasmine.md)'s syntax is designed to be easy to read and write, aiming to be both expressive and comprehensive.
  Tests in [Jasmine](../J/jasmine.md) are called **specs**, which are defined by calling the global `it` function. Specs are grouped into suites, which are defined by calling the global `describe` function. Suites can be nested within other suites, allowing for a hierarchical structure to organize tests.
  [Jasmine](../J/jasmine.md) provides built-in **matchers** that let you express expectations about values in a readable form. These matchers include functions like `toEqual`, `toBe`, `toMatch`, and many others. Custom matchers can also be defined to extend the framework's capabilities.
  **Spies** are [Jasmine](../J/jasmine.md)'s way of creating test doubles, which can track calls to functions and their arguments, return values, and the value of `this`. They are useful for isolating code under test by replacing real functions with spy objects.
  For asynchronous operations, [Jasmine](../J/jasmine.md) offers the `done` callback to signal the framework that an asynchronous spec has completed. Alternatively, you can use the newer `async/await` syntax in combination with [Jasmine](../J/jasmine.md)'s `beforeAll`, `afterAll`, `beforeEach`, and `afterEach` functions to handle [setup](../S/setup.md) and teardown tasks.
  [Jasmine](../J/jasmine.md)'s flexibility allows it to be used with other libraries and frameworks, and it integrates well with various continuous integration tools. It is a popular choice for developers who need a robust, feature-rich testing solution for their JavaScript code.

#### Why is Jasmine considered important in e2e testing?

  [Jasmine](../J/jasmine.md) is considered important in **end-to-end (e2e) testing** because it provides a **behavior-driven development ([BDD](../B/bdd.md))** framework specifically tailored for testing JavaScript applications. Its significance lies in its ability to simulate user interactions with a web application, thus ensuring that the entire flow works as expected from the user's perspective.
  In e2e testing, [Jasmine](../J/jasmine.md) is often used in conjunction with tools like **Protractor**, which allow for testing of Angular applications, or with **[Selenium](../S/selenium.md) [WebDriver](../W/webdriver.md)** for non-Angular web applications. This combination enables testers to write clear and comprehensive [test suites](../T/test-suite.md) that cover user stories and [use cases](../U/use-case.md) in real browser environments.
  [Jasmine](../J/jasmine.md)'s syntax and structure make tests **readable and maintainable**, which is crucial for e2e [test suites](../T/test-suite.md) that can become complex. The framework's support for **asynchronous operations** is also vital for e2e testing, where waiting for page loads, AJAX calls, and UI updates is common.
  Moreover, [Jasmine](../J/jasmine.md)'s **spies** and **mocks** are essential for isolating tests from external dependencies, ensuring that e2e tests focus on the user experience rather than the underlying implementation. This isolation helps in identifying issues that could affect the end user, making [Jasmine](../J/jasmine.md) an integral part of the e2e testing process.
  By providing a robust set of features for simulating user interactions and verifying application behavior, [Jasmine](../J/jasmine.md) plays a key role in delivering high-quality, user-friendly software.

#### What are the key features of Jasmine?

  Key features of [Jasmine](../J/jasmine.md) include:

  - **Behavior-Driven Development ([BDD](../B/bdd.md)) syntax** : Encourages writing tests that are easy to read and understand.
  - **No external dependencies** : Works out of the box without the need for other libraries.
  - **Rich set of matchers** : Provides built-in matchers for common assertions, such as
    `toEqual`
    ,
    `toBe`
    ,
    `toMatch`
    , and more.

  - **Clean and straightforward syntax** : Offers a simple interface for describing tests, setting up conditions, and checking outcomes.
  - **Asynchronous support** : Handles async code with
    `done`
    callback or promises using
    `async`
    /
    `await`
    .

  - **Spies** : Built-in test doubles for tracking function calls, arguments, and return values.
  - **Clock control** : Jasmine's mock clock allows for testing time-dependent code.
  - **Automatic test discovery** : Automatically finds and runs tests defined in spec files.
  - **Flexible reporting** : Supports various reporters to display test results, which can be customized or extended.
  - **Extensibility** : Allows for custom matchers and reporters to be added to fit specific needs.
  - **Cross-platform** : Runs on any JavaScript-enabled platform.
  - **Integration friendly** : Can be used with other tools and frameworks like Karma, Protractor, and more.

  ```
  // Example of a simple Jasmine test
  describe('A suite', () => {
    it('contains a spec with an expectation', () => {
      expect(true).toBe(true);
    });
  });
  ```
  These features make [Jasmine](../J/jasmine.md) a powerful and versatile tool for writing and maintaining tests for JavaScript applications.

  - **Behavior-Driven Development ([BDD](../B/bdd.md)) syntax** : Encourages writing tests that are easy to read and understand.
  - **No external dependencies** : Works out of the box without the need for other libraries.
  - **Rich set of matchers** : Provides built-in matchers for common assertions, such as
    `toEqual`
    ,
    `toBe`
    ,
    `toMatch`
    , and more.

  - **Clean and straightforward syntax** : Offers a simple interface for describing tests, setting up conditions, and checking outcomes.
  - **Asynchronous support** : Handles async code with
    `done`
    callback or promises using
    `async`
    /
    `await`
    .

  - **Spies** : Built-in test doubles for tracking function calls, arguments, and return values.
  - **Clock control** : Jasmine's mock clock allows for testing time-dependent code.
  - **Automatic test discovery** : Automatically finds and runs tests defined in spec files.
  - **Flexible reporting** : Supports various reporters to display test results, which can be customized or extended.
  - **Extensibility** : Allows for custom matchers and reporters to be added to fit specific needs.
  - **Cross-platform** : Runs on any JavaScript-enabled platform.
  - **Integration friendly** : Can be used with other tools and frameworks like Karma, Protractor, and more.

#### How does Jasmine compare to other testing frameworks?

  [Jasmine](../J/jasmine.md) stands out for its **behavior-driven development ([BDD](../B/bdd.md))** style, but when compared to other testing frameworks, there are several distinctions to consider:

  - **Mocha**: Another popular JavaScript testing framework that is flexible and requires assertion libraries like Chai for assertions. Mocha is often paired with Chai and Sinon for spies, stubs, and mocks. [Jasmine](../J/jasmine.md), however, comes with these features out-of-the-box.
  - **[Jest](../J/jest.md)**: Developed by Facebook, [Jest](../J/jest.md) is often used for React applications. It's inspired by [Jasmine](../J/jasmine.md) but includes additional features like snapshot testing, built-in coverage reports, and a more powerful mocking library. [Jest](../J/jest.md) runs tests in parallel, which can lead to faster [test execution](../T/test-execution.md).
  - **QUnit**: A powerful framework for [unit testing](../U/unit-testing.md), QUnit is particularly well-suited for testing jQuery projects. It's more traditional in its approach compared to [Jasmine](../J/jasmine.md)'s [BDD](../B/bdd.md) style.
  - **Karma**: Not a testing framework itself, but rather a [test runner](../T/test-runner.md) that can work with [Jasmine](../J/jasmine.md), Mocha, or QUnit. Karma is often used for running tests on real browsers and devices.
  - **[Cypress](../C/cypress.md)**: An [end-to-end testing](../E/end-to-end-testing.md) tool that differs from [Jasmine](../J/jasmine.md) in that it runs in the browser, which can make it easier to test web applications in a real-world scenario. [Cypress](../C/cypress.md) also provides a rich interactive [test runner](../T/test-runner.md).
  - **Protractor**: An end-to-end test framework specifically for Angular applications. It uses [Jasmine](../J/jasmine.md) for its syntax but is now less favored since the Angular team recommends [Cypress](../C/cypress.md) or [Jest](../J/jest.md) for new projects.
  [Jasmine](../J/jasmine.md)'s simplicity and self-contained nature make it a good choice for developers who prefer an all-in-one solution without the need for additional libraries. However, for more complex needs or specific integrations, other frameworks might be more suitable.

  - **Mocha**: Another popular JavaScript testing framework that is flexible and requires assertion libraries like Chai for assertions. Mocha is often paired with Chai and Sinon for spies, stubs, and mocks. [Jasmine](../J/jasmine.md), however, comes with these features out-of-the-box.
  - **[Jest](../J/jest.md)**: Developed by Facebook, [Jest](../J/jest.md) is often used for React applications. It's inspired by [Jasmine](../J/jasmine.md) but includes additional features like snapshot testing, built-in coverage reports, and a more powerful mocking library. [Jest](../J/jest.md) runs tests in parallel, which can lead to faster [test execution](../T/test-execution.md).
  - **QUnit**: A powerful framework for [unit testing](../U/unit-testing.md), QUnit is particularly well-suited for testing jQuery projects. It's more traditional in its approach compared to [Jasmine](../J/jasmine.md)'s [BDD](../B/bdd.md) style.
  - **Karma**: Not a testing framework itself, but rather a [test runner](../T/test-runner.md) that can work with [Jasmine](../J/jasmine.md), Mocha, or QUnit. Karma is often used for running tests on real browsers and devices.
  - **[Cypress](../C/cypress.md)**: An [end-to-end testing](../E/end-to-end-testing.md) tool that differs from [Jasmine](../J/jasmine.md) in that it runs in the browser, which can make it easier to test web applications in a real-world scenario. [Cypress](../C/cypress.md) also provides a rich interactive [test runner](../T/test-runner.md).
  - **Protractor**: An end-to-end test framework specifically for Angular applications. It uses [Jasmine](../J/jasmine.md) for its syntax but is now less favored since the Angular team recommends [Cypress](../C/cypress.md) or [Jest](../J/jest.md) for new projects.

### Installation and Setup

#### How do you install Jasmine for JavaScript testing?

  To install [Jasmine](../J/jasmine.md) for JavaScript testing, you'll need [Node.js](../N/node-js.md) and npm (Node Package Manager) already installed as prerequisites. Follow these steps:

  1. Open your terminal or command prompt.
  2. Navigate to your project directory where you want to set up Jasmine.
  3. Run the following command to initialize a new npm package if you haven't already:

  ```
  npm init
  ```

  1. Follow the prompts to create a
    `package.json`
    file, or if you prefer to skip the prompts, use
    `npm init -y`
    for a default setup.

  2. Install Jasmine by running:

  ```
  npm install --save-dev jasmine
  ```
  This command installs [Jasmine](../J/jasmine.md) as a development dependency and adds it to your `package.json` file.

  1. Initialize Jasmine in your project, which creates a spec directory and configuration file (
    `jasmine.json`
    ) for your tests:

  ```
  npx jasmine init
  ```

  1. To run Jasmine tests, add a test script to your
    `package.json`
    file:

  ```
  "scripts": {
    "test": "jasmine"
  }
  ```

  1. Now, you can run your Jasmine tests using:

  ```
  npm test
  ```
  This [setup](../S/setup.md) allows you to write and run [Jasmine](../J/jasmine.md) tests for your JavaScript code. Remember to create your test files in the `spec` directory with a naming convention like `*.spec.js` to be recognized by [Jasmine](../J/jasmine.md).

  1. Open your terminal or command prompt.
  2. Navigate to your project directory where you want to set up Jasmine.
  3. Run the following command to initialize a new npm package if you haven't already:
  1. Follow the prompts to create a
    `package.json`
    file, or if you prefer to skip the prompts, use
    `npm init -y`
    for a default setup.

  2. Install Jasmine by running:
  1. Initialize Jasmine in your project, which creates a spec directory and configuration file (
    `jasmine.json`
    ) for your tests:

  1. To run Jasmine tests, add a test script to your
    `package.json`
    file:

  1. Now, you can run your Jasmine tests using:

#### What are the prerequisites for installing Jasmine?

  To install [Jasmine](../J/jasmine.md), ensure you have the following prerequisites:

  - **[Node.js](../N/node-js.md)**: [Jasmine](../J/jasmine.md) requires [Node.js](../N/node-js.md) to run. Make sure you have the latest stable version installed. You can download it from the official [Node.js website](https://nodejs.org/).
  - **npm (Node Package Manager)**: npm is included with [Node.js](../N/node-js.md) and is used to install [Jasmine](../J/jasmine.md). Verify its installation by running `npm -v` in your terminal.
  - **A JavaScript environment**: [Jasmine](../J/jasmine.md) can be used for both browser-based and [Node.js](../N/node-js.md) applications. Ensure you have a suitable environment set up for your project.
  - **A package.json file**: If you don't have one in your project, create it by running `npm init` in your project's root directory. This will manage the project's dependencies.
  Once these prerequisites are met, install [Jasmine](../J/jasmine.md) by running the following command in your terminal:

  ```
  npm install --save-dev jasmine
  ```
  This will install [Jasmine](../J/jasmine.md) as a development dependency in your project. After installation, initialize [Jasmine](../J/jasmine.md) by running:

  ```
  npx jasmine init
  ```
  This will set up the basic configuration and directory structure for your tests. You can now start writing your [Jasmine](../J/jasmine.md) tests.

  - **[Node.js](../N/node-js.md)**: [Jasmine](../J/jasmine.md) requires [Node.js](../N/node-js.md) to run. Make sure you have the latest stable version installed. You can download it from the official [Node.js website](https://nodejs.org/).
  - **npm (Node Package Manager)**: npm is included with [Node.js](../N/node-js.md) and is used to install [Jasmine](../J/jasmine.md). Verify its installation by running `npm -v` in your terminal.
  - **A JavaScript environment**: [Jasmine](../J/jasmine.md) can be used for both browser-based and [Node.js](../N/node-js.md) applications. Ensure you have a suitable environment set up for your project.
  - **A package.json file**: If you don't have one in your project, create it by running `npm init` in your project's root directory. This will manage the project's dependencies.

#### How do you set up a basic Jasmine test environment?

  To set up a basic [Jasmine](../J/jasmine.md) [test environment](../T/test-environment.md), follow these steps:

  1. **Install [Node.js](../N/node-js.md)** if it's not already installed. [Jasmine](../J/jasmine.md) requires [Node.js](../N/node-js.md) to run in a standalone environment.
  2. **Install [Jasmine](../J/jasmine.md) globally** using npm to make it available from anywhere in your system:

    ```
    npm install -g jasmine
    ```

  3. **Initialize [Jasmine](../J/jasmine.md)** in your project directory to create a `spec` directory and configuration file (`jasmine.json`):

    ```
    jasmine init
    ```

  4. **Create your first spec file** inside the `spec` directory. [Jasmine](../J/jasmine.md) spec files typically have a `.spec.js` suffix:

    ```
    touch spec/yourTest.spec.js
    ```

  5. **Write your tests** in the spec file using `describe` and `it` blocks. Since you're avoiding details on writing tests, we'll skip the content here.
  6. **Run your tests** by simply executing the `jasmine` command in your terminal:

    ```
    jasmine
    ```
  [Jasmine](../J/jasmine.md) will automatically find and execute all spec files matching the pattern defined in the `jasmine.json` configuration file.
  Remember to **manage your project dependencies** by creating a `package.json` file if you plan to use [Jasmine](../J/jasmine.md) with other libraries or integrate it into a larger project. You can do this by running `npm init` and then installing [Jasmine](../J/jasmine.md) as a development dependency with `npm install --save-dev jasmine`.
  For continuous integration or to integrate with build tools, you might need to set up additional configurations or scripts in your `package.json` to ensure [Jasmine](../J/jasmine.md) runs as part of your build process.

  1. **Install [Node.js](../N/node-js.md)** if it's not already installed. [Jasmine](../J/jasmine.md) requires [Node.js](../N/node-js.md) to run in a standalone environment.
  2. **Install [Jasmine](../J/jasmine.md) globally** using npm to make it available from anywhere in your system:

    ```
    npm install -g jasmine
    ```

  3. **Initialize [Jasmine](../J/jasmine.md)** in your project directory to create a `spec` directory and configuration file (`jasmine.json`):

    ```
    jasmine init
    ```

  4. **Create your first spec file** inside the `spec` directory. [Jasmine](../J/jasmine.md) spec files typically have a `.spec.js` suffix:

    ```
    touch spec/yourTest.spec.js
    ```

  5. **Write your tests** in the spec file using `describe` and `it` blocks. Since you're avoiding details on writing tests, we'll skip the content here.
  6. **Run your tests** by simply executing the `jasmine` command in your terminal:

    ```
    jasmine
    ```

### Test Writing

#### How do you write a basic test in Jasmine?

  To write a basic test in [Jasmine](../J/jasmine.md), you'll use the `describe` and `it` functions to define a [test suite](../T/test-suite.md) and a spec (test) respectively. Here's a step-by-step guide:

  1. **Define a [test suite](../T/test-suite.md)**
    using
    `describe`
    . The first argument is a string that describes the suite, and the second is a function that contains one or more specs.

  ```
  describe('My Test Suite', () => {
    // Specs go here
  });
  ```

  1. **Create a spec**
    within the suite using
    `it`
    . Like
    `describe`
    ,
    `it`
    takes a string describing the spec and a function that implements the test.

  ```
  it('does something expected', () => {
    // Test implementation goes here
  });
  ```

  1. **Assert expectations**
    within the spec using
    `expect`
    combined with a matcher function to make an assertion about a value.

  ```
  it('adds two numbers correctly', () => {
    let sum = 1 + 2;
    expect(sum).toEqual(3);
  });
  ```

  1. **Run your tests**
    using the Jasmine command-line tool or by including Jasmine in your HTML file and opening it in a browser.
  Remember to structure your tests to reflect the behavior of the code rather than its implementation details. This makes your tests more resilient to changes in the codebase. Also, keep your specs focused on a single behavior to make it easier to identify issues when a test fails.

  1. **Define a [test suite](../T/test-suite.md)**
    using
    `describe`
    . The first argument is a string that describes the suite, and the second is a function that contains one or more specs.

  1. **Create a spec**
    within the suite using
    `it`
    . Like
    `describe`
    ,
    `it`
    takes a string describing the spec and a function that implements the test.

  1. **Assert expectations**
    within the spec using
    `expect`
    combined with a matcher function to make an assertion about a value.

  1. **Run your tests**
    using the Jasmine command-line tool or by including Jasmine in your HTML file and opening it in a browser.

#### What is the structure of a Jasmine test?

  The structure of a [Jasmine](../J/jasmine.md) test is composed of **suites** and **specifications**. Suites are defined using the `describe` function, which takes a string and a function. The string is the title of the suite and the function is the block where you can define [setup](../S/setup.md), teardown, and specs.
  Specifications, or specs, are defined using the `it` function. Each spec represents a single test, with a string explaining what the test should do, and a function containing the test code.
  Within a spec, you use **matchers** to assert different things about your code. The `expect` function is used to make an assertion about a value, which is then tested against a matcher.
  Here's a basic structure:

  ```
  describe('My Test Suite', () => {
    beforeEach(() => {
      // Setup code before each spec
    });
    afterEach(() => {
      // Teardown code after each spec
    });
    it('does something expected', () => {
      expect(someValue).toBe(expectedValue);
    });
    // More specs (it blocks) can follow
  });
  ```
  **Nested suites** are possible by calling `describe` within another `describe`. This allows you to create sub-suites for more granular organization of specs.
  **Hooks** like `beforeEach`, `afterEach`, `beforeAll`, and `afterAll` are used to set up preconditions and clean up after your tests.
  The `it` block can also handle asynchronous code by taking a `done` callback or returning a promise.
  Remember to keep your specs **focused** and **independent** to ensure reliable and maintainable tests.

#### How do you use 'describe' and 'it' functions in Jasmine?

  In [Jasmine](../J/jasmine.md), the `describe` function is used to group related specs, commonly known as a "suite". It takes two parameters: a string and a function. The string is the title of the suite and the function is the block of code that implements the suite.

  ```
  describe('A suite', () => {
    // Specs go here
  });
  ```
  The `it` function is used to define a spec, which is a single [test case](../T/test-case.md). It also takes a string and a function. The string is the title of the spec and the function is the [test case](../T/test-case.md) itself.

  ```
  it('contains spec with an expectation', () => {
    expect(true).toBe(true);
  });
  ```
  **Usage**:

  - **Nesting** :
    `describe`
    blocks can be nested within each other to create sub-suites for more granular organization of specs.

  - **Scoping** : Variables declared in a
    `describe`
    are accessible to any
    `it`
    or
    `beforeEach`
    /
    `afterEach`
    within that suite.

  - **Execution** : When Jasmine runs, it executes
    `describe`
    blocks in the order they are defined and, within each suite,
    `it`
    blocks are run in the order they are defined.
  **Example**:

  ```
  describe('A suite of basic functions', () => {
    let num;
    beforeEach(() => {
      num = 5;
    });
    it('can add numbers', () => {
      num += 5;
      expect(num).toEqual(10);
    });
    it('can subtract numbers', () => {
      num -= 3;
      expect(num).toEqual(2);
    });
  });
  ```
  In this example, `beforeEach` runs before each `it`, setting the `num` variable to 5 before each spec. Each `it` contains an expectation, which is the actual test assertion.

  - **Nesting** :
    `describe`
    blocks can be nested within each other to create sub-suites for more granular organization of specs.

  - **Scoping** : Variables declared in a
    `describe`
    are accessible to any
    `it`
    or
    `beforeEach`
    /
    `afterEach`
    within that suite.

  - **Execution** : When Jasmine runs, it executes
    `describe`
    blocks in the order they are defined and, within each suite,
    `it`
    blocks are run in the order they are defined.

#### What are 'beforeEach' and 'afterEach' functions in Jasmine and how are they used?

  In [Jasmine](../J/jasmine.md), `beforeEach` and `afterEach` are functions that define code to run **before** and **after** each `it` block within a `describe` suite. These functions are used to set up preconditions and clean up after tests to ensure a consistent testing environment.
  **`beforeEach`** is typically used for setting up the state before each test runs. This might involve initializing variables, creating test fixtures, or resetting the environment to a known state.

  ```
  beforeEach(() => {
    // Code to set up the state before each test
  });
  ```
  **`afterEach`** is used for teardown logic that needs to run after each test completes. This can include releasing resources, cleaning up mock states, or resetting modifications made during the test.

  ```
  afterEach(() => {
    // Code to clean up after each test
  });
  ```
  These functions help to reduce code duplication and promote separation of concerns by encapsulating [setup](../S/setup.md) and teardown logic away from the actual test assertions. They contribute to more maintainable and readable [test suites](../T/test-suite.md) by ensuring each test runs in isolation without unintended side effects from previous tests.

### Assertions and Matchers

#### What are Jasmine matchers and how are they used?

  [Jasmine](../J/jasmine.md) matchers are functions that implement boolean comparison between the actual value and the expected value. They are used to write assertions in tests, allowing you to check if certain conditions are met. Matchers are invoked using the `expect` function, which takes the actual value as an argument, followed by a matcher function that specifies the expected outcome.
  Here's an example of using a matcher:

  ```
  expect(someValue).toBe(42);
  ```
  In this case, `toBe` is the matcher that checks if `someValue` is strictly equal to `42`.
  Common matchers include:

  - `toBe` : Strict equality (===) comparison.
  - `toEqual` : Deep equality comparison, useful for objects or arrays.
  - `toMatch` : String matching against a regular expression.
  - `toBeDefined` : Checks that a variable is not
    `undefined`
    .

  - `toBeNull` : Checks that a variable is
    `null`
    .

  - `toBeTruthy` : Checks that a variable is truthy.
  - `toBeFalsy` : Checks that a variable is falsy.
  - `toContain` : Checks if an array or string contains a specific item or substring.
  - `toBeGreaterThan`
    ,
    `toBeLessThan` : Numerical comparisons.

  - `toThrow` : Checks if a function throws an error.
  Custom matchers can also be created to encapsulate repetitive or complex logic. They are added to [Jasmine](../J/jasmine.md) by extending the `jasmine.addMatchers` method with a matcher object that defines a `compare` function.
  Matchers are essential for expressing the intent of the test clearly and concisely, making tests easier to read and maintain. They are a core part of the [Jasmine](../J/jasmine.md) framework, providing a rich language for specifying various conditions and expectations in your [test cases](../T/test-case.md).

  - `toBe` : Strict equality (===) comparison.
  - `toEqual` : Deep equality comparison, useful for objects or arrays.
  - `toMatch` : String matching against a regular expression.
  - `toBeDefined` : Checks that a variable is not
    `undefined`
    .

  - `toBeNull` : Checks that a variable is
    `null`
    .

  - `toBeTruthy` : Checks that a variable is truthy.
  - `toBeFalsy` : Checks that a variable is falsy.
  - `toContain` : Checks if an array or string contains a specific item or substring.
  - `toBeGreaterThan`
    ,
    `toBeLessThan` : Numerical comparisons.

  - `toThrow` : Checks if a function throws an error.

#### How do you create custom matchers in Jasmine?

  Creating custom matchers in [Jasmine](../J/jasmine.md) allows you to express expectations in a more domain-specific way, enhancing the readability and [maintainability](../M/maintainability.md) of your tests. Here's how to define a custom matcher in [Jasmine](../J/jasmine.md):

  1. Use
    `jasmine.addMatchers`
    to add a new matcher.

  2. Inside
    `jasmine.addMatchers`
    , define an object where the keys are the names of your custom matchers.

  3. Each matcher is a factory function that returns an object with a
    `compare`
    function.

  4. The
    `compare`
    function should return an object with a
    `pass`
    property, which is a boolean indicating if the expectation is met, and an optional
    `message`
    property for custom failure messages.
  Here's an example of a custom matcher that checks if a number is even:

  ```
  beforeEach(function() {
    jasmine.addMatchers({
      toBeEven: function() {
        return {
          compare: function(actual) {
            const result = {};
            result.pass = actual % 2 === 0;
            if (result.pass) {
              result.message = `Expected ${actual} not to be even`;
            } else {
              result.message = `Expected ${actual} to be even`;
            }
            return result;
          }
        };
      }
    });
  });
  ```
  To use this matcher in a test:

  ```
  it('is an even number', function() {
    expect(4).toBeEven();
  });
  ```
  Custom matchers can be reused across different specs by including them in a `beforeEach` at the top level of your [test suite](../T/test-suite.md) or in a separate file that is included in your test [setup](../S/setup.md).

  1. Use
    `jasmine.addMatchers`
    to add a new matcher.

  2. Inside
    `jasmine.addMatchers`
    , define an object where the keys are the names of your custom matchers.

  3. Each matcher is a factory function that returns an object with a
    `compare`
    function.

  4. The
    `compare`
    function should return an object with a
    `pass`
    property, which is a boolean indicating if the expectation is met, and an optional
    `message`
    property for custom failure messages.

#### What are the different types of assertions in Jasmine?

  In [Jasmine](../J/jasmine.md), assertions are made using **matchers**. A matcher in [Jasmine](../J/jasmine.md) is responsible for checking if a certain condition is true. The different types of assertions, or matchers, provided by [Jasmine](../J/jasmine.md) include:

  - `toBe` : Checks if the actual value is the same as the expected value (===).
  - `toEqual` : Checks for equality of the actual and the expected values, including for objects and arrays.
  - `toMatch` : Checks if a value matches a specified regular expression.
  - `toBeDefined` : Asserts that a variable is not
    `undefined`
    .

  - `toBeUndefined` : Asserts that a variable is
    `undefined`
    .

  - `toBeNull` : Checks if the actual value is
    `null`
    .

  - `toBeTruthy` : Asserts that the actual value is truthy.
  - `toBeFalsy` : Asserts that the actual value is falsy.
  - `toContain` : Checks if an array or string contains a specific item or substring.
  - `toBeLessThan` : Asserts that a value is less than another.
  - `toBeGreaterThan` : Asserts that a value is greater than another.
  - `toBeCloseTo` : Checks if a number is close to another number, within a specified precision.
  - `toThrow` : Asserts that a function throws an exception.
  - `toThrowError` : Checks if a function throws a specific type of exception.
  Here is an example of using some matchers in a [Jasmine](../J/jasmine.md) test:

  ```
  describe("Different types of matchers in Jasmine", () => {
    it("demonstrates the use of various Jasmine matchers", () => {
      expect(true).toBeTruthy();
      expect(null).toBeNull();
      expect(123).toBeGreaterThan(100);
      expect("Hello World").toContain("World");
      expect(() => { throw new Error("Error thrown"); }).toThrow();
    });
  });
  ```
  These matchers are used within an `expect` function and are chained with the actual value that is being tested. Matchers are crucial for validating the behavior of the code under test.

  - `toBe` : Checks if the actual value is the same as the expected value (===).
  - `toEqual` : Checks for equality of the actual and the expected values, including for objects and arrays.
  - `toMatch` : Checks if a value matches a specified regular expression.
  - `toBeDefined` : Asserts that a variable is not
    `undefined`
    .

  - `toBeUndefined` : Asserts that a variable is
    `undefined`
    .

  - `toBeNull` : Checks if the actual value is
    `null`
    .

  - `toBeTruthy` : Asserts that the actual value is truthy.
  - `toBeFalsy` : Asserts that the actual value is falsy.
  - `toContain` : Checks if an array or string contains a specific item or substring.
  - `toBeLessThan` : Asserts that a value is less than another.
  - `toBeGreaterThan` : Asserts that a value is greater than another.
  - `toBeCloseTo` : Checks if a number is close to another number, within a specified precision.
  - `toThrow` : Asserts that a function throws an exception.
  - `toThrowError` : Checks if a function throws a specific type of exception.

### Spies and Mocking

#### What are Jasmine spies and how are they used?

  [Jasmine](../J/jasmine.md) spies are functions that record how they are called, allowing you to verify that interactions with them occur as expected. They can be used to track whether a function was called, how many times it was called, with what arguments, and what it returned. Spies can also be used to stub any function and simulate its behavior.
  To create a spy, you use the `spyOn` function, passing the object and the name of the function you want to spy on:

  ```
  spyOn(someObject, 'someFunction');
  ```
  If you need to create a spy without an existing function, you can use `jasmine.createSpy` or `jasmine.createSpyObj` for multiple functions:

  ```
  let mySpy = jasmine.createSpy('mySpy');
  let mySpies = jasmine.createSpyObj('mySpies', ['firstFunction', 'secondFunction']);
  ```
  Spies are particularly useful when you want to isolate the unit of work by replacing dependent functions with spies that can be controlled and inspected. They are also handy when you want to prevent the actual implementation of a function from being executed during a test, especially if it's expensive, slow, or has side effects.
  You can set up a spy to return a specific value using `.and.returnValue`:

  ```
  mySpy.and.returnValue(someValue);
  ```
  Or to call a fake function:

  ```
  mySpy.and.callFake(() => {
    // Fake implementation
  });
  ```
  After the test, you can check if the spy was called correctly:

  ```
  expect(mySpy).toHaveBeenCalled();
  expect(mySpy).toHaveBeenCalledWith(expectedArgs);
  ```
  Spies are essential for maintaining **test isolation** and ensuring that your tests are not affected by external code or side effects.

#### How do you create a mock in Jasmine?

  Creating a mock in [Jasmine](../J/jasmine.md) involves using **spies** to track and control the behavior of functions, methods, or objects. Here's a step-by-step guide:

  1. **Create a spy**
    for the function you want to mock using
    `spyOn`
    . This replaces the function with a spy that can track calls, arguments, and set return values.

  ```
  spyOn(obj, 'methodName');
  ```

  1. **Configure the spy's behavior**
    using chaining functions like
    `.and.returnValue()`
    ,
    `.and.callFake()`
    , or
    `.and.throwError()`
    to control what happens when the method is called.

  ```
  // Return a specific value
  spyOn(obj, 'methodName').and.returnValue('mocked value');
  // Provide a fake implementation
  spyOn(obj, 'methodName').and.callFake(() => 'fake implementation');
  // Throw an error
  spyOn(obj, 'methodName').and.throwError('error message');
  ```

  1. **Create a [Jasmine](../J/jasmine.md) spy object**
    to mock an entire object with multiple methods using
    `jasmine.createSpyObj`
    . This is useful when you need to mock an object with several methods.

  ```
  let mockObject = jasmine.createSpyObj('mockObject', ['method1', 'method2']);
  ```

  1. **Set up return values or implementations**
    for the spy object's methods if needed.

  ```
  mockObject.method1.and.returnValue('value1');
  mockObject.method2.and.callFake(() => 'value2');
  ```

  1. **Integrate the mock**
    into your test, replacing the real implementation with the mock.
  Remember, mocks created with spies in [Jasmine](../J/jasmine.md) are temporary and will be removed after each test, ensuring test isolation. Use `beforeEach` to set up mocks for each test if needed.

  1. **Create a spy**
    for the function you want to mock using
    `spyOn`
    . This replaces the function with a spy that can track calls, arguments, and set return values.

  1. **Configure the spy's behavior**
    using chaining functions like
    `.and.returnValue()`
    ,
    `.and.callFake()`
    , or
    `.and.throwError()`
    to control what happens when the method is called.

  1. **Create a [Jasmine](../J/jasmine.md) spy object**
    to mock an entire object with multiple methods using
    `jasmine.createSpyObj`
    . This is useful when you need to mock an object with several methods.

  1. **Set up return values or implementations**
    for the spy object's methods if needed.

  1. **Integrate the mock**
    into your test, replacing the real implementation with the mock.

#### What is the difference between a spy and a mock in Jasmine?

  In [Jasmine](../J/jasmine.md), **spies** and **mocks** serve different purposes for testing.
  A **spy** is a function that records information about its calls, such as how many times it was called, with what arguments, and what values were returned. Spies can also fake return values or errors, allowing you to simulate behavior without executing the actual code. They are primarily used to gather information about function calls to verify that the functions are being used correctly.

  ```
  spyOn(someObject, 'someMethod');
  ```
  A **mock**, on the other hand, is an object that mimics the structure and behavior of a real object, with pre-programmed behavior and expectations. In [Jasmine](../J/jasmine.md), mocks are often created using spies in combination with other techniques to simulate complex behavior. Mocks are useful when you need to test interactions with an object that would be difficult or impractical to include in your tests, such as an [API](../A/api.md) or a [database](../D/database.md).

  ```
  const mock = jasmine.createSpyObj('mock', ['method1', 'method2']);
  mock.method1.and.returnValue('some value');
  ```
  In summary, use a **spy** when you want to observe an existing function, and use a **mock** when you need to create a stand-in for an entire object with multiple methods or properties. Both are essential tools in a [test automation](../T/test-automation.md) engineer's toolkit for isolating units of code and verifying interactions between different parts of a system.

### Advanced Concepts

#### How do you handle asynchronous testing in Jasmine?

  Handling asynchronous testing in [Jasmine](../J/jasmine.md) involves using the `done` callback, `async`/`await` syntax, or the `done.fail` function for error handling.
  **Using the `done` callback:**
  [Jasmine](../J/jasmine.md) provides a `done` function that you can call to signal that an asynchronous test or [setup](../S/setup.md)/teardown method is complete. Pass `done` as an argument to the `it`, `beforeEach`, or `afterEach` function, and call it when the asynchronous operation finishes.

  ```
  it('should handle async operation', (done) => {
    setTimeout(() => {
      expect(true).toBe(true);
      done();
    }, 1000);
  });
  ```
  **Using `async`/`await`:**
  With the support for modern JavaScript, you can use `async`/`await` for a cleaner syntax. Mark the test function as `async`, and `await` the asynchronous calls within it.

  ```
  it('should handle async operation with async/await', async () => {
    const result = await someAsyncFunction();
    expect(result).toBe(expectedValue);
  });
  ```
  **Error handling with `done.fail`:**
  If an error occurs during an asynchronous operation, you can use `done.fail` to pass the error to [Jasmine](../J/jasmine.md), which will then fail the test with the provided error message.

  ```
  it('should handle async errors', (done) => {
    setTimeout(() => {
      try {
        expect(true).toBe(false);
        done();
      } catch (error) {
        done.fail(error);
      }
    }, 1000);
  });
  ```
  Remember to handle timeouts and ensure that `done` is called appropriately to avoid [false positives](../F/false-positive.md) where tests pass because `done` was never invoked.

#### How do you use Jasmine with other libraries or frameworks like Angular or React?

  Integrating [Jasmine](../J/jasmine.md) with frameworks like **Angular** or **React** involves setting up a [test environment](../T/test-environment.md) that allows [Jasmine](../J/jasmine.md) to interact with the components or services of these frameworks.
  For **Angular**, you can use **Angular CLI** to generate a project with a testing [setup](../S/setup.md) that includes [Jasmine](../J/jasmine.md) and **Karma**. Angular's testing utilities provide ways to test components and services in isolation. Here's a basic example of how you might test a component:

  ```
  import { TestBed, async } from '@angular/core/testing';
  import { AppComponent } from './app.component';
  describe('AppComponent', () => {
    beforeEach(async(() => {
      TestBed.configureTestingModule({
        declarations: [
          AppComponent
        ],
      }).compileComponents();
    }));
    it('should create the app', () => {
      const fixture = TestBed.createComponent(AppComponent);
      const app = fixture.debugElement.componentInstance;
      expect(app).toBeTruthy();
    });
  });
  ```
  For **React**, you'll typically use **Enzyme** or **React Testing Library** alongside [Jasmine](../J/jasmine.md) to render components and handle their interaction with the DOM. You can set up [Jasmine](../J/jasmine.md) with React by configuring your [test runner](../T/test-runner.md) (like Karma) to work with React's JSX syntax. Here's a simple React component test using [Jasmine](../J/jasmine.md) and Enzyme:

  ```
  import React from 'react';
  import { shallow } from 'enzyme';
  import MyComponent from './MyComponent';
  describe('<MyComponent />', () => {
    it('renders three <MyComponent /> components', () => {
      const wrapper = shallow(<MyComponent />);
      expect(wrapper.find('.my-component').length).toBe(3);
    });
  });
  ```
  In both cases, you'll need to configure your [test runner](../T/test-runner.md) to work with the specific build tools and transpilers (like **Webpack** and **Babel**) that are part of your project's stack. This ensures that your tests can understand the module syntax and JSX (for React) used in your application code.

#### What are some best practices for writing tests in Jasmine?

  Best practices for writing tests in [Jasmine](../J/jasmine.md) include:

  - **Keep tests isolated**: Ensure each test can run independently without relying on the state from another test. Use `beforeEach` and `afterEach` to set up and tear down [test environments](../T/test-environment.md).
  - **Write descriptive [test cases](../T/test-case.md)**: Use clear, descriptive names for `describe` and `it` blocks to convey the intent of the [test suite](../T/test-suite.md) and individual tests.
  - **DRY (Don't Repeat Yourself)**: Factor out common [setup](../S/setup.md) and teardown steps into `beforeEach` and `afterEach` blocks. Use helper functions for repetitive tasks.
  - **Test one aspect per spec**: Each `it` block should focus on a single behavior or aspect of the code under test.
  - **Use Behavior-Driven Development ([BDD](../B/bdd.md)) language**: Write tests that describe the behavior of the feature rather than the implementation details.
  - **Assert with clear expectations**: Use [Jasmine](../J/jasmine.md) matchers to write assertions that are easy to read and understand. Custom matchers can be created for domain-specific assertions.
  - **Handle asynchronous code properly**: Use [Jasmine](../J/jasmine.md)'s `done` callback or return a promise to ensure that asynchronous operations complete before evaluating expectations.
  - **Avoid testing implementation details**: Focus on the public [API](../A/api.md) and expected outcomes rather than the internal workings of a function or component.
  - **Keep tests fast**: Slow tests can hinder the development process. Optimize tests to run quickly and avoid unnecessary complexity.
  - **Structure tests logically**: Group related tests using nested `describe` blocks to create a readable and maintainable test hierarchy.
  - **Regularly refactor tests**: As the codebase evolves, revisit and refactor tests to ensure they remain effective and do not become flaky or irrelevant.

  ```
  describe('MyComponent', () => {
    let component;
    beforeEach(() => {
      component = new MyComponent();
    });
    it('should initialize with default values', () => {
      expect(component.someValue).toBe('default');
    });
    // More tests...
  });
  ```

  - **Keep tests isolated**: Ensure each test can run independently without relying on the state from another test. Use `beforeEach` and `afterEach` to set up and tear down [test environments](../T/test-environment.md).
  - **Write descriptive [test cases](../T/test-case.md)**: Use clear, descriptive names for `describe` and `it` blocks to convey the intent of the [test suite](../T/test-suite.md) and individual tests.
  - **DRY (Don't Repeat Yourself)**: Factor out common [setup](../S/setup.md) and teardown steps into `beforeEach` and `afterEach` blocks. Use helper functions for repetitive tasks.
  - **Test one aspect per spec**: Each `it` block should focus on a single behavior or aspect of the code under test.
  - **Use Behavior-Driven Development ([BDD](../B/bdd.md)) language**: Write tests that describe the behavior of the feature rather than the implementation details.
  - **Assert with clear expectations**: Use [Jasmine](../J/jasmine.md) matchers to write assertions that are easy to read and understand. Custom matchers can be created for domain-specific assertions.
  - **Handle asynchronous code properly**: Use [Jasmine](../J/jasmine.md)'s `done` callback or return a promise to ensure that asynchronous operations complete before evaluating expectations.
  - **Avoid testing implementation details**: Focus on the public [API](../A/api.md) and expected outcomes rather than the internal workings of a function or component.
  - **Keep tests fast**: Slow tests can hinder the development process. Optimize tests to run quickly and avoid unnecessary complexity.
  - **Structure tests logically**: Group related tests using nested `describe` blocks to create a readable and maintainable test hierarchy.
  - **Regularly refactor tests**: As the codebase evolves, revisit and refactor tests to ensure they remain effective and do not become flaky or irrelevant.
