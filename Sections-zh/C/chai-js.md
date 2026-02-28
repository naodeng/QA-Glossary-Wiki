# 柴.js

<!-- TOC START -->
- [相关术语：](#相关术语：)
  - [另请参阅：](#另请参阅：)
- [关于 Chai.js 有疑问吗？](#关于-chaijs-有疑问吗？)
  - [基础知识和重要性](#基础知识和重要性)
    - [Chai.js 是什么？](#chaijs-是什么？)
    - [为什么在测试中使用 Chai.js？](#为什么在测试中使用-chaijs？)
    - [Chai.js 的主要功能是什么？](#chaijs-的主要功能是什么？)
    - [Chai.js 与其他 JavaScript 测试库相比如何？](#chaijs-与其他-javascript-测试库相比如何？)
    - [使用 Chai.js 进行测试有哪些优势？](#使用-chaijs-进行测试有哪些优势？)
  - [安装和设置](#安装和设置)
    - [如何安装 Chai.js？](#如何安装-chaijs？)
    - [使用 Chai.js 有哪些先决条件？](#使用-chaijs-有哪些先决条件？)
    - [如何为项目设置 Chai.js？](#如何为项目设置-chaijs？)
    - [如何将 Chai.js 导入 JavaScript 文件？](#如何将-chaijs-导入-javascript-文件？)
  - [断言](#断言)
    - [Chai.js 中的断言是什么？](#chaijs-中的断言是什么？)
    - [如何在 Chai.js 中编写基本断言？](#如何在-chaijs-中编写基本断言？)
    - [Chai.js 中有哪些不同类型的断言可用？](#chaijs-中有哪些不同类型的断言可用？)
    - [如何断言 Chai.js 中的函数抛出错误？](#如何断言-chaijs-中的函数抛出错误？)
    - [如何在 Chai.js 中断言深度平等？](#如何在-chaijs-中断言深度平等？)
  - [插件](#插件)
    - [Chai.js 插件是什么？](#chaijs-插件是什么？)
    - [如何使用 Chai.js 插件？](#如何使用-chaijs-插件？)
    - [有哪些流行的 Chai.js 插件以及它们的作用是什么？](#有哪些流行的-chaijs-插件以及它们的作用是什么？)
    - [如何创建自己的 Chai.js 插件？](#如何创建自己的-chaijs-插件？)
  - [高级概念](#高级概念)
    - [如何将 Chai.js 与异步代码结合使用？](#如何将-chaijs-与异步代码结合使用？)
    - [如何将 Chai.js 与 Promises 结合使用？](#如何将-chaijs-与-promises-结合使用？)
    - [Chai.js 的 .should 接口是什么以及它是如何工作的？](#chaijs-的-should-接口是什么以及它是如何工作的？)
    - [如何自定义 Chai.js 的断言错误消息？](#如何自定义-chaijs-的断言错误消息？)
<!-- TOC END -->

Chai.js

，通常简称为 Chai，是

BDD

/TDD（行为驱动开发/

测试驱动开发

) 断言库

Node.js

和浏览器。它与流行的 JavaScript 测试框架无缝配对，例如 Mocha 和

茉莉花

。 Chai 为开发人员提供了以可读语言表达断言的能力，模仿自然语言结构。

## 相关术语：

- [Assertion library](../A/assertion-library.md)
- [Jest](../J/jest.md)
- [Jasmine](../J/jasmine.md)

### 另请参阅：

- [Official Website](https://www.chaijs.com/)

## 关于 Chai.js 有疑问吗？

### 基础知识和重要性

#### Chai.js 是什么？

[Chai.js](../C/chai-js.md) 是一个**行为驱动开发 ([BDD](../B/bdd.md))** / **[test-driven development](../T/test-driven-development.md) (TDD)** 断言库，适用于 [Node.js](../N/node-js.md) 和浏览器，可以与任何 JavaScript 测试框架完美搭配。它为开发人员提供了一组丰富的、可读且富有表现力的断言。
  [Chai.js](../C/chai-js.md) 提供三种不同风格的断言：**should**、**expect** 和 **assert**。每种样式都有自己的语法，允许开发人员选择最适合他们的偏好或项目需求的样式。

  ```
  // Should style
  should.exist(foo);
  // Expect style
  expect(foo).to.exist;
  // Assert style
  assert.exists(foo);
  ```[Chai.js](../C/chai-js.md) 断言可以处理各种测试条件，包括但不限于属性值、深度相等检查和引发的异常。它还支持使用回调和承诺来测试异步操作。
  该库可通过插件进行扩展，可以添加新的断言和测试条件以满足特定的测试要求。这种可扩展性使[Chai.js](../C/chai-js.md)能够适应各种[use cases](../U/use-case.md)并与其他工具和库集成。
  [Chai.js](../C/chai-js.md) 通常与其他测试工具（例如 Mocha、[Jest](../J/jest.md) 或 Karma）结合使用，提供完整的测试解决方案。它通过 npm 安装，可以轻松集成到任何 JavaScript 项目中，使其成为希望增强测试能力的开发人员的便捷选择。

#### 为什么在测试中使用 Chai.js？

[Chai.js](../C/chai-js.md) 用于测试主要是因为其在编写断言时的**灵活性**和**可读性**。它允许开发人员编写富有表现力且易于维护的测试。通过提供**行为驱动开发 ([BDD](../B/bdd.md))** 和 **[Test-Driven Development](../T/test-driven-development.md) (TDD)** 断言样式，它可以满足不同的偏好，并且可以轻松与 Mocha 或 [Jest](../J/jest.md) 等各种测试框架集成。
  [Chai.js](../C/chai-js.md) 的使用增强了**调试体验**，因为它提供了信息丰富的错误消息，其中详细说明了断言失败时的预期与 [actual result](../A/actual-result.md) 的情况。此功能显着减少了确定测试失败原因所花费的时间。
  此外，[Chai.js](../C/chai-js.md) 支持**可链接断言**，这使得能够以可读的方式组合复杂的条件。这种链接模仿自然语言，使新开发人员或非技术利益相关者更容易理解测试。
  [Chai.js](../C/chai-js.md) 通过插件的可扩展性允许定制和扩展其核心功能。这意味着团队可以使库适应他们的特定测试需求，而无需等待核心包提供这些功能。
  总之，选择 [Chai.js](../C/chai-js.md) 是因为它的**表达语法**、**有用的错误消息**、**与其他工具的兼容性**和**可扩展性**，所有这些都有助于提供更高效、更愉快的测试体验。

#### Chai.js 的主要功能是什么？

[Chai.js](../C/chai-js.md) 提供了一系列**关键功能**，使其成为[test automation](../T/test-automation.md) 的多功能且强大的断言库：

- **[BDD](../B/bdd.md)/TDD 断言样式**：Chai 提供两种主要的断言样式：**行为驱动开发 ([BDD](../B/bdd.md))** 使用 `expect` 或 `should`，以及 **[Test-Driven Development](../T/test-driven-development.md) (TDD)** 使用 `assert`。这使得开发人员可以选择最适合他们的测试理念的风格，或者在他们的[test suite](../T/test-suite.md) 中混合搭配。
  - **可链接语言**：可以使用自然语言结构将断言链接在一起以形成可读的语句。这提高了测试的可读性并使编写断言更加直观。
  - **类型检查**：Chai 包含用于类型检查的断言，例如 `expect(value).to.be.a('string')`，它通过确保值属于预期类型来增强测试的稳健性。
  - **属性测试**：它允许轻松检查对象属性，这对于测试 [API](../A/api.md) 响应和复杂的数据结构非常有用。
  - **相等和比较**：Chai 提供了一套全面的相等和比较断言，包括深度相等检查和大于/小于关系的断言。
  - **错误处理**：包含错误处理断言，允许开发人员断言某些函数在特定条件下抛出预期错误。
  - **插件架构**：Chai 通过插件的可扩展性意味着它可以适应各种 [use cases](../U/use-case.md) 并与其他库和工具集成。
  - **异步支持**：它内置了对测试异步代码的支持，包括 Promise，这对于现代 JavaScript 开发至关重要。
  - **自定义消息**：开发人员可以为断言提供自定义错误消息，这可以使调试失败的测试更容易、信息更丰富。
  - **跨平台**：[Chai.js](../C/chai-js.md) 可在 [Node.js](../N/node-js.md) 和浏览器环境中工作，使其适用于各种 JavaScript 项目。
  - **[BDD](../B/bdd.md)/TDD 断言样式**：Chai 提供两种主要的断言样式：**行为驱动开发 ([BDD](../B/bdd.md))** 与 `expect` 或 `should`，以及 **[Test-Driven Development](../T/test-driven-development.md) (TDD)** 与 `assert`。这使得开发人员可以选择最适合他们的测试理念的风格，或者在他们的[test suite](../T/test-suite.md) 中混合搭配。
  - **可链接语言**：可以使用自然语言结构将断言链接在一起以形成可读的语句。这提高了测试的可读性并使编写断言更加直观。
  - **类型检查**：Chai 包含用于类型检查的断言，例如 `expect(value).to.be.a('string')`，它通过确保值属于预期类型来增强测试的稳健性。
  - **属性测试**：它允许轻松检查对象属性，这对于测试 [API](../A/api.md) 响应和复杂的数据结构非常有用。
  - **相等和比较**：Chai 提供了一套全面的相等和比较断言，包括深度相等检查和大于/小于关系的断言。
  - **错误处理**：包含错误处理断言，允许开发人员断言某些函数在特定条件下抛出预期错误。
  - **插件架构**：Chai 通过插件的可扩展性意味着它可以适应各种 [use cases](../U/use-case.md) 并与其他库和工具集成。
  - **异步支持**：它内置了对测试异步代码的支持，包括 Promise，这对于现代 JavaScript 开发至关重要。
  - **自定义消息**：开发人员可以为断言提供自定义错误消息，这可以使调试失败的测试更容易、信息更丰富。
  - **跨平台**：[Chai.js](../C/chai-js.md) 可在 [Node.js](../N/node-js.md) 和浏览器环境中工作，使其适用于各种 JavaScript 项目。

#### Chai.js 与其他 JavaScript 测试库相比如何？

[Chai.js](../C/chai-js.md) 因其**灵活的断言样式**而在 JavaScript 测试领域脱颖而出：[BDD](../B/bdd.md)（期望/应该）和 TDD（断言）。这种适应性允许开发人员选择最适合他们的偏好或现有代码库的样式。
  与**[Jest](../J/jest.md)**（提供自己的断言的成熟测试框架）相比，Chai 更像是一个断言库，可以与 Mocha 或 [Jasmine](../J/jasmine.md) 等任何测试框架配合使用。 [Jest](../J/jest.md) 的断言是内置的，不能脱离框架，而 Chai 的断言是独立的，可以通过插件扩展。
  **[Jasmine](../J/jasmine.md)** 带有自己的断言库，因此将 Chai 与 [Jasmine](../J/jasmine.md) 一起使用是出于偏好原因而不是必要。 Chai 可能因其更丰富的插件生态系统或 [Jasmine](../J/jasmine.md) 中未找到的特定断言风格而被选中。
  **Mocha** 没有附带断言库，这使得 Chai 成为 Mocha 用户的热门选择。 Mocha 的测试运行能力和 Chai 的断言相结合，提供了强大而灵活的测试[setup](../S/setup.md)。
  **Sinon** 经常与 Chai 一起用于间谍、模拟和存根。虽然Sinon有一些断言，但主要集中在这三个领域，而Chai用于更一般的断言。 `sinon-chai` 插件允许将Sinon 的功能与Chai 的断言语法无缝集成。
  综上所述，[Chai.js](../C/chai-js.md)的主要比较点是其**灵活的语法**和**通过插件的扩展性**，使其能够与各种测试框架很好地集成，并补充像Sinon这样的库来满足全面的测试需求。

#### 使用 Chai.js 进行测试有哪些优势？

[Chai.js](../C/chai-js.md) 为 [test automation](../T/test-automation.md) 提供了多项优势：

- **流畅且可读的语法**：Chai 的可链接语言结构使测试更易于阅读和编写。其 [BDD](../B/bdd.md)/TDD 风格断言为 [test cases](../T/test-case.md) 提供了清晰的语言。
  - **灵活性**：通过 `expect`、`should` 和 `assert` 等接口，Chai 可以适应不同的测试风格和偏好。
  - **可扩展性**：可以创建自定义插件或使用现有插件来扩展 Chai 的功能，从而允许根据特定需求定制更专业的断言。
  - **兼容性**：与 Mocha、[Jest](../J/jest.md) 和 Karma 等各种测试框架无缝协作，使其适用于不同环境。
  - **丰富的断言库**：提供各种开箱即用的断言，减少了为测试编写复杂逻辑的需要。
  - **跨平台**：可在[Node.js](../N/node-js.md)和浏览器环境中使用，确保跨平台测试的一致性。
  - **社区支持**：大型社区和生态系统意味着更好的支持、持续改进以及丰富的故障排除资源。
  - **错误处理**：提供详细的错误消息，其中可以包括堆栈跟踪，使调试更容易。
  - **异步支持**：内置支持使用 Promises 和 async/await 模式测试异步代码。
  通过利用这些优势，[Chai.js](../C/chai-js.md) 增强了[test suites](../T/test-suite.md) 的效率、可读性和[maintainability](../M/maintainability.md)，从而有助于实现更加稳健和可靠的自动化流程。

- **流畅且可读的语法**：Chai 的可链接语言结构使测试更易于阅读和编写。其 [BDD](../B/bdd.md)/TDD 风格断言为 [test cases](../T/test-case.md) 提供了清晰的语言。
  - **灵活性**：通过 `expect`、`should` 和 `assert` 等接口，Chai 可以适应不同的测试风格和偏好。
  - **可扩展性**：可以创建自定义插件或使用现有插件来扩展 Chai 的功能，从而允许根据特定需求定制更专业的断言。
  - **兼容性**：与 Mocha、[Jest](../J/jest.md) 和 Karma 等各种测试框架无缝协作，使其适用于不同环境。
  - **丰富的断言库**：提供各种开箱即用的断言，减少了为测试编写复杂逻辑的需要。
  - **跨平台**：可在[Node.js](../N/node-js.md)和浏览器环境中使用，确保跨平台测试的一致性。
  - **社区支持**：大型社区和生态系统意味着更好的支持、持续改进以及丰富的故障排除资源。
  - **错误处理**：提供详细的错误消息，其中可以包括堆栈跟踪，使调试更容易。
  - **异步支持**：内置支持使用 Promises 和 async/await 模式测试异步代码。

### 安装和设置

#### 如何安装 Chai.js？

要安装 **[Chai.js](../C/chai-js.md)**，请确保已安装 **[Node.js](../N/node-js.md)** 和 **npm**（节点包管理器）。打开终端或命令提示符并导航到您的项目目录。运行以下命令：

  ```
  npm install chai --save-dev
  ```此命令将 [Chai.js](../C/chai-js.md) 作为开发依赖项安装，并将其添加到 `package.json` 文件中。安装完成后，您可以使用以下命令将 Chai 导入到测试文件中：
  对于 CommonJS 模块：

  ```
  const chai = require('chai');
  ```对于 ES6 模块：

  ```
  import chai from 'chai';
  ```然后，您可以使用 Chai 的 `expect`、`should` 或 `assert` 接口来编写测试。如果您还没有安装，请记住还要安装[test runner](../T/test-runner.md)，如 **Mocha** 或 **[Jest](../J/jest.md)**，因为 Chai 是一个断言库，本身不提供测试框架。

#### 使用 Chai.js 有哪些先决条件？

要使用 **[Chai.js](../C/chai-js.md)**，请确保满足以下先决条件：

- **[Node.js](../N/node-js.md)** ：Chai 是一个 Node.js 库，因此您需要在系统上安装 Node.js。该版本应与您计划使用的 Chai 版本兼容。
  - **NPM 或 Yarn** ：这些是处理 Chai 及其依赖项的安装的包管理器。他们还管理特定于项目的包。
  - **A [test runner](../T/test-runner.md)** ：Chai 是一个断言库，不包含测试运行程序。您需要像 Mocha、Jest 或 Karma 这样的测试运行程序来执行您的测试。
  - **项目[setup](../S/setup.md)** ：您的项目应该使用
    `package.json`
    文件（如果您使用的是 NPM 或 Yarn）。该文件跟踪与您的项目相关的依赖项和脚本。

- **JavaScript 知识**：由于 Chai 是一个 JavaScript 库，因此对 JavaScript（包括 ES6 功能）的良好理解至关重要。
  - **理解测试概念**：熟悉单元测试、测试驱动开发 (TDD) 和行为驱动开发 (BDD) 是有益的，因为 Chai 支持这些测试方法。
  要安装 Chai，请在项目目录中运行以下命令：

  ```
  npm install chai --save-dev
  ```或者，如果您使用的是 Yarn：

  ```
  yarn add chai --dev
  ```安装后，您可以使用以下命令将 Chai 导入到测试文件中：

  ```
  const chai = require('chai');
  ```或者，如果您使用 ES6 模块：

  ```
  import chai from 'chai';
  ```确保您的 [test environment](../T/test-environment.md) 已正确配置为将 Chai 与您选择的 [test runner](../T/test-runner.md) 和断言样式（`expect`、`should` 或 `assert`）结合使用。

- **[Node.js](../N/node-js.md)** ：Chai 是一个 Node.js 库，因此您需要在系统上安装 Node.js。该版本应与您计划使用的 Chai 版本兼容。
  - **NPM 或 Yarn** ：这些是处理 Chai 及其依赖项的安装的包管理器。他们还管理特定于项目的包。
  - **A [test runner](../T/test-runner.md)** ：Chai 是一个断言库，不包含测试运行程序。您需要像 Mocha、Jest 或 Karma 这样的测试运行程序来执行您的测试。
  - **项目[setup](../S/setup.md)** ：您的项目应该使用
    `package.json`
    文件（如果您使用的是 NPM 或 Yarn）。该文件跟踪与您的项目相关的依赖项和脚本。

- **JavaScript 知识**：由于 Chai 是一个 JavaScript 库，因此对 JavaScript（包括 ES6 功能）的良好理解至关重要。
  - **理解测试概念**：熟悉单元测试、测试驱动开发 (TDD) 和行为驱动开发 (BDD) 是有益的，因为 Chai 支持这些测试方法。

#### 如何为项目设置 Chai.js？

要为您的项目设置 [Chai.js](../C/chai-js.md)，请按照以下步骤操作：

1. **使用 npm 或 YARN 安装 Chai**（如果尚未安装）：
    或

    ```
    npm install chai --save-dev
    ```

    ```
    yarn add chai --dev
    ```

2. **在测试文件中导入 Chai**：

    ```
    const chai = require('chai');
    ```

3. **选择并设置断言样式**。 Chai 提供`should`、`expect` 和`assert` 样式。例如，要使用`expect`，您可以编写：

    ```
    const expect = chai.expect;
    ```

4. **使用所选的断言样式编写测试**。这是使用 `expect` 的简单测试示例：

    ```
    expect(2 + 2).to.equal(4);
    ```

5. **使用您选择的[test runner](../T/test-runner.md)（例如，Mocha、[Jest](../J/jest.md)）运行测试**。
  6. 或者，如果需要，**使用其他设置配置 Chai**，例如使用插件或向断言添加自定义消息。
  7. **将 Chai 与其他工具集成**，例如 [test runners](../T/test-runner.md) 或测试环境所需的模拟库。
  请记住**检查项目的依赖项**以确保它们与您正在使用的 Chai 版本兼容。保持 Chai 和所有插件更新，以受益于最新功能和[bug](../B/bug.md) 修复。

1. **使用 npm 或 YARN 安装 Chai**（如果尚未安装）：
    或

    ```
    npm install chai --save-dev
    ```

    ```
    yarn add chai --dev
    ```

2. **在测试文件中导入 Chai**：

    ```
    const chai = require('chai');
    ```

3. **选择并设置断言样式**。 Chai 提供`should`、`expect` 和`assert` 样式。例如，要使用`expect`，您可以编写：

    ```
    const expect = chai.expect;
    ```

4. **使用所选的断言样式编写测试**。这是使用 `expect` 的简单测试示例：

    ```
    expect(2 + 2).to.equal(4);
    ```

5. **使用您选择的[test runner](../T/test-runner.md)（例如，Mocha、[Jest](../J/jest.md)）运行测试**。
  6. 或者，如果需要，**使用其他设置配置 Chai**，例如使用插件或向断言添加自定义消息。
  7. **将 Chai 与其他工具集成**，如 [test runners](../T/test-runner.md) 或测试环境所需的模拟库。

#### 如何将 Chai.js 导入 JavaScript 文件？

要将 [Chai.js](../C/chai-js.md) 导入 JavaScript 文件，首先确保您的项目中安装了 Chai。如果尚未安装，您可以使用 npm 等包管理器以及命令 `npm install chai` 添加它。
  安装 Chai 后，您可以使用 CommonJS 或 ES6 模块语法将其导入 JavaScript 文件，具体取决于您的环境和项目 [setup](../S/setup.md)。
  对于 **CommonJS**（通常在 [Node.js](../N/node-js.md) 环境中使用），请使用 `require` 函数：

  ```
  const chai = require('chai');
  const expect = chai.expect;
  ```对于 **ES6 模块**（可能在具有支持 ES6 模块的构建系统的前端项目中使用），请使用 `import` 语句：

  ```
  import chai from 'chai';
  const expect = chai.expect;
  ```导入后，您可以使用 Chai 的断言方法（例如 `expect`、`should` 或 `assert`）来编写测试。
  如果您使用 **TypeScript**，则可以以类似的方式导入 Chai，但您可能还需要安装 Chai 的类型定义：

  ```
  npm install @types/chai
  ```然后，在您的 TypeScript 文件中：

  ```
  import * as chai from 'chai';
  const expect = chai.expect;
  ```如果您使用 `import` 语句，请记住将 TypeScript 编译器配置为识别 ES6 语法。

### 断言

#### Chai.js 中的断言是什么？

[Chai.js](../C/chai-js.md) 中的 **断言** 是计算测试中的表达式或值的语句。它检查该表达式或值是否满足某些条件，如果不满足，则断言将失败，从而导致测试失败。断言是[test suites](../T/test-suite.md) 的核心组件，因为它们验证被测代码的行为。
  Chai 提供了多种断言样式，但无论哪种样式，断言通常都包含三个部分：

1. **实际值** ：您正在测试的值，来自您的代码。
  2. **期望值**：您在测试中定义的期望值。
  3. **匹配器函数**：将实际值与期望值进行比较的函数。
  以下是使用 Chai 的 `expect` 接口的简单断言示例：

  ```
  const expect = require('chai').expect;
  expect(2 + 2).to.equal(4);
  ```在本例中，`2 + 2` 是实际值，`4` 是期望值，`.to.equal` 是匹配器函数。
  Chai 断言可以链接起来执行更复杂的检查：

  ```
  expect([1, 2, 3]).to.include(2).and.to.have.lengthOf(3);
  ```这里，`.include(2)` 检查数组是否包含数字 2，`.have.lengthOf(3)` 检查数组的长度是否为 3。`.and` 链用于组合同一主题的多个断言。
  断言对于验证代码是否按预期运行至关重要，并且是使用 [Chai.js](../C/chai-js.md) 编写有效且可靠的测试的基本部分。

1. **实际值** ：您正在测试的值，来自您的代码。
  2. **期望值**：您在测试中定义的期望值。
  3. **匹配器函数**：将实际值与期望值进行比较的函数。

#### 如何在 Chai.js 中编写基本断言？

要在 [Chai.js](../C/chai-js.md) 中编写基本断言，您可以使用其任何接口：`expect`、`should` 或 `assert`。以下是使用 `expect` 接口的示例：

  ```
  const expect = require('chai').expect;
  describe('Array', function() {
    describe('#indexOf()', function() {
      it('should return -1 when the value is not present', function() {
        expect([1, 2, 3].indexOf(4)).to.equal(-1);
      });
    });
  });
  ```在此示例中，`expect` 函数用于对`[1, 2, 3].indexOf(4)` 的结果进行断言。 `.to.equal(-1)` 链是实际的断言，表明[expected result](../E/expected-result.md) 应该是`-1`。
  对于 `should` 接口，语法会略有不同：

  ```
  const should = require('chai').should();
  describe('Array', function() {
    describe('#indexOf()', function() {
      it('should return -1 when the value is not present', function() {
        [1, 2, 3].indexOf(4).should.equal(-1);
      });
    });
  });
  ```对于 `assert` 接口，它更传统并且不使用链接：

  ```
  const assert = require('chai').assert;
  describe('Array', function() {
    describe('#indexOf()', function() {
      it('should return -1 when the value is not present', function() {
        assert.equal([1, 2, 3].indexOf(4), -1);
      });
    });
  });
  ```这些示例中的每一个都完成相同的事情：它们断言 `indexOf` 方法在使用数组中不存在的值调用时返回 `-1`。选择最适合您的编码风格或团队标准的界面。

#### Chai.js 中有哪些不同类型的断言可用？

[Chai.js](../C/chai-js.md) 提供三种断言样式：**should**、**expect** 和 **assert**。每种风格都提供了多种断言来测试不同的条件：
  ### 应该和期望
  这些[BDD](../B/bdd.md)（行为驱动开发）样式在功能上相似，但在语法上有所不同。它们提供了一种可链接的语言来构造断言。

- **.equal(value)** ：断言严格相等（
    `===`
    ）。

- **.eql(value)** ：断言深度相等。
  - **.above(value)** ：断言数字大于值。
  - **.least(value)** ：断言 number 至少等于 value。
  - **.below(value)** ：断言数字小于值。
  - **.most(value)** ：断言 number 至多等于 value。
  - **.instanceOf(constructor)** ：断言构造函数的实例。
  - **.property(name, [value])** ：断言对象有一个属性，可以选择有一个值。
  - **.ownProperty(name)** ：断言对象有自己的属性。
  - **.lengthOf(value)** ：断言数组或字符串的长度。
  - **.match(regex)** ：断言值与正则表达式匹配。
  - **.contain(value)** ：断言数组包含一个值。
  - **.ok** ：断言真实性。
  - **.true** ：断言严格等于
    `true`
    。

- **.false** ：断言严格等于
    `false`
    。

- **.null** ：断言严格等于
    `null`
    。

- **.undefined** ：断言严格等于
    `undefined`
    。

- **.NaN** ：断言值为
    `NaN`
    。

- **.exist** ：断言非空且非未定义。
  - **.empty** ：断言空数组、字符串或对象。
  ### 断言
  TDD ([Test-Driven Development](../T/test-driven-development.md)) 风格使用更传统的断言方法，无需可链接语言。

- **assert.equal(actual, Expected)** : 断言松散相等 (
    `==`
    ）。

- **assert.strictEqual(actual, Expected)** : 断言严格相等 (
    `===`
    ）。

- **assert.deepEqual(actual, Expected)** ：断言深度相等。
  - **assert.isAbove(valueToCheck, valueToBeAbove)** ：断言数量大于值。
  - **assert.isAtLeast(valueToCheck, valueToBeAtLeast)** ：断言数量至少等于值。
  - **assert.isBelow(valueToCheck, valueToBeBelow)** ：断言数量小于值。
  - **assert.isAtMost(valueToCheck, valueToBeAtMost)** ：断言数量最多等于值。
  - **assert.instanceOf(object, constructor)** ：断言构造函数的实例。
  - **assert.property(object, property)** ：断言对象有一个属性。
  - **assert.lengthOf(object, length)** ：断言数组或字符串的长度。
  - **assert.match(value, regex)** ：断言值与正则表达式匹配。
  - **assert.containsAllKeys(object, keys)** ：断言对象包含所有提供的键。
  - **assert.ok(value)** ：断言真实性。
  - **assert.isTrue(value)** ：断言严格等于
    `true`
    。

- **assert.isFalse(value)** ：断言严格等于
    `false`
    。

- **assert.isNull(value)** ：断言严格等于
    `null`
    。

- **assert.isUndefined(value)** ：断言严格等于
    `undefined`
    。

- **assert.isNaN(value)** ：断言值为
    `NaN`
    。

- **assert.exists(value)** ：断言非空且非未定义。
  - **assert.isEmpty(value)** ：断言空数组、字符串或对象。
  每个断言类型都满足特定的测试需求，允许进行全面且可读的测试。

- **.equal(value)** ：断言严格相等（
    `===`
    ）。

- **.eql(value)** ：断言深度相等。
  - **.above(value)** ：断言数字大于值。
  - **.least(value)** ：断言 number 至少等于 value。
  - **.below(value)** ：断言数字小于值。
  - **.most(value)** ：断言 number 至多等于 value。
  - **.instanceOf(constructor)** ：断言构造函数的实例。
  - **.property(name, [value])** ：断言对象有一个属性，可以选择有一个值。
  - **.ownProperty(name)** ：断言对象有自己的属性。
  - **.lengthOf(value)** ：断言数组或字符串的长度。
  - **.match(regex)** ：断言值与正则表达式匹配。
  - **.contain(value)** ：断言数组包含一个值。
  - **.ok** ：断言真实性。
  - **.true** ：断言严格等于
    `true`
    。

- **.false** ：断言严格等于
    `false`
    。

- **.null** ：断言严格等于
    `null`
    。

- **.undefined** ：断言严格等于
    `undefined`
    。

- **.NaN** ：断言值为
    `NaN`
    。

- **.exist** ：断言非空且非未定义。
  - **.empty** ：断言空数组、字符串或对象。
  - **assert.equal(actual, Expected)** : 断言松散相等 (
    `==`
    ）。

- **assert.strictEqual(actual, Expected)** : 断言严格相等 (
    `===`
    ）。

- **assert.deepEqual(actual, Expected)** ：断言深度相等。
  - **assert.isAbove(valueToCheck, valueToBeAbove)** ：断言数量大于值。
  - **assert.isAtLeast(valueToCheck, valueToBeAtLeast)** ：断言数量至少等于值。
  - **assert.isBelow(valueToCheck, valueToBeBelow)** ：断言数量小于值。
  - **assert.isAtMost(valueToCheck, valueToBeAtMost)** ：断言数量最多等于值。
  - **assert.instanceOf(object, constructor)** ：断言构造函数的实例。
  - **assert.property(object, property)** ：断言对象有一个属性。
  - **assert.lengthOf(object, length)** ：断言数组或字符串的长度。
  - **assert.match(value, regex)** ：断言值与正则表达式匹配。
  - **assert.containsAllKeys(object, keys)** ：断言对象包含所有提供的键。
  - **assert.ok(value)** ：断言真实性。
  - **assert.isTrue(value)** ：断言严格等于
    `true`
    。

- **assert.isFalse(value)** ：断言严格等于
    `false`
    。

- **assert.isNull(value)** ：断言严格等于
    `null`
    。

- **assert.isUndefined(value)** ：断言严格等于
    `undefined`
    。

- **assert.isNaN(value)** ：断言值为
    `NaN`
    。

- **assert.exists(value)** ：断言非空且非未定义。
  - **assert.isEmpty(value)** ：断言空数组、字符串或对象。

#### 如何断言 Chai.js 中的函数抛出错误？

要断言函数在 [Chai.js](../C/chai-js.md) 中引发错误，您可以使用 `expect` 或 `should` 接口中的 `throw` 或 `throws` 方法。以下是使用这两个界面执行此操作的方法：
  **使用`expect`接口：**

  ```
  const expect = require('chai').expect;
  expect(functionUnderTest).to.throw(ExpectedError);
  expect(functionUnderTest).to.throw("Error message");
  expect(functionUnderTest).to.throw(ExpectedError, "Error message");
  expect(functionUnderTest).to.throw(/Error message regex/);
  ```**使用`should`接口：**

  ```
  const should = require('chai').should();
  functionUnderTest.should.throw(ExpectedError);
  functionUnderTest.should.throw("Error message");
  functionUnderTest.should.throw(ExpectedError, "Error message");
  functionUnderTest.should.throw(/Error message regex/);
  ```将 `functionUnderTest` 替换为您正在测试的函数，将 `ExpectedError` 替换为您期望抛出的错误构造函数。如果您要检查特定的错误消息，则可以传递字符串或正则表达式来与错误消息进行匹配。
  **例子：**

  ```
  function willThrow() {
    throw new Error('This is an error!');
  }
  // Using expect
  expect(willThrow).to.throw(Error, 'This is an error!');
  // Using should
  willThrow.should.throw(Error, 'This is an error!');
  ```确保函数被传递而不是直接调用它；否则，Chai 不会捕获该错误，并且断言将会失败。

#### 如何在 Chai.js 中断言深度平等？

要断言[Chai.js](../C/chai-js.md) 中的深度相等，请使用`.deep` 链，后跟`.equal` 或`.eql` 断言。这将在考虑所有嵌套属性的情况下，在目标和预期对象之间执行深度比较。
  以下是使用 `expect` 接口的示例：

  ```
  const expect = require('chai').expect;
  const actual = { a: 1, b: { c: 3 } };
  const expected = { a: 1, b: { c: 3 } };
  expect(actual).to.deep.equal(expected);
  ```或者，使用 `should` 接口：

  ```
  const should = require('chai').should();
  const actual = { a: 1, b: { c: 3 } };
  const expected = { a: 1, b: { c: 3 } };
  actual.should.deep.equal(expected);
  ```对于数组，`deep.equal` 也有效：

  ```
  expect([1, 2, [3, 4]]).to.deep.equal([1, 2, [3, 4]]);
  ```请记住，如果没有`.deep` 链，`equal` 断言将检查严格相等性（使用`===`），这不适合比较对象或数组的内容。

### 插件

#### Chai.js 插件是什么？

[Chai.js](../C/chai-js.md) 插件扩展了 Chai 断言库的功能，允许根据特定测试需求定制更专业或更复杂的断言。它们与 Chai 现有的[API](../A/api.md) 无缝集成，通过附加方法和属性丰富了它。
  要使用 [Chai.js](../C/chai-js.md) 插件，您通常在 Chai 之后需要它，然后使用 `use` 方法将其添加到您的 Chai [setup](../S/setup.md) 中：

  ```
  const chai = require('chai');
  const somePlugin = require('chai-some-plugin');
  chai.use(somePlugin);
  ```**流行插件**包括：

- `chai-http` ：启用 HTTP 断言，使测试 Web 服务变得容易。
  - `chai-as-promised` ：简化在断言中使用 Promise 的过程。
  - `chai-dom` ：为 DOM 元素提供断言，在浏览器或基于 DOM 的测试中很有用。
  - `sinon-chai` ：为Sinon.js 间谍、存根和模拟提供断言，集成两个库。
  创建**自定义 [Chai.js](../C/chai-js.md) 插件**涉及定义导出函数的模块。此函数应接受 Chai 实例，并应使用 Chai 的 [API](../A/api.md) 添加新方法或属性：

  ```
  module.exports = function (chai, utils) {
    const Assertion = chai.Assertion;
    Assertion.addMethod('myAssertion', function (expected) {
      // Custom assertion logic here
    });
  };
  ```插件对于使 Chai 适应新框架、库或特定项目要求特别有用，使其成为[test automation](../T/test-automation.md) 工程师武器库中的强大工具。

- `chai-http` ：启用 HTTP 断言，使测试 Web 服务变得容易。
  - `chai-as-promised` ：简化在断言中使用 Promise 的过程。
  - `chai-dom` ：为 DOM 元素提供断言，在浏览器或基于 DOM 的测试中很有用。
  - `sinon-chai` ：为Sinon.js 间谍、存根和模拟提供断言，集成两个库。

#### 如何使用 Chai.js 插件？

要使用 [Chai.js](../C/chai-js.md) 插件，请按照以下步骤操作：

1. **通过npm或yarn安装**插件，例如：

    ```
    npm install chai-http
    ```

2. **导入**测试文件中的插件：

    ```
    const chai = require('chai');
    const chaiHttp = require('chai-http');
    ```

3. **使用** `chai` 对象上的 `use` 方法来添加插件：

    ```
    chai.use(chaiHttp);
    ```

4. 添加插件后，您可以在测试中**利用其方法**。例如，使用 `chai-http` 您可以发出 HTTP 请求：

    ```
    chai.request('http://example.com')
        .get('/')
        .end((err, res) => {
            expect(res).to.have.status(200);
        });
    ```请记住**阅读插件的文档**以获取具体的使用说明，因为每个插件可能会引入独特的方法或语法。
  下面是一个使用 `chai-as-promised` 处理 Promise 的简短示例：

1. **安装**插件：

    ```
    npm install chai-as-promised
    ```

2. **导入**并**使用**插件：

    ```
    const chai = require('chai');
    const chaiAsPromised = require('chai-as-promised');
    chai.use(chaiAsPromised);
    ```

3. **为 Promise 编写断言**：

    ```
    const expect = chai.expect;
    const promise = returnsAPromise(); // some function that returns a promise
    // Now you can use Chai as Promised for assertions
    expect(promise).to.eventually.equal('expected value');
    ```通过执行这些步骤，您可以扩展 Chai 的功能并根据项目的需求定制测试套件。

1. **通过npm或yarn安装**插件，例如：

    ```
    npm install chai-http
    ```

2. **导入**测试文件中的插件：

    ```
    const chai = require('chai');
    const chaiHttp = require('chai-http');
    ```

3. **使用** `chai` 对象上的 `use` 方法来添加插件：

    ```
    chai.use(chaiHttp);
    ```

4. 添加插件后，您可以在测试中**利用其方法**。例如，使用 `chai-http` 您可以发出 HTTP 请求：

    ```
    chai.request('http://example.com')
        .get('/')
        .end((err, res) => {
            expect(res).to.have.status(200);
        });
    ```

1. **安装**插件：

    ```
    npm install chai-as-promised
    ```

2. **导入**并**使用**插件：

    ```
    const chai = require('chai');
    const chaiAsPromised = require('chai-as-promised');
    chai.use(chaiAsPromised);
    ```

3. **为 Promise 编写断言**：

    ```
    const expect = chai.expect;
    const promise = returnsAPromise(); // some function that returns a promise
    // Now you can use Chai as Promised for assertions
    expect(promise).to.eventually.equal('expected value');
    ```

#### 有哪些流行的 Chai.js 插件以及它们的作用是什么？

[Chai.js](../C/chai-js.md) 拥有丰富的插件生态系统，可扩展其核心功能。以下是一些受欢迎的：

- **chai-as-promised** ：简化 Promise 的使用。它允许您以更具表现力的方式处理异步操作的断言。

    ```
    expect(promise).to.eventually.equal('foo');
    ```

- **chai-http** ：对于 HTTP 集成测试很有用。它允许您向 HTTP 服务器发送请求并断言响应。

    ```
    chai.request(app).get('/').end((err, res) => {
      expect(res).to.have.status(200);
    });
    ```

- **sinon-chai** ：为Sinon.js spies、stubs和mocks提供一组断言，使得使用测试替身更容易。

    ```
    expect(spy).to.have.been.calledOnce;
    ```

- **chai-dom** ：使用 DOM 操作断言扩展 Chai，使其成为基于浏览器的测试的不错选择。

    ```
    expect(element).to.have.text('hello');
    ```

- **chai-enzyme**：专为使用 Enzyme 进行 React.js 测试而定制。它为组件属性、状态和渲染添加了特定于酶的断言。

    ```
    expect(wrapper).to.have.className('foo');
    ```

- **chai-jquery** ：将 Chai 与 jQuery 集成，为 jQuery 对象（例如 CSS、属性和事件）提供断言。

    ```
    expect($el).to.have.css('display', 'none');
    ```

- **chai-subset** ：允许您断言一个对象是否是另一个对象的一部分，对于测试 API 响应很有用。

    ```
    expect(result).to.containSubset({ name: 'foo' });
    ```

- **dirty-chai** ：提供一种将 Chai 断言用作函数而不是属性的方法，这对于 linting 目的很有帮助。

    ```
    expect(foo).to.be.a.function();
    ```每个插件都旨在满足特定的测试需求和场景，增强 Chai 断言的表现力和力量。

- **chai-as-promised** ：简化 Promise 的使用。它允许您以更具表现力的方式处理异步操作的断言。

    ```
    expect(promise).to.eventually.equal('foo');
    ```

- **chai-http** ：对于 HTTP 集成测试很有用。它允许您向 HTTP 服务器发送请求并断言响应。

    ```
    chai.request(app).get('/').end((err, res) => {
      expect(res).to.have.status(200);
    });
    ```

- **sinon-chai** ：为Sinon.js spies、stubs和mocks提供一组断言，使得使用测试替身更容易。

    ```
    expect(spy).to.have.been.calledOnce;
    ```

- **chai-dom** ：使用 DOM 操作断言扩展 Chai，使其成为基于浏览器的测试的不错选择。

    ```
    expect(element).to.have.text('hello');
    ```

- **chai-enzyme**：专为使用 Enzyme 进行 React.js 测试而定制。它为组件属性、状态和渲染添加了特定于酶的断言。

    ```
    expect(wrapper).to.have.className('foo');
    ```

- **chai-jquery** ：将 Chai 与 jQuery 集成，为 jQuery 对象（例如 CSS、属性和事件）提供断言。

    ```
    expect($el).to.have.css('display', 'none');
    ```

- **chai-subset** ：允许您断言一个对象是否是另一个对象的一部分，对于测试 API 响应很有用。

    ```
    expect(result).to.containSubset({ name: 'foo' });
    ```

- **dirty-chai** ：提供一种将 Chai 断言用作函数而不是属性的方法，这对于 linting 目的很有帮助。

    ```
    expect(foo).to.be.a.function();
    ```

#### 如何创建自己的 Chai.js 插件？

创建您自己的 [Chai.js](../C/chai-js.md) 插件涉及使用新的断言或行为来扩展 Chai。请按照下列步骤操作：

1. **使用 `npm init` 为您的插件初始化一个新项目**，并将 Chai 安装为对等依赖项。
  2. **为您的插件创建一个主文件**，例如`chai-myplugin.js`。
  3. **通过导出 Chai 将用来安装插件的函数来定义您的插件**：

  ```
  module.exports = function(chai, utils) {
    // Plugin code goes here
  };
  ```

1. **添加方法或属性**
    到柴家
    `Assertion`
    对象。使用
    `utils.addMethod`
    对于新的断言方法或
    `utils.addProperty`
    对于新属性：

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

1. **彻底测试您的插件**。使用 Mocha 或其他测试框架创建 [test cases](../T/test-case.md) 以确保您的断言按预期工作。
  2. **记录您的插件**。清楚地解释如何安装和使用您的插件，包括断言的示例。
  3. **将您的插件**发布到 npm 以供其他人使用。在发布之前，使用有关您的插件的详细信息更新 `package.json` 文件。
  要使用您的插件，用户需要通过 npm 安装它并在测试文件中使用`chai.use()`：

  ```
  var chai = require('chai');
  var myPlugin = require('chai-myplugin');
  chai.use(myPlugin);
  // Now they can use your plugin's assertions
  ```请记住遵循命名插件的最佳实践，通常以 `chai-` 开头，并根据需要维护您的插件并提供更新和支持。

1. **使用 `npm init` 为您的插件初始化一个新项目**，并将 Chai 安装为对等依赖项。
  2. **为您的插件创建一个主文件**，例如`chai-myplugin.js`。
  3. **通过导出 Chai 将用来安装插件的函数来定义您的插件**：
  1. **添加方法或属性**
    到柴家
    `Assertion`
    对象。使用
    `utils.addMethod`
    对于新的断言方法或
    `utils.addProperty`
    对于新属性：

1. **彻底测试您的插件**。使用 Mocha 或其他测试框架创建 [test cases](../T/test-case.md) 以确保您的断言按预期工作。
  2. **记录您的插件**。清楚地解释如何安装和使用您的插件，包括断言的示例。
  3. **将您的插件**发布到 npm 以供其他人使用。在发布之前更新 `package.json` 文件，其中包含有关您的插件的详细信息。

### 高级概念

#### 如何将 Chai.js 与异步代码结合使用？

将 [Chai.js](../C/chai-js.md) 与异步代码一起使用通常涉及使用 Promise 或 async/await 语法。 Chai 提供了 `chai-as-promised` 插件来无缝处理 Promise 断言。
  首先，确保 `chai-as-promised` 已安装并添加到您的 Chai [setup](../S/setup.md) 中：

  ```
  const chai = require('chai');
  const chaiAsPromised = require('chai-as-promised');
  chai.use(chaiAsPromised);
  const expect = chai.expect;
  ```在处理 Promise 时，您可以将带有断言的 Promise 返回给 [test runner](../T/test-runner.md)，它将等待 Promise 解析或拒绝：

  ```
  it('should eventually have a value of 42', function() {
    return expect(Promise.resolve(42)).to.eventually.equal(42);
  });
  ```对于 async/await，请在测试函数中使用 `async` 并等待承诺。将断言应用于解析值：

  ```
  it('should have a value of 42', async function() {
    const value = await Promise.resolve(42);
    expect(value).to.equal(42);
  });
  ```要处理被拒绝的承诺，请使用 `.rejected` 属性并链接任何其他断言：

  ```
  it('should be rejected with an error', function() {
    return expect(Promise.reject(new Error('fail'))).to.be.rejected;
  });
  it('should be rejected with an error message', function() {
    return expect(Promise.reject(new Error('fail'))).to.be.rejectedWith('fail');
  });
  ```请记住在测试中处理已解决和拒绝的情况，以确保异步操作的全面覆盖。

#### 如何将 Chai.js 与 Promises 结合使用？

将 **[Chai.js](../C/chai-js.md)** 与 Promise 一起使用涉及利用 **chai-as-promised** 插件，该插件扩展了 Chai 以实现流畅的 Promise 断言。首先，确保安装 **chai-as-promised** 并将其与 Chai 集成：

  ```
  const chai = require('chai');
  const chaiAsPromised = require('chai-as-promised');
  chai.use(chaiAsPromised);
  const expect = chai.expect;
  ```使用 **chai-as-promised**，您可以以更具可读性的方式处理 Promise 断言。下面是测试返回 Promise 的函数的示例：

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
  ```请记住从 [test case](../T/test-case.md) 返回 Promise 或使用 `done` 回调来确保测试等待 Promise 解析：

  ```
  it('should resolve to the expected value', function() {
    return expect(asyncFunction()).to.eventually.equal('expected value');
  });
  // Using done callback
  it('should resolve to the expected value', function(done) {
    expect(asyncFunction()).to.eventually.equal('expected value').notify(done);
  });
  ```**chai-as-promised** 支持在 `eventually` 之后链接附加断言，并与 **mocha** 和其他处理返回 Promise 的 [test runners](../T/test-runner.md) 无缝集成。

#### Chai.js 的 .should 接口是什么以及它是如何工作的？

[Chai.js](../C/chai-js.md) 的 `.should` 接口是 [BDD](../B/bdd.md)（行为驱动开发）样式断言，它使用 `should` 属性扩展每个对象以启动断言链。该界面允许更具可读性和表现力的测试。
  要使用`.should` 接口，首先需要执行`chai.should()` 对`Object.prototype` 进行必要的修改。这是一个例子：

  ```
  const chai = require('chai');
  const should = chai.should();
  const number = 2;
  number.should.be.a('number');
  number.should.equal(2);
  ````.should` 接口的工作原理是向 `Object.prototype` 添加一个 getter，返回 `Should` 断言对象。然后可以使用该对象将进一步的断言链接到正在测试的值。请务必注意，使用 `.should` 会修改 `Object.prototype`，如果您的应用程序依赖于对象的枚举属性，这可能会导致意外行为。
  使用`.should` 的断言在失败时抛出`AssertionError`，然后[test runner](../T/test-runner.md) 可以捕获该断言以报告失败。 `.should` 接口支持与 Chai 的 `expect` 和 `assert` 接口相同的所有断言，提供丰富的断言集，如 `.equal`、`.deep.equal`、`.have.property` 等。
  使用 `.should` 时，您还可以利用 Chai 的可链接语言来增强测试的可读性：

  ```
  'hello'.should.be.a('string').and.have.lengthOf(5);
  ```请记住处理正在测试的对象上可能不存在的属性，因为尝试访问 `null` 或 `undefined` 上的 `should` 属性将引发错误。

#### 如何自定义 Chai.js 的断言错误消息？

自定义[Chai.js](../C/chai-js.md)断言错误消息可以增强测试结果的可读性和清晰度。要自定义错误消息，请使用 Chai 提供的 `.message` 可链接方法。此方法允许您指定断言失败时将显示的自定义消息。
  以下是使用 `expect` 接口的示例：

  ```
  const expect = require('chai').expect;
  expect(myFunction, 'custom error message if myFunction does not meet expectations').to.be.a('function');
  ```对于 `should` 接口，您可以将自定义消息作为第二个参数传递给断言方法：

  ```
  should = require('chai').should();
  myVariable.should.equal('expected value', 'custom error message if myVariable is not equal to expected value');
  ```对于 `assert` 接口，自定义消息通常是断言函数中的最后一个参数：

  ```
  const assert = require('chai').assert;
  assert.typeOf(myFunction, 'function', 'custom error message if myFunction is not a function');
  ```**注意：** 自定义消息应该简洁且具有足够的描述性，以便无需深入研究测试代码即可理解失败的上下文。
