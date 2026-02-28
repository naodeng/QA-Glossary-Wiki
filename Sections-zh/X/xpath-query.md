# XPath 查询

<!-- TOC START -->
- [相关术语：](#相关术语：)
  - [另请参阅：](#另请参阅：)
- [有关 XPath 查询的问题吗？](#有关-xpath-查询的问题吗？)
  - [基础知识和重要性](#基础知识和重要性)
    - [什么是 XPath 查询？](#什么是-xpath-查询？)
    - [为什么 XPath 查询在软件自动化中很重要？](#为什么-xpath-查询在软件自动化中很重要？)
    - [XPath 查询的基本组件是什么？](#xpath-查询的基本组件是什么？)
    - [XPath 查询在 e2e 测试中的作用是什么？](#xpath-查询在-e2e-测试中的作用是什么？)
    - [XPath 查询与其他查询语言有何不同？](#xpath-查询与其他查询语言有何不同？)
  - [语法和结构](#语法和结构)
    - [XPath 查询的基本语法是什么？](#xpath-查询的基本语法是什么？)
    - [如何构建 XPath 查询来选择节点？](#如何构建-xpath-查询来选择节点？)
    - [XPath 轴有哪些不同类型？](#xpath-轴有哪些不同类型？)
    - [如何在 XPath 查询中使用谓词？](#如何在-xpath-查询中使用谓词？)
    - [什么是 XPath 函数以及它们如何在查询中使用？](#什么是-xpath-函数以及它们如何在查询中使用？)
  - [应用与使用](#应用与使用)
    - [如何使用 Selenium 中的 XPath 查询进行 Web 自动化测试？](#如何使用-selenium-中的-xpath-查询进行-web-自动化测试？)
    - [XPath 查询在软件自动化中有哪些常见用例？](#xpath-查询在软件自动化中有哪些常见用例？)
    - [如何使用 XPath 查询来导航 XML 文档？](#如何使用-xpath-查询来导航-xml-文档？)
    - [使用 XPath 查询有哪些挑战以及如何克服这些挑战？](#使用-xpath-查询有哪些挑战以及如何克服这些挑战？)
    - [如何使用 XPath Query 从 HTML 中提取数据？](#如何使用-xpath-query-从-html-中提取数据？)
  - [高级概念](#高级概念)
    - [有哪些高级 XPath 函数以及如何使用它们？](#有哪些高级-xpath-函数以及如何使用它们？)
    - [XPath 查询如何与 XML 中的命名空间一起使用？](#xpath-查询如何与-xml-中的命名空间一起使用？)
    - [什么是 XPath 注入以及如何防止它？](#什么是-xpath-注入以及如何防止它？)
    - [编写高效 XPath 查询的最佳实践有哪些？](#编写高效-xpath-查询的最佳实践有哪些？)
    - [XPath Query 如何与 SQL 等其他查询语言结合使用？](#xpath-query-如何与-sql-等其他查询语言结合使用？)
<!-- TOC END -->

一种设计用于提取和操作 XML 文档数据的语言。对于检索 XML 数据以进行内容扫描很有用。

## 相关术语：

- [Web Testing](../W/web-testing.md)
- [UI Testing](../U/ui-testing.md)

### 另请参阅：

- [Wikipedia](https://en.wikipedia.org/wiki/XPath)

## 有关 XPath 查询的问题吗？

### 基础知识和重要性

#### 什么是 XPath 查询？

[XPath Query](../X/xpath-query.md) 是一种功能强大的语言，设计用于从 XML 文档中选择节点。它在查询 HTML 结构时同样有效，特别是在 [web automation](../W/web-automation.md) 框架（如 [Selenium](../S/selenium.md)）中使用时。 XPath 因其精确执行复杂查询的能力而脱颖而出，使测试人员能够精确地定位网页 DOM 中的元素。
  以下是 XPath 表达式的示例，该表达式选择具有包含子字符串“user”的 `name` 属性的所有 `input` 元素：

  ```
  //input[contains(@name, 'user')]
  ```XPath 能够使用各种轴（例如 `ancestor`、`descendant`、`following` 和 `preceding`）导航 DOM，为测试人员提供了一个通用工具包，可以根据 Web 元素在 DOM 树中的位置与它们进行交互。当元素缺乏唯一标识符或 DOM 结构是动态时，这特别有用。
  在[test automation](../T/test-automation.md) 中，XPath 查询通常在脚本中使用来与 Web 元素交互，例如单击按钮或提取文本。 XPath 的精确性使其对​​于断言元素或其状态的存在非常有价值，这对于验证 Web 应用程序的功能至关重要。
  虽然 XPath 是 [web automation](../W/web-automation.md) 的基石，但它需要精心设计，以避免可能因 UI 更改而破坏的脆弱选择器。测试人员必须平衡特异性和灵活性，通常选择能够承受 DOM 结构中微小变化的相对 XPath 表达式。有效使用 XPath 可以显着增强自动化 [test suites](../T/test-suite.md) 的稳健性和 [maintainability](../M/maintainability.md)。

#### 为什么 XPath 查询在软件自动化中很重要？

[XPath Query](../X/xpath-query.md) 在软件[test automation](../T/test-automation.md) 中至关重要，因为它在 XML 和 HTML 文档中定位元素时具有**精确性**和**灵活性**。它使测试人员能够识别具有**特定属性**、**文本值**或**层次关系**的元素，这在处理元素属性或位置可能发生变化的动态或复杂网页时至关重要。
  使用 XPath，自动化工程师可以制作**独特的路径**来与缺少标识符或类的元素进行交互，或者在其他定位器策略不可行时进行交互。这在**端到端 (e2e) 测试**中特别有用，因为在这种情况下需要复制用户与 UI 的交互。
  此外，XPath 在 DOM（文档对象模型）层次结构中**向前和向后**的能力允许更**复杂的元素搜索**，包括根据子元素的属性查找父元素，反之亦然。
  在 **[Selenium](../S/selenium.md)** 和其他 [web automation](../W/web-automation.md) 工具的上下文中，XPath 通常是**首选**查询语言，因为它具有**跨浏览器兼容性**和对**复杂定位器**的支持。它也是用于**断言**的强大工具，允许测试人员验证页面中元素的存在、不存在或状态。
  然而，与 CSS 选择器相比，XPath 查询可能**脆弱**且**慢**，尤其是对于结构不良的 HTML。为了缓解这种情况，编写**高效**和**弹性** XPath 表达式非常重要，重点关注**相对路径**和**鲁棒属性**。
  总之，XPath 是 [test automation](../T/test-automation.md) 工程师的工具库中不可或缺的工具，它提供了在自动化测试中有效地与 UI 元素交互和验证 UI 元素所需的**粒度**和**控制**。

#### XPath 查询的基本组件是什么？

[XPath query](../X/xpath-query.md) 的基本组件包括：

- **根节点** ：查询的起点，表示为
    `/`
    。

- **Element** ：XML/HTML 元素的标签名称。例如，
    `div`
    。

- **属性**：元素的属性，可通过以下方式访问
    `@`
    。例如，
    `@id`
    。

- **文本节点**：元素内的文本内容，可通过以下方式访问
    `text()`
    。

- **通配符**：
    `*`
    符号，匹配任何元素节点。

- **谓词**：用方括号括起来
    `[]`
    、谓词通过提供具体标准来细化选择。

- **运算符**：符号如
    `=`
    ,
    `!=`
    ,
    `>`
    ,
    `<`
    ,
    `or`
    , 和
    `and`
    定义谓词内的条件。

- **函数**：内置函数，例如
    `contains()`
    ,
    `starts-with()`
    , 和
    `count()`
    在节点上执行操作。

- **轴说明符** ：定义节点之间的树关系，如
    `child::`
    ,
    `ancestor::`
    , 或
    `following-sibling::`
    。
  [XPath query](../X/xpath-query.md) 结构示例：

  ```
  //div[@class='example']//a[text()='Click Here']/@href
  ```在这个例子中：

- `//`
    从文档中的任意位置选择节点。

- `div`
    指定元素类型。

- `[@class='example']`
    是一个谓词过滤
    `div`
    类属性为“example”的元素。

- `//a`
    选择全部
    `a`
    的后代元素
    `div`
    。

- `[text()='Click Here']`
    是另一个谓词，这次选择
    `a`
    带有文本“单击此处”的元素。

- `/@href`
    选择
    `href`
    的属性
    `a`
    元素。

- **根节点** ：查询的起点，表示为
    `/`
    。

- **Element** ：XML/HTML 元素的标签名称。例如，
    `div`
    。

- **属性**：元素的属性，可通过以下方式访问
    `@`
    。例如，
    `@id`
    。

- **文本节点**：元素内的文本内容，可通过以下方式访问
    `text()`
    。

- **通配符**：
    `*`
    符号，匹配任何元素节点。

- **谓词**：用方括号括起来
    `[]`
    、谓词通过提供具体标准来细化选择。

- **运算符**：符号如
    `=`
    ,
    `!=`
    ,
    `>`
    ,
    `<`
    ,
    `or`
    , 和
    `and`
    定义谓词内的条件。

- **函数**：内置函数，例如
    `contains()`
    ,
    `starts-with()`
    , 和
    `count()`
    在节点上执行操作。

- **轴说明符** ：定义节点之间的树关系，如
    `child::`
    ,
    `ancestor::`
    , 或
    `following-sibling::`
    。

- `//`
    从文档中的任意位置选择节点。

- `div`
    指定元素类型。

- `[@class='example']`
    是一个谓词过滤
    `div`
    类属性为“example”的元素。

- `//a`
    选择全部
    `a`
    的后代元素
    `div`
    。

- `[text()='Click Here']`
    是另一个谓词，这次选择
    `a`
    带有文本“单击此处”的元素。

- `/@href`
    选择
    `href`
    的属性
    `a`
    元素。

#### XPath 查询在 e2e 测试中的作用是什么？

在端到端 (e2e) 测试中，**[XPath Query](../X/xpath-query.md)** 在定位 Web 元素并与之交互方面发挥着至关重要的作用。它使测试人员能够精确定位网页的文档对象模型 (DOM) 中的特定元素，这对于模拟用户交互（例如单击按钮、输入文本以及验证元素的存在或属性）至关重要。
  XPath 能够使用各种轴和函数在 DOM 中导航，从而实现动态且灵活的元素选择。这在网页结构可能发生变化的 e2e 测试中特别有用，需要选择器能够适应这些变化而不破坏测试。
  例如，在复杂的 Web 应用程序中，元素可能没有唯一的标识符或一致的 CSS 类。 XPath 可以遍历 DOM，根据元素与其他元素的关系来查找元素，这在面对 UI 变化时不那么脆弱。
  此外，XPath 对谓词的支持使测试人员能够根据条件细化其元素选择，确保即使具有相似属性的元素也能被区分并准确定位。
  在 [Selenium](../S/selenium.md) 等自动化 e2e 测试框架中，XPath 通常用于创建强大的定位器。例如：

  ```
  driver.findElement(By.xpath("//button[text()='Submit']")).click();
  ```这行代码将找到一个带有文本“提交”的按钮并执行单击操作，模仿用户在 [test scenario](../T/test-scenario.md) 期间的交互。
  总体而言，[XPath Query](../X/xpath-query.md) 对于在 e2e 测试中实现元件定位策略的精确性和灵活性是不可或缺的，有助于实现更可靠和可维护的[test suites](../T/test-suite.md)。

#### XPath 查询与其他查询语言有何不同？

[XPath Query](../X/xpath-query.md) 与其他查询语言的不同之处主要在于它对 XML 和 HTML 结构的**特异性。与 [SQL](../S/sql.md)（设计用于查询关系 [databases](../D/database.md)）或 CSS 选择器（用于在 HTML 中设置样式和选择元素）不同，XPath 允许根据各种条件（包括节点的层次结构、属性和 XML 文档中的内容）**选择节点**。
  XPath 以其**丰富的函数**和**轴**而脱颖而出，允许复杂的遍历和选择，而这在其他语言中并不那么简单。例如，虽然 CSS 选择器可用于导航 HTML 文档，但它们缺乏在文档层次结构中向上遍历或基于文本内容选择节点的能力，而 XPath 可以轻松做到这两点。
  此外，XPath 使用**谓词**的能力提供了比 CSS 选择器中通常提供的更精细的选择控制级别。这使得它对于需要精确提取数据的场景特别强大，例如在需要针对特定​​元素的[test automation](../T/test-automation.md)中。
  与用于 JSON 对象的 JSONPath 不同，XPath 是针对 XML 的结构化特性而设计的，不能直接应用于 JSON。但是，两者都具有相似的路径表达式概念来导航元素。
  总体而言，XPath 的独特功能使其成为需要在 XML 和 HTML 文档中**精确导航和选择**的场景中不可或缺的工具，特别是在软件[test automation](../T/test-automation.md) 的上下文中。

### 语法和结构

#### XPath 查询的基本语法是什么？

[XPath query](../X/xpath-query.md) 的基本语法由路径表达式组成，该表达式定义在 XML 文档中导航元素和属性的方式。这是一个简化的细分：

- **绝对路径**：以单个正斜杠开头
    `/`
    指示根节点，后跟所需元素的路径。

    ```
    /root/child/grandchild
    ```

- **相对路径**：以双正斜杠开头
    `//`
    它从当前节点中选择与选择匹配的节点，无论它们位于文档中的位置。

    ```
    //grandchild
    ```

- **谓词**：使用方括号
    `[]`
    按条件过滤节点。

    ```
    /root/child[1]
    ```

- **属性**：使用
    `@`
    用于选择属性的符号。

    ```
    //child[@attr='value']
    ```

- **通配符**：星号
    `*`
    匹配任意元素节点。

    ```
    /root/*
    ```

- **当前节点**：一个句点
    `.`
    表示当前节点上下文。

    ```
    .//child
    ```

- **父节点**：两个周期
    `..`
    向上导航到父节点。

    ```
    ../sibling
    ```这些元素可以组合起来形成复杂的查询，从而精确定位 XML 结构中所需的节点。请记住使用简洁的表达式并利用特定的路径和谓词来实现高效的查询。

- **绝对路径**：以单个正斜杠开头
    `/`
    指示根节点，后跟所需元素的路径。

    ```
    /root/child/grandchild
    ```

- **相对路径**：以双正斜杠开头
    `//`
    它从当前节点中选择与选择匹配的节点，无论它们位于文档中的位置。

    ```
    //grandchild
    ```

- **谓词**：使用方括号
    `[]`
    按条件过滤节点。

    ```
    /root/child[1]
    ```

- **属性**：使用
    `@`
    用于选择属性的符号。

    ```
    //child[@attr='value']
    ```

- **通配符**：星号
    `*`
    匹配任意元素节点。

    ```
    /root/*
    ```

- **当前节点**：一个句点
    `.`
    表示当前节点上下文。

    ```
    .//child
    ```

- **父节点**：两个周期
    `..`
    向上导航到父节点。

    ```
    ../sibling
    ```

#### 如何构建 XPath 查询来选择节点？

要构造[XPath query](../X/xpath-query.md)来选择节点，请遵循以下准则：

- **识别起点**：选择搜索应开始的上下文节点。如果没有指定上下文，则从根节点开始查询。
  - **使用路径表达式**：组合步骤以在节点中导航。步骤之间用斜杠分隔（`/` 表示直接子级，`//` 表示任何后代）。
  - **按名称选择节点**：指定所需节点的标签名称。使用`*` 匹配任何节点。
  - **应用谓词**：将谓词括在方括号`[]` 中，以根据属性、位置或内容等条件过滤节点。
  - **指定轴**：包括轴来定义当前节点和要选择的节点之间的关系（例如，`ancestor`、`descendant`、`following-sibling`）。
  - **利用运算符**：使用 `and`、`or`、`=`、`!=` 等运算符组合谓词内的条件。
  - **合并函数**：使用 XPath 函数进行字符串操作、数值计算或节点集处理（例如 `text()`、`contains()`、`count()`）。
  以下是结构化 [XPath query](../X/xpath-query.md) 的示例：

  ```
  //div[@class='container']/table//tr[td[contains(text(),'Automation')]]
  ```此查询选择所有 `tr` 元素，这些元素的 `td` 子元素包含任何 `table` 中的文本“Automation”，该 `table` 是类属性为“container”的 `div` 的后代。

- **识别起点**：选择搜索应开始的上下文节点。如果没有指定上下文，则从根节点开始查询。
  - **使用路径表达式**：组合步骤以在节点中导航。步骤之间用斜杠分隔（`/` 表示直接子级，`//` 表示任何后代）。
  - **按名称选择节点**：指定所需节点的标签名称。使用`*` 匹配任何节点。
  - **应用谓词**：将谓词括在方括号`[]` 中，以根据属性、位置或内容等条件过滤节点。
  - **指定轴**：包括轴来定义当前节点和要选择的节点之间的关系（例如，`ancestor`、`descendant`、`following-sibling`）。
  - **利用运算符**：使用 `and`、`or`、`=`、`!=` 等运算符组合谓词内的条件。
  - **合并函数**：使用 XPath 函数进行字符串操作、数值计算或节点集处理（例如 `text()`、`contains()`、`count()`）。

#### XPath 轴有哪些不同类型？

XPath 轴定义相对于当前节点的节点集。以下是查询中使用的不同类型的 XPath 轴：

- **ancestor** ：选择当前节点的所有祖先（父节点、祖父母等）。
  - **ancestor-or-self** ：选择所有祖先和当前节点。
  - **attribute** ：选择当前节点的所有属性。
  - **child** ：选择当前节点的所有子节点。
  - **descendant** ：选择当前节点的所有后代（子节点、孙子节点等）。
  - **descendant-or-self** ：选择所有后代和当前节点本身。
  - **following** ：选择文档中当前节点结束标记之后的所有内容。
  - **following-sibling** ：选择当前节点之后的所有同级节点。
  - **namespace** ：选择当前节点的所有命名空间节点。
  - **parent** ：选择当前节点的父节点。
  - **preceding** ：选择文档中当前节点之前出现的所有节点，祖先、属性节点和命名空间节点除外。
  - **preceding-sibling** ：选择当前节点之前的所有同级节点。
  - **self** ：选择当前节点。
  [XPath query](../X/xpath-query.md) 中的用法示例：

  ```
  //book/child::*
  ```这将选择 `book` 节点的所有子元素。 [Test automation](../T/test-automation.md) 工程师使用这些轴在 XML 或 HTML 文档结构中导航，从而可以精确定位用于交互和验证的元素。

- **ancestor** ：选择当前节点的所有祖先（父节点、祖父母等）。
  - **ancestor-or-self** ：选择所有祖先和当前节点。
  - **attribute** ：选择当前节点的所有属性。
  - **child** ：选择当前节点的所有子节点。
  - **descendant** ：选择当前节点的所有后代（子节点、孙子节点等）。
  - **descendant-or-self** ：选择所有后代和当前节点本身。
  - **following** ：选择文档中当前节点结束标记之后的所有内容。
  - **following-sibling** ：选择当前节点之后的所有同级节点。
  - **namespace** ：选择当前节点的所有命名空间节点。
  - **parent** ：选择当前节点的父节点。
  - **preceding** ：选择文档中当前节点之前出现的所有节点，祖先、属性节点和命名空间节点除外。
  - **preceding-sibling** ：选择当前节点之前的所有同级节点。
  - **self** ：选择当前节点。

#### 如何在 XPath 查询中使用谓词？

XPath 中的谓词在方括号内使用，以按特定条件过滤节点。他们通过提供选择节点必须满足的附加条件来完善选择。
  例如，要选择文档中的第三个 `book` 元素：

  ```
  //book[3]
  ```您还可以使用谓词根据子节点值或属性过滤节点。要选择`category` 属性为`fiction` 的`book` 元素：

  ```
  //book[@category='fiction']
  ```谓词可以包含函数。要选择具有多个 `author` 子级的 `book` 元素：

  ```
  //book[count(author) > 1]
  ```逻辑运算符可用于组合多个条件。要选择 `fiction` 类别中且价格小于 10 的 `book` 元素：

  ```
  //book[@category='fiction' and price<10]
  ```谓词也可以嵌套。要选择所有`book` 元素中第一个`author` 的`name`：

  ```
  //book/author[1]/name
  ```有效使用谓词可以实现更精确、更高效的 XPath 查询，这对于 [test automation](../T/test-automation.md) 中准确定位元素并对元素执行操作或验证至关重要。

#### 什么是 XPath 函数以及它们如何在查询中使用？

XPath 函数是可在 XPath 表达式中使用的操作，用于在节点或节点集、字符串、数字和布尔值上执行各种任务。它们是完善 XPath 查询不可或缺的一部分，可分为：

- **节点集函数**：在节点集上操作，例如，
    `count()`
    ,
    `position()`
    。

- **字符串函数**：操作字符串，例如，
    `concat()`
    ,
    `contains()`
    ,
    `substring()`
    。

- **布尔函数**：处理逻辑运算，例如，
    `not()`
    ,
    `true()`
    ,
    `false()`
    。

- **数字函数**：执行数字运算，例如，
    `sum()`
    ,
    `floor()`
    ,
    `round()`
    。
  在[test automation](../T/test-automation.md)中，函数用于增强节点的选择。例如，要查找具有特定属性值的元素，您可以使用：

  ```
  //input[contains(@id, 'username')]
  ```这里，`contains()` 是一个字符串函数，用于检查`id` 属性是否包含子字符串“username”。
  要选择元素列表，然后在该列表中查找第三个元素，您可以使用：

  ```
  (//div[@class='item'])[position()=3]
  ```在本例中，`position()` 是一个节点集函数，用于检索节点在其上下文中的索引。
  可以嵌套和组合函数来创建复杂的查询。例如，要选择一个未选中的复选框：

  ```
  //input[@type='checkbox' and not(@checked)]
  ````not()` 函数反转`@checked` 谓词的布尔结果。
  正确使用函数可以大大提高 [test automation](../T/test-automation.md) 脚本中 XPath 查询的精度和效率。

- **节点集函数**：在节点集上操作，例如，
    `count()`
    ,
    `position()`
    。

- **字符串函数**：操作字符串，例如，
    `concat()`
    ,
    `contains()`
    ,
    `substring()`
    。

- **布尔函数**：处理逻辑运算，例如，
    `not()`
    ,
    `true()`
    ,
    `false()`
    。

- **数字函数**：执行数字运算，例如，
    `sum()`
    ,
    `floor()`
    ,
    `round()`
    。

### 应用与使用

#### 如何使用 Selenium 中的 XPath 查询进行 Web 自动化测试？

在 [Selenium](../S/selenium.md) 中使用 **XPath** 进行 [web automation](../W/web-automation.md) 测试涉及通过元素的 XML 路径来定位网页上的元素。以下是有关如何实现此目的的简明指南：

1. **导入**
    测试脚本中必要的 Selenium WebDriver 类：

  ```
  import org.openqa.selenium.By;
  import org.openqa.selenium.WebDriver;
  import org.openqa.selenium.WebElement;
  ```

1. **实例化**
    WebDriver 并导航到所需的 URL：

  ```
  WebDriver driver = new ChromeDriver();
  driver.get("http://example.com");
  ```

1. **定位元素**
    使用
    `driver.findElement()`
    方法结合
    `By.xpath()`：

  ```
  WebElement element = driver.findElement(By.xpath("//tagname[@attribute='value']"));
  ```将 `tagname`、`attribute` 和 `value` 替换为您想要查找的适当的 HTML 元素标记、属性名称和属性值。

1. **互动**
    使用找到的元素，例如，通过单击按钮或检索其文本：

  ```
  element.click();
  String text = element.getText();
  ```

1. **链** XPath 函数和谓词可在处理复杂的 HTML 结构时优化您的选择。
  2. 测试完成后**关闭**浏览器：

  ```
  driver.quit();
  ```请记住**处理异常**，例如`NoSuchElementException`，以使您的测试稳健。在尝试对元素执行操作之前，使用**显式等待**来确保元素存在且可交互。

  ```
  WebDriverWait wait = new WebDriverWait(driver, Duration.ofSeconds(10));
  WebElement dynamicElement = wait.until(ExpectedConditions.presenceOfElementLocated(By.xpath("//tagname[@attribute='value']")));
  ```通过执行这些步骤，您可以有效地利用 [Selenium](../S/selenium.md) 中的 XPath 来定位和操作 Web 元素，以满足您的自动化测试需求。

1. **导入**
    测试脚本中必要的 Selenium WebDriver 类：

1. **实例化**
    WebDriver 并导航到所需的 URL：

1. **定位元素**
    使用
    `driver.findElement()`
    方法结合
    `By.xpath()`：

1. **互动**
    使用找到的元素，例如，通过单击按钮或检索其文本：

1. **链** XPath 函数和谓词可在处理复杂的 HTML 结构时优化您的选择。
  2. 测试完成后**关闭**浏览器：

#### XPath 查询在软件自动化中有哪些常见用例？

[XPath Query](../X/xpath-query.md) 通常用于软件[test automation](../T/test-automation.md)，用于以下[use cases](../U/use-case.md)：

- **定位元素**：自动化程序使用 XPath 来查明网页或 XML 文档中需要交互或验证的特定元素。例如，单击按钮、选中复选框或验证节点是否存在。

  ```
  driver.findElement(By.xpath("//button[text()='Submit']")).click();
  ```

- **动态元素识别**：当元素具有动态 ID 或类时，XPath 可以使用部分匹配或其他属性来定位这些元素。

  ```
  driver.findElement(By.xpath("//div[contains(@class,'dynamic-class')]"));
  ```

- **复杂 DOM 遍历**：XPath 擅长通过使用轴和谓词遍历父节点、子节点或同级节点来导航复杂的文档对象模型 (DOM)。

  ```
  driver.findElement(By.xpath("//table[@id='data']/tbody/tr[3]/td[2]"));
  ```

- **处理 Web 表**：XPath 查询可以迭代 Web 表的行和列以提取数据或与数据交互。

  ```
  driver.findElement(By.xpath("//table[@id='data']/tbody/tr[*]/td[1]"));
  ```

- **自定义搜索**：XPath 的功能允许自定义搜索，例如选择具有特定文本、属性值或遵循特定模式的元素。

  ```
  driver.findElement(By.xpath("//p[starts-with(@id,'message')]"));
  ```

- **XML 数据提取**：在非 Web 上下文中，XPath 用于从 XML 文件中提取信息，这对于配置、数据驱动测试或验证 API 响应非常有用。

  ```
  Document doc = builder.parse(new File("config.xml"));
  XPathExpression expr = xpath.compile("//settings/timeout");
  ```

- **条件元素选择**：XPath 在谓词中使用条件的能力使测试人员能够根据复杂的标准选择元素。

  ```
  driver.findElement(By.xpath("//input[@type='checkbox' and not(@disabled)]"));
  ```这些[use cases](../U/use-case.md) 展示了 XPath 在解决软件[test automation](../T/test-automation.md) 中遇到的各种场景方面的多功能性。

- **定位元素**：自动化程序使用 XPath 来查明网页或 XML 文档中需要交互或验证的特定元素。例如，单击按钮、选中复选框或验证节点是否存在。
  - **动态元素识别**：当元素具有动态 ID 或类时，XPath 可以使用部分匹配或其他属性来定位这些元素。
  - **复杂 DOM 遍历**：XPath 擅长通过使用轴和谓词遍历父节点、子节点或同级节点来导航复杂的文档对象模型 (DOM)。
  - **处理 Web 表**：XPath 查询可以迭代 Web 表的行和列以提取数据或与数据交互。
  - **自定义搜索**：XPath 的功能允许自定义搜索，例如选择具有特定文本、属性值或遵循特定模式的元素。
  - **XML 数据提取**：在非 Web 上下文中，XPath 用于从 XML 文件中提取信息，这对于配置、数据驱动测试或验证 API 响应非常有用。
  - **条件元素选择**：XPath 在谓词中使用条件的能力使测试人员能够根据复杂的标准选择元素。

#### 如何使用 XPath 查询来导航 XML 文档？

[XPath Query](../X/xpath-query.md) 可用于通过提供一种选择和遍历文档树中的节点的方法来导航 XML 文档。它允许精确定位 XML 结构中的特定元素、属性或文本，从而实现精确的数据提取或操作。
  例如，要选择 `library` 元素中的所有 `book` 元素，您可以使用：

  ```
  /library/book
  ```要进一步细化对具有特定 `author` 属性的书籍的选择，您可以添加一个谓词：

  ```
  /library/book[@author='John Doe']
  ```导航到子节点很简单；如果您需要选择每个`book`的`title`，则查询将为：

  ```
  /library/book/title
  ```对于相对导航，XPath 提供了 `ancestor`、`descendant`、`following` 和 `preceding` 等轴。要选择 `book` 后面带有特定 `id` 的所有 `book` 元素，您可以使用：

  ```
  //book[@id='123']/following-sibling::book
  ```XPath 还允许根据节点的位置选择节点。要获取`library`中的第一个`book`：

  ```
  /library/book[1]
  ```或者选择除第一个之外的所有 `book` 元素：

  ```
  /library/book[position()>1]
  ```使用[test automation](../T/test-automation.md) 中的 XPath，工程师可以断言 XML 响应或配置的存在、值和结构，确保软件在与基于 XML 的数据交互时按预期运行。

#### 使用 XPath 查询有哪些挑战以及如何克服这些挑战？

XPath 查询可能会给 [test automation](../T/test-automation.md) 带来一些挑战：

- **性能问题**：复杂的 XPath 表达式可能会很慢，尤其是对于大型文档。为了克服这个问题，请使用更具体的路径并避免使用通配符。通过针对具有独特属性的元素进行优化。
  - **[Maintainability](../M/maintainability.md)**：XPath 可能很脆弱，会随着 UI 更改而中断。尽可能使用`id` 或`name` 等稳定标识符。在适当的情况下使用 CSS 选择器可以增强 [maintainability](../M/maintainability.md)。
  - **动态内容**：具有动态内容的页面可能会使 XPath 无效。利用`contains()`、`starts-with()` 或`text()` 等函数来匹配动态文本模式。对于动态 ID，与这些函数的部分匹配会有所帮助。
  - **复杂性**：编写复杂的 XPath 可能容易出错。将复杂的查询分解为更简单、可组合的部分。在组合每个部分之前测试并验证它们。
  - **命名空间处理**：XML 命名空间可能会使 XPath 查询复杂化。使用 local-name() 和 namespace-uri() 函数来处理命名空间或在 XPath 引擎中注册命名空间前缀。
  - **跨浏览器兼容性**：不同的浏览器对 XPath 的解释可能略有不同。通过跨浏览器测试 XPath 并使用 [Selenium](../S/selenium.md) 等工具来消除一些差异，确保跨浏览器兼容性。
  - **学习曲线**：XPath 的灵活性和强大功能也伴随着复杂性。投入时间学习和实践。使用 XPath 帮助器扩展等工具来构建和测试查询。
  以下是优化 XPath 以获得更好性能的示例：

  ```
  //div[@id='content']/table//tr[td/text()='Specific Text']
  ```如果结构已知，可以通过避免 `//` 运算符来优化：

  ```
  //div[@id='content']/table/tbody/tr[td='Specific Text']
  ```通过采用战略方法应对这些挑战，XPath 可以成为定位 [test automation](../T/test-automation.md) 中元素的强大工具。

- **性能问题**：复杂的 XPath 表达式可能会很慢，尤其是对于大型文档。为了克服这个问题，请使用更具体的路径并避免使用通配符。通过针对具有独特属性的元素进行优化。
  - **[Maintainability](../M/maintainability.md)**：XPath 可能很脆弱，会随着 UI 更改而中断。尽可能使用`id` 或`name` 等稳定标识符。在适当的情况下使用 CSS 选择器可以增强 [maintainability](../M/maintainability.md)。
  - **动态内容**：具有动态内容的页面可能会使 XPath 无效。利用`contains()`、`starts-with()` 或`text()` 等函数来匹配动态文本模式。对于动态 ID，与这些函数的部分匹配会有所帮助。
  - **复杂性**：编写复杂的 XPath 可能容易出错。将复杂的查询分解为更简单、可组合的部分。在组合每个部分之前测试并验证它们。
  - **命名空间处理**：XML 命名空间可能会使 XPath 查询复杂化。使用 local-name() 和 namespace-uri() 函数来处理命名空间或在 XPath 引擎中注册命名空间前缀。
  - **跨浏览器兼容性**：不同的浏览器对 XPath 的解释可能略有不同。通过跨浏览器测试 XPath 并使用 [Selenium](../S/selenium.md) 等工具来消除一些差异，确保跨浏览器兼容性。
  - **学习曲线**：XPath 的灵活性和强大功能也伴随着复杂性。投入时间学习和实践。使用 XPath 帮助器扩展等工具来构建和测试查询。

#### 如何使用 XPath Query 从 HTML 中提取数据？

[XPath Query](../X/xpath-query.md) 可用于通过定位 HTML DOM 结构中的特定元素、属性或文本来**从 HTML 中提取数据**。由于 HTML 在结构上与 XML 类似，因此可以有效地应用 XPath 来遍历 HTML 树并选择感兴趣的节点。
  提取数据：

1. **识别HTML元素**
    包含所需的数据。

2. **构造XPath表达式**
    在 DOM 中唯一定位该元素。

3. **执行[XPath query](../X/xpath-query.md)**
    使用支持 XPath 的工具或库，例如 Python 中的 Selenium 或 lxml。
  例如，要从具有特定 `id` 的段落中提取文本，您可以使用：

  ```
  //p[@id='unique-paragraph-id']/text()
  ```要检索属性值，例如来自锚标记的 `href`：

  ```
  //a[@class='link-class']/@href
  ```在 [test automation](../T/test-automation.md) 框架（如 [Selenium](../S/selenium.md)）中，您可以将这些 XPath 表达式与 `find_element_by_xpath()` 等方法一起使用来与 Web 元素进行交互：

  ```
  WebElement element = driver.findElement(By.xpath("//p[@id='unique-paragraph-id']"));
  String text = element.getText();
  ```**记住**要确保您的 XPath 查询精确且高效，以避免性能问题并明确定位元素。使用相对路径和谓词来缩小选择范围并避免过于复杂的表达式，因为表达式可能脆弱且难以维护。

1. **识别HTML元素**
    包含所需的数据。

2. **构造XPath表达式**
    在 DOM 中唯一定位该元素。

3. **执行[XPath query](../X/xpath-query.md)**
    使用支持 XPath 的工具或库，例如 Python 中的 Selenium 或 lxml。

### 高级概念

#### 有哪些高级 XPath 函数以及如何使用它们？

XPath 提供了多种高级功能，可用于在 XML 和 HTML 文档中执行复杂的查询和操作。以下是一些示例：

- **`normalize-space()`**：去除前导和尾随空白，并用单个空格替换空白字符序列。对于清理文本节点很有用。

    ```
    //div[normalize-space(text()) = 'Some text']
    ```

- **`contains()`**：检查第一个参数字符串是否包含第二个参数字符串。

    ```
    //div[contains(@class, 'partial-class-name')]
    ```

- **`starts-with()`**：确定第一个参数字符串是否以第二个参数字符串开头。

    ```
    //div[starts-with(@id, 'prefix')]
    ```

- **`substring()`**：返回给定字符串的一部分，从指定位置开始。

    ```
    //div[substring(@id, 1, 4) = 'item']
    ```

- **`string-length()`**：返回给定字符串的长度。

    ```
    //div[string-length(text()) > 10]
    ```

- **`sum()`**：计算数字序列的总和。

    ```
    sum(//input[@type='number']/@value)
    ```

- **`floor()`**、**`ceiling()`** 和 **`round()`**：对数字执行数学舍入运算。

    ```
    //div[number() > floor(1.5)]
    ```

- **`translate()`**：将字符串中的字符替换为相应字符串中的字符。

    ```
    //div[translate(text(), 'abc', 'ABC') = 'ABCText']
    ```

- **`not()`**：返回参数的布尔否定。

    ```
    //input[not(@disabled)]
    ```这些函数增强了直接在 XPath 查询中执行文本操作、字符串比较和数学计算的能力，使其成为[test automation](../T/test-automation.md) 工程师的强大工具。

- **`normalize-space()`**：去除前导和尾随空白，并用单个空格替换空白字符序列。对于清理文本节点很有用。

    ```
    //div[normalize-space(text()) = 'Some text']
    ```

- **`contains()`**：检查第一个参数字符串是否包含第二个参数字符串。

    ```
    //div[contains(@class, 'partial-class-name')]
    ```

- **`starts-with()`**：确定第一个参数字符串是否以第二个参数字符串开头。

    ```
    //div[starts-with(@id, 'prefix')]
    ```

- **`substring()`**：返回给定字符串的一部分，从指定位置开始。

    ```
    //div[substring(@id, 1, 4) = 'item']
    ```

- **`string-length()`**：返回给定字符串的长度。

    ```
    //div[string-length(text()) > 10]
    ```

- **`sum()`**：计算数字序列的总和。

    ```
    sum(//input[@type='number']/@value)
    ```

- **`floor()`**、**`ceiling()`** 和 **`round()`**：对数字执行数学舍入运算。

    ```
    //div[number() > floor(1.5)]
    ```

- **`translate()`**：将字符串中的字符替换为相应字符串中的字符。

    ```
    //div[translate(text(), 'abc', 'ABC') = 'ABCText']
    ```

- **`not()`**：返回参数的布尔否定。

    ```
    //input[not(@disabled)]
    ```

#### XPath 查询如何与 XML 中的命名空间一起使用？

在处理使用命名空间的 XML 文档时，必须调整 XPath 查询以正确引用这些命名空间内的元素。为此，您必须注册命名空间并在编写 XPath 表达式时使用前缀。
  以下是有关如何处理 XPath 查询中的名称空间的简要指南：

1. **注册命名空间**：在执行[XPath query](../X/xpath-query.md)之前，使用XML解析库提供的[API](../A/api.md)以前缀注册命名空间。例如，在 Java 的 XPath [API](../A/api.md) 中，您可以使用 `NamespaceContext` 将前缀映射到名称空间 URI。
  2. **在 [XPath query](../X/xpath-query.md) 中使用前缀**：注册后，请在 XPath 表达式中使用前缀来引用命名空间中的元素。

  ```
  <!-- Example XML with namespaces -->
  <root xmlns:ns="http://example.com/ns">
    <ns:child>Content</ns:child>
  </root>
  ```

  ```
  // Example of registering a namespace in Java
  XPath xpath = XPathFactory.newInstance().newXPath();
  xpath.setNamespaceContext(new NamespaceContextMap("ns", "http://example.com/ns"));
  ```

1. **编写 XPath 表达式** ：注册命名空间后，您现在可以使用前缀编写 XPath 表达式。

  ```
  // Example of an XPath query with a namespace prefix
  String expression = "/root/ns:child";
  Node childNode = (Node) xpath.evaluate(expression, document, XPathConstants.NODE);
  ```请记住，前缀的选择是任意的，不必与 XML 文档中使用的前缀相匹配；它只需要在您的 [XPath query](../X/xpath-query.md) 和命名空间注册中保持一致。

1. **注册命名空间**：在执行[XPath query](../X/xpath-query.md)之前，使用XML解析库提供的[API](../A/api.md)以前缀注册命名空间。例如，在 Java 的 XPath [API](../A/api.md) 中，您可以使用 `NamespaceContext` 将前缀映射到名称空间 URI。
  2. **在 [XPath query](../X/xpath-query.md) 中使用前缀**：注册后，请在 XPath 表达式中使用前缀来引用命名空间中的元素。
  1. **编写 XPath 表达式** ：注册命名空间后，您现在可以使用前缀编写 XPath 表达式。

#### 什么是 XPath 注入以及如何防止它？

XPath 注入是一种攻击形式，针对从用户提供的输入构建 XPath 查询的 Web 应用程序。攻击者操纵这些查询以获得对数据的未经授权的访问或绕过身份验证。
  **预防**涉及验证和清理输入、使用参数化查询以及采用最小权限方法：

- **输入验证**：使用正则表达式或验证库确保输入符合预期格式。
  - **清理输入**：在将潜在危险字符包含在 XPath 查询中之前删除或编码它们。
  - **参数化查询**：使用支持参数化的[APIs](../A/api.md)，它将查询结构与输入值分开。

    ```
    // Example using a safe parameterized API
    XPathExpression expr = xpath.compile("/users/user[@name=$username]");
    expr.setParameter("username", userInput);
    ```

- **最小权限**：将 XML 数据访问权限限制为应用程序功能所需的最低限度。
  - **安全库**：利用提供安全方法的库来创建 XPath 查询。
  - **错误处理**：实现安全的错误处理，即使检测到 XPath 注入尝试，也不会暴露敏感信息。
  通过结合这些策略，您可以显着降低软件 [test automation](../T/test-automation.md) 中 XPath 注入漏洞的风险。

- **输入验证**：使用正则表达式或验证库确保输入符合预期格式。
  - **清理输入**：在将潜在危险字符包含在 XPath 查询中之前删除或编码它们。
  - **参数化查询**：使用支持参数化的[APIs](../A/api.md)，它将查询结构与输入值分开。

    ```
    // Example using a safe parameterized API
    XPathExpression expr = xpath.compile("/users/user[@name=$username]");
    expr.setParameter("username", userInput);
    ```

- **最小权限**：将 XML 数据访问权限限制为应用程序功能所需的最低限度。
  - **安全库**：利用提供安全方法的库来创建 XPath 查询。
  - **错误处理**：实现安全的错误处理，即使检测到 XPath 注入尝试，也不会暴露敏感信息。

#### 编写高效 XPath 查询的最佳实践有哪些？

要编写高效的 XPath 查询，请遵循以下最佳实践：

- **使用特定路径**：更喜欢使用直接路径而不是搜索整个文档的`//`。例如，使用 `/html/body/div` 而不是 `//div`。
  - **利用 ID 和类**：如果可用，请使用 `@id` 和 `@class` 属性，因为它们通常是唯一的，可以使您的 XPath 更加高效。例如，`//*[@id='submit-button']`。
  - **避免使用索引**：`/div[2]` 等索引会使您的 XPath 变得脆弱。相反，找到一个独特的属性或路径。
  - **尽量减少通配符的使用`*`**：通配符匹配任何元素时都会减慢查询速度。尽可能具体。
  - **明智地使用 contains()**：`contains()` 函数很有用，但可能会被过度使用。当属性值是动态时使用它，例如`contains(@class, 'partial-class-name')`。
  - **当唯一时选择 text()**：如果文本是唯一的，则使用它来标识元素，例如`//a[text()='Click here']`。
  - **保持可读**：虽然效率是关键，但请确保您的 XPath 仍然可读以用于维护目的。
  - **使用starts-with()或ends-with()**：如果您的动态内容具有一致的开始或结束，请使用这些函数以获得更好的匹配。
  - **如果重用则缓存结果**：如果您在循环或重复中使用相同的 XPath，请将结果存储在变量中。
  - **测试您的 XPath**：在自动化脚本中实现 XPath 之前，使用浏览器开发人员工具等工具来测试 XPath 的效率和正确性。
  下面是一个结构良好的 XPath 的示例：

  ```
  /html/body//div[@class='content-wrapper']//button[@id='submit-button']
  ```该查询是直接的，使用特定的属性，并避免不必要的通配符和索引。

- **使用特定路径**：更喜欢使用直接路径而不是搜索整个文档的`//`。例如，使用 `/html/body/div` 而不是 `//div`。
  - **利用 ID 和类**：如果可用，请使用 `@id` 和 `@class` 属性，因为它们通常是唯一的，可以使您的 XPath 更加高效。例如，`//*[@id='submit-button']`。
  - **避免使用索引**：`/div[2]` 等索引会使您的 XPath 变得脆弱。相反，找到一个独特的属性或路径。
  - **尽量减少通配符的使用`*`**：通配符匹配任何元素时都会减慢查询速度。尽可能具体。
  - **明智地使用 contains()**：`contains()` 函数很有用，但可能会被过度使用。当属性值是动态时使用它，例如`contains(@class, 'partial-class-name')`。
  - **当唯一时选择 text()**：如果文本是唯一的，则使用它来标识元素，例如`//a[text()='Click here']`。
  - **保持可读**：虽然效率是关键，但请确保您的 XPath 仍然可读以用于维护目的。
  - **使用starts-with()或ends-with()**：如果您的动态内容具有一致的开始或结束，请使用这些函数以获得更好的匹配。
  - **如果重用则缓存结果**：如果您在循环或重复中使用相同的 XPath，请将结果存储在变量中。
  - **测试您的 XPath**：在自动化脚本中实现 XPath 之前，使用浏览器开发人员工具等工具来测试 XPath 的效率和正确性。

#### XPath Query 如何与 SQL 等其他查询语言结合使用？

在处理[databases](../D/database.md) 中支持XML 查询和操作的XML 数据类型时，[XPath Query](../X/xpath-query.md) 可以与[SQL](../S/sql.md) 集成。此集成允许提取和操作存储在 [SQL](../S/sql.md) [databases](../D/database.md) 中的 XML 数据。
  例如，在 Microsoft [SQL](../S/sql.md) Server 中，您可以使用 `nodes()` 方法将 XML 数据分解为关系行和列，然后将 XPath 表达式应用于目标特定元素或属性。以下是如何将 XPath 与 [SQL](../S/sql.md) 结合起来的示例：

  ```
  SELECT
      Tbl.Col.query('XPath_Expression') as Result
  FROM
      YourTable as Tbl
  CROSS APPLY
      Tbl.XmlColumn.nodes('XPath_Node_Selection') as T(XCol)
  ```在此[SQL](../S/sql.md) 查询中，`XPath_Expression` 是您放置[XPath query](../X/xpath-query.md) 来过滤或选择特定XML 数据的位置，`XPath_Node_Selection` 是用于标识将表示为行的节点的XPath 表达式。
  通过在 [SQL](../S/sql.md) 查询中利用 XPath，您可以执行涉及关系数据结构和分层数据结构的复杂查询，为需要与传统 [SQL](../S/sql.md) 查询结合查询 XML 数据的场景提供强大的工具。这在 XML 数据存储在 [SQL](../S/sql.md) [databases](../D/database.md) 中的报告、数据迁移或集成任务等场景中特别有用。
