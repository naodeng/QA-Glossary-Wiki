# Jest
[Jest](#jest) [Jest](/wiki/jest) [Unit Testing](/wiki/unit-testing)

### 相关术语 (Related Terms):
- 测试框架 (Testing framework)
- Jasmine
- Chai.js
[Testing framework](/glossary/testing-framework) [Jasmine](/glossary/jasmine) [Chai.js](/glossary/chaijs)

### 参见 (See also):
- [官方网站](https://jestjs.io/)

## 关于 Jest 的常见问题

#### 基础与重要性
- **什么是 Jest 以及它的用途？**
  Jest 是由 Facebook 开发的 JavaScript 测试框架，旨在确保任何 JavaScript 代码库的正确性。它广泛应用于前端（React, Vue, Angular）和后端（Node.js）项目。它支持**单元测试 (Unit Testing)**、**集成测试 (Integration Testing)** 和**端到端测试 (E2E Testing)**，并能通过与 Babel、TypeScript 的无缝集成实现并行执行以提高速度。

- **为什么 Jest 在 JavaScript 测试中如此流行？**
  核心优势在于其**简洁性**和**功能集成**。
  - **开箱即用**：内置断言、Mocking 库和覆盖率报告。
  - **观察模式 (Watch Mode)**：仅运行与修改相关的测试，加速开发。
  - **快照测试 (Snapshot Testing)**：轻松对比 UI 组件或数据的变动。
  - **并行执行**：在独立的进程中运行测试，极大地缩短执行时间。
  - **社区生态**：丰富的插件和强力的官方维护。

- **Jest 与其他框架相比如何？**
  - 与 **Mocha** 相比：Mocha 需要额外配置断言库（Chai）和模拟库（Sinon），而 Jest 是一站式集成。
  - 与 **Jasmine** 相比：Jest 基于 Jasmine，但提供了更现代、更强大的 Mocking API 和快照功能。
  - 与 **AVA** 相比：AVA 强调高度并发，而 Jest 在并行与共享上下文（如 JSDom 模拟浏览器环境）之间取得了更好的平衡。

- **什么是“零配置 (Zero-configuration)”？**
  Jest 旨在通过合理的默认约定（常规项目结构、文件名 `*.test.js` 或 `*.spec.js`）让开发者无需编写配置文件即可开始测试。

#### 安装与设置
- **如何安装 Jest？**
  1. 使用 npm 或 yarn 安装：
     `npm install --save-dev jest` 或 `yarn add --dev jest`
  2. 在 `package.json` 中配置脚本：
     `"scripts": { "test": "jest" }`
  3. 运行测试：`npm test`
  *注：TypeScript 项目需额外安装 `ts-jest` 和 `@types/jest`。*

#### 编写与运行测试
- **Jasmine 测试的文件结构是怎样的？**
  典型的 Jest 测试使用 `describe` 块进行逻辑分组，`it` 或 `test` 块定义具体用例。
  ```javascript
  const sum = require('./sum');
  describe('加法功能', () => {
    test('应该将 1 + 2 计算为 3', () => {
      expect(sum(1, 2)).toBe(3);
    });
  });
  ```

- **有哪些常用的断言 (Assertions)？**
  使用 `expect()` 配合匹配器 (Matchers)：
  - **等值比较**：`toBe`（严格相等）、`toEqual`（对象深度相等）。
  - **真值检查**：`toBeNull`, `toBeDefined`, `toBeTruthy`, `toBeFalsy`。
  - **数字比较**：`toBeGreaterThan`, `toBeLessThanOrEqual`。
  - **字符串/数组**：`toMatch` (正则), `toContain` (包含元素)。
  - **异常捕获**：`toThrow`。

#### 核心高级特性
- **什么是 Mocking 以及如何使用？**
  Mocking（模拟）用于隔离外部依赖（如网络请求或复杂模型）。
  - **Mock 函数**：`jest.fn()` 用于跟踪调用和设定返回值。
  - **手动模拟 (Manual Mocks)**：在 `__mocks__` 目录下创建模拟模块。
  - **自动模拟**：通过 `jest.mock('./module')` 自动接管导入。

- **快照测试 (Snapshot Testing) 的作用是什么？**
  通过捕捉组件渲染的输出（串行化后的树）并将其保存为文件，在后续运行中对比当前输出与保存版本是否一致。如果 UI 发生非预期变更，Jest 会提示。

- **如何处理异步测试？**
  - **返回 Promise**：Jest 会等待 Promise 被 Resolves。
  - **Async/Await**：最直观的方式，标记测试函数为 `async`。
  - **回调函数**：使用 `done` 参数在异步结束时显式调用 `done()`。

- **如何生成覆盖率报告？**
  运行 `jest --coverage` 即可直接在终端和 `coverage` 目录生成包含语句、分支、函数和行数的详细报告。

- **最佳实践**：
  - **测试隔离**：利用 `beforeEach` 重置状态。
  - **避免测试细节**：测试外部观察到的行为而不是私有方法。
  - **保持快照简洁**：不要快照过大的对象，否则难以查看 Diff。
  - **明确 Mock 的范围**：尽可能只在需要的测试用例中进行模拟。
