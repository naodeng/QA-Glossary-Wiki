# Jest
[Jest](#jest)[Jest](/wiki/jest)[unit testing](/wiki/unit-testing)
### Related Terms:
- Testing framework
- Jasmine
- Chai.js
[Testing framework](/glossary/testing-framework)[Jasmine](/glossary/jasmine)[Chai.js](/glossary/chaijs)
### See also:
- Wikipedia
[Wikipedia](https://jestjs.io/)
## Questions aboutJest?

#### Basics and Importance
- What is Jest and what is it used for?Jestis aJavaScript testing frameworkdesigned to ensure correctness of any JavaScript codebase. It allows developers to write tests with anAPIthat encourages good testing practices and is commonly used for both front-end and back-end JavaScript applications.WithJest, you can performunit teststo validate individual functions or modules,integration teststo ensure different parts of the application work together as expected, andend-to-end testsfor testing the flow of an application.Jestintegrates well with projects usingBabel,TypeScript,Node.js,React,Angular, andVue, making it a versatile choice for a wide range of JavaScript projects. It also supportstest parallelization, where tests are run simultaneously in separate processes to maximize performance and speed.To integrateJestinto a project, you typically install it via npm or yarn, and then create a configuration file if needed, although many projects can useJestwith little to no configuration due to its convention over configuration design.Here's a basic example of how aJesttest looks:test('adds 1 + 2 to equal 3', () => {
  expect(1 + 2).toBe(3);
});Jest's assertion library provides a range of matchers that let you validate different things, from simple equality checks to more complex conditions. Itsinteractive watch modeallows you to automatically re-run tests related to changed files, and itsbuilt-in coverage reportshelp you understand which parts of your codebase may not be covered by tests.
- Why is Jest popular for testing JavaScript code?Jestis popular for testing JavaScript code due to itssimplicityandease of use. It integrates well with projects usingReact,Angular,Vue, andNode.js, making it a versatile choice for a wide range of JavaScript applications. Itswatch modeautomatically runs tests related to changed files, enhancing developer productivity.Developers appreciateJest'sintegrated coverage reports, which are generated without additionalsetup, providing immediate insight intotest coverage. The framework'spowerful mocking librarysimplifies the testing of code with complex dependencies.Jest'sparalleltest executionoptimizes performance by running tests concurrently, reducing the time required to run extensivetest suites. Itsconsistent environmentacross test runs, thanks to a custom resolver and the use of JSDom for DOMAPIemulation, ensures test reliability.The community aroundJestis active, contributing to a rich ecosystem ofpluginsandextensionsthat enhance its functionality. Regular updates and improvements by the maintainers keepJestat the forefront of testing technologies.test('adds 1 + 2 to equal 3', () => {
  expect(sum(1, 2)).toBe(3);
});The above example demonstratesJest's straightforward syntax, making tests readable and maintainable.Jest's popularity is a testament to its ability to balanceflexibility,features, anddeveloper experience, making it a go-to choice for JavaScript testing.
- How does Jest compare to other testing frameworks?Jeststands out for itssimplicityandintegrated featureswhen compared to other testing frameworks like Mocha,Jasmine, or AVA. Unlike Mocha, which requires additional plugins for functionalities like mocking, coverage, and snapshot testing,Jestcomes with these features out-of-the-box. This reduces the need for configuring multiple libraries, makingJesta morestreamlined choice.Jestruns tests in parallel, which can lead tofaster execution timescompared to some other frameworks. Itswatch modeis also highly optimized for developer experience, allowing for tests related to changed files to be run automatically.In contrast toJasmine, which has a similar syntax,Jestprovides a moremodern and powerful mocking library. This makes it easier to test JavaScript applications, especially those built with React, whereJestis often the recommended choice due to itsnative support for React testing utilities.While AVA emphasizesconcurrencyin test runs,Jestbalances paralleltest executionwith ashared contextthat can be beneficial for certain types oftest suites. Additionally,Jest'ssnapshot testingcapability is more advanced than similar features in other frameworks, offering a straightforward way to test the output of components.Forasynchronous testing,Jestsupports async/await, promises, and callbacks, similar to other frameworks, but with a moreunified syntaxand better error handling.Overall,Jestis often preferred for itsdeveloper-friendly approach, comprehensive documentation, andtight integrationwith the JavaScript ecosystem, particularly in projects created withcreate-react-appor using Babel and TypeScript.
- What are the key features of Jest?Key features ofJestinclude:Snapshot Testing:Jestcan capture "snapshots" of React trees or other serializable values to simplifyUI testingand ensure the UI does not change unexpectedly.Interactive Watch Mode:Jestcan run in a watch mode that automatically reruns tests when it detects changes in the codebase, enhancing developer productivity.Built-in Coverage Reports:Jestincludes an integratedcode coveragereporter that can be activated with a simple command line flag (--coverage).Isolated and ParallelTest Execution: Tests are run in parallel in separate processes to maximize performance and ensure tests do not affect each other.GlobalSetup/Teardown:Jestprovides hooks for setting up and tearing down the environment before and after all tests have run.Manual Mocks: Developers can create manual mocks to stub out functionality with mock implementations.Timer Mocks:Jestcan mock timers in your tests, allowing you to control the passage of time.Custom Matchers: ExtendJest's matcher library with custom matchers for more descriptive test statements.Seamless TypeScript Integration:Jestsupports TypeScript, allowing for type-safe testing without additional configuration.Rich Assertion Library:Jestcomes with a vast array of matchers that enable a variety of assertions for differentuse cases.Extensibility:Jestcan be extended with custom reporters, custom matchers, and customtest runnersto fit the needs of any project.Easy Mocking of ES Modules:Jestallows for easy mocking of ES6 modules, which can be particularly useful when dealing with external dependencies.
- Why is Jest considered a 'zero-configuration' testing platform?Jestis considered azero-configurationtesting platform because it aims to work out of the box, with minimalsetuprequired. Upon installation,Jestprovides sensible defaults for most projects, allowing developers to start writing and running tests immediately.The framework is designed with conventions that enable it to automatically find and execute tests. By default,Jestlooks for test files with any of the following popular naming conventions:Files with.jssuffix in__tests__folders.Files with.test.jssuffix.Files with.spec.jssuffix.Jestalso comes with a built-in assertion library andtest runner, which means there's no need to install or configure additional modules to start testing. It handles the transformation of modern JavaScript features throughBabelintegration, and it can mock dependencies and timers out of the box.For many applications, the default configuration is sufficient to begin testing. However, if customization is needed,Jestprovides an easy-to-use configuration file (jest.config.js) where developers can override defaults and tailor the testing environment to their specific needs.Here's an example of how simple it is to start withJest:npm install --save-dev jestThen, in asum.test.jsfile:const sum = require('./sum');

test('adds 1 + 2 to equal 3', () => {
  expect(sum(1, 2)).toBe(3);
});Run the tests with:npx jestThis ease ofsetupand sensible defaults are what makeJestazero-configurationtesting platform for many developers.

Jestis aJavaScript testing frameworkdesigned to ensure correctness of any JavaScript codebase. It allows developers to write tests with anAPIthat encourages good testing practices and is commonly used for both front-end and back-end JavaScript applications.
[Jest](/wiki/jest)**JavaScript testing framework**[API](/wiki/api)
WithJest, you can performunit teststo validate individual functions or modules,integration teststo ensure different parts of the application work together as expected, andend-to-end testsfor testing the flow of an application.
[Jest](/wiki/jest)**unit tests****integration tests****end-to-end tests**
Jestintegrates well with projects usingBabel,TypeScript,Node.js,React,Angular, andVue, making it a versatile choice for a wide range of JavaScript projects. It also supportstest parallelization, where tests are run simultaneously in separate processes to maximize performance and speed.
[Jest](/wiki/jest)**Babel****TypeScript****Node.js**[Node.js](/wiki/node-js)**React****Angular****Vue****test parallelization**
To integrateJestinto a project, you typically install it via npm or yarn, and then create a configuration file if needed, although many projects can useJestwith little to no configuration due to its convention over configuration design.
[Jest](/wiki/jest)[Jest](/wiki/jest)
Here's a basic example of how aJesttest looks:
[Jest](/wiki/jest)
```
test('adds 1 + 2 to equal 3', () => {
  expect(1 + 2).toBe(3);
});
```
`test('adds 1 + 2 to equal 3', () => {
  expect(1 + 2).toBe(3);
});`
Jest's assertion library provides a range of matchers that let you validate different things, from simple equality checks to more complex conditions. Itsinteractive watch modeallows you to automatically re-run tests related to changed files, and itsbuilt-in coverage reportshelp you understand which parts of your codebase may not be covered by tests.
[Jest](/wiki/jest)**interactive watch mode****built-in coverage reports**
Jestis popular for testing JavaScript code due to itssimplicityandease of use. It integrates well with projects usingReact,Angular,Vue, andNode.js, making it a versatile choice for a wide range of JavaScript applications. Itswatch modeautomatically runs tests related to changed files, enhancing developer productivity.
[Jest](/wiki/jest)**simplicity****ease of use****React****Angular****Vue****Node.js**[Node.js](/wiki/node-js)**watch mode**
Developers appreciateJest'sintegrated coverage reports, which are generated without additionalsetup, providing immediate insight intotest coverage. The framework'spowerful mocking librarysimplifies the testing of code with complex dependencies.
[Jest](/wiki/jest)**integrated coverage reports**[setup](/wiki/setup)[test coverage](/wiki/test-coverage)**powerful mocking library**
Jest'sparalleltest executionoptimizes performance by running tests concurrently, reducing the time required to run extensivetest suites. Itsconsistent environmentacross test runs, thanks to a custom resolver and the use of JSDom for DOMAPIemulation, ensures test reliability.
[Jest](/wiki/jest)**paralleltest execution**[test execution](/wiki/test-execution)[test suites](/wiki/test-suite)**consistent environment**[API](/wiki/api)
The community aroundJestis active, contributing to a rich ecosystem ofpluginsandextensionsthat enhance its functionality. Regular updates and improvements by the maintainers keepJestat the forefront of testing technologies.
[Jest](/wiki/jest)**plugins****extensions**[Jest](/wiki/jest)
```
test('adds 1 + 2 to equal 3', () => {
  expect(sum(1, 2)).toBe(3);
});
```
`test('adds 1 + 2 to equal 3', () => {
  expect(sum(1, 2)).toBe(3);
});`
The above example demonstratesJest's straightforward syntax, making tests readable and maintainable.Jest's popularity is a testament to its ability to balanceflexibility,features, anddeveloper experience, making it a go-to choice for JavaScript testing.
[Jest](/wiki/jest)[Jest](/wiki/jest)**flexibility****features****developer experience**
Jeststands out for itssimplicityandintegrated featureswhen compared to other testing frameworks like Mocha,Jasmine, or AVA. Unlike Mocha, which requires additional plugins for functionalities like mocking, coverage, and snapshot testing,Jestcomes with these features out-of-the-box. This reduces the need for configuring multiple libraries, makingJesta morestreamlined choice.
[Jest](/wiki/jest)**simplicity****integrated features**[Jasmine](/wiki/jasmine)[Jest](/wiki/jest)[Jest](/wiki/jest)**streamlined choice**
Jestruns tests in parallel, which can lead tofaster execution timescompared to some other frameworks. Itswatch modeis also highly optimized for developer experience, allowing for tests related to changed files to be run automatically.
[Jest](/wiki/jest)**faster execution times****watch mode**
In contrast toJasmine, which has a similar syntax,Jestprovides a moremodern and powerful mocking library. This makes it easier to test JavaScript applications, especially those built with React, whereJestis often the recommended choice due to itsnative support for React testing utilities.
[Jasmine](/wiki/jasmine)[Jest](/wiki/jest)**modern and powerful mocking library**[Jest](/wiki/jest)**native support for React testing utilities**
While AVA emphasizesconcurrencyin test runs,Jestbalances paralleltest executionwith ashared contextthat can be beneficial for certain types oftest suites. Additionally,Jest'ssnapshot testingcapability is more advanced than similar features in other frameworks, offering a straightforward way to test the output of components.
**concurrency**[Jest](/wiki/jest)[test execution](/wiki/test-execution)**shared context**[test suites](/wiki/test-suite)[Jest](/wiki/jest)**snapshot testing**
Forasynchronous testing,Jestsupports async/await, promises, and callbacks, similar to other frameworks, but with a moreunified syntaxand better error handling.
**asynchronous testing**[Jest](/wiki/jest)**unified syntax**
Overall,Jestis often preferred for itsdeveloper-friendly approach, comprehensive documentation, andtight integrationwith the JavaScript ecosystem, particularly in projects created withcreate-react-appor using Babel and TypeScript.
[Jest](/wiki/jest)**developer-friendly approach****tight integration**`create-react-app`
Key features ofJestinclude:
[Jest](/wiki/jest)- Snapshot Testing:Jestcan capture "snapshots" of React trees or other serializable values to simplifyUI testingand ensure the UI does not change unexpectedly.
- Interactive Watch Mode:Jestcan run in a watch mode that automatically reruns tests when it detects changes in the codebase, enhancing developer productivity.
- Built-in Coverage Reports:Jestincludes an integratedcode coveragereporter that can be activated with a simple command line flag (--coverage).
- Isolated and ParallelTest Execution: Tests are run in parallel in separate processes to maximize performance and ensure tests do not affect each other.
- GlobalSetup/Teardown:Jestprovides hooks for setting up and tearing down the environment before and after all tests have run.
- Manual Mocks: Developers can create manual mocks to stub out functionality with mock implementations.
- Timer Mocks:Jestcan mock timers in your tests, allowing you to control the passage of time.
- Custom Matchers: ExtendJest's matcher library with custom matchers for more descriptive test statements.
- Seamless TypeScript Integration:Jestsupports TypeScript, allowing for type-safe testing without additional configuration.
- Rich Assertion Library:Jestcomes with a vast array of matchers that enable a variety of assertions for differentuse cases.
- Extensibility:Jestcan be extended with custom reporters, custom matchers, and customtest runnersto fit the needs of any project.
- Easy Mocking of ES Modules:Jestallows for easy mocking of ES6 modules, which can be particularly useful when dealing with external dependencies.

Snapshot Testing:Jestcan capture "snapshots" of React trees or other serializable values to simplifyUI testingand ensure the UI does not change unexpectedly.
**Snapshot Testing**[Jest](/wiki/jest)[UI testing](/wiki/ui-testing)
Interactive Watch Mode:Jestcan run in a watch mode that automatically reruns tests when it detects changes in the codebase, enhancing developer productivity.
**Interactive Watch Mode**[Jest](/wiki/jest)
Built-in Coverage Reports:Jestincludes an integratedcode coveragereporter that can be activated with a simple command line flag (--coverage).
**Built-in Coverage Reports**[Jest](/wiki/jest)[code coverage](/wiki/code-coverage)`--coverage`
Isolated and ParallelTest Execution: Tests are run in parallel in separate processes to maximize performance and ensure tests do not affect each other.
**Isolated and ParallelTest Execution**[Test Execution](/wiki/test-execution)
GlobalSetup/Teardown:Jestprovides hooks for setting up and tearing down the environment before and after all tests have run.
**GlobalSetup/Teardown**[Setup](/wiki/setup)[Jest](/wiki/jest)
Manual Mocks: Developers can create manual mocks to stub out functionality with mock implementations.
**Manual Mocks**
Timer Mocks:Jestcan mock timers in your tests, allowing you to control the passage of time.
**Timer Mocks**[Jest](/wiki/jest)
Custom Matchers: ExtendJest's matcher library with custom matchers for more descriptive test statements.
**Custom Matchers**[Jest](/wiki/jest)
Seamless TypeScript Integration:Jestsupports TypeScript, allowing for type-safe testing without additional configuration.
**Seamless TypeScript Integration**[Jest](/wiki/jest)
Rich Assertion Library:Jestcomes with a vast array of matchers that enable a variety of assertions for differentuse cases.
**Rich Assertion Library**[Jest](/wiki/jest)[use cases](/wiki/use-case)
Extensibility:Jestcan be extended with custom reporters, custom matchers, and customtest runnersto fit the needs of any project.
**Extensibility**[Jest](/wiki/jest)[test runners](/wiki/test-runner)
Easy Mocking of ES Modules:Jestallows for easy mocking of ES6 modules, which can be particularly useful when dealing with external dependencies.
**Easy Mocking of ES Modules**[Jest](/wiki/jest)
Jestis considered azero-configurationtesting platform because it aims to work out of the box, with minimalsetuprequired. Upon installation,Jestprovides sensible defaults for most projects, allowing developers to start writing and running tests immediately.
[Jest](/wiki/jest)**zero-configuration**[setup](/wiki/setup)[Jest](/wiki/jest)
The framework is designed with conventions that enable it to automatically find and execute tests. By default,Jestlooks for test files with any of the following popular naming conventions:
[Jest](/wiki/jest)- Files with.jssuffix in__tests__folders.
- Files with.test.jssuffix.
- Files with.spec.jssuffix.
`.js``__tests__``.test.js``.spec.js`
Jestalso comes with a built-in assertion library andtest runner, which means there's no need to install or configure additional modules to start testing. It handles the transformation of modern JavaScript features throughBabelintegration, and it can mock dependencies and timers out of the box.
[Jest](/wiki/jest)[test runner](/wiki/test-runner)**Babel**
For many applications, the default configuration is sufficient to begin testing. However, if customization is needed,Jestprovides an easy-to-use configuration file (jest.config.js) where developers can override defaults and tailor the testing environment to their specific needs.
[Jest](/wiki/jest)`jest.config.js`
Here's an example of how simple it is to start withJest:
[Jest](/wiki/jest)
```
npm install --save-dev jest
```
`npm install --save-dev jest`
Then, in asum.test.jsfile:
`sum.test.js`
```
const sum = require('./sum');

test('adds 1 + 2 to equal 3', () => {
  expect(sum(1, 2)).toBe(3);
});
```
`const sum = require('./sum');

test('adds 1 + 2 to equal 3', () => {
  expect(sum(1, 2)).toBe(3);
});`
Run the tests with:

```
npx jest
```
`npx jest`
This ease ofsetupand sensible defaults are what makeJestazero-configurationtesting platform for many developers.
[setup](/wiki/setup)[Jest](/wiki/jest)**zero-configuration**
#### Installation and Setup
- How do you install Jest?To installJest, you need to haveNode.jsandnpm(Node Package Manager) installed on your system. If you're usingyarn, you can use that as well. Here's how you can installJest:For npm users:npm install --save-dev jestFor yarn users:yarn add --dev jestThis command will addJestas a development dependency in your project'spackage.jsonfile. After installation, you can add a script to yourpackage.jsonto easily runJest:"scripts": {
  "test": "jest"
}Now, you can run your tests using the following command:For npm users:npm testFor yarn users:yarn testEnsure that your test files are named using the.test.jsor.spec.jssuffix, or are placed in a__tests__folder, soJestcan automatically find and execute them.If you're usingTypeScript, you'll also need to installts-jestand@types/jestto handle TypeScript compilation and type definitions:npm install --save-dev ts-jest @types/jestOr with yarn:yarn add --dev ts-jest @types/jestYou'll then need to configureJestto usets-jestby adding the following to yourJestconfiguration:"jest": {
  "preset": "ts-jest",
  "testMatch": ["**/*.test.ts"]
}This will directJestto process.tsfiles withts-jest.
- What are the prerequisites for using Jest?To useJesteffectively, certain prerequisites should be met:Node.js: Jest is a Node-based tool, so a current version of Node.js must be installed on your system.npm or Yarn: Package managers to install Jest and manage its dependencies.JavaScript Knowledge: Familiarity with JavaScript (or TypeScript) is essential since Jest is designed for testing JS codebases.ProjectSetup: A JavaScript project with a package.json file to configure and include Jest as a dependency.Understanding of Testing Concepts: Knowledge of unit testing, mocking, and assertions to write meaningful tests.ES Module Support: If using ES Modules, ensure compatibility or configure Babel for transpilation.Version Control: (Optional) A version control system like Git to track changes in tests alongside code.InstallJestusing npm or Yarn:npm install --save-dev jestoryarn add --dev jestEnsure yourpackage.jsonincludes atest script:"scripts": {
  "test": "jest"
}For TypeScript projects, installts-jestand@types/jestto handle type-checking and provide autocompletion:npm install --save-dev ts-jest @types/jestoryarn add --dev ts-jest @types/jestFinally, familiarity withJest'sAPIand lifecycle methods will help in structuring tests effectively.
- How do you set up a basic Jest testing environment?To set up a basicJesttesting environment, follow these steps:Initialize your project(if not already done) withnpm initoryarn init.InstallJestusing npm or Yarn:npm install --save-dev jestoryarn add --dev jestIn yourpackage.json, add the following script to runJest:"scripts": {
  "test": "jest"
}ConfigureJestif needed. For most projects,Jestworks out of the box with zero configuration. However, if you need to customizeJest's behavior, create ajest.config.jsfile or add ajestkey in yourpackage.json.Write your tests. Create files with.test.jsor.spec.jssuffixes, or put them in a__tests__folder.Jestwill automatically find these files.Usetestoritto define yourtest cases:test('adds 1 + 2 to equal 3', () => {
  expect(1 + 2).toBe(3);
});Run your testsby executing thetest script:npm testoryarn testJestwill execute the tests and provide a summary of the results. Adjust your tests and code based on the feedback from the test runs.
- How do you configure Jest for a project?To configureJestfor a project, create ajest.config.jsfile at the root of your project or define ajestkey in yourpackage.json. Here's a basic example of what ajest.config.jsfile might look like:module.exports = {
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
};verbose: Enables verbose output for test results.testEnvironment: Sets the environment in which tests are run.setupFilesAfterEnv: Lists scripts to run after the test framework is installed in the environment.transform: Specifies how to process files using a transformer.testMatch: Determines which files are considered test files.moduleNameMapper: Maps module paths for easier imports.coverageThreshold: Sets the minimum coverage thresholds for the project.For TypeScript projects, you'll need to installts-jestand configure thetransformproperty to use it.To include the configuration in yourpackage.json, it would look like this:"jest": {
  "verbose": true,
  // ... other configurations
}Remember to install any additionalJestplugins or presets you need for your project. Adjust the configuration options to match the specific needs of your project, such as custom global variables, module path aliases, or different environments for testing.

To installJest, you need to haveNode.jsandnpm(Node Package Manager) installed on your system. If you're usingyarn, you can use that as well. Here's how you can installJest:
[Jest](/wiki/jest)**Node.js**[Node.js](/wiki/node-js)**npm****yarn**[Jest](/wiki/jest)
For npm users:

```
npm install --save-dev jest
```
`npm install --save-dev jest`
For yarn users:

```
yarn add --dev jest
```
`yarn add --dev jest`
This command will addJestas a development dependency in your project'spackage.jsonfile. After installation, you can add a script to yourpackage.jsonto easily runJest:
[Jest](/wiki/jest)`package.json``package.json`[Jest](/wiki/jest)
```
"scripts": {
  "test": "jest"
}
```
`"scripts": {
  "test": "jest"
}`
Now, you can run your tests using the following command:

For npm users:

```
npm test
```
`npm test`
For yarn users:

```
yarn test
```
`yarn test`
Ensure that your test files are named using the.test.jsor.spec.jssuffix, or are placed in a__tests__folder, soJestcan automatically find and execute them.
`.test.js``.spec.js``__tests__`[Jest](/wiki/jest)
If you're usingTypeScript, you'll also need to installts-jestand@types/jestto handle TypeScript compilation and type definitions:
**TypeScript**`ts-jest``@types/jest`
```
npm install --save-dev ts-jest @types/jest
```
`npm install --save-dev ts-jest @types/jest`
Or with yarn:

```
yarn add --dev ts-jest @types/jest
```
`yarn add --dev ts-jest @types/jest`
You'll then need to configureJestto usets-jestby adding the following to yourJestconfiguration:
[Jest](/wiki/jest)`ts-jest`[Jest](/wiki/jest)
```
"jest": {
  "preset": "ts-jest",
  "testMatch": ["**/*.test.ts"]
}
```
`"jest": {
  "preset": "ts-jest",
  "testMatch": ["**/*.test.ts"]
}`
This will directJestto process.tsfiles withts-jest.
[Jest](/wiki/jest)`.ts``ts-jest`
To useJesteffectively, certain prerequisites should be met:
[Jest](/wiki/jest)- Node.js: Jest is a Node-based tool, so a current version of Node.js must be installed on your system.
- npm or Yarn: Package managers to install Jest and manage its dependencies.
- JavaScript Knowledge: Familiarity with JavaScript (or TypeScript) is essential since Jest is designed for testing JS codebases.
- ProjectSetup: A JavaScript project with a package.json file to configure and include Jest as a dependency.
- Understanding of Testing Concepts: Knowledge of unit testing, mocking, and assertions to write meaningful tests.
- ES Module Support: If using ES Modules, ensure compatibility or configure Babel for transpilation.
- Version Control: (Optional) A version control system like Git to track changes in tests alongside code.
**Node.js**[Node.js](/wiki/node-js)**npm or Yarn****JavaScript Knowledge****ProjectSetup**[Setup](/wiki/setup)**Understanding of Testing Concepts****ES Module Support****Version Control**
InstallJestusing npm or Yarn:
[Jest](/wiki/jest)
```
npm install --save-dev jest
```
`npm install --save-dev jest`
or

```
yarn add --dev jest
```
`yarn add --dev jest`
Ensure yourpackage.jsonincludes atest script:
`package.json`[test script](/wiki/test-script)
```
"scripts": {
  "test": "jest"
}
```
`"scripts": {
  "test": "jest"
}`
For TypeScript projects, installts-jestand@types/jestto handle type-checking and provide autocompletion:
`ts-jest``@types/jest`
```
npm install --save-dev ts-jest @types/jest
```
`npm install --save-dev ts-jest @types/jest`
or

```
yarn add --dev ts-jest @types/jest
```
`yarn add --dev ts-jest @types/jest`
Finally, familiarity withJest'sAPIand lifecycle methods will help in structuring tests effectively.
[Jest](/wiki/jest)[API](/wiki/api)
To set up a basicJesttesting environment, follow these steps:
[Jest](/wiki/jest)1. Initialize your project(if not already done) withnpm initoryarn init.
2. InstallJestusing npm or Yarn:npm install --save-dev jestoryarn add --dev jest
3. In yourpackage.json, add the following script to runJest:"scripts": {
  "test": "jest"
}
4. ConfigureJestif needed. For most projects,Jestworks out of the box with zero configuration. However, if you need to customizeJest's behavior, create ajest.config.jsfile or add ajestkey in yourpackage.json.
5. Write your tests. Create files with.test.jsor.spec.jssuffixes, or put them in a__tests__folder.Jestwill automatically find these files.
6. Usetestoritto define yourtest cases:test('adds 1 + 2 to equal 3', () => {
  expect(1 + 2).toBe(3);
});
7. Run your testsby executing thetest script:npm testoryarn test

Initialize your project(if not already done) withnpm initoryarn init.
**Initialize your project**`npm init``yarn init`
InstallJestusing npm or Yarn:
**InstallJest**[Jest](/wiki/jest)
```
npm install --save-dev jest
```
`npm install --save-dev jest`
or

```
yarn add --dev jest
```
`yarn add --dev jest`
In yourpackage.json, add the following script to runJest:
`package.json`[Jest](/wiki/jest)
```
"scripts": {
  "test": "jest"
}
```
`"scripts": {
  "test": "jest"
}`
ConfigureJestif needed. For most projects,Jestworks out of the box with zero configuration. However, if you need to customizeJest's behavior, create ajest.config.jsfile or add ajestkey in yourpackage.json.
**ConfigureJest**[Jest](/wiki/jest)[Jest](/wiki/jest)[Jest](/wiki/jest)`jest.config.js``jest``package.json`
Write your tests. Create files with.test.jsor.spec.jssuffixes, or put them in a__tests__folder.Jestwill automatically find these files.
**Write your tests**`.test.js``.spec.js``__tests__`[Jest](/wiki/jest)
Usetestoritto define yourtest cases:
**Usetestorit**`test``it`[test cases](/wiki/test-case)
```
test('adds 1 + 2 to equal 3', () => {
  expect(1 + 2).toBe(3);
});
```
`test('adds 1 + 2 to equal 3', () => {
  expect(1 + 2).toBe(3);
});`
Run your testsby executing thetest script:
**Run your tests**[test script](/wiki/test-script)
```
npm test
```
`npm test`
or

```
yarn test
```
`yarn test`
Jestwill execute the tests and provide a summary of the results. Adjust your tests and code based on the feedback from the test runs.
[Jest](/wiki/jest)
To configureJestfor a project, create ajest.config.jsfile at the root of your project or define ajestkey in yourpackage.json. Here's a basic example of what ajest.config.jsfile might look like:
[Jest](/wiki/jest)`jest.config.js``jest``package.json``jest.config.js`
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
`module.exports = {
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
};`- verbose: Enables verbose output for test results.
- testEnvironment: Sets the environment in which tests are run.
- setupFilesAfterEnv: Lists scripts to run after the test framework is installed in the environment.
- transform: Specifies how to process files using a transformer.
- testMatch: Determines which files are considered test files.
- moduleNameMapper: Maps module paths for easier imports.
- coverageThreshold: Sets the minimum coverage thresholds for the project.
**verbose****testEnvironment****setupFilesAfterEnv****transform****testMatch****moduleNameMapper****coverageThreshold**
For TypeScript projects, you'll need to installts-jestand configure thetransformproperty to use it.
`ts-jest``transform`
To include the configuration in yourpackage.json, it would look like this:
`package.json`
```
"jest": {
  "verbose": true,
  // ... other configurations
}
```
`"jest": {
  "verbose": true,
  // ... other configurations
}`
Remember to install any additionalJestplugins or presets you need for your project. Adjust the configuration options to match the specific needs of your project, such as custom global variables, module path aliases, or different environments for testing.
[Jest](/wiki/jest)
#### Writing and Running Tests
- How do you write a basic test in Jest?Writing a basic test inJestinvolves creating a test file with.test.jsor.spec.jssuffix, importing the necessary modules, and using thetestoritglobal function to define yourtest cases. Here's a succinct example:const sum = require('./sum'); // Import the function to test

test('adds 1 + 2 to equal 3', () => {
  expect(sum(1, 2)).toBe(3); // Use expect and matchers to test the function
});In this example,sumis a simple function that adds two numbers. Thetestfunction takes two arguments: a string describing thetest case, and a callback function where the actual testing code is written. Theexpectfunction is used to assert the expected outcome, and.toBeis a matcher that checks for strict equality.Remember to structure your tests logically and clearly, so they are easy to read and understand. Usedescriptive test namesandassertionsthat accurately reflect the behavior you are testing. Keep testsfocusedon a single functionality to make them maintainable and to facilitate easier debugging when a test fails.
- What is the structure of a Jest test?AJesttest structure typically consists of a series ofdescribeblocks that group together related tests, anditortestblocks that define individualtest cases. Here's a basic outline:describe('Component or Functionality Group', () => {
  
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

});describe: Groups multiple tests; useful for organizing tests by functionality or components.beforeEach/afterEach: Setup/teardown hooks that run before/after each test in the describe block.it/test: Defines an individual test case;itis an alias fortest, and both are interchangeable.expect: Creates an assertion about the expected outcome of the test case.Tests can be nested withindescribeblocks for further organization.beforeAllandafterAllhooks are also available forsetup/teardown that should only happen once before/after all tests in a describe block.
- How do you run tests in Jest?To run tests inJest, follow these steps:Navigate to your project directoryin the terminal.Ensure you have apackage.jsonfile in your project. If not, create one usingnpm init.Run testsusing one of the following commands:To run all tests:jestor if Jest is not globally installed:npx jestor by using an npm script inpackage.json:"scripts": {
  "test": "jest"
}then execute with npm:npm testRun a specific test fileby appending the file path:jest path/to/your_test_file.jsWatch mode: To runJestin watch mode, which reruns tests on file changes, use the--watchflag:jest --watchFilter testsby test name using the--testNamePatternflag:jest --testNamePattern="pattern"Run tests matching a specific filename patternwith the--testPathPatternflag:jest --testPathPattern="pattern"Run tests related to changed filesbased on your Git repository with:jest --onlyChangedRun tests in a specific environmentby setting thetestEnvironmentin yourJestconfiguration.Generate coverage reportsusing the--coverageflag:jest --coverageJestCLI offers many other options, which can be listed by runningjest --help.
- What are some common assertions in Jest?InJest, assertions are made using theexpectfunction, which is chained with "matcher" functions to test values in different ways. Here are some common assertions:Equality:toBe(value)checks strict equality (===).toEqual(value)checks value equality, useful for objects and arrays.expect(5).toBe(5);
expect({ a: 1 }).toEqual({ a: 1 });Truthiness:toBeNull()checks that a value isnull.toBeUndefined()checks that a value isundefined.toBeDefined()checks that a value is notundefined.toBeTruthy()checks that a value is truthy.toBeFalsy()checks that a value is falsy.expect(null).toBeNull();
expect(undefined).toBeUndefined();
expect(1).toBeTruthy();Numbers:toBeGreaterThan(number)checks that a value is greater than a number.toBeGreaterThanOrEqual(number)checks that a value is greater than or equal to a number.toBeLessThan(number)checks that a value is less than a number.toBeLessThanOrEqual(number)checks that a value is less than or equal to a number.expect(10).toBeGreaterThan(5);
expect(10).toBeLessThanOrEqual(10);Strings:toMatch(regexpOrString)checks that a string matches a regular expression or string.expect('team').toMatch(/T/i);Arrays:toContain(item)checks that an array contains a specific item.expect(['Alice', 'Bob', 'Eve']).toContain('Bob');Exceptions:toThrow(error?)checks that a function throws an error when called.expect(() => { throw new Error('Error!'); }).toThrow('Error!');Objects:toHaveProperty(keyPath, value?)checks that an object has a property at the specified key path, optionally checking the value.expect({ a: { b: 1 } }).toHaveProperty('a.b', 1);These assertions help ensure that the code behaves as expected, and they are a crucial part of writing comprehensivetest suiteswithJest.
- How do you group tests in Jest?InJest, you can group tests using thedescribefunction. This function allows you to create a block that groups together several related tests. Here's a basic example:describe('My Feature', () => {
  test('should do behavior A', () => {
    // Test for behavior A
  });

  test('should do behavior B', () => {
    // Test for behavior B
  });
});Eachdescribeblock can contain its ownsetupand teardown for the group of tests usingbeforeEach,afterEach,beforeAll, andafterAllfunctions. This helps in organizing tests logically and managing sharedsetupand teardown processes efficiently.Nesteddescribeblocks can be used for more granular grouping:describe('My Feature', () => {
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
});Usingdescribeblocks is particularly useful for differentiating between various states or conditions of the feature being tested, and it enhances the readability oftest reportsby clearly showing which group a failing test belongs to.

Writing a basic test inJestinvolves creating a test file with.test.jsor.spec.jssuffix, importing the necessary modules, and using thetestoritglobal function to define yourtest cases. Here's a succinct example:
[Jest](/wiki/jest)`.test.js``.spec.js``test``it`[test cases](/wiki/test-case)
```
const sum = require('./sum'); // Import the function to test

test('adds 1 + 2 to equal 3', () => {
  expect(sum(1, 2)).toBe(3); // Use expect and matchers to test the function
});
```
`const sum = require('./sum'); // Import the function to test

test('adds 1 + 2 to equal 3', () => {
  expect(sum(1, 2)).toBe(3); // Use expect and matchers to test the function
});`
In this example,sumis a simple function that adds two numbers. Thetestfunction takes two arguments: a string describing thetest case, and a callback function where the actual testing code is written. Theexpectfunction is used to assert the expected outcome, and.toBeis a matcher that checks for strict equality.
`sum``test`[test case](/wiki/test-case)`expect``.toBe`
Remember to structure your tests logically and clearly, so they are easy to read and understand. Usedescriptive test namesandassertionsthat accurately reflect the behavior you are testing. Keep testsfocusedon a single functionality to make them maintainable and to facilitate easier debugging when a test fails.
**descriptive test names****assertions****focused**
AJesttest structure typically consists of a series ofdescribeblocks that group together related tests, anditortestblocks that define individualtest cases. Here's a basic outline:
[Jest](/wiki/jest)**describe****it****test**[test cases](/wiki/test-case)
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
`describe('Component or Functionality Group', () => {
  
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

});`- describe: Groups multiple tests; useful for organizing tests by functionality or components.
- beforeEach/afterEach: Setup/teardown hooks that run before/after each test in the describe block.
- it/test: Defines an individual test case;itis an alias fortest, and both are interchangeable.
- expect: Creates an assertion about the expected outcome of the test case.
**describe****beforeEach/afterEach****it/test**`it``test`**expect**
Tests can be nested withindescribeblocks for further organization.beforeAllandafterAllhooks are also available forsetup/teardown that should only happen once before/after all tests in a describe block.
**describe****beforeAll****afterAll**[setup](/wiki/setup)
To run tests inJest, follow these steps:
[Jest](/wiki/jest)1. Navigate to your project directoryin the terminal.
2. Ensure you have apackage.jsonfile in your project. If not, create one usingnpm init.
3. Run testsusing one of the following commands:To run all tests:jestor if Jest is not globally installed:npx jestor by using an npm script inpackage.json:"scripts": {
  "test": "jest"
}then execute with npm:npm test
4. Run a specific test fileby appending the file path:jest path/to/your_test_file.js
5. Watch mode: To runJestin watch mode, which reruns tests on file changes, use the--watchflag:jest --watch
6. Filter testsby test name using the--testNamePatternflag:jest --testNamePattern="pattern"
7. Run tests matching a specific filename patternwith the--testPathPatternflag:jest --testPathPattern="pattern"
8. Run tests related to changed filesbased on your Git repository with:jest --onlyChanged
9. Run tests in a specific environmentby setting thetestEnvironmentin yourJestconfiguration.
10. Generate coverage reportsusing the--coverageflag:jest --coverage

Navigate to your project directoryin the terminal.
**Navigate to your project directory**
Ensure you have apackage.jsonfile in your project. If not, create one usingnpm init.
`package.json``npm init`
Run testsusing one of the following commands:
**Run tests**- To run all tests:jestor if Jest is not globally installed:npx jestor by using an npm script inpackage.json:"scripts": {
  "test": "jest"
}then execute with npm:npm test

```
jest
```
`jest`
```
npx jest
```
`npx jest``package.json`
```
"scripts": {
  "test": "jest"
}
```
`"scripts": {
  "test": "jest"
}`
```
npm test
```
`npm test`
Run a specific test fileby appending the file path:
**Run a specific test file**
```
jest path/to/your_test_file.js
```
`jest path/to/your_test_file.js`
Watch mode: To runJestin watch mode, which reruns tests on file changes, use the--watchflag:
**Watch mode**[Jest](/wiki/jest)`--watch`
```
jest --watch
```
`jest --watch`
Filter testsby test name using the--testNamePatternflag:
**Filter tests**`--testNamePattern`
```
jest --testNamePattern="pattern"
```
`jest --testNamePattern="pattern"`
Run tests matching a specific filename patternwith the--testPathPatternflag:
**Run tests matching a specific filename pattern**`--testPathPattern`
```
jest --testPathPattern="pattern"
```
`jest --testPathPattern="pattern"`
Run tests related to changed filesbased on your Git repository with:
**Run tests related to changed files**
```
jest --onlyChanged
```
`jest --onlyChanged`
Run tests in a specific environmentby setting thetestEnvironmentin yourJestconfiguration.
**Run tests in a specific environment**`testEnvironment`[Jest](/wiki/jest)
Generate coverage reportsusing the--coverageflag:
**Generate coverage reports**`--coverage`
```
jest --coverage
```
`jest --coverage`
JestCLI offers many other options, which can be listed by runningjest --help.
[Jest](/wiki/jest)`jest --help`
InJest, assertions are made using theexpectfunction, which is chained with "matcher" functions to test values in different ways. Here are some common assertions:
[Jest](/wiki/jest)`expect`- Equality:toBe(value)checks strict equality (===).toEqual(value)checks value equality, useful for objects and arrays.expect(5).toBe(5);
expect({ a: 1 }).toEqual({ a: 1 });
- Truthiness:toBeNull()checks that a value isnull.toBeUndefined()checks that a value isundefined.toBeDefined()checks that a value is notundefined.toBeTruthy()checks that a value is truthy.toBeFalsy()checks that a value is falsy.expect(null).toBeNull();
expect(undefined).toBeUndefined();
expect(1).toBeTruthy();
- Numbers:toBeGreaterThan(number)checks that a value is greater than a number.toBeGreaterThanOrEqual(number)checks that a value is greater than or equal to a number.toBeLessThan(number)checks that a value is less than a number.toBeLessThanOrEqual(number)checks that a value is less than or equal to a number.expect(10).toBeGreaterThan(5);
expect(10).toBeLessThanOrEqual(10);
- Strings:toMatch(regexpOrString)checks that a string matches a regular expression or string.expect('team').toMatch(/T/i);
- Arrays:toContain(item)checks that an array contains a specific item.expect(['Alice', 'Bob', 'Eve']).toContain('Bob');
- Exceptions:toThrow(error?)checks that a function throws an error when called.expect(() => { throw new Error('Error!'); }).toThrow('Error!');
- Objects:toHaveProperty(keyPath, value?)checks that an object has a property at the specified key path, optionally checking the value.expect({ a: { b: 1 } }).toHaveProperty('a.b', 1);

Equality:
**Equality**- toBe(value)checks strict equality (===).
- toEqual(value)checks value equality, useful for objects and arrays.
`toBe(value)``toEqual(value)`
```
expect(5).toBe(5);
expect({ a: 1 }).toEqual({ a: 1 });
```
`expect(5).toBe(5);
expect({ a: 1 }).toEqual({ a: 1 });`
Truthiness:
**Truthiness**- toBeNull()checks that a value isnull.
- toBeUndefined()checks that a value isundefined.
- toBeDefined()checks that a value is notundefined.
- toBeTruthy()checks that a value is truthy.
- toBeFalsy()checks that a value is falsy.
`toBeNull()``null``toBeUndefined()``undefined``toBeDefined()``undefined``toBeTruthy()``toBeFalsy()`
```
expect(null).toBeNull();
expect(undefined).toBeUndefined();
expect(1).toBeTruthy();
```
`expect(null).toBeNull();
expect(undefined).toBeUndefined();
expect(1).toBeTruthy();`
Numbers:
**Numbers**- toBeGreaterThan(number)checks that a value is greater than a number.
- toBeGreaterThanOrEqual(number)checks that a value is greater than or equal to a number.
- toBeLessThan(number)checks that a value is less than a number.
- toBeLessThanOrEqual(number)checks that a value is less than or equal to a number.
`toBeGreaterThan(number)``toBeGreaterThanOrEqual(number)``toBeLessThan(number)``toBeLessThanOrEqual(number)`
```
expect(10).toBeGreaterThan(5);
expect(10).toBeLessThanOrEqual(10);
```
`expect(10).toBeGreaterThan(5);
expect(10).toBeLessThanOrEqual(10);`
Strings:
**Strings**- toMatch(regexpOrString)checks that a string matches a regular expression or string.
`toMatch(regexpOrString)`
```
expect('team').toMatch(/T/i);
```
`expect('team').toMatch(/T/i);`
Arrays:
**Arrays**- toContain(item)checks that an array contains a specific item.
`toContain(item)`
```
expect(['Alice', 'Bob', 'Eve']).toContain('Bob');
```
`expect(['Alice', 'Bob', 'Eve']).toContain('Bob');`
Exceptions:
**Exceptions**- toThrow(error?)checks that a function throws an error when called.
`toThrow(error?)`
```
expect(() => { throw new Error('Error!'); }).toThrow('Error!');
```
`expect(() => { throw new Error('Error!'); }).toThrow('Error!');`
Objects:
**Objects**- toHaveProperty(keyPath, value?)checks that an object has a property at the specified key path, optionally checking the value.
`toHaveProperty(keyPath, value?)`
```
expect({ a: { b: 1 } }).toHaveProperty('a.b', 1);
```
`expect({ a: { b: 1 } }).toHaveProperty('a.b', 1);`
These assertions help ensure that the code behaves as expected, and they are a crucial part of writing comprehensivetest suiteswithJest.
[test suites](/wiki/test-suite)[Jest](/wiki/jest)
InJest, you can group tests using thedescribefunction. This function allows you to create a block that groups together several related tests. Here's a basic example:
[Jest](/wiki/jest)`describe`
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
`describe('My Feature', () => {
  test('should do behavior A', () => {
    // Test for behavior A
  });

  test('should do behavior B', () => {
    // Test for behavior B
  });
});`
Eachdescribeblock can contain its ownsetupand teardown for the group of tests usingbeforeEach,afterEach,beforeAll, andafterAllfunctions. This helps in organizing tests logically and managing sharedsetupand teardown processes efficiently.
`describe`[setup](/wiki/setup)`beforeEach``afterEach``beforeAll``afterAll`[setup](/wiki/setup)
Nesteddescribeblocks can be used for more granular grouping:
`describe`
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
`describe('My Feature', () => {
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
});`
Usingdescribeblocks is particularly useful for differentiating between various states or conditions of the feature being tested, and it enhances the readability oftest reportsby clearly showing which group a failing test belongs to.
`describe`[test reports](/wiki/test-report)
#### Advanced Concepts
- What is mocking in Jest and how is it used?Mocking inJestis a technique used to isolate and simulate the behavior of external modules or functions that a piece of code depends on. By creating mock functions or objects, you can control the inputs and outputs of these dependencies, allowing for more predictable and controlled testing environments.Mock functionscan be created usingjest.fn()to track calls and define return values. They can replace actual functions in your modules, letting you assert how they have been called and with what arguments.const mockFunction = jest.fn();
mockFunction.mockReturnValue('mocked value');Manual mocksare useful for modules and complex dependencies. You can create a__mocks__directory adjacent to the module, andJestwill use the mocked version instead of the real one when thejest.mock()function is called in your tests.// In your test file
jest.mock('./path/to/module');Automatic mockingwithjest.mock()allowsJestto take over module imports and replace them with a suitable mock object, with all exports being mocked functions.// In your test file
jest.mock('axios');Mocking is also used tostub out functionalitythat would otherwise have side effects, such as network requests or file system operations, by replacing them with mock implementations that mimic the behavior without performing the actual operation.Mocking inJestis essential for creating unit tests that are independent of external factors and for ensuring that your tests are deterministic, meaning they produce the same results every time they are run.
- How does Jest handle asynchronous testing?Jesthandles asynchronous testing by providing several methods to deal with different types of async code. These include:Callbacks: For testing older callback-style code, Jest provides thedoneparameter in test functions. Calldone()when the async operation completes to signal Jest that the test is finished.test('async test with callback', done => {
  setTimeout(() => {
    expect(true).toBe(true);
    done();
  }, 1000);
});Promises: If the code returns a promise, return it from the test, and Jest will wait for it to resolve or reject.test('async test with promise', () => {
  return fetchData().then(data => {
    expect(data).toBe('expected data');
  });
});Async/Await: For modern async code, useasyncfunctions andawaitthe asynchronous operation. Jest will wait for theasyncfunction to resolve before completing the test.test('async test with async/await', async () => {
  const data = await fetchData();
  expect(data).toBe('expected data');
});Timers: Jest can mock timers and control time for operations that usesetTimeout,setInterval, orsetImmediatewithjest.useFakeTimers()and related timer control functions.jest.useFakeTimers();
test('async test with timers', () => {
  const callback = jest.fn();
  setTimeout(callback, 1000);
  jest.runAllTimers();
  expect(callback).toHaveBeenCalled();
});These methods allow for comprehensive testing of asynchronous operations, ensuring that tests only complete when all async actions have been accounted for.
- How can you use Jest for snapshot testing?Jest's snapshot testing feature allows you totest the "shape" of your code's output. This is particularly useful for UI components, ensuring that changes to components don't cause unexpected results.To useJestfor snapshot testing, follow these steps:Write a testthat renders your component or calls your function.Useexpectalong with thetoMatchSnapshot()matcher toassert that the output matches the saved snapshot.Here's a basic example using a React component:import React from 'react';
import renderer from 'react-test-renderer';
import MyComponent from './MyComponent';

test('MyComponent renders correctly', () => {
  const tree = renderer.create(<MyComponent />).toJSON();
  expect(tree).toMatchSnapshot();
});When this test runs for the first time,Jestcreates a snapshot file in a__snapshots__directory next to the test file. The snapshot contains a string representation of the component's render output.On subsequent test runs,Jestcompares the rendered output with the saved snapshot. If there's a difference, the test fails, prompting a review. If the change is intentional,update the snapshotusingJest's--updateSnapshotor-uflag:jest --updateSnapshotor for a specific test file:jest MyComponent.test.js --updateSnapshotRemember, snapshots should be committed alongside code changes. Review snapshots during code reviews tocatch unintended changes. Use snapshot testing judiciously, as over-reliance can lead to large snapshot files and reduced test sensitivity to meaningful changes.
- What is the role of 'describe' function in Jest?InJest, thedescribefunction is used togroup together related tests. It serves as a way to organize yourtest suitebyencapsulating multipletest casesthat test a specific feature or component. This is particularly useful for readability and maintenance, as it allows developers to see at a glance which tests are related and to run a subset of tests that are relevant to the area of code they are working on.Thedescribeblock can contain any number oftestoritblocks, and can also benestedwithin otherdescribeblocks to further structure your tests hierarchically. Eachdescribeblock can also have its ownbeforeEach,afterEach,beforeAll, andafterAlllifecycle methods, which apply only to the tests within thatdescribeblock.Here's a basic example of usingdescribeinJest:describe('MyComponent', () => {
  beforeEach(() => {
    // Setup code specific to this group
  });

  test('should render correctly', () => {
    // Test case for rendering
  });

  test('should handle user input', () => {
    // Test case for user input
  });
});Usingdescribehelps to keep testsDRY(Don't Repeat Yourself) by allowing sharedsetupand teardown code for the tests in the group, and it enhances theorganizationandreadabilityof the test output, asJestwill report results based on these groupings.
- How can you use 'beforeEach' and 'afterEach' in Jest?InJest,beforeEachandafterEachare lifecycle methods used to run some code before and after each test within adescribeblock. They help in setting up preconditions and cleaning up after tests to avoid side effects.UsebeforeEachwhen you want to initialize certain variables, mock functions, or set up the environment for eachtest case. It ensures that every test runs with a fresh state.beforeEach(() => {
  // Initialization or setup code here
});afterEachis used for teardown activities, such as clearing mocks, resetting modules, or releasing resources used by the tests.afterEach(() => {
  // Teardown or cleanup code here
});Example:describe('test suite', () => {
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
});In this example, thesetupcode will run beforetest case 1andtest case 2, and the cleanup code will run after each of thesetest casescompletes. This ensures that each test is isolated and does not affect the other.

Mocking inJestis a technique used to isolate and simulate the behavior of external modules or functions that a piece of code depends on. By creating mock functions or objects, you can control the inputs and outputs of these dependencies, allowing for more predictable and controlled testing environments.
[Jest](/wiki/jest)
Mock functionscan be created usingjest.fn()to track calls and define return values. They can replace actual functions in your modules, letting you assert how they have been called and with what arguments.
**Mock functions**`jest.fn()`
```
const mockFunction = jest.fn();
mockFunction.mockReturnValue('mocked value');
```
`const mockFunction = jest.fn();
mockFunction.mockReturnValue('mocked value');`
Manual mocksare useful for modules and complex dependencies. You can create a__mocks__directory adjacent to the module, andJestwill use the mocked version instead of the real one when thejest.mock()function is called in your tests.
**Manual mocks**`__mocks__`[Jest](/wiki/jest)`jest.mock()`
```
// In your test file
jest.mock('./path/to/module');
```
`// In your test file
jest.mock('./path/to/module');`
Automatic mockingwithjest.mock()allowsJestto take over module imports and replace them with a suitable mock object, with all exports being mocked functions.
**Automatic mocking**`jest.mock()`[Jest](/wiki/jest)
```
// In your test file
jest.mock('axios');
```
`// In your test file
jest.mock('axios');`
Mocking is also used tostub out functionalitythat would otherwise have side effects, such as network requests or file system operations, by replacing them with mock implementations that mimic the behavior without performing the actual operation.
**stub out functionality**
Mocking inJestis essential for creating unit tests that are independent of external factors and for ensuring that your tests are deterministic, meaning they produce the same results every time they are run.
[Jest](/wiki/jest)
Jesthandles asynchronous testing by providing several methods to deal with different types of async code. These include:
[Jest](/wiki/jest)- Callbacks: For testing older callback-style code, Jest provides thedoneparameter in test functions. Calldone()when the async operation completes to signal Jest that the test is finished.
**Callbacks**`done``done()`
```
test('async test with callback', done => {
  setTimeout(() => {
    expect(true).toBe(true);
    done();
  }, 1000);
});
```
`test('async test with callback', done => {
  setTimeout(() => {
    expect(true).toBe(true);
    done();
  }, 1000);
});`- Promises: If the code returns a promise, return it from the test, and Jest will wait for it to resolve or reject.
**Promises**
```
test('async test with promise', () => {
  return fetchData().then(data => {
    expect(data).toBe('expected data');
  });
});
```
`test('async test with promise', () => {
  return fetchData().then(data => {
    expect(data).toBe('expected data');
  });
});`- Async/Await: For modern async code, useasyncfunctions andawaitthe asynchronous operation. Jest will wait for theasyncfunction to resolve before completing the test.
**Async/Await**`async``await``async`
```
test('async test with async/await', async () => {
  const data = await fetchData();
  expect(data).toBe('expected data');
});
```
`test('async test with async/await', async () => {
  const data = await fetchData();
  expect(data).toBe('expected data');
});`- Timers: Jest can mock timers and control time for operations that usesetTimeout,setInterval, orsetImmediatewithjest.useFakeTimers()and related timer control functions.
**Timers**`setTimeout``setInterval``setImmediate``jest.useFakeTimers()`
```
jest.useFakeTimers();
test('async test with timers', () => {
  const callback = jest.fn();
  setTimeout(callback, 1000);
  jest.runAllTimers();
  expect(callback).toHaveBeenCalled();
});
```
`jest.useFakeTimers();
test('async test with timers', () => {
  const callback = jest.fn();
  setTimeout(callback, 1000);
  jest.runAllTimers();
  expect(callback).toHaveBeenCalled();
});`
These methods allow for comprehensive testing of asynchronous operations, ensuring that tests only complete when all async actions have been accounted for.

Jest's snapshot testing feature allows you totest the "shape" of your code's output. This is particularly useful for UI components, ensuring that changes to components don't cause unexpected results.
[Jest](/wiki/jest)**test the "shape" of your code's output**
To useJestfor snapshot testing, follow these steps:
[Jest](/wiki/jest)1. Write a testthat renders your component or calls your function.
2. Useexpectalong with thetoMatchSnapshot()matcher toassert that the output matches the saved snapshot.
**Write a test**`expect``toMatchSnapshot()`**assert that the output matches the saved snapshot**
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
`import React from 'react';
import renderer from 'react-test-renderer';
import MyComponent from './MyComponent';

test('MyComponent renders correctly', () => {
  const tree = renderer.create(<MyComponent />).toJSON();
  expect(tree).toMatchSnapshot();
});`
When this test runs for the first time,Jestcreates a snapshot file in a__snapshots__directory next to the test file. The snapshot contains a string representation of the component's render output.
[Jest](/wiki/jest)`__snapshots__`
On subsequent test runs,Jestcompares the rendered output with the saved snapshot. If there's a difference, the test fails, prompting a review. If the change is intentional,update the snapshotusingJest's--updateSnapshotor-uflag:
[Jest](/wiki/jest)**update the snapshot**[Jest](/wiki/jest)`--updateSnapshot``-u`
```
jest --updateSnapshot
```
`jest --updateSnapshot`
or for a specific test file:

```
jest MyComponent.test.js --updateSnapshot
```
`jest MyComponent.test.js --updateSnapshot`
Remember, snapshots should be committed alongside code changes. Review snapshots during code reviews tocatch unintended changes. Use snapshot testing judiciously, as over-reliance can lead to large snapshot files and reduced test sensitivity to meaningful changes.
**catch unintended changes**
InJest, thedescribefunction is used togroup together related tests. It serves as a way to organize yourtest suitebyencapsulating multipletest casesthat test a specific feature or component. This is particularly useful for readability and maintenance, as it allows developers to see at a glance which tests are related and to run a subset of tests that are relevant to the area of code they are working on.
[Jest](/wiki/jest)`describe`**group together related tests**[test suite](/wiki/test-suite)**encapsulating multipletest cases**[test cases](/wiki/test-case)
Thedescribeblock can contain any number oftestoritblocks, and can also benestedwithin otherdescribeblocks to further structure your tests hierarchically. Eachdescribeblock can also have its ownbeforeEach,afterEach,beforeAll, andafterAlllifecycle methods, which apply only to the tests within thatdescribeblock.
`describe``test``it`**nested**`describe``describe``beforeEach``afterEach``beforeAll``afterAll``describe`
Here's a basic example of usingdescribeinJest:
`describe`[Jest](/wiki/jest)
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
`describe('MyComponent', () => {
  beforeEach(() => {
    // Setup code specific to this group
  });

  test('should render correctly', () => {
    // Test case for rendering
  });

  test('should handle user input', () => {
    // Test case for user input
  });
});`
Usingdescribehelps to keep testsDRY(Don't Repeat Yourself) by allowing sharedsetupand teardown code for the tests in the group, and it enhances theorganizationandreadabilityof the test output, asJestwill report results based on these groupings.
`describe`**DRY**[setup](/wiki/setup)**organization****readability**[Jest](/wiki/jest)
InJest,beforeEachandafterEachare lifecycle methods used to run some code before and after each test within adescribeblock. They help in setting up preconditions and cleaning up after tests to avoid side effects.
[Jest](/wiki/jest)`beforeEach``afterEach``describe`
UsebeforeEachwhen you want to initialize certain variables, mock functions, or set up the environment for eachtest case. It ensures that every test runs with a fresh state.
`beforeEach`[test case](/wiki/test-case)
```
beforeEach(() => {
  // Initialization or setup code here
});
```
`beforeEach(() => {
  // Initialization or setup code here
});`
afterEachis used for teardown activities, such as clearing mocks, resetting modules, or releasing resources used by the tests.
`afterEach`
```
afterEach(() => {
  // Teardown or cleanup code here
});
```
`afterEach(() => {
  // Teardown or cleanup code here
});`
Example:
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
`describe('test suite', () => {
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
});`
In this example, thesetupcode will run beforetest case 1andtest case 2, and the cleanup code will run after each of thesetest casescompletes. This ensures that each test is isolated and does not affect the other.
[setup](/wiki/setup)`test case 1``test case 2`[test cases](/wiki/test-case)
