# swagger

<!-- TOC START -->
- [相关术语：](#相关术语：)
  - [另请参阅：](#另请参阅：)
- [关于 Swagger 有疑问吗？](#关于-swagger-有疑问吗？)
  - [基础知识和重要性](#基础知识和重要性)
    - [Swagger 是什么？为什么它在 API 开发中很重要？](#swagger-是什么？为什么它在-api-开发中很重要？)
    - [Swagger 的主要组件有哪些？](#swagger-的主要组件有哪些？)
    - [Swagger 如何帮助设计和记录 API？](#swagger-如何帮助设计和记录-api？)
    - [Swagger 在 RESTful Web 服务中的作用是什么？](#swagger-在-restful-web-服务中的作用是什么？)
    - [Swagger 如何为 API 生命周期做出贡献？](#swagger-如何为-api-生命周期做出贡献？)
  - [swagger工具](#swagger工具)
    - [Swagger UI 是什么以及它有什么好处？](#swagger-ui-是什么以及它有什么好处？)
    - [Swagger 编辑器是什么以及如何使用它？](#swagger-编辑器是什么以及如何使用它？)
    - [Swagger Codegen 是什么以及它的用途是什么？](#swagger-codegen-是什么以及它的用途是什么？)
    - [Swagger Inspector 如何帮助测试 API？](#swagger-inspector-如何帮助测试-api？)
    - [SwaggerHub 是什么以及它如何增强 API 开发？](#swaggerhub-是什么以及它如何增强-api-开发？)
  - [实施和使用](#实施和使用)
    - [如何将 Swagger 与 Spring Boot 应用程序集成？](#如何将-swagger-与-spring-boot-应用程序集成？)
    - [如何使用Swagger生成API文档？](#如何使用swagger生成api文档？)
    - [如何自定义Swagger的默认UI？](#如何自定义swagger的默认ui？)
    - [如何使用Swagger测试API？](#如何使用swagger测试api？)
    - [如何在 Swagger 中定义 API 端点？](#如何在-swagger-中定义-api-端点？)
  - [高级概念](#高级概念)
    - [OpenAPI 规范是什么以及它与 Swagger 有何关系？](#openapi-规范是什么以及它与-swagger-有何关系？)
    - [如何使用 Swagger 进行 API 版本控制？](#如何使用-swagger-进行-api-版本控制？)
    - [如何使用 Swagger 处理身份验证和授权？](#如何使用-swagger-处理身份验证和授权？)
    - [Swagger 有哪些限制？](#swagger-有哪些限制？)
    - [如何扩展Swagger的功能？](#如何扩展swagger的功能？)
<!-- TOC END -->

昂首阔步

现在通常称为 OpenAPI，是一组用于构建、设计和记录 RESTful 的工具和规范

蜜蜂

。它提供了一个标准的、与语言无关的 RESTful 接口

蜜蜂

，允许人类和计算机了解服务的功能，而无需访问其源代码或进一步详细的文档。

## 相关术语：

- [API documentation](../A/api-documentation.md)
- [Postman](../P/postman.md)

### 另请参阅：

- [Official Website](https://swagger.io/)

## 关于 Swagger 有疑问吗？

### 基础知识和重要性

#### Swagger 是什么？为什么它在 API 开发中很重要？

[Swagger](../S/swagger.md) 是一套供开发人员设计、构建、记录和使用 RESTful Web 服务的工具。它在 [API](../A/api.md) 开发中发挥着至关重要的作用，它提供了一种通用语言，确保人类和计算机无需直接访问其源代码或文档即可理解服务的功能。
  **[API](../A/api.md) 开发的重要性：**

- **标准化：**
    Swagger 基于 OpenAPI 规范，提供了一种标准化的方式来描述 RESTful API，从而促进跨服务和平台的一致性。

- **互操作性：**
    围绕 Swagger 构建的工具可以轻松解释和使用不同来源的 API，从而增强协作和集成。

- **自动化：**
    Swagger 能够生成客户端库、服务器存根和 API 文档，从而减少了手动编码并加速了开发过程。

- **[Quality Assurance](../Q/quality-assurance.md):**
    通过精确的 API 定义，测试变得更加高效，因为测试自动化工程师可以直接从 API 规范生成测试用例。

- **能见度：**
    Swagger 的交互式文档允许开发人员可视化 API 的资源并与之交互，而无需任何实现逻辑。
  从本质上讲，[Swagger](../S/swagger.md) 促进了团队成员之间更清晰的沟通、更高效的设计和测试阶段以及从设计到实现的更平稳过渡。它是现代 [API](../A/api.md) 开发的基础工具，可实现更快、更可靠且可扩展的服务创建和维护。

- **标准化：**
    Swagger 基于 OpenAPI 规范，提供了一种标准化的方式来描述 RESTful API，从而促进跨服务和平台的一致性。

- **互操作性：**
    围绕 Swagger 构建的工具可以轻松解释和使用不同来源的 API，从而增强协作和集成。

- **自动化：**
    Swagger 能够生成客户端库、服务器存根和 API 文档，从而减少了手动编码并加速了开发过程。

- **[Quality Assurance](../Q/quality-assurance.md):**
    通过精确的 API 定义，测试变得更加高效，因为测试自动化工程师可以直接从 API 规范生成测试用例。

- **能见度：**
    Swagger 的交互式文档允许开发人员可视化 API 的资源并与之交互，而无需任何实现逻辑。

#### Swagger 的主要组件有哪些？

[Swagger](../S/swagger.md) 由几个有助于[API](../A/api.md) 设计、文档和测试的关键组件组成：

- **[Swagger](../S/swagger.md) 工具**：[Swagger](../S/swagger.md) 提供的一套工具，包括 [Swagger](../S/swagger.md) UI、[Swagger](../S/swagger.md) Editor、[Swagger](../S/swagger.md) Codegen 和 [Swagger](../S/swagger.md) Inspector，每个工具在 [API](../A/api.md) 开发过程中都有特定的用途。
  - **OpenAPI 规范 (OAS)**：一种与语言无关的框架，用于描述 RESTful [APIs](../A/api.md)，它允许人类和计算机在不直接访问源代码或文档的情况下了解服务的功能。
  - **[Swagger](../S/swagger.md) UI**：一种交互式文档工具，允许用户可视化[API](../A/api.md) 的资源并与之交互，而无需任何实现逻辑。
  - **[Swagger](../S/swagger.md) 编辑器**：基于浏览器的编辑器，开发人员可以使用 YAML 或 JSON 编写 OpenAPI 规范，并实时预览和验证 [API](../A/api.md) 文档。
  - **[Swagger](../S/swagger.md) Codegen**：一种根据 OpenAPI 规范生成服务器存根、客户端库和 [API](../A/api.md) 文档的工具，支持多种语言和框架。
  - **[Swagger](../S/swagger.md) Inspector**：一种在线工具，允许开发人员直接从浏览器测试[APIs](../A/api.md)，根据 OpenAPI 规范验证[API](../A/api.md)。
  - **SwaggerHub**：一个平台，汇集了所有 [Swagger](../S/swagger.md) 工具，并允许团队在 [API](../A/api.md) 设计和文档方面进行协作，并具有版本控制和集成功能。
  将[Swagger](../S/swagger.md) 集成到项目中通常涉及为[API](../A/api.md) 文档设置[Swagger](../S/swagger.md) UI，使用[Swagger](../S/swagger.md) 编辑器进行[API](../A/api.md) 设计，利用[Swagger](../S/swagger.md) Codegen 生成SDK，以及使用[Swagger](../S/swagger.md) Inspector 进行测试和验证。

- **[Swagger](../S/swagger.md) 工具**：[Swagger](../S/swagger.md) 提供的一套工具，包括 [Swagger](../S/swagger.md) UI、[Swagger](../S/swagger.md) Editor、[Swagger](../S/swagger.md) Codegen 和 [Swagger](../S/swagger.md) Inspector，每个工具在 [API](../A/api.md) 开发过程中都有特定的用途。
  - **OpenAPI 规范 (OAS)**：一种与语言无关的框架，用于描述 RESTful [APIs](../A/api.md)，它允许人类和计算机在不直接访问源代码或文档的情况下了解服务的功能。
  - **[Swagger](../S/swagger.md) UI**：一种交互式文档工具，允许用户可视化[API](../A/api.md) 的资源并与之交互，而无需任何实现逻辑。
  - **[Swagger](../S/swagger.md) 编辑器**：基于浏览器的编辑器，开发人员可以使用 YAML 或 JSON 编写 OpenAPI 规范，并实时预览和验证 [API](../A/api.md) 文档。
  - **[Swagger](../S/swagger.md) Codegen**：根据 OpenAPI 规范生成服务器存根、客户端库和 [API](../A/api.md) 文档的工具，支持多种语言和框架。
  - **[Swagger](../S/swagger.md) Inspector**：一种在线工具，允许开发人员直接从浏览器测试[APIs](../A/api.md)，根据 OpenAPI 规范验证[API](../A/api.md)。
  - **SwaggerHub**：一个平台，汇集了所有 [Swagger](../S/swagger.md) 工具，并允许团队在 [API](../A/api.md) 设计和文档方面进行协作，并具有版本控制和集成功能。

#### Swagger 如何帮助设计和记录 API？

[Swagger](../S/swagger.md) 通过提供一套工具来促进[API](../A/api.md) 设计和文档编制，使开发人员能够以机器可读的格式描述其[APIs](../A/api.md) 的结构。然后可以使用此描述自动生成交互式文档、客户端 SDK 和服务器存根。
  在设计方面，[Swagger](../S/swagger.md) 的 **OpenAPI 规范 (OAS)** 允许您定义 [API](../A/api.md) 的各个方面，从端点和方法到参数、响应和安全性。该规范充当合同，确保 [API](../A/api.md) 的设计和实现之间的一致性。
  对于文档，[Swagger](../S/swagger.md) 工具（如 **[Swagger](../S/swagger.md) UI**）将 OAS 呈现为交互式文档，允许用户探索 [API](../A/api.md)。该文档不仅是人类可读的，而且是交互式的，这意味着用户可以直接从文档界面进行[API](../A/api.md) 调用。
  以下是如何在 [Swagger](../S/swagger.md) OAS 中描述 [API](../A/api.md) 端点的基本示例：

  ```
  paths:
    /users:
      get:
        summary: Returns a list of users.
        responses:
          '200':
            description: A JSON array of user names
            content:
              application/json:
                schema:
                  type: array
                  items:
                    type: string
  ```此 YAML 片段定义了一个返回用户列表的简单 GET 端点。 [Swagger](../S/swagger.md) 工具可以使用此定义生成文档，甚至生成 [API](../A/api.md) 的模拟实现以用于测试目的。
  通过使用 [Swagger](../S/swagger.md) 进行 [API](../A/api.md) 设计和文档，您可以确保您的 [API](../A/api.md) 以标准的、与语言无关的方式进行描述，这对于创建清晰、可维护且易于使用的 [APIs](../A/api.md) 至关重要。

#### Swagger 在 RESTful Web 服务中的作用是什么？

[Swagger](../S/swagger.md) 通过提供用于描述 REST [APIs](../A/api.md) 结构的标准化接口，在 **RESTful Web 服务** 中发挥着至关重要的作用。这使得人类和计算机都能够了解服务的功能，而无需直接访问源代码或文档。
  对于[test automation](../T/test-automation.md)、[Swagger](../S/swagger.md) 的意义在于它能够动态生成**客户端库**、**服务器存根**和**[API](../A/api.md) 文档**。测试工程师可以利用它们来创建强大且可维护的[test suites](../T/test-suite.md)。 [Swagger](../S/swagger.md) 的详细[API](../A/api.md) 描述允许自动生成测试，确保测试与[API](../A/api.md) 的实际行为一致。
  使用[Swagger](../S/swagger.md)，[test automation](../T/test-automation.md) 工程师可以：

- **自动化[test case](../T/test-case.md) 创建**：直接根据 API 规范生成测试用例。
  - **验证 [API](../A/api.md) 响应**：确保 API 的响应符合定义的架构。
  - **模拟服务**：根据API规范创建模拟服务以进行隔离测试。
  - **数据驱动测试**：使用 Swagger 规范中提供的示例将测试数据输入到自动化测试中。
  [Swagger](../S/swagger.md) 能够描述 RESTful Web 服务的各个方面（从端点到身份验证方法），这使其成为 [test automation](../T/test-automation.md) 不可或缺的工具，使工程师能够快速适应变化并以最少的手动工作保持高[test coverage](../T/test-coverage.md)。

- **自动化[test case](../T/test-case.md) 创建**：直接根据 API 规范生成测试用例。
  - **验证 [API](../A/api.md) 响应**：确保 API 的响应遵循定义的架构。
  - **模拟服务**：根据API规范创建模拟服务以进行隔离测试。
  - **数据驱动测试**：使用 Swagger 规范中提供的示例将测试数据输入到自动化测试中。

#### Swagger 如何为 API 生命周期做出贡献？

[Swagger](../S/swagger.md) 通过提供支持从设计到测试的各个阶段的工具，简化了 **[API](../A/api.md) 生命周期**。在**开发阶段**，[Swagger](../S/swagger.md) 的工具（例如[Swagger](../S/swagger.md) 编辑器）允许创建和编辑 OpenAPI 规范，确保[API](../A/api.md) 设计保持一致并遵循最佳实践。在编写任何代码之前，可以与利益相关者共享此前期设计以获取反馈。
  在**测试阶段**，[Swagger](../S/swagger.md) Inspector 可用于执行[API](../A/api.md) 调用并确保[API](../A/api.md) 按预期运行。该工具简化了根据 OpenAPI 规范验证 [API](../A/api.md) 响应的过程。它还有助于为现有的 [APIs](../A/api.md) 生成 OpenAPI 定义，这可以作为创建测试的起点。
  为了**持续集成**和部署，[Swagger](../S/swagger.md) Codegen 可以根据 OpenAPI 规范自动生成服务器存根、客户端库和 [API](../A/api.md) 文档。这种自动化减少了手动编码，并有助于保持不同[API](../A/api.md)版本和实现之间的一致性。
  [Swagger](../S/swagger.md) 在**维护阶段**的角色涉及使用[Swagger](../S/swagger.md) UI，它提供了交互式文档界面。这使得开发人员和测试人员能够轻松理解[API](../A/api.md)并与之交互，而无需深入代码库，从而有助于更快地识别和解决问题。
  总体而言，[Swagger](../S/swagger.md) 的工具套件增强了协作，减少了人为错误的可能性，并加速了[API](../A/api.md) 生命周期中高质量软件的交付。

### swagger工具

#### Swagger UI 是什么以及它有什么好处？

[Swagger](../S/swagger.md) UI 是一个基于 Web 的交互式界面，允许用户可视化 [API](../A/api.md) 的资源并与之交互，而无需任何实现逻辑。它是根据 OpenAPI 规范 (OAS) 生成的，为开发人员提供了一种清晰、直观的方式来了解服务的功能，而无需访问其源代码。
  **[Swagger](../S/swagger.md) UI 的好处：**

- **易于使用：**
    为人类与 API 的交互提供简单易读的界面。

- **实时互动：**
    使用户能够向 API 发送实时请求并直接在浏览器中查看响应。

- **文档：**
    自动生成并呈现最新的 API 文档，减少手动文档工作的需要。

- **调试：**
    通过允许用户执行 API 方法来促进快速识别问题，这在测试阶段至关重要。

- **领养：**
    通过为潜在消费者提供沙箱来试验 API 来鼓励采用。

- **定制：**
    提供定制选项以匹配应用程序或公司品牌的外观和感觉。

- **整合：**
    轻松与现有项目集成，无需进行大量设置即可增强开发人员体验。
  通过利用[Swagger](../S/swagger.md) UI，[test automation](../T/test-automation.md) 工程师可以快速了解[API](../A/api.md) 端点、参数和预期响应，从而简化自动化测试的创建并有助于更高效的[API testing](../A/api-testing.md) 流程。

- **易于使用：**
    为人类与 API 的交互提供简单易读的界面。

- **实时互动：**
    使用户能够向 API 发送实时请求并直接在浏览器中查看响应。

- **文档：**
    自动生成并呈现最新的 API 文档，减少手动文档工作的需要。

- **调试：**
    通过允许用户执行 API 方法来促进快速识别问题，这在测试阶段至关重要。

- **领养：**
    通过为潜在消费者提供沙箱来试验 API 来鼓励采用。

- **定制：**
    提供定制选项以匹配应用程序或公司品牌的外观和感觉。

- **整合：**
    轻松与现有项目集成，无需进行大量设置即可增强开发人员体验。

#### Swagger 编辑器是什么以及如何使用它？

[Swagger](../S/swagger.md) Editor 是一个基于 Web 的开源编辑器，用于设计和编辑 **OpenAPI 规范 (OAS)** 文档。它使开发人员和测试人员能够以 YAML 或 JSON 格式编写 [API](../A/api.md) 定义，并进行实时验证和错误反馈。该编辑器提供了用于创建和编辑OAS文档的**可视化界面**，可用于描述RESTful[APIs](../A/api.md)。
  以下是它在 [test automation](../T/test-automation.md) 中的典型使用方式：

1. **编写[API](../A/api.md)规范**：您可以从空白文档开始或导入现有的OAS文件。当您键入时，编辑器提供**语法突出显示**、**自动完成**和**错误检查**来帮助您编写有效的规范。
  2. **预览文档**：[Swagger](../S/swagger.md) 编辑器在您编写规范时呈现 [API](../A/api.md) 文档的并排预览。这可以帮助您了解最终用户对文档的看法，并让您及早发现问题。
  3. **生成服务器存根和客户端 SDK**：[API](../A/api.md) 定义完成后，您可以直接从编辑器使用[Swagger](../S/swagger.md) Codegen 工具来生成服务器存根、客户端库，甚至完整的[API](../A/api.md) 文档。
  4. **测试端点**：虽然[Swagger](../S/swagger.md) Editor本身不是测试工具，但生成的有效OAS文件可以与其他[Swagger](../S/swagger.md)工具（例如[Swagger](../S/swagger.md) UI和[Swagger](../S/swagger.md) Inspector）一起使用来测试[API](../A/api.md)端点。
  要使用 [Swagger](../S/swagger.md) 编辑器，您通常导航到其 Web 界面或在本地运行它。以下是启动新 [API](../A/api.md) 规范的示例：

  ```
  openapi: 3.0.0
  info:
    title: Sample API
    description: API specification for my application.
    version: 1.0.0
  paths:
    /users:
      get:
        summary: List all users
        responses:
          '200':
            description: A list of users.
  ```[Swagger](../S/swagger.md) 编辑器是[test automation](../T/test-automation.md) 工程师高效定义、可视化[API](../A/api.md) 规范并进行协作的强大工具。

1. **编写[API](../A/api.md)规范**：您可以从空白文档开始或导入现有的OAS文件。当您键入时，编辑器提供**语法突出显示**、**自动完成**和**错误检查**来帮助您编写有效的规范。
  2. **预览文档**：[Swagger](../S/swagger.md) 编辑器在您编写规范时呈现 [API](../A/api.md) 文档的并排预览。这可以帮助您了解最终用户对文档的看法，并让您及早发现问题。
  3. **生成服务器存根和客户端 SDK**：[API](../A/api.md) 定义完成后，您可以直接从编辑器使用 [Swagger](../S/swagger.md) Codegen 工具来生成服务器存根、客户端库，甚至完整的 [API](../A/api.md) 文档。
  4. **测试端点**：虽然[Swagger](../S/swagger.md) Editor本身不是测试工具，但生成的有效OAS文件可以与其他[Swagger](../S/swagger.md)工具（例如[Swagger](../S/swagger.md) UI和[Swagger](../S/swagger.md) Inspector）一起使用来测试[API](../A/api.md)端点。

#### Swagger Codegen 是什么以及它的用途是什么？

[Swagger](../S/swagger.md) Codegen 是一个工具，可以**根据 OpenAPI 规范（以前称为 [Swagger](../S/swagger.md) 规范）自动生成客户端库、服务器存根和 [API](../A/api.md) 文档**。其主要目的是通过生成样板代码来**简化开发过程**，这在手动完成时可能是一项耗时的任务。
  通过输入OpenAPI规范文档，[Swagger](../S/swagger.md) Codegen可以生成各种编程语言和框架的代码，允许开发人员快速启动他们的[API](../A/api.md)客户端或服务器项目。这对于 [test automation](../T/test-automation.md) 工程师特别有用，因为它使他们能够**快速为 [API testing](../A/api-testing.md)** 生成客户端，而无需从头开始编写它们。
  以下是如何通过命令行使用 [Swagger](../S/swagger.md) Codegen 的基本示例：

  ```
  java -jar swagger-codegen-cli.jar generate -i my_api.yaml -l java -o /path/to/output/dir
  ```在此命令中，`-i` 指定输入 OpenAPI 规范文件，`-l` 指示生成代码的语言（在本例中为 Java），`-o` 定义输出目录。
  [Swagger](../S/swagger.md) Codegen 支持多种语言和框架，这意味着[test automation](../T/test-automation.md) 工程师可以生成与其现有[test suites](../T/test-suite.md) 和基础设施兼容的代码。此外，可以使用**模板**或通过修改生成器的**胡子文件**来自定义生成的代码，从而提供遵守特定编码标准或实践的灵活性。

#### Swagger Inspector 如何帮助测试 API？

[Swagger](../S/swagger.md) Inspector 是一款基于云的工具，允许用户验证其[APIs](../A/api.md) 的功能，而无需进行大量[setup](../S/setup.md)，从而简化了**测试[APIs](../A/api.md)** 的过程。它支持 REST 和 SOAP [APIs](../A/api.md)，并且特别适用于：

- **执行[API](../A/api.md)请求**：它允许用户向任何端点发送请求并查看响应，有助于快速验证API行为。
  - **验证 [API](../A/api.md) 响应**：用户可以检查状态代码、响应内容和标头，以确保 API 按预期响应。
  - **生成 OpenAPI 定义** ：经过测试，Swagger Inspector 可以自动生成 OpenAPI（以前称为 Swagger）定义，可用于进一步的文档或代码生成。
  - **与 SwaggerHub 集成**：对于使用 SwaggerHub 的团队，在 Swagger Inspector 中创建的测试和定义可以直接推送到 SwaggerHub 以进行进一步的协作和集成。
  通过提供用于进行[API](../A/api.md) 调用和分析响应的简单界面，[Swagger](../S/swagger.md) Inspector 帮助[test automation](../T/test-automation.md) 工程师快速识别问题并确保[APIs](../A/api.md) 满足其设计规范。这加速了测试阶段，并有助于提高 [API](../A/api.md) 开发生命周期。

- **执行[API](../A/api.md)请求**：它允许用户向任何端点发送请求并查看响应，有助于快速验证API行为。
  - **验证 [API](../A/api.md) 响应**：用户可以检查状态代码、响应内容和标头，以确保 API 按预期响应。
  - **生成 OpenAPI 定义** ：经过测试，Swagger Inspector 可以自动生成 OpenAPI（以前称为 Swagger）定义，可用于进一步的文档或代码生成。
  - **与 SwaggerHub 集成**：对于使用 SwaggerHub 的团队，在 Swagger Inspector 中创建的测试和定义可以直接推送到 SwaggerHub 以进行进一步的协作和集成。

#### SwaggerHub 是什么以及它如何增强 API 开发？

SwaggerHub 是一个集成的[API](../A/api.md) 设计和文档平台，通过支持[API](../A/api.md) 设计和文档的协作、标准化和版本控制来增强[API](../A/api.md) 开发。它为团队在[APIs](../A/api.md) 上协同工作提供了一个中心枢纽，其功能支持从设计到部署的整个[API](../A/api.md) 生命周期。
  **SwaggerHub 提供的主要增强功能：**

- **协作：** SwaggerHub 允许多个用户同时处理 [API](../A/api.md) 定义并进行实时同步，从而提高团队生产力和沟通。
  - **版本控制：** 它提供内置版本控制来管理 [API](../A/api.md) 生命周期的不同阶段，从而更轻松地跟踪更改并保持 [API](../A/api.md) 版本之间的一致性。
  - **标准化：** SwaggerHub 通过允许组织创建和应用自定义规则和样式指南来强制一致性，以确保所有 [APIs](../A/api.md) 都遵守公司标准。
  - **集成：** 它与[API](../A/api.md) 开发工作流程中的其他工具无缝集成，例如[API](../A/api.md) 网关和源控制系统，促进从设计到部署的顺利过渡。
  - **托管：** SwaggerHub 提供了一个空间来托管您的[API](../A/api.md) 文档，使利益相关者和消费者无需额外的基础设施即可访问该文档。
  通过利用 SwaggerHub，[test automation](../T/test-automation.md) 工程师可以确保[APIs](../A/api.md) 的设计一致、准确记录并且易于测试，最终导致[APIs](../A/api.md) 更加可靠和可维护。

- **协作：** SwaggerHub 允许多个用户同时处理 [API](../A/api.md) 定义并进行实时同步，从而提高团队生产力和沟通。
  - **版本控制：** 它提供内置版本控制来管理 [API](../A/api.md) 生命周期的不同阶段，从而更轻松地跟踪更改并保持 [API](../A/api.md) 版本之间的一致性。
  - **标准化：** SwaggerHub 通过允许组织创建和应用自定义规则和样式指南来强制一致性，以确保所有[APIs](../A/api.md) 都遵守公司标准。
  - **集成：** 它与[API](../A/api.md) 开发工作流程中的其他工具无缝集成，例如[API](../A/api.md) 网关和源控制系统，促进从设计到部署的顺利过渡。
  - **托管：** SwaggerHub 提供了一个空间来托管您的[API](../A/api.md) 文档，使利益相关者和消费者无需额外的基础设施即可访问该文档。

### 实施和使用

#### 如何将 Swagger 与 Spring Boot 应用程序集成？

将 [Swagger](../S/swagger.md) 与 Spring Boot 应用程序集成可简化 [API](../A/api.md) 文档和测试。使用以下步骤：

1. **添加依赖**
    给你的
    `pom.xml`
    对于 Maven 或
    `build.gradle`
    对于 Gradle。对于Maven：

  ```
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
  ```对于摇篮：

  ```
  implementation 'io.springfox:springfox-swagger2:2.9.2'
  implementation 'io.springfox:springfox-swagger-ui:2.9.2'
  ```

1. **创建配置类**
    启用 Swagger2 并设置 Docket bean：

  ```
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

1. **根据需要自定义 Docket bean**，以设置 [API](../A/api.md) 信息、安全方案或 [API](../A/api.md) 选择器。
  2. **运行您的 Spring Boot 应用程序**。 [Swagger](../S/swagger.md) UI 将在`http://localhost:8080/swagger-ui.html` 上提供。
  3. **直接从[Swagger](../S/swagger.md) UI 测试您的[APIs](../A/api.md)**，它提供了用于发送请求和查看响应的可视化界面。
  请记住在生产环境中**限制[Swagger](../S/swagger.md) 访问**，因为它会暴露您的[API](../A/api.md) 的结构。使用配置文件或条件配置仅在开发或测试环境中启用[Swagger](../S/swagger.md)。

1. **添加依赖**
    给你的
    `pom.xml`
    对于 Maven 或
    `build.gradle`
    对于 Gradle。对于Maven：

1. **创建配置类**
    启用 Swagger2 并设置 Docket bean：

1. **根据需要自定义 Docket bean**，以设置 [API](../A/api.md) 信息、安全方案或 [API](../A/api.md) 选择器。
  2. **运行您的 Spring Boot 应用程序**。 [Swagger](../S/swagger.md) UI 将在 `http://localhost:8080/swagger-ui.html` 上提供。
  3. **直接从[Swagger](../S/swagger.md) UI 测试您的[APIs](../A/api.md)**，它提供了用于发送请求和查看响应的可视化界面。

#### 如何使用Swagger生成API文档？

要使用 [Swagger](../S/swagger.md) 生成 [API](../A/api.md) 文档，请执行以下步骤：

1. **安装[Swagger](../S/swagger.md)**：确保您已安装[Swagger](../S/swagger.md)。对于 [Node.js](../N/node-js.md) 项目，使用 npm：

    ```
    npm install -g swagger
    ```

2. **创建 [Swagger](../S/swagger.md) 规范**：使用 YAML 或 JSON 文件中的 OpenAPI 规范 (OAS) 定义 [API](../A/api.md)。这包括路径、操作、参数和响应。

    ```
    swagger: '2.0'
    info:
      title: Sample API
      description: API documentation example
      version: 1.0.0
    host: api.example.com
    basePath: /v1
    schemes:
      - https
    paths:
      /items:
        get:
          summary: List all items
          responses:
            200:
              description: An array of items
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

3. **提供文档**：使用[Swagger](../S/swagger.md) UI 提供您的[API](../A/api.md) 文档。如果您使用的是 Express.js 等框架，则可以设置一条路由来服务 [Swagger](../S/swagger.md) UI：

    ```
    const swaggerUi = require('swagger-ui-express');
    const swaggerDocument = require('./path-to-swagger.json');
    app.use('/api-docs', swaggerUi.serve, swaggerUi.setup(swaggerDocument));
    ```

4. **访问文档**：导航到提供 [Swagger](../S/swagger.md) UI 的 URL（例如 `http://localhost:3000/api-docs`）以查看 [API](../A/api.md) 文档并与之交互。
  请记住，随着 [API](../A/api.md) 的发展，使您的 [API](../A/api.md) 规范保持最新。这可以确保您的文档仍然是开发人员的可靠来源。

1. **安装[Swagger](../S/swagger.md)**：确保您已安装[Swagger](../S/swagger.md)。对于 [Node.js](../N/node-js.md) 项目，使用 npm：

    ```
    npm install -g swagger
    ```

2. **创建 [Swagger](../S/swagger.md) 规范**：使用 YAML 或 JSON 文件中的 OpenAPI 规范 (OAS) 定义 [API](../A/api.md)。这包括路径、操作、参数和响应。

    ```
    swagger: '2.0'
    info:
      title: Sample API
      description: API documentation example
      version: 1.0.0
    host: api.example.com
    basePath: /v1
    schemes:
      - https
    paths:
      /items:
        get:
          summary: List all items
          responses:
            200:
              description: An array of items
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

3. **提供文档**：使用[Swagger](../S/swagger.md) UI 提供您的[API](../A/api.md) 文档。如果您使用的是 Express.js 等框架，则可以设置一条路由来服务 [Swagger](../S/swagger.md) UI：

    ```
    const swaggerUi = require('swagger-ui-express');
    const swaggerDocument = require('./path-to-swagger.json');
    app.use('/api-docs', swaggerUi.serve, swaggerUi.setup(swaggerDocument));
    ```

4. **访问文档**：导航到提供 [Swagger](../S/swagger.md) UI 的 URL（例如 `http://localhost:3000/api-docs`）以查看 [API](../A/api.md) 文档并与之交互。

#### 如何自定义Swagger的默认UI？

自定义[Swagger](../S/swagger.md) 的默认 UI 涉及覆盖 [Swagger](../S/swagger.md) 提供的默认样式和功能。为此，请按照下列步骤操作：

1. **下载并托管** [Swagger](../S/swagger.md) UI 的源文件到您的项目本地。您可以在[Swagger UI GitHub repository](https://github.com/swagger-api/swagger-ui) 中找到这些文件。
  2. **修改为 [Swagger](../S/swagger.md) UI 提供服务的 HTML 文件**。在下载的源中找到`index.html` 文件并更新引用以指向[Swagger](../S/swagger.md) UI 资产的本地副本。
  3. **通过编辑`swagger-ui.css` 文件或添加覆盖默认样式的新样式表来自定义样式**。使用特定的 CSS 选择器来更改 UI 组件的外观和感觉。
  4. **自定义 JavaScript** 以通过编辑 `swagger-ui-bundle.js` 和 `swagger-ui-standalone-preset.js` 文件来更改功能。您可以在`index.html`中添加或修改[Swagger](../S/swagger.md) UI初始化代码来设置自定义配置，例如：

  ```
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
    // Add any other custom configurations here
  })
  ```

1. **扩展功能**
    通过编写自定义插件或使用现有插件。插件可以修改或添加UI组件、拦截和修改请求等等。
  请记住彻底测试您的自定义 UI，以确保它仍然准确地表示 [API](../A/api.md) 并且所有交互功能都按预期工作。

1. **下载并托管** [Swagger](../S/swagger.md) UI 的源文件到您的项目本地。您可以在[Swagger UI GitHub repository](https://github.com/swagger-api/swagger-ui) 中找到这些文件。
  2. **修改为 [Swagger](../S/swagger.md) UI 提供服务的 HTML 文件**。在下载的源中找到`index.html` 文件并更新引用以指向[Swagger](../S/swagger.md) UI 资产的本地副本。
  3. **通过编辑`swagger-ui.css` 文件或添加覆盖默认样式的新样式表来自定义样式**。使用特定的 CSS 选择器来更改 UI 组件的外观和感觉。
  4. **自定义 JavaScript** 以通过编辑 `swagger-ui-bundle.js` 和 `swagger-ui-standalone-preset.js` 文件来更改功能。您可以在`index.html`中添加或修改[Swagger](../S/swagger.md) UI初始化代码来设置自定义配置，例如：
  1. **扩展功能**
    通过编写自定义插件或使用现有插件。插件可以修改或添加UI组件、拦截和修改请求等等。

#### 如何使用Swagger测试API？

使用[Swagger](../S/swagger.md) 测试[APIs](../A/api.md) 涉及利用[Swagger](../S/swagger.md) UI 和[Swagger](../S/swagger.md) 检查器工具。 [Swagger](../S/swagger.md) UI 提供了一个交互式界面，用于向[API](../A/api.md) 发送请求并查看响应。
  **要使用[Swagger](../S/swagger.md) UI 测试[APIs](../A/api.md)：**

1. **导航**
    到您的 API 的 Swagger UI。

2. **展开**
    您要测试的端点。

3. **填写**
    所需的参数或请求正文。

4. **执行**
    单击“尝试”按钮来满足请求。

5. **审查**
    用于验证 API 行为的响应代码、标头和正文。
  **[Swagger](../S/swagger.md) Inspector** 可用于更深入的测试：

1. **访问**
    斯威格督察。

2. **输入**
    您想要测试的 API 端点。

3. **定制**
    HTTP 方法并根据需要添加标头或正文。

4. **发送**
    查看实时响应的请求。

5. **验证**
    状态代码和响应负载。

6. **保存**
    如果需要，可以将 API 调用作为 Swagger 定义。
  对于**[automated testing](../A/automated-testing.md)**，您可以使用[Swagger](../S/swagger.md)生成的客户端库：

1. **生成**
    使用 Swagger Codegen 作为您的首选语言的客户端代码。

2. **写**
    使用生成的客户端库测试脚本。

3. **包括**
    根据预期结果验证响应的断言。

4. **运行**
    您的测试作为 CI/CD 管道或测试套件的一部分。

  ```
  // Example test script using a Swagger-generated client library
  const client = new ApiClient();
  client.endpoint(parameters).then(response => {
    assert.equal(response.status, 200);
    // Additional assertions...
  });
  ```请记住，不仅要**验证**响应数据，还要**错误处理**和**边缘情况**，以确保全面的 [API](../A/api.md) 覆盖范围。

1. **导航**
    到您的 API 的 Swagger UI。

2. **展开**
    您要测试的端点。

3. **填写**
    所需的参数或请求正文。

4. **执行**
    单击“尝试”按钮来满足请求。

5. **审查**
    用于验证 API 行为的响应代码、标头和正文。

1. **访问**
    斯威格督察。

2. **输入**
    您想要测试的 API 端点。

3. **定制**
    HTTP 方法并根据需要添加标头或正文。

4. **发送**
    查看实时响应的请求。

5. **验证**
    状态代码和响应负载。

6. **保存**
    如果需要，可以将 API 调用作为 Swagger 定义。

1. **生成**
    使用 Swagger Codegen 作为您的首选语言的客户端代码。

2. **写**
    使用生成的客户端库测试脚本。

3. **包括**
    根据预期结果验证响应的断言。

4. **运行**
    您的测试作为 CI/CD 管道或测试套件的一部分。

#### 如何在 Swagger 中定义 API 端点？

在[Swagger](../S/swagger.md) 中定义[API](../A/api.md) 端点涉及使用OpenAPI 规范(OAS) 来描述[API](../A/api.md) 的路径和操作。这是一个简洁的指南：

1. **从 `paths` 对象开始**：您将在此处列出 API 中的可用路径 (URI)。

  ```
  paths:
    /users:
      get:
        # GET operation details
    /users/{id}:
      get:
        # GET operation details for a single user
  ```

1. **定义操作**：在每个路径下，指定 HTTP 方法（例如，
    `get`
    ,
    `post`
    ,
    `put`
    ,
    `delete`
    ）并提供每项操作的详细信息。

  ```
  get:
    summary: Returns a list of users
    responses:
      '200':
        description: A JSON array of user names
        content:
          application/json:
            schema:
              type: array
              items:
                type: string
  ```

1. **包含参数** ：对于需要输入的操作，定义路径变量、查询参数或标头等参数。

  ```
  get:
    summary: Returns a user by ID
    parameters:
      - in: path
        name: id
        required: true
        schema:
          type: string
        description: The user's ID
  ```

1. **描述响应** ：对于每个操作，描述可能的响应，包括状态代码、描述和数据结构。

  ```
  responses:
    '200':
      description: A user object
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/User'
  ```

1. **参考模式**：使用
    `$ref`
    参考中定义的模式
    `components/schemas`
    部分以避免重复并保持 API 定义干燥。

  ```
  components:
    schemas:
      User:
        type: object
        properties:
          id:
            type: string
          name:
            type: string
  ```通过执行以下步骤，您可以在[Swagger](../S/swagger.md)中有效地定义[API](../A/api.md)端点，创建清晰且可执行的[API](../A/api.md)合约。

1. **从 `paths` 对象开始**：您将在此处列出 API 中的可用路径 (URI)。
  1. **定义操作**：在每个路径下，指定 HTTP 方法（例如，
    `get`
    ,
    `post`
    ,
    `put`
    ,
    `delete`
    ）并提供每项操作的详细信息。

1. **包含参数** ：对于需要输入的操作，定义路径变量、查询参数或标头等参数。
  1. **描述响应** ：对于每个操作，描述可能的响应，包括状态代码、描述和数据结构。
  1. **参考模式**：使用
    `$ref`
    参考中定义的模式
    `components/schemas`
    部分以避免重复并保持 API 定义干燥。

### 高级概念

#### OpenAPI 规范是什么以及它与 Swagger 有何关系？

**OpenAPI 规范 (OAS)** 是一个与语言无关的框架，用于描述 RESTful [APIs](../A/api.md)。它提供了定义[APIs](../A/api.md)的标准方法，包括端点、请求/响应类型和身份验证方法，这有助于后端和前端团队之间以及人与计算机之间的清晰通信。
  [Swagger](../S/swagger.md)，现在称为 **[Swagger](../S/swagger.md) Suite**，是一组与 OpenAPI 规范配合使用的工具。最初，[Swagger](../S/swagger.md) 既指规范又指工具，但当该规范捐赠给 OpenAPI Initiative (OAI) 时，它被重命名为 OpenAPI 规范。 [Swagger](../S/swagger.md) 工具包括 [Swagger](../S/swagger.md) UI、[Swagger](../S/swagger.md) Editor、[Swagger](../S/swagger.md) Codegen 和 [Swagger](../S/swagger.md) Inspector，每个工具在 [API](../A/api.md) 生命周期（从设计到文档、生成和测试）中服务于不同的目的。
  对于[test automation](../T/test-automation.md)，OpenAPI 规范可用于自动生成客户端库、服务器存根和[API](../A/api.md) 文档。 [Test cases](../T/test-case.md) 可以从规范中派生，确保它们与[API](../A/api.md) 的合同一致。这种自动化减少了 [API](../A/api.md) 更改时维护测试所需的手动工作，因为可以更新规范并可以重新生成相应的客户端库和测试。
  以下是如何在 [test automation](../T/test-automation.md) 场景中使用 OpenAPI 规范的示例：

  ```
  openapi: 3.0.0
  info:
    title: Sample API
    version: 1.0.0
  paths:
    /users:
      get:
        summary: List all users
        responses:
          '200':
            description: A JSON array of user names
            content:
              application/json:
                schema:
                  type: array
                  items:
                    type: string
  ```此 YAML 片段定义了一个简单的 [API](../A/api.md) 端点来列出用户，该端点可用于生成验证响应结构和状态代码的测试。

#### 如何使用 Swagger 进行 API 版本控制？

使用**[Swagger](../S/swagger.md)** 进行版本控制[APIs](../A/api.md) 需要在[Swagger](../S/swagger.md) 规范文件中定义[API](../A/api.md) 的不同版本。以下是有关如何使用 [Swagger](../S/swagger.md) 管理 [API](../A/api.md) 版本控制的简洁指南：

1. **URI 版本控制**：将版本号包含在 [API](../A/api.md) 路径中。这对于用户来说是简单且可见的。

    ```
    /api/v1/pets:
      get:
        # ...
    /api/v2/pets:
      get:
        # ...
    ```

2. **参数版本控制**：使用查询参数指定版本。这可以保持 URL 的干净，但不那么明确。

    ```
    /api/pets:
      get:
        parameters:
          - name: version
            in: query
            required: true
            type: string
            enum:
              - v1
              - v2
        # ...
    ```

3. **标头版本控制**：在自定义标头中指定版本。这在 URL 中是不可见的，当您不想向客户端 URL 公开版本控制时，这可能是首选方法。

    ```
    /api/pets:
      get:
        parameters:
          - name: X-API-Version
            in: header
            required: true
            type: string
            enum:
              - v1
              - v2
        # ...
    ```

4. **媒体类型版本控制**：使用 `Accept` 标头来定义使用自定义媒体类型的版本。

    ```
    /api/pets:
      get:
        produces:
          - application/vnd.myapi.v1+json
          - application/vnd.myapi.v2+json
        # ...
    ```选择最适合您的[API](../A/api.md) 需求的版本控制策略，并确保您的[API](../A/api.md) 文档的一致性。 **[Swagger](../S/swagger.md) UI** 将显示不同的版本，允许用户与他们感兴趣的[API](../A/api.md) 的特定版本进行交互。请记住在新版本发布时更新您的[Swagger](../S/swagger.md) 文件，以保持您的[API](../A/api.md) 文档准确且最新。

1. **URI 版本控制**：将版本号包含在 [API](../A/api.md) 路径中。这对于用户来说是简单且可见的。

    ```
    /api/v1/pets:
      get:
        # ...
    /api/v2/pets:
      get:
        # ...
    ```

2. **参数版本控制**：使用查询参数指定版本。这可以保持 URL 的干净，但不那么明确。

    ```
    /api/pets:
      get:
        parameters:
          - name: version
            in: query
            required: true
            type: string
            enum:
              - v1
              - v2
        # ...
    ```

3. **标头版本控制**：在自定义标头中指定版本。这在 URL 中是不可见的，当您不想向客户端 URL 公开版本控制时，这可能是首选方法。

    ```
    /api/pets:
      get:
        parameters:
          - name: X-API-Version
            in: header
            required: true
            type: string
            enum:
              - v1
              - v2
        # ...
    ```

4. **媒体类型版本控制**：使用 `Accept` 标头来定义使用自定义媒体类型的版本。

    ```
    /api/pets:
      get:
        produces:
          - application/vnd.myapi.v1+json
          - application/vnd.myapi.v2+json
        # ...
    ```

#### 如何使用 Swagger 处理身份验证和授权？

在[Swagger](../S/swagger.md) 中处理身份验证和授权涉及定义安全方案并将其应用到您的[API](../A/api.md) 操作。 [Swagger](../S/swagger.md) 支持各种类型的安全方案，例如 HTTP 身份验证、[API](../A/api.md) 密钥和 OAuth2。
  要定义安全方案，请使用 OpenAPI ([Swagger](../S/swagger.md)) 规范中`components` 部分下的`securitySchemes`。例如，定义 [API](../A/api.md) 密钥方案：

  ```
  components:
    securitySchemes:
      ApiKeyAuth:
        type: apiKey
        in: header
        name: X-API-KEY
  ```对于 OAuth2，您可以定义如下内容：

  ```
  components:
    securitySchemes:
      OAuth2:
        type: oauth2
        flows:
          authorizationCode:
            authorizationUrl: https://example.com/oauth/authorize
            tokenUrl: https://example.com/oauth/token
            scopes:
              read: Read access
              write: Write access
  ```定义安全方案后，使用 `security` 字段将它们应用到整个 [API](../A/api.md) 或单个操作：

  ```
  security:
    - ApiKeyAuth: []
  ```或者对于特定操作：

  ```
  paths:
    /users:
      get:
        security:
          - OAuth2: [read, write]
  ```在 [Swagger](../S/swagger.md) UI 中，系统将提示用户输入其凭据，然后该凭据将包含在 [Swagger](../S/swagger.md) UI 发出的 [API](../A/api.md) 调用中。这允许直接从文档界面对安全端点进行交互式测试。
  请记住在生产环境中**保护您的[Swagger](../S/swagger.md) UI**，以防止未经授权访问您的[API](../A/api.md) 文档和测试界面。

#### Swagger 有哪些限制？

[Swagger](../S/swagger.md) 虽然功能强大，但有几个限制：

- **静态文档**：Swagger 生成静态 API 文档，这可能无法反映 API 的实时变化或动态特性。
  - **开销**：引入 Swagger 会给项目增加额外的开销，因为它需要维护 Swagger 配置和注释。
  - **学习曲线**：新用户必须学习 Swagger 特定的语法和注释，这可能是进入的障碍。
  - **对超媒体 [APIs](../A/api.md)** 的有限支持：Swagger 可能不完全支持大量使用超媒体控件 (HATEOAS) 的 API。
  - **冗长**：Swagger 文件可能会变得冗长且难以管理，特别是对于具有许多端点的大型 API。
  - **自定义约束**：虽然 Swagger UI 是可自定义的，但无需大量努力即可更改外观和感觉的程度是有限的。
  - **[API](../A/api.md) 设计优先方法**：Swagger 通常与设计优先方法相关联，该方法可能不适合所有开发工作流程，尤其是那些喜欢代码优先方法的开发工作流程。
  - **工具依赖性**：依赖 Swagger 工具可能会产生可能影响长期灵活性的依赖性，特别是在项目需要摆脱 Swagger 的情况下。
  - **版本控制挑战**：使用 Swagger 处理 API 版本控制可能很麻烦，并且可能需要手动干预才能保持文档与 API 版本保持一致。
  尽管存在这些限制，[Swagger](../S/swagger.md) 由于其全面的功能集和活跃的社区，仍然是[API](../A/api.md) 文档和设计的广泛使用的工具。

- **静态文档**：Swagger 生成静态 API 文档，这可能无法反映 API 的实时变化或动态特性。
  - **开销**：引入 Swagger 会给项目增加额外的开销，因为它需要维护 Swagger 配置和注释。
  - **学习曲线**：新用户必须学习 Swagger 特定的语法和注释，这可能是进入的障碍。
  - **对超媒体 [APIs](../A/api.md)** 的有限支持：Swagger 可能不完全支持大量使用超媒体控件 (HATEOAS) 的 API。
  - **冗长**：Swagger 文件可能会变得冗长且难以管理，特别是对于具有许多端点的大型 API。
  - **自定义约束**：虽然 Swagger UI 是可自定义的，但无需大量努力即可更改外观和感觉的程度是有限的。
  - **[API](../A/api.md) 设计优先方法** ：Swagger 通常与设计优先方法相关联，该方法可能不适合所有开发工作流程，尤其是那些喜欢代码优先方法的开发工作流程。
  - **工具依赖性**：依赖 Swagger 工具可能会产生可能影响长期灵活性的依赖性，特别是在项目需要摆脱 Swagger 的情况下。
  - **版本控制挑战**：使用 Swagger 处理 API 版本控制可能很麻烦，并且可能需要手动干预才能保持文档与 API 版本保持一致。

#### 如何扩展Swagger的功能？

可以通过自定义插件、装饰器以及与其他工具集成来扩展[Swagger](../S/swagger.md) 的功能。方法如下：
  **自定义插件**：开发自定义插件以增强[Swagger](../S/swagger.md) UI 或[Swagger](../S/swagger.md) 编辑器。例如，您可以创建一个插件来向 UI 添加新功能或与其他系统集成。
  **装饰器**：在 Java 或 TypeScript 等语言中，使用装饰器来丰富您的 [API](../A/api.md) 注释。这可以提供额外的元数据，[Swagger](../S/swagger.md) 可以使用这些元数据来生成更详细的文档或客户端库。
  **中间件集成**：将[Swagger](../S/swagger.md) 与应用程序框架中的中间件集成，以添加或修改[API](../A/api.md) 行为。例如，您可以使用中间件根据 [Swagger](../S/swagger.md) 定义验证请求参数。
  **[Swagger](../S/swagger.md) 扩展**：利用 [Swagger](../S/swagger.md) 扩展 (`x-`) 将自定义属性添加到您的 OpenAPI 定义中。这些可用于文档目的或由理解这些扩展的工具使用。
  **第三方工具**：将[Swagger](../S/swagger.md) 与第三方工具（例如[Postman](../P/postman.md) for [API testing](../A/api-testing.md)）结合起来。您可以将[Swagger](../S/swagger.md) 定义导入[Postman](../P/postman.md) 以快速创建[test suites](../T/test-suite.md)。
  **[API](../A/api.md) 网关**：使用支持[Swagger](../S/swagger.md)/OpenAPI 的[API](../A/api.md) 网关自动导入定义并应用速率限制或身份验证等策略。
  **[Swagger](../S/swagger.md) Codegen 自定义模板**：在 [Swagger](../S/swagger.md) Codegen 中自定义代码生成模板，以根据您的需求定制生成的代码。

  ```
  paths:
    /pets:
      get:
        x-my-extension: value
  ```**自定义验证器**：编写与 [Swagger](../S/swagger.md) 配合使用的自定义验证器，以对 [API](../A/api.md) 输入和输出强制执行附加约束。
  通过利用这些方法，您可以定制[Swagger](../S/swagger.md)以满足您的特定要求，使其成为[API](../A/api.md)开发和测试工具库中更强大的工具。
