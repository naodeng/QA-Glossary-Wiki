# Postman
[Postman](#postman) [Postman](/wiki/postman) [API](/wiki/api)

### 相关术语：
- [API 测试工具 (API testing tool)](/glossary/api-testing-tool)
- [Swagger](/glossary/swagger)

### 了解更多：
- [官方网站](https://www.postman.com/)
- [维基百科](https://en.wikipedia.org/wiki/Postman_(software))

## 关于 Postman 的常见问题？

#### 基础与重要性
- **什么是 Postman？它有什么用途？**
  Postman 是一个 **API 开发工具**，简化了构建、测试和修改 API 的过程。它提供了一个友好的界面，用于发送 HTTP 请求（GET, POST, PUT, DELETE 等）并查看响应，而无需编写自定义客户端代码。
  开发人员和测试人员使用它来验证 API 行为，确保返回的数据正确，并模拟各种错误情况。

- **为什么 Postman 在软件测试中很重要？**
  - **验证 API 契约**：确保端点按预期工作。
  - **自动化与 CI/CD**：通过 **Newman**（命令行工具）将测试集成到流水线中。
  - **脚本能力**：支持 JavaScript 编写预请求脚本和测试脚本，实现复杂逻辑验证。
  - **监控与协作**：支持线上监控、团队共享集合（Collections）和环境变量。

- **核心功能有哪些？**
  - **内置认证协议**：支持 OAuth、Basic Auth、API Key 等。
  - **环境与变量**：轻松切换开发、测试和生产环境配置。
  - **Mock 服务**：在后端开发完成前模拟 API 返回。
  - **文档生成**：自动从集合生成精美的 API 文档。
  - **可视化器 (Visualizer)**：将响应数据渲染成图表或自定义 HTML 格式。

#### 操作与使用
- **如何安装与设置？**
  1. 从官网下载对应系统的安装包（Windows, macOS, Linux）。
  2. 注册账号（可选）以同步数据。
  3. 配置代理、证书及环境变量。

- **如何创建并发送请求？**
  - 点击“New”创建请求，输入 URL，选择方法。
  - 在 Params、Headers 或 Body 标签页添加数据。
  - 点击 **Send** 发送，并在下层窗口查看状态码、响应时间和返回体。

- **变量如何在 Postman 中使用？**
  - 使用 `{{variable_name}}` 语法在 URL 或 Body 中引用。
  - 在脚本中使用 `pm.environment.set()` 或 `pm.globals.get()` 进行操作。

#### 自动化与进阶
- **如何进行自动化测试？**
  在 **Tests** 标签页编写断言：
  ```javascript
  pm.test("状态码为 200", function () {
      pm.response.to.have.status(200);
  });
  ```
  然后使用 **Collection Runner**（集合运行器）批量执行，或在命令行使用 **Newman** 执行。

- **Postman 监视器 (Monitors) 是什么？**
  它是在云端按计划（如每 5 分钟）运行的自动化过程，用于持续监控 API 的性能、可用性和响应时间，并在失败时发送预警（如 Slack 或邮件）。

- **性能测试能力**：
  支持基础的并发负载测试，通过调整 Collection Runner 的迭代次数和延迟来观察系统响应，但对于超大规模压力测试，建议使用专门的工具如 JMeter。

#### 团队协作
- **工作区 (Workspaces)**：团队共享资源的核心。
- **版本控制**：支持 Fork 和 Merge 集合，追踪变更记录。
- **集成**：支持与 GitHub、Datadog、PagerDuty 等第三方工具无缝对接。
