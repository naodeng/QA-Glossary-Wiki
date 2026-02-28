# 节点.js

<!-- TOC START -->
- [相关术语：](#相关术语：)
  - [另请参阅：](#另请参阅：)
- [关于 Node.js 有疑问吗？](#关于-nodejs-有疑问吗？)
  - [基础知识和重要性](#基础知识和重要性)
    - [Node.js 是什么以及为什么它很重要？](#nodejs-是什么以及为什么它很重要？)
    - [Node.js 和 JavaScript 之间有什么区别？](#nodejs-和-javascript-之间有什么区别？)
    - [Node.js 的主要特性是什么？](#nodejs-的主要特性是什么？)
    - [为什么 Node.js 是单线程的？](#为什么-nodejs-是单线程的？)
    - [Node.js 中的事件驱动编程是什么？](#nodejs-中的事件驱动编程是什么？)
  - [使用 Node.js](#使用-nodejs)
    - [如何在系统上安装 Node.js？](#如何在系统上安装-nodejs？)
    - [如何更新 Node.js？](#如何更新-nodejs？)
    - [如何调试 Node.js 应用程序？](#如何调试-nodejs-应用程序？)
    - [什么是 NPM 以及它在 Node.js 中如何使用？](#什么是-npm-以及它在-nodejs-中如何使用？)
    - [如何在 Node.js 中创建服务器？](#如何在-nodejs-中创建服务器？)
  - [Node.js 模块](#nodejs-模块)
    - [Node.js 中的模块是什么？](#nodejs-中的模块是什么？)
    - [如何在 Node.js 中创建和使用模块？](#如何在-nodejs-中创建和使用模块？)
    - [Node.js 中有哪些内置模块？](#nodejs-中有哪些内置模块？)
    - [Node.js 中 module.exports 的用途是什么？](#nodejs-中-moduleexports-的用途是什么？)
    - [如何在 Node.js 应用程序中包含第三方模块？](#如何在-nodejs-应用程序中包含第三方模块？)
  - [Node.js 和数据库](#nodejs-和数据库)
    - [如何将 Node.js 应用程序连接到数据库？](#如何将-nodejs-应用程序连接到数据库？)
    - [如何在 Node.js 中执行 CRUD 操作？](#如何在-nodejs-中执行-crud-操作？)
    - [什么是 ORM 以及它如何在 Node.js 中使用？](#什么是-orm-以及它如何在-nodejs-中使用？)
    - [如何处理 Node.js 中的数据库错误？](#如何处理-nodejs-中的数据库错误？)
  - [高级概念](#高级概念)
    - [Node.js 中的事件循环是什么？](#nodejs-中的事件循环是什么？)
    - [什么是回调地狱以及如何在 Node.js 中避免它？](#什么是回调地狱以及如何在-nodejs-中避免它？)
    - [Node.js 中的 Promise 和 async/await 是什么？](#nodejs-中的-promise-和-asyncawait-是什么？)
    - [Node.js 中的 cluster 模块是什么以及它为什么有用？](#nodejs-中的-cluster-模块是什么以及它为什么有用？)
    - [Node.js 如何处理子进程？](#nodejs-如何处理子进程？)
<!-- TOC END -->

Node.js

是一个开源、跨平台的 JavaScript 运行时环境，允许开发人员在服务器端执行 JavaScript 代码。传统上，JavaScript 主要用于 Web 浏览器中的客户端脚本编写。

Node.js

然而，JavaScript 可以用于在浏览器之外构建可扩展的网络应用程序。基于 Chrome 的 V8 JavaScript 引擎构建，

Node.js

旨在构建快速高效的 Web 应用程序，尤其是 I/O 密集型应用程序。

## 相关术语：

- [JavaScript runtime](../J/javascript-runtime.md)
- [Jest](../J/jest.md)
- [Jasmine](../J/jasmine.md)

### 另请参阅：

- [Official Website](https://nodejs.org/)
- [Wikipedia](https://en.wikipedia.org/wiki/Node.js)

## 关于 Node.js 有疑问吗？

### 基础知识和重要性

#### Node.js 是什么以及为什么它很重要？

[Node.js](../N/node-js.md) 是一个开源的跨平台运行时环境，允许您在服务器端运行 JavaScript。它基于 Chrome 的 V8 JavaScript 引擎构建，使开发人员能够使用 JavaScript 编写命令行工具和服务器端脚本，即在服务器端运行脚本以生成动态网页内容，然后再将页面发送到用户的 Web 浏览器。
  **[Node.js](../N/node-js.md) 的重要性：**

- **统一语言**：[Node.js](../N/node-js.md)使用JavaScript，这意味着客户端和服务器端可以使用相同的语言。这简化了开发，并可以提高团队之间的效率和理解。
  - **异步I/O**：它异步处理I/O操作，这可以带来更好的性能和可扩展性，特别是对于需要大量I/O操作的应用程序，例如可能需要同时处理多个任务的[test automation](../T/test-automation.md)系统。
  - **NPM 生态系统**：[Node.js](../N/node-js.md) 附带 npm（节点包管理器），这是一个庞大的库和工具存储库，这对 [test automation](../T/test-automation.md) 非常有利，提供了丰富的模块来扩展功能并减少开发时间。
  - **微服务架构**：它非常适合构建微服务，微服务是构建可扩展系统的流行架构风格，包括可能需要与各种服务和工具集成的[test automation](../T/test-automation.md)框架。
  - **跨平台**：[Node.js](../N/node-js.md) 应用程序无需修改即可在各种操作系统上运行，使其成为需要与平台无关的[test automation](../T/test-automation.md) 工具的理想选择。
  - **社区和支持**：它拥有一个庞大而活跃的社区，这意味着丰富的资源、支持和对技术的不断改进，这对于维护和更新[test automation](../T/test-automation.md)框架是有利的。
  - **统一语言**：[Node.js](../N/node-js.md)使用JavaScript，这意味着客户端和服务器端可以使用相同的语言。这简化了开发，并可以提高团队之间的效率和理解。
  - **异步I/O**：它异步处理I/O操作，这可以带来更好的性能和可扩展性，特别是对于需要大量I/O操作的应用程序，例如可能需要同时处理多个任务的[test automation](../T/test-automation.md)系统。
  - **NPM 生态系统**：[Node.js](../N/node-js.md) 附带 npm（节点包管理器），这是一个庞大的库和工具存储库，这对 [test automation](../T/test-automation.md) 非常有利，提供了丰富的模块来扩展功能并减少开发时间。
  - **微服务架构**：它非常适合构建微服务，微服务是构建可扩展系统的流行架构风格，包括可能需要与各种服务和工具集成的[test automation](../T/test-automation.md)框架。
  - **跨平台**：[Node.js](../N/node-js.md) 应用程序无需修改即可在各种操作系统上运行，使其成为需要与平台无关的[test automation](../T/test-automation.md) 工具的理想选择。
  - **社区和支持**：拥有庞大且活跃的社区，这意味着丰富的资源、支持以及对技术的不断改进，这对于维护和更新[test automation](../T/test-automation.md)框架是有利的。

#### Node.js 和 JavaScript 之间有什么区别？

JavaScript 是一种**编程语言**，作为文档对象模型 (DOM) 的一部分在 Web 浏览器中运行，支持动态内容和交互式网页。它是网络脚本语言，旨在轻量级和多功能。
  另一方面，[Node.js](../N/node-js.md) 是一个**运行时环境**，允许 JavaScript 在服务器端执行。它基于 Chrome 的 V8 JavaScript 引擎构建，使 JavaScript 能够执行通常为后端语言保留的操作，例如文件系统访问和网络通信。
  主要区别在于它们的**执行环境**和**应用程序**。 JavaScript 传统上在浏览器中运行并操作网页内容，响应用户交互。 [Node.js](../N/node-js.md) 在服务器上运行，而不是在浏览器中运行，用于构建可扩展的网络应用程序。
  [Node.js](../N/node-js.md) 还提供了**非阻塞 I/O 模型**和**异步编程**，它们不是 JavaScript 本身固有的，而是 [Node.js](../N/node-js.md) 运行时的一部分。
  这是代码中的一个简单类比：

  ```
  // JavaScript in a browser
  document.getElementById('button').addEventListener('click', function() {
    alert('Button clicked!');
  });
  // Node.js on a server
  const http = require('http');
  http.createServer((request, response) => {
    response.writeHead(200, {'Content-Type': 'text/plain'});
    response.end('Hello World\n');
  }).listen(3000);
  ```总而言之，JavaScript 是一种语言，而 [Node.js](../N/node-js.md) 是将 JavaScript 的功能扩展到非浏览器环境的平台。

#### Node.js 的主要特性是什么？

[Node.js](../N/node-js.md) 提供**非阻塞 I/O [API](../A/api.md)**，可优化实时 Web 应用程序的应用程序吞吐量和可扩展性。其**异步事件驱动架构**确保[Node.js](../N/node-js.md) 可以有效地处理大量并发连接。
  **libuv 库** 支持 [Node.js](../N/node-js.md)，提供一组跨平台的 I/O 原语。 [Node.js](../N/node-js.md) 构建于 **V8 JavaScript 运行时**，它以其速度和性能而闻名。
  **流**是数据的集合 - 例如数组或字符串，您可以异步读取或写入。 [Node.js](../N/node-js.md) 使用流来处理块中的数据，这对于处理大量数据（例如文件或网络通信）非常有效。
  [Node.js](../N/node-js.md) 拥有一个称为 npm 的**软件包生态系统**，它是世界上最大的开源库生态系统。它允许轻松共享和重用代码。
  **REPL（读取-评估-打印循环）**是用于测试 [Node.js](../N/node-js.md)/JavaScript 代码的工具。它是一个处理 [Node.js](../N/node-js.md) 表达式的交互式 shell。该环境允许快速原型设计和调试。
  [Node.js](../N/node-js.md) 支持数据的**缓冲区和缓存**，这是数据从一个地方传输到另一个地方的临时保存点。这提高了 I/O 操作的性能。
  最后，[Node.js](../N/node-js.md) 具有用于服务器端和客户端脚本的**统一[API](../A/api.md)**。这意味着两者通常使用相同的模式和方法，这可以简化同构应用程序的开发过程。

#### 为什么 Node.js 是单线程的？

[Node.js](../N/node-js.md) 被设计为**单线程**，以优化 Web 环境中的**性能**和**可扩展性**。该架构允许[Node.js](../N/node-js.md) 以较低的开销处理大量并发连接。单线程事件循环是 [Node.js](../N/node-js.md) 的核心，可以管理许多连接，因为它执行非阻塞 I/O 操作，这意味着服务器可以在等待 I/O 操作完成的同时继续处理其他任务。
  单线程模型还简化了开发，因为它消除了与线程管理和同步相关的复杂性。开发人员无需担心多线程环境中常见的**死锁**或**竞争条件**。
  但是，[Node.js](../N/node-js.md) 不限于单个线程；它使用**工作线程**来执行文件系统操作或繁重计算等任务，确保这些任务不会阻塞主事件循环。 **集群模块**允许运行多个[Node.js](../N/node-js.md)工作进程，这些进程可以共享服务器端口，从而实现多个CPU核心的负载平衡。
  这是使用 cluster 模块的示例：

  ```
  const cluster = require('cluster');
  const http = require('http');
  const numCPUs = require('os').cpus().length;
  if (cluster.isMaster) {
    for (let i = 0; i < numCPUs; i++) {
      cluster.fork();
    }
  } else {
    http.createServer((req, res) => {
      res.writeHead(200);
      res.end('Hello World\n');
    }).listen(8000);
  }
  ```在此代码中，`cluster.isMaster` 检查确定当前进程是否为主进程，然后创建工作进程。每个工作进程都会创建一个监听同一端口的 HTTP 服务器。

#### Node.js 中的事件驱动编程是什么？

[Node.js](../N/node-js.md) 中的事件驱动编程是一种范例，其中程序流程由用户操作、传感器输出或来自其他程序的消息传递等事件确定。在[Node.js](../N/node-js.md) 中，这是由**EventEmitter** 类实现的，它是**events** 模块的一部分，也是[Node.js](../N/node-js.md) 的内置模块之一。
  事件驱动编程特别适合 I/O 密集型任务，这在 Web 服务器和实时应用程序中很常见。 [Node.js](../N/node-js.md) 使用此模型来处理异步操作，使其能够执行非阻塞 I/O 任务。
  以下是 [Node.js](../N/node-js.md) 中事件驱动编程的基本示例：

  ```
  const EventEmitter = require('events');
  class MyEmitter extends EventEmitter {}
  const myEmitter = new MyEmitter();
  myEmitter.on('event', () => {
    console.log('An event occurred!');
  });
  myEmitter.emit('event');
  ```在此代码段中，`MyEmitter` 是`EventEmitter` 的扩展。我们实例化 `myEmitter`，然后使用 `.on()` 方法来监听“event”事件。当 `myEmitter.emit('event')` 被调用时，附加到该事件的回调函数被执行，记录“发生了事件！”到控制台。
  此模式对于处理未立即完成的任务至关重要，例如读取文件、发出 HTTP 请求或查询 [database](../D/database.md)。通过响应事件，[Node.js](../N/node-js.md) 可以继续执行其他代码而不是等待，这是其非阻塞性质的一个关键方面。这种方法对于 [test automation](../T/test-automation.md) 工程师来说至关重要，因为它影响测试和断言在异步环境中的构建和执行方式。

### 使用 Node.js

#### 如何在系统上安装 Node.js？

要在您的系统上安装 **[Node.js](../N/node-js.md)**，请按照以下特定于平台的说明进行操作：
  ### 对于 Windows 和 macOS：

1. 访问 Node.js 官方网站：
    [nodejs.org](https://nodejs.org/)
    。

2. 单击
    **长期支持**
    （长期支持）或
    **当前**
    版本下载按钮，根据您的要求。

3. 运行下载的安装程序并按照提示完成安装。
  ### 对于基于 Ubuntu 的发行版：
  打开终端并运行以下命令：

  ```
  curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
  sudo apt-get install -y nodejs
  ```将 `14.x` 替换为您要安装的版本。
  ### 对于 CentOS、Fedora 和基于 Red Hat 的发行版：
  在终端中执行这些命令：

  ```
  curl -sL https://rpm.nodesource.com/setup_14.x | sudo bash -
  sudo yum install nodejs
  ```再次将 `14.x` 替换为所需的版本。
  ### 对于 Arch Linux：
  使用包管理器`pacman`来安装[Node.js](../N/node-js.md)：

  ```
  sudo pacman -S nodejs npm
  ```### 验证：
  安装完成后，通过检查[Node.js](../N/node-js.md)和npm的版本来验证安装：

  ```
  node -v
  npm -v
  ```这将输出 [Node.js](../N/node-js.md) 和 npm 的已安装版本，确认安装成功。

1. 访问 Node.js 官方网站：
    [nodejs.org](https://nodejs.org/)
    。

2. 单击
    **长期支持**
    （长期支持）或
    **当前**
    版本下载按钮，根据您的要求。

3. 运行下载的安装程序并按照提示完成安装。

#### 如何更新 Node.js？

要更新 [Node.js](../N/node-js.md)，您可以使用 `nvm`（节点版本管理器）或 `n`（对于基于 Unix 的系统）等包管理器，或者直接从 [Node.js](../N/node-js.md) 网站（对于 Windows）下载最新版本。
  **使用nvm：**

1. 打开您的终端。
  2. 跑步
    `nvm ls`
    列出已安装的版本。

3. 更新到最新版本
    `nvm install node`
    。

4.使用切换到新版本
    `nvm use node`
    。

5. 验证更新
    `node -v`
    。
  **使用 n:**

1. 打开您的终端。
  2. 安装
    `n`
    全球范围内与
    `npm install -g n`
    。

3. 将 Node.js 更新到最新版本
    `n latest`
    。

4. 验证更新
    `node -v`
    。
  **对于 Windows：**

1. 前往
    [Node.js website](https://nodejs.org/)
    。

2. 下载最新版本的 Windows Installer。
  3. 运行安装程序并按照提示更新 Node.js。
  4. 重新启动终端并使用以下命令验证更新
    `node -v`
    。
  **使用npm（跨平台）：**
  如果您安装了 npm，则可以在 Windows 上使用 `npm` 包 `npm-windows-upgrade` 或在基于 Unix 的系统上使用 `npm` 本身将 [Node.js](../N/node-js.md) 更新到最新稳定版本：

  ```
  npm install -g npm-windows-upgrade
  npm-windows-upgrade
  ```或者在基于 Unix 的系统上：

  ```
  npm cache clean -f
  npm install -g n
  n stable
  ```更新后，始终确保您的全局 npm 包和本地项目依赖项与新的 [Node.js](../N/node-js.md) 版本兼容。

1. 打开您的终端。
  2. 跑步
    `nvm ls`
    列出已安装的版本。

3. 更新到最新版本
    `nvm install node`
    。

4.使用切换到新版本
    `nvm use node`
    。

5. 验证更新
    `node -v`
    。

1. 打开您的终端。
  2. 安装
    `n`
    全球范围内与
    `npm install -g n`
    。

3. 将 Node.js 更新到最新版本
    `n latest`
    。

4. 验证更新
    `node -v`
    。

1. 前往
    [Node.js website](https://nodejs.org/)
    。

2. 下载最新版本的 Windows Installer。
  3. 运行安装程序并按照提示更新 Node.js。
  4. 重新启动终端并使用以下命令验证更新
    `node -v`
    。

#### 如何调试 Node.js 应用程序？

可以使用多种方法调试 [Node.js](../N/node-js.md) 应用程序：
  **内置调试器**：[Node.js](../N/node-js.md) 附带一个内置 CLI 调试器，可以通过运行 `node inspect yourScript.js` 来启动。您可以设置断点、单步调试代码以及​​检查变量。
  **Chrome DevTools**：通过使用 `--inspect` 标志（例如 `node --inspect yourScript.js`）启动 [Node.js](../N/node-js.md) 应用程序，您可以连接到 Chrome DevTools 以获得更直观的调试体验。

  ```
  node --inspect yourScript.js
  ```**Visual Studio Code**：VS Code 具有出色的 [Node.js](../N/node-js.md) 调试支持。通过在项目中创建 `.vscode/launch.json` 文件并设置适当的配置来配置调试会话。

  ```
  {
    "version": "0.2.0",
    "configurations": [
      {
        "type": "node",
        "request": "launch",
        "name": "Launch Program",
        "skipFiles": ["<node_internals>/**"],
        "program": "${workspaceFolder}/yourScript.js"
      }
    ]
  }
  ```**日志记录**：有时，简单的 `console.log()` 语句可以帮助跟踪执行流程并了解应用程序中不同点的变量状态。
  **第三方工具**：`node-inspector` 或 `ndb` 等工具可以通过 npm 安装，并提供额外的调试功能。
  **[Unit Testing](../U/unit-testing.md)**：使用 Mocha 或 [Jest](../J/jest.md) 等库编写单元测试可以帮助隔离和调试应用程序的特定部分。
  **分析**：使用[Node.js](../N/node-js.md) 分析工具（例如`--prof`）来识别性能瓶颈。
  请记住在将应用程序部署到生产环境之前删除或注释掉调试代码，以避免性能影响和潜在的安全风险。

#### 什么是 NPM 以及它在 Node.js 中如何使用？

NPM 或 **Node Package Manager**，是用于管理和共享 [Node.js](../N/node-js.md) 项目中的 JavaScript 包的工具。它提供了一个命令行界面 (CLI)，用于安装、更新和删除包以及管理项目依赖项。
  要使用 NPM，通常首先使用 `npm init` 初始化一个新的 [Node.js](../N/node-js.md) 项目，这会创建一个 `package.json` 文件。该文件列出了项目的依赖项和其他元数据。要添加包，请使用 `npm install <package-name>`，它从 NPM 注册表下载包并将其添加到 `node_modules` 目录和 `package.json` 文件。
  对于[test automation](../T/test-automation.md)，可以使用NPM安装测试框架和工具，例如Mocha、[Jest](../J/jest.md)或[Selenium](../S/selenium.md) [WebDriver](../W/webdriver.md)。这是安装 Mocha 的示例：

  ```
  npm install mocha --save-dev
  ````--save-dev` 标志将 Mocha 添加到 `package.json` 中的 `devDependencies` 中，表明它是仅开发依赖项。
  NPM 还支持脚本，可以在`package.json` 中定义脚本并使用`npm run <script-name>` 运行。例如，您可以定义 [test script](../T/test-script.md) 来运行自动化测试：

  ```
  "scripts": {
    "test": "mocha"
  }
  ```然后，您可以使用以下命令执行测试：

  ```
  npm test
  ```NPM 确保所有开发人员和 CI/CD 管道使用相同的包版本，这要归功于 `package-lock.json` 文件，它锁定了安装的确切包版本。这种一致性对于可靠、可重复的[test automation](../T/test-automation.md) 至关重要。

#### 如何在 Node.js 中创建服务器？

在[Node.js](../N/node-js.md) 中创建服务器通常涉及使用内置`http` 模块。下面是如何设置基本 HTTP 服务器的简洁示例：

  ```
  const http = require('http');
  const server = http.createServer((req, res) => {
    res.statusCode = 200;
    res.setHeader('Content-Type', 'text/plain');
    res.end('Hello, World!\n');
  });
  const PORT = 3000;
  server.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
  });
  ```在此示例中，使用请求侦听器函数调用 `http.createServer()`，每次服务器收到请求时都会调用该函数。 `req` 参数表示请求对象，而`res` 是响应对象。我们将状态代码设置为 200（正常），将内容类型设置为纯文本。响应以使用 `res.end()` 的消息结束。
  服务器侦听指定端口（在本例中为 3000），一旦准备就绪，就会调用回调函数，将消息记录到控制台。
  对于[test automation](../T/test-automation.md) 工程师来说，这个基本服务器可以作为模拟[APIs](../A/api.md) 或创建[test environment](../T/test-environment.md) 的起点。它可以根据需要使用路由、中间件和更复杂的请求处理逻辑进行扩展。请记住处理实际应用程序中的错误和边缘情况，以确保稳定性和可靠性。

### Node.js 模块

#### Node.js 中的模块是什么？

[Node.js](../N/node-js.md) 中的模块是封装的代码块，可以在应用程序的不同部分甚至不同应用程序之间共享和重用。它们提供了一种将代码组织到单独的文件和命名空间中的方法，从而促进模块化和[maintainability](../M/maintainability.md)。
  [Node.js](../N/node-js.md) 中的每个模块都有自己的上下文，这意味着除非显式导出，否则无法从外部访问模块中定义的变量和函数。要在另一个文件中使用模块，您必须使用 `require` 函数来请求它，该函数读取模块文件，执行它，然后返回模块的 `exports` 对象。
  以下是如何定义简单模块并导出其功能的示例：

  ```
  // myModule.js
  const myFunction = () => {
    console.log('Function from myModule');
  };
  module.exports = myFunction;
  ```要在另一个文件中使用 `myModule.js` 导出的函数：

  ```
  // app.js
  const myFunction = require('./myModule');
  myFunction(); // Outputs: Function from myModule
  ```[Node.js](../N/node-js.md) 还具有一组**内置模块**，提供各种功能，例如文件系统访问、HTTP 网络等。这些模块可以按照与自定义模块相同的方式包含，但不需要文件路径。

  ```
  const fs = require('fs'); // fs is a built-in module for file system operations
  ```模块可以导出多个值，例如函数、对象或基元，方法是将它们附加到 `exports` 对象或直接设置 `module.exports`。该模块化系统基于 CommonJS 模块模式。

#### 如何在 Node.js 中创建和使用模块？

在 [Node.js](../N/node-js.md) 中创建模块涉及将相关代码封装到单个文件中，然后可以在 [Node.js](../N/node-js.md) 应用程序中重复使用该文件。要创建模块，请按照下列步骤操作：

1. **创建一个新文件**
    与一个
    `.js`
    扩展名，例如
    `calculator.js`
    。

2. **编写模块代码**
    在此文件内。定义您想要供其他文件使用的函数、对象或任何其他变量。

  ```
  // calculator.js
  function add(a, b) {
    return a + b;
  }
  function subtract(a, b) {
    return a - b;
  }
  module.exports = { add, subtract };
  ```

1. 使用
    `module.exports`
    到
    **导出模块的功能**
    你想要暴露的。这可以是函数、对象、类等。
  要在另一个文件中使用该模块：

1. **需要模块**
    使用
    `require()`
    函数与模块文件的路径。

  ```
  // app.js
  const calculator = require('./calculator');
  const sum = calculator.add(5, 10);
  const difference = calculator.subtract(10, 5);
  console.log(sum); // Outputs: 15
  console.log(difference); // Outputs: 5
  ```

1. **调用方法**
    或访问您从模块导出的属性。
  请记住，[Node.js](../N/node-js.md) 使用 CommonJS 模块系统，每个文件都被视为一个单独的模块。通过使用`require()` 和`module.exports`，您可以创建模块化、可维护且可重用的代码，这在[test automation](../T/test-automation.md) 中特别有用，可用于构建[test cases](../T/test-case.md) 和实用函数。

1. **创建一个新文件**
    与一个
    `.js`
    扩展名，例如
    `calculator.js`
    。

2. **编写模块代码**
    在此文件内。定义您想要供其他文件使用的函数、对象或任何其他变量。

1. 使用
    `module.exports`
    到
    **导出模块的功能**
    你想要暴露的。这可以是函数、对象、类等。

1. **需要模块**
    使用
    `require()`
    函数与模块文件的路径。

1. **调用方法**
    或访问您从模块导出的属性。

#### Node.js 中有哪些内置模块？

[Node.js](../N/node-js.md) 附带各种内置模块，无需外部库即可提供基础功能。其中一些包括：

- **fs** ：提供文件系统操作，例如读取和写入文件。

    ```
    const fs = require('fs');
    ```

- **http** ：允许创建 HTTP 服务器和客户端。

    ```
    const http = require('http');
    ```

- **https** ：类似于
    `http`
    但对于 HTTPS。

    ```
    const https = require('https');
    ```

- **path** ：提供用于处理和转换文件路径的实用程序。

    ```
    const path = require('path');
    ```

- **os** ：提供与操作系统相关的基本实用功能。

    ```
    const os = require('os');
    ```

- **util** ：包含用于调试和弃用处理的实用程序函数。

    ```
    const util = require('util');
    ```

- **events** ：提供EventEmitter类来处理事件。

    ```
    const EventEmitter = require('events');
    ```

- **stream**：允许处理流数据，例如以块的形式读取和写入文件。

    ```
    const stream = require('stream');
    ```

- **child_process** ：启用运行子进程来执行其他程序。

    ```
    const { exec } = require('child_process');
    ```

- **url** ：提供 URL 解析和解析的实用程序。

    ```
    const url = require('url');
    ```

- **querystring** ：解析和格式化 URL 查询字符串。

    ```
    const querystring = require('querystring');
    ```

- **crypto** ：提供加密功能，包括一组 OpenSSL 散列、HMAC、密码、解密、签名和验证功能的包装器。

    ```
    const crypto = require('crypto');
    ```

- **buffer** ：使用 Buffer 类直接处理二进制数据。

    ```
    const Buffer = require('buffer').Buffer;
    ```

- **dns** ：提供执行名称解析的功能。

    ```
    const dns = require('dns');
    ```

- **net** ：提供异步网络包装器，用于创建基于流的 TCP 或 IPC 服务器和客户端。

    ```
    const net = require('net');
    ```这些模块是 [Node.js](../N/node-js.md) 的组成部分，并且可以通过 `require` 函数包含在您的应用程序中。它们提供了轻松构建复杂应用程序所需的工具。

- **fs** ：提供文件系统操作，例如读取和写入文件。

    ```
    const fs = require('fs');
    ```

- **http** ：允许创建 HTTP 服务器和客户端。

    ```
    const http = require('http');
    ```

- **https** ：类似于
    `http`
    但对于 HTTPS。

    ```
    const https = require('https');
    ```

- **path** ：提供用于处理和转换文件路径的实用程序。

    ```
    const path = require('path');
    ```

- **os** ：提供与操作系统相关的基本实用功能。

    ```
    const os = require('os');
    ```

- **util** ：包含用于调试和弃用处理的实用程序函数。

    ```
    const util = require('util');
    ```

- **events** ：提供EventEmitter类来处理事件。

    ```
    const EventEmitter = require('events');
    ```

- **stream**：允许处理流数据，例如以块的形式读取和写入文件。

    ```
    const stream = require('stream');
    ```

- **child_process** ：启用运行子进程来执行其他程序。

    ```
    const { exec } = require('child_process');
    ```

- **url** ：提供 URL 解析和解析的实用程序。

    ```
    const url = require('url');
    ```

- **querystring** ：解析和格式化 URL 查询字符串。

    ```
    const querystring = require('querystring');
    ```

- **crypto** ：提供加密功能，包括一组 OpenSSL 散列、HMAC、密码、解密、签名和验证功能的包装器。

    ```
    const crypto = require('crypto');
    ```

- **buffer** ：使用 Buffer 类直接处理二进制数据。

    ```
    const Buffer = require('buffer').Buffer;
    ```

- **dns** ：提供执行名称解析的功能。

    ```
    const dns = require('dns');
    ```

- **net** ：提供异步网络包装器，用于创建基于流的 TCP 或 IPC 服务器和客户端。

    ```
    const net = require('net');
    ```

#### Node.js 中 module.exports 的用途是什么？

在[Node.js](../N/node-js.md)中，`module.exports`是当前模块在另一个模块中`require`d时返回的对象。本质上，它定义了模块中的**可导出实体**，例如函数、对象或原语，使它们可供其他模块访问。
  以下是如何使用 `module.exports` 的基本示例：

  ```
  // In a file named greet.js
  function sayHello(name) {
    return `Hello, ${name}!`;
  }
  module.exports = sayHello;
  ```在另一个文件中，您可以使用导出的函数：

  ```
  // In another file
  const greet = require('./greet');
  console.log(greet('World')); // Outputs: Hello, World!
  ````module.exports` 还可以通过将多个实体附加到 `exports` 对象来导出它们：

  ```
  // In greet.js
  function sayHello(name) {
    return `Hello, ${name}!`;
  }
  function sayGoodbye(name) {
    return `Goodbye, ${name}!`;
  }
  module.exports = {
    sayHello,
    sayGoodbye
  };
  ```然后，您可以解构以使用多个导出函数：

  ```
  // In another file
  const { sayHello, sayGoodbye } = require('./greet');
  console.log(sayHello('Alice')); // Outputs: Hello, Alice!
  console.log(sayGoodbye('Bob')); // Outputs: Goodbye, Bob!
  ```这种机制对于创建**模块化**和**可维护**代码库至关重要，其中每个模块仅向应用程序的其余部分公开必要的部分，从而增强**封装性**和**可重用性**。

#### 如何在 Node.js 应用程序中包含第三方模块？

要在 [Node.js](../N/node-js.md) 应用程序中包含第三方模块，请使用 **npm** （节点包管理器）或 **yarn**，它们是用于管理包的命令行工具。请按照下列步骤操作：

1. **通过运行 `npm init` 或 `yarn init` 初始化您的项目**（如果尚未完成）。这将创建一个`package.json` 文件来跟踪项目的依赖项。
  2. **通过运行`npm install <module-name>` 或`yarn add <module-name>` 安装第三方模块**。将 `<module-name>` 替换为您要包含的模块的实际名称。此命令将模块及其依赖项下载到`node_modules` 目录并更新`package.json` 文件。
  3. **使用 `require()` 函数在您的应用程序代码中需要该模块**。例如：
    此行导入 `express` 模块，您现在可以在应用程序中使用该模块。

    ```
    const express = require('express');
    ```

4. **如果仅需要用于开发目的（例如，测试框架），请使用 `--save-dev` 标志将模块保存为开发依赖项**：
    或对于纱线：

    ```
    npm install <module-name> --save-dev
    ```

    ```
    yarn add <module-name> --dev
    ```

5. **根据模块的文档调用其函数或类，在代码中使用该模块**。
  请记住**将 `package.json` 和 `package-lock.json` 或 `yarn.lock`** 文件提交到版本控制系统，以确保其他开发人员可以安装相同的依赖项。但是，`node_modules` 目录通常添加到`.gitignore` 中，因为它可以使用`npm install` 或`yarn install` 轻松重建。

1. **通过运行 `npm init` 或 `yarn init` 初始化您的项目**（如果尚未完成）。这将创建一个`package.json` 文件来跟踪项目的依赖项。
  2. **通过运行`npm install <module-name>` 或`yarn add <module-name>` 安装第三方模块**。将 `<module-name>` 替换为您要包含的模块的实际名称。此命令将模块及其依赖项下载到`node_modules` 目录并更新`package.json` 文件。
  3. **使用 `require()` 函数在您的应用程序代码中需要该模块**。例如：
    此行导入 `express` 模块，您现在可以在应用程序中使用该模块。

    ```
    const express = require('express');
    ```

4. **如果仅需要用于开发目的（例如，测试框架），请使用 `--save-dev` 标志将模块保存为开发依赖项**：
    或对于纱线：

    ```
    npm install <module-name> --save-dev
    ```

    ```
    yarn add <module-name> --dev
    ```

5. **根据模块的文档调用其函数或类，在代码中使用该模块**。

### Node.js 和数据库

#### 如何将 Node.js 应用程序连接到数据库？

要将 [Node.js](../N/node-js.md) 应用程序连接到 [database](../D/database.md)，您通常使用 **[database](../D/database.md) 驱动程序** 或与您选择的 [database](../D/database.md) 兼容的 **ORM（对象关系映射）** 库。以下是使用 **MySQL** [database](../D/database.md) 驱动程序作为示例的一般过程：

1. **使用 npm 安装 [database](../D/database.md) 驱动程序**。对于 MySQL，您将运行：

    ```
    npm install mysql
    ```

2. **在您的 [Node.js](../N/node-js.md) 应用程序中导入驱动程序**：

    ```
    const mysql = require('mysql');
    ```

3. **使用必要的凭据创建到 [database](../D/database.md) 的连接**：

    ```
    const connection = mysql.createConnection({
      host: 'localhost',
      user: 'your_username',
      password: 'your_password',
      database: 'your_database_name'
    });
    ```

4. **打开连接**并处理任何错误：

    ```
    connection.connect(error => {
      if (error) throw error;
      console.log('Connected to the database.');
    });
    ```

5. **使用连接执行[database](../D/database.md)操作**，例如查询：

    ```
    connection.query('SELECT * FROM your_table', (error, results, fields) => {
      if (error) throw error;
      // Process results here
    });
    ```

6. **完成后关闭连接**：

    ```
    connection.end();
    ```对于其他 [databases](../D/database.md)（如 PostgreSQL 或 MongoDB），您可以使用它们各自的驱动程序（`pg` 用于 PostgreSQL，`mongodb` 用于 MongoDB 等）并遵循类似的过程。如果使用像 Sequelize 这样的 ORM，该过程将涉及定义模型并使用 ORM 的方法与 [database](../D/database.md) 进行交互。始终优雅地处理错误并确保正确关闭连接以避免资源泄漏。

1. **使用 npm 安装 [database](../D/database.md) 驱动程序**。对于 MySQL，您将运行：

    ```
    npm install mysql
    ```

2. **在您的 [Node.js](../N/node-js.md) 应用程序中导入驱动程序**：

    ```
    const mysql = require('mysql');
    ```

3. **使用必要的凭据创建到 [database](../D/database.md) 的连接**：

    ```
    const connection = mysql.createConnection({
      host: 'localhost',
      user: 'your_username',
      password: 'your_password',
      database: 'your_database_name'
    });
    ```

4. **打开连接**并处理任何错误：

    ```
    connection.connect(error => {
      if (error) throw error;
      console.log('Connected to the database.');
    });
    ```

5. **使用连接执行[database](../D/database.md)操作**，例如查询：

    ```
    connection.query('SELECT * FROM your_table', (error, results, fields) => {
      if (error) throw error;
      // Process results here
    });
    ```

6. **完成后关闭连接**：

    ```
    connection.end();
    ```

#### 如何在 Node.js 中执行 CRUD 操作？

要在 [Node.js](../N/node-js.md) 中执行 CRUD 操作，您通常使用驱动程序或 ORM 与 [database](../D/database.md) 进行交互。下面是一个使用流行的 MongoDB 和 Mongoose ORM 的简洁示例：
  **创建** - 将新文档插入集合中：

  ```
  const mongoose = require('mongoose');
  const { Schema } = mongoose;
  const userSchema = new Schema({ name: String, age: Number });
  const User = mongoose.model('User', userSchema);
  const newUser = new User({ name: 'Alice', age: 30 });
  newUser.save(err => {
    if (err) return handleError(err);
    // Document saved
  });
  ```**阅读** - 从集合中获取文档：

  ```
  User.find({ age: { $gte: 18 } }, (err, users) => {
    if (err) return handleError(err);
    // users is an array of adult users
  });
  ```**更新** - 修改现有文档：

  ```
  User.updateOne({ name: 'Alice' }, { age: 31 }, err => {
    if (err) return handleError(err);
    // Document updated
  });
  ```**删除** - 要从集合中删除文档：

  ```
  User.deleteOne({ name: 'Alice' }, err => {
    if (err) return handleError(err);
    // Document deleted
  });
  ```请记住适当地处理错误，可能使用 `handleError` 函数。另外，在执行这些操作之前，请确保您已建立与[database](../D/database.md) 的连接。使用 `async/await` 来获得更干净的异步代码，避免回调地狱。

#### 什么是 ORM 以及它如何在 Node.js 中使用？

ORM 代表**对象关系映射**，这是一种编程技术，用于在面向对象编程语言中的不兼容类型系统之间转换数据。在[Node.js](../N/node-js.md) 上下文中，ORM 允许开发人员使用JavaScript 对象而不是[SQL](../S/sql.md) 查询与[database](../D/database.md) 进行交互。
  ORM 在关系 [database](../D/database.md) 上提供了高级抽象，可以更轻松地操作数据。这意味着您可以使用 JavaScript 编写 [database](../D/database.md) 查询，这对于可能不熟悉 [SQL](../S/sql.md) 语法的开发人员特别有用。
  以下是 ORM 在 [Node.js](../N/node-js.md) 中的典型使用方式：

1. **安装 ORM 包** ：选择一个 ORM（例如 Sequelize、TypeORM 或 Bookshelf），然后使用 npm 安装它。

    ```
    npm install sequelize
    ```

2. **使用 [database](../D/database.md) 详细信息配置 ORM** ：通过提供凭据和其他配置详细信息来设置与数据库的连接。

    ```
    const Sequelize = require('sequelize');
    const sequelize = new Sequelize('database', 'username', 'password', {
      host: 'localhost',
      dialect: 'mysql'
    });
    ```

3. **定义模型**：创建代表数据库中表的模型，将对象属性映射到表列。

    ```
    const User = sequelize.define('user', {
      username: Sequelize.STRING,
      birthday: Sequelize.DATE
    });
    ```

4. **执行CRUD操作**：使用ORM方法创建、读取、更新和删除数据库中的记录。

    ```
    User.create({
      username: 'johndoe',
      birthday: new Date(1980, 6, 20)
    });
    ```使用 ORM 可以帮助简化[database](../D/database.md) 交互、减少[SQL](../S/sql.md) 样板文件并改进代码[maintainability](../M/maintainability.md)。然而，了解 ORM 可能带来的潜在性能开销和复杂性非常重要，尤其是对于复杂查询。

1. **安装 ORM 包** ：选择一个 ORM（例如 Sequelize、TypeORM 或 Bookshelf），然后使用 npm 安装它。

    ```
    npm install sequelize
    ```

2. **使用 [database](../D/database.md) 详细信息配置 ORM** ：通过提供凭据和其他配置详细信息来设置与数据库的连接。

    ```
    const Sequelize = require('sequelize');
    const sequelize = new Sequelize('database', 'username', 'password', {
      host: 'localhost',
      dialect: 'mysql'
    });
    ```

3. **定义模型**：创建代表数据库中表的模型，将对象属性映射到表列。

    ```
    const User = sequelize.define('user', {
      username: Sequelize.STRING,
      birthday: Sequelize.DATE
    });
    ```

4. **执行CRUD操作**：使用ORM方法创建、读取、更新和删除数据库中的记录。

    ```
    User.create({
      username: 'johndoe',
      birthday: new Date(1980, 6, 20)
    });
    ```

#### 如何处理 Node.js 中的数据库错误？

处理[Node.js](../N/node-js.md) 中的[database](../D/database.md) 错误通常涉及实现错误处理机制，以捕获并响应[database](../D/database.md) 操作期间可能出现的问题。这是一个简洁的指南：
  **对同步代码使用 try-catch**：使用同步 [database](../D/database.md) 操作时，将代码包装在 `try-catch` 块中以处理错误。

  ```
  try {
    // Synchronous database operation
  } catch (error) {
    // Handle error
  }
  ```**利用 Promise 和 async/await 实现异步代码**：大多数 [Node.js](../N/node-js.md) [database](../D/database.md) 库都会返回异步操作的 Promise。将`async/await` 与`try-catch` 一起使用以进行更清晰的错误处理。

  ```
  async function queryDatabase() {
    try {
      const result = await database.query('SELECT * FROM table');
      // Process result
    } catch (error) {
      // Handle error
    }
  }
  ```**处理承诺拒绝**：始终使用 `.catch()` 处理承诺拒绝，以防止未处理的承诺拒绝。

  ```
  database.query('SELECT * FROM table')
    .then(result => {
      // Process result
    })
    .catch(error => {
      // Handle error
    });
  ```**在 Express 中使用中间件进行错误处理**：如果您使用的是 Express，请定义错误处理中间件来管理 [database](../D/database.md) 错误。

  ```
  app.use((error, req, res, next) => {
    if (error instanceof DatabaseError) {
      res.status(500).send('Database error occurred');
    } else {
      next(error);
    }
  });
  ```**记录错误**：始终记录错误以进行调试和监视。

  ```
  console.error('Database error:', error);
  ```**正常关闭**：如果 [database](../D/database.md) 错误很严重，请考虑在记录错误并向客户端发送响应后正常关闭进程。
  请记住，**永远不要向客户端公开敏感的错误详细信息**，因为这可能会带来安全风险。相反，记录详细错误并向客户端发送一般错误消息。

### 高级概念

#### Node.js 中的事件循环是什么？

**事件循环**是[Node.js](../N/node-js.md) 中的核心概念，尽管是单线程，但仍可实现非阻塞 I/O 操作。它负责调度异步操作并管理它们的完成。当 [Node.js](../N/node-js.md) 启动时，它会初始化事件循环，该循环会重复检查 **回调队列** 是否有来自已完成的 I/O 事件或计时器的任何待处理回调。
  以下是事件循环操作的简化视图：

1. **定时器**：检查
    `setTimeout()`
    和
    `setInterval()`
    回调。

2. **待处理回调** ：执行推迟到下一个循环迭代的 I/O 相关回调。
  3. **空闲，准备**：内部维护阶段。
  4. **Poll** ：检索新的I/O事件；执行他们的回调。
  5. **检查**：
    `setImmediate()`
    此处调用回调。

6. **关闭回调** ：句柄
    `close`
    事件，例如套接字关闭。
  **轮询**阶段至关重要，因为它决定等待传入连接、请求等多长时间，以及如果没有回调则是否终止。如果使用 `setImmediate()` 调度脚本，事件循环将结束轮询阶段并运行这些脚本。
  [Node.js](../N/node-js.md) 使用 **libuv** 库来实现事件循环，该循环处理异步 I/O 操作。事件循环使 [Node.js](../N/node-js.md) 能够通过尽可能将任务卸载到系统内核来执行非阻塞操作，并在操作完成或数据可用时管理回调执行。

  ```
  setImmediate(() => {
    console.log('Immediate execution');
  });
  setTimeout(() => {
    console.log('Timeout execution');
  }, 0);
  // Output order may vary depending on the performance of the process
  ```了解事件循环对于优化 [Node.js](../N/node-js.md) 应用程序和避免 CPU 密集型任务阻塞循环等性能问题至关重要。

1. **定时器**：检查
    `setTimeout()`
    和
    `setInterval()`
    回调。

2. **待处理回调** ：执行推迟到下一个循环迭代的 I/O 相关回调。
  3. **空闲，准备**：内部维护阶段。
  4. **Poll** ：检索新的I/O事件；执行他们的回调。
  5. **检查**：
    `setImmediate()`
    此处调用回调。

6. **关闭回调** ：句柄
    `close`
    事件，例如套接字关闭。

#### 什么是回调地狱以及如何在 Node.js 中避免它？

回调地狱，也称为“末日金字塔”，是指回调嵌套在其他回调中数层深度的情况，导致代码难以阅读和维护。由于[Node.js](../N/node-js.md) 的异步特性，这种情况经常出现。
  为了避免回调地狱：

- **模块化**：将大型功能分解为更小的、可重用的功能。这使得代码更易于管理且更易于遵循。
  - **命名函数**：使用命名函数代替匿名回调。这提高了调试期间的可读性和堆栈跟踪。
  - **控制流库**：利用 `async` 等库，它们提供了用于处理异步 JavaScript 的强大功能。
  - **Promises**：用 Promise 替换回调。它们允许您链接 `.then()` 和 `.catch()` 方法，从而获得更扁平的代码结构。
  - **Async/Await**：ES2017中引入async/await，可以用同步的方式编写异步代码，进一步扁平化结构，提高可读性。
  下面是将嵌套回调转换为 async/await 的示例：

  ```
  // Callback hell
  fs.readdir(source, function (err, files) {
    if (err) {
      console.log('Error finding files: ' + err);
    } else {
      files.forEach(function (filename, fileIndex) {
        console.log(filename);
        // More nested callbacks...
      });
    }
  });
  // Using async/await
  async function listFiles() {
    try {
      const files = await fs.promises.readdir(source);
      files.forEach(filename => {
        console.log(filename);
        // More synchronous-looking code...
      });
    } catch (err) {
      console.log('Error finding files: ' + err);
    }
  }
  ```通过遵循这些实践，您可以编写更干净、更易于维护的[Node.js](../N/node-js.md)代码，并有效避免回调地狱。

- **模块化**：将大型功能分解为更小的、可重用的功能。这使得代码更易于管理且更易于遵循。
  - **命名函数**：使用命名函数代替匿名回调。这提高了调试期间的可读性和堆栈跟踪。
  - **控制流库**：利用 `async` 等库，它们提供了用于处理异步 JavaScript 的强大功能。
  - **Promises**：用 Promise 替换回调。它们允许您链接 `.then()` 和 `.catch()` 方法，从而获得更扁平的代码结构。
  - **Async/Await**：ES2017中引入async/await，可以用同步的方式编写异步代码，进一步扁平化结构，提高可读性。

#### Node.js 中的 Promise 和 async/await 是什么？

[Node.js](../N/node-js.md) 中的 Promise 是表示异步操作最终完成或失败的对象。它们允许您通过避免深度嵌套的回调（通常称为“回调地狱”）来编写更清晰、更易于管理的异步代码。
  Promise 具有三种状态：

- **待处理**：初始状态，既不满足也不拒绝。
  - **已完成**：操作成功完成。
  - **拒绝**：操作失败。
  这是 Promise 的一个基本示例：

  ```
  const myPromise = new Promise((resolve, reject) => {
    // Asynchronous operation here
    if (/* operation successful */) {
      resolve('Success!');
    } else {
      reject('Failure.');
    }
  });
  myPromise.then((successMessage) => {
    console.log(successMessage);
  }).catch((failureMessage) => {
    console.log(failureMessage);
  });
  ````async/await` 是构建在 Promises 之上的语法糖，在 ES2017 中引入，旨在以更同步的方式简化异步代码的编写。 `async` 关键字被添加到函数中以告诉它们返回 Promise。 `await` 关键字用于暂停函数的执行，直到 Promise 得到解析。
  使用 `async/await` 的示例：

  ```
  async function asyncFunction() {
    try {
      const result = await someAsyncOperation();
      console.log(result);
    } catch (error) {
      console.error(error);
    }
  }
  ````async/await` 使异步代码的外观和行为更像同步代码，这可以使其更易于理解和维护。

- **待处理**：初始状态，既不满足也不拒绝。
  - **已完成**：操作成功完成。
  - **拒绝**：操作失败。

#### Node.js 中的 cluster 模块是什么以及它为什么有用？

[Node.js](../N/node-js.md) 中的 **集群模块** 允许您创建所有共享服务器端口的子进程。它对于在多个 CPU 核心上启用**负载平衡**很有用。由于[Node.js](../N/node-js.md) 是单线程的，因此默认情况下它不会利用多核系统。集群模块通过将主 [Node.js](../N/node-js.md) 进程分叉为多个可以同时运行的子进程来解决这个问题。
  每个子进程（也称为工作进程）是[Node.js](../N/node-js.md) 事件循环的单独实例。这意味着您的[Node.js](../N/node-js.md) 应用程序可以并行处理更多任务，从而提高性能和吞吐量。这些工作进程是使用 `child_process` 模块的 `fork` 方法生成的，并且它们通过 IPC（进程间通信）与父进程进行通信。
  这是如何使用 cluster 模块的基本示例：

  ```
  const cluster = require('cluster');
  const http = require('http');
  const numCPUs = require('os').cpus().length;
  if (cluster.isMaster) {
    console.log(`Master ${process.pid} is running`);
    // Fork workers.
    for (let i = 0; i < numCPUs; i++) {
      cluster.fork();
    }
    cluster.on('exit', (worker, code, signal) => {
      console.log(`worker ${worker.process.pid} died`);
    });
  } else {
    // Workers can share any TCP connection
    // In this case it is an HTTP server
    http.createServer((req, res) => {
      res.writeHead(200);
      res.end('Hello world\n');
    }).listen(8000);
    console.log(`Worker ${process.pid} started`);
  }
  ```在测试环境中，集群模块对于模拟高流量场景并确保应用程序可以跨多个处理器有效扩展特别有用。这也有利于在 [performance testing](../P/performance-testing.md) 期间最大限度地利用资源。

#### Node.js 如何处理子进程？

[Node.js](../N/node-js.md) 使用`child_process` 模块处理子进程，这允许它在新进程中执行其他应用程序或脚本。该模块提供了多种生成子进程的方法，例如`exec`、`execFile`、`spawn` 和`fork`。

- **exec** ：用于在 shell 中运行命令并缓冲输出。适合小尺寸数据，因为它将输出缓冲在内存中。

  ```
  const { exec } = require('child_process');
  exec('ls -lh', (error, stdout, stderr) => {
    if (error) {
      console.error(`exec error: ${error}`);
      return;
    }
    console.log(`stdout: ${stdout}`);
    console.error(`stderr: ${stderr}`);
  });
  ```

- **execFile** ：类似于
    `exec`
    但默认情况下不会生成 shell。调用可执行文件更加高效。

  ```
  const { execFile } = require('child_process');
  execFile('script.sh', (error, stdout, stderr) => {
    // handle output
  });
  ```

- **spawn** ：使用给定命令启动新进程。它流式传输数据输入/输出，使其适合大数据量。

  ```
  const { spawn } = require('child_process');
  const child = spawn('ls', ['-lh', '/usr']);
  child.stdout.on('data', (data) => {
    console.log(`stdout: ${data}`);
  });
  ```

- **叉子**：一个特殊情况
    `spawn`
    创建 V8 引擎的新实例。它用于在单独的进程中运行 Node.js 模块并启用进程间通信 (IPC)。

  ```
  const { fork } = require('child_process');
  const child = fork('script.js');
  child.on('message', (message) => {
    console.log('Message from child', message);
  });
  child.send({ hello: 'world' });
  ```子进程对于执行 CPU 密集型操作非常有用，而不会阻塞 [Node.js](../N/node-js.md) 事件循环，从而保持应用程序的响应能力。

- **exec** ：用于在 shell 中运行命令并缓冲输出。适合小尺寸数据，因为它将输出缓冲在内存中。
  - **execFile** ：类似于
    `exec`
    但默认情况下不会生成 shell。调用可执行文件更加高效。

- **spawn** ：使用给定命令启动新进程。它流式传输数据输入/输出，使其适合大数据量。
  - **叉子**：一个特殊情况
    `spawn`
    创建 V8 引擎的新实例。它用于在单独的进程中运行 Node.js 模块并启用进程间通信 (IPC)。
