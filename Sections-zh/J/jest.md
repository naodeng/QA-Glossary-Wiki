# Jest




<!-- TOC START -->
- [# 另请参阅：](##-另请参阅：)
- [# 基础知识和重要性](##-基础知识和重要性)
  - [# Jest 是什么以及它的用途是什么？](##-jest-是什么以及它的用途是什么？)
  - [# 为什么Jest 很受测试JavaScript 代码的欢迎？](##-为什么jest-很受测试javascript-代码的欢迎？)
  - [# Jest 与其他测试框架相比如何？](##-jest-与其他测试框架相比如何？)
  - [# Jest 的主要功能是什么？](##-jest-的主要功能是什么？)
  - [# 为什么Jest 被视为“零配置”测试平台？](##-为什么jest-被视为零配置测试平台？)
- [# 安装和设置](##-安装和设置)
  - [# 如何安装Jest？](##-如何安装jest？)
  - [# 使用Jest 有哪些先决条件？](##-使用jest-有哪些先决条件？)
  - [# 如何设置基本的Jest 测试环境？](##-如何设置基本的jest-测试环境？)
  - [# 如何为项目配置Jest？](##-如何为项目配置jest？)
- [# 编写和运行测试](##-编写和运行测试)
  - [# 如何在 Jest 中编写基本测试？](##-如何在-jest-中编写基本测试？)
  - [# Jest 测试的结构是什么？](##-jest-测试的结构是什么？)
  - [# 如何在 Jest 中运行测试？](##-如何在-jest-中运行测试？)
  - [# Jest 中有哪些常见断言？](##-jest-中有哪些常见断言？)
  - [# 如何在 Jest 中对测试进行分组？](##-如何在-jest-中对测试进行分组？)
- [# 高级概念](##-高级概念)
  - [# Jest 中的模拟是什么以及如何使用它？](##-jest-中的模拟是什么以及如何使用它？)
  - [# Jest 如何处理异步测试？](##-jest-如何处理异步测试？)
  - [# 如何使用 Jest 进行快照测试？](##-如何使用-jest-进行快照测试？)
  - [# Jest 中“描述”函数的作用是什么？](##-jest-中描述函数的作用是什么？)
  - [# 如何在Jest 中使用“beforeEach”和“afterEach”？](##-如何在jest-中使用beforeeach和aftereach？)
<!-- TOC END -->

Jest

是JavaScript

单元测试

Meta 框架。它主要用于编写单元测试来评估各个代码段。

# # 相关术语：

- [Testing framework](../T/testing-framework.md)
- [Jasmine](../J/jasmine.md)
- [Chai.js](../C/chaijs.md)

## # 另请参阅：

- [Wikipedia](https://jestjs.io/)

# # 关于Jest 有疑问吗？

## # 基础知识和重要性

### # Jest 是什么以及它的用途是什么？

[Jest](../J/jest.md) 是一个**JavaScript 测试框架**，旨在确保任何JavaScript 代码库的正确性。它允许开发人员使用[API](../A/api.md) 编写测试，鼓励良好的测试实践，并且通常用于前端和后端JavaScript 应用程序。
  使用[Jest](../J/jest.md)，您可以执行**单元测试**来验证各个功能或模块，**集成测试**以确保应用程序的不同部分按预期协同工作，以及**端到端测试**来测试应用程序的流程。
  [Jest](../J/jest.md) 与使用 **Babel**、**TypeScript**、**[Node.js](../N/node-js.md)**、**React**、**Angular** 和 **Vue** 的项目完美集成，使其成为各种 JavaScript 项目的多功能选择。它还支持**测试并行化**，其中测试在单独的进程中同时运行，以最大限度地提高性能和速度。
  要将[Jest](../J/jest.md)集成到项目中，通常通过npm或yarn安装它，然后根据需要创建配置文件，尽管由于其约定优于配置设计，许多项目可以使用[Jest](../J/jest.md)而几乎不需要配置。
  以下是[Jest](../J/jest.md) 测试的基本示例：

  ```
  test('adds 1 + 2 to equal 3', () => {
    expect(1 + 2).toBe(3);
  });
  ```
[Jest](../J/jest.md) 的断言库提供了一系列匹配器，可让您验证不同的事物，从简单的相等性检查到更复杂的条件。它的**交互式监视模式**允许您自动重新运行与更改的文件相关的测试，并且它的**内置覆盖率报告**可以帮助您了解代码库的哪些部分可能未被测试覆盖。

### # 为什么Jest 很受测试JavaScript 代码的欢迎？

[Jest](../J/jest.md) 因其**简单**和**易于使用**而在测试 JavaScript 代码时很受欢迎。它与使用 **React**、**Angular**、**Vue** 和 **[Node.js](../N/node-js.md)** 的项目完美集成，使其成为各种 JavaScript 应用程序的多功能选择。其**监视模式**自动运行与更改的文件相关的测试，从而提高开发人员的工作效率。
  开发人员欣赏[Jest](../J/jest.md) 的**集成覆盖率报告**，该报告无需额外的[setup](../S/setup.md) 即可生成，可立即洞察[test coverage](../T/test-coverage.md)。该框架的**强大的模拟库**简化了具有复杂依赖项的代码的测试。
  [Jest](../J/jest.md) 的**并行[test execution](../T/test-execution.md)** 通过同时运行测试来优化性能，减少运行大量[test suites](../T/test-suite.md) 所需的时间。得益于自定义解析器以及使用 JSDom 进行 DOM [API](../A/api.md) 仿真，其跨测试运行的**一致的环境**确保了测试的可靠性。
  [Jest](../J/jest.md) 周围的社区非常活跃，为增强其功能的 **插件** 和 **扩展** 的丰富生态系统做出了贡献。维护人员的定期更新和改进使 [Jest](../J/jest.md) 保持在测试技术的最前沿。

  ```
  test('adds 1 + 2 to equal 3', () => {
    expect(sum(1, 2)).toBe(3);
  });
  ```
上面的示例演示了 [Jest](../J/jest.md) 的简单语法，使测试具有可读性和可维护性。 [Jest](../J/jest.md) 的受欢迎程度证明了其平衡**灵活性**、**功能**和**开发人员体验**的能力，使其成为JavaScript 测试的首选。

### # Jest 与其他测试框架相比如何？

与 Mocha、[Jasmine](../J/jasmine.md) 或 AVA 等其他测试框架相比，[Jest](../J/jest.md) 因其**简单**和**集成功能**而脱颖而出。与 Mocha 不同，Mocha 需要额外的插件来实现模拟、覆盖和快照测试等功能，[Jest](../J/jest.md) 附带了这些开箱即用的功能。这减少了配置多个库的需要，使 [Jest](../J/jest.md) 成为更**简化的选择**。
  [Jest](../J/jest.md) 并行运行测试，与其他一些框架相比，这可以导致**更快的执行时间**。其**监视模式**也针对开发人员体验进行了高度优化，允许自动运行与更改文件相关的测试。
  与具有类似语法的[Jasmine](../J/jasmine.md) 相比，[Jest](../J/jest.md) 提供了更**现代且强大的模拟库**。这使得测试JavaScript应用程序变得更容易，特别是那些使用React构建的应用程序，其中[Jest](../J/jest.md)通常是推荐的选择，因为它**对React测试实用程序的本机支持**。
  虽然 AVA 在测试运行中强调**并发**，但 [Jest](../J/jest.md) 平衡并行 [test execution](../T/test-execution.md) 与**共享上下文**，这对某些类型的 [test suites](../T/test-suite.md) 可能是有益的。此外，[Jest](../J/jest.md) 的**快照测试**功能比其他框架中的类似功能更先进，提供了一种测试组件输出的简单方法。
  对于**异步测试**，[Jest](../J/jest.md) 支持 async/await、promise 和回调，与其他框架类似，但具有更**统一的语法**和更好的错误处理。
  总体而言，[Jest](../J/jest.md) 通常因其**开发人员友好的方法**、全面的文档以及与 JavaScript 生态系统的**紧密集成**而受到青睐，特别是在使用 `create-react-app` 或使用 Babel 和 TypeScript 创建的项目中。

### # Jest 的主要功能是什么？

[Jest](../J/jest.md) 的主要功能包括：

- **快照测试**：[Jest](../J/jest.md) 可以捕获 React 树或其他可序列化值的“快照”，以简化 [UI testing](../U/ui-testing.md) 并确保 UI 不会意外更改。
  - **交互式监视模式**：[Jest](../J/jest.md) 可以在监视模式下运行，当检测到代码库中的更改时，该模式会自动重新运行测试，从而提高开发人员的工作效率。
  - **内置覆盖率报告**：[Jest](../J/jest.md) 包括一个集成的 [code coverage](../C/code-coverage.md) 报告器，可以使用简单的命令行标志 (`--coverage`) 激活。
  - **隔离和并行[Test Execution](../T/test-execution.md)**：测试在单独的进程中并行运行，以最大限度地提高性能并确保测试不会相互影响。
  - **全局[Setup](../S/setup.md)/Teardown**：[Jest](../J/jest.md) 提供了用于在所有测试运行之前和之后设置和拆除环境的挂钩。
  - **手动模拟**：开发人员可以创建手动模拟，以通过模拟实现来消除功能。
  - **计时器模拟**：[Jest](../J/jest.md) 可以在您的测试中模拟计时器，允许您控制时间的流逝。
  - **自定义匹配器**：使用自定义匹配器扩展[Jest](../J/jest.md) 的匹配器库，以获得更具描述性的测试语句。
  - **无缝TypeScript 集成**：[Jest](../J/jest.md) 支持TypeScript，无需额外配置即可进行类型安全测试。
  - **丰富的断言库**：[Jest](../J/jest.md) 附带大量匹配器，可以为不同的 [use cases](../U/use-case.md) 启用各种断言。
  - **可扩展性**：[Jest](../J/jest.md) 可以使用自定义报告器、自定义匹配器和自定义 [test runners](../T/test-runner.md) 进行扩展，以满足任何项目的需求。
  - **轻松模拟 ES 模块**：[Jest](../J/jest.md) 允许轻松模拟 ES6 模块，这在处理外部依赖项时特别有用。
  - **快照测试**：[Jest](../J/jest.md) 可以捕获 React 树或其他可序列化值的“快照”，以简化 [UI testing](../U/ui-testing.md) 并确保 UI 不会意外更改。
  - **交互式监视模式**：[Jest](../J/jest.md) 可以在监视模式下运行，当检测到代码库中的更改时，该模式会自动重新运行测试，从而提高开发人员的工作效率。
  - **内置覆盖率报告**：[Jest](../J/jest.md) 包括一个集成的 [code coverage](../C/code-coverage.md) 报告器，可以使用简单的命令行标志 (`--coverage`) 激活。
  - **隔离和并行[Test Execution](../T/test-execution.md)**：测试在单独的进程中并行运行，以最大限度地提高性能并确保测试不会相互影响。
  - **全局[Setup](../S/setup.md)/Teardown**：[Jest](../J/jest.md) 提供了用于在所有测试运行之前和之后设置和拆除环境的挂钩。
  - **手动模拟**：开发人员可以创建手动模拟，以通过模拟实现来消除功能。
  - **计时器模拟**：[Jest](../J/jest.md) 可以在您的测试中模拟计时器，允许您控制时间的流逝。
  - **自定义匹配器**：使用自定义匹配器扩展[Jest](../J/jest.md) 的匹配器库，以获得更具描述性的测试语句。
  - **无缝TypeScript 集成**：[Jest](../J/jest.md) 支持TypeScript，无需额外配置即可进行类型安全测试。
  - **丰富的断言库**：[Jest](../J/jest.md) 附带大量匹配器，可以为不同的 [use cases](../U/use-case.md) 启用各种断言。
  - **可扩展性**：[Jest](../J/jest.md) 可以使用自定义报告器、自定义匹配器和自定义 [test runners](../T/test-runner.md) 进行扩展，以满足任何项目的需求。
  - **轻松模拟 ES 模块**：[Jest](../J/jest.md) 允许轻松模拟 ES6 模块，这在处理外部依赖项时特别有用。

### # 为什么Jest 被视为“零配置”测试平台？

[Jest](../J/jest.md) 被认为是一个**零配置**测试平台，因为它的目标是开箱即用，只需要最少的[setup](../S/setup.md)。安装后，[Jest](../J/jest.md) 为大多数项目提供合理的默认值，允许开发人员立即开始编写和运行测试。
  该框架的设计符合约定，使其能够自动查找和执行测试。默认情况下，[Jest](../J/jest.md) 会查找具有以下任何流行命名约定的测试文件：

- 文件与
    `.js`
    后缀在
    `__tests__`
    文件夹。

- 文件与
    `.test.js`
    后缀。

- 文件与
    `.spec.js`
    后缀。
  [Jest](../J/jest.md) 还附带内置断言库和[test runner](../T/test-runner.md)，这意味着无需安装或配置其他模块即可开始测试。它通过 **Babel** 集成处理现代 JavaScript 功能的转换，并且它可以开箱即用地模拟依赖项和计时器。
  对于许多应用程序来说，默认配置足以开始测试。但是，如果需要自定义，[Jest](../J/jest.md) 提供了一个易于使用的配置文件 (`jest.config.js`)，开发人员可以在其中覆盖默认值并根据其特定需求定制测试环境。
  下面的示例说明了从 [Jest](../J/jest.md) 开始是多么简单：

  ```
  npm install --save-dev jest
  ```
然后，在 `sum.test.js` 文件中：

  ```
  const sum = require('./sum');
  test('adds 1 + 2 to equal 3', () => {
    expect(sum(1, 2)).toBe(3);
  });
  ```
使用以下命令运行测试：

  ```
  npx jest
  ```
[setup](../S/setup.md) 的易用性和合理的默认设置使得 [Jest](../J/jest.md) 成为许多开发人员的**零配置**测试平台。

- 文件与
    `.js`
    后缀在
    `__tests__`
    文件夹。

- 文件与
    `.test.js`
    后缀。

- 文件与
    `.spec.js`
    后缀。

## # 安装和设置

### # 如何安装Jest？

要安装 [Jest](../J/jest.md)，您需要在系统上安装 **[Node.js](../N/node-js.md)** 和 **npm** （节点包管理器）。如果您使用 **yarn**，也可以使用它。以下是安装 [Jest](../J/jest.md) 的方法：
  对于npm 用户：

  ```
  npm install --save-dev jest
  ```
对于纱线用户：

  ```
  yarn add --dev jest
  ```
此命令会将 [Jest](../J/jest.md) 添加为项目的 `package.json` 文件中的开发依赖项。安装后，您可以将脚本添加到`package.json`以轻松运行[Jest](../J/jest.md)：

  ```
  "scripts": {
    "test": "jest"
  }
  ```
现在，您可以使用以下命令运行测试：
  对于npm 用户：

  ```
  npm test
  ```
对于纱线用户：

  ```
  yarn test
  ```
确保您的测试文件使用`.test.js` 或`.spec.js` 后缀命名，或者放置在`__tests__` 文件夹中，以便[Jest](../J/jest.md) 可以自动查找并执行它们。
  如果您使用 **TypeScript**，您还需要安装 `ts-jest` 和 `@types/jest` 来处理 TypeScript 编译和类型定义：

  ```
  npm install --save-dev ts-jest @types/jest
  ```
或者用纱线：

  ```
  yarn add --dev ts-jest @types/jest
  ```
然后，您需要将以下内容添加到 [Jest](../J/jest.md) 配置中，将 [Jest](../J/jest.md) 配置为使用 `ts-jest`：

  ```
  "jest": {
    "preset": "ts-jest",
    "testMatch": ["**/*.test.ts"]
  }
  ```
这将指示[Jest](../J/jest.md) 使用`ts-jest` 处理`.ts` 文件。

### # 使用Jest 有哪些先决条件？

要有效使用[Jest](../J/jest.md)，应满足某些先决条件：

- **[Node.js](../N/node-js.md)** ：Jest 是基于节点的工具，因此必须在您的系统上安装当前版本的Node.js。
  - **npm 或 Yarn** ：包管理器用于安装 Jest 并管理其依赖项。
  - **JavaScript 知识**：熟悉JavaScript（或TypeScript）至关重要，因为Jest 是为测试JS 代码库而设计的。
  - **项目 [Setup](../S/setup.md)** ：带有 package.json 文件的 JavaScript 项目，用于配置 Jest 并将其包含为依赖项。
  - **理解测试概念**：了解单元测试、模拟和断言以编写有意义的测试。
  - **ES 模块支持**：如果使用 ES 模块，请确保兼容性或配置 Babel 进行转译。
  - **版本控制**：（可选）像 Git 这样的版本控制系统，用于跟踪测试中的更改以及代码。
  使用 npm 或 Yarn 安装[Jest](../J/jest.md)：

  ```
  npm install --save-dev jest
  ```
或者

  ```
  yarn add --dev jest
  ```
确保您的`package.json` 包含[test script](../T/test-script.md)：

  ```
  "scripts": {
    "test": "jest"
  }
  ```
对于 TypeScript 项目，安装 `ts-jest` 和 `@types/jest` 来处理类型检查并提供自动完成：

  ```
  npm install --save-dev ts-jest @types/jest
  ```
或者

  ```
  yarn add --dev ts-jest @types/jest
  ```
最后，熟悉 [Jest](../J/jest.md) 的 [API](../A/api.md) 和生命周期方法将有助于有效地构建测试。

- **[Node.js](../N/node-js.md)** ：Jest 是基于节点的工具，因此必须在您的系统上安装当前版本的 Node.js。
  - **npm 或 Yarn** ：包管理器用于安装 Jest 并管理其依赖项。
  - **JavaScript 知识**：熟悉JavaScript（或TypeScript）至关重要，因为Jest 是为测试JS 代码库而设计的。
  - **项目 [Setup](../S/setup.md)** ：带有 package.json 文件的 JavaScript 项目，用于配置 Jest 并将其包含为依赖项。
  - **理解测试概念**：了解单元测试、模拟和断言以编写有意义的测试。
  - **ES 模块支持**：如果使用 ES 模块，请确保兼容性或配置 Babel 进行转译。
  - **版本控制**：（可选）像 Git 这样的版本控制系统，用于跟踪测试中的更改以及代码。

### # 如何设置基本的Jest 测试环境？

要设置基本的 [Jest](../J/jest.md) 测试环境，请按照以下步骤操作：

1. **使用 `npm init` 或 `yarn init` 初始化您的项目**（如果尚未完成）。
  2. **使用 npm 或 Yarn 安装 [Jest](../J/jest.md)**：
    或

    ```
    npm install --save-dev jest
    ```

    ```
    yarn add --dev jest
    ```
3. 在`package.json` 中，添加以下脚本以运行[Jest](../J/jest.md)：

    ```
    "scripts": {
      "test": "jest"
    }
    ```
4. **如果需要，配置[Jest](../J/jest.md)**。对于大多数项目，[Jest](../J/jest.md) 可以零配置开箱即用。但是，如果您需要自定义 [Jest](../J/jest.md) 的行为，请创建 `jest.config.js` 文件或在 `package.json` 中添加 `jest` 密钥。
  5. **编写您的测试**。创建带有`.test.js` 或`.spec.js` 后缀的文件，或将它们放入`__tests__` 文件夹中。 [Jest](../J/jest.md) 将自动查找这些文件。
  6. **使用`test` 或`it`** 定义您的[test cases](../T/test-case.md)：

    ```
    test('adds 1 + 2 to equal 3', () => {
      expect(1 + 2).toBe(3);
    });
    ```
7. **通过执行 [test script](../T/test-script.md) 来运行测试**：
    或

    ```
    npm test
    ```

    ```
    yarn test
    ```
[Jest](../J/jest.md) 将执行测试并提供结果摘要。根据测试运行的反馈调整您的测试和代码。

1. **使用 `npm init` 或 `yarn init` 初始化您的项目**（如果尚未完成）。
  2. **使用 npm 或 Yarn 安装 [Jest](../J/jest.md)**：
    或

    ```
    npm install --save-dev jest
    ```

    ```
    yarn add --dev jest
    ```
3. 在`package.json` 中，添加以下脚本以运行[Jest](../J/jest.md)：

    ```
    "scripts": {
      "test": "jest"
    }
    ```
4. **如果需要，配置[Jest](../J/jest.md)**。对于大多数项目，[Jest](../J/jest.md) 可以零配置开箱即用。但是，如果您需要自定义 [Jest](../J/jest.md) 的行为，请创建 `jest.config.js` 文件或在 `package.json` 中添加 `jest` 密钥。
  5. **编写您的测试**。创建带有`.test.js` 或`.spec.js` 后缀的文件，或将它们放入`__tests__` 文件夹中。 [Jest](../J/jest.md) 将自动查找这些文件。
  6. **使用`test` 或`it`** 定义您的[test cases](../T/test-case.md)：

    ```
    test('adds 1 + 2 to equal 3', () => {
      expect(1 + 2).toBe(3);
    });
    ```
7. **通过执行 [test script](../T/test-script.md) 来运行测试**：
    或

    ```
    npm test
    ```

    ```
    yarn test
    ```
### # 如何为项目配置Jest？

要为项目配置[Jest](../J/jest.md)，请在项目的根目录中创建`jest.config.js` 文件，或在`package.json` 中定义`jest` 密钥。以下是 `jest.config.js` 文件的基本示例：

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
- **verbose** ：启用测试结果的详细输出。
  - **testEnvironment** ：设置运行测试的环境。
  - **setupFilesAfterEnv** ：列出在环境中安装测试框架后运行的脚本。
  - **transform** ：指定如何使用转换器处理文件。
  - **testMatch** ：确定哪些文件被视为测试文件。
  - **moduleNameMapper** ：映射模块路径以便于导入。
  - **coverageThreshold** ：设置项目的最小覆盖阈值。
  对于TypeScript 项目，您需要安装`ts-jest` 并配置`transform` 属性才能使用它。
  要将配置包含在`package.json`中，它看起来像这样：

  ```
  "jest": {
    "verbose": true,
    // ... other configurations
  }
  ```
请记住安装项目所需的任何其他 [Jest](../J/jest.md) 插件或预设。调整配置选项以匹配项目的特定需求，例如自定义全局变量、模块路径别名或不同的测试环境。

- **verbose** ：启用测试结果的详细输出。
  - **testEnvironment** ：设置运行测试的环境。
  - **setupFilesAfterEnv** ：列出在环境中安装测试框架后运行的脚本。
  - **transform** ：指定如何使用转换器处理文件。
  - **testMatch** ：确定哪些文件被视为测试文件。
  - **moduleNameMapper** ：映射模块路径以便于导入。
  - **coverageThreshold** ：设置项目的最小覆盖阈值。

## # 编写和运行测试

### # 如何在 Jest 中编写基本测试？

在[Jest](../J/jest.md) 中编写基本测试涉及创建带有`.test.js` 或`.spec.js` 后缀的测试文件，导入必要的模块，并使用`test` 或`it` 全局函数来定义[test cases](../T/test-case.md)。这是一个简洁的例子：

  ```
  const sum = require('./sum'); // Import the function to test
  test('adds 1 + 2 to equal 3', () => {
    expect(sum(1, 2)).toBe(3); // Use expect and matchers to test the function
  });
  ```
在此示例中，`sum` 是一个将两个数字相加的简单函数。 `test` 函数有两个参数：一个描述 [test case](../T/test-case.md) 的字符串，以及一个编写实际测试代码的回调函数。 `expect` 函数用于断言预期结果，`.toBe` 是检查严格相等性的匹配器。
  请记住以逻辑清晰的方式构建测试，以便它们易于阅读和理解。使用准确反映您正在测试的行为的**描述性测试名称**和**断言**。让测试**集中**在单一功能上，使它们可维护，并在测试失败时更容易进行调试。

### # Jest 测试的结构是什么？

[Jest](../J/jest.md) 测试结构通常由一系列将相关测试组合在一起的 **describe** 块以及定义各个 [test cases](../T/test-case.md) 的 **it** 或 **test** 块组成。这是一个基本轮廓：

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
- **描述**：对多个测试进行分组；对于按功能或组件组织测试很有用。
  - **beforeEach/afterEach** ：在描述块中的每个测试之前/之后运行的安装/拆卸挂钩。
  - **it/test** ：定义单个测试用例；
    `it`
    是一个别名
    `test`
    ，并且两者可以互换。

- **expect** ：创建关于测试用例的预期结果的断言。
  测试可以嵌套在**描述**块中以进行进一步组织。 **beforeAll** 和 **afterAll** 钩子也可用于[setup](../S/setup.md)/teardown，这些钩子只能在描述块中的所有测试之前/之后发生一次。

- **描述**：对多个测试进行分组；对于按功能或组件组织测试很有用。
  - **beforeEach/afterEach** ：在描述块中的每个测试之前/之后运行的安装/拆卸挂钩。
  - **it/test** ：定义单个测试用例；
    `it`
    是一个别名
    `test`
    ，并且两者可以互换。

- **expect** ：创建关于测试用例的预期结果的断言。

### # 如何在 Jest 中运行测试？

要在 [Jest](../J/jest.md) 中运行测试，请按照下列步骤操作：

1. **在终端中导航到您的项目目录**。
  2. 确保您的项目中有`package.json` 文件。如果没有，请使用 `npm init` 创建一个。
  3. **使用以下命令之一运行测试**：
    - 运行所有测试：
      或者如果 Jest 未全局安装：
      或者使用 npm 脚本
      `package.json`：
      然后使用npm执行：

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
- 运行所有测试：
      或者如果 Jest 未全局安装：
      或者使用 npm 脚本
      `package.json`：
      然后使用npm执行：

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
4. **通过附加文件路径来运行特定的测试文件**：

    ```
    jest path/to/your_test_file.js
    ```
5. **监视模式**：要在监视模式下运行 [Jest](../J/jest.md)（对文件更改重新运行测试），请使用 `--watch` 标志：

    ```
    jest --watch
    ```
6. **使用 `--testNamePattern` 标志按测试名称过滤测试**：

    ```
    jest --testNamePattern="pattern"
    ```
7. **使用 `--testPathPattern` 标志运行与特定文件名模式匹配的测试：

    ```
    jest --testPathPattern="pattern"
    ```
8. **根据您的 Git 存储库运行与已更改文件相关的测试**：

    ```
    jest --onlyChanged
    ```
9. **通过在[Jest](../J/jest.md) 配置中设置`testEnvironment` 在特定环境中运行测试**。
  10. **使用 `--coverage` 标志生成覆盖率报告**：

    ```
    jest --coverage
    ```
[Jest](../J/jest.md) CLI 提供了许多其他选项，可以通过运行 `jest --help` 列出这些选项。

1. **在终端中导航到您的项目目录**。
  2. 确保您的项目中有`package.json` 文件。如果没有，请使用 `npm init` 创建一个。
  3. **使用以下命令之一运行测试**：
    - 运行所有测试：
      或者如果 Jest 未全局安装：
      或者使用 npm 脚本
      `package.json`：
      然后使用npm执行：

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
- 运行所有测试：
      或者如果 Jest 未全局安装：
      或者使用 npm 脚本
      `package.json`：
      然后使用npm执行：

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
4. **通过附加文件路径来运行特定的测试文件**：

    ```
    jest path/to/your_test_file.js
    ```
5. **监视模式**：要在监视模式下运行 [Jest](../J/jest.md)（对文件更改重新运行测试），请使用 `--watch` 标志：

    ```
    jest --watch
    ```
6. **使用 `--testNamePattern` 标志按测试名称过滤测试**：

    ```
    jest --testNamePattern="pattern"
    ```
7. **使用 `--testPathPattern` 标志运行与特定文件名模式匹配的测试：

    ```
    jest --testPathPattern="pattern"
    ```
8. **根据您的 Git 存储库运行与已更改文件相关的测试**：

    ```
    jest --onlyChanged
    ```
9. **通过在[Jest](../J/jest.md) 配置中设置`testEnvironment` 在特定环境中运行测试**。
  10. **使用 `--coverage` 标志生成覆盖率报告**：

    ```
    jest --coverage
    ```
### # Jest 中有哪些常见断言？

在[Jest](../J/jest.md) 中，使用`expect` 函数进行断言，该函数与“匹配器”函数链接以以不同方式测试值。以下是一些常见的断言：

- **平等**：

    ```
    expect(5).toBe(5);
    expect({ a: 1 }).toEqual({ a: 1 });
    ```
- `toBe(value)`
      检查严格相等 (===)。

- `toEqual(value)`
      检查值是否相等，对于对象和数组很有用。

- `toBe(value)`
      检查严格相等 (===)。

- `toEqual(value)`
      检查值是否相等，对于对象和数组很有用。

- **真实性**：

    ```
    expect(null).toBeNull();
    expect(undefined).toBeUndefined();
    expect(1).toBeTruthy();
    ```
- `toBeNull()`
      检查一个值是否是
      `null`
      。

- `toBeUndefined()`
      检查一个值是否是
      `undefined`
      。

- `toBeDefined()`
      检查某个值是否不是
      `undefined`
      。

- `toBeTruthy()`
      检查值是否为真。

- `toBeFalsy()`
      检查一个值是否为假值。

- `toBeNull()`
      检查一个值是否是
      `null`
      。

- `toBeUndefined()`
      检查一个值是否是
      `undefined`
      。

- `toBeDefined()`
      检查某个值是否不是
      `undefined`
      。

- `toBeTruthy()`
      检查值是否为真。

- `toBeFalsy()`
      检查一个值是否为假值。

- **数字**：

    ```
    expect(10).toBeGreaterThan(5);
    expect(10).toBeLessThanOrEqual(10);
    ```
- `toBeGreaterThan(number)`
      检查一个值是否大于一个数字。

- `toBeGreaterThanOrEqual(number)`
      检查值是否大于或等于数字。

- `toBeLessThan(number)`
      检查值是否小于数字。

- `toBeLessThanOrEqual(number)`
      检查值是否小于或等于数字。

- `toBeGreaterThan(number)`
      检查一个值是否大于一个数字。

- `toBeGreaterThanOrEqual(number)`
      检查值是否大于或等于数字。

- `toBeLessThan(number)`
      检查值是否小于数字。

- `toBeLessThanOrEqual(number)`
      检查值是否小于或等于数字。

- **字符串**：

    ```
    expect('team').toMatch(/T/i);
    ```
- `toMatch(regexpOrString)`
      检查字符串是否与正则表达式或字符串匹配。

- `toMatch(regexpOrString)`
      检查字符串是否与正则表达式或字符串匹配。

- **数组**：

    ```
    expect(['Alice', 'Bob', 'Eve']).toContain('Bob');
    ```
- `toContain(item)`
      检查数组是否包含特定项目。

- `toContain(item)`
      检查数组是否包含特定项目。

- **例外**：

    ```
    expect(() => { throw new Error('Error!'); }).toThrow('Error!');
    ```
-`toThrow（错误？
      )`
      检查函数在调用时是否抛出错误。

-`toThrow（错误？
      )`
      检查函数在调用时是否抛出错误。

- **对象**：

    ```
    expect({ a: { b: 1 } }).toHaveProperty('a.b', 1);
    ```
- `toHaveProperty(keyPath, 值?
      )`
      检查对象在指定的键路径处是否具有属性，可以选择检查该值。

- `toHaveProperty(keyPath, 值?
      )`
      检查对象在指定的键路径处是否具有属性，可以选择检查该值。
  这些断言有助于确保代码的行为符合预期，并且它们是使用 [Jest](../J/jest.md) 编写全面的 [test suites](../T/test-suite.md) 的关键部分。

- **平等**：

    ```
    expect(5).toBe(5);
    expect({ a: 1 }).toEqual({ a: 1 });
    ```
- `toBe(value)`
      检查严格相等 (===)。

- `toEqual(value)`
      检查值是否相等，对于对象和数组很有用。

- `toBe(value)`
      检查严格相等 (===)。

- `toEqual(value)`
      检查值是否相等，对于对象和数组很有用。

- **真实性**：

    ```
    expect(null).toBeNull();
    expect(undefined).toBeUndefined();
    expect(1).toBeTruthy();
    ```
- `toBeNull()`
      检查一个值是否是
      `null`
      。

- `toBeUndefined()`
      检查一个值是否是
      `undefined`
      。

- `toBeDefined()`
      检查某个值是否不是
      `undefined`
      。

- `toBeTruthy()`
      检查值是否为真。

- `toBeFalsy()`
      检查一个值是否为假值。

- `toBeNull()`
      检查一个值是否是
      `null`
      。

- `toBeUndefined()`
      检查一个值是否是
      `undefined`
      。

- `toBeDefined()`
      检查某个值是否不是
      `undefined`
      。

- `toBeTruthy()`
      检查值是否为真。

- `toBeFalsy()`
      检查一个值是否为假值。

- **数字**：

    ```
    expect(10).toBeGreaterThan(5);
    expect(10).toBeLessThanOrEqual(10);
    ```
- `toBeGreaterThan(number)`
      检查一个值是否大于一个数字。

- `toBeGreaterThanOrEqual(number)`
      检查值是否大于或等于数字。

- `toBeLessThan(number)`
      检查值是否小于数字。

- `toBeLessThanOrEqual(number)`
      检查值是否小于或等于数字。

- `toBeGreaterThan(number)`
      检查一个值是否大于一个数字。

- `toBeGreaterThanOrEqual(number)`
      检查值是否大于或等于数字。

- `toBeLessThan(number)`
      检查值是否小于数字。

- `toBeLessThanOrEqual(number)`
      检查值是否小于或等于数字。

- **字符串**：

    ```
    expect('team').toMatch(/T/i);
    ```
- `toMatch(regexpOrString)`
      检查字符串是否与正则表达式或字符串匹配。

- `toMatch(regexpOrString)`
      检查字符串是否与正则表达式或字符串匹配。

- **数组**：

    ```
    expect(['Alice', 'Bob', 'Eve']).toContain('Bob');
    ```
- `toContain(item)`
      检查数组是否包含特定项目。

- `toContain(item)`
      检查数组是否包含特定项目。

- **例外**：

    ```
    expect(() => { throw new Error('Error!'); }).toThrow('Error!');
    ```
-`toThrow（错误？
      )`
      检查函数在调用时是否抛出错误。

-`toThrow（错误？
      )`
      检查函数在调用时是否抛出错误。

- **对象**：

    ```
    expect({ a: { b: 1 } }).toHaveProperty('a.b', 1);
    ```
- `toHaveProperty(keyPath, 值?
      )`
      检查对象在指定的键路径处是否具有属性，可以选择检查该值。

- `toHaveProperty(keyPath, 值?
      )`
      检查对象在指定的键路径处是否具有属性，可以选择检查该值。

### # 如何在 Jest 中对测试进行分组？

在[Jest](../J/jest.md) 中，您可以使用`describe` 函数对测试进行分组。此功能允许您创建一个将多个相关测试组合在一起的块。这是一个基本示例：

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
每个`describe` 块可以包含自己的[setup](../S/setup.md) 以及使用`beforeEach`、`afterEach`、`beforeAll` 和`afterAll` 函数进行的测试组的拆卸。这有助于逻辑地组织测试并有效管理共享[setup](../S/setup.md)和拆卸过程。
  嵌套`describe`块可用于更细粒度的分组：

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
使用`describe` 块对于区分正在测试的功能的各种状态或条件特别有用，并且它通过清楚地显示失败的测试属于哪个组来增强[test reports](../T/test-report.md) 的可读性。

## # 高级概念

### # Jest 中的模拟是什么以及如何使用它？

[Jest](../J/jest.md) 中的模拟是一种用于隔离和模拟一段代码所依赖的外部模块或函数的行为的技术。通过创建模拟函数或对象，您可以控制这些依赖项的输入和输出，从而实现更可预测和受控的测试环境。
  **模拟函数**可以使用 `jest.fn()` 创建来跟踪调用并定义返回值。它们可以替换模块中的实际函数，让您断言它们是如何调用的以及使用什么参数。

  ```
  const mockFunction = jest.fn();
  mockFunction.mockReturnValue('mocked value');
  ```
**手动模拟**对于模块和复杂的依赖项很有用。您可以在模块附近创建一个 `__mocks__` 目录，并且在测试中调用 `jest.mock()` 函数时，[Jest](../J/jest.md) 将使用模拟版本而不是真实版本。

  ```
  // In your test file
  jest.mock('./path/to/module');
  ```
使用 `jest.mock()` 的 **自动模拟** 允许 [Jest](../J/jest.md) 接管模块导入并将其替换为合适的模拟对象，所有导出都是模拟函数。

  ```
  // In your test file
  jest.mock('axios');
  ```
模拟还用于**消除那些可能产生副作用的功能**，例如网络请求或文件系统操作，方法是将它们替换为模仿行为而不执行实际操作的模拟实现。
  [Jest](../J/jest.md) 中的模拟对于创建独立于外部因素的单元测试以及确保测试是确定性的至关重要，这意味着它们每次运行时都会产生相同的结果。

### # Jest 如何处理异步测试？

[Jest](../J/jest.md) 通过提供多种方法来处理不同类型的异步代码来处理异步测试。这些包括：

- **回调**：为了测试较旧的回调样式代码，Jest 提供了
    `done`
    测试函数中的参数。致电
    `done()`
    当异步操作完成时，向 Jest 发出测试已完成的信号。

  ```
  test('async test with callback', done => {
    setTimeout(() => {
      expect(true).toBe(true);
      done();
    }, 1000);
  });
  ```
- **Promises** ：如果代码返回一个 Promise，则从测试中返回它，Jest 将等待它解析或拒绝。

  ```
  test('async test with promise', () => {
    return fetchData().then(data => {
      expect(data).toBe('expected data');
    });
  });
  ```
- **Async/Await** ：对于现代异步代码，请使用
    `async`
    功能和
    `await`
    异步操作。 Jest 将等待
    `async`
    在完成测试之前要解决的函数。

  ```
  test('async test with async/await', async () => {
    const data = await fetchData();
    expect(data).toBe('expected data');
  });
  ```
- **计时器**：Jest 可以模拟计时器并控制使用的操作的时间
    `setTimeout`
    ,
    `setInterval`
    , 或
    `setImmediate`
    与
    `jest.useFakeTimers()`
    以及相关的定时器控制功能。

  ```
  jest.useFakeTimers();
  test('async test with timers', () => {
    const callback = jest.fn();
    setTimeout(callback, 1000);
    jest.runAllTimers();
    expect(callback).toHaveBeenCalled();
  });
  ```
这些方法允许对异步操作进行全面测试，确保仅在考虑了所有异步操作后才能完成测试。

- **回调**：为了测试较旧的回调样式代码，Jest 提供了
    `done`
    测试函数中的参数。致电
    `done()`
    当异步操作完成时，向 Jest 发出测试已完成的信号。

- **Promises** ：如果代码返回一个 Promise，则从测试中返回它，Jest 将等待它解析或拒绝。
  - **Async/Await** ：对于现代异步代码，请使用
    `async`
    功能和
    `await`
    异步操作。 Jest 将等待
    `async`
    在完成测试之前要解决的函数。

- **计时器**：Jest 可以模拟计时器并控制使用的操作的时间
    `setTimeout`
    ,
    `setInterval`
    , 或
    `setImmediate`
    与
    `jest.useFakeTimers()`
    以及相关的定时器控制功能。

### # 如何使用 Jest 进行快照测试？

[Jest](../J/jest.md) 的快照测试功能允许您**测试代码输出的“形状”**。这对于 UI 组件特别有用，可确保对组件的更改不会导致意外结果。
  要使用 [Jest](../J/jest.md) 进行快照测试，请执行以下步骤：

1. **编写测试**
    呈现您的组件或调用您的函数。

2. 使用
    `expect`
    连同
    `toMatchSnapshot()`
    匹配器到
    **断言输出与保存的快照匹配**
    。
  这是使用 React 组件的基本示例：

  ```
  import React from 'react';
  import renderer from 'react-test-renderer';
  import MyComponent from './MyComponent';
  test('MyComponent renders correctly', () => {
    const tree = renderer.create(<MyComponent />).toJSON();
    expect(tree).toMatchSnapshot();
  });
  ```
第一次运行此测试时，[Jest](../J/jest.md) 在测试文件旁边的 `__snapshots__` 目录中创建一个快照文件。快照包含组件渲染输出的字符串表示形式。
  在后续测试运行中，[Jest](../J/jest.md) 会将渲染的输出与保存的快照进行比较。如果存在差异，则测试失败，并提示进行审核。如果更改是故意的，请使用 [Jest](../J/jest.md) 的 `--updateSnapshot` 或 `-u` 标志**更新快照**：

  ```
  jest --updateSnapshot
  ```
或者对于特定的测试文件：

  ```
  jest MyComponent.test.js --updateSnapshot
  ```
请记住，快照应与代码更改一起提交。在代码审查期间审查快照以**捕获意外更改**。明智地使用快照测试，因为过度依赖可能会导致快照文件过大，并降低测试对有意义的更改的敏感性。

1. **编写测试**
    呈现您的组件或调用您的函数。

2. 使用
    `expect`
    连同
    `toMatchSnapshot()`
    匹配器到
    **断言输出与保存的快照匹配**
    。

### # Jest 中“描述”函数的作用是什么？

在[Jest](../J/jest.md) 中，`describe` 函数用于**将相关测试组合在一起**。它通过**封装多个测试特定功能或组件的[test cases](../T/test-case.md)**来组织[test suite](../T/test-suite.md)。这对于可读性和维护特别有用，因为它允许开发人员一目了然地看到哪些测试是相关的，并运行与他们正在处理的代码区域相关的测试子集。
  `describe` 块可以包含任意数量的`test` 或`it` 块，并且还可以**嵌套**在其他`describe` 块中，以进一步分层构建测试。每个`describe` 块还可以有自己的`beforeEach`、`afterEach`、`beforeAll` 和`afterAll` 生命周期方法，这些方法仅适用于该`describe` 块内的测试。
  以下是在 [Jest](../J/jest.md) 中使用 `describe` 的基本示例：

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
使用`describe` 允许组中的测试共享[setup](../S/setup.md) 和拆卸代码，有助于保持测试**干燥**（不要重复），并且它增强了测试输出的**组织** 和**可读性**，因为[Jest](../J/jest.md) 将根据这些分组报告结果。

### # 如何在Jest 中使用“beforeEach”和“afterEach”？

在 [Jest](../J/jest.md) 中，`beforeEach` 和 `afterEach` 是生命周期方法，用于在 `describe` 块中的每个测试之前和之后运行一些代码。它们帮助设置先决条件并在测试后进行清理以避免副作用。
  当您想要初始化某些变量、模拟函数或为每个[test case](../T/test-case.md) 设置环境时，请使用`beforeEach`。它确保每个测试都以新状态运行。

  ```
  beforeEach(() => {
    // Initialization or setup code here
  });
  ```
`afterEach` 用于拆卸活动，例如清除模拟、重置模块或释放测试使用的资源。

  ```
  afterEach(() => {
    // Teardown or cleanup code here
  });
  ```
**例子：**

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
在此示例中，[setup](../S/setup.md) 代码将在`test case 1` 和`test case 2` 之前运行，而清理代码将在每个[test cases](../T/test-case.md) 完成之后运行。这确保了每个测试都是隔离的并且不会影响其他测试。
