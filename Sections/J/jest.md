# Jest


<!-- TOC START -->
- [Related Terms:](#related-terms)
  - [See also:](#see-also)
- [Questions about Jest ?](#questions-about-jest)
  - [Basics and Importance](#basics-and-importance)
    - [What is Jest and what is it used for?](#what-is-jest-and-what-is-it-used-for)
    - [Why is Jest popular for testing JavaScript code?](#why-is-jest-popular-for-testing-javascript-code)
    - [How does Jest compare to other testing frameworks?](#how-does-jest-compare-to-other-testing-frameworks)
    - [What are the key features of Jest?](#what-are-the-key-features-of-jest)
    - [Why is Jest considered a 'zero-configuration' testing platform?](#why-is-jest-considered-a-zero-configuration-testing-platform)
  - [Installation and Setup](#installation-and-setup)
    - [How do you install Jest?](#how-do-you-install-jest)
    - [What are the prerequisites for using Jest?](#what-are-the-prerequisites-for-using-jest)
    - [How do you set up a basic Jest testing environment?](#how-do-you-set-up-a-basic-jest-testing-environment)
    - [How do you configure Jest for a project?](#how-do-you-configure-jest-for-a-project)
  - [Writing and Running Tests](#writing-and-running-tests)
    - [How do you write a basic test in Jest?](#how-do-you-write-a-basic-test-in-jest)
    - [What is the structure of a Jest test?](#what-is-the-structure-of-a-jest-test)
    - [How do you run tests in Jest?](#how-do-you-run-tests-in-jest)
    - [What are some common assertions in Jest?](#what-are-some-common-assertions-in-jest)
    - [How do you group tests in Jest?](#how-do-you-group-tests-in-jest)
  - [Advanced Concepts](#advanced-concepts)
    - [What is mocking in Jest and how is it used?](#what-is-mocking-in-jest-and-how-is-it-used)
    - [How does Jest handle asynchronous testing?](#how-does-jest-handle-asynchronous-testing)
    - [How can you use Jest for snapshot testing?](#how-can-you-use-jest-for-snapshot-testing)
    - [What is the role of 'describe' function in Jest?](#what-is-the-role-of-describe-function-in-jest)
    - [How can you use 'beforeEach' and 'afterEach' in Jest?](#how-can-you-use-beforeeach-and-aftereach-in-jest)
<!-- TOC END -->

Jest

is a JavaScript

unit testing

framework by Meta. It's primarily used for writing unit tests to assess individual code segments.

## Related Terms:

- [Testing framework](../T/testing-framework.md)
- [Jasmine](../J/jasmine.md)
- [Chai.js](../C/chaijs.md)

### See also:

- [Wikipedia](https://jestjs.io/)

## Questions about Jest ?

### Basics and Importance

#### What is Jest and what is it used for?

  [Jest](../J/jest.md) is a **JavaScript testing framework** designed to ensure correctness of any JavaScript codebase. It allows developers to write tests with an [API](../A/api.md) that encourages good testing practices and is commonly used for both front-end and back-end JavaScript applications.
  With [Jest](../J/jest.md), you can perform **unit tests** to validate individual functions or modules, **integration tests** to ensure different parts of the application work together as expected, and **end-to-end tests** for testing the flow of an application.
  [Jest](../J/jest.md) integrates well with projects using **Babel**, **TypeScript**, **[Node.js](../N/node-js.md)**, **React**, **Angular**, and **Vue**, making it a versatile choice for a wide range of JavaScript projects. It also supports **test parallelization**, where tests are run simultaneously in separate processes to maximize performance and speed.
  To integrate [Jest](../J/jest.md) into a project, you typically install it via npm or yarn, and then create a configuration file if needed, although many projects can use [Jest](../J/jest.md) with little to no configuration due to its convention over configuration design.
  Here's a basic example of how a [Jest](../J/jest.md) test looks:

  ```
  test('adds 1 + 2 to equal 3', () => {
    expect(1 + 2).toBe(3);
  });
  ```
  [Jest](../J/jest.md)'s assertion library provides a range of matchers that let you validate different things, from simple equality checks to more complex conditions. Its **interactive watch mode** allows you to automatically re-run tests related to changed files, and its **built-in coverage reports** help you understand which parts of your codebase may not be covered by tests.

#### Why is Jest popular for testing JavaScript code?

  [Jest](../J/jest.md) is popular for testing JavaScript code due to its **simplicity** and **ease of use**. It integrates well with projects using **React**, **Angular**, **Vue**, and **[Node.js](../N/node-js.md)**, making it a versatile choice for a wide range of JavaScript applications. Its **watch mode** automatically runs tests related to changed files, enhancing developer productivity.
  Developers appreciate [Jest](../J/jest.md)'s **integrated coverage reports**, which are generated without additional [setup](../S/setup.md), providing immediate insight into [test coverage](../T/test-coverage.md). The framework's **powerful mocking library** simplifies the testing of code with complex dependencies.
  [Jest](../J/jest.md)'s **parallel [test execution](../T/test-execution.md)** optimizes performance by running tests concurrently, reducing the time required to run extensive [test suites](../T/test-suite.md). Its **consistent environment** across test runs, thanks to a custom resolver and the use of JSDom for DOM [API](../A/api.md) emulation, ensures test reliability.
  The community around [Jest](../J/jest.md) is active, contributing to a rich ecosystem of **plugins** and **extensions** that enhance its functionality. Regular updates and improvements by the maintainers keep [Jest](../J/jest.md) at the forefront of testing technologies.

  ```
  test('adds 1 + 2 to equal 3', () => {
    expect(sum(1, 2)).toBe(3);
  });
  ```
  The above example demonstrates [Jest](../J/jest.md)'s straightforward syntax, making tests readable and maintainable. [Jest](../J/jest.md)'s popularity is a testament to its ability to balance **flexibility**, **features**, and **developer experience**, making it a go-to choice for JavaScript testing.

#### How does Jest compare to other testing frameworks?

  [Jest](../J/jest.md) stands out for its **simplicity** and **integrated features** when compared to other testing frameworks like Mocha, [Jasmine](../J/jasmine.md), or AVA. Unlike Mocha, which requires additional plugins for functionalities like mocking, coverage, and snapshot testing, [Jest](../J/jest.md) comes with these features out-of-the-box. This reduces the need for configuring multiple libraries, making [Jest](../J/jest.md) a more **streamlined choice**.
  [Jest](../J/jest.md) runs tests in parallel, which can lead to **faster execution times** compared to some other frameworks. Its **watch mode** is also highly optimized for developer experience, allowing for tests related to changed files to be run automatically.
  In contrast to [Jasmine](../J/jasmine.md), which has a similar syntax, [Jest](../J/jest.md) provides a more **modern and powerful mocking library**. This makes it easier to test JavaScript applications, especially those built with React, where [Jest](../J/jest.md) is often the recommended choice due to its **native support for React testing utilities**.
  While AVA emphasizes **concurrency** in test runs, [Jest](../J/jest.md) balances parallel [test execution](../T/test-execution.md) with a **shared context** that can be beneficial for certain types of [test suites](../T/test-suite.md). Additionally, [Jest](../J/jest.md)'s **snapshot testing** capability is more advanced than similar features in other frameworks, offering a straightforward way to test the output of components.
  For **asynchronous testing**, [Jest](../J/jest.md) supports async/await, promises, and callbacks, similar to other frameworks, but with a more **unified syntax** and better error handling.
  Overall, [Jest](../J/jest.md) is often preferred for its **developer-friendly approach**, comprehensive documentation, and **tight integration** with the JavaScript ecosystem, particularly in projects created with `create-react-app` or using Babel and TypeScript.

#### What are the key features of Jest?

  Key features of [Jest](../J/jest.md) include:

  - **Snapshot Testing**: [Jest](../J/jest.md) can capture "snapshots" of React trees or other serializable values to simplify [UI testing](../U/ui-testing.md) and ensure the UI does not change unexpectedly.
  - **Interactive Watch Mode**: [Jest](../J/jest.md) can run in a watch mode that automatically reruns tests when it detects changes in the codebase, enhancing developer productivity.
  - **Built-in Coverage Reports**: [Jest](../J/jest.md) includes an integrated [code coverage](../C/code-coverage.md) reporter that can be activated with a simple command line flag (`--coverage`).
  - **Isolated and Parallel [Test Execution](../T/test-execution.md)**: Tests are run in parallel in separate processes to maximize performance and ensure tests do not affect each other.
  - **Global [Setup](../S/setup.md)/Teardown**: [Jest](../J/jest.md) provides hooks for setting up and tearing down the environment before and after all tests have run.
  - **Manual Mocks**: Developers can create manual mocks to stub out functionality with mock implementations.
  - **Timer Mocks**: [Jest](../J/jest.md) can mock timers in your tests, allowing you to control the passage of time.
  - **Custom Matchers**: Extend [Jest](../J/jest.md)'s matcher library with custom matchers for more descriptive test statements.
  - **Seamless TypeScript Integration**: [Jest](../J/jest.md) supports TypeScript, allowing for type-safe testing without additional configuration.
  - **Rich Assertion Library**: [Jest](../J/jest.md) comes with a vast array of matchers that enable a variety of assertions for different [use cases](../U/use-case.md).
  - **Extensibility**: [Jest](../J/jest.md) can be extended with custom reporters, custom matchers, and custom [test runners](../T/test-runner.md) to fit the needs of any project.
  - **Easy Mocking of ES Modules**: [Jest](../J/jest.md) allows for easy mocking of ES6 modules, which can be particularly useful when dealing with external dependencies.
  - **Snapshot Testing**: [Jest](../J/jest.md) can capture "snapshots" of React trees or other serializable values to simplify [UI testing](../U/ui-testing.md) and ensure the UI does not change unexpectedly.
  - **Interactive Watch Mode**: [Jest](../J/jest.md) can run in a watch mode that automatically reruns tests when it detects changes in the codebase, enhancing developer productivity.
  - **Built-in Coverage Reports**: [Jest](../J/jest.md) includes an integrated [code coverage](../C/code-coverage.md) reporter that can be activated with a simple command line flag (`--coverage`).
  - **Isolated and Parallel [Test Execution](../T/test-execution.md)**: Tests are run in parallel in separate processes to maximize performance and ensure tests do not affect each other.
  - **Global [Setup](../S/setup.md)/Teardown**: [Jest](../J/jest.md) provides hooks for setting up and tearing down the environment before and after all tests have run.
  - **Manual Mocks**: Developers can create manual mocks to stub out functionality with mock implementations.
  - **Timer Mocks**: [Jest](../J/jest.md) can mock timers in your tests, allowing you to control the passage of time.
  - **Custom Matchers**: Extend [Jest](../J/jest.md)'s matcher library with custom matchers for more descriptive test statements.
  - **Seamless TypeScript Integration**: [Jest](../J/jest.md) supports TypeScript, allowing for type-safe testing without additional configuration.
  - **Rich Assertion Library**: [Jest](../J/jest.md) comes with a vast array of matchers that enable a variety of assertions for different [use cases](../U/use-case.md).
  - **Extensibility**: [Jest](../J/jest.md) can be extended with custom reporters, custom matchers, and custom [test runners](../T/test-runner.md) to fit the needs of any project.
  - **Easy Mocking of ES Modules**: [Jest](../J/jest.md) allows for easy mocking of ES6 modules, which can be particularly useful when dealing with external dependencies.

#### Why is Jest considered a 'zero-configuration' testing platform?

  [Jest](../J/jest.md) is considered a **zero-configuration** testing platform because it aims to work out of the box, with minimal [setup](../S/setup.md) required. Upon installation, [Jest](../J/jest.md) provides sensible defaults for most projects, allowing developers to start writing and running tests immediately.
  The framework is designed with conventions that enable it to automatically find and execute tests. By default, [Jest](../J/jest.md) looks for test files with any of the following popular naming conventions:

  - Files with
    `.js`
    suffix in
    `__tests__`
    folders.

  - Files with
    `.test.js`
    suffix.

  - Files with
    `.spec.js`
    suffix.
  [Jest](../J/jest.md) also comes with a built-in assertion library and [test runner](../T/test-runner.md), which means there's no need to install or configure additional modules to start testing. It handles the transformation of modern JavaScript features through **Babel** integration, and it can mock dependencies and timers out of the box.
  For many applications, the default configuration is sufficient to begin testing. However, if customization is needed, [Jest](../J/jest.md) provides an easy-to-use configuration file (`jest.config.js`) where developers can override defaults and tailor the testing environment to their specific needs.
  Here's an example of how simple it is to start with [Jest](../J/jest.md):

  ```
  npm install --save-dev jest
  ```
  Then, in a `sum.test.js` file:

  ```
  const sum = require('./sum');
  test('adds 1 + 2 to equal 3', () => {
    expect(sum(1, 2)).toBe(3);
  });
  ```
  Run the tests with:

  ```
  npx jest
  ```
  This ease of [setup](../S/setup.md) and sensible defaults are what make [Jest](../J/jest.md) a **zero-configuration** testing platform for many developers.

  - Files with
    `.js`
    suffix in
    `__tests__`
    folders.

  - Files with
    `.test.js`
    suffix.

  - Files with
    `.spec.js`
    suffix.

### Installation and Setup

#### How do you install Jest?

  To install [Jest](../J/jest.md), you need to have **[Node.js](../N/node-js.md)** and **npm** (Node Package Manager) installed on your system. If you're using **yarn**, you can use that as well. Here's how you can install [Jest](../J/jest.md):
  For npm users:

  ```
  npm install --save-dev jest
  ```
  For yarn users:

  ```
  yarn add --dev jest
  ```
  This command will add [Jest](../J/jest.md) as a development dependency in your project's `package.json` file. After installation, you can add a script to your `package.json` to easily run [Jest](../J/jest.md):

  ```
  "scripts": {
    "test": "jest"
  }
  ```
  Now, you can run your tests using the following command:
  For npm users:

  ```
  npm test
  ```
  For yarn users:

  ```
  yarn test
  ```
  Ensure that your test files are named using the `.test.js` or `.spec.js` suffix, or are placed in a `__tests__` folder, so [Jest](../J/jest.md) can automatically find and execute them.
  If you're using **TypeScript**, you'll also need to install `ts-jest` and `@types/jest` to handle TypeScript compilation and type definitions:

  ```
  npm install --save-dev ts-jest @types/jest
  ```
  Or with yarn:

  ```
  yarn add --dev ts-jest @types/jest
  ```
  You'll then need to configure [Jest](../J/jest.md) to use `ts-jest` by adding the following to your [Jest](../J/jest.md) configuration:

  ```
  "jest": {
    "preset": "ts-jest",
    "testMatch": ["**/*.test.ts"]
  }
  ```
  This will direct [Jest](../J/jest.md) to process `.ts` files with `ts-jest`.

#### What are the prerequisites for using Jest?

  To use [Jest](../J/jest.md) effectively, certain prerequisites should be met:

  - **[Node.js](../N/node-js.md)** : Jest is a Node-based tool, so a current version of Node.js must be installed on your system.
  - **npm or Yarn** : Package managers to install Jest and manage its dependencies.
  - **JavaScript Knowledge** : Familiarity with JavaScript (or TypeScript) is essential since Jest is designed for testing JS codebases.
  - **Project [Setup](../S/setup.md)** : A JavaScript project with a package.json file to configure and include Jest as a dependency.
  - **Understanding of Testing Concepts** : Knowledge of unit testing, mocking, and assertions to write meaningful tests.
  - **ES Module Support** : If using ES Modules, ensure compatibility or configure Babel for transpilation.
  - **Version Control** : (Optional) A version control system like Git to track changes in tests alongside code.
  Install [Jest](../J/jest.md) using npm or Yarn:

  ```
  npm install --save-dev jest
  ```
  or

  ```
  yarn add --dev jest
  ```
  Ensure your `package.json` includes a [test script](../T/test-script.md):

  ```
  "scripts": {
    "test": "jest"
  }
  ```
  For TypeScript projects, install `ts-jest` and `@types/jest` to handle type-checking and provide autocompletion:

  ```
  npm install --save-dev ts-jest @types/jest
  ```
  or

  ```
  yarn add --dev ts-jest @types/jest
  ```
  Finally, familiarity with [Jest](../J/jest.md)'s [API](../A/api.md) and lifecycle methods will help in structuring tests effectively.

  - **[Node.js](../N/node-js.md)** : Jest is a Node-based tool, so a current version of Node.js must be installed on your system.
  - **npm or Yarn** : Package managers to install Jest and manage its dependencies.
  - **JavaScript Knowledge** : Familiarity with JavaScript (or TypeScript) is essential since Jest is designed for testing JS codebases.
  - **Project [Setup](../S/setup.md)** : A JavaScript project with a package.json file to configure and include Jest as a dependency.
  - **Understanding of Testing Concepts** : Knowledge of unit testing, mocking, and assertions to write meaningful tests.
  - **ES Module Support** : If using ES Modules, ensure compatibility or configure Babel for transpilation.
  - **Version Control** : (Optional) A version control system like Git to track changes in tests alongside code.

#### How do you set up a basic Jest testing environment?

  To set up a basic [Jest](../J/jest.md) testing environment, follow these steps:

  1. **Initialize your project** (if not already done) with `npm init` or `yarn init`.
  2. **Install [Jest](../J/jest.md)** using npm or Yarn:
    or

    ```
    npm install --save-dev jest
    ```

    ```
    yarn add --dev jest
    ```

  3. In your `package.json`, add the following script to run [Jest](../J/jest.md):

    ```
    "scripts": {
      "test": "jest"
    }
    ```

  4. **Configure [Jest](../J/jest.md)** if needed. For most projects, [Jest](../J/jest.md) works out of the box with zero configuration. However, if you need to customize [Jest](../J/jest.md)'s behavior, create a `jest.config.js` file or add a `jest` key in your `package.json`.
  5. **Write your tests**. Create files with `.test.js` or `.spec.js` suffixes, or put them in a `__tests__` folder. [Jest](../J/jest.md) will automatically find these files.
  6. **Use `test` or `it`** to define your [test cases](../T/test-case.md):

    ```
    test('adds 1 + 2 to equal 3', () => {
      expect(1 + 2).toBe(3);
    });
    ```

  7. **Run your tests** by executing the [test script](../T/test-script.md):
    or

    ```
    npm test
    ```

    ```
    yarn test
    ```
  [Jest](../J/jest.md) will execute the tests and provide a summary of the results. Adjust your tests and code based on the feedback from the test runs.

  1. **Initialize your project** (if not already done) with `npm init` or `yarn init`.
  2. **Install [Jest](../J/jest.md)** using npm or Yarn:
    or

    ```
    npm install --save-dev jest
    ```

    ```
    yarn add --dev jest
    ```

  3. In your `package.json`, add the following script to run [Jest](../J/jest.md):

    ```
    "scripts": {
      "test": "jest"
    }
    ```

  4. **Configure [Jest](../J/jest.md)** if needed. For most projects, [Jest](../J/jest.md) works out of the box with zero configuration. However, if you need to customize [Jest](../J/jest.md)'s behavior, create a `jest.config.js` file or add a `jest` key in your `package.json`.
  5. **Write your tests**. Create files with `.test.js` or `.spec.js` suffixes, or put them in a `__tests__` folder. [Jest](../J/jest.md) will automatically find these files.
  6. **Use `test` or `it`** to define your [test cases](../T/test-case.md):

    ```
    test('adds 1 + 2 to equal 3', () => {
      expect(1 + 2).toBe(3);
    });
    ```

  7. **Run your tests** by executing the [test script](../T/test-script.md):
    or

    ```
    npm test
    ```

    ```
    yarn test
    ```

#### How do you configure Jest for a project?

  To configure [Jest](../J/jest.md) for a project, create a `jest.config.js` file at the root of your project or define a `jest` key in your `package.json`. Here's a basic example of what a `jest.config.js` file might look like:

  ```
  module.exports = {
    verbose: true,
    testEnvironment: 'node',
    setupFilesAfterEnv: ['./jest.setup.js'],
    transform: {
      '^.+\\.tsx?$': 'ts-jest',
    },
    testMatch: ['**/__tests__/**/*.ts?(x)', '**/?(*.)+(spec|test).ts?(x)'],
    moduleNameMapper: {
      '^@components/(.*)$': '<rootDir>/src/components/$1',
    },
    coverageThreshold: {
      global: {
        branches: 50,
        functions: 50,
        lines: 50,
        statements: -10,
      },
    },
  };
  ```

  - **verbose** : Enables verbose output for test results.
  - **testEnvironment** : Sets the environment in which tests are run.
  - **setupFilesAfterEnv** : Lists scripts to run after the test framework is installed in the environment.
  - **transform** : Specifies how to process files using a transformer.
  - **testMatch** : Determines which files are considered test files.
  - **moduleNameMapper** : Maps module paths for easier imports.
  - **coverageThreshold** : Sets the minimum coverage thresholds for the project.
  For TypeScript projects, you'll need to install `ts-jest` and configure the `transform` property to use it.
  To include the configuration in your `package.json`, it would look like this:

  ```
  "jest": {
    "verbose": true,
    // ... other configurations
  }
  ```
  Remember to install any additional [Jest](../J/jest.md) plugins or presets you need for your project. Adjust the configuration options to match the specific needs of your project, such as custom global variables, module path aliases, or different environments for testing.

  - **verbose** : Enables verbose output for test results.
  - **testEnvironment** : Sets the environment in which tests are run.
  - **setupFilesAfterEnv** : Lists scripts to run after the test framework is installed in the environment.
  - **transform** : Specifies how to process files using a transformer.
  - **testMatch** : Determines which files are considered test files.
  - **moduleNameMapper** : Maps module paths for easier imports.
  - **coverageThreshold** : Sets the minimum coverage thresholds for the project.

### Writing and Running Tests

#### How do you write a basic test in Jest?

  Writing a basic test in [Jest](../J/jest.md) involves creating a test file with `.test.js` or `.spec.js` suffix, importing the necessary modules, and using the `test` or `it` global function to define your [test cases](../T/test-case.md). Here's a succinct example:

  ```
  const sum = require('./sum'); // Import the function to test
  test('adds 1 + 2 to equal 3', () => {
    expect(sum(1, 2)).toBe(3); // Use expect and matchers to test the function
  });
  ```
  In this example, `sum` is a simple function that adds two numbers. The `test` function takes two arguments: a string describing the [test case](../T/test-case.md), and a callback function where the actual testing code is written. The `expect` function is used to assert the expected outcome, and `.toBe` is a matcher that checks for strict equality.
  Remember to structure your tests logically and clearly, so they are easy to read and understand. Use **descriptive test names** and **assertions** that accurately reflect the behavior you are testing. Keep tests **focused** on a single functionality to make them maintainable and to facilitate easier debugging when a test fails.

#### What is the structure of a Jest test?

  A [Jest](../J/jest.md) test structure typically consists of a series of **describe** blocks that group together related tests, and **it** or **test** blocks that define individual [test cases](../T/test-case.md). Here's a basic outline:

  ```
  describe('Component or Functionality Group', () => {
    beforeEach(() => {
      // Initialization or setup before each test runs
    });
    afterEach(() => {
      // Cleanup after each test runs
    });
    it('should do something expected', () => {
      // Test logic for a specific case
      expect(someFunction()).toBe(someValue);
    });
    test('should handle a particular scenario', () => {
      // Another test case
      expect(anotherFunction()).toEqual(anotherValue);
    });
    // Additional it/test cases as needed
  });
  ```

  - **describe** : Groups multiple tests; useful for organizing tests by functionality or components.
  - **beforeEach/afterEach** : Setup/teardown hooks that run before/after each test in the describe block.
  - **it/test** : Defines an individual test case;
    `it`
    is an alias for
    `test`
    , and both are interchangeable.

  - **expect** : Creates an assertion about the expected outcome of the test case.
  Tests can be nested within **describe** blocks for further organization. **beforeAll** and **afterAll** hooks are also available for [setup](../S/setup.md)/teardown that should only happen once before/after all tests in a describe block.

  - **describe** : Groups multiple tests; useful for organizing tests by functionality or components.
  - **beforeEach/afterEach** : Setup/teardown hooks that run before/after each test in the describe block.
  - **it/test** : Defines an individual test case;
    `it`
    is an alias for
    `test`
    , and both are interchangeable.

  - **expect** : Creates an assertion about the expected outcome of the test case.

#### How do you run tests in Jest?

  To run tests in [Jest](../J/jest.md), follow these steps:

  1. **Navigate to your project directory** in the terminal.
  2. Ensure you have a `package.json` file in your project. If not, create one using `npm init`.
  3. **Run tests** using one of the following commands:
    - To run all tests:
      or if Jest is not globally installed:
      or by using an npm script in
      `package.json` :
      then execute with npm:

      ```
      jest
      ```

      ```
      npx jest
      ```

      ```
      "scripts": {
        "test": "jest"
      }
      ```

      ```
      npm test
      ```

    - To run all tests:
      or if Jest is not globally installed:
      or by using an npm script in
      `package.json` :
      then execute with npm:

      ```
      jest
      ```

      ```
      npx jest
      ```

      ```
      "scripts": {
        "test": "jest"
      }
      ```

      ```
      npm test
      ```

  4. **Run a specific test file** by appending the file path:

    ```
    jest path/to/your_test_file.js
    ```

  5. **Watch mode**: To run [Jest](../J/jest.md) in watch mode, which reruns tests on file changes, use the `--watch` flag:

    ```
    jest --watch
    ```

  6. **Filter tests** by test name using the `--testNamePattern` flag:

    ```
    jest --testNamePattern="pattern"
    ```

  7. **Run tests matching a specific filename pattern** with the `--testPathPattern` flag:

    ```
    jest --testPathPattern="pattern"
    ```

  8. **Run tests related to changed files** based on your Git repository with:

    ```
    jest --onlyChanged
    ```

  9. **Run tests in a specific environment** by setting the `testEnvironment` in your [Jest](../J/jest.md) configuration.
  10. **Generate coverage reports** using the `--coverage` flag:

    ```
    jest --coverage
    ```
  [Jest](../J/jest.md) CLI offers many other options, which can be listed by running `jest --help`.

  1. **Navigate to your project directory** in the terminal.
  2. Ensure you have a `package.json` file in your project. If not, create one using `npm init`.
  3. **Run tests** using one of the following commands:
    - To run all tests:
      or if Jest is not globally installed:
      or by using an npm script in
      `package.json` :
      then execute with npm:

      ```
      jest
      ```

      ```
      npx jest
      ```

      ```
      "scripts": {
        "test": "jest"
      }
      ```

      ```
      npm test
      ```

    - To run all tests:
      or if Jest is not globally installed:
      or by using an npm script in
      `package.json` :
      then execute with npm:

      ```
      jest
      ```

      ```
      npx jest
      ```

      ```
      "scripts": {
        "test": "jest"
      }
      ```

      ```
      npm test
      ```

  4. **Run a specific test file** by appending the file path:

    ```
    jest path/to/your_test_file.js
    ```

  5. **Watch mode**: To run [Jest](../J/jest.md) in watch mode, which reruns tests on file changes, use the `--watch` flag:

    ```
    jest --watch
    ```

  6. **Filter tests** by test name using the `--testNamePattern` flag:

    ```
    jest --testNamePattern="pattern"
    ```

  7. **Run tests matching a specific filename pattern** with the `--testPathPattern` flag:

    ```
    jest --testPathPattern="pattern"
    ```

  8. **Run tests related to changed files** based on your Git repository with:

    ```
    jest --onlyChanged
    ```

  9. **Run tests in a specific environment** by setting the `testEnvironment` in your [Jest](../J/jest.md) configuration.
  10. **Generate coverage reports** using the `--coverage` flag:

    ```
    jest --coverage
    ```

#### What are some common assertions in Jest?

  In [Jest](../J/jest.md), assertions are made using the `expect` function, which is chained with "matcher" functions to test values in different ways. Here are some common assertions:

  - **Equality**:

    ```
    expect(5).toBe(5);
    expect({ a: 1 }).toEqual({ a: 1 });
    ```

    - `toBe(value)`
      checks strict equality (===).

    - `toEqual(value)`
      checks value equality, useful for objects and arrays.

    - `toBe(value)`
      checks strict equality (===).

    - `toEqual(value)`
      checks value equality, useful for objects and arrays.

  - **Truthiness**:

    ```
    expect(null).toBeNull();
    expect(undefined).toBeUndefined();
    expect(1).toBeTruthy();
    ```

    - `toBeNull()`
      checks that a value is
      `null`
      .

    - `toBeUndefined()`
      checks that a value is
      `undefined`
      .

    - `toBeDefined()`
      checks that a value is not
      `undefined`
      .

    - `toBeTruthy()`
      checks that a value is truthy.

    - `toBeFalsy()`
      checks that a value is falsy.

    - `toBeNull()`
      checks that a value is
      `null`
      .

    - `toBeUndefined()`
      checks that a value is
      `undefined`
      .

    - `toBeDefined()`
      checks that a value is not
      `undefined`
      .

    - `toBeTruthy()`
      checks that a value is truthy.

    - `toBeFalsy()`
      checks that a value is falsy.

  - **Numbers**:

    ```
    expect(10).toBeGreaterThan(5);
    expect(10).toBeLessThanOrEqual(10);
    ```

    - `toBeGreaterThan(number)`
      checks that a value is greater than a number.

    - `toBeGreaterThanOrEqual(number)`
      checks that a value is greater than or equal to a number.

    - `toBeLessThan(number)`
      checks that a value is less than a number.

    - `toBeLessThanOrEqual(number)`
      checks that a value is less than or equal to a number.

    - `toBeGreaterThan(number)`
      checks that a value is greater than a number.

    - `toBeGreaterThanOrEqual(number)`
      checks that a value is greater than or equal to a number.

    - `toBeLessThan(number)`
      checks that a value is less than a number.

    - `toBeLessThanOrEqual(number)`
      checks that a value is less than or equal to a number.

  - **Strings**:

    ```
    expect('team').toMatch(/T/i);
    ```

    - `toMatch(regexpOrString)`
      checks that a string matches a regular expression or string.

    - `toMatch(regexpOrString)`
      checks that a string matches a regular expression or string.

  - **Arrays**:

    ```
    expect(['Alice', 'Bob', 'Eve']).toContain('Bob');
    ```

    - `toContain(item)`
      checks that an array contains a specific item.

    - `toContain(item)`
      checks that an array contains a specific item.

  - **Exceptions**:

    ```
    expect(() => { throw new Error('Error!'); }).toThrow('Error!');
    ```

    - `toThrow(error?
      )`
      checks that a function throws an error when called.

    - `toThrow(error?
      )`
      checks that a function throws an error when called.

  - **Objects**:

    ```
    expect({ a: { b: 1 } }).toHaveProperty('a.b', 1);
    ```

    - `toHaveProperty(keyPath, value?
      )`
      checks that an object has a property at the specified key path, optionally checking the value.

    - `toHaveProperty(keyPath, value?
      )`
      checks that an object has a property at the specified key path, optionally checking the value.
  These assertions help ensure that the code behaves as expected, and they are a crucial part of writing comprehensive [test suites](../T/test-suite.md) with [Jest](../J/jest.md).

  - **Equality**:

    ```
    expect(5).toBe(5);
    expect({ a: 1 }).toEqual({ a: 1 });
    ```

    - `toBe(value)`
      checks strict equality (===).

    - `toEqual(value)`
      checks value equality, useful for objects and arrays.

    - `toBe(value)`
      checks strict equality (===).

    - `toEqual(value)`
      checks value equality, useful for objects and arrays.

  - **Truthiness**:

    ```
    expect(null).toBeNull();
    expect(undefined).toBeUndefined();
    expect(1).toBeTruthy();
    ```

    - `toBeNull()`
      checks that a value is
      `null`
      .

    - `toBeUndefined()`
      checks that a value is
      `undefined`
      .

    - `toBeDefined()`
      checks that a value is not
      `undefined`
      .

    - `toBeTruthy()`
      checks that a value is truthy.

    - `toBeFalsy()`
      checks that a value is falsy.

    - `toBeNull()`
      checks that a value is
      `null`
      .

    - `toBeUndefined()`
      checks that a value is
      `undefined`
      .

    - `toBeDefined()`
      checks that a value is not
      `undefined`
      .

    - `toBeTruthy()`
      checks that a value is truthy.

    - `toBeFalsy()`
      checks that a value is falsy.

  - **Numbers**:

    ```
    expect(10).toBeGreaterThan(5);
    expect(10).toBeLessThanOrEqual(10);
    ```

    - `toBeGreaterThan(number)`
      checks that a value is greater than a number.

    - `toBeGreaterThanOrEqual(number)`
      checks that a value is greater than or equal to a number.

    - `toBeLessThan(number)`
      checks that a value is less than a number.

    - `toBeLessThanOrEqual(number)`
      checks that a value is less than or equal to a number.

    - `toBeGreaterThan(number)`
      checks that a value is greater than a number.

    - `toBeGreaterThanOrEqual(number)`
      checks that a value is greater than or equal to a number.

    - `toBeLessThan(number)`
      checks that a value is less than a number.

    - `toBeLessThanOrEqual(number)`
      checks that a value is less than or equal to a number.

  - **Strings**:

    ```
    expect('team').toMatch(/T/i);
    ```

    - `toMatch(regexpOrString)`
      checks that a string matches a regular expression or string.

    - `toMatch(regexpOrString)`
      checks that a string matches a regular expression or string.

  - **Arrays**:

    ```
    expect(['Alice', 'Bob', 'Eve']).toContain('Bob');
    ```

    - `toContain(item)`
      checks that an array contains a specific item.

    - `toContain(item)`
      checks that an array contains a specific item.

  - **Exceptions**:

    ```
    expect(() => { throw new Error('Error!'); }).toThrow('Error!');
    ```

    - `toThrow(error?
      )`
      checks that a function throws an error when called.

    - `toThrow(error?
      )`
      checks that a function throws an error when called.

  - **Objects**:

    ```
    expect({ a: { b: 1 } }).toHaveProperty('a.b', 1);
    ```

    - `toHaveProperty(keyPath, value?
      )`
      checks that an object has a property at the specified key path, optionally checking the value.

    - `toHaveProperty(keyPath, value?
      )`
      checks that an object has a property at the specified key path, optionally checking the value.

#### How do you group tests in Jest?

  In [Jest](../J/jest.md), you can group tests using the `describe` function. This function allows you to create a block that groups together several related tests. Here's a basic example:

  ```
  describe('My Feature', () => {
    test('should do behavior A', () => {
      // Test for behavior A
    });
    test('should do behavior B', () => {
      // Test for behavior B
    });
  });
  ```
  Each `describe` block can contain its own [setup](../S/setup.md) and teardown for the group of tests using `beforeEach`, `afterEach`, `beforeAll`, and `afterAll` functions. This helps in organizing tests logically and managing shared [setup](../S/setup.md) and teardown processes efficiently.
  Nested `describe` blocks can be used for more granular grouping:

  ```
  describe('My Feature', () => {
    describe('Behavior A', () => {
      test('should do something specific', () => {
        // Test for a specific aspect of behavior A
      });
    });
    describe('Behavior B', () => {
      test('should do something else', () => {
        // Test for a specific aspect of behavior B
      });
    });
  });
  ```
  Using `describe` blocks is particularly useful for differentiating between various states or conditions of the feature being tested, and it enhances the readability of [test reports](../T/test-report.md) by clearly showing which group a failing test belongs to.

### Advanced Concepts

#### What is mocking in Jest and how is it used?

  Mocking in [Jest](../J/jest.md) is a technique used to isolate and simulate the behavior of external modules or functions that a piece of code depends on. By creating mock functions or objects, you can control the inputs and outputs of these dependencies, allowing for more predictable and controlled testing environments.
  **Mock functions** can be created using `jest.fn()` to track calls and define return values. They can replace actual functions in your modules, letting you assert how they have been called and with what arguments.

  ```
  const mockFunction = jest.fn();
  mockFunction.mockReturnValue('mocked value');
  ```
  **Manual mocks** are useful for modules and complex dependencies. You can create a `__mocks__` directory adjacent to the module, and [Jest](../J/jest.md) will use the mocked version instead of the real one when the `jest.mock()` function is called in your tests.

  ```
  // In your test file
  jest.mock('./path/to/module');
  ```
  **Automatic mocking** with `jest.mock()` allows [Jest](../J/jest.md) to take over module imports and replace them with a suitable mock object, with all exports being mocked functions.

  ```
  // In your test file
  jest.mock('axios');
  ```
  Mocking is also used to **stub out functionality** that would otherwise have side effects, such as network requests or file system operations, by replacing them with mock implementations that mimic the behavior without performing the actual operation.
  Mocking in [Jest](../J/jest.md) is essential for creating unit tests that are independent of external factors and for ensuring that your tests are deterministic, meaning they produce the same results every time they are run.

#### How does Jest handle asynchronous testing?

  [Jest](../J/jest.md) handles asynchronous testing by providing several methods to deal with different types of async code. These include:

  - **Callbacks** : For testing older callback-style code, Jest provides the
    `done`
    parameter in test functions. Call
    `done()`
    when the async operation completes to signal Jest that the test is finished.

  ```
  test('async test with callback', done => {
    setTimeout(() => {
      expect(true).toBe(true);
      done();
    }, 1000);
  });
  ```

  - **Promises** : If the code returns a promise, return it from the test, and Jest will wait for it to resolve or reject.

  ```
  test('async test with promise', () => {
    return fetchData().then(data => {
      expect(data).toBe('expected data');
    });
  });
  ```

  - **Async/Await** : For modern async code, use
    `async`
    functions and
    `await`
    the asynchronous operation. Jest will wait for the
    `async`
    function to resolve before completing the test.

  ```
  test('async test with async/await', async () => {
    const data = await fetchData();
    expect(data).toBe('expected data');
  });
  ```

  - **Timers** : Jest can mock timers and control time for operations that use
    `setTimeout`
    ,
    `setInterval`
    , or
    `setImmediate`
    with
    `jest.useFakeTimers()`
    and related timer control functions.

  ```
  jest.useFakeTimers();
  test('async test with timers', () => {
    const callback = jest.fn();
    setTimeout(callback, 1000);
    jest.runAllTimers();
    expect(callback).toHaveBeenCalled();
  });
  ```
  These methods allow for comprehensive testing of asynchronous operations, ensuring that tests only complete when all async actions have been accounted for.

  - **Callbacks** : For testing older callback-style code, Jest provides the
    `done`
    parameter in test functions. Call
    `done()`
    when the async operation completes to signal Jest that the test is finished.

  - **Promises** : If the code returns a promise, return it from the test, and Jest will wait for it to resolve or reject.
  - **Async/Await** : For modern async code, use
    `async`
    functions and
    `await`
    the asynchronous operation. Jest will wait for the
    `async`
    function to resolve before completing the test.

  - **Timers** : Jest can mock timers and control time for operations that use
    `setTimeout`
    ,
    `setInterval`
    , or
    `setImmediate`
    with
    `jest.useFakeTimers()`
    and related timer control functions.

#### How can you use Jest for snapshot testing?

  [Jest](../J/jest.md)'s snapshot testing feature allows you to **test the "shape" of your code's output**. This is particularly useful for UI components, ensuring that changes to components don't cause unexpected results.
  To use [Jest](../J/jest.md) for snapshot testing, follow these steps:

  1. **Write a test**
    that renders your component or calls your function.

  2. Use
    `expect`
    along with the
    `toMatchSnapshot()`
    matcher to
    **assert that the output matches the saved snapshot**
    .
  Here's a basic example using a React component:

  ```
  import React from 'react';
  import renderer from 'react-test-renderer';
  import MyComponent from './MyComponent';
  test('MyComponent renders correctly', () => {
    const tree = renderer.create(<MyComponent />).toJSON();
    expect(tree).toMatchSnapshot();
  });
  ```
  When this test runs for the first time, [Jest](../J/jest.md) creates a snapshot file in a `__snapshots__` directory next to the test file. The snapshot contains a string representation of the component's render output.
  On subsequent test runs, [Jest](../J/jest.md) compares the rendered output with the saved snapshot. If there's a difference, the test fails, prompting a review. If the change is intentional, **update the snapshot** using [Jest](../J/jest.md)'s `--updateSnapshot` or `-u` flag:

  ```
  jest --updateSnapshot
  ```
  or for a specific test file:

  ```
  jest MyComponent.test.js --updateSnapshot
  ```
  Remember, snapshots should be committed alongside code changes. Review snapshots during code reviews to **catch unintended changes**. Use snapshot testing judiciously, as over-reliance can lead to large snapshot files and reduced test sensitivity to meaningful changes.

  1. **Write a test**
    that renders your component or calls your function.

  2. Use
    `expect`
    along with the
    `toMatchSnapshot()`
    matcher to
    **assert that the output matches the saved snapshot**
    .

#### What is the role of 'describe' function in Jest?

  In [Jest](../J/jest.md), the `describe` function is used to **group together related tests**. It serves as a way to organize your [test suite](../T/test-suite.md) by **encapsulating multiple [test cases](../T/test-case.md)** that test a specific feature or component. This is particularly useful for readability and maintenance, as it allows developers to see at a glance which tests are related and to run a subset of tests that are relevant to the area of code they are working on.
  The `describe` block can contain any number of `test` or `it` blocks, and can also be **nested** within other `describe` blocks to further structure your tests hierarchically. Each `describe` block can also have its own `beforeEach`, `afterEach`, `beforeAll`, and `afterAll` lifecycle methods, which apply only to the tests within that `describe` block.
  Here's a basic example of using `describe` in [Jest](../J/jest.md):

  ```
  describe('MyComponent', () => {
    beforeEach(() => {
      // Setup code specific to this group
    });
    test('should render correctly', () => {
      // Test case for rendering
    });
    test('should handle user input', () => {
      // Test case for user input
    });
  });
  ```
  Using `describe` helps to keep tests **DRY** (Don't Repeat Yourself) by allowing shared [setup](../S/setup.md) and teardown code for the tests in the group, and it enhances the **organization** and **readability** of the test output, as [Jest](../J/jest.md) will report results based on these groupings.

#### How can you use 'beforeEach' and 'afterEach' in Jest?

  In [Jest](../J/jest.md), `beforeEach` and `afterEach` are lifecycle methods used to run some code before and after each test within a `describe` block. They help in setting up preconditions and cleaning up after tests to avoid side effects.
  Use `beforeEach` when you want to initialize certain variables, mock functions, or set up the environment for each [test case](../T/test-case.md). It ensures that every test runs with a fresh state.

  ```
  beforeEach(() => {
    // Initialization or setup code here
  });
  ```
  `afterEach` is used for teardown activities, such as clearing mocks, resetting modules, or releasing resources used by the tests.

  ```
  afterEach(() => {
    // Teardown or cleanup code here
  });
  ```
  **Example:**

  ```
  describe('test suite', () => {
    beforeEach(() => {
      // Code to set up state before each test
    });
    afterEach(() => {
      // Code to clean up after each test
    });
    test('test case 1', () => {
      // Test code
    });
    test('test case 2', () => {
      // Test code
    });
  });
  ```
  In this example, the [setup](../S/setup.md) code will run before `test case 1` and `test case 2`, and the cleanup code will run after each of these [test cases](../T/test-case.md) completes. This ensures that each test is isolated and does not affect the other.
