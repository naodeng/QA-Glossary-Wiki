# 邮递员

<!-- TOC START -->
- [相关术语：](#相关术语：)
  - [另请参阅：](#另请参阅：)
- [关于邮递员的问题吗？](#关于邮递员的问题吗？)
  - [基础知识和重要性](#基础知识和重要性)
    - [Postman 是什么以及它的用途是什么？](#postman-是什么以及它的用途是什么？)
    - [为什么 Postman 在软件测试中很重要？](#为什么-postman-在软件测试中很重要？)
    - [Postman 的主要功能是什么？](#postman-的主要功能是什么？)
    - [Postman 如何改进 API 开发流程？](#postman-如何改进-api-开发流程？)
  - [与postman一起工作](#与postman一起工作)
    - [如何安装和设置 Postman？](#如何安装和设置-postman？)
    - [如何在 Postman 中创建新请求？](#如何在-postman-中创建新请求？)
    - [如何在 Postman 中发送请求？](#如何在-postman-中发送请求？)
    - [如何在 Postman 中保存回复？](#如何在-postman-中保存回复？)
    - [如何在 Postman 中使用变量？](#如何在-postman-中使用变量？)
  - [高级功能](#高级功能)
    - [如何使用Postman进行自动化测试？](#如何使用postman进行自动化测试？)
    - [什么是 Postman Collection Runner？如何使用它？](#什么是-postman-collection-runner？如何使用它？)
    - [如何使用 Postman 的脚本功能？](#如何使用-postman-的脚本功能？)
    - [什么是 Postman Monitors 以及它如何工作？](#什么是-postman-monitors-以及它如何工作？)
    - [如何使用Postman进行性能测试？](#如何使用postman进行性能测试？)
  - [集成与协作](#集成与协作)
    - [您如何与其他人共享 Postman 收藏？](#您如何与其他人共享-postman-收藏？)
    - [Postman 如何与其他工具和系统集成？](#postman-如何与其他工具和系统集成？)
    - [Postman 在持续集成（CI）和持续部署（CD）中的作用是什么？](#postman-在持续集成（ci）和持续部署（cd）中的作用是什么？)
    - [在团队环境中如何使用 Postman？](#在团队环境中如何使用-postman？)
<!-- TOC END -->

postman

是一种广泛使用的软件工具，可以帮助

应用程序编程接口

（应用程序编程接口）开发和测试。它提供了一个用户友好的界面，允许开发人员和测试人员向 Web 服务发送请求并接收来自 Web 服务的响应。和

postman

，用户可以创建、保存和组织HTTP请求、测试

蜜蜂

通过发送各种请求类型（GET、POST、PUT、DELETE 等）并检查响应。其他功能包括自动化测试、创建模拟服务器和文档的能力

蜜蜂

。

postman

还为团队提供协作功能，使他们能够共享请求、环境和其他数据的集合。随着时间的推移，

postman

已经从简单的演变而来

API测试

工具综合

应用程序编程接口

开发环境。

## 相关术语：

- [API testing tool](../A/api-testing-tool.md)
- [Swagger](../S/swagger.md)

### 另请参阅：

- [Official Website](https://www.postman.com/)
- [Wikipedia](https://en.wikipedia.org/wiki/Postman_(software))

## 关于邮递员的问题吗？

### 基础知识和重要性

#### Postman 是什么以及它的用途是什么？

[Postman](../P/postman.md) 是一个**[API](../A/api.md)（应用程序编程接口）开发工具**，它简化了构建、测试和修改[APIs](../A/api.md) 的过程。它提供了一个用户友好的界面，用于向 Web 服务发送 HTTP 请求并查看响应，而无需专用客户端或编写自定义代码。 [Postman](../P/postman.md) 支持各种 HTTP 方法，例如 GET、POST、PUT、DELETE，并包含设置标头、添加正文数据和构造查询参数的功能。
  开发人员和测试人员使用 [Postman](../P/postman.md) **验证 [APIs](../A/api.md)** 的行为，确保它们按预期运行、返回正确的数据并正确处理错误。它还用于模拟[API](../A/api.md)请求以检查服务器在不同条件下的响应方式。凭借保存请求和响应的能力，[Postman](../P/postman.md) 促进了团队内或跨项目的[API](../A/api.md) 调用的重用和共享。
  [Postman](../P/postman.md) 的功能超出了[manual testing](../M/manual-testing.md) 的范围。它可用于**自动化 [test suites](../T/test-suite.md)** 并将其集成到 CI/CD 管道中，从而允许定期、系统地验证 [API](../A/api.md) 端点。 [Postman](../P/postman.md) 的脚本功能增强了这种自动化功能，可以执行用 JavaScript 编写的预请求或 [test scripts](../T/test-script.md)。
  在团队环境中，[Postman](../P/postman.md) 提供**协作功能**，允许共享集合、环境和其他配置，确保[API testing](../A/api-testing.md) 和开发工作的一致性和效率。其与其他工具和系统的集成功能进一步简化了工作流程并实现了更具凝聚力的开发流程。

#### 为什么 Postman 在软件测试中很重要？

[Postman](../P/postman.md) 在[software testing](../S/software-testing.md) 中至关重要，因为它能够**验证[API](../A/api.md) 合约**并确保**[API](../A/api.md) 端点**按预期运行。它简化了[API](../A/api.md) 测试的**创建、维护和执行**，从而可以快速反馈服务的运行状况。通过[Postman](../P/postman.md)，测试人员可以轻松地将测试组织到集合中，并将其集成到**CI/CD管道**中，从而大规模推广**[test automation](../T/test-automation.md)**和**[regression testing](../R/regression-testing.md)**。
  该工具的**脚本功能**能够模拟复杂的用户行为和数据驱动的测试，从而增强[API testing](../A/api-testing.md)的深度。 [Postman](../P/postman.md) 的**监控功能**对于生产环境中的**主动问题检测**至关重要，其**共享功能**促进团队成员之间的**协作**，确保[test strategy](../T/test-strategy.md) 实施的一致性和效率。
  通过支持各种**身份验证方法**，[Postman](../P/postman.md) 确保对需要凭据的[APIs](../A/api.md) 进行安全测试。其**[performance testing](../P/performance-testing.md) 功能**支持基本的[load testing](../L/load-testing.md)，有助于在开发周期的早期识别瓶颈和性能问题。
  总之，[Postman](../P/postman.md) 在[software testing](../S/software-testing.md) 中很重要，因为它支持**自动化**、**协作**和**高效测试实践**，这对于现代[API](../A/api.md) 驱动的应用程序至关重要。

#### Postman 的主要功能是什么？

[Postman](../P/postman.md) 的主要功能包括：

- **内置身份验证协议**：简化设置各种身份验证类型（例如 OAuth、基本身份验证、摘要身份验证和[API](../A/api.md) 密钥）的过程。
  - **预请求脚本**：允许编写在发送请求之前运行的 JavaScript 代码，以设置变量或修改请求。
  - **测试**：允许编写 JavaScript 测试来验证响应数据、状态代码和响应时间。
  - **环境**：提供创建不同环境来存储和管理变量集的能力，从而可以轻松切换上下文。
  - **请求链接**：通过在后续请求中使用响应数据，有助于从响应和链接请求中提取数据。
  - **模拟服务器**：提供在实际实现可用之前模拟 [API](../A/api.md) 端点的能力。
  - **文档生成**：自动为[API](../A/api.md) 集合生成并托管精美的机器可读文档。
  - **[API](../A/api.md) 发布**：允许[APIs](../A/api.md) 发布并与其他人共享，提供协作平台。
  - **版本控制**：与版本控制系统集成，以保持 [API](../A/api.md) 集合和环境在团队成员之间保持同步。
  - **工作空间**：支持个人和团队工作空间来组织工作并与团队成员协作。
  - **[API](../A/api.md) 监控**：提供设置按计划时间间隔运行的自动化测试的能力，以监控[APIs](../A/api.md) 的性能和运行状况。
  - **互操作性**：以各种格式导出和导入集合，并与[Swagger](../S/swagger.md)/OpenAPI 规范集成。
  - **插件**：支持一系列插件以及与 Newman 等其他工具的集成，用于从命令行运行集合。
  - **可视化工具**：将响应数据呈现为可自定义的视觉格式，从而实现更直观的数据分析。
  这些功能共同使[Postman](../P/postman.md)成为[API testing](../A/api-testing.md)和开发工作流程的多功能工具。

- **内置身份验证协议**：简化设置各种身份验证类型（例如 OAuth、基本身份验证、摘要身份验证和[API](../A/api.md) 密钥）的过程。
  - **预请求脚本**：允许编写在发送请求之前运行的 JavaScript 代码，以设置变量或修改请求。
  - **测试**：允许编写 JavaScript 测试来验证响应数据、状态代码和响应时间。
  - **环境**：提供创建不同环境来存储和管理变量集的能力，从而可以轻松切换上下文。
  - **请求链接**：通过在后续请求中使用响应数据，有助于从响应和链接请求中提取数据。
  - **模拟服务器**：提供在实际实现可用之前模拟 [API](../A/api.md) 端点的能力。
  - **文档生成**：自动为[API](../A/api.md) 集合生成并托管精美的机器可读文档。
  - **[API](../A/api.md) 发布**：允许[APIs](../A/api.md) 发布并与其他人共享，提供协作平台。
  - **版本控制**：与版本控制系统集成，以保持 [API](../A/api.md) 集合和环境在团队成员之间保持同步。
  - **工作空间**：支持个人和团队工作空间来组织工作并与团队成员协作。
  - **[API](../A/api.md) 监控**：提供设置按计划时间间隔运行的自动化测试的能力，以监控[APIs](../A/api.md) 的性能和运行状况。
  - **互操作性**：以各种格式导出和导入集合，并与[Swagger](../S/swagger.md)/OpenAPI 规范集成。
  - **插件**：支持一系列插件以及与 Newman 等其他工具的集成，用于从命令行运行集合。
  - **可视化工具**：将响应数据呈现为可自定义的视觉格式，从而实现更直观的数据分析。

#### Postman 如何改进 API 开发流程？

[Postman](../P/postman.md) 通过提供用于发送请求、分析响应和共享[APIs](../A/api.md) 的**统一接口**，简化了[API](../A/api.md) 开发。它使开发人员能够通过[API](../A/api.md)端点进行**快速迭代**，并具有可用JavaScript编写的**预请求脚本**和**测试**等功能，从而允许手动和自动验证[API](../A/api.md)行为。
  通过**环境和变量**，[Postman](../P/postman.md)可以方便地模拟不同的应用程序状态，从而可以更轻松地在各种条件下测试[APIs](../A/api.md)，而无需更改代码。此功能对于模拟生产、开发或登台环境特别有用。
  [Postman](../P/postman.md) 中的**模拟服务器** 允许开发人员在实际实现完成之前对 [APIs](../A/api.md) 进行原型设计并模拟后端响应。这可以显着加快前端开发并实现并行工作流。
  **文档生成**是[Postman](../P/postman.md) 帮助[API](../A/api.md) 开发的另一个关键方面。当请求和响应发生变化时，它会自动生成和更新[API](../A/api.md) 文档，确保文档与[API](../A/api.md) 的当前状态保持同步。
  [Postman](../P/postman.md) 的 **协作功能** 通过允许团队成员共享集合和环境来提高团队生产力，为团队内的 [API](../A/api.md) 资源提供单一事实来源。
  最后，[Postman](../P/postman.md) 与 Git 和 CI/CD 工具等版本控制系统的**集成功能**可确保 [API testing](../A/api-testing.md) 和开发实践无缝融入到更广泛的软件开发生命周期中，从而促进更加面向 DevOps 的工作流程。
  通过结合这些功能，[Postman](../P/postman.md) 不仅改善了个人开发人员的体验，还增强了团队协作，从而实现更高效、更集成的[API](../A/api.md) 开发流程。

### 与postman一起工作

#### 如何安装和设置 Postman？

要安装和设置[Postman](../P/postman.md)，请按照以下步骤操作：

1. **下载[Postman](../P/postman.md)**：转到[Postman website](https://www.postman.com/downloads/)并下载适合您的操作系统（Windows、macOS或Linux）的版本。
  2. **安装[Postman](../P/postman.md)**：
    - 对于
      **Windows**
      ，运行下载的
      `.exe`
      文件并按照安装提示进行操作。

- 对于
      **macOS**
      ，打开下载的
      `.zip`
      文件，然后将 Postman 应用程序拖到您的
      `Applications`
      文件夹。

- 对于
      **Linux**
      ，根据发行版，使用包管理器安装下载的
      `.tar.gz`
      或
      `.deb`
      文件。

- 对于
      **Windows**
      ，运行下载的
      `.exe`
      文件并按照安装提示进行操作。

- 对于
      **macOS**
      ，打开下载的
      `.zip`
      文件，然后将 Postman 应用程序拖到您的
      `Applications`
      文件夹。

- 对于
      **Linux**
      ，根据发行版，使用包管理器安装下载的
      `.tar.gz`
      或
      `.deb`
      文件。

3. **启动[Postman](../P/postman.md)**：打开已安装的[Postman](../P/postman.md) 应用程序。
  4. **登录或创建帐户**（可选）：您可以使用现有的 [Postman](../P/postman.md) 帐户登录或创建一个新帐户以跨设备同步您的工作并与其他人协作。
  5. **配置设置**（如有必要）：通过单击右上角的齿轮图标访问设置。根据测试环境的需要配置代理、证书和其他首选项。
  6. **更新环境变量**（如果适用）：如果您有特定于环境的变量，请通过单击右上角的“环境”快速查看（眼睛图标）并管理您的环境来设置它们。
  7. **导入集合或[APIs](../A/api.md)**（可选）：如果您有现有的[Postman](../P/postman.md)集合或[APIs](../A/api.md)，请使用左上角的“导入”按钮导入它们。
  8. **验证安装**：创建一个到公共 [API](../A/api.md) 端点的简单 GET 请求，以确保 [Postman](../P/postman.md) 设置正确并且可以发送请求。
  [Postman](../P/postman.md) 现已安装并设置完毕，可供您创建、发送和管理 [API](../A/api.md) 请求并自动执行测试。

1. **下载[Postman](../P/postman.md)**：转到[Postman website](https://www.postman.com/downloads/)并下载适合您的操作系统（Windows、macOS或Linux）的版本。
  2. **安装[Postman](../P/postman.md)**：
    - 对于
      **Windows**
      ，运行下载的
      `.exe`
      文件并按照安装提示进行操作。

- 对于
      **macOS**
      ，打开下载的
      `.zip`
      文件，然后将 Postman 应用程序拖到您的
      `Applications`
      文件夹。

- 对于
      **Linux**
      ，根据发行版，使用包管理器安装下载的
      `.tar.gz`
      或
      `.deb`
      文件。

- 对于
      **Windows**
      ，运行下载的
      `.exe`
      文件并按照安装提示进行操作。

- 对于
      **macOS**
      ，打开下载的
      `.zip`
      文件，然后将 Postman 应用程序拖到您的
      `Applications`
      文件夹。

- 对于
      **Linux**
      ，根据发行版，使用包管理器安装下载的
      `.tar.gz`
      或
      `.deb`
      文件。

3. **启动[Postman](../P/postman.md)**：打开已安装的[Postman](../P/postman.md) 应用程序。
  4. **登录或创建帐户**（可选）：您可以使用现有的 [Postman](../P/postman.md) 帐户登录或创建一个新帐户以跨设备同步您的工作并与其他人协作。
  5. **配置设置**（如有必要）：通过单击右上角的齿轮图标访问设置。根据测试环境的需要配置代理、证书和其他首选项。
  6. **更新环境变量**（如果适用）：如果您有特定于环境的变量，请通过单击右上角的“环境”快速查看（眼睛图标）并管理您的环境来设置它们。
  7. **导入集合或[APIs](../A/api.md)**（可选）：如果您有现有的[Postman](../P/postman.md)集合或[APIs](../A/api.md)，请使用左上角的“导入”按钮导入它们。
  8. **验证安装**：创建一个到公共 [API](../A/api.md) 端点的简单 GET 请求，以确保 [Postman](../P/postman.md) 设置正确并且可以发送请求。

#### 如何在 Postman 中创建新请求？

要在 [Postman](../P/postman.md) 中创建新请求：

1. 打开 Postman 并确保您位于
    **工作区**
    您要在其中创建请求的位置。

2. 单击
    **新**
    按钮（加号
    `+`
    图标）位于左上角或使用快捷方式
    `Ctrl + N`
    （Windows）或
    `Cmd + N`
    （麦克）。

3. 选择
    **请求**
    从下拉菜单中。

4. 将出现一个对话框。输入一个
    **姓名**
    在“请求名称”字段中输入您的请求。

5. 您可以选择添加
    **描述**
    描述请求的目的。

6. 要整理您的请求，您可以选择将新请求保存到现有的请求中。
    **收藏**
    或通过单击创建一个新的
    **创建收藏**
    按钮。

7. 选择或创建集合后，单击
    **保存到**
    按钮。
  保存后，您可以开始配置您的请求：

- 在请求选项卡中，选择适当的
    **HTTP 方法**
    （GET、POST、PUT、DELETE 等）来自 URL 字段旁边的下拉列表。

- 输入
    **网址**
    您想要将请求发送至。

- 添加
    **标题**
    ,
    **参数**
    , 或
    **身体数据**
    根据您的要求。

- 单击
    **发送**
    按钮来执行请求并查看响应。
  如果您进行了任何修改，请记得单击“**保存**”按钮来保存对请求的更改。

1. 打开 Postman 并确保您位于
    **工作区**
    您要在其中创建请求的位置。

2. 单击
    **新**
    按钮（加号
    `+`
    图标）位于左上角或使用快捷方式
    `Ctrl + N`
    （Windows）或
    `Cmd + N`
    （麦克）。

3. 选择
    **请求**
    从下拉菜单中。

4. 将出现一个对话框。输入一个
    **姓名**
    在“请求名称”字段中输入您的请求。

5. 您可以选择添加
    **描述**
    描述请求的目的。

6. 要整理您的请求，您可以选择将新请求保存到现有的请求中。
    **收藏**
    或通过单击创建一个新的
    **创建收藏**
    按钮。

7. 选择或创建集合后，单击
    **保存到**
    按钮。

- 在请求选项卡中，选择适当的
    **HTTP 方法**
    （GET、POST、PUT、DELETE 等）来自 URL 字段旁边的下拉列表。

- 输入
    **网址**
    您想要将请求发送至。

- 添加
    **标题**
    ,
    **参数**
    , 或
    **身体数据**
    根据您的要求。

- 单击
    **发送**
    按钮来执行请求并查看响应。

#### 如何在 Postman 中发送请求？

要在 [Postman](../P/postman.md) 中发送请求，请按照以下步骤操作：

1. 打开 Postman 并选择
    **工作区**
    您想在哪里工作。

2. 确保您已创建新请求或已打开现有请求。
  3. 在请求选项卡中，选择适当的
    **HTTP 方法**
    （GET、POST、PUT、DELETE 等）从下拉菜单中。

4. 输入
    **网址**
    您想要将请求发送到地址栏中。

5. 如果需要，添加
    **标题**
    单击“标题”选项卡并输入键值对。

6. 对于 POST 或 PUT 等方法，您可能需要随请求发送正文。单击“正文”选项卡，选择适当的格式（例如 raw、form-data、x-www-form-urlencoded），然后输入数据。
  7. 您可以选择添加
    **参数**
    通过单击“参数”选项卡并输入名称-值对来访问 URL。

8. 设置请求后，单击
    **发送**
    按钮。
  响应将出现在 [Postman](../P/postman.md) 界面的下部。您可以查看状态代码、响应时间、大小和响应正文。如果您需要进一步调整，您可以根据需要修改请求并重新发送。
  对于[automated testing](../A/automated-testing.md)，您可以使用JavaScript 在“测试”选项卡中编写**测试**，并利用[Postman](../P/postman.md) 的内置测试片段进行常见断言。发送请求后，测试结果将显示在“测试结果”选项卡中。

1. 打开 Postman 并选择
    **工作区**
    您想在哪里工作。

2. 确保您已创建新请求或已打开现有请求。
  3. 在请求选项卡中，选择适当的
    **HTTP 方法**
    （GET、POST、PUT、DELETE 等）从下拉菜单中。

4. 输入
    **网址**
    您想要将请求发送到地址栏中。

5. 如果需要，添加
    **标题**
    单击“标题”选项卡并输入键值对。

6. 对于 POST 或 PUT 等方法，您可能需要随请求发送正文。单击“正文”选项卡，选择适当的格式（例如 raw、form-data、x-www-form-urlencoded），然后输入数据。
  7. 您可以选择添加
    **参数**
    通过单击“参数”选项卡并输入名称-值对来访问 URL。

8. 设置请求后，单击
    **发送**
    按钮。

#### 如何在 Postman 中保存回复？

要将回复保存在[Postman](../P/postman.md)中，您可以使用以下方法：

1. **手动复制粘贴**：发送请求后，只需选择响应正文，将其复制并粘贴到您所需的位置，例如文本文件或笔记应用程序。
  2. **将响应保存到文件**：
    - 单击
      **“保存响应”**
      按钮位于响应正文旁边。

- 选择
      **“保存到文件”**
      从下拉菜单中。

- 选择文件系统上的位置并使用适当的扩展名保存文件。
    - 单击
      **“保存响应”**
      按钮位于响应正文旁边。

- 选择
      **“保存到文件”**
      从下拉菜单中。

- 选择文件系统上的位置并使用适当的扩展名保存文件。
  3. **使用测试和脚本**：
    - 在
      **“测试”**
      选项卡，编写一个脚本来保存对环境或全局变量的响应：

      ```
      var jsonData = pm.response.json();
      pm.environment.set("responseVariable", JSON.stringify(jsonData));
      ```

- 在需要时从环境或全局变量访问保存的响应。
    - 在
      **“测试”**
      选项卡，编写一个脚本来保存对环境或全局变量的响应：

      ```
      var jsonData = pm.response.json();
      pm.environment.set("responseVariable", JSON.stringify(jsonData));
      ```

- 在需要时从环境或全局变量访问保存的响应。
  4. **使用 Collection Runner 实现自动化**：
    - 创建一个测试脚本来保存如上所述的响应。
    - 使用 Collection Runner 执行请求。
    - 响应将保存在环境或全局变量中以供以后使用或进一步的自动化步骤。
    - 创建一个测试脚本来保存如上所述的响应。
    - 使用 Collection Runner 执行请求。
    - 响应将保存在环境或全局变量中以供以后使用或进一步的自动化步骤。
  5. **[Postman](../P/postman.md) [API](../A/api.md)**：
    - 使用 Postman 的 API 以编程方式检索和保存响应。
    - 使用集合和请求 ID 向 Postman API 发送请求以获取响应数据。
    - 将 API 调用的响应保存到您所需的位置。
    - 使用 Postman 的 API 以编程方式检索和保存响应。
    - 使用集合和请求 ID 向 Postman API 发送请求以获取响应数据。
    - 将 API 调用的响应保存到您所需的位置。
  请记住在保存响应时适当处理敏感数据，确保不会不安全地存储机密信息。

1. **手动复制粘贴**：发送请求后，只需选择响应正文，将其复制并粘贴到您所需的位置，例如文本文件或笔记应用程序。
  2. **将响应保存到文件**：
    - 单击
      **“保存响应”**
      按钮位于响应正文旁边。

- 选择
      **“保存到文件”**
      从下拉菜单中。

- 选择文件系统上的位置并使用适当的扩展名保存文件。
    - 单击
      **“保存响应”**
      按钮位于响应正文旁边。

- 选择
      **“保存到文件”**
      从下拉菜单中。

- 选择文件系统上的位置并使用适当的扩展名保存文件。
  3. **使用测试和脚本**：
    - 在
      **“测试”**
      选项卡，编写一个脚本来保存对环境或全局变量的响应：

      ```
      var jsonData = pm.response.json();
      pm.environment.set("responseVariable", JSON.stringify(jsonData));
      ```

- 在需要时从环境或全局变量访问保存的响应。
    - 在
      **“测试”**
      选项卡，编写一个脚本来保存对环境或全局变量的响应：

      ```
      var jsonData = pm.response.json();
      pm.environment.set("responseVariable", JSON.stringify(jsonData));
      ```

- 在需要时从环境或全局变量访问保存的响应。
  4. **使用 Collection Runner 实现自动化**：
    - 创建一个测试脚本来保存如上所述的响应。
    - 使用 Collection Runner 执行请求。
    - 响应将保存在环境或全局变量中以供以后使用或进一步的自动化步骤。
    - 创建一个测试脚本来保存如上所述的响应。
    - 使用 Collection Runner 执行请求。
    - 响应将保存在环境或全局变量中以供以后使用或进一步的自动化步骤。
  5. **[Postman](../P/postman.md) [API](../A/api.md)**：
    - 使用 Postman 的 API 以编程方式检索和保存响应。
    - 使用集合和请求 ID 向 Postman API 发送请求以获取响应数据。
    - 将 API 调用的响应保存到您所需的位置。
    - 使用 Postman 的 API 以编程方式检索和保存响应。
    - 使用集合和请求 ID 向 Postman API 发送请求以获取响应数据。
    - 将 API 调用的响应保存到您所需的位置。

#### 如何在 Postman 中使用变量？

在 [Postman](../P/postman.md) 中使用变量允许您在请求和脚本中存储和重用值。以下是如何使用它们：

1. **设置变量**：您可以使用`Environment` 或`Globals` 选项卡在[Postman](../P/postman.md) 中设置变量。单击右上角的 `Environment quick look` 图标，然后通过添加变量名称和值来编辑当前环境或全局变量。

    ```
    pm.environment.set("variable_key", "variable_value");
    ```

2. **在请求中使用变量**：通过将变量键括在双花括号中，将变量插入 URL、标头或正文中。

    ```
    https://api.example.com/users/{{user_id}}
    ```

3. **访问脚本中的变量**：使用`pm`对象检索预请求或[test scripts](../T/test-script.md)中的变量值。

    ```
    let userId = pm.environment.get("user_id");
    ```

4. **更新变量**：在脚本执行期间更改现有变量的值。

    ```
    pm.environment.set("user_id", 12345);
    ```

5. **清除变量**：删除变量的值，使其变为未定义。

    ```
    pm.environment.unset("user_id");
    ```[Postman](../P/postman.md) 中的变量按层次划分范围，允许您在全局、集合、环境和本地（数据文件）级别定义它们。这种灵活性使您能够为不同的测试场景和阶段维护不同的值集。请记住为变量使用有意义的名称，以保持请求和脚本的清晰度和可读性。

1. **设置变量**：您可以使用`Environment` 或`Globals` 选项卡在[Postman](../P/postman.md) 中设置变量。单击右上角的 `Environment quick look` 图标，然后通过添加变量名称和值来编辑当前环境或全局变量。

    ```
    pm.environment.set("variable_key", "variable_value");
    ```

2. **在请求中使用变量**：通过将变量键括在双花括号中，将变量插入 URL、标头或正文中。

    ```
    https://api.example.com/users/{{user_id}}
    ```

3. **访问脚本中的变量**：使用`pm`对象检索预请求或[test scripts](../T/test-script.md)中的变量值。

    ```
    let userId = pm.environment.get("user_id");
    ```

4. **更新变量**：在脚本执行期间更改现有变量的值。

    ```
    pm.environment.set("user_id", 12345);
    ```

5. **清除变量**：删除变量的值，使其变为未定义。

    ```
    pm.environment.unset("user_id");
    ```

### 高级功能

#### 如何使用Postman进行自动化测试？

要使用 [Postman](../P/postman.md) 自动进行测试，请执行以下步骤：

1. **创建集合** ：将相关的API请求分组到一个集合中。
  2. **编写测试**：对于每个请求，使用 JavaScript 和 Postman 的 pm 对象在“测试”选项卡中编写测试。例子：

    ```
    pm.test("Status code is 200", function () {
        pm.response.to.have.status(200);
    });
    ```

3. **使用环境变量**：为请求和测试中的动态数据设置环境变量。
  4. **链式请求**：使用
    `pm.sendRequest`
    链接请求并将一个请求的响应用作另一请求的输入。

5. **运行集合** ：使用 Collection Runner 执行集合中的所有请求。或者，选择一个环境并指定迭代和延迟。
  6. **查看结果**：运行后，在 Collection Runner 中分析通过和失败测试的结果。
  7. **使用 Newman 实现自动化**：安装 Postman 的命令行伴侣 Newman，以在 Postman 之外运行集合。使用以下命令：

    ```
    newman run <Collection URL> -e <Environment URL>
    ```

8. **与 CI/CD 集成**：使用构建脚本或配置文件中的适当命令将 Newman 合并到 CI/CD 管道中。
  通过在 [Postman](../P/postman.md) 中自动执行测试，您可以确保 [API](../A/api.md) 在更改后按预期运行，并且您可以将这些测试集成到您的开发工作流程中以进行持续测试。

1. **创建集合** ：将相关的API请求分组到一个集合中。
  2. **编写测试**：对于每个请求，使用 JavaScript 和 Postman 的 pm 对象在“测试”选项卡中编写测试。例子：

    ```
    pm.test("Status code is 200", function () {
        pm.response.to.have.status(200);
    });
    ```

3. **使用环境变量**：为请求和测试中的动态数据设置环境变量。
  4. **链式请求**：使用
    `pm.sendRequest`
    链接请求并将一个请求的响应用作另一请求的输入。

5. **运行集合** ：使用 Collection Runner 执行集合中的所有请求。或者，选择一个环境并指定迭代和延迟。
  6. **查看结果**：运行后，在 Collection Runner 中分析通过和失败测试的结果。
  7. **使用 Newman 实现自动化**：安装 Postman 的命令行伴侣 Newman，以在 Postman 之外运行集合。使用以下命令：

    ```
    newman run <Collection URL> -e <Environment URL>
    ```

8. **与 CI/CD 集成**：使用构建脚本或配置文件中的适当命令将 Newman 合并到 CI/CD 管道中。

#### 什么是 Postman Collection Runner？如何使用它？

**[Postman](../P/postman.md) Collection Runner** 是[Postman](../P/postman.md) 中的一个工具，允许您按指定顺序执行多个[API](../A/api.md) 请求。它对于跨端点集合运行测试、模拟工作流程或执行冒烟测试特别有用。
  要使用集合运行器：

1. 打开Postman并选择您要运行的集合。
  2. 单击
    **跑步者**
    邮递员窗口左下角的按钮。

3. 在 Collection Runner 窗口中，选择集合和环境（如果您使用环境变量）。
  4. 配置迭代、请求之间的延迟和日志响应等选项。
  5. 如果您想要使用不同的数据集运行集合（数据驱动测试），则可以选择一个数据文件。
  6. 单击
    **运行[集合名称]**
    按钮开始执行。
  当 Collection Runner 执行请求时，它会显示实时结果，包括通过/失败的测试、响应时间和日志输出。您可以使用此反馈来调试和优化您的[API](../A/api.md) 请求和测试。
  对于自动化，您可以使用 [Postman](../P/postman.md) 的配套工具 Newman 通过命令行触发 Collection Runner，用于在 [Postman](../P/postman.md) 应用程序之外运行集合。这对于与 CI/CD 管道集成特别有用。

  ```
  newman run <Collection URL or Path> -e <Environment File Path>
  ```请记住在集合中利用 **脚本** 来增强自动化功能，例如设置预请求脚本或将与运行程序中的每个请求一起运行的测试。

1. 打开Postman并选择您要运行的集合。
  2. 单击
    **跑步者**
    邮递员窗口左下角的按钮。

3. 在 Collection Runner 窗口中，选择集合和环境（如果您使用环境变量）。
  4. 配置迭代、请求之间的延迟和日志响应等选项。
  5. 如果您想要使用不同的数据集运行集合（数据驱动测试），则可以选择一个数据文件。
  6. 单击
    **运行[集合名称]**
    按钮开始执行。

#### 如何使用 Postman 的脚本功能？

[Postman](../P/postman.md) 的脚本功能通过请求中的 **预请求脚本** 和 **测试** 选项卡来利用。这些脚本是用 JavaScript 编写的，允许您以编程方式与请求和响应数据进行交互。
  **请求前脚本**：在请求运行之前执行 JavaScript。用它来设置变量、参数或标题。例如：

  ```
  pm.variables.set("timestamp", Date.now());
  ```**测试**：编写测试断言以在发送请求后验证响应数据、状态代码和响应时间。 [Postman](../P/postman.md) 使用 Chai 断言库。例子：

  ```
  pm.test("Status code is 200", function () {
      pm.response.to.have.status(200);
  });
  pm.test("Response time is less than 500ms", function () {
      pm.expect(pm.response.responseTime).to.be.below(500);
  });
  ```**动态变量**：使用 `{{$randomInt}}` 等动态变量为请求生成随机数据。
  **数据文件**：使用 JSON 或 CSV 格式的外部数据文件对不同的数据集运行迭代测试。
  **pm.* API**：访问各种 [Postman](../P/postman.md) 特定的对象和函数，以与环境、集合和请求/响应详细信息进行交互。
  **片段**：从右侧边栏快速添加常用脚本片段以加快测试编写速度。
  **控制台**：通过将输出记录到 [Postman](../P/postman.md) 控制台 (`View` > `Show Postman Console`) 来调试脚本。
  **全局/环境变量**：脚本可以创建、修改或删除全局变量和环境变量以维护请求之间的状态。
  将这些脚本功能与 **Collection Runner** 或 **[Postman](../P/postman.md) Monitors** 相结合，以按计划的时间间隔自动执行 [test suites](../T/test-suite.md) 并监控 [APIs](../A/api.md)。

#### 什么是 Postman Monitors 以及它如何工作？

[Postman](../P/postman.md) 监视器是按计划时间间隔运行收集以检查[APIs](../A/api.md) 的性能和响应的自动化进程。它们通过执行一个集合来工作，该集合是一组预定义的请求，并且可以设置为在各种环境中运行，确保 [APIs](../A/api.md) 随着时间的推移按预期运行。
  要设置监视器，您需要选择一个集合、配置运行频率并指定环境。监视器可以每 5 分钟运行一次，也可以每天、每周或每月运行一次。当监视器运行时，它会执行集合中的每个请求并报告结果。
  监视器可用于：

- **持续监控**：确保您的 API 始终启动并运行。
  - **版本检查**：验证最新部署是否未破坏任何现有功能。
  - **响应时间警报**：当 API 响应速度慢于预期时发出通知，这可能表明存在性能问题。
  监视器的结果可以在 [Postman](../P/postman.md) 应用程序或 Web 仪表板中查看，您可以在其中查看运行历史记录、响应时间以及任何故障的详细信息。您还可以设置集成，以便在监视器出现故障或检测到问题时通过电子邮件、Slack 或其他平台接收通知。
  以下是如何使用 [Postman](../P/postman.md) 的 [API](../A/api.md) 设置监视器的基本示例：

  ```
  POST /monitors
  {
    "name": "API Health Check",
    "collection_uid": "12345-abcdef",
    "environment_uid": "98765-fedcba",
    "schedule": {
      "interval": 10,
      "unit": "minutes"
    }
  }
  ```这将创建一个名为“[API](../A/api.md) Health Check”的监视器，该监视器使用指定的集合和环境每 10 分钟运行一次。

- **持续监控**：确保您的 API 始终启动并运行。
  - **版本检查**：验证最新部署是否未破坏任何现有功能。
  - **响应时间警报**：当 API 响应速度慢于预期时发出通知，这可能表明存在性能问题。

#### 如何使用Postman进行性能测试？

要将[Postman](../P/postman.md) 用于[performance testing](../P/performance-testing.md)，您将主要利用**Collection Runner** 和**[Postman](../P/postman.md) 监视器**。这是一个简洁的指南：

1. **创建集合**：将要测试的所有请求分组到单个集合下。
  2. **编写预请求和[Test Scripts](../T/test-script.md)**：在“预请求”和“测试”选项卡中使用 JavaScript 自定义您的请求和响应处理。
  3. **设置变量**：使用环境或集合变量来模拟不同的场景和数据集。
  4. **运行集合**：使用Collection Runner执行整个集合。调整 [iterations](../I/iteration.md) 和请求之间的延迟以模拟负载。

    ```
    // Example of setting a variable in pre-request script
    pm.variables.set("dynamicValue", Math.floor(Math.random() * 100));
    ```

5. **分析结果**：运行后，检查响应时间、错误率和其他重要指标以评估性能。
  6. **监控性能**：设置 [Postman](../P/postman.md) 监控器以定期运行您的集合，这有助于跟踪一段时间内的性能。
  7. **与 CI/CD 集成**：使用 [Postman](../P/postman.md) 的 Newman 命令行工具将性能测试集成到 CI/CD 管道中以获取定期反馈。
  8. **使用云代理进行扩展**：对于更广泛的[performance testing](../P/performance-testing.md)，请使用[Postman](../P/postman.md) 的云代理来模拟更高的负载和更真实的条件。
  请记住，虽然 [Postman](../P/postman.md) 可以处理基本的 [performance testing](../P/performance-testing.md)，但在处理复杂的 [load testing](../L/load-testing.md) 场景时，它不能替代 [performance testing](../P/performance-testing.md) 等专用工具，例如 [JMeter](../J/jmeter.md) 或 LoadRunner。使用[Postman](../P/postman.md) 进行轻量级性能检查，并使用[API](../A/api.md) 端点[stress testing](../S/stress-testing.md)。

1. **创建集合**：将要测试的所有请求分组到单个集合下。
  2. **编写预请求和[Test Scripts](../T/test-script.md)**：在“预请求”和“测试”选项卡中使用 JavaScript 自定义您的请求和响应处理。
  3. **设置变量**：使用环境或集合变量来模拟不同的场景和数据集。
  4. **运行集合**：使用Collection Runner执行整个集合。调整 [iterations](../I/iteration.md) 和请求之间的延迟以模拟负载。

    ```
    // Example of setting a variable in pre-request script
    pm.variables.set("dynamicValue", Math.floor(Math.random() * 100));
    ```

5. **分析结果**：运行后，检查响应时间、错误率和其他重要指标以评估性能。
  6. **监控性能**：设置 [Postman](../P/postman.md) 监控器以定期运行您的集合，这有助于跟踪一段时间内的性能。
  7. **与 CI/CD 集成**：使用 [Postman](../P/postman.md) 的 Newman 命令行工具将性能测试集成到 CI/CD 管道中以获取定期反馈。
  8. **使用云代理进行扩展**：对于更广泛的[performance testing](../P/performance-testing.md)，请使用[Postman](../P/postman.md) 的云代理来模拟更高的负载和更真实的条件。

### 集成与协作

#### 您如何与其他人共享 Postman 收藏？

要与其他人共享 [Postman](../P/postman.md) 集合，请按照以下步骤操作：

1. **导出收藏集**：单击要共享的收藏集，然后单击三个点以打开收藏集菜单。选择“导出”并选择格式版本。将文件保存到本地系统。
  2. **通过[Postman](../P/postman.md)分享**：如果您使用[Postman](../P/postman.md)的协作功能，请单击收藏选项卡顶部的“分享”按钮。然后，您可以通过电子邮件邀请团队成员或共享该集合的链接。
  3. **使用版本控制**：将导出的集合文件提交到版本控制系统（例如Git）。这允许其他人将集合拉入他们的本地 [Postman](../P/postman.md) 环境中。
  4. **电子邮件或文件共享服务**：将导出的集合文件附加到电子邮件或将其上传到文件共享服务，然后与同事共享链接。
  5. **[Postman](../P/postman.md) [API](../A/api.md) 网络**：将您的收藏发布到 [Postman](../P/postman.md) [API](../A/api.md) 网络以供更广泛的访问。转到[Postman](../P/postman.md) 仪表板，选择您的集合，并将其发布到[API](../A/api.md) 网络。
  6. **[Postman](../P/postman.md) 文档**：生成并共享您的集合的文档。这提供了一个网页，其中包含可以直接从文档运行的所有请求。
  以下是如何使用 [Postman](../P/postman.md) 的 UI 导出集合的示例：

  ```
  1. Click on the collection in the sidebar.
  2. Click on the three dots to open the menu.
  3. Select "Export" -> "Collection v2.1 (Recommended)" -> "Export".
  4. Save the JSON file to your desired location.
  ```请记住告知收件人有效使用集合所需的任何环境变量或先决条件。

1. **导出收藏集**：单击要共享的收藏集，然后单击三个点以打开收藏集菜单。选择“导出”并选择格式版本。将文件保存到本地系统。
  2. **通过 [Postman](../P/postman.md) 共享**：如果您使用 [Postman](../P/postman.md) 的协作功能，请单击收藏选项卡顶部的“共享”按钮。然后，您可以通过电子邮件邀请团队成员或共享该集合的链接。
  3. **使用版本控制**：将导出的集合文件提交到版本控制系统（例如Git）。这允许其他人将集合拉入他们的本地 [Postman](../P/postman.md) 环境。
  4. **电子邮件或文件共享服务**：将导出的集合文件附加到电子邮件或将其上传到文件共享服务，然后与同事共享链接。
  5. **[Postman](../P/postman.md) [API](../A/api.md) 网络**：将您的收藏发布到 [Postman](../P/postman.md) [API](../A/api.md) 网络以供更广泛的访问。转到[Postman](../P/postman.md) 仪表板，选择您的集合，并将其发布到[API](../A/api.md) 网络。
  6. **[Postman](../P/postman.md) 文档**：生成并共享您的集合的文档。这提供了一个网页，其中包含可以直接从文档运行的所有请求。

#### Postman 如何与其他工具和系统集成？

[Postman](../P/postman.md) 与各种工具和系统集成，以增强[test automation](../T/test-automation.md) 和[API](../A/api.md) 开发能力。它提供了与 **Newman**（命令行集合运行器）的 **本机集成**，允许您直接从命令行运行和测试 [Postman](../P/postman.md) 集合。这对于与 **CI/CD 管道**（例如 Jenkins、Travis CI 或 CircleCI）集成特别有用。

  ```
  newman run collection.json
  ```对于**版本控制**，[Postman](../P/postman.md) 与 **Git** 存储库集成，使您能够将集合与源代码同步。这允许[API](../A/api.md) 测试更好地协作和版本控制。
  [Postman](../P/postman.md) 还提供了可用于与其他服务集成的 **[Postman](../P/postman.md) [API](../A/api.md)**。您可以使用此[API](../A/api.md) 以编程方式访问和操作您的集合、环境和运行，这对于自定义集成或扩展[Postman](../P/postman.md) 的功能非常有用。

  ```
  const postmanApiKey = 'PMAK-your-api-key';
  const collectionId = 'your-collection-id';
  ```[Postman](../P/postman.md) 中的 **Webhook** 可以在收集运行完成后触发其他系统中的工作流程，这有利于触发 CI/CD 流程其他部分中的操作。
  对于**监控和报告**，[Postman](../P/postman.md) 与 **Datadog**、**BigPanda** 和 **PagerDuty** 等系统集成，允许您根据监控运行的结果发送警报或日志数据。
  最后，[Postman](../P/postman.md) 的 **Interceptor** 扩展捕获并同步来自浏览器的 cookie 和请求，从而促进 Web 应用程序的测试并允许与基于浏览器的工作流程无缝集成。

#### Postman 在持续集成（CI）和持续部署（CD）中的作用是什么？

[Postman](../P/postman.md) 通过在这些管道中启用自动化 [API testing](../A/api-testing.md)，在**持续集成 (CI)** 和 **持续部署 (CD)** 中发挥着至关重要的作用。通过将 [Postman](../P/postman.md) 集合集成到 CI/CD 工作流程中，团队可以确保每次将更改提交到代码库时，一致且自动地测试 [API](../A/api.md) 端点。
  在 CI/CD [setup](../S/setup.md) 中，[Postman](../P/postman.md) 集合可以使用 [Postman](../P/postman.md) 的命令行 Collection Runner **Newman** 作为构建过程的一部分来执行。 Newman 可以与 Jenkins、Travis CI、CircleCI 和 GitLab CI 等流行的 CI/CD 工具集成，允许在触发新构建时运行 [API](../A/api.md) 测试。
  以下是如何在 CI 脚本中使用 Newman 运行 [Postman](../P/postman.md) 集合的示例：

  ```
  newman run collection.json -e environment.json
  ```如果 [Postman](../P/postman.md) 测试失败，则可以停止构建，确保不会将损坏的代码部署到生产中。这有助于保持应用程序的稳定性和可靠性。
  对于 CD，[Postman](../P/postman.md) 可用于在部署后执行**运行状况检查**和**冒烟测试**，验证实时应用程序是否按预期运行。在将应用程序提供给最终用户之前，此自动化[verification](../V/verification.md) 步骤增加了一层额外的信心。
  通过将 [Postman](../P/postman.md) 集成到 CI/CD 管道中，团队可以实现更快的发布周期、更高质量的软件并减少 [manual testing](../M/manual-testing.md) 工作量，同时确保 [APIs](../A/api.md) 在整个开发生命周期中满足其设计和性能标准。

#### 在团队环境中如何使用 Postman？

在团队环境中使用 [Postman](../P/postman.md) 涉及资源的协作和共享，例如集合、环境和 [APIs](../A/api.md)。以下是如何与您的团队有效使用[Postman](../P/postman.md)：

- **工作空间**：为您的团队创建一个共享工作空间，以访问所有相关的 [Postman](../P/postman.md) 组件。工作空间可以是个人的、团队的、私人的或公共的。
  - **收藏集**：在工作区中与您的团队共享收藏集。使用 **共享** 按钮或将集合拖放到团队工作区中。
  - **环境**：定义具有可在团队中共享的变量的环境。这确保了不同本地 [setups](../S/setup.md) 之间测试的一致性。
  - **角色和权限**：向团队成员分配角色，以控制谁可以查看、编辑或共享集合和环境。
  - **版本控制**：使用[Postman](../P/postman.md)的内置版本控制系统来跟踪集合的更改。提交更改并合并来自队友的更新。
  - **评论**：添加对集合的评论或团队内沟通和反馈的请求。
  - **分叉和合并**：分叉集合以进行实验或进行更改，而不影响团队的主要集合。准备好后合并更改。
  - **集成**：将 [Postman](../P/postman.md) 与 GitHub 等版本控制系统连接，以同步和备份 [Postman](../P/postman.md) 集合。
  - **监控**：在集合上设置监控器以定期运行测试并与团队共享结果。
  - **[API](../A/api.md) 文档**：自动生成[API](../A/api.md) 文档并与您的团队或利益相关者共享，以实现更好的协作。
  - **[Postman](../P/postman.md) [API](../A/api.md)**：使用[Postman](../P/postman.md) [API](../A/api.md) 以编程方式访问和更新[Postman](../P/postman.md) 数据，这对于 CI/CD 管道非常有用。
  请记住在 [Postman](../P/postman.md) 中维护清晰的命名约定和文档，以确保所有团队成员都能轻松理解和使用共享资源。

- **工作空间**：为您的团队创建一个共享工作空间，以访问所有相关的 [Postman](../P/postman.md) 组件。工作空间可以是个人的、团队的、私人的或公共的。
  - **收藏集**：在工作区中与您的团队共享收藏集。使用 **共享** 按钮或将集合拖放到团队工作区中。
  - **环境**：定义具有可在团队中共享的变量的环境。这确保了不同本地 [setups](../S/setup.md) 之间测试的一致性。
  - **角色和权限**：向团队成员分配角色，以控制谁可以查看、编辑或共享集合和环境。
  - **版本控制**：使用[Postman](../P/postman.md)的内置版本控制系统来跟踪集合的更改。提交更改并合并来自队友的更新。
  - **评论**：添加对集合的评论或团队内沟通和反馈的请求。
  - **分叉和合并**：分叉集合以进行实验或进行更改，而不影响团队的主要集合。准备好后合并更改。
  - **集成**：将 [Postman](../P/postman.md) 与 GitHub 等版本控制系统连接，以同步和备份 [Postman](../P/postman.md) 集合。
  - **监控**：在集合上设置监控器以定期运行测试并与团队共享结果。
  - **[API](../A/api.md) 文档**：自动生成[API](../A/api.md) 文档并与您的团队或利益相关者共享，以实现更好的协作。
  - **[Postman](../P/postman.md) [API](../A/api.md)**：使用[Postman](../P/postman.md) [API](../A/api.md) 以编程方式访问和更新[Postman](../P/postman.md) 数据，这对于 CI/CD 管道非常有用。
