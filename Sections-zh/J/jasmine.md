# Jasmine
[Jasmine](#jasmine) [Jasmine](/wiki/jasmine)

### 相关术语 (Related Terms):
- 测试框架 (Testing framework)
- Jest
- Chai.js
[Testing framework](/glossary/testing-framework) [Jest](/glossary/jest) [Chai.js](/glossary/chaijs)

### 参见 (See also):
- [官方网站](https://jasmine.github.io/)
- [维基百科](https://en.wikipedia.org/wiki/Jasmine_(software))

## 关于 Jasmine 的常见问题

#### 基础与重要性
- **什么是软件测试中的 Jasmine？**
  Jasmine 是一个用于测试 JavaScript 代码的**行为驱动开发 (BDD)** 框架。它不依赖于浏览器、DOM 或任何 JavaScript 框架，适用于测试任何 JavaScript 应用。其语法设计简洁易读，旨在通过 `describe`（套件）和 `it`（规格/测试用例）实现层次化的测试结构。Jasmine 提供内置的 **matchers**（匹配器，如 `toEqual`, `toBe`）进行断言，并支持 **Spies**（间谍/测试双倍）来跟踪函数调用。对于异步操作，它支持 `done` 回调或现代的 `async/await` 语法。

- **为什么 Jasmine 在 E2E 测试中很重要？**
  在端到端 (E2E) 测试中，Jasmine 常与 **Protractor**（针对 Angular）或 **Selenium WebDriver** 配合使用。它的 BDD 语法能清晰描述用户故事和用例，支持处理浏览器中的异步操作（如 AJAX 调用、UI 更新），并通过 Spies 和 Mocks 隔离外部依赖，确保测试聚焦于用户体验。

- **Jasmine 的核心特性有哪些？**
  - **BDD 语法**：易于编写和理解。
  - **无外部依赖**：开箱即用。
  - **丰富的匹配器 (Matchers)**：内置多种断言方法。
  - **异步支持**：通过回调或 Promise 处理异步。
  - **Spies**：内置函数监控和伪造功能。
  - **时钟控制**：可模拟时间流逝进行测试。
  - **可扩展性**：支持自定义匹配器和报告器。

- **Jasmine 与其他框架（如 Mocha, Jest, Cypress）相比如何？**
  - **Mocha**：更灵活，但通常需要配合 Chai（断言）和 Sinon（Mock）使用，而 Jasmine 是全功能内置。
  - **Jest**：基于 Jasmine，但增加了快照测试、内置覆盖率和并行执行等高级功能。
  - **Cypress**：运行在浏览器内，提供交互式运行器，更适合现代 Web 端的 E2E 测试。
  - **Karma**：不是框架，而是可以运行 Jasmine 代码的测试运行器。

#### 安装与设置
- **如何安装 Jasmine？**
  前提条件是安装了 **Node.js** 和 **npm**。步骤如下：
  1. 初始化 npm：`npm init -y`
  2. 安装 Jasmine：`npm install --save-dev jasmine`
  3. 初始化 Jasmine 目录：`npx jasmine init`
  4. 在 `package.json` 中添加脚本：`"scripts": { "test": "jasmine" }`
  5. 运行测试：`npm test`

#### 编写与运行测试
- **如何编写基础的 Jasmine 测试？**
  使用 `describe` 定义测试套件，使用 `it` 定义具体规格，使用 `expect` 配合匹配器进行断言。
  ```javascript
  describe('我的测试套件', () => {
    it('应正确执行加法', () => {
      let sum = 1 + 2;
      expect(sum).toEqual(3);
    });
  });
  ```

- **什么是 `beforeEach` 和 `afterEach`？**
  它们是钩子函数，用于在**每个** `it` 块运行前（`beforeEach`）或运行后（`afterEach`）执行设置（Setup）和清理（Teardown）逻辑，以确保测试环境的一致性和隔离性。

#### 断言与匹配器 (Matchers)
- **什么是 Matchers 以及如何使用？**
  Matchers 是执行布尔比较的函数。常用匹配器包括：
  - `toBe`: 严格相等 (===)
  - `toEqual`: 深度相等（对比对象/数组内容）
  - `toMatch`: 正则匹配
  - `toContain`: 是否包含子串或元素
  - `toThrow`: 是否抛出错误

- **如何创建自定义匹配器？**
  通过 `jasmine.addMatchers` 扩展。每个匹配器返回一个包含 `compare` 函数的对象，该函数返回 `pass` 状态和可选的 `message`。

#### Spies 与 Mocking
- **什么是 Jasmine Spies？**
  Spies 是用于记录函数调用信息的函数。
  - 创建方法：`spyOn(obj, 'method')` 或 `jasmine.createSpy()`。
  - 功能：跟踪调用次数、参数，或伪造返回值（`.and.returnValue()`）、模拟实现（`.and.callFake()`）。
  - 断言：使用 `toHaveBeenCalled()` 或 `toHaveBeenCalledWith()`。

- **Spy 和 Mock 的区别是什么？**
  **Spy** 通常是观察现有函数的调用情况；**Mock** 则是模拟整个对象及其行为（使用 `jasmine.createSpyObj`）。两者都是为了隔离测试单元并验证交互。

#### 高级概念
- **如何处理异步测试？**
  1. 使用 `done` 回调：在异步操作完成后调用 `done()`。
  2. 使用 `async/await`：将测试函数设为 `async` 并 `await` 异步调用（最推荐）。
  3. 错误处理：可以使用 `done.fail(error)` 显式标记失败。

- **最佳实践有哪些？**
  - **保持测试隔离**：不依赖其他测试的状态。
  - **描述性命名**：使测试意图清晰。
  - **单一职责**：每个 `it` 块只测试一个行为。
  - **避免测试细节**：关注公共 API 和结果，而非内部实现。
  - **保持快速**：优化测试性能。
