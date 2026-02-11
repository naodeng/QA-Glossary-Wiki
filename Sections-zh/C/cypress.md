# Cypress

[Cypress](#cypress) 是一个为现代 Web 应用程序设计的**端到端测试 (end-to-end testing)** 框架。它在浏览器中运行，建立在 JavaScript 和 Node.js 技术之上。与许多其他测试工具不同，Cypress 在与应用程序相同的运行循环中执行测试，从而无需单独的驱动程序或服务器即可原生访问每个对象。

### 相关术语：
- **Web 自动化工具**
- **Playwright**

### 参见：
- [官方网站](https://www.cypress.io/)
- [维基百科](https://en.wikipedia.org/wiki/Cypress_(software))

---

## 关于 Cypress 的问题？

#### 基础与重要性

- **什么是 Cypress？**
Cypress 是一个现代前端测试框架。它提供了一个功能丰富的**交互式测试运行器 (test runner)**，允许你在查看被测应用程序的同时观察命令的执行。
其核心特性包括：
    - **实时重载 (Real-time reloads)**：保存文件时测试自动重跑。
    - **可链式调用 API (Chainable API)**：简化异步操作。
    - **自动等待 (Automatic waiting)**：在执行操作或断言前自动等待，减少了显式等待的需求。
    - **原生调试能力**：可以直接使用浏览器的开发者工具进行调试。
    - **快照与时间旅行 (Time Travel)**：记录测试运行时的每个步骤，方便回溯。

Cypress 不使用 Selenium 或 WebDriver，这使得执行速度更快且控制力更强。它支持 Chrome 系列浏览器、Edge、Electron 和 Firefox。

- **为什么在测试中使用 Cypress？**
Cypress 因其**简单性**和**开发者友好**而备受青睐。由于它在应用相同的运行循环内运行，可以编写几乎没有**不稳定性 (flakiness-free)** 的测试。
主要优势包括：
    - **可靠性与一致性**。
    - **高度集成**：与现代开发工具和 CI/CD 流程紧密结合。
    - **强大的调试与可视化能力**：具备屏幕截图和视频录制功能。
    - **网络流量控制**：可以轻松 stub（存根）网络请求，测试边界情况。

- **Cypress 的主要特性有哪些？**
    - **实时重载**。
    - **时间旅行 (Time Travel)**：通过命令日志查看历史快照。
    - **自动等待**。
    - **网络流量拦截 (Network Traffic Control)**。
    - **截图与视频**。
    - **跨浏览器测试**。
    - **并行执行 (Parallelization)**。
    - **仪表板服务 (Dashboard Service)**：提供分析、并行化和历史记录。
    - **Spies、Stubs 和 Clocks**：验证和控制函数/定时器行为。
    - **无障碍测试 (Accessibility Testing)**：配合 `cypress-axe` 插件。

- **Cypress 与 Selenium 有何不同？**
    - **架构**：Cypress 运行在浏览器内部；Selenium 在浏览器外部通过 WebDriver 通信。
    - **语言**：Cypress 仅支持 JavaScript/TypeScript；Selenium 支持多种语言。
    - **安装**：Cypress 开箱即用，无需额外驱动；Selenium 需要配置浏览器特定的 Driver。
    - **等待机制**：Cypress 内置自动等待；Selenium 通常需要显式编写等待逻辑。
    - **API 测试**：Cypress 内置 API 测试支持。

- **Cypress 可以进行哪些类型的测试？**
    - **端到端测试 (E2E)**。
    - **集成测试 (Integration)**。
    - **单元测试 (Unit)**。
    - **组件测试 (Component)**：特别是针对 React/Vue/Angular 组件。
    - **视觉回归测试 (Visual Regression)**：集成 Percy 等工具。
    - **API 测试**。
    - **性能测试**（基础指标监控）。

#### 安装与设置

- **如何安装 Cypress？**
确保已安装 Node.js，在项目目录下运行：
```bash
npm install cypress --save-dev
# 或
yarn add cypress --dev
```
安装后，通过以下命令打开测试运行器：
```bash
npx cypress open
```

- **系统要求？**
支持 Windows、macOS 和 Linux。
    - Node.js 12+。
    - 内存推荐 2GB 以上。
    - Linux 用户可能需要安装额外的依赖库。

- **如何设置项目？**
1. 初始化项目：`npm init -y`。
2. 安装 Cypress。
3. 运行 `npx cypress open` 进行初始化脚手架搭建（生成 `cypress` 目录）。
4. 在 `cypress.config.js`（或旧版的 `cypress.json`）中进行配置（如 `baseUrl`）。

- **如何针对特定环境进行配置？**
可以通过环境变量、不同的配置文件或在插件文件中动态修改配置。使用 `Cypress.env()` 在测试中访问环境变量。

#### 编写与运行测试

- **结构示例？**
```javascript
describe('用户登录', () => {
  beforeEach(() => {
    cy.visit('/login');
  });

  it('使用有效凭据应登录成功', () => {
    cy.get('input[name="username"]').type('user');
    cy.get('input[name="password"]').type('password');
    cy.get('form').submit();
    cy.url().should('include', '/dashboard');
  });
});
```

- **如何使用断言？**
Cypress 使用 Chai 断言库，支持 `should`、`expect` 和 `assert` 语法。
```javascript
cy.get('.element').should('be.visible').and('contain', 'Hello');
```

- **如何处理事件？**
使用 `.click()`、`.type()`、`.submit()`、`.trigger('mouseover')` 等命令。

- **如何使用 Fixtures？**
将静态测试数据放在 `cypress/fixtures` 下，使用 `cy.fixture('user.json')` 加载使用。

#### 高级概念

- **异步操作处理？**
Cypress 自动处理异步，通过内部命令队列和重试机制确保步骤按顺序完成，无需 `async/await`。

- **自定义命令 (Custom Commands)？**
在 `cypress/support/commands.js` 中定义：
```javascript
Cypress.Commands.add('login', (user, pass) => { ... });
```

- **网络请求拦截？**
使用 `cy.intercept()` 捕获或 mock 接口。
```javascript
cy.intercept('GET', '/api/data', { fixture: 'data.json' }).as('getData');
cy.wait('@getData');
```

- **Cookie 与本地存储？**
使用 `cy.getCookie()`、`cy.setCookie()`、`cy.setLocalStorage()` 等命令。

- **处理 iframe？**
需要先获取 iframe 元素，然后通过 `.its('contentDocument.body').then(cy.wrap)` 进入其内容区。

#### 最佳实践与调试

- **最佳实践**：
    - 逻辑化组织测试。
    - 保持测试独立。
    - 使用 Page Object 模式。
    - 优先测试核心用户旅程。
    - 利用 CI 自动运行。

- **如何调试？**
    - 使用**时间旅行**回溯步骤。
    - 使用 `.debug()` 或 `debugger`。
    - 查看命令日志中的 Console 输出。
    - 观察 `cy.intercept()` 的网络细节。

- **性能优化**：
    - 并行执行。
    - 使用 `.only` 专注于特定测试。
    - 启用测试重试处理不稳定测试。
    - 使用 API 快速设置状态，避免重复 UI 操作。
