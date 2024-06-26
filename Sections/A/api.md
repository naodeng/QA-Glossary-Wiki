<!-- markdownlint-disable MD041 -->
- [API 应用程序编程接口](#api-应用程序编程接口)
- [关于 API 的问题](#关于-api-的问题)
  - [基础知识和重要性](#基础知识和重要性)
    - [什么是 API 以及它如何工作？](#什么是-api-以及它如何工作)
    - [为什么 API 在软件开发中很重要？](#为什么-api-在软件开发中很重要)
    - [API 有哪些不同类型？](#api-有哪些不同类型)
    - [Web API 和库 API 有什么区别？](#web-api-和库-api-有什么区别)
    - [API 在微服务架构中的作用是什么？](#api-在微服务架构中的作用是什么)
  - [API 设计与开发](#api-设计与开发)
    - [设计 API 的最佳实践是什么？](#设计-api-的最佳实践是什么)
    - [如何对 API 进行版本控制？](#如何对-api-进行版本控制)
    - [什么是 API 优先设计以及为什么它很重要？](#什么是-api-优先设计以及为什么它很重要)
    - [开发 API 时需要考虑哪些关键因素？](#开发-api-时需要考虑哪些关键因素)
    - [API 网关的作用是什么？](#api-网关的作用是什么)
  - [API 测试](#api-测试)
    - [什么是 API 测试以及为什么它很重要？](#什么是-api-测试以及为什么它很重要)
    - [API 测试有哪些不同类型？](#api-测试有哪些不同类型)
    - [API 测试常用的工具有哪些？](#api-测试常用的工具有哪些)
    - [API 测试的关键步骤是什么？](#api-测试的关键步骤是什么)
    - [如何自动化 API 测试？](#如何自动化-api-测试)
  - [API 安全](#api-安全)
    - [与 API 相关的常见安全风险有哪些？](#与-api-相关的常见安全风险有哪些)
    - [如何保护 API 的安全？](#如何保护-api-的安全)
    - [什么是 API 密钥认证？](#什么是-api-密钥认证)
    - [什么是 OAuth 以及它如何在 API 安全中使用？](#什么是-oauth-以及它如何在-api-安全中使用)
    - [SSL/TLS 在 API 安全中的作用是什么？](#ssltls-在-api-安全中的作用是什么)
  - [API 文档](#api-文档)
    - [为什么 API 文档很重要？](#为什么-api-文档很重要)
    - [好的 API 文档中应该包含哪些内容？](#好的-api-文档中应该包含哪些内容)
    - [有哪些工具可用于创建 API 文档？](#有哪些工具可用于创建-api-文档)
    - [API 文档应该多久更新一次？](#api-文档应该多久更新一次)
    - [API 文档在 API 测试中的作用是什么？](#api-文档在-api-测试中的作用是什么)

# API 应用程序编程接口

应用程序编程接口（API）是一组允许两个应用程序进行通信的规则。在这里，“应用程序”一词指的是具有特定功能的任何软件。API 定义了这些应用程序如何发送和接收请求及响应。

相关术语：

- [API Testing  API 测试](../A/api-testing.md)
- [Microservices Testing  微服务测试](../M/microservices-testing.md)

也可以看看：

[维基百科](https://zh.wikipedia.org/wiki/%E5%BA%94%E7%94%A8%E7%A8%8B%E5%BA%8F%E6%8E%A5%E5%8F%A3)

# 关于 API 的问题

## 基础知识和重要性

### 什么是 API 以及它如何工作？

API（应用程序编程接口）是一套用于构建软件应用程序的协议、例程和工具。它规定了软件组件的互动方式，使得不同系统能够轻松通信。将 API 视为一个中介层，它处理请求并确保企业系统的平稳运行。

API 通过互联网上的“调用”或“请求”进行操作，数据通常以 JSON 或 XML 等格式进行交换。当对 API 发出请求时，它执行预定义的操作并返回响应。这可能包括数据检索、更新或其他 CRUD（创建、读取、更新、删除）操作。

以下是使用 JavaScript 中的`fetch`函数调用 API 的基本示例：

```JavaScript
fetch('https://api.example.com/data', {
  method: 'GET',
  headers: {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer Your-API-Key'
  }
})
.then(response => response.json())
.then(data => console.log(data))
.catch(error => console.error('Error:', error));
```

在这个例子中，通过`GET`请求调用位于`https://api.example.com/data`的 API 以检索数据。`fetch`函数处理 HTTP 请求，响应被处理并记录到控制台。标头通常包括内容类型和授权信息，以确保 API 能够识别并允许执行请求。

### 为什么 API 在软件开发中很重要？

在软件开发中，APIs 对于**促进不同软件组件或系统之间的通信**至关重要。它们充当**合同**，规定软件元素如何互动，确保对一个部分的更改不会破坏其他地方的功能。这种**解耦**使得**模块化**成为可能，更容易设计、开发和维护应用程序。

APIs 促进了**可重用性**，允许开发人员利用现有功能而不必重新发明轮子。它们还实现了**可扩展性**，因为服务可以独立扩展以满足需求。在[测试自动化](../T/test-automation.md)的背景下，APIs 在**[集成测试](../I/integration-testing.md)**中起到了关键作用，确保应用程序的不同部分按预期一起工作。

此外，APIs 在**持续集成/持续部署（CI/CD）**流水线中至关重要，允许自动化工具与正在开发的软件进行交互，从而加速发布过程。它们还提供了一种进行**监控和健康检查**的手段，这对于维护实时系统的可靠性至关重要。

总之，APIs 是现代软件开发的支柱，支持**通信**、**模块化**、**可重用性**、**可扩展性**和**自动化**。它们是创建复杂、健壮和高效软件系统不可或缺的组成部分。

### API 有哪些不同类型？

APIs 有各种形式，每种都有不同的用途。以下是不同类型的 APIs：

- **REST（表征状态转移）**：使用 HTTP 请求来获取、放置、提交和删除数据。它是无状态的，并使用标准 HTTP 状态代码来指示请求的成功或失败。

- **SOAP（简单对象访问协议）**：依赖基于 XML 的消息协议来交换信息。它是协议无关的，并带有内置的错误处理。

- **GraphQL**：允许客户端仅请求其需要的数据，使其对于具有许多实体和关系的复杂系统非常高效。

- **gRPC（Google 远程过程调用）**：使用协议缓冲作为接口定义语言，旨在进行高性能的 RPC 通信，特别适用于微服务。

- **OData（开放数据协议）**：使用 RESTful APIs 标准化数据的查询和更新。它对于在网络上公开和使用数据非常有用。

- **JSON-RPC 和 XML-RPC**：分别以 JSON 和 XML 编码的远程过程调用协议。它们允许发送多个参数并以结构化格式接收结果。

- **WebSocket**：在单个 TCP 连接上提供全双工通信通道，实现客户端和服务器之间的实时数据传输。

每种 API 都有其自己的实施和测试标准和最佳实践。了解每种类型的特性对于有效的[测试自动化](../T/test-automation.md)至关重要。

### Web API 和库 API 有什么区别？

**Web API**是一种接口，允许不同软件系统通过互联网进行通信，通常使用 HTTP/HTTPS 协议。它通过 Web 请求和响应使服务和客户端通过 JSON 或 XML 格式交换数据和功能。Web APIs 设计用于远程访问，并支持基于 Web 的交互。

另一方面，**库 API**是由库提供的一组函数、类或协议，库是计算机程序使用的一组非易失性资源。这些 APIs 旨在直接在软件中使用，并且不通过网络公开。它们为开发人员提供了一种在不必从头编写代码的情况下利用预定义功能的方式，确保代码重用和模块化。

总之，关键区别在于它们的使用上下文：Web APIs 用于**在 Web 上进行系统间通信**，而库 APIs 用于**在应用程序代码库内部直接使用**。

### API 在微服务架构中的作用是什么？

在**微服务架构**中，APIs 充当服务之间的**主要通信渠道**，使每个服务能够独立运行，同时仍然是一个有机系统的一部分。它们允许服务**无缝交换数据**和**功能**，而无需共享代码或实现细节。

在微服务中，APIs 被设计为**轻量级**和**专注的**，通常围绕特定的业务能力。这与**单一职责**的原则一致，其中每个微服务负责一个明确定义的特性或流程。

在这种背景下使用 APIs 支持**服务可伸缩性**和**灵活性**，因为服务可以独立开发、部署和扩展。APIs 促进了服务之间的**松耦合**，这对于一个能够处理微服务的动态特性（如频繁更新和服务故障）的弹性系统是至关重要的。

此外，APIs 实现了**多语言编程**，允许服务使用最适合其功能的不同编程语言编写。这是因为 APIs 提供了一种语言无关的交互接口。

总之，APIs 对于微服务架构至关重要，为服务提供了一种在保持**隔离**和**自治**的同时相互交互的机制，支持微服务的灵活性、可伸缩性和弹性目标。

## API 设计与开发

### 设计 API 的最佳实践是什么？

在设计 API 时，务必遵循以下最佳实践：

- **一致性**至关重要。确保端点命名、请求/响应结构和错误处理在整个 API 中保持一致。
- 在适用的情况下，设计应遵循**RESTful 原则**，适当使用 HTTP 方法（用于检索的 GET，用于创建的 POST 等）。
- 对资源名称使用**名词**，对操作使用**动词**。避免在 URL 中使用动词。
- **版本控制**：实施 API 版本控制以避免对客户端的破坏性更改。使用简单的版本控制方案，例如 URL 路径或标头。
- **分页**：对于大型集合，使用分页来限制响应大小，提供更好的客户端体验。
- **过滤、排序和搜索**：允许客户端通过查询参数进行数据过滤、排序和搜索。
- **速率限制**：通过实施速率限制来保护 API 免受滥用和过度使用。
- **缓存**：使用 HTTP 缓存头以提高性能并减少服务器负载。
- **安全性**：实施身份验证、授权和加密。使用令牌或 OAuth 进行安全访问。
- **错误处理**：提供有意义的 HTTP 状态码和错误消息。包括唯一的错误标识符以便更容易进行故障排除。
- **内容协商**：支持多种格式（如 JSON 和 XML），并使用`Accept`头进行格式选择。
- **文档**：保持文档更新，并提供清晰、简洁的示例。使用 Swagger 或 API Blueprint 等工具。
- **反馈循环**：鼓励并促使 API 使用者提供反馈，以不断改进 API。

```JavaScript
// Example of a RESTful endpoint for retrieving a user
GET /api/v1/users/{id}
```

记住，目标是创建一个易于理解、与之集成并随时间推移易于维护的 API。

### 如何对 API 进行版本控制？

对于保持兼容性和通知用户变更，API 的版本管理至关重要。以下是简明的指南：

**语义版本控制（SemVer）**是一种流行的方案，采用 `MAJOR.MINOR.PATCH` 格式，其中：

- 进行不兼容的 API 更改时，递增 `MAJOR` 版本，
- 在向后兼容的方式中添加功能时，递增 `MINOR` 版本，
- 在进行向后兼容的错误修复时，递增 `PATCH` 版本。

**URI 版本控制**包括在 API 端点路径中包含版本号，如 `/v1/resource`。

**参数版本控制**使用请求参数指定版本，例如 `?version=1`。

**头部版本控制**利用自定义 HTTP 头部指示版本。

**媒体类型版本控制**在`Accept`头部中指定版本，使用自定义媒体类型。

选择与你的 API 需求和使用者期望相一致的版本控制策略。通过**变更日志**清晰地传达变更，并确保文档随着 API 一起更新。

对于[向后兼容性](../B/backward-compatibility.md)，考虑同时支持多个版本或提供**弃用政策**，以便给使用者迁移的时间。

以下是使用 URI 版本控制的 API 端点的示例：

```JavaScript
GET /v2/users/123
Host: api.example.com
```

记得保持 API 中的版本控制策略**一致**，以避免混淆。

### 什么是 API 优先设计以及为什么它很重要？

API 优先设计是一种在实施核心应用程序之前优先开发**APIs**的方法。这是一种将 APIs 视为软件开发过程中“一等公民”的策略。

这种设计理念之所以重要，是因为它确保 APIs 是：

- **一致和可重用**的，使它们更有效地为各种客户端应用程序提供服务。
- **明确定义**的，有助于为软件组件之间的交互设定清晰的契约。
- **易于测试**的，因为它们从根本上设计了可以独立验证的端点。
- **灵活**的，可以更容易地与将来的其他服务和系统集成。
- **可扩展**的，因为它们可以开发以处理对核心应用程序的重负载而无需进行重大更改。

通过采用 API 优先设计，组织可以加速其**上线**策略，因为前端和后端团队可以并行工作。它还为开发人员、测试人员和业务利益相关者提供了一个更加**协作的环境**，使其能够在开发周期的早期对 API 的目的和功能达成一致。

在**[测试自动化](../T/test-automation.md)**的背景下，API 优先设计简化了自动化测试的创建，提供了稳定且有文档的接口。这使得测试自动化工程师能够编写更不容易破碎、更专注于验证业务逻辑而不是处理 UI 变化或其他前端问题的测试。

### 开发 API 时需要考虑哪些关键因素？

在开发 API 时，**一致性**对于[可维护性](../M/maintainability.md)和可用性至关重要。确保端点之间的命名惯例、请求/响应格式和行为保持一致。

**性能**必须进行优化；设计高效的数据检索，并考虑实施缓存、分页和压缩以减少延迟。

**可扩展性**是至关重要的；设计你的 API 以优雅地处理用户和数据量的增长，使用负载平衡和水平扩展策略。

**错误处理**应该健壮，提供有意义的 HTTP 状态码和错误消息，使客户端能够理解和解决问题。

**版本控制**对于[向后兼容性](../B/backward-compatibility.md)至关重要；使用清晰的策略，例如基于 URI 路径或标头的版本控制，以管理更改而不干扰客户端。

**安全性**是至关重要的；实施身份验证、授权、输入验证和速率限制，以防范常见的漏洞。

**文档**应该全面且及时，提供清晰的示例和解释，以便为开发人员提供易于集成的支持。

**测试**是不可妥协的；编写自动化测试以覆盖各种场景，包括成功路径、失败和边缘案例。

**弃用政策**应该明确，提供客户端对于重大更改的提前通知和足够的时间来适应。

**监控和日志记录**对于维护健康的 API 至关重要；跟踪使用模式、性能指标和错误，以主动管理 API。

**用户反馈**是无价的；与 API 消费者互动，收集见解并根据他们的经验进行改进。

### API 网关的作用是什么？

**API 网关**充当反向代理，接受所有应用程序编程接口（API）调用，聚合完成这些调用所需的各种服务，并返回适当的结果。在**微服务架构**中，它充当所有客户端的单一入口点，将请求路由到适当的微服务。

API 网关可以处理**横切关注点**，如：

- **身份验证和授权**：验证身份，确保调用者有权限访问服务。
- **速率限制**：控制用户在给定时间范围内可以发出的请求数量，以防止滥用。
- **负载平衡**：将传入的 API 流量分发到多个后端服务，以确保可扩展性和可靠性。
- **缓存**：存储频繁访问的数据副本，以提高响应时间并减少后端负载。
- **请求形状和协议转换**：根据需要修改请求并在不同的 Web 协议之间进行转换。

对于[测试自动化](../T/test-automation.md)工程师来说，API 网关引入了有关**[测试策略](../T/test-strategy.md)**的额外考虑因素。测试应该考虑到网关的行为，包括它如何路由流量和应用策略。自动化测试可能需要模拟网关的操作或绕过它，直接测试各个微服务。

总之，API 网关在微服务架构中扮演着管理 API 调用流的关键角色，提供了一个集中点，用于共享在维护可扩展、安全和高效系统方面至关重要的通用功能。

## API 测试

### 什么是 API 测试以及为什么它很重要？

[API 测试](../A/api-testing.md)是一种[软件测试](../S/software-testing.md)类型，涉及验证和验证应用程序编程接口 (APIs) 及其与其他软件组件的交互。这对确保 APIs 按预期方式运行，高效处理负载并正确响应边缘情况和意外输入是**至关重要**的。

[API 测试](../A/api-testing.md)的重要性在于它专注于软件架构的**业务逻辑层**。与评估前端界面的[UI 测试](../U/ui-testing.md)不同，[API 测试](../A/api-testing.md)处理处理数据和交易的代码，这通常比 UI 更稳定。这种稳定性使得在软件开发生命周期的早期进行测试开发和执行成为可能，从而实现**更快的反馈**和**更快的[迭代](../I/iteration.md)**。

[API 测试](../A/api-testing.md)对于以下方面至关重要：

- 验证通过 APIs 暴露的软件的**核心功能**。
- 确保**数据一致性**、**响应时间**和**错误处理**符合所需的标准。
- 检测安全漏洞和访问控制问题。
- 在不同条件下（包括负载和压力测试）评估性能。
- 通过检查不同软件组件之间的交互促进**[集成测试](../I/integration-testing.md)**。

鉴于微服务和分布式架构的崛起，[API 测试](../A/api-testing.md)变得更加重要，因为系统越

来越多地依赖多个 APIs 协同工作。自动化 API 测试是一种最佳实践，支持持续测试和集成，这是敏捷和 DevOps 方法论的基石。  

### API 测试有哪些不同类型？

不同类型的[API 测试](../A/api-testing.md)侧重于 API 的功能、可靠性、性能和安全性的各个方面。以下是主要类型：

- **[功能测试](../F/functional-testing.md)**: 验证 API 是否按预期行为，涵盖单个功能和端到端场景。
- **[负载测试](../L/load-testing.md)**: 评估高流量下的性能，确保 API 能够处理预期的负载。
- **[压力测试](../S/stress-testing.md)**: 通过超过正常运行能力来确定 API 的破坏点。
- **[安全测试](../S/security-testing.md)**: 识别漏洞，确保数据加密和安全，并验证认证和授权机制的健壮性。
- **[集成测试](../I/integration-testing.md)**: 检查 API 与其他服务和数据库的交互，确保无缝集成。
- **[兼容性测试](../C/compatibility-testing.md)**: 确保 API 在不同设备、操作系统和网络环境中正常工作。
- **[可靠性测试](../R/reliability-testing.md)**: 验证 API 是否可以持续连接并保持稳定性能。
- **[互操作性测试](../I/interoperability-testing.md)**: 确认 API 是否遵循与其他 API 交互的标准和协议。
- **[回归测试](../R/regression-testing.md)**: 在对 API 进行更改后执行，确保新代码不会对现有功能产生不利影响。
- **[性能测试](../P/performance-testing.md)**: 在不同条件下测量 API 的响应速度和稳定性。
- **[API 监控](../A/api-monitoring.md)**: 持续检查生产中的 API，以确保正常运行、响应时间和正确行为。

每种测试类型对于确保 API 的可靠性、安全性、良好性能和与其他系统组件的平滑集成都至关重要。

### API 测试常用的工具有哪些？

常用的[API 测试](../A/api-testing.md)工具包括：

- **[Postman](../P/postman.md)**: 用于 API 开发和测试的热门工具，提供用户友好的界面和各种功能，用于发送请求、分析响应和自动化测试。
- **SoapUI**: 专为 SOAP 和 REST API 测试而设计的开源工具，提供全面的测试功能，包括功能测试、回归测试和负载测试。
- **[JMeter](../J/jmeter.md)**: 主要是性能测试工具，也可用于 API 测试，特别是压力测试和负载测试。
- **Rest-Assured**: 用于简化 RESTful API 测试的 Java DSL，与现有的基于 Java 的测试框架无缝集成。
- **Insomnia**: 强大的 REST 客户端，具有 API 探索和调试功能，以及基本的自动化测试功能。
- **Katalon Studio**: 一体化的自动化解决方案，支持 API 和 UI 测试，提供用户友好的界面用于创建自动化测试。
- **Paw**: 专为 Mac 设计的 API 测试和描述工具，具有完整功能的开发环境。
- **Karate DSL**: 一个开源工具，将 API 测试自动化、模拟、性能测试甚至 UI 自动化集成到一个统一的框架中。
- **[Cypress](../C/cypress.md)**: 主要用于端到端测试 Web 应用程序，但也可通过在测试中直接发送 HTTP 请求进行 API 测试。

这些工具提供各种功能，如[测试自动化](../wTiki/test-automation.md)、请求链接、环境变量和与 CI/CD 管道的集成，以简化和增强[API 测试](../A/api-testing.md)过程。

### API 测试的关键步骤是什么？

[API 测试](../A/api-testing.md)涉及多个关键步骤，以确保应用程序编程接口的功能性、可靠性、安全性和性能。以下是这些基本步骤：

1. **理解 API 需求**：深入了解 API 的预期功能、输入、输出和错误代码。

2. **设置测试环境**：配置进行 API 测试所需的参数、[数据库](../D/database.md)和服务器。

3. **编写[测试用例](../T/test-case.md)**：创建覆盖 API 各个方面的[测试用例](../T/test-case.md)，包括正向、负向、边界和安全测试。

4. **选择合适的工具**：选择符合您需求并与您的 CI/CD 流水线集成的[API 测试](../A/api-testing.md)工具。

5. **执行[测试用例](../T/test-case.md)**：运行测试，验证 API 是否符合定义的需求。这包括对以下方面进行测试：

   - 功能性
   - 可靠性
   - 性能
   - 安全性

6. **检查 API 响应**：确保 API 返回正确的状态码、响应时间和数据结构。

7. **验证数据完整性**：验证在创建、读取、更新或删除资源时，API 是否保持数据一致性和完整性。

8. **使用自动化脚本**：实施自动化的[测试脚本](../T/test-script.md)以使测试过程高效且可重复。

9. **监控性能**：在各种负载条件下评估 API 的响应时间和吞吐量。

10. **分析和报告**：评估测试结果，记录发现，并报告任何缺陷或性能问题。

11. **审查和重构**：持续审查[测试用例](../T/test-case.md)和脚本，以寻求改进和[可维护性](../M/maintainability.md)。

通过遵循这些步骤，您可以确保对[API 测试](../A/api-testing.md)进行全面覆盖，实现强大可靠的 API 集成。

### 如何自动化 API 测试？

要实现[API 测试](../A/api-testing.md)的自动化，按照以下步骤操作：

- **定义[测试用例](../T/test-case.md)**：明确各种 API 请求的预期结果，包括成功和错误的情景。

- **选择测试工具**：选择支持 API 自动化的工具，如[Postman](../P/postman.md)、RestAssured 或 SoapUI。

- **设置测试环境**：配置测试环境，包括必要的标头、身份验证令牌和其他前提条件。

- **编写[测试脚本](../T/test-script.md)**：创建脚本进行 API 调用并验证响应。根据工具的不同，可以使用 JavaScript、Python 或 Java 等编程语言。

```JavaScript
// Example using JavaScript with a testing framework like Mocha
describe('GET /users', () => {
  it('should return a list of users', async () => {
    const response = await request(app).get('/users');
    expect(response.status).to.equal(200);
    expect(response.body).to.be.an('array');
  });
});
```

- **为测试参数化**：使用变量作为输入，轻松测试不同的场景。

- **断言条件**：使用断言检查响应状态码、响应时间和有效负载。

- **与 CI/CD 集成**：在 CI/CD 流水线中自动执行测试，实现持续测试。

- **分析测试结果**：查看[测试报告](../T/test-report.md)，识别任何失败或性能问题。

- **维护测试**：定期更新测试以反映 API 中的更改。

通过自动化 API 测试，确保对 API 功能、可靠性和安全性进行一致高效的验证。

## API 安全

### 与 API 相关的常见安全风险有哪些？

与 APIs 相关的一些常见安全风险包括：

- **注入攻击**：将恶意代码或命令注入到 API 中，以利用漏洞获取未经授权的访问或数据。例如[SQL](../S/sql.md)注入、命令注入和跨站脚本（XSS）攻击。

- **身份验证失效**：身份验证机制存在缺陷，可能允许攻击者冒充合法用户或完全绕过身份验证。

- **敏感数据暴露**：不足的保护机制可能导致敏感数据（如个人信息、凭据或财务数据）的泄露。

- **访问控制问题**：访问控制的不正确实施可能导致未经授权访问 API 功能或数据，即访问控制失效。

- **安全配置错误**：默认配置、不完整的[设置](../S/setup.md)或配置不当的 HTTP 头可能使 APIs 容易受到攻击。

- **大规模赋值**：未经适当过滤的接受 JSON 或 XML 输入的 APIs 可能允许攻击者修改其不应访问的对象属性。

- **日志记录和监控不足**：不足的 API 活动记录和缺乏实时监控可能阻止对主动入侵的检测和响应。

- **不安全的反序列化**：在未经验证的情况下对不受信任的数据进行反序列化可能导致远程代码执行、重放攻击、注入攻击和权限升级。

- **使用已知漏洞的组件**：依赖于具有已知漏洞的库或软件的 APIs 可能容易受到攻击。

- **缺乏速率限制和节流**：没有速率限制，APIs 容易受到暴力攻击和拒绝服务（DoS）攻击。

减轻这些风险涉及实施强大的身份验证和授权、在传输和静态状态下对数据进行加密、验证和清理输入、使用安全的编码实践以及保持所有组件更新。定期进行安全审计和[渗透测试](../P/penetration-testing.md)对于维护 API 安全也至关重要。

### 如何保护 API 的安全？

如何确保 API 的安全性？

确保 API 的安全性涉及采取措施以防止未经授权的访问和各类威胁。以下是一些关键策略：

- **身份验证**：使用 API 密钥、令牌或 HTTP 基本身份验证等机制验证身份。可以考虑使用**OAuth**以实现更精细的访问控制。

- **授权**：确保用户有权执行操作。可以实施基于角色的访问控制（RBAC）或基于属性的访问控制（ABAC）。

- **传输安全**：使用**HTTPS**与**SSL/TLS**加密传输中的数据，以防止被截取或篡改。

- **输入验证**：验证所有输入，以防止注入攻击。使用严格的类型、格式和范围检查。

- **输出编码**：在输出时对数据进行编码，以避免注入漏洞，特别是在 JSON 或 XML API 中。

- **速率限制**：通过限制用户在给定时间内的请求次数来防御 DDoS 攻击。

- **日志记录和监控**：保留详细的日志并监控 API 的使用情况，以便快速检测和响应可疑活动。

- **安全头**：使用 HTTP 头，如`Content-Security-Policy`、`X-Content-Type-Options`和`X-Frame-Options`，以减轻常见攻击。

- **错误处理**：避免在错误消息中显示堆栈跟踪或敏感信息。使用通用错误消息并在服务器端记录详细信息。

- **补丁管理**：定期更新软件，修补 API 平台和依赖项中已知的漏洞。

- **[安全测试](../S/security-testing.md)**：在自动化测试套件中包含安全测试。进行静态分析、动态分析和渗透测试。

通过实施这些实践，您可以为 API 打造一个强大的安全防线。

### 什么是 API 密钥认证？

API 密钥认证是一种简单的安全方法，涉及在请求中发送一个**秘密令牌**以访问 API。API 密钥是服务器用于**验证**请求者身份并**授权**访问 API 资源的唯一标识符。

要实施 API 密钥认证，客户端必须在请求头或作为查询参数中包含 API 密钥。以下是使用 JavaScript 将 API 密钥包含在请求头中的示例：

```JavaScript
fetch('https://api.example.com/data', {
  method: 'GET',
  headers: {
    'Authorization': 'ApiKey YOUR_API_KEY_HERE'
  }
})
.then(response => response.json())
.then(data => console.log(data))
.catch(error => console.error('Error:', error));
```

API 密钥通常由 API 提供者在**注册**过程中提供，并应保持**保密**以防止未经授权的访问。虽然 API 密钥认证易于实施，但单独使用时安全性不是最高的，因为如果未正确处理，密钥可能会被拦截或泄漏。通常与其他安全措施（例如**HTTPS**）一起使用，以确保密钥传输安全。

### 什么是 OAuth 以及它如何在 API 安全中使用？

OAuth 是一种**开放标准**，通常用于允许网站或应用在不需要用户提供密码的情况下访问其他网站上的用户数据。它充当中间层，提供令牌而不是用户凭证，用于访问资源。

在 API 安全中，OAuth 允许客户端代表资源所有者访问服务器资源。它规定了资源所有者在不共享凭证的情况下授权第三方访问其服务器资源的过程。设计时特别考虑了与**HTTP**的兼容性，为发放、验证令牌以及定义访问权限的范围和持续时间提供了安全且标准化的方法。

OAuth 2.0 是目前最广泛使用的版本，定义了四个角色：

- **资源所有者**：授权应用访问其账户的用户。
- **资源服务器**：托管受保护资源的服务器。
- **客户端**：请求访问资源服务器的应用。
- **授权服务器**：在成功验证资源所有者并获得授权后，向客户端发放访问令牌的服务器。

OAuth 的流程通常包括以下步骤：

1. 应用请求用户对其访问服务资源的授权。
2. 如果用户授权该请求，应用收到一个授权授予。
3. 应用通过提供其自身身份和授权授予，向授权服务器请求访问令牌。
4. 如果确认了应用的身份并且授权授予有效，授权服务器向应用发放访问令牌。
5. 应用请求资源服务器的资源并呈现访问令牌进行身份验证。
6. 如果访问令牌有效，资源服务器向应用提供资源。

OAuth 因其能够提供对不同类型访问的**细粒度授权**而在 API 安全领域得到广泛使用。

### SSL/TLS 在 API 安全中的作用是什么？

SSL/TLS通过在客户端和服务器之间建立加密链接，在**API 安全**中发挥着至关重要的作用。这确保了两方之间传输的所有数据都是**私密和完整**的，从而防止窃听、篡改和消息伪造。

当 API 通过 HTTPS 提供服务时，实际上是在 SSL/TLS 上层的 HTTP，因此可以受益于底层的安全特性：

- **加密**：传输过程中对数据进行加密，防止未经授权的访问敏感信息。
- **认证**：使用 SSL/TLS 证书对服务器进行认证，确保客户端与合法服务器进行通信。
- **完整性**：执行数据完整性检查，以检测对传输数据的任何更改。

在进行[API 测试](../A/api-testing.md)时，验证 SSL/TLS 是否得到正确实施变得非常重要：

- **证书验证**：确保 API 服务器提供由受信任的证书颁发机构（CA）颁发的有效证书。
- **协议版本**：确认 API 是否支持协议的安全版本（例如 TLS 1.2、TLS 1.3），并禁用不推荐使用的版本（例如 SSL 3.0、TLS 1.0）。
- **密码套件**：检查 API 是否配置为使用提供强大加密的强密码套件。

将 SSL/TLS 检查纳入到自动化的[API 测试](../A/api-testing.md)中，有助于保持安全姿态并符合最佳实践，使其成为[API 测试](../A/api-testing.md)过程中不可或缺的一环。

## API 文档

### 为什么 API 文档很重要？

API 文档有几个至关重要的原因：

- **清晰性**：文档清晰地描述了 API 提供的内容，包括端点、方法、参数和数据格式。
- **可用性**：良好的文档使开发人员能够快速理解并无需外部支持即可集成 API。
- **效率**：文档降低了学习曲线，有助于在敏捷环境中进行更快的开发和集成。
- **测试**：文档作为测试自动化工程师验证 API 行为是否符合规范的参考。
- **维护**：文档有助于随时间的推移维护 API，使其更容易更新、重构或扩展功能。
- **入职**：新团队成员可以迅速上手，确保连续性和生产力。
- **社区**：对于开源或公共 API，它可以培养一个开发者社区，他们可以为 API 的生态系统做出贡献。

在[测试自动化](../T/test-automation.md)领域，文档有以下应用：

- **生成[测试用例](../T/test-case.md)**：自动化工具可以利用文档生成不同场景的测试用例。
- **模拟服务**：可以创建模拟服务，模拟 API 响应进行测试。
- **验证响应**：确保 API 的输出与文档中预期的响应相匹配。

总体而言，API 文档是支持整个 API 生命周期的基础要素，从设计和开发到测试和维护。

### 好的 API 文档中应该包含哪些内容？

良好的 API 文档应包含以下要素：

- **概述**：对 API 进行简要描述，说明其目的和高层功能。
- **身份验证**：清晰说明如何对 API 进行身份验证，包括任何必需的密钥或令牌。
- **端点**：全面列出可用端点，包括路径、HTTP 方法和每个端点的简要描述。
- **参数**：详细说明请求参数，包括名称、数据类型、是否为强制或可选，以及适用的默认值。
- **请求示例**：每个端点的示例请求，最好用多种语言或工具（如`curl`、`JavaScript`、`Python`）编写。

```Shell
curl -X POST https://api.example.com/v1/resource \
-H "Authorization: Bearer {token}" \
-d '{ "param1": "value1", "param2": "value2" }'
```

- **响应示例**：每个端点的示例响应，包括状态代码、标头和主体内容。
- **错误代码**：列出可能的错误代码、它们的含义以及可能的解决方案或故障排除提示。
- **速率限制**：提供适用于 API 的任何速率限制的信息，包括计算方法以及超出限制时的处理方式。
- **更改日志**：记录 API 所做的所有更改，包括新功能、更新、弃用和删除。
- **联系信息**：提供如何联系 API 提供商以获取支持或反馈的详细信息。

请记住，保持文档**更新**和**准确**，以确保用户获得无缝的集成和测试体验。

### 有哪些工具可用于创建 API 文档？

使用旨在简化流程的各种工具，可以更高效地创建 API 文档。以下是一些广泛使用的选项：

- **[Swagger](../S/swagger.md)/OpenAPI**：提供规范和一套工具，用于生成、可视化和与 API 文档交互。[Swagger](../S/swagger.md) UI 提供了一个基于 Web 的界面，供用户探索 API，而[Swagger](../S/swagger.md) Editor 允许编辑 OpenAPI 规范。

```JavaScript
paths:
  /users:
    get:
      summary: "List all users"
```

- **[Postman](../P/postman.md)**：主要是一个用于[API 测试](../A/api-testing.md)的平台，[Postman](../P/postman.md)还包括用于文档化 APIs 的功能。它可以生成和托管交互式文档，并允许直接从文档页面调用 API。

- **Apiary**：使用 API Blueprint，这是一种基于 Markdown 的文档格式。Apiary 提供一个模拟服务器和其他工具，用于在文档旁边设计和原型化 APIs。

- **Read the Docs**：与您的版本控制系统集成，以每次提交都自动更新文档。它支持 Sphinx，这是一个创建智能且美观文档的工具。

- **Docusaurus**：用于轻松构建、部署和维护开源项目网站的项目。它支持 Markdown，并且与 JSDoc 等文档生成器结合使用时可用于文档化 APIs。

- **MkDocs**：一个面向项目文档的静态站点生成器。通过使用插件，它也可以成为文档化 API 的不错选择。

每个工具都提供独特的功能和集成，因此选择取决于具体的项目要求、首选工作流程以及正在使用的技术栈。

### API 文档应该多久更新一次？

在对 API 进行更改时，应**立即更新**文档。这样可以确保文档准确地反映了 API 的当前状态，对于那些依赖文档进行集成和测试的开发人员来说，这是至关重要的。更新内容应该包括新的端点、对现有端点的更改、不再建议使用的操作以及对请求或响应结构的任何修改。

对于持续交付的环境，考虑将文档过程纳入 CI/CD 流水线。这可以通过使用能够直接从代码或 API 规范生成文档的工具（如 OpenAPI/[Swagger](../S/swagger.md)）来实现。这样，文档将在每次代码发布时自动生成和发布，确保其保持最新状态。

除了自动更新之外，还应定期进行**手动审查**，以确保文档清晰、准确且完整。这可以作为敏捷团队冲刺审查的一部分，也可以按计划定期进行，例如每季度一次。

请记住，过时或不正确的文档可能导致在开发和测试中浪费时间，并有可能引起团队之间的误解。因此，保持 API 文档的实时性不仅是良好实践，也是维护软件开发和[测试自动化](../T/test-automation.md)过程的必要条件。

### API 文档在 API 测试中的作用是什么？

API 文档在[API 测试](../A/api-testing.md)中至关重要，就像一张**路线图**，帮助我们了解 API 的功能、期望行为和集成方式。文档详细介绍了**端点**、**方法**、**参数**以及**请求/响应结构**，测试人员依此创建有实际意义的[test cases](../T/test-case.md)。优秀的文档还包括对请求和响应的**示例**，使得验证 API 是否符合其合同变得更加轻松。

测试人员依赖文档以确保 API 遵循其**规范**。没有准确的文档，测试人员无法有效地执行**合同测试**，验证 API 是否符合服务之间的协定标准。

此外，文档通常详细说明**错误代码**和**消息**，这对于**[负向测试](../N/negative-testing.md)**至关重要。了解 API 在各种故障场景下的行为对于确保错误处理强大且在使用应用程序中出现问题时平滑降级至关重要。

在[自动化测试](../A/automated-testing.md)中，文档可以用于生成在隔离环境中测试的**存根**和**模拟**API 响应。支持**OpenAPI**或其他 API 规范格式的工具可以自动生成这些测试工件，从而简化测试开发流程。

最后，及时更新的文档对于维护和扩展[测试套件](../T/test-suite.md)尤为重要，特别是在 APIs 发生变化时。

它使测试人员能够快速识别变更并调整其测试，确保 API 在更新后仍然能够按预期运行。
