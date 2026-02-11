# Swagger
[Swagger](#swagger) [Swagger](/wiki/swagger) [APIs](/wiki/api) [APIs](/wiki/api)

### 相关术语：
- [API 文档 (API documentation)](/glossary/api-documentation)
- [Postman](/glossary/postman)

### 参见：
- [官方网站](https://swagger.io/)

## 关于 Swagger 的常见问题？

#### 基础与重要性
- **什么是 Swagger，为什么它在 API 开发中很重要？**
  **[Swagger](/wiki/swagger)** 是一套供开发人员设计、构建、记载和使用 RESTful Web 服务的工具。它通过提供一种通用的语言，在不直接访问源码或文档的情况下，确保人类和计算机都能理解服务的功能，从而在 **[API](/wiki/api)** 开发中发挥着至关重要的作用。
  **API 开发中的重要性：**
  - **标准化**：Swagger 基于 OpenAPI 规范，提供了一种标准化的方式来描述 RESTful API，促进了跨服务和跨平台的一致性。
  - **互操作性**：围绕 Swagger 构建的工具可以轻松解释和使用来自不同来源的 API，增强了协作和集成。
  - **自动化**：Swagger 生成客户端库、服务器存根和 API 文档的能力减少了手动编码并加速了开发过程。
  - **质量保证**：通过精确的 API 定义，测试变得更加高效，测试自动化工程师可以根据 API 规范直接生成测试用例。
  - **可见性**：Swagger 的交互式文档允许开发人员在没有任何实现逻辑的情况下可视化并与 API 资源进行交互。
  本质上，**[Swagger](/wiki/swagger)** 促进了团队成员之间更清晰的沟通，实现了更高效的设计和测试阶段，并让从设计到实现的过渡更加平滑。它是现代 **[API](/wiki/api)** 开发的基础工具，能够实现更快、更可靠且可扩展的服务创建和维护。

- **Swagger 的主要组件有哪些？**
  **[Swagger](/wiki/swagger)** 由几个关键组件组成，这些组件促进了 **[API](/wiki/api)** 的设计、文档编制和测试：
  - **Swagger 工具 (Swagger Tools)**：Swagger 提供的一套工具，包括 **Swagger UI**、**Swagger Editor**、**Swagger Codegen** 和 **Swagger Inspector**，各自在 API 开发过程中承担特定职责。
  - **OpenAPI 规范 (OAS)**：一种与语言无关的框架，用于描述 RESTful API，允许人类和计算机在不访问源码的情况下理解服务功能。
  - **Swagger UI**：一种交互式文档工具，允许用户在没有实现逻辑的情况下可视化并与 API 资源交互。
  - **Swagger Editor**：一个基于浏览器的编辑器，开发人员可以在其中使用 YAML 或 JSON 编写 OpenAPI 规范，并实时预览和验证 API 文档。
  - **Swagger Codegen**：一个根据 OpenAPI 规范生成服务器存根、客户端库和 API 文档的工具，支持多种语言和框架。
  - **Swagger Inspector**：一个在线工具，允许开发人员直接从浏览器测试 API，根据 OpenAPI 规范验证 API。
  - **SwaggerHub**：一个不仅整合了所有 Swagger 工具，还允许团队在 API 设计和文档上进行协作的平台，具备版本控制和集成能力。
  将 **[Swagger](/wiki/swagger)** 集成到项目中通常涉及：设置用于 API 文档的 Swagger UI，使用 Swagger Editor 进行 API 设计，利用 Swagger Codegen 生成 SDK，以及采用 Swagger Inspector 进行测试和验证。

- **Swagger 如何帮助设计和记载 API？**
  **[Swagger](/wiki/swagger)** 通过提供一套工具让开发人员以机器可读的格式描述 API 结构，从而促进了 **[API](/wiki/api)** 设计和文档编制。这种描述可用于自动生成交互式文档、客户端 SDK 和服务器存根。
  在设计方面，**[Swagger](/wiki/swagger)** 的 **OpenAPI 规范 (OAS)** 允许你定义 API 的每个方面，从端点和方法到参数、响应和安全性。该规范充当了确保设计与实现之间一致性的契约。
  在文档方面，像 **Swagger UI** 这样的工具将 OAS 渲染为交互式文档，允许用户探索 API。这些文档不仅易于阅读，而且是交互式的，意味着用户可以直接从文档界面发起 API 调用。
  以下是在 Swagger OAS 中描述 API 端点的基础示例：
  ```yaml
  paths:
    /users:
      get:
        summary: 返回用户列表。
        responses:
          '200':
            description: 用户名的 JSON 数组
            content:
              application/json:
                schema: 
                  type: array
                  items: 
                    type: string
  ```
  这个 YAML 片段定义了一个简单的 GET 端点，返回用户列表。**[Swagger](/wiki/swagger)** 工具可以使用此定义生成文档，甚至是用于测试的 API 模拟实现。
  通过使用 **[Swagger](/wiki/swagger)** 进行 **[API](/wiki/api)** 设计和文档编制，你可以确保 API 以标准、语言无关的方式进行描述，这对于创建清晰、可维护且易用的 API 至关重要。

- **Swagger 在 RESTful Web 服务中扮演什么角色？**
  **[Swagger](/wiki/swagger)** 在 **RESTful Web 服务** 中扮演着通过提供标准化接口来描述 REST API 结构的至关重要角色。
  对于自动化测试，Swagger 的意义在于它能动态生成 **客户端库 (client libraries)**、**服务器存根 (server stubs)** 和 **API 文档**。测试工程师可以利用这些来创建健壮且可维护的测试套件。Swagger 详尽的 API 描述允许自动化生成测试，确保测试与 API 的实际行为保持一致。
  使用 **[Swagger](/wiki/swagger)**，测试自动化工程师可以：
  - **自动创建测试用例**：直接从 API 规范生成测试用例。
  - **验证 API 响应**：确保 API 响应符合定义的 schema。
  - **模拟 (Mock) 服务**：根据 API 规范创建模拟服务进行隔离测试。
  - **数据驱动测试**：使用 Swagger 规范中提供的示例作为自动化测试的输入数据。
  **[Swagger](/wiki/swagger)** 描述 RESTful Web 服务各个方面（从端点到认证方法）的能力，使其成为 **测试自动化** 中不可或缺的工具。

- **Swagger 如何对 API 生命周期做出贡献？**
  **[Swagger](/wiki/swagger)** 通过提供支持从设计到测试各个阶段的工具，简化了 **API 生命周期**。
  在 **开发阶段**，**[Swagger](/wiki/swagger)** 工具（如 Swagger Editor）允许创建和编辑 OpenAPI 规范，确保 API 设计的一致性并遵循最佳实践。在编写任何代码之前，这种前期设计可以与利益相关者共享以获取反馈。
  在 **测试阶段**，**Swagger Inspector** 可用于执行 API 调用并确保行为符合预期。它简化了根据 OpenAPI 规范验证 API 响应的过程。它还有助于为现有 API 生成 OpenAPI 定义，作为测试基础。
  对于 **持续集成**，**Swagger Codegen** 可以自动生成服务器存根、客户端库和 API 文档。这种自动化减少了手动编码，并有助于维持不同 API 版本和实现之间的一致性。
  在 **维护阶段**，**Swagger UI** 提供了交互式文档界面。这让开发人员和测试人员都能轻松理解并与 API 交互，而无需深入代码库，从而加快了问题识别和解决的速度。

#### Swagger 工具
- **什么是 Swagger UI，它的优势是什么？**
  **Swagger UI** 是一个交互式的 Web 界面，允许用户在没有实现逻辑的情况下可视化并与 **[API](/wiki/api)** 资源交互。它根据 OpenAPI 规范 (OAS) 生成，为开发人员提供了一种直观的方式来理解服务功能。
  **[Swagger](/wiki/swagger)** UI 的优势：
  - **易用性**：提供直观易读的界面进行人机交互。
  - **实时交互**：允许用户发送实时请求并直接在浏览器中查看响应。
  - **文档化**：自动生成并展示最新的 API 文档，减少手动编写文档的工。
  - **调试**：允许用户执行 API 方法，便于在测试阶段快速识别问题。
  - **采纳**：为潜在使用者提供沙盒环境进行实验，从而提高采纳率。
  - **自定义**：提供自定义选项以匹配应用外观或品牌形象。
  - **集成**：轻松集成到现有项目中，无需大量设置。
  通过利用 **[Swagger](/wiki/swagger)** UI，**测试自动化** 工程师可以快速理解 API 端点、参数和预期响应，从而简化自动化测试的创建。

- **什么是 Swagger Editor，如何使用它？**
  **Swagger Editor** 是一个开源的基于 Web 的编辑器，用于设计和编辑 **OpenAPI 规范 (OAS)** 文档。它支持开发人员和测试人员以 YAML 或 JSON 格式编写 API 定义，并提供实时验证和错误反馈。该编辑器提供了一个 **可视化界面** 来创建和编辑用于描述 RESTful API 的 OAS 文档。
  以下是它在 **测试自动化** 中的典型用法：
  - **编写 API 规范**：可以从空白文档开始或导入现有的 OAS 文件。在你输入时，编辑器提供 **语法高亮**、**自动完成** 和 **错误检查**。
  - **预览文档**：在你编写规范时，**[Swagger](/wiki/swagger)** Editor 会同步渲染 API 文档预览。这有助于你查看最终用户看到的文档效果并及早发现问题。
  - **生成服务器存根和客户端 SDK**：API 定义完成后，你可以直接从编辑器使用 **Swagger Codegen** 工具生成代码或完整的 API 文档。
  - **测试端点**：虽然编辑器本身不是测试工具，但输出的 OAS 文件可配合其他 **[Swagger](/wiki/swagger)** 工具（如 Swagger UI 和 Swagger Inspector）进行 API 端点测试。
  要使用编辑器，通常访问其 Web 界面或在本地运行。以下是启动新规范的示例：
  ```yaml
  openapi: 3.0.0
  info:
    title: 示例 API
    description: 我的应用的 API 规范。
    version: 1.0.0
  paths:
    /users:
      get:
        summary: 列出所有用户
        responses:
          '200':
            description: 用户列表。
  ```

- **什么是 Swagger Codegen，它的目的是什么？**
  **Swagger Codegen** 是一个能根据 OpenAPI 规范 **自动生成客户端库、服务器存根和 API 文档** 的工具。其主要目的是通过生成样板代码来 **简化开发过程**，因为手动编写代码可能非常耗时。
  通过输入 OpenAPI 规范文档，该工具可以生成各种编程语言和框架的代码。这对于 **测试自动化** 工程师特别有用，因为它可以让他们 **快速生成 API 测试客户端**。
  命令行使用基本示例：
  ```bash
  java -jar swagger-codegen-cli.jar generate -i my_api.yaml -l java -o /path/to/output/dir
  ```
  在此命令中，`-i` 指定输入规范文件，`-l` 指示生成的语言（此处为 Java），`-o` 定义输出目录。
  **[Swagger](/wiki/swagger)** Codegen 支持多种语言，这意味着可以生成与现有 **测试套件** 兼容的代码。此外，生成的代码可以使用 **模板 (templates)** 或通过修改生成器的 **mustache 文件** 进行自定义。

- **Swagger Inspector 如何帮助测试 API？**
  **Swagger Inspector** 是一个云端工具，允许用户在无需大量 **[设置 (setup)](/wiki/setup)** 的情况下验证 **API 功能**。它特别适用于：
  - **执行 API 请求**：允许向任何端点发送请求并查看响应，从而快速验证 API 行为。
  - **验证 API 响应**：检查状态码、响应内容和 Header，确保符合预期。
  - **生成 OpenAPI 定义**：测试完成后，它能自动生成可用于文档或代码生成的 OpenAPI 定义。
  - **与 SwaggerHub 集成**：创建的测试和定义可以直接推送到 SwaggerHub 进行协作。
  通过提供简便的调用界面，该工具帮助 **测试自动化** 工程师快速识别问题，并确保 API 符合设计规范。

- **什么是 SwaggerHub，它如何增强 API 开发？**
  **SwaggerHub** 是一个集成的 API 设计和文档平台，通过支持协作、标准化和版本控制来增强 **[API](/wiki/api)** 开发。它为团队提供了一个中心枢纽，支持从设计到部署的全生命周期。
  **SwaggerHub 提供的关键增强功能：**
  - **协作**：允许各用户实时同步处理 API 定义，提高团队生产力。
  - **版本控制**：提供内置版本管理，方便跟踪更改并维持一致性。
  - **标准化**：通过允许组织应用自定义规则和风格指南，强制执行 API 标准。
  - **集成**：无缝集成到 API 栅、源码控制系统等开发工作流中。
  - **托管**：提供托管 API 文档的空间，无需额外基础设施即可供相关方访问。
  测试自动化工程师可以确保 API 被一致地设计、准确地记载且易于测试。

#### 实施与用法
- **如何将 Swagger 与 Spring Boot 应用集成？**
  将 **[Swagger](/wiki/swagger)** 与 Spring Boot 应用集成可以简化 **[API](/wiki/api)** 文档和测试。步骤如下：
  1. 向 `pom.xml` 或 `build.gradle` **添加依赖项**。对于 Maven：
  ```xml
  <dependency>
      <groupId>io.springfox</groupId>
      <artifactId>springfox-swagger2</artifactId>
      <version>2.9.2</version>
  </dependency>
  <dependency>
      <groupId>io.springfox</groupId>
      <artifactId>springfox-swagger-ui</artifactId>
      <version>2.9.2</version>
  </dependency>
  ```
  对于 Gradle：
  ```groovy
  implementation 'io.springfox:springfox-swagger2:2.9.2'
  implementation 'io.springfox:springfox-swagger-ui:2.9.2'
  ```
  2. **创建配置类** 以启用 Swagger2 并设置 Docket bean：
  ```java
  import springfox.documentation.swagger2.annotations.EnableSwagger2;
  import org.springframework.context.annotation.Bean;
  import org.springframework.context.annotation.Configuration;
  import springfox.documentation.spring.web.plugins.Docket;
  import springfox.documentation.spi.DocumentationType;

  @Configuration
  @EnableSwagger2
  public class SwaggerConfig {                                    
      @Bean
      public Docket api() { 
          return new Docket(DocumentationType.SWAGGER_2);  
      }
  }
  ```
  3. **自定义 Docket bean**（如有需要），设置 API 信息、安全方案或 API 选择器。
  4. 运行应用。**[Swagger](/wiki/swagger)** UI 通常可在 `http://localhost:8080/swagger-ui.html` 访问。
  5. 直接从界面测试 API。
  **注意：** 记得在生产环境中 **限制 Swagger 访问**，通常使用 Spring Profile 仅在开发或测试环境启用。

- **如何使用 Swagger 生成 API 文档？**
  1. **安装 Swagger**：对于 Node.js 项目，使用 `npm install -g swagger`。
  2. **创建 Swagger 规范**：使用 YAML 或 JSON 文件定义 API。
  ```yaml
  swagger: '2.0'
  info:
    title: 示例 API
    description: API 文档示例
    version: 1.0.0
  host: api.example.com
  basePath: /v1
  schemes:
    - https
  paths:
    /items:
      get:
        summary: 列出所有项
        responses:
          200:
            description: 项数组
            schema:
              type: array
              items:
                $ref: '#/definitions/Item'
  definitions:
    Item:
      type: object
      properties:
        id:
          type: integer
          format: int64
        name:
          type: string
  ```
  3. **提供 (Serve) 文档**：使用 **Swagger UI**。如果是 Express.js：
  ```javascript
  const swaggerUi = require('swagger-ui-express');
  const swaggerDocument = require('./path-to-swagger.json');

  app.use('/api-docs', swaggerUi.serve, swaggerUi.setup(swaggerDocument));
  ```
  4. **访问文档**：导航到对应 URL（如 `http://localhost:3000/api-docs`）。

- **如何自定义 Swagger 的默认 UI？**
  1. **下载并托管** Swagger UI 的源文件（见 [GitHub 仓库](https://github.com/swagger-api/swagger-ui)）。
  2. **修改 HTML 文件**：定位并更新 `index.html` 中的资源引用。
  3. **自定义样式**：编辑 `swagger-ui.css` 或添加覆盖样式的新样式表。
  4. **自定义 JavaScript**：编辑 `swagger-ui-bundle.js` 和 `swagger-ui-standalone-preset.js` 来更改功能。你可以在 `index.html` 中设置属性：
  ```javascript
  const ui = SwaggerUIBundle({
    url: "http://petstore.swagger.io/v2/swagger.json",
    dom_id: '#swagger-ui',
    deepLinking: true,
    presets: [
      SwaggerUIBundle.presets.apis,
      SwaggerUIStandalonePreset
    ],
    plugins: [
      SwaggerUIBundle.plugins.DownloadUrl
    ],
    layout: "StandaloneLayout",
    // 在此处添加其他自定义配置
  })
  ```
  5. **扩展功能**：编写自定义插件。

- **如何使用 Swagger 进行 API 测试？**
  涉及利用 Swagger UI 和 Swagger Inspector。界面提供了向 API 发送请求并查看响应的功能。
  **使用 Swagger UI 测试 API：**
  - **导航** 到 API 的 Swagger UI。
  - **展开** 要测试的端点。
  - **填写** 参数或 Request Body。
  - **执行** 请求（点击 "Try it out"）。
  - **审查** 结果。
  **Swagger Inspector** 可进行更深入的手动测试。
  对于 **自动化测试**，可以使用 **[Swagger](/wiki/swagger)** 生成的客户端库：
  - 使用 Codegen **生成** 代码。
  - 使用生成的库 **编写** 脚本。
  - **包含** 断言。
  - 将测试作为 CI/CD 流水线或 **测试套件** 的一部分 **运行**。
  ```javascript
  // 使用生成的客户端库的测试脚本示例
  const client = new ApiClient();
  client.endpoint(parameters).then(response => {
    assert.equal(response.status, 200);
    // 其他断言...
  });
  ```
  务必验证错误处理和边缘情况。

- **如何在 Swagger 中定义 API 端点？**
  使用 OpenAPI 规范 (OAS)：
  1. **从 `paths` 对象开始**：列出 API 中可用的路径。
  ```yaml
  paths:
    /users:
      get:
        # GET 操作详情
    /users/{id}:
      get:
        # 单个用户的 GET 详情
  ```
  2. **定义操作**：指定 HTTP 方法（`get`、`post`、`put`、`delete` 等）。
  3. **包含参数**：定义路径变量、查询参数或 Header。
  4. **描述响应**：为每个操作描述可能的结果（状态码、描述、数据结构）。
  5. **引用 Schema**：使用 `$ref` 引用 `components/schemas` 中定义的结构，保持 DRY（不要重复）。
  ```yaml
  components:
    schemas:
      User:
        type: object
        properties:
          id: {type: string}
          name: {type: string}
  ```

#### 高级概念
- **什么是 OpenAPI 规范，它与 Swagger 有什么关系？**
  **OpenAPI 规范 (OAS)** 是一种用于描述 RESTful API 的语言无关框架。它提供了一种定义 API 的标准方法。
  **[Swagger](/wiki/swagger)**（现称为 Swagger 套件）是与该规范配合使用的一套工具。最初 Swagger 既指规范也指工具，但当规范捐赠给 OpenAPI 倡议组织 (OAI) 后，规范更名为 OpenAPI Specification。Swagger 工具包括集成了 OAS 的 UI、Editor、Codegen 和 Inspector。
  在 **自动化测试** 中，OAS 可用于自动生成代码。**测试用例** 可以源自规范，确保与 API 契约一致。
  YAML 示例：
  ```yaml
  openapi: 3.0.0
  info:
    title: 示例 API
    version: 1.0.0
  paths:
    /users:
      get:
        summary: 列出所有用户
        responses:
          '200':
            description: 用户名 JSON 数组
            content:
              application/json:
                schema:
                  type: array
                  items: {type: string}
  ```

- **如何使用 Swagger 进行 API 版本控制？**
  1. **URI 版本控制**：在路径中包含版本号。
  ```yaml
  /api/v1/pets:
    get:
  /api/v2/pets:
    get:
  ```
  2. **参数版本控制**：使用查询参数。
  3. **Header 版本控制**：使用自定义 Header（如 `X-API-Version`）。
  4. **媒体类型 (Media Type) 版本控制**：使用 `Accept` Header。
  ```yaml
  /api/pets:
    get:
      produces:
        - application/vnd.myapi.v1+json
        - application/vnd.myapi.v2+json
  ```
  5. **多个 OpenAPI 文件**：为每个版本维护单独的规格文件。
  6. **SwaggerHub 版本管理**：利用其内置的版本管理功能。

- **Swagger、Postman 和 SoapUI 之间有什么区别？**
  - **Swagger**：专注于 API 设计、文档和样板代码生成。它是契约驱动的。
  - **Postman**：最初是请求测试工具，现在是支持 API 全生命周区的协作平台。其优势在于手动测试、环境管理和 Collection 共享。
  - **SoapUI**：专注于功能、加压和安全测试，最初针对 SOAP，现在也支持 REST。它在复杂断言和集成测试方面非常强大。
  
  **自动化测试** 工程师通常结合使用这些工具，例如用 **[Swagger](/wiki/swagger)** 定义契约，用 Postman 进行 API 探索和集成测试，用 SoapUI 进行高级验证。

- **Swagger 管理大型 API 的一些最佳实践是什么？**
  1. **模块化**：使用 `$ref` 将大规格文件拆分为多个相互引用的较小文件。
  2. **标准化**：建立全公司级的命名约定和数据结构。
  3. **版本控制**：尽早实施版本策略。
  4. **详细说明**：充分利用描述字段为以后提供上下文。
  5. **安全统筹**：在全局 `securityDefinitions` 中统一管理认证模式。
  6. **使用 Tags**：对操作进行分组，使界面整洁易读。
  7. **自动化集成**：将规格文件纳入源码控制系统。
  8. **治理**：使用 SwaggerHub 等平台实施风格指南检查。
  9. **文档及时更新**：确保代码更改能反映到规格文件中。
  10. **代码审查**：将规格文件的更改也纳入 Pull Request 审查流程。
