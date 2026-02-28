# Chai.js


<!-- TOC START -->
- [Related Terms:](#related-terms)
  - [See also:](#see-also)
- [Questions about Chai.js ?](#questions-about-chaijs)
  - [Basics and Importance](#basics-and-importance)
    - [What is Chai.js?](#what-is-chaijs)
    - [Why is Chai.js used in testing?](#why-is-chaijs-used-in-testing)
    - [What are the key features of Chai.js?](#what-are-the-key-features-of-chaijs)
    - [How does Chai.js compare to other JavaScript testing libraries?](#how-does-chaijs-compare-to-other-javascript-testing-libraries)
    - [What are the advantages of using Chai.js for testing?](#what-are-the-advantages-of-using-chaijs-for-testing)
  - [Installation and Setup](#installation-and-setup)
    - [How do you install Chai.js?](#how-do-you-install-chaijs)
    - [What are the prerequisites for using Chai.js?](#what-are-the-prerequisites-for-using-chaijs)
    - [How do you set up Chai.js for a project?](#how-do-you-set-up-chaijs-for-a-project)
    - [How do you import Chai.js into a JavaScript file?](#how-do-you-import-chaijs-into-a-javascript-file)
  - [Assertions](#assertions)
    - [What is an assertion in Chai.js?](#what-is-an-assertion-in-chaijs)
    - [How do you write a basic assertion in Chai.js?](#how-do-you-write-a-basic-assertion-in-chaijs)
    - [What are the different types of assertions available in Chai.js?](#what-are-the-different-types-of-assertions-available-in-chaijs)
    - [How do you assert that a function throws an error in Chai.js?](#how-do-you-assert-that-a-function-throws-an-error-in-chaijs)
    - [How do you assert deep equality in Chai.js?](#how-do-you-assert-deep-equality-in-chaijs)
  - [Plugins](#plugins)
    - [What are Chai.js plugins?](#what-are-chaijs-plugins)
    - [How do you use a Chai.js plugin?](#how-do-you-use-a-chaijs-plugin)
    - [What are some popular Chai.js plugins and what do they do?](#what-are-some-popular-chaijs-plugins-and-what-do-they-do)
    - [How do you create your own Chai.js plugin?](#how-do-you-create-your-own-chaijs-plugin)
  - [Advanced Concepts](#advanced-concepts)
    - [How do you use Chai.js with asynchronous code?](#how-do-you-use-chaijs-with-asynchronous-code)
    - [How do you use Chai.js with Promises?](#how-do-you-use-chaijs-with-promises)
    - [What is Chai.js's .should interface and how does it work?](#what-is-chaijss-should-interface-and-how-does-it-work)
    - [How do you customize Chai.js's assertion error messages?](#how-do-you-customize-chaijss-assertion-error-messages)
<!-- TOC END -->

Chai.js

, often simply referred to as Chai, is a

BDD

/TDD (Behavior-Driven Development/

Test-Driven Development

) assertion library for

Node.js

and browsers. It pairs seamlessly with popular JavaScript testing frameworks, such as Mocha and

Jasmine

. Chai provides developers with the capability to express assertions in a readable language, mimicking natural language constructions.

## Related Terms:

- [Assertion library](../A/assertion-library.md)
- [Jest](../J/jest.md)
- [Jasmine](../J/jasmine.md)

### See also:

- [Official Website](https://www.chaijs.com/)

## Questions about Chai.js ?

### Basics and Importance

#### What is Chai.js?

  [Chai.js](../C/chai-js.md) is a **behavior-driven development ([BDD](../B/bdd.md))** / **[test-driven development](../T/test-driven-development.md) (TDD)** assertion library for [Node.js](../N/node-js.md) and the browser that can be delightfully paired with any JavaScript testing framework. It provides developers with a rich set of assertions that are readable and expressive.
  [Chai.js](../C/chai-js.md) offers three different styles of assertions: **should**, **expect**, and **assert**. Each style has its own syntax, allowing developers to choose the one that best fits their preference or the needs of their project.

  ```
  // Should style
  should.exist(foo);
  // Expect style
  expect(foo).to.exist;
  // Assert style
  assert.exists(foo);
  ```
  [Chai.js](../C/chai-js.md) assertions can handle a variety of test conditions, including but not limited to, property values, deep equality checks, and thrown exceptions. It also supports testing asynchronous operations, both with callbacks and promises.
  The library is extensible through plugins, which can add new assertions and test conditions to fit specific testing requirements. This extensibility allows [Chai.js](../C/chai-js.md) to adapt to a wide range of [use cases](../U/use-case.md) and integrate with other tools and libraries.
  [Chai.js](../C/chai-js.md) is often used in combination with other testing tools such as Mocha, [Jest](../J/jest.md), or Karma, providing a complete testing solution. It is installed via npm and can be easily integrated into any JavaScript project, making it a convenient choice for developers looking to enhance their testing capabilities.

#### Why is Chai.js used in testing?

  [Chai.js](../C/chai-js.md) is utilized in testing primarily for its **flexibility** and **readability** when writing assertions. It allows developers to write tests that are expressive and easy to maintain. By offering **Behavior-Driven Development ([BDD](../B/bdd.md))** and **[Test-Driven Development](../T/test-driven-development.md) (TDD)** assertion styles, it caters to different preferences and can easily integrate with various testing frameworks like Mocha or [Jest](../J/jest.md).
  The use of [Chai.js](../C/chai-js.md) enhances the **debugging experience** due to its informative error messages, which detail the expected versus the [actual result](../A/actual-result.md) when an assertion fails. This feature significantly reduces the time spent on identifying the cause of a failed test.
  Moreover, [Chai.js](../C/chai-js.md) supports **chainable assertions**, which enable the composition of complex conditions in a readable manner. This chaining mimics natural language, making the tests more understandable to new developers or non-technical stakeholders.
  [Chai.js](../C/chai-js.md)'s extensibility through plugins allows for customization and extension of its core functionalities. This means that teams can adapt the library to their specific testing needs without waiting for the core package to provide those features.
  In summary, [Chai.js](../C/chai-js.md) is chosen for its **expressive syntax**, **helpful error messages**, **compatibility with other tools**, and **extensibility**, which all contribute to a more efficient and pleasant testing experience.

#### What are the key features of Chai.js?

  [Chai.js](../C/chai-js.md) offers a range of **key features** that make it a versatile and powerful assertion library for [test automation](../T/test-automation.md):

  - **[BDD](../B/bdd.md)/TDD Assertion Styles**: Chai provides two main styles of assertions: **Behavior-Driven Development ([BDD](../B/bdd.md))** with `expect` or `should`, and **[Test-Driven Development](../T/test-driven-development.md) (TDD)** with `assert`. This allows developers to choose the style that best fits their testing philosophy or to mix and match within their [test suite](../T/test-suite.md).
  - **Chainable Language**: Assertions can be chained together to form readable statements using natural language constructs. This improves the readability of tests and makes writing assertions more intuitive.
  - **Type Checking**: Chai includes assertions for type checking, such as `expect(value).to.be.a('string')`, which enhances the robustness of tests by ensuring that values are of the expected type.
  - **Property Testing**: It allows for easy checking of object properties, which is useful for testing [API](../A/api.md) responses and complex data structures.
  - **Equality and Comparisons**: Chai provides a comprehensive set of assertions for equality and comparison, including deep equality checks and assertions for greater than/less than relationships.
  - **Error Handling**: Assertions for error handling are included, allowing developers to assert that certain functions throw expected errors under specific conditions.
  - **Plugin Architecture**: Chai's extensibility through plugins means that it can be adapted to a wide variety of [use cases](../U/use-case.md) and integrated with other libraries and tools.
  - **Asynchronous Support**: It has built-in support for testing asynchronous code, including promises, which is essential for modern JavaScript development.
  - **Custom Messages**: Developers can provide custom error messages for assertions, which can make debugging failed tests easier and more informative.
  - **Cross-Platform**: [Chai.js](../C/chai-js.md) works in both [Node.js](../N/node-js.md) and browser environments, making it suitable for a wide range of JavaScript projects.
  - **[BDD](../B/bdd.md)/TDD Assertion Styles**: Chai provides two main styles of assertions: **Behavior-Driven Development ([BDD](../B/bdd.md))** with `expect` or `should`, and **[Test-Driven Development](../T/test-driven-development.md) (TDD)** with `assert`. This allows developers to choose the style that best fits their testing philosophy or to mix and match within their [test suite](../T/test-suite.md).
  - **Chainable Language**: Assertions can be chained together to form readable statements using natural language constructs. This improves the readability of tests and makes writing assertions more intuitive.
  - **Type Checking**: Chai includes assertions for type checking, such as `expect(value).to.be.a('string')`, which enhances the robustness of tests by ensuring that values are of the expected type.
  - **Property Testing**: It allows for easy checking of object properties, which is useful for testing [API](../A/api.md) responses and complex data structures.
  - **Equality and Comparisons**: Chai provides a comprehensive set of assertions for equality and comparison, including deep equality checks and assertions for greater than/less than relationships.
  - **Error Handling**: Assertions for error handling are included, allowing developers to assert that certain functions throw expected errors under specific conditions.
  - **Plugin Architecture**: Chai's extensibility through plugins means that it can be adapted to a wide variety of [use cases](../U/use-case.md) and integrated with other libraries and tools.
  - **Asynchronous Support**: It has built-in support for testing asynchronous code, including promises, which is essential for modern JavaScript development.
  - **Custom Messages**: Developers can provide custom error messages for assertions, which can make debugging failed tests easier and more informative.
  - **Cross-Platform**: [Chai.js](../C/chai-js.md) works in both [Node.js](../N/node-js.md) and browser environments, making it suitable for a wide range of JavaScript projects.

#### How does Chai.js compare to other JavaScript testing libraries?

  [Chai.js](../C/chai-js.md) stands out in the JavaScript testing landscape for its **flexible assertion styles**: [BDD](../B/bdd.md) (expect/should) and TDD (assert). This adaptability allows developers to choose a style that best fits their preferences or existing codebase.
  Compared to **[Jest](../J/jest.md)**, which is a full-fledged testing framework providing its own assertions, Chai is more of an assertion library that can be paired with any testing framework like Mocha or [Jasmine](../J/jasmine.md). [Jest](../J/jest.md)'s assertions are built-in and cannot be separated from the framework, while Chai's assertions are standalone and can be extended with plugins.
  **[Jasmine](../J/jasmine.md)** comes with its own assertion library, so using Chai with [Jasmine](../J/jasmine.md) would be for preference reasons rather than necessity. Chai might be chosen for its richer plugin ecosystem or specific assertion style not found in [Jasmine](../J/jasmine.md).
  **Mocha** does not come with an assertion library, making Chai a popular choice for Mocha users. The combination of Mocha's test running capabilities and Chai's assertions provides a powerful and flexible testing [setup](../S/setup.md).
  **Sinon** is often used alongside Chai for spies, mocks, and stubs. While Sinon has some assertions, they are mainly focused on these three areas, and Chai is used for more general assertions. The `sinon-chai` plugin allows for seamless integration of Sinon's capabilities with Chai's assertion syntax.
  In summary, [Chai.js](../C/chai-js.md)'s main comparison point is its **flexible syntax** and **extensibility through plugins**, allowing it to integrate well with various testing frameworks and complement libraries like Sinon for comprehensive testing needs.

#### What are the advantages of using Chai.js for testing?

  [Chai.js](../C/chai-js.md) offers several advantages for [test automation](../T/test-automation.md):

  - **Fluent and Readable Syntax**: Chai's chainable language constructs make tests easier to read and write. Its [BDD](../B/bdd.md)/TDD style assertions provide clear language for [test cases](../T/test-case.md).
  - **Flexibility**: With interfaces like `expect`, `should`, and `assert`, Chai accommodates different testing styles and preferences.
  - **Extensibility**: Custom plugins can be created or existing ones used to extend Chai's functionality, allowing for more specialized assertions tailored to specific needs.
  - **Compatibility**: Works seamlessly with various testing frameworks like Mocha, [Jest](../J/jest.md), and Karma, making it versatile for different environments.
  - **Rich Assertion Library**: Offers a wide range of assertions out of the box, reducing the need to write complex logic for tests.
  - **Cross-Platform**: Can be used in both [Node.js](../N/node-js.md) and browser environments, ensuring consistent testing across platforms.
  - **Community Support**: A large community and ecosystem mean better support, continuous improvements, and a wealth of resources for troubleshooting.
  - **Error Handling**: Provides detailed error messages that can include stack traces, making debugging easier.
  - **Asynchronous Support**: Built-in support for testing asynchronous code with Promises and async/await patterns.
  By leveraging these advantages, [Chai.js](../C/chai-js.md) enhances the efficiency, readability, and [maintainability](../M/maintainability.md) of [test suites](../T/test-suite.md), contributing to a more robust and reliable automation process.

  - **Fluent and Readable Syntax**: Chai's chainable language constructs make tests easier to read and write. Its [BDD](../B/bdd.md)/TDD style assertions provide clear language for [test cases](../T/test-case.md).
  - **Flexibility**: With interfaces like `expect`, `should`, and `assert`, Chai accommodates different testing styles and preferences.
  - **Extensibility**: Custom plugins can be created or existing ones used to extend Chai's functionality, allowing for more specialized assertions tailored to specific needs.
  - **Compatibility**: Works seamlessly with various testing frameworks like Mocha, [Jest](../J/jest.md), and Karma, making it versatile for different environments.
  - **Rich Assertion Library**: Offers a wide range of assertions out of the box, reducing the need to write complex logic for tests.
  - **Cross-Platform**: Can be used in both [Node.js](../N/node-js.md) and browser environments, ensuring consistent testing across platforms.
  - **Community Support**: A large community and ecosystem mean better support, continuous improvements, and a wealth of resources for troubleshooting.
  - **Error Handling**: Provides detailed error messages that can include stack traces, making debugging easier.
  - **Asynchronous Support**: Built-in support for testing asynchronous code with Promises and async/await patterns.

### Installation and Setup

#### How do you install Chai.js?

  To install **[Chai.js](../C/chai-js.md)**, ensure you have **[Node.js](../N/node-js.md)** and **npm** (Node Package Manager) installed. Open your terminal or command prompt and navigate to your project directory. Run the following command:

  ```
  npm install chai --save-dev
  ```
  This command installs [Chai.js](../C/chai-js.md) as a development dependency, adding it to your `package.json` file. Once the installation is complete, you can import Chai in your test files using:
  For CommonJS modules:

  ```
  const chai = require('chai');
  ```
  For ES6 modules:

  ```
  import chai from 'chai';
  ```
  You can then use Chai's `expect`, `should`, or `assert` interfaces to write your tests. Remember to also install a [test runner](../T/test-runner.md) like **Mocha** or **[Jest](../J/jest.md)** if you haven't already, as Chai is an assertion library and does not provide a test framework itself.

#### What are the prerequisites for using Chai.js?

  To use **[Chai.js](../C/chai-js.md)**, ensure the following prerequisites are met:

  - **[Node.js](../N/node-js.md)** : Chai is a Node.js library, so you need Node.js installed on your system. The version should be compatible with the version of Chai you plan to use.
  - **NPM or Yarn** : These are package managers that handle the installation of Chai and its dependencies. They also manage project-specific packages.
  - **A [test runner](../T/test-runner.md)** : Chai is an assertion library and does not include a test runner. You need a test runner like Mocha, Jest, or Karma to execute your tests.
  - **Project [setup](../S/setup.md)** : Your project should be initialized with a
    `package.json`
    file if you're using NPM or Yarn. This file tracks dependencies and scripts related to your project.

  - **Knowledge of JavaScript** : As Chai is a JavaScript library, a good understanding of JavaScript, including ES6 features, is essential.
  - **Understanding of testing concepts** : Familiarity with unit testing, test-driven development (TDD), and behavior-driven development (BDD) is beneficial since Chai supports these testing methodologies.
  To install Chai, run the following command in your project directory:

  ```
  npm install chai --save-dev
  ```
  Or, if you're using Yarn:

  ```
  yarn add chai --dev
  ```
  Once installed, you can import Chai in your test files using:

  ```
  const chai = require('chai');
  ```
  Or, if you're using ES6 modules:

  ```
  import chai from 'chai';
  ```
  Ensure your [test environment](../T/test-environment.md) is properly configured to use Chai with your chosen [test runner](../T/test-runner.md) and assertion style (`expect`, `should`, or `assert`).

  - **[Node.js](../N/node-js.md)** : Chai is a Node.js library, so you need Node.js installed on your system. The version should be compatible with the version of Chai you plan to use.
  - **NPM or Yarn** : These are package managers that handle the installation of Chai and its dependencies. They also manage project-specific packages.
  - **A [test runner](../T/test-runner.md)** : Chai is an assertion library and does not include a test runner. You need a test runner like Mocha, Jest, or Karma to execute your tests.
  - **Project [setup](../S/setup.md)** : Your project should be initialized with a
    `package.json`
    file if you're using NPM or Yarn. This file tracks dependencies and scripts related to your project.

  - **Knowledge of JavaScript** : As Chai is a JavaScript library, a good understanding of JavaScript, including ES6 features, is essential.
  - **Understanding of testing concepts** : Familiarity with unit testing, test-driven development (TDD), and behavior-driven development (BDD) is beneficial since Chai supports these testing methodologies.

#### How do you set up Chai.js for a project?

  To set up [Chai.js](../C/chai-js.md) for your project, follow these steps:

  1. **Install Chai** using npm or yarn if you haven't already:
    or

    ```
    npm install chai --save-dev
    ```

    ```
    yarn add chai --dev
    ```

  2. **Import Chai** in your test file:

    ```
    const chai = require('chai');
    ```

  3. **Choose and set up an assertion style**. Chai provides `should`, `expect`, and `assert` styles. For example, to use `expect`, you would write:

    ```
    const expect = chai.expect;
    ```

  4. **Write your tests** using the chosen assertion style. Here's a simple test example using `expect`:

    ```
    expect(2 + 2).to.equal(4);
    ```

  5. **Run your tests** using your chosen [test runner](../T/test-runner.md) (e.g., Mocha, [Jest](../J/jest.md)).
  6. Optionally, **configure Chai** with additional settings if needed, such as using plugins or adding custom messages to assertions.
  7. **Integrate Chai with other tools** like [test runners](../T/test-runner.md) or mocking libraries as necessary for your testing environment.
  Remember to **check your project's dependencies** to ensure they are compatible with the version of Chai you are using. Keep Chai and any plugins updated to benefit from the latest features and [bug](../B/bug.md) fixes.

  1. **Install Chai** using npm or yarn if you haven't already:
    or

    ```
    npm install chai --save-dev
    ```

    ```
    yarn add chai --dev
    ```

  2. **Import Chai** in your test file:

    ```
    const chai = require('chai');
    ```

  3. **Choose and set up an assertion style**. Chai provides `should`, `expect`, and `assert` styles. For example, to use `expect`, you would write:

    ```
    const expect = chai.expect;
    ```

  4. **Write your tests** using the chosen assertion style. Here's a simple test example using `expect`:

    ```
    expect(2 + 2).to.equal(4);
    ```

  5. **Run your tests** using your chosen [test runner](../T/test-runner.md) (e.g., Mocha, [Jest](../J/jest.md)).
  6. Optionally, **configure Chai** with additional settings if needed, such as using plugins or adding custom messages to assertions.
  7. **Integrate Chai with other tools** like [test runners](../T/test-runner.md) or mocking libraries as necessary for your testing environment.

#### How do you import Chai.js into a JavaScript file?

  To import [Chai.js](../C/chai-js.md) into a JavaScript file, first ensure that Chai is installed in your project. If it's not already installed, you can add it using a package manager like npm with the command `npm install chai`.
  Once Chai is installed, you can import it into your JavaScript file using either CommonJS or ES6 module syntax, depending on your environment and project [setup](../S/setup.md).
  For **CommonJS** (typically used in [Node.js](../N/node-js.md) environments), use the `require` function:

  ```
  const chai = require('chai');
  const expect = chai.expect;
  ```
  For **ES6 modules** (which might be used in front-end projects with a build system that supports ES6 modules), use the `import` statement:

  ```
  import chai from 'chai';
  const expect = chai.expect;
  ```
  After importing, you can use Chai's assertion methods, such as `expect`, `should`, or `assert`, to write your tests.
  If you're using **TypeScript**, you can import Chai in a similar manner, but you might also need to install type definitions for Chai:

  ```
  npm install @types/chai
  ```
  Then, in your TypeScript file:

  ```
  import * as chai from 'chai';
  const expect = chai.expect;
  ```
  Remember to configure your TypeScript compiler to recognize ES6 syntax if you're using `import` statements.

### Assertions

#### What is an assertion in Chai.js?

  An **assertion** in [Chai.js](../C/chai-js.md) is a statement that evaluates an expression or a value in your tests. It checks if that expression or value meets certain conditions, and if it doesn't, the assertion will fail, causing the test to fail. Assertions are the core component of [test suites](../T/test-suite.md), as they validate the behavior of the code under test.
  Chai provides several assertion styles, but regardless of the style, an assertion typically has three parts:

  1. **Actual value** : The value you are testing, which comes from your code.
  2. **Expected value** : The value you expect, which you define in your test.
  3. **Matcher function** : A function that compares the actual value to the expected value.
  Here's an example of a simple assertion using Chai's `expect` interface:

  ```
  const expect = require('chai').expect;
  expect(2 + 2).to.equal(4);
  ```
  In this case, `2 + 2` is the actual value, `4` is the expected value, and `.to.equal` is the matcher function.
  Chai assertions can be chained to perform more complex checks:

  ```
  expect([1, 2, 3]).to.include(2).and.to.have.lengthOf(3);
  ```
  Here, `.include(2)` checks if the array contains the number 2, and `.have.lengthOf(3)` checks if the array's length is 3. The `.and` chain is used to combine multiple assertions on the same subject.
  Assertions are essential for verifying that your code behaves as expected and are a fundamental part of writing effective and reliable tests with [Chai.js](../C/chai-js.md).

  1. **Actual value** : The value you are testing, which comes from your code.
  2. **Expected value** : The value you expect, which you define in your test.
  3. **Matcher function** : A function that compares the actual value to the expected value.

#### How do you write a basic assertion in Chai.js?

  To write a basic assertion in [Chai.js](../C/chai-js.md), you can use any of its interfaces: `expect`, `should`, or `assert`. Here's an example using the `expect` interface:

  ```
  const expect = require('chai').expect;
  describe('Array', function() {
    describe('#indexOf()', function() {
      it('should return -1 when the value is not present', function() {
        expect([1, 2, 3].indexOf(4)).to.equal(-1);
      });
    });
  });
  ```
  In this example, the `expect` function is used to make an assertion about the result of `[1, 2, 3].indexOf(4)`. The `.to.equal(-1)` chain is the actual assertion, stating that the [expected result](../E/expected-result.md) should be `-1`.
  For the `should` interface, the syntax would be slightly different:

  ```
  const should = require('chai').should();
  describe('Array', function() {
    describe('#indexOf()', function() {
      it('should return -1 when the value is not present', function() {
        [1, 2, 3].indexOf(4).should.equal(-1);
      });
    });
  });
  ```
  And for the `assert` interface, which is more traditional and does not use chaining:

  ```
  const assert = require('chai').assert;
  describe('Array', function() {
    describe('#indexOf()', function() {
      it('should return -1 when the value is not present', function() {
        assert.equal([1, 2, 3].indexOf(4), -1);
      });
    });
  });
  ```
  Each of these examples accomplishes the same thing: they assert that the `indexOf` method, when called with a value not present in the array, returns `-1`. Choose the interface that best fits your coding style or team's standards.

#### What are the different types of assertions available in Chai.js?

  [Chai.js](../C/chai-js.md) offers three assertion styles: **should**, **expect**, and **assert**. Each style provides a variety of assertions to test different conditions:
  ### Should & Expect
  These [BDD](../B/bdd.md) (Behavior-Driven Development) styles are similar in functionality but differ in syntax. They provide a chainable language to construct assertions.

  - **.equal(value)** : Asserts strict equality (
    `===`
    ).

  - **.eql(value)** : Asserts deep equality.
  - **.above(value)** : Asserts number is greater than value.
  - **.least(value)** : Asserts number is at least equal to value.
  - **.below(value)** : Asserts number is less than value.
  - **.most(value)** : Asserts number is at most equal to value.
  - **.instanceOf(constructor)** : Asserts instance of a constructor.
  - **.property(name, [value])** : Asserts object has a property, optionally with a value.
  - **.ownProperty(name)** : Asserts object has an own property.
  - **.lengthOf(value)** : Asserts length of array or string.
  - **.match(regex)** : Asserts value matches a regular expression.
  - **.contain(value)** : Asserts array contains a value.
  - **.ok** : Asserts truthiness.
  - **.true** : Asserts strict equality to
    `true`
    .

  - **.false** : Asserts strict equality to
    `false`
    .

  - **.null** : Asserts strict equality to
    `null`
    .

  - **.undefined** : Asserts strict equality to
    `undefined`
    .

  - **.NaN** : Asserts value is
    `NaN`
    .

  - **.exist** : Asserts non-null and non-undefined.
  - **.empty** : Asserts empty array, string, or object.
  ### Assert
  The TDD ([Test-Driven Development](../T/test-driven-development.md)) style uses a more traditional assertion approach without chainable language.

  - **assert.equal(actual, expected)** : Asserts loose equality (
    `==`
    ).

  - **assert.strictEqual(actual, expected)** : Asserts strict equality (
    `===`
    ).

  - **assert.deepEqual(actual, expected)** : Asserts deep equality.
  - **assert.isAbove(valueToCheck, valueToBeAbove)** : Asserts number is greater than value.
  - **assert.isAtLeast(valueToCheck, valueToBeAtLeast)** : Asserts number is at least equal to value.
  - **assert.isBelow(valueToCheck, valueToBeBelow)** : Asserts number is less than value.
  - **assert.isAtMost(valueToCheck, valueToBeAtMost)** : Asserts number is at most equal to value.
  - **assert.instanceOf(object, constructor)** : Asserts instance of a constructor.
  - **assert.property(object, property)** : Asserts object has a property.
  - **assert.lengthOf(object, length)** : Asserts length of array or string.
  - **assert.match(value, regex)** : Asserts value matches a regular expression.
  - **assert.containsAllKeys(object, keys)** : Asserts object contains all provided keys.
  - **assert.ok(value)** : Asserts truthiness.
  - **assert.isTrue(value)** : Asserts strict equality to
    `true`
    .

  - **assert.isFalse(value)** : Asserts strict equality to
    `false`
    .

  - **assert.isNull(value)** : Asserts strict equality to
    `null`
    .

  - **assert.isUndefined(value)** : Asserts strict equality to
    `undefined`
    .

  - **assert.isNaN(value)** : Asserts value is
    `NaN`
    .

  - **assert.exists(value)** : Asserts non-null and non-undefined.
  - **assert.isEmpty(value)** : Asserts empty array, string, or object.
  Each assertion type serves a specific testing need, allowing for comprehensive and readable tests.

  - **.equal(value)** : Asserts strict equality (
    `===`
    ).

  - **.eql(value)** : Asserts deep equality.
  - **.above(value)** : Asserts number is greater than value.
  - **.least(value)** : Asserts number is at least equal to value.
  - **.below(value)** : Asserts number is less than value.
  - **.most(value)** : Asserts number is at most equal to value.
  - **.instanceOf(constructor)** : Asserts instance of a constructor.
  - **.property(name, [value])** : Asserts object has a property, optionally with a value.
  - **.ownProperty(name)** : Asserts object has an own property.
  - **.lengthOf(value)** : Asserts length of array or string.
  - **.match(regex)** : Asserts value matches a regular expression.
  - **.contain(value)** : Asserts array contains a value.
  - **.ok** : Asserts truthiness.
  - **.true** : Asserts strict equality to
    `true`
    .

  - **.false** : Asserts strict equality to
    `false`
    .

  - **.null** : Asserts strict equality to
    `null`
    .

  - **.undefined** : Asserts strict equality to
    `undefined`
    .

  - **.NaN** : Asserts value is
    `NaN`
    .

  - **.exist** : Asserts non-null and non-undefined.
  - **.empty** : Asserts empty array, string, or object.
  - **assert.equal(actual, expected)** : Asserts loose equality (
    `==`
    ).

  - **assert.strictEqual(actual, expected)** : Asserts strict equality (
    `===`
    ).

  - **assert.deepEqual(actual, expected)** : Asserts deep equality.
  - **assert.isAbove(valueToCheck, valueToBeAbove)** : Asserts number is greater than value.
  - **assert.isAtLeast(valueToCheck, valueToBeAtLeast)** : Asserts number is at least equal to value.
  - **assert.isBelow(valueToCheck, valueToBeBelow)** : Asserts number is less than value.
  - **assert.isAtMost(valueToCheck, valueToBeAtMost)** : Asserts number is at most equal to value.
  - **assert.instanceOf(object, constructor)** : Asserts instance of a constructor.
  - **assert.property(object, property)** : Asserts object has a property.
  - **assert.lengthOf(object, length)** : Asserts length of array or string.
  - **assert.match(value, regex)** : Asserts value matches a regular expression.
  - **assert.containsAllKeys(object, keys)** : Asserts object contains all provided keys.
  - **assert.ok(value)** : Asserts truthiness.
  - **assert.isTrue(value)** : Asserts strict equality to
    `true`
    .

  - **assert.isFalse(value)** : Asserts strict equality to
    `false`
    .

  - **assert.isNull(value)** : Asserts strict equality to
    `null`
    .

  - **assert.isUndefined(value)** : Asserts strict equality to
    `undefined`
    .

  - **assert.isNaN(value)** : Asserts value is
    `NaN`
    .

  - **assert.exists(value)** : Asserts non-null and non-undefined.
  - **assert.isEmpty(value)** : Asserts empty array, string, or object.

#### How do you assert that a function throws an error in Chai.js?

  To assert that a function throws an error in [Chai.js](../C/chai-js.md), you can use the `throw` or `throws` method from the `expect` or `should` interface. Here's how you can do it with both interfaces:
  **Using the `expect` interface:**

  ```
  const expect = require('chai').expect;
  expect(functionUnderTest).to.throw(ExpectedError);
  expect(functionUnderTest).to.throw("Error message");
  expect(functionUnderTest).to.throw(ExpectedError, "Error message");
  expect(functionUnderTest).to.throw(/Error message regex/);
  ```
  **Using the `should` interface:**

  ```
  const should = require('chai').should();
  functionUnderTest.should.throw(ExpectedError);
  functionUnderTest.should.throw("Error message");
  functionUnderTest.should.throw(ExpectedError, "Error message");
  functionUnderTest.should.throw(/Error message regex/);
  ```
  Replace `functionUnderTest` with the function you are testing, and `ExpectedError` with the error constructor you expect to be thrown. If you're checking for a specific error message, you can pass a string or a regular expression to match against the error message.
  **Example:**

  ```
  function willThrow() {
    throw new Error('This is an error!');
  }
  // Using expect
  expect(willThrow).to.throw(Error, 'This is an error!');
  // Using should
  willThrow.should.throw(Error, 'This is an error!');
  ```
  Ensure that the function is passed without invoking it directly; otherwise, the error will not be caught by Chai and the assertion will fail.

#### How do you assert deep equality in Chai.js?

  To assert deep equality in [Chai.js](../C/chai-js.md), use the `.deep` chain followed by the `.equal` or `.eql` assertion. This will perform a deep comparison between the target and the expected objects, considering all nested properties.
  Here's an example using the `expect` interface:

  ```
  const expect = require('chai').expect;
  const actual = { a: 1, b: { c: 3 } };
  const expected = { a: 1, b: { c: 3 } };
  expect(actual).to.deep.equal(expected);
  ```
  Alternatively, with the `should` interface:

  ```
  const should = require('chai').should();
  const actual = { a: 1, b: { c: 3 } };
  const expected = { a: 1, b: { c: 3 } };
  actual.should.deep.equal(expected);
  ```
  For arrays, `deep.equal` also works effectively:

  ```
  expect([1, 2, [3, 4]]).to.deep.equal([1, 2, [3, 4]]);
  ```
  Remember that without the `.deep` chain, the `equal` assertion checks for strict equality (using `===`), which is not suitable for comparing the contents of objects or arrays.

### Plugins

#### What are Chai.js plugins?

  [Chai.js](../C/chai-js.md) plugins extend the functionality of Chai's assertion library, allowing for more specialized or complex assertions tailored to specific testing needs. They integrate seamlessly with Chai's existing [API](../A/api.md), enriching it with additional methods and properties.
  To use a [Chai.js](../C/chai-js.md) plugin, you typically require it after Chai and then use the `use` method to add it to your Chai [setup](../S/setup.md):

  ```
  const chai = require('chai');
  const somePlugin = require('chai-some-plugin');
  chai.use(somePlugin);
  ```
  **Popular plugins** include:

  - `chai-http` : Enables HTTP assertions, making it easy to test web services.
  - `chai-as-promised` : Simplifies the process of working with promises in assertions.
  - `chai-dom` : Provides assertions for DOM elements, useful in browser or DOM-based testing.
  - `sinon-chai` : Offers assertions for Sinon.js spies, stubs, and mocks, integrating both libraries.
  Creating a **custom [Chai.js](../C/chai-js.md) plugin** involves defining a module that exports a function. This function should accept the Chai instance and should use Chai's [API](../A/api.md) to add new methods or properties:

  ```
  module.exports = function (chai, utils) {
    const Assertion = chai.Assertion;
    Assertion.addMethod('myAssertion', function (expected) {
      // Custom assertion logic here
    });
  };
  ```
  Plugins can be particularly useful for adapting Chai to work with new frameworks, libraries, or specific project requirements, making them a powerful tool in a [test automation](../T/test-automation.md) engineer's arsenal.

  - `chai-http` : Enables HTTP assertions, making it easy to test web services.
  - `chai-as-promised` : Simplifies the process of working with promises in assertions.
  - `chai-dom` : Provides assertions for DOM elements, useful in browser or DOM-based testing.
  - `sinon-chai` : Offers assertions for Sinon.js spies, stubs, and mocks, integrating both libraries.

#### How do you use a Chai.js plugin?

  To use a [Chai.js](../C/chai-js.md) plugin, follow these steps:

  1. **Install** the plugin via npm or yarn, for example:

    ```
    npm install chai-http
    ```

  2. **Import** the plugin in your test file:

    ```
    const chai = require('chai');
    const chaiHttp = require('chai-http');
    ```

  3. **Use** the `use` method on the `chai` object to add the plugin:

    ```
    chai.use(chaiHttp);
    ```

  4. After adding the plugin, you can **utilize its methods** in your tests. For instance, with `chai-http` you can make HTTP requests:

    ```
    chai.request('http://example.com')
        .get('/')
        .end((err, res) => {
            expect(res).to.have.status(200);
        });
    ```
  Remember to **read the plugin's documentation** for specific usage instructions, as each plugin may introduce unique methods or syntax.
  Here's a brief example using `chai-as-promised` for handling promises:

  1. **Install** the plugin:

    ```
    npm install chai-as-promised
    ```

  2. **Import** and **use** the plugin:

    ```
    const chai = require('chai');
    const chaiAsPromised = require('chai-as-promised');
    chai.use(chaiAsPromised);
    ```

  3. **Write assertions** for promises:

    ```
    const expect = chai.expect;
    const promise = returnsAPromise(); // some function that returns a promise
    // Now you can use Chai as Promised for assertions
    expect(promise).to.eventually.equal('expected value');
    ```
  By following these steps, you can extend Chai's functionality and tailor your testing suite to your project's needs.

  1. **Install** the plugin via npm or yarn, for example:

    ```
    npm install chai-http
    ```

  2. **Import** the plugin in your test file:

    ```
    const chai = require('chai');
    const chaiHttp = require('chai-http');
    ```

  3. **Use** the `use` method on the `chai` object to add the plugin:

    ```
    chai.use(chaiHttp);
    ```

  4. After adding the plugin, you can **utilize its methods** in your tests. For instance, with `chai-http` you can make HTTP requests:

    ```
    chai.request('http://example.com')
        .get('/')
        .end((err, res) => {
            expect(res).to.have.status(200);
        });
    ```

  1. **Install** the plugin:

    ```
    npm install chai-as-promised
    ```

  2. **Import** and **use** the plugin:

    ```
    const chai = require('chai');
    const chaiAsPromised = require('chai-as-promised');
    chai.use(chaiAsPromised);
    ```

  3. **Write assertions** for promises:

    ```
    const expect = chai.expect;
    const promise = returnsAPromise(); // some function that returns a promise
    // Now you can use Chai as Promised for assertions
    expect(promise).to.eventually.equal('expected value');
    ```

#### What are some popular Chai.js plugins and what do they do?

  [Chai.js](../C/chai-js.md) has a rich ecosystem of plugins that extend its core functionalities. Here are some popular ones:

  - **chai-as-promised** : Simplifies working with promises. It allows you to deal with assertions on asynchronous operations in a more expressive manner.

    ```
    expect(promise).to.eventually.equal('foo');
    ```

  - **chai-http** : Useful for HTTP integration testing. It allows you to send requests to an HTTP server and assert the response.

    ```
    chai.request(app).get('/').end((err, res) => {
      expect(res).to.have.status(200);
    });
    ```

  - **sinon-chai** : Provides a set of assertions for Sinon.js spies, stubs, and mocks, making it easier to work with test doubles.

    ```
    expect(spy).to.have.been.calledOnce;
    ```

  - **chai-dom** : Extends Chai with assertions for DOM manipulation, making it a good choice for browser-based testing.

    ```
    expect(element).to.have.text('hello');
    ```

  - **chai-enzyme** : Tailored for React.js testing with Enzyme. It adds enzyme-specific assertions for component properties, state, and rendering.

    ```
    expect(wrapper).to.have.className('foo');
    ```

  - **chai-jquery** : Integrates Chai with jQuery, providing assertions for jQuery objects such as CSS, attributes, and events.

    ```
    expect($el).to.have.css('display', 'none');
    ```

  - **chai-subset** : Allows you to assert if an object is part of another object, useful for testing API responses.

    ```
    expect(result).to.containSubset({ name: 'foo' });
    ```

  - **dirty-chai** : Provides a way to use Chai assertions as functions rather than properties, which can be helpful for linting purposes.

    ```
    expect(foo).to.be.a.function();
    ```
  Each plugin is designed to address specific testing needs and scenarios, enhancing the expressiveness and power of Chai assertions.

  - **chai-as-promised** : Simplifies working with promises. It allows you to deal with assertions on asynchronous operations in a more expressive manner.

    ```
    expect(promise).to.eventually.equal('foo');
    ```

  - **chai-http** : Useful for HTTP integration testing. It allows you to send requests to an HTTP server and assert the response.

    ```
    chai.request(app).get('/').end((err, res) => {
      expect(res).to.have.status(200);
    });
    ```

  - **sinon-chai** : Provides a set of assertions for Sinon.js spies, stubs, and mocks, making it easier to work with test doubles.

    ```
    expect(spy).to.have.been.calledOnce;
    ```

  - **chai-dom** : Extends Chai with assertions for DOM manipulation, making it a good choice for browser-based testing.

    ```
    expect(element).to.have.text('hello');
    ```

  - **chai-enzyme** : Tailored for React.js testing with Enzyme. It adds enzyme-specific assertions for component properties, state, and rendering.

    ```
    expect(wrapper).to.have.className('foo');
    ```

  - **chai-jquery** : Integrates Chai with jQuery, providing assertions for jQuery objects such as CSS, attributes, and events.

    ```
    expect($el).to.have.css('display', 'none');
    ```

  - **chai-subset** : Allows you to assert if an object is part of another object, useful for testing API responses.

    ```
    expect(result).to.containSubset({ name: 'foo' });
    ```

  - **dirty-chai** : Provides a way to use Chai assertions as functions rather than properties, which can be helpful for linting purposes.

    ```
    expect(foo).to.be.a.function();
    ```

#### How do you create your own Chai.js plugin?

  Creating your own [Chai.js](../C/chai-js.md) plugin involves extending Chai with new assertions or behaviors. Follow these steps:

  1. **Initialize a new project** for your plugin with `npm init` and install Chai as a peer dependency.
  2. **Create a main file** for your plugin, e.g., `chai-myplugin.js`.
  3. **Define your plugin** by exporting a function that Chai will use to install the plugin:

  ```
  module.exports = function(chai, utils) {
    // Plugin code goes here
  };
  ```

  1. **Add methods or properties**
    to Chai's
    `Assertion`
    object. Use
    `utils.addMethod`
    for new assertion methods or
    `utils.addProperty`
    for new properties:

  ```
  utils.addMethod(chai.Assertion.prototype, 'myAssertion', function (expected) {
    var actual = this._obj;
    // Assertion logic here
    this.assert(
      actual === expected,
      'expected #{this} to be #{exp}',
      'expected #{this} not to be #{exp}',
      expected,
      actual
    );
  });
  ```

  1. **Test your plugin** thoroughly. Create [test cases](../T/test-case.md) using Mocha or another testing framework to ensure your assertions work as expected.
  2. **Document your plugin**. Clearly explain how to install and use your plugin, including examples of the assertions.
  3. **Publish your plugin** to npm to make it available for others. Update the `package.json` file with details about your plugin before publishing.
  To use your plugin, users will need to install it via npm and use `chai.use()` in their test files:

  ```
  var chai = require('chai');
  var myPlugin = require('chai-myplugin');
  chai.use(myPlugin);
  // Now they can use your plugin's assertions
  ```
  Remember to follow best practices for naming your plugin, usually starting with `chai-`, and maintain your plugin with updates and support as needed.

  1. **Initialize a new project** for your plugin with `npm init` and install Chai as a peer dependency.
  2. **Create a main file** for your plugin, e.g., `chai-myplugin.js`.
  3. **Define your plugin** by exporting a function that Chai will use to install the plugin:
  1. **Add methods or properties**
    to Chai's
    `Assertion`
    object. Use
    `utils.addMethod`
    for new assertion methods or
    `utils.addProperty`
    for new properties:

  1. **Test your plugin** thoroughly. Create [test cases](../T/test-case.md) using Mocha or another testing framework to ensure your assertions work as expected.
  2. **Document your plugin**. Clearly explain how to install and use your plugin, including examples of the assertions.
  3. **Publish your plugin** to npm to make it available for others. Update the `package.json` file with details about your plugin before publishing.

### Advanced Concepts

#### How do you use Chai.js with asynchronous code?

  Using [Chai.js](../C/chai-js.md) with asynchronous code typically involves working with promises or async/await syntax. Chai provides the `chai-as-promised` plugin to handle assertions on promises seamlessly.
  First, ensure `chai-as-promised` is installed and added to your Chai [setup](../S/setup.md):

  ```
  const chai = require('chai');
  const chaiAsPromised = require('chai-as-promised');
  chai.use(chaiAsPromised);
  const expect = chai.expect;
  ```
  When dealing with promises, you can return the promise with the assertion to the [test runner](../T/test-runner.md), which will wait for the promise to resolve or reject:

  ```
  it('should eventually have a value of 42', function() {
    return expect(Promise.resolve(42)).to.eventually.equal(42);
  });
  ```
  For async/await, use `async` in your test function and await the promise. Apply assertions to the resolved value:

  ```
  it('should have a value of 42', async function() {
    const value = await Promise.resolve(42);
    expect(value).to.equal(42);
  });
  ```
  To handle rejected promises, use the `.rejected` property and chain any additional assertions:

  ```
  it('should be rejected with an error', function() {
    return expect(Promise.reject(new Error('fail'))).to.be.rejected;
  });
  it('should be rejected with an error message', function() {
    return expect(Promise.reject(new Error('fail'))).to.be.rejectedWith('fail');
  });
  ```
  Remember to handle both resolved and rejected cases in your tests to ensure comprehensive coverage of asynchronous operations.

#### How do you use Chai.js with Promises?

  Using **[Chai.js](../C/chai-js.md)** with promises involves leveraging the **chai-as-promised** plugin, which extends Chai for fluent promise assertions. First, ensure **chai-as-promised** is installed and then integrate it with Chai:

  ```
  const chai = require('chai');
  const chaiAsPromised = require('chai-as-promised');
  chai.use(chaiAsPromised);
  const expect = chai.expect;
  ```
  With **chai-as-promised**, you can handle promise assertions in a more readable way. Here's an example of testing a function that returns a promise:

  ```
  const asyncFunction = () => {
    return new Promise((resolve, reject) => {
      // Asynchronous operation
    });
  };
  // Assertion for a resolved promise
  expect(asyncFunction()).to.eventually.equal('expected value');
  // Assertion for a rejected promise
  expect(asyncFunction()).to.be.rejectedWith(Error);
  // Assertion for a promise that resolves before a timeout
  expect(asyncFunction()).to.eventually.equal('expected value').and.notify(done);
  ```
  Remember to return the promise from your [test case](../T/test-case.md) or use the `done` callback to ensure the test waits for the promise resolution:

  ```
  it('should resolve to the expected value', function() {
    return expect(asyncFunction()).to.eventually.equal('expected value');
  });
  // Using done callback
  it('should resolve to the expected value', function(done) {
    expect(asyncFunction()).to.eventually.equal('expected value').notify(done);
  });
  ```
  **chai-as-promised** supports chaining of additional assertions after `eventually` and integrates seamlessly with both **mocha** and other [test runners](../T/test-runner.md) that handle returned promises.

#### What is Chai.js's .should interface and how does it work?

  [Chai.js](../C/chai-js.md)'s `.should` interface is a [BDD](../B/bdd.md) (Behavior-Driven Development) style assertion that extends each object with a `should` property to start a chain of assertions. This interface allows for more readable and expressive tests.
  To use the `.should` interface, you first need to execute `chai.should()` to perform the necessary modifications to `Object.prototype`. Here's an example:

  ```
  const chai = require('chai');
  const should = chai.should();
  const number = 2;
  number.should.be.a('number');
  number.should.equal(2);
  ```
  The `.should` interface works by adding a getter to `Object.prototype` that returns a `Should` assertion object. This object can then be used to chain further assertions to the value being tested. It's important to note that using `.should` modifies the `Object.prototype`, which might lead to unexpected behavior if your application relies on enumerating properties of objects.
  Assertions with `.should` throw `AssertionError` when they fail, which can then be caught by the [test runner](../T/test-runner.md) to report the failure. The `.should` interface supports all the same assertions as Chai's `expect` and `assert` interfaces, providing a rich set of assertions like `.equal`, `.deep.equal`, `.have.property`, and many others.
  When using `.should`, you can also take advantage of Chai's chainable language to enhance the readability of your tests:

  ```
  'hello'.should.be.a('string').and.have.lengthOf(5);
  ```
  Remember to handle properties that may not exist on the object being tested, as trying to access a `should` property on `null` or `undefined` will throw an error.

#### How do you customize Chai.js's assertion error messages?

  Customizing [Chai.js](../C/chai-js.md) assertion error messages can enhance the readability and clarity of test results. To customize an error message, use the `.message` chainable method provided by Chai. This method allows you to specify a custom message that will be displayed if the assertion fails.
  Here's an example using the `expect` interface:

  ```
  const expect = require('chai').expect;
  expect(myFunction, 'custom error message if myFunction does not meet expectations').to.be.a('function');
  ```
  For the `should` interface, you can pass the custom message as the second argument to the assertion method:

  ```
  should = require('chai').should();
  myVariable.should.equal('expected value', 'custom error message if myVariable is not equal to expected value');
  ```
  And for the `assert` interface, the custom message is typically the last argument in the assertion function:

  ```
  const assert = require('chai').assert;
  assert.typeOf(myFunction, 'function', 'custom error message if myFunction is not a function');
  ```
  **Note:** Custom messages should be concise yet descriptive enough to understand the context of the failure without having to delve into the test code.
