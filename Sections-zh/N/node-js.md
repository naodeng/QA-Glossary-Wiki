# Node.js
[Node.js](#node-js) [Node.js](/wiki/node-js)

### 相关术语：
- JavaScript 运行时 (JavaScript runtime)
- Jest
- Jasmine
[JavaScript runtime](/glossary/javascript-runtime) [Jest](/glossary/jest) [Jasmine](/glossary/jasmine)

### 参见：
- [官方网站](https://nodejs.org/)
- [维基百科](https://en.wikipedia.org/wiki/Node.js)

## 关于 Node.js 的常见问题

#### 基础与重要性
- **什么是 Node.js 及其重要性？**
  Node.js 是一个开源、跨平台的运行时环境，允许在服务器端运行 JavaScript。它基于 Chrome 的 V8 JavaScript 引擎构建，使开发者能够使用 JavaScript 编写命令行工具和服务器端脚本，从而在页面发送到浏览器之前生成动态网页内容。
  **Node.js 的重要性：**
  - **统一语言**：前后端都使用 JavaScript，简化开发并提高团队效率。
  - **异步 I/O**：异步处理 I/O 操作，提供更好的性能和可扩展性，特别适合需要处理并发任务的**测试自动化**系统。
  - **NPM 生态系统**：自带 npm（Node 包管理器），拥有庞大的库和工具仓库，对扩展测试自动化功能非常有利。
  - **微服务架构**：非常适合构建可扩展的系统和集成各种服务。
  - **跨平台**：一次编写，随处运行，是构建平台无关测试工具的理想选择。

- **Node.js 和 JavaScript 有什么区别？**
  - **JavaScript** 是在浏览器中运行的**编程语言**，用于操作 DOM、实现交互。
  - **Node.js** 是允许 JavaScript 在服务器端执行的**运行时环境**。
  区别在于**执行环境**和**应用领域**：JS 传统上运行在浏览器端，而 Node.js 运行在服务器端，用于构建可扩展的网络应用。Node.js 还提供了原生 JS 不具备的非阻塞 I/O 模型和异步编程能力。

- **Node.js 的关键特性有哪些？**
  - **非阻塞 I/O API**：优化高负载下的吞吐量。
  - **异步事件驱动架构**：高效处理大量并发连接。
  - **V8 引擎**：以高性能和速度著称。
  - **流 (Streams)**：异步处理大块数据（如文件、网络通信）。
  - **NPM 生态**：全球最大的开源库生态系统。
  - **REPL (交互式解释器)**：用于快速原型设计和调试代码。
  - **Buffer 和 缓存**：优化数据传输性能。

- **为什么 Node.js 是单线程的？**
  设计为**单线程**是为了优化 Web 环境下的**性能**和**可扩展性**。单线程事件循环利用**非阻塞 I/O** 可以在低开销下管理成千上万的并发连接。同时避免了多线程环境中的线程同步、**死锁**和**竞态条件**等复杂性。不过，Node.js 内部会使用**工作线程 (Worker Threads)** 处理文件系统或重计算任务，并支持 **Cluster 模块** 利用多核 CPU。

- **什么是 Node.js 中的事件驱动编程？**
  这是一种流程由用户操作、系统输出或消息传递等“事件”决定的范式。在 Node.js 中主要由内置的 `EventEmitter` 类实现。此模型非常适合处理 I/O 密集型任务，是实现**非阻塞**特性的关键，**测试自动化**工程师需要理解这一点，以正确结构化异步测试断言。

#### 使用 Node.js
- **如何安装 Node.js？**
  - **Windows/macOS**：从 [nodejs.org](https://nodejs.org/) 下载 **LTS** 或最新版本安装程序。
  - **Ubuntu**：使用 `curl` 脚本添加源后通过 `apt-get` 安装。
  - **CentOS/Fedora**：通过 `yum` 安装。
  - **Arch Linux**：使用 `pacman -S nodejs npm`。
  安装后运行 `node -v` 和 `npm -v` 进行验证。

- **如何更新 Node.js？**
  推荐使用版本管理器：**nvm** (Node Version Manager) 或 **n**。Windows 也可以直接下载覆盖安装，或使用 `npm-windows-upgrade` 工具。

- **如何调试 Node.js 应用？**
  - **内置调试器**：运行 `node inspect script.js`。
  - **Chrome DevTools**：带 `--inspect` 参数启动应用。
  - **VS Code**：使用 `.vscode/launch.json` 配置调试环境。
  - **日志记录**：使用 `console.log()` 追踪。
  - **第三方工具**：如 `ndb`。
  - **单元测试**：使用 Mocha 或 **Jest** 隔离调试。

- **什么是 NPM 及其用法？**
  **Node Package Manager (Node 包管理器)** 用于管理 JS 包。通过 `npm init` 创建 `package.json`，使用 `npm install <package>` 安装依赖。在测试自动化中，常用于安装 Mocha、Jest 或 Selenium WebDriver。通过配置 `scripts` 字段（如 `"test": "mocha"`），可以使用 `npm test` 运行测试。`package-lock.json` 确保各环境依赖版本一致。

- **如何创建服务器？**
  利用内置的 `http` 模块。调用 `http.createServer()` 并监听端口（如 3000）。这对 Mock API 或创建测试环境非常有用。

#### 模块系统
- **什么是 Node.js 模块？**
  模块是封装的代码块，增强了代码的**可维护性**。每个文件被视为一个独立模块，拥有自己的上下文。
  - **定义模块**：使用 `module.exports` 导出。
  - **引入模块**：使用 `require()`。
  Node.js 拥有**内置模块**（如 `fs`, `http`, `path`）和通过 NPM 引入的第三方模块。

- **常用内置模块**：
  - `fs`：文件系统操作。
  - `path`：路径处理。
  - `os`：操作系统工具。
  - `events`：事件触发处理。
  - `stream`：处理流式数据。
  - `child_process`：运行子进程。
  - `crypto`：加密功能。

#### 数据库与异步编程
- **连接数据库**：使用数据库驱动或 **ORM**（如 Sequelize, Mongoose）。
- **CRUD 操作**：通过驱动执行增删改查。推荐使用 **async/await** 编写清晰的异步代码，避免回调地狱。
- **ORM 的作用**：**对象关系映射**允许开发者使用 JS 对象而非 SQL 语句操作数据库，提高开发效率并便于维护。

- **异步模式**：
  - **回调函数 (Callbacks)**：传统方式，易导致回调地狱。
  - **Promise**：链式调用处理结果。
  - **Async/Await**：以同步写法编写异步逻辑，是目前的主流推荐方式。

#### 自动化测试与最佳实践
- **测试框架**：**Mocha** 和 **Jest** 是最流行的选择。
- **中间件 (Middleware)**：常用在 Express 等框架中处理请求生命周期。
- **全局对象**：如 `__filename`, `__dirname`, `process`, `Buffer`。
- **安全性**：输入验证、HTTPS、保持 NPM 包更新、限制权限等。
- **开发工具**：**Nodemon** 可在代码更改时自动重启应用。
