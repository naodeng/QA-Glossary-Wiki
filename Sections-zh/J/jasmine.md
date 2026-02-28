# 茉莉花

<!-- TOC START -->
- [相关术语：](#相关术语：)
  - [另请参阅：](#另请参阅：)
- [关于茉莉花的问题吗？](#关于茉莉花的问题吗？)
  - [基础知识和重要性](#基础知识和重要性)
    - [软件测试中的 Jasmine 是什么？](#软件测试中的-jasmine-是什么？)
    - [为什么 Jasmine 在 e2e 测试中被认为很重要？](#为什么-jasmine-在-e2e-测试中被认为很重要？)
    - [Jasmine 的主要特点是什么？](#jasmine-的主要特点是什么？)
    - [Jasmine 与其他测试框架相比如何？](#jasmine-与其他测试框架相比如何？)
  - [安装和设置](#安装和设置)
    - [如何安装 Jasmine 进行 JavaScript 测试？](#如何安装-jasmine-进行-javascript-测试？)
    - [安装 Jasmine 有哪些先决条件？](#安装-jasmine-有哪些先决条件？)
    - [如何设置基本的 Jasmine 测试环境？](#如何设置基本的-jasmine-测试环境？)
  - [测试写作](#测试写作)
    - [如何在 Jasmine 中编写基本测试？](#如何在-jasmine-中编写基本测试？)
    - [Jasmine 测试的结构是什么？](#jasmine-测试的结构是什么？)
    - [如何在 Jasmine 中使用“describe”和“it”函数？](#如何在-jasmine-中使用describe和it函数？)
    - [Jasmine 中的 'beforeEach' 和 'afterEach' 函数是什么以及它们如何使用？](#jasmine-中的-beforeeach-和-aftereach-函数是什么以及它们如何使用？)
  - [断言和匹配器](#断言和匹配器)
    - [什么是 Jasmine 匹配器以及它们如何使用？](#什么是-jasmine-匹配器以及它们如何使用？)
    - [如何在 Jasmine 中创建自定义匹配器？](#如何在-jasmine-中创建自定义匹配器？)
    - [Jasmine 中有哪些不同类型的断言？](#jasmine-中有哪些不同类型的断言？)
  - [间谍和嘲笑](#间谍和嘲笑)
    - [什么是 Jasmine 间谍以及如何使用它们？](#什么是-jasmine-间谍以及如何使用它们？)
    - [如何在 Jasmine 中创建模拟？](#如何在-jasmine-中创建模拟？)
    - [Jasmine 中的间谍和模拟有什么区别？](#jasmine-中的间谍和模拟有什么区别？)
  - [高级概念](#高级概念)
    - [Jasmine 中如何处理异步测试？](#jasmine-中如何处理异步测试？)
    - [如何将 Jasmine 与其他库或框架（如 Angular 或 React）一起使用？](#如何将-jasmine-与其他库或框架（如-angular-或-react）一起使用？)
    - [在 Jasmine 中编写测试的最佳实践有哪些？](#在-jasmine-中编写测试的最佳实践有哪些？)
<!-- TOC END -->

茉莉花

是一个 JavaScript 开源测试框架。它被设计为行为驱动的，允许开发人员以清晰、人类可读的术语描述软件预期行为的方式编写测试。

茉莉花

提供构建测试、设置前提条件和定义断言的函数。

## 相关术语：

- [Testing framework](../T/testing-framework.md)
- [Jest](../J/jest.md)
- [Chai.js](../C/chaijs.md)

### 另请参阅：

- [Official Website](https://jasmine.github.io/)
- [Wikipedia](https://en.wikipedia.org/wiki/Jasmine_(software))

## 关于茉莉花的问题吗？

### 基础知识和重要性

#### 软件测试中的 Jasmine 是什么？

[Jasmine](../J/jasmine.md) 是一个用于测试 JavaScript 代码的 **行为驱动开发 ([BDD](../B/bdd.md))** 框架。它不依赖于浏览器、DOM 或任何 JavaScript 框架，因此适合测试任何 JavaScript 应用程序。 [Jasmine](../J/jasmine.md) 的语法被设计为易于阅读和编写，旨在既具有表现力又全面。
  [Jasmine](../J/jasmine.md) 中的测试称为 **specs**，它是通过调用全局 `it` 函数来定义的。规范被分组为套件，这些套件是通过调用全局 `describe` 函数来定义的。套件可以嵌套在其他套件中，从而允许使用分层结构来组织测试。
  [Jasmine](../J/jasmine.md) 提供内置的**匹配器**，让您以可读的形式表达对值的期望。这些匹配器包括 `toEqual`、`toBe`、`toMatch` 等函数。还可以定义自定义匹配器来扩展框架的功能。
  **间谍**是[Jasmine](../J/jasmine.md) 创建测试替身的方式，它可以跟踪对函数及其参数的调用、返回值以及`this` 的值。它们通过用间谍对象替换实际函数来隔离测试中的代码非常有用。
  对于异步操作，[Jasmine](../J/jasmine.md) 提供`done` 回调来向框架发出异步规范已完成的信号。或者，您可以将较新的`async/await` 语法与[Jasmine](../J/jasmine.md) 的`beforeAll`、`afterAll`、`beforeEach` 和`afterEach` 函数结合使用来处理[setup](../S/setup.md) 和拆卸任务。
  [Jasmine](../J/jasmine.md)的灵活性使其可以与其他库和框架一起使用，并且与各种持续集成工具集成良好。对于需要为其 JavaScript 代码提供强大、功能丰富的测试解决方案的开发人员来说，这是一个流行的选择。

#### 为什么 Jasmine 在 e2e 测试中被认为很重要？

[Jasmine](../J/jasmine.md) 在**端到端 (e2e) 测试**中被认为很重要，因为它提供了专门为测试 JavaScript 应用程序而定制的**行为驱动开发 ([BDD](../B/bdd.md))** 框架。它的重要性在于它能够模拟用户与 Web 应用程序的交互，从而确保整个流程从用户的角度按预期工作。
  在 e2e 测试中，[Jasmine](../J/jasmine.md) 通常与 **Protractor** 等工具结合使用，该工具允许测试 Angular 应用程序，或者与 **[Selenium](../S/selenium.md) [WebDriver](../W/webdriver.md)** 结合使用以测试非 Angular Web 应用程序。这种组合使测试人员能够在真实的浏览器环境中编写清晰且全面的[test suites](../T/test-suite.md)，涵盖用户故事和[use cases](../U/use-case.md)。
  [Jasmine](../J/jasmine.md) 的语法和结构使测试**可读且可维护**，这对于可能变得复杂的 e2e [test suites](../T/test-suite.md) 至关重要。该框架对**异步操作**的支持对于 e2e 测试也至关重要，在 e2e 测试中，等待页面加载、AJAX 调用和 UI 更新很常见。
  此外，[Jasmine](../J/jasmine.md) 的 **spies** 和 **mocks** 对于将测试与外部依赖项隔离至关重要，确保 e2e 测试重点关注用户体验而不是底层实现。这种隔离有助于识别可能影响最终用户的问题，使 [Jasmine](../J/jasmine.md) 成为 e2e 测试过程中不可或缺的一部分。
  通过提供一组强大的功能来模拟用户交互和验证应用程序行为，[Jasmine](../J/jasmine.md) 在提供高质量、用户友好的软件方面发挥着关键作用。

#### Jasmine 的主要特点是什么？

[Jasmine](../J/jasmine.md) 的主要功能包括：

- **行为驱动开发 ([BDD](../B/bdd.md)) 语法**：鼓励编写易于阅读和理解的测试。
  - **无外部依赖**：开箱即用，无需其他库。
  - **丰富的匹配器集**：为常见断言提供内置匹配器，例如
    `toEqual`
    ,
    `toBe`
    ,
    `toMatch`
    ，等等。

- **简洁明了的语法**：提供一个简单的界面来描述测试、设置条件和检查结果。
  - **异步支持**：处理异步代码
    `done`
    回调或承诺使用
    `async`
    /
    `await`
    。

- **Spies** ：内置测试替身，用于跟踪函数调用、参数和返回值。
  - **时钟控制**：Jasmine 的模拟时钟允许测试时间相关的代码。
  - **自动测试发现**：自动查找并运行规范文件中定义的测试。
  - **灵活的报告**：支持多种报告器显示测试结果，可定制或扩展。
  - **可扩展性**：允许添加自定义匹配器和报告器以满足特定需求。
  - **跨平台**：在任何支持 JavaScript 的平台上运行。
  - **集成友好**：可以与其他工具和框架一起使用，例如 Karma、Protractor 等。

  ```
  // Example of a simple Jasmine test
  describe('A suite', () => {
    it('contains a spec with an expectation', () => {
      expect(true).toBe(true);
    });
  });
  ```这些功能使 [Jasmine](../J/jasmine.md) 成为编写和维护 JavaScript 应用程序测试的强大且多功能的工具。

- **行为驱动开发 ([BDD](../B/bdd.md)) 语法**：鼓励编写易于阅读和理解的测试。
  - **无外部依赖**：开箱即用，无需其他库。
  - **丰富的匹配器集**：为常见断言提供内置匹配器，例如
    `toEqual`
    ,
    `toBe`
    ,
    `toMatch`
    ，等等。

- **简洁明了的语法**：提供一个简单的界面来描述测试、设置条件和检查结果。
  - **异步支持**：处理异步代码
    `done`
    回调或承诺使用
    `async`
    /
    `await`
    。

- **Spies** ：内置测试替身，用于跟踪函数调用、参数和返回值。
  - **时钟控制**：Jasmine 的模拟时钟允许测试时间相关的代码。
  - **自动测试发现**：自动查找并运行规范文件中定义的测试。
  - **灵活的报告**：支持多种报告器显示测试结果，可定制或扩展。
  - **可扩展性**：允许添加自定义匹配器和报告器以满足特定需求。
  - **跨平台**：在任何支持 JavaScript 的平台上运行。
  - **集成友好**：可以与其他工具和框架一起使用，例如 Karma、Protractor 等。

#### Jasmine 与其他测试框架相比如何？

[Jasmine](../J/jasmine.md) 因其**行为驱动开发 ([BDD](../B/bdd.md))** 风格而脱颖而出，但与其他测试框架相比，有几个区别需要考虑：

- **Mocha**：另一个流行的 JavaScript 测试框架，它很灵活，需要像 Chai 这样的断言库来进行断言。 Mocha 经常与 Chai 和 Sinon 搭配用于间谍、存根和模拟。然而，[Jasmine](../J/jasmine.md) 具有开箱即用的这些功能。
  - **[Jest](../J/jest.md)**：[Jest](../J/jest.md) 由 Facebook 开发，通常用于 React 应用程序。它的灵感来自[Jasmine](../J/jasmine.md)，但包括快照测试、内置覆盖率报告和更强大的模拟库等附加功能。 [Jest](../J/jest.md) 并行运行测试，这可以导致更快的[test execution](../T/test-execution.md)。
  - **QUnit**：QUnit 是 [unit testing](../U/unit-testing.md) 的强大框架，特别适合测试 jQuery 项目。与[Jasmine](../J/jasmine.md) 的[BDD](../B/bdd.md) 风格相比，它的方法更为传统。
  - **Karma**：本身不是一个测试框架，而是一个可以与 [Jasmine](../J/jasmine.md)、Mocha 或 QUnit 配合使用的 [test runner](../T/test-runner.md)。 Karma 通常用于在真实浏览器和设备上运行测试。
  - **[Cypress](../C/cypress.md)**：[end-to-end testing](../E/end-to-end-testing.md) 工具，与[Jasmine](../J/jasmine.md) 不同的是，它在浏览器中运行，这可以让您更轻松地在现实场景中测试 Web 应用程序。 [Cypress](../C/cypress.md)还提供了丰富的互动[test runner](../T/test-runner.md)。
  - **Protractor**：专门针对 Angular 应用程序的端到端测试框架。它使用 [Jasmine](../J/jasmine.md) 作为语法，但现在不太受欢迎，因为 Angular 团队推荐 [Cypress](../C/cypress.md) 或 [Jest](../J/jest.md) 用于新项目。
  [Jasmine](../J/jasmine.md) 的简单性和独立性使其成为那些喜欢一体化解决方案而不需要额外库的开发人员的不错选择。但是，对于更复杂的需求或特定的集成，其他框架可能更合适。

- **Mocha**：另一个流行的 JavaScript 测试框架，它很灵活，需要像 Chai 这样的断言库来进行断言。 Mocha 经常与 Chai 和 Sinon 搭配用于间谍、存根和模拟。然而，[Jasmine](../J/jasmine.md) 具有开箱即用的这些功能。
  - **[Jest](../J/jest.md)**：[Jest](../J/jest.md) 由 Facebook 开发，通常用于 React 应用程序。它的灵感来自[Jasmine](../J/jasmine.md)，但包括快照测试、内置覆盖率报告和更强大的模拟库等附加功能。 [Jest](../J/jest.md) 并行运行测试，这可以导致更快的[test execution](../T/test-execution.md)。
  - **QUnit**：QUnit 是 [unit testing](../U/unit-testing.md) 的强大框架，特别适合测试 jQuery 项目。与 [Jasmine](../J/jasmine.md) 的 [BDD](../B/bdd.md) 风格相比，它的方法更为传统。
  - **Karma**：本身不是一个测试框架，而是一个可以与 [Jasmine](../J/jasmine.md)、Mocha 或 QUnit 配合使用的 [test runner](../T/test-runner.md)。 Karma 通常用于在真实浏览器和设备上运行测试。
  - **[Cypress](../C/cypress.md)**：[end-to-end testing](../E/end-to-end-testing.md) 工具与[Jasmine](../J/jasmine.md) 不同，它在浏览器中运行，可以更轻松地在现实场景中测试 Web 应用程序。 [Cypress](../C/cypress.md) 还提供了丰富的交互式[test runner](../T/test-runner.md)。
  - **Protractor**：专门针对 Angular 应用程序的端到端测试框架。它使用 [Jasmine](../J/jasmine.md) 作为语法，但现在不太受欢迎，因为 Angular 团队推荐 [Cypress](../C/cypress.md) 或 [Jest](../J/jest.md) 用于新项目。

### 安装和设置

#### 如何安装 Jasmine 进行 JavaScript 测试？

要安装 [Jasmine](../J/jasmine.md) 进行 JavaScript 测试，您需要先安装 [Node.js](../N/node-js.md) 和 npm（节点包管理器）。请按照下列步骤操作：

1. 打开终端或命令提示符。
  2. 导航到要设置 Jasmine 的项目目录。
  3. 运行以下命令来初始化新的 npm 包（如果尚未初始化）：

  ```
  npm init
  ```

1. 按照提示创建
    `package.json`
    文件，或者如果您想跳过提示，请使用
    `npm init -y`
    对于默认设置。

2. 通过运行以下命令安装 Jasmine：

  ```
  npm install --save-dev jasmine
  ```此命令将 [Jasmine](../J/jasmine.md) 作为开发依赖项安装并将其添加到 `package.json` 文件中。

1. 在项目中初始化 Jasmine，这会创建一个spec目录和配置文件（
    `jasmine.json`
    ）用于您的测试：

  ```
  npx jasmine init
  ```

1. 要运行 Jasmine 测试，请将测试脚本添加到您的
    `package.json`
    文件：

  ```
  "scripts": {
    "test": "jasmine"
  }
  ```

1. 现在，您可以使用以下命令运行 Jasmine 测试：

  ```
  npm test
  ```此 [setup](../S/setup.md) 允许您为 JavaScript 代码编写和运行 [Jasmine](../J/jasmine.md) 测试。请记住在 `spec` 目录中创建测试文件，并使用 `*.spec.js` 等命名约定，以便 [Jasmine](../J/jasmine.md) 识别。

1. 打开终端或命令提示符。
  2. 导航到要设置 Jasmine 的项目目录。
  3. 运行以下命令来初始化新的 npm 包（如果尚未初始化）：
  1. 按照提示创建
    `package.json`
    文件，或者如果您想跳过提示，请使用
    `npm init -y`
    对于默认设置。

2. 通过运行以下命令安装 Jasmine：
  1. 在项目中初始化 Jasmine，这会创建一个spec目录和配置文件（
    `jasmine.json`
    ）用于您的测试：

1. 要运行 Jasmine 测试，请将测试脚本添加到您的
    `package.json`
    文件：

1. 现在，您可以使用以下命令运行 Jasmine 测试：

#### 安装 Jasmine 有哪些先决条件？

要安装[Jasmine](../J/jasmine.md)，请确保您满足以下先决条件：

- **[Node.js](../N/node-js.md)**：[Jasmine](../J/jasmine.md) 需要 [Node.js](../N/node-js.md) 才能运行。确保您安装了最新的稳定版本。您可以从官方[Node.js website](https://nodejs.org/)下载。
  - **npm（节点包管理器）**：npm 包含在[Node.js](../N/node-js.md) 中，用于安装[Jasmine](../J/jasmine.md)。通过在终端中运行 `npm -v` 来验证其安装。
  - **JavaScript 环境**：[Jasmine](../J/jasmine.md) 可用于基于浏览器的应用程序和[Node.js](../N/node-js.md) 应用程序。确保您为您的项目设置了合适的环境。
  - **package.json 文件**：如果您的项目中没有该文件，请通过在项目的根目录中运行 `npm init` 来创建它。这将管理项目的依赖关系。
  满足这些先决条件后，通过在终端中运行以下命令来安装[Jasmine](../J/jasmine.md)：

  ```
  npm install --save-dev jasmine
  ```这将在您的项目中安装 [Jasmine](../J/jasmine.md) 作为开发依赖项。安装后，通过运行以下命令初始化[Jasmine](../J/jasmine.md)：

  ```
  npx jasmine init
  ```这将为您的测试设置基本配置和目录结构。您现在可以开始编写 [Jasmine](../J/jasmine.md) 测试。

- **[Node.js](../N/node-js.md)**：[Jasmine](../J/jasmine.md) 需要 [Node.js](../N/node-js.md) 才能运行。确保您安装了最新的稳定版本。您可以从官方[Node.js website](https://nodejs.org/)下载。
  - **npm（节点包管理器）**：npm 包含在[Node.js](../N/node-js.md) 中，用于安装[Jasmine](../J/jasmine.md)。通过在终端中运行 `npm -v` 来验证其安装。
  - **JavaScript 环境**：[Jasmine](../J/jasmine.md) 可用于基于浏览器的应用程序和[Node.js](../N/node-js.md) 应用程序。确保您为您的项目设置了合适的环境。
  - **package.json 文件**：如果您的项目中没有该文件，请通过在项目的根目录中运行 `npm init` 来创建它。这将管理项目的依赖关系。

#### 如何设置基本的 Jasmine 测试环境？

要设置基本 [Jasmine](../J/jasmine.md) [test environment](../T/test-environment.md)，请执行以下步骤：

1. **如果尚未安装[Node.js](../N/node-js.md)**，请安装它。 [Jasmine](../J/jasmine.md) 需要[Node.js](../N/node-js.md) 在独立环境中运行。
  2. **使用 npm 全局安装[Jasmine](../J/jasmine.md)**，使其可以从系统中的任何位置使用：

    ```
    npm install -g jasmine
    ```

3. **在项目目录中初始化[Jasmine](../J/jasmine.md)**，创建`spec`目录和配置文件（`jasmine.json`）：

    ```
    jasmine init
    ```

4. **在 `spec` 目录中创建您的第一个规范文件**。 [Jasmine](../J/jasmine.md) 规范文件通常具有 `.spec.js` 后缀：

    ```
    touch spec/yourTest.spec.js
    ```

5. **使用 `describe` 和 `it` 块在规范文件中编写测试**。由于您避免了编写测试的细节，因此我们将跳过此处的内容。
  6. **运行测试** 只需在终端中执行 `jasmine` 命令即可：

    ```
    jasmine
    ```[Jasmine](../J/jasmine.md) 将自动查找并执行与 `jasmine.json` 配置文件中定义的模式匹配的所有规范文件。
  如果您计划将 [Jasmine](../J/jasmine.md) 与其他库一起使用或将其集成到更大的项目中，请记住通过创建 `package.json` 文件来**管理您的项目依赖项**。您可以通过运行`npm init`，然后安装[Jasmine](../J/jasmine.md) 作为`npm install --save-dev jasmine` 的开发依赖项来完成此操作。
  为了持续集成或与构建工具集成，您可能需要在 `package.json` 中设置其他配置或脚本，以确保 [Jasmine](../J/jasmine.md) 作为构建过程的一部分运行。

1. **如果尚未安装[Node.js](../N/node-js.md)**，请安装它。 [Jasmine](../J/jasmine.md) 需要[Node.js](../N/node-js.md) 在独立环境中运行。
  2. **使用 npm 全局安装[Jasmine](../J/jasmine.md)**，使其可以从系统中的任何位置使用：

    ```
    npm install -g jasmine
    ```

3. **在项目目录中初始化[Jasmine](../J/jasmine.md)**，创建`spec`目录和配置文件（`jasmine.json`）：

    ```
    jasmine init
    ```

4. **在 `spec` 目录中创建您的第一个规范文件**。 [Jasmine](../J/jasmine.md) 规范文件通常具有 `.spec.js` 后缀：

    ```
    touch spec/yourTest.spec.js
    ```

5. **使用 `describe` 和 `it` 块在规范文件中编写测试**。由于您避免了编写测试的细节，因此我们将跳过此处的内容。
  6. **运行测试** 只需在终端中执行 `jasmine` 命令即可：

    ```
    jasmine
    ```

### 测试写作

#### 如何在 Jasmine 中编写基本测试？

要在 [Jasmine](../J/jasmine.md) 中编写基本测试，您将使用 `describe` 和 `it` 函数分别定义 [test suite](../T/test-suite.md) 和规范（测试）。这是分步指南：

1. **定义[test suite](../T/test-suite.md)**
    使用
    `describe`
    。第一个参数是描述套件的字符串，第二个参数是包含一个或多个规范的函数。

  ```
  describe('My Test Suite', () => {
    // Specs go here
  });
  ```

1. **创建规范**
    套房内使用
    `it`
    。喜欢
    `describe`
    ,
    `it`
    接受一个描述规范的字符串和一个实现测试的函数。

  ```
  it('does something expected', () => {
    // Test implementation goes here
  });
  ```

1. **断言期望**
    在规范内使用
    `expect`
    与匹配器函数结合以对值进行断言。

  ```
  it('adds two numbers correctly', () => {
    let sum = 1 + 2;
    expect(sum).toEqual(3);
  });
  ```

1. **运行测试**
    使用 Jasmine 命令行工具或将 Jasmine 包含在 HTML 文件中并在浏览器中打开它。
  请记住构建测试以反映代码的行为而不是其实现细节。这使您的测试对代码库中的更改更具弹性。此外，让您的规范集中于单一行为，以便在测试失败时更容易识别问题。

1. **定义一个[test suite](../T/test-suite.md)**
    使用
    `describe`
    。第一个参数是描述套件的字符串，第二个参数是包含一个或多个规范的函数。

1. **创建规范**
    套房内使用
    `it`
    。喜欢
    `describe`
    ,
    `it`
    接受一个描述规范的字符串和一个实现测试的函数。

1. **断言期望**
    在规范内使用
    `expect`
    与匹配器函数结合以对值进行断言。

1. **运行测试**
    使用 Jasmine 命令行工具或将 Jasmine 包含在 HTML 文件中并在浏览器中打开它。

#### Jasmine 测试的结构是什么？

[Jasmine](../J/jasmine.md) 测试的结构由**套件**和**规范**组成。套件是使用 `describe` 函数定义的，该函数接受一个字符串和一个函数。字符串是套件的标题，函数是可以定义 [setup](../S/setup.md)、拆卸和规格的块。
  规范或规格是使用 `it` 函数定义的。每个规范代表一个测试，其中有一个字符串解释测试应该做什么，以及一个包含测试代码的函数。
  在规范中，您使用**匹配器**来断言有关代码的不同内容。 `expect` 函数用于对值进行断言，然后针对匹配器进行测试。
  这是一个基本结构：

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
  ```**嵌套套件**可以通过在另一个`describe` 中调用`describe` 来实现。这允许您创建子套件以更精细地组织规范。
  `beforeEach`、`afterEach`、`beforeAll` 和 `afterAll` 等 **钩子** 用于设置前提条件并在测试后进行清理。
  `it` 块还可以通过采用 `done` 回调或返回 Promise 来处理异步代码。
  请记住保持您的规范**集中**和**独立**，以确保可靠且可维护的测试。

#### 如何在 Jasmine 中使用“describe”和“it”函数？

在[Jasmine](../J/jasmine.md) 中，`describe` 函数用于对相关规范进行分组，通常称为“套件”。它有两个参数：一个字符串和一个函数。字符串是套件的标题，函数是实现套件的代码块。

  ```
  describe('A suite', () => {
    // Specs go here
  });
  ````it` 函数用于定义一个规范，它是单个[test case](../T/test-case.md)。它还需要一个字符串和一个函数。字符串是规范的标题，函数是 [test case](../T/test-case.md) 本身。

  ```
  it('contains spec with an expectation', () => {
    expect(true).toBe(true);
  });
  ```**用法**：

- **嵌套**：
    `describe`
    块可以相互嵌套以创建子套件，以更精细地组织规范。

- **范围**：在 a 中声明的变量
    `describe`
    任何人都可以访问
    `it`
    或
    `beforeEach`
    /
    `afterEach`
    在那间套房内。

- **执行** ：当 Jasmine 运行时，它会执行
    `describe`
    块按照定义的顺序排列，并且在每个套件中，
    `it`
    块按照定义的顺序运行。
  **例子**：

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
  ```在此示例中，`beforeEach` 在每个 `it` 之前运行，并在每个规范之前将 `num` 变量设置为 5。每个`it` 都包含一个期望，这是实际的测试断言。

- **嵌套**：
    `describe`
    块可以相互嵌套以创建子套件，以更精细地组织规范。

- **范围**：在 a 中声明的变量
    `describe`
    任何人都可以访问
    `it`
    或
    `beforeEach`
    /
    `afterEach`
    在那间套房内。

- **执行** ：当 Jasmine 运行时，它会执行
    `describe`
    块按照定义的顺序排列，并且在每个套件中，
    `it`
    块按照定义的顺序运行。

#### Jasmine 中的 'beforeEach' 和 'afterEach' 函数是什么以及它们如何使用？

在[Jasmine](../J/jasmine.md) 中，`beforeEach` 和`afterEach` 是定义要在`describe` 套件中的每个`it` 块**之前**和**之后**运行的代码的函数。这些函数用于设置前提条件并在测试后进行清理，以确保一致的测试环境。
  **`beforeEach`** 通常用于在每次测试运行之前设置状态。这可能涉及初始化变量、创建测试装置或将环境重置为已知状态。

  ```
  beforeEach(() => {
    // Code to set up the state before each test
  });
  ```**`afterEach`** 用于每次测试完成后需要运行的拆卸逻辑。这可以包括释放资源、清理模拟状态或重置测试期间所做的修改。

  ```
  afterEach(() => {
    // Code to clean up after each test
  });
  ```这些函数通过将 [setup](../S/setup.md) 和拆卸逻辑封装在实际测试断言之外，有助于减少代码重复并促进关注点分离。它们通过确保每个测试独立运行而不会产生先前测试的意外副作用，从而有助于提高[test suites](../T/test-suite.md) 的可维护性和可读性。

### 断言和匹配器

#### 什么是 Jasmine 匹配器以及它们如何使用？

[Jasmine](../J/jasmine.md) 匹配器是实现实际值和期望值之间的布尔比较的函数。它们用于在测试中编写断言，允许您检查是否满足某些条件。使用 `expect` 函数调用匹配器，该函数将实际值作为参数，后跟指定预期结果的匹配器函数。
  这是使用匹配器的示例：

  ```
  expect(someValue).toBe(42);
  ```在本例中，`toBe` 是检查`someValue` 是否严格等于`42` 的匹配器。
  常见的匹配器包括：

- `toBe` ：严格相等（===）比较。
  - `toEqual` ：深度相等比较，对于对象或数组很有用。
  - `toMatch` ：与正则表达式匹配的字符串。
  - `toBeDefined` ：检查变量是否不是
    `undefined`
    。

- `toBeNull` ：检查变量是否存在
    `null`
    。

- `toBeTruthy` ：检查变量是否为真。
  - `toBeFalsy` ：检查变量是否为假。
  - `toContain` ：检查数组或字符串是否包含特定项目或子字符串。
  - `toBeGreaterThan`
    ,
    `toBeLessThan`：数值比较。

- `toThrow` ：检查函数是否抛出错误。
  还可以创建自定义匹配器来封装重复或复杂的逻辑。通过使用定义 `compare` 函数的匹配器对象扩展 `jasmine.addMatchers` 方法，将它们添加到 [Jasmine](../J/jasmine.md) 中。
  匹配器对于清晰简洁地表达测试意图至关重要，使测试更易于阅读和维护。它们是 [Jasmine](../J/jasmine.md) 框架的核心部分，提供丰富的语言来指定 [test cases](../T/test-case.md) 中的各种条件和期望。

- `toBe` ：严格相等（===）比较。
  - `toEqual` ：深度相等比较，对于对象或数组很有用。
  - `toMatch` ：与正则表达式匹配的字符串。
  - `toBeDefined` ：检查变量是否不是
    `undefined`
    。

- `toBeNull` ：检查变量是否
    `null`
    。

- `toBeTruthy` ：检查变量是否为真。
  - `toBeFalsy` ：检查变量是否为假。
  - `toContain` ：检查数组或字符串是否包含特定项目或子字符串。
  - `toBeGreaterThan`
    ,
    `toBeLessThan`：数值比较。

- `toThrow` ：检查函数是否抛出错误。

#### 如何在 Jasmine 中创建自定义匹配器？

在[Jasmine](../J/jasmine.md) 中创建自定义匹配器允许您以更特定于领域的方式表达期望，从而增强测试的可读性和[maintainability](../M/maintainability.md)。以下是在 [Jasmine](../J/jasmine.md) 中定义自定义匹配器的方法：

1. 使用
    `jasmine.addMatchers`
    添加一个新的匹配器。

2. 内部
    `jasmine.addMatchers`
    ，定义一个对象，其中键是自定义匹配器的名称。

3. 每个匹配器都是一个工厂函数，返回一个带有
    `compare`
    功能。

4. 的
    `compare`
    函数应该返回一个带有
    `pass`
    属性，它是一个布尔值，指示是否满足期望，以及一个可选的
    `message`
    自定义失败消息的属性。
  下面是一个自定义匹配器的示例，用于检查数字是否为偶数：

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
  ```要在测试中使用此匹配器：

  ```
  it('is an even number', function() {
    expect(4).toBeEven();
  });
  ```通过将自定义匹配器包含在 [test suite](../T/test-suite.md) 顶层的 `beforeEach` 中或包含在测试 [setup](../S/setup.md) 中的单独文件中，可以在不同规范中重复使用自定义匹配器。

1. 使用
    `jasmine.addMatchers`
    添加一个新的匹配器。

2. 内部
    `jasmine.addMatchers`
    ，定义一个对象，其中键是自定义匹配器的名称。

3. 每个匹配器都是一个工厂函数，返回一个带有
    `compare`
    功能。

4. 的
    `compare`
    函数应该返回一个带有
    `pass`
    属性，它是一个布尔值，指示是否满足期望，以及一个可选的
    `message`
    自定义失败消息的属性。

#### Jasmine 中有哪些不同类型的断言？

在[Jasmine](../J/jasmine.md) 中，断言是使用**匹配器**进行的。 [Jasmine](../J/jasmine.md) 中的匹配器负责检查某个条件是否为真。 [Jasmine](../J/jasmine.md) 提供的不同类型的断言或匹配器包括：

- `toBe` ：检查实际值是否与预期值相同（===）。
  - `toEqual` ：检查实际值和预期值是否相等，包括对象和数组。
  - `toMatch` ：检查值是否与指定的正则表达式匹配。
  - `toBeDefined` ：断言变量不是
    `undefined`
    。

- `toBeUndefined` ：断言变量是
    `undefined`
    。

- `toBeNull` ：检查实际值是否为
    `null`
    。

- `toBeTruthy` ：断言实际值是真实的。
  - `toBeFalsy` ：断言实际值是假的。
  - `toContain` ：检查数组或字符串是否包含特定项目或子字符串。
  - `toBeLessThan` ：断言一个值小于另一个值。
  - `toBeGreaterThan` ：断言一个值大于另一个值。
  - `toBeCloseTo` ：检查一个数字是否在指定精度内接近另一个数字。
  - `toThrow` ：断言函数抛出异常。
  - `toThrowError` ：检查函数是否抛出特定类型的异常。
  以下是在 [Jasmine](../J/jasmine.md) 测试中使用一些匹配器的示例：

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
  ```这些匹配器在 `expect` 函数中使用，并与正在测试的实际值链接。匹配器对于验证被测代码的行为至关重要。

- `toBe` ：检查实际值是否与预期值相同（===）。
  - `toEqual` ：检查实际值和预期值是否相等，包括对象和数组。
  - `toMatch` ：检查值是否与指定的正则表达式匹配。
  - `toBeDefined` ：断言变量不是
    `undefined`
    。

- `toBeUndefined` ：断言变量是
    `undefined`
    。

- `toBeNull` ：检查实际值是否为
    `null`
    。

- `toBeTruthy` ：断言实际值是真实的。
  - `toBeFalsy` ：断言实际值是假的。
  - `toContain` ：检查数组或字符串是否包含特定项目或子字符串。
  - `toBeLessThan` ：断言一个值小于另一个值。
  - `toBeGreaterThan` ：断言一个值大于另一个值。
  - `toBeCloseTo` ：检查一个数字是否在指定精度内接近另一个数字。
  - `toThrow` ：断言函数抛出异常。
  - `toThrowError` ：检查函数是否引发特定类型的异常。

### 间谍和嘲笑

#### 什么是 Jasmine 间谍以及如何使用它们？

[Jasmine](../J/jasmine.md) spies 是记录它们如何被调用的函数，允许您验证与它们的交互是否按预期发生。它们可用于跟踪函数是否被调用、调用次数、参数是什么以及返回什么。间谍还可以用于存根任何函数并模拟其行为。
  要创建间谍，您可以使用`spyOn`函数，传递对象和您想要监视的函数的名称：

  ```
  spyOn(someObject, 'someFunction');
  ```如果您需要创建一个没有现有函数的间谍，您可以使用 `jasmine.createSpy` 或 `jasmine.createSpyObj` 来实现多个函数：

  ```
  let mySpy = jasmine.createSpy('mySpy');
  let mySpies = jasmine.createSpyObj('mySpies', ['firstFunction', 'secondFunction']);
  ```当您想要通过用可控制和检查的间谍替换依赖函数来隔离工作单元时，间谍特别有用。当您想要阻止在测试期间执行函数的实际实现时，它们也很方便，特别是当它昂贵、缓慢或有副作用时。
  您可以使用 `.and.returnValue` 设置间谍以返回特定值：

  ```
  mySpy.and.returnValue(someValue);
  ```或者调用一个假函数：

  ```
  mySpy.and.callFake(() => {
    // Fake implementation
  });
  ```测试完成后，可以检查spy是否被正确调用：

  ```
  expect(mySpy).toHaveBeenCalled();
  expect(mySpy).toHaveBeenCalledWith(expectedArgs);
  ```间谍对于维护**测试隔离**并确保您的测试不受外部代码或副作用的影响至关重要。

#### 如何在 Jasmine 中创建模拟？

在 [Jasmine](../J/jasmine.md) 中创建模拟涉及使用 **spies** 来跟踪和控制函数、方法或对象的行为。这是分步指南：

1. **创建一个间谍**
    对于你想要模拟的函数
    `spyOn`
    。这将函数替换为可以跟踪调用、参数和设置返回值的间谍。

  ```
  spyOn(obj, 'methodName');
  ```

1. **配置间谍的行为**
    使用链接函数，例如
    `.and.returnValue()`
    ,
    `.and.callFake()`
    , 或
    `.and.throwError()`
    控制调用该方法时发生的情况。

  ```
  // Return a specific value
  spyOn(obj, 'methodName').and.returnValue('mocked value');
  // Provide a fake implementation
  spyOn(obj, 'methodName').and.callFake(() => 'fake implementation');
  // Throw an error
  spyOn(obj, 'methodName').and.throwError('error message');
  ```

1. **创建[Jasmine](../J/jasmine.md)间谍对象**
    使用多种方法模拟整个对象
    `jasmine.createSpyObj`
    。当您需要使用多种方法模拟对象时，这非常有用。

  ```
  let mockObject = jasmine.createSpyObj('mockObject', ['method1', 'method2']);
  ```

1. **设置返回值或实现**
    如果需要的话，获取间谍对象的方法。

  ```
  mockObject.method1.and.returnValue('value1');
  mockObject.method2.and.callFake(() => 'value2');
  ```

1. **集成模拟**
    进入您的测试，用模拟替换真实的实现。
  请记住，在 [Jasmine](../J/jasmine.md) 中使用间谍创建的模拟是临时的，将在每次测试后删除，以确保测试隔离。如果需要，使用 `beforeEach` 为每个测试设置模拟。

1. **创建一个间谍**
    对于你想要模拟的函数
    `spyOn`
    。这将函数替换为可以跟踪调用、参数和设置返回值的间谍。

1. **配置间谍的行为**
    使用链接函数，例如
    `.and.returnValue()`
    ,
    `.and.callFake()`
    , 或
    `.and.throwError()`
    控制调用该方法时发生的情况。

1. **创建[Jasmine](../J/jasmine.md)间谍对象**
    使用多种方法模拟整个对象
    `jasmine.createSpyObj`
    。当您需要使用多种方法模拟对象时，这非常有用。

1. **设置返回值或实现**
    如果需要的话，获取间谍对象的方法。

1. **集成模拟**
    进入您的测试，用模拟替换真实的实现。

#### Jasmine 中的间谍和模拟有什么区别？

在[Jasmine](../J/jasmine.md) 中，**spies** 和 **mocks** 用于不同的测试目的。
  **spy** 是一个记录有关其调用的信息的函数，例如调用了多少次、使用了哪些参数以及返回了哪些值。间谍还可以伪造返回值或错误，使您可以在不执行实际代码的情况下模拟行为。它们主要用于收集有关函数调用的信息，以验证函数是否被正确使用。

  ```
  spyOn(someObject, 'someMethod');
  ```另一方面，**模拟**是模仿真实对象的结构和行为的对象，具有预先编程的行为和期望。在[Jasmine](../J/jasmine.md) 中，通常使用间谍结合其他技术来创建模拟来模拟复杂的行为。当您需要测试与难以或不切实际的对象（例如 [API](../A/api.md) 或 [database](../D/database.md)）的交互时，模拟非常有用。

  ```
  const mock = jasmine.createSpyObj('mock', ['method1', 'method2']);
  mock.method1.and.returnValue('some value');
  ```总之，当您想要观察现有函数时，请使用 **spy**；当您需要为具有多个方法或属性的整个对象创建替代对象时，请使用 **mock**。两者都是 [test automation](../T/test-automation.md) 工程师工具包中用于隔离代码单元并验证系统不同部分之间交互的重要工具。

### 高级概念

#### Jasmine 中如何处理异步测试？

在[Jasmine](../J/jasmine.md) 中处理异步测试涉及使用`done` 回调、`async`/`await` 语法或`done.fail` 函数进行错误处理。
  **使用`done`回调：**
  [Jasmine](../J/jasmine.md) 提供了 `done` 函数，您可以调用该函数来发出异步测试或 [setup](../S/setup.md)/teardown 方法已完成的信号。将`done` 作为参数传递给`it`、`beforeEach` 或`afterEach` 函数，并在异步操作完成时调用它。

  ```
  it('should handle async operation', (done) => {
    setTimeout(() => {
      expect(true).toBe(true);
      done();
    }, 1000);
  });
  ```**使用`async`/`await`：**
  借助对现代 JavaScript 的支持，您可以使用`async`/`await` 获得更清晰的语法。将测试函数标记为`async`，并将其中的异步调用标记为`await`。

  ```
  it('should handle async operation with async/await', async () => {
    const result = await someAsyncFunction();
    expect(result).toBe(expectedValue);
  });
  ```**使用`done.fail`进行错误处理：**
  如果在异步操作期间发生错误，您可以使用 `done.fail` 将错误传递给 [Jasmine](../J/jasmine.md)，然后 [Jasmine](../J/jasmine.md) 将使测试失败并显示提供的错误消息。

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
  ```请记住处理超时并确保正确调用 `done` 以避免 [false positives](../F/false-positive.md) 测试通过，因为 `done` 从未被调用。

#### 如何将 Jasmine 与其他库或框架（如 Angular 或 React）一起使用？

将 [Jasmine](../J/jasmine.md) 与 **Angular** 或 **React** 等框架集成涉及设置 [test environment](../T/test-environment.md)，允许 [Jasmine](../J/jasmine.md) 与这些框架的组件或服务进行交互。
  对于 **Angular**，您可以使用 **Angular CLI** 生成带有测试 [setup](../S/setup.md) 的项目，其中包括 [Jasmine](../J/jasmine.md) 和 **Karma**。 Angular 的测试实用程序提供了独立测试组件和服务的方法。以下是如何测试组件的基本示例：

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
  ```对于 **React**，您通常会使用 **Enzyme** 或 **React 测试库** 以及 [Jasmine](../J/jasmine.md) 来渲染组件并处理它们与 DOM 的交互。您可以通过配置 [test runner](../T/test-runner.md)（如 Karma）来使用 React 设置 [Jasmine](../J/jasmine.md) 以使用 React 的 JSX 语法。这是使用 [Jasmine](../J/jasmine.md) 和 Enzyme 的简单 React 组件测试：

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
  ```在这两种情况下，您都需要配置 [test runner](../T/test-runner.md) 以使用属于项目堆栈一部分的特定构建工具和转译器（例如 **Webpack** 和 **Babel**）。这确保您的测试可以理解应用程序代码中使用的模块语法和 JSX（用于 React）。

#### 在 Jasmine 中编写测试的最佳实践有哪些？

在 [Jasmine](../J/jasmine.md) 中编写测试的最佳实践包括：

- **保持测试隔离**：确保每个测试可以独立运行，而不依赖于另一个测试的状态。使用`beforeEach` 和`afterEach` 设置和拆除[test environments](../T/test-environment.md)。
  - **编写描述性[test cases](../T/test-case.md)**：为`describe` 和`it` 块使用清晰的描述性名称来传达[test suite](../T/test-suite.md) 和各个测试的意图。
  - **DRY（不要重复）**：将常见的 [setup](../S/setup.md) 和拆卸步骤分解为 `beforeEach` 和 `afterEach` 块。使用辅助函数来执行重复性任务。
  - **根据规范测试一个方面**：每个 `it` 块应重点关注被测代码的单个行为或方面。
  - **使用行为驱动开发 ([BDD](../B/bdd.md)) 语言**：编写描述功能行为而不是实现细节的测试。
  - **具有明确期望的断言**：使用 [Jasmine](../J/jasmine.md) 匹配器编写易于阅读和理解的断言。可以为特定于域的断言创建自定义匹配器。
  - **正确处理异步代码**：使用[Jasmine](../J/jasmine.md) 的`done` 回调或返回一个承诺，以确保异步操作在评估期望之前完成。
  - **避免测试实现细节**：关注公共[API](../A/api.md)和预期结果，而不是功能或组件的内部工作原理。
  - **保持测试快速**：缓慢的测试可能会阻碍开发过程。优化测试以快速运行并避免不必要的复杂性。
  - **逻辑地构建测试**：使用嵌套的 `describe` 块对相关测试进行分组，以创建可读且可维护的测试层次结构。
  - **定期重构测试**：随着代码库的发展，重新访问和重构测试以确保它们保持有效并且不会变得不稳定或无关紧要。

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

- **保持测试隔离**：确保每个测试可以独立运行，而不依赖于另一个测试的状态。使用`beforeEach` 和`afterEach` 设置和拆除[test environments](../T/test-environment.md)。
  - **编写描述性[test cases](../T/test-case.md)**：为`describe` 和`it` 块使用清晰的描述性名称来传达[test suite](../T/test-suite.md) 和各个测试的意图。
  - **DRY（不要重复）**：将常见的 [setup](../S/setup.md) 和拆卸步骤分解为 `beforeEach` 和 `afterEach` 块。使用辅助函数来执行重复性任务。
  - **根据规范测试一个方面**：每个 `it` 块应重点关注被测代码的单个行为或方面。
  - **使用行为驱动开发 ([BDD](../B/bdd.md)) 语言**：编写描述功能行为而不是实现细节的测试。
  - **具有明确期望的断言**：使用 [Jasmine](../J/jasmine.md) 匹配器编写易于阅读和理解的断言。可以为特定于域的断言创建自定义匹配器。
  - **正确处理异步代码**：使用[Jasmine](../J/jasmine.md) 的`done` 回调或返回一个承诺，以确保异步操作在评估期望之前完成。
  - **避免测试实现细节**：关注公共 [API](../A/api.md) 和预期结果，而不是功能或组件的内部工作原理。
  - **保持测试快速**：缓慢的测试可能会阻碍开发过程。优化测试以快速运行并避免不必要的复杂性。
  - **逻辑地构建测试**：使用嵌套的 `describe` 块对相关测试进行分组，以创建可读且可维护的测试层次结构。
  - **定期重构测试**：随着代码库的发展，重新访问和重构测试以确保它们保持有效并且不会变得不稳定或无关紧要。
