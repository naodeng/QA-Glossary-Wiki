# 本地化测试

<!-- TOC START -->
- [相关术语：](#相关术语：)
- [有关本地化测试的问题吗？](#有关本地化测试的问题吗？)
  - [基础知识和重要性](#基础知识和重要性)
    - [软件测试中什么是本地化测试？](#软件测试中什么是本地化测试？)
    - [为什么本地化测试很重要？](#为什么本地化测试很重要？)
    - [本地化测试需要考虑哪些关键要素？](#本地化测试需要考虑哪些关键要素？)
    - [本地化测试如何改善整体用户体验？](#本地化测试如何改善整体用户体验？)
    - [不进行本地化测试的潜在后果是什么？](#不进行本地化测试的潜在后果是什么？)
  - [流程和技术](#流程和技术)
    - [本地化测试涉及哪些步骤？](#本地化测试涉及哪些步骤？)
    - [本地化测试中常用哪些技术？](#本地化测试中常用哪些技术？)
    - [本地化测试与其他类型的软件测试有何不同？](#本地化测试与其他类型的软件测试有何不同？)
    - [如何确保本地化测试的彻底性？](#如何确保本地化测试的彻底性？)
    - [本地化测试常用哪些工具？](#本地化测试常用哪些工具？)
  - [挑战和解决方案](#挑战和解决方案)
    - [本地化测试中遇到哪些常见挑战？](#本地化测试中遇到哪些常见挑战？)
    - [如何减轻或克服这些挑战？](#如何减轻或克服这些挑战？)
    - [本地化测试的最佳实践有哪些？](#本地化测试的最佳实践有哪些？)
    - [自动化如何应用于本地化测试？](#自动化如何应用于本地化测试？)
    - [您如何处理从右向左阅读的语言（如阿拉伯语和希伯来语）的本地化测试？](#您如何处理从右向左阅读的语言（如阿拉伯语和希伯来语）的本地化测试？)
  - [实际应用](#实际应用)
    - [您能提供成功的本地化测试示例吗？](#您能提供成功的本地化测试示例吗？)
    - [糟糕的本地化测试会带来哪些现实后果？](#糟糕的本地化测试会带来哪些现实后果？)
    - [本地化测试如何应用于移动应用程序？](#本地化测试如何应用于移动应用程序？)
    - [本地化测试如何应用于 Web 应用程序？](#本地化测试如何应用于-web-应用程序？)
    - [本地化测试如何应用于桌面应用程序？](#本地化测试如何应用于桌面应用程序？)
<!-- TOC END -->

本地化测试

确保软件产品在特定地区的用户中产生文化共鸣，保证其在该地区的可用性。

## 相关术语：

- [Internationalization Testing](../I/internationalization-testing.md)

## 有关本地化测试的问题吗？

### 基础知识和重要性

#### 软件测试中什么是本地化测试？

[Localization testing](../L/localization-testing.md) 是一个确保软件应用程序适合特定区域或语言的过程，不仅验证文本翻译，还验证文化差异、货币、日期格式和其他特定区域元素的适应性。它是全球化测试的一个子集，一次专注于一个特定的区域设置。
  要有效地执行[localization testing](../L/localization-testing.md)，请考虑目标区域设置中应用程序使用的**上下文**。这包括语言准确性、文化适宜性以及与当地标准的技术一致性。 **伪本地化** 可以作为模拟翻译和检测 UI 布局或字符编码潜在问题的初步步骤。
  [localization testing](../L/localization-testing.md) 中的自动化可以使用支持国际化库和特定于语言环境的数据集的工具来实现。可以设计脚本来切换区域设置并相应地验证应用程序的行为。例如：

  ```
  // Pseudo-code for automated localization test
  switchLocale('fr-FR');
  verifyTextTranslation('welcome_message', 'Bienvenue');
  verifyDateFormat('date_field', 'dd/mm/yyyy');
  verifyCurrencyFormat('price', '€');
  ```将 **区域特定的 [test cases](../T/test-case.md)** 纳入您的自动化套件中，以确保覆盖不同的语言和地区。定期更新这些案例以反映应用程序和目标区域设置的变化。
  请记住，[localization testing](../L/localization-testing.md) 不仅仅涉及翻译，还涉及确保应用程序引起当地受众的共鸣并遵守他们的期望和标准。这是向全球用户提供本土化产品的关键一步。

#### 为什么本地化测试很重要？

[Localization testing](../L/localization-testing.md) 对于确保软件产品**适当地适应**特定目标市场、考虑语言、文化规范和其他区域细节至关重要。它有助于识别**特定于区域设置的问题**，例如内容截断、不正确的日期和时间格式、货币问题等，否则可能会导致**误解**或**用户沮丧**。
  通过执行[localization testing](../L/localization-testing.md)，您可以确保产品**满足本地用户的期望**，这对于**全球市场的成功**至关重要。它不仅涉及翻译[verification](../V/verification.md)，还涉及检查**文化适当性**、**法律要求**和**当地标准合规性**。
  忽视[localization testing](../L/localization-testing.md)可能会导致**用户疏远**、**品牌损害**以及潜在的**法律后果**。对于旨在**跨国存在**的产品来说，这是质量保证流程中的关键步骤。
  为了确保彻底性，结合**自动化和[manual testing](../M/manual-testing.md)工作**，使用**[localization testing](../L/localization-testing.md)工具**，并让**母语人士**参与语言和文化见解。自动化对于重复性任务特别有用，例如跨不同区域检查 UI 元素，但 [manual testing](../M/manual-testing.md) 对于理解文化相关性的**细微差别**至关重要。
  对于从右向左阅读的语言，需要特别注意**UI布局**、**文本对齐**和**输入字段方向性**。通过使用**模拟器**、**众包测试**和**特定于脚本的测试工具**可以缓解**对母语人士的访问受限**或**复杂的脚本处理**等挑战。
  纳入最佳实践，例如**本地化团队的早期参与**、**持续本地化**以及翻译记忆库的**定期更新**。成功的[localization testing](../L/localization-testing.md)通常涉及**协作方法**，利用本地用户的**反馈循环**来迭代地完善产品。

#### 本地化测试需要考虑哪些关键要素？

在考虑 **[localization testing](../L/localization-testing.md)** 中的关键元素时，请重点关注：

- **文化适宜性**：确保内容在文化上可接受并且对当地习俗和传统敏感。
  - **本地格式**：验证日期、货币、电话号码和地址的格式。
  - **UI 布局**：检查布局和对齐是否正确，特别是当文本因翻译而扩展或收缩时。
  - **语言一致性**：验证整个应用程序中术语和风格的使用是否一致。
  - **法律要求**：确认遵守当地法律和法规，包括数据保护和隐私。
  - **性能**：评估本地化是否影响性能，特别是在添加语言包或不同字符集的情况下。
  - **资源文件**：将文本与代码分开，以方便翻译并确保资源文件正常工作。
  - **文本方向**：对于从右向左阅读的语言，确保文本正确排列并且 UI 元素相应调整。
  - **输入法**：测试与本地输入法的兼容性，例如虚拟键盘或 IME。
  - **字符集和编码**：确认对本地字符集的支持和正确的编码以防止字符损坏。
  - **内容本地化**：除了翻译之外，还要确保图像、符号和颜色适当并传达正确的含义。
  - **回退机制**：实现当本地数据丢失或不正确时优雅回退到默认语言或格式的机制。
  - **自动化[Test Cases](../T/test-case.md)** ：开发可以轻松适应不同区域设置的自动化测试，重点关注上述元素。
  通过解决这些要素，您可以提高软件在不同市场的质量和相关性。

- **文化适宜性**：确保内容在文化上可接受并且对当地习俗和传统敏感。
  - **本地格式**：验证日期、货币、电话号码和地址的格式。
  - **UI 布局**：检查布局和对齐是否正确，特别是当文本因翻译而扩展或收缩时。
  - **语言一致性**：验证整个应用程序中术语和风格的使用是否一致。
  - **法律要求**：确认遵守当地法律和法规，包括数据保护和隐私。
  - **性能**：评估本地化是否影响性能，特别是在添加语言包或不同字符集的情况下。
  - **资源文件**：将文本与代码分开，以方便翻译并确保资源文件正常工作。
  - **文本方向**：对于从右向左阅读的语言，确保文本正确排列并且 UI 元素相应调整。
  - **输入法**：测试与本地输入法的兼容性，例如虚拟键盘或 IME。
  - **字符集和编码**：确认对本地字符集的支持和正确的编码以防止字符损坏。
  - **内容本地化**：除了翻译之外，还要确保图像、符号和颜色适当并传达正确的含义。
  - **回退机制**：实现当本地数据丢失或不正确时优雅回退到默认语言或格式的机制。
  - **自动化[Test Cases](../T/test-case.md)** ：开发可以轻松适应不同区域设置的自动化测试，重点关注上述元素。

#### 本地化测试如何改善整体用户体验？

[Localization testing](../L/localization-testing.md) 通过确保软件感觉是为来自不同地区的用户**原生设计**，从而增强整体用户体验。它不仅仅是翻译，还解决文化差异、日期、货币和地址的本地格式以及遵守当地法规。这种对细节的关注使用户在使用产品时更加舒适和自信，从而提高**满意度**和**参与度**。
  当产品本地化良好时，它可以最大限度地减少用户因误解信息而可能产生的困惑和错误。它还表现出对用户的语言和文化的尊重，这可以培养对品牌的**忠诚度**和**信任**。此外，本地化可以开辟新市场并增加产品的潜在**用户群**。
  相反，缺乏适当的本地化可能会导致**令人沮丧的用户体验**，可能疏远用户并导致他们寻求替代方案。它还可能产生严重的影响，例如，如果不遵守当地法律，就会出现法律问题，或者由于货币处理不当而造成经济损失。
  总体而言，[localization testing](../L/localization-testing.md) 是交付一款能够与全球用户产生共鸣的精美产品的关键组成部分，确保该软件不仅能够在不同的地区正常运行，而且让使用它的人**感觉良好**。

#### 不进行本地化测试的潜在后果是什么？

忽视[localization testing](../L/localization-testing.md)可能会导致多种不良后果：

- **用户疏远**：如果应用程序不迎合当地语言和文化差异，用户可能会感到脱节，并且不太可能与该产品互动。
  - **功能问题**：由于日期、货币或地址等区域特定格式，功能可能会出现故障，从而导致令人沮丧的用户体验。
  - **法律影响**：不遵守当地法规和标准可能会导致法律挑战和罚款。
  - **品牌受损**：糟糕的本地化可能会损害品牌的声誉，使其看起来粗心或不尊重文化差异。
  - **竞争劣势**：与那些投资于更定制的用户体验的竞争对手相比，未能正确本地化可能会使产品处于劣势。
  - **收入损失**：如果用户无法正确使用产品或遇到阻碍交易的特定于区域设置的错误，则可能会损失潜在的销售额。
  - **支持成本增加**：用户因本地化问题而苦苦挣扎，可能会提出更多的支持请求，从而导致运营成本增加。
  - **延迟发布**：未识别的本地化问题可能会导致产品发布延迟，因为它们可能需要在开发周期后期进行大量返工。
  总之，缺乏彻底的[localization testing](../L/localization-testing.md) 可能会严重影响软件产品的成功和全球影响力。

- **用户疏远**：如果应用程序不迎合当地语言和文化差异，用户可能会感到脱节，并且不太可能与该产品互动。
  - **功能问题**：由于日期、货币或地址等区域特定格式，功能可能会出现故障，从而导致令人沮丧的用户体验。
  - **法律影响**：不遵守当地法规和标准可能会导致法律挑战和罚款。
  - **品牌受损**：糟糕的本地化可能会损害品牌的声誉，使其看起来粗心或不尊重文化差异。
  - **竞争劣势**：与那些投资于更定制的用户体验的竞争对手相比，未能正确本地化可能会使产品处于劣势。
  - **收入损失**：如果用户无法正确使用产品或遇到阻碍交易的特定于区域设置的错误，则可能会损失潜在的销售额。
  - **支持成本增加**：用户因本地化问题而苦苦挣扎，可能会提出更多的支持请求，从而导致运营成本增加。
  - **延迟发布**：未识别的本地化问题可能会导致产品发布延迟，因为它们可能需要在开发周期后期进行大量返工。

### 流程和技术

#### 本地化测试涉及哪些步骤？

[Localization testing](../L/localization-testing.md) 涉及多个步骤，以确保软件在不同区域设置中按预期运行。这是一个简洁的细分：

1. **准备**：定义本地化范围，包括语言和区域。收集所有必要的资源，例如本地化字符串、区域数据格式和文化差异。
  2. **伪本地化**：实施伪本地化以在应用实际翻译之前检测 UI 布局和字符编码的潜在问题。
  3. **翻译**：将翻译集成到应用程序中。确保所有 UI 元素、文档和帮助文件均已翻译。
  4. **[Functional Testing](../F/functional-testing.md)**：验证应用程序在每个区域设置中是否正常运行。这包括输入字段验证、排序、搜索以及可能因地区而异的其他功能。
  5. **UI 和布局测试**：检查 UI 是否可以容纳翻译后的文本而不会截断或重叠，并且布局更改（如果有）是否适合目标区域设置。
  6. **文化正确性**：评估内容、符号、颜色和图像的文化适当性，以避免冒犯用户。
  7. **[Compatibility Testing](../C/compatibility-testing.md)**：确保应用程序与本地化操作系统、浏览器和设备兼容。
  8. **[Performance Testing](../P/performance-testing.md)**：评估应用程序的性能，考虑处理多个区域设置的额外负载。
  9. **[Regression Testing](../R/regression-testing.md)**：进行回归测试以确认新的更新或修复没有引入新的本地化问题。
  10. **审查和反馈**：收集母语人士的反馈并解决发现的任何语言或文化问题。
  11. **最终[Verification](../V/verification.md)**：执行最后一轮测试，以确保所有问题均已解决，并且应用程序已准备好在目标市场发布。
  1. **准备**：定义本地化范围，包括语言和区域。收集所有必要的资源，例如本地化字符串、区域数据格式和文化差异。
  2. **伪本地化**：实施伪本地化以在应用实际翻译之前检测 UI 布局和字符编码的潜在问题。
  3. **翻译**：将翻译集成到应用程序中。确保所有 UI 元素、文档和帮助文件均已翻译。
  4. **[Functional Testing](../F/functional-testing.md)**：验证应用程序在每个区域设置中是否正常运行。这包括输入字段验证、排序、搜索以及可能因地区而异的其他功能。
  5. **UI 和布局测试**：检查 UI 是否可以容纳翻译后的文本而不会截断或重叠，并且布局更改（如果有）是否适合目标区域设置。
  6. **文化正确性**：评估内容、符号、颜色和图像的文化适当性，以避免冒犯用户。
  7. **[Compatibility Testing](../C/compatibility-testing.md)**：确保应用程序与本地化操作系统、浏览器和设备兼容。
  8. **[Performance Testing](../P/performance-testing.md)**：评估应用程序的性能，考虑处理多个区域设置的额外负载。
  9. **[Regression Testing](../R/regression-testing.md)**：进行回归测试以确认新的更新或修复没有引入新的本地化问题。
  10. **审查和反馈**：收集母语人士的反馈并解决发现的任何语言或文化问题。
  11. **最终[Verification](../V/verification.md)**：执行最后一轮测试，以确保所有问题均已解决，并且应用程序已准备好在目标市场发布。

#### 本地化测试中常用哪些技术？

**[localization testing](../L/localization-testing.md)** 中的常用技术包括：

- **伪本地化**：通过用重音版本或其他字母替换原始语言中的字符来模拟本地化内容，以识别字符编码、布局和 UI 元素的潜在问题，而无需实际翻译。
  - **语言测试**：让母语人士审查应用程序，以确保内容的准确性、上下文和文化适当性。
  - **外观测试**：专注于 UI 元素，以确保文本适合按钮、标签和字段，并且不会发生截断或重叠。
  - **[Functional Testing](../F/functional-testing.md)**：验证应用程序在本地化版本中是否正常运行，包括特定于区域设置的输入方法、排序和数据格式。
  - **合规性测试**：确保软件符合当地法律和文化规范，包括内容法规、数据隐私法和交易要求。
  - **自动化脚本国际化**：脚本旨在处理多种语言和区域设置，通常使用外部数据文件进行输入，以便在不同的 [test cases](../T/test-case.md) 之间轻松切换。
  - **区域特定的[Test Cases](../T/test-case.md)**：[Test cases](../T/test-case.md) 是为解决区域设置特定的场景而定制的，例如日期和时间格式、货币和地址结构。
  - **持续本地化**：将本地化集成到持续开发和测试周期中，允许在添加新内容时进行持续测试和更新。
  这些技术通常结合起来创建一个全面的[localization testing](../L/localization-testing.md)策略，以确保该软件受到不同地区用户的好评。

- **伪本地化**：通过用重音版本或其他字母替换原始语言中的字符来模拟本地化内容，以识别字符编码、布局和 UI 元素的潜在问题，而无需实际翻译。
  - **语言测试**：让母语人士审查应用程序，以确保内容的准确性、上下文和文化适当性。
  - **外观测试**：专注于 UI 元素，以确保文本适合按钮、标签和字段，并且不会发生截断或重叠。
  - **[Functional Testing](../F/functional-testing.md)**：验证应用程序在本地化版本中是否正常运行，包括特定于区域设置的输入方法、排序和数据格式。
  - **合规性测试**：确保软件符合当地法律和文化规范，包括内容法规、数据隐私法和交易要求。
  - **自动化脚本国际化**：脚本旨在处理多种语言和区域设置，通常使用外部数据文件进行输入，以便在不同的 [test cases](../T/test-case.md) 之间轻松切换。
  - **区域特定的[Test Cases](../T/test-case.md)**：[Test cases](../T/test-case.md) 是为解决区域设置特定的场景而定制的，例如日期和时间格式、货币和地址结构。
  - **持续本地化**：将本地化集成到持续开发和测试周期中，允许在添加新内容时进行持续测试和更新。

#### 本地化测试与其他类型的软件测试有何不同？

[Localization testing](../L/localization-testing.md) 与其他类型的[software testing](../S/software-testing.md) 的不同之处在于它**特别关注不同目标市场的文化和语言准确性**。与[functional testing](../F/functional-testing.md)（确保软件正确运行）或[performance testing](../P/performance-testing.md)（衡量软件在各种条件下的响应能力和稳定性）不同，[localization testing](../L/localization-testing.md) 验证软件是否适合不同地理区域的用户。
  此类测试不仅涉及检查文本翻译，还涉及**日期、货币和数值的格式**，以及确保图像、颜色和内容在文化上适当且不会造成冒犯。它还包括验证软件是否可以处理多种语言的输入和显示，特别是那些具有独特字符集或方向性的语言，例如中文或阿拉伯语。
  [Localization testing](../L/localization-testing.md) 的独特之处在于它需要**语言技能和技术理解的结合**。测试人员必须熟悉目标地区的当地文化和语言细微差别，以及所测试软件的技术方面。
  另一个区别是[localization testing](../L/localization-testing.md) 通常需要**额外的工具和技术**来管理多语言[test cases](../T/test-case.md) 和数据。例如，字符编码问题特定于[localization testing](../L/localization-testing.md)，并且需要可以处理不同文本编码的工具。
  总之，[localization testing](../L/localization-testing.md) 是一种专门的测试形式，可确保软件产品完全适应并可以在特定区域使用，而不仅仅是文本翻译，还涵盖该测试形式所特有的文化、功能和技术方面。

#### 如何确保本地化测试的彻底性？

为了确保 [localization testing](../L/localization-testing.md) 的彻底性，请考虑以下策略：

- **开发全面的[test plan](../T/test-plan.md)**，其中包括所有区域设置和特定于语言的场景。这不仅应涵盖文本翻译，还应涵盖文化差异、法律要求以及日期、货币和计量单位的特定地区格式。
  - **利用自动化**执行重复性任务，例如切换区域设置和捕获屏幕截图以进行视觉比较。使用参数化测试有效地覆盖多种语言。
  - **将 [localization testing](../L/localization-testing.md) 集成到您的 CI/CD 管道**以尽早且经常发现问题。作为常规测试过程的一部分，自动化测试应该针对本地化构建运行。
  - $

    ```
    ```// 伪代码中的参数化测试示例
  测试.each（语言环境=> {
  setLocale(区域设置);
  Expect(page.title).toBe(localizedTitleFor(locale));
  });

  ```
  - **Utilize pseudo-localization** to detect layout issues and ensure that your application can handle longer text strings that often occur in translation.
  - **Engage native speakers** for exploratory testing to uncover subtle language or cultural issues that automated tests may miss.
  - **Review and update test cases regularly** to reflect changes in the application and the addition of new locales.
  - **Monitor and analyze user feedback** from each locale to identify and address issues that were not caught during testing.
  - **Collaborate with translators and localization experts** to understand the context and ensure that translations are accurate and appropriate.
  By combining these strategies, you can achieve a high level of thoroughness in your localization testing efforts, ensuring a quality experience for all users, regardless of their language or region.
  ```

- **开发全面的[test plan](../T/test-plan.md)**，其中包括所有区域设置和特定于语言的场景。这不仅应涵盖文本翻译，还应涵盖文化差异、法律要求以及日期、货币和计量单位的特定地区格式。
  - **利用自动化**执行重复性任务，例如切换区域设置和捕获屏幕截图以进行视觉比较。使用参数化测试有效地覆盖多种语言。
  - **将 [localization testing](../L/localization-testing.md) 集成到您的 CI/CD 管道**以尽早且经常发现问题。作为常规测试过程的一部分，自动化测试应该针对本地化构建运行。
  - $

    ```
    ```

#### 本地化测试常用哪些工具？

[localization testing](../L/localization-testing.md) 中使用的常用工具包括：

- **伪本地化工具**：这些工具通过用重音字符或其他脚本替换原始语言中的字符来模拟翻译。示例包括 **PseudoLocalizer** 和 **AccChecker**。
  - **翻译管理系统 (TMS)**：**Crowdin**、**Transifex** 和 **Smartling** 等平台有助于管理和自动化翻译工作流程，包括测试。
  - **自动化视觉测试工具**：**Applitools** 和 **Percy** 等工具捕获本地化 UI 的屏幕截图，以检测文本溢出或错位等视觉问题。
  - **国际化 (i18n) 库**：特定于框架的库，例如用于 JavaScript 的 **i18next** 或 **.NET 的全球化和本地化**功能有助于管理动态内容本地化。
  - **特定于语言的测试框架**：某些框架提供对 [localization testing](../L/localization-testing.md) 的内置支持，例如带有 **ResourceBundle** 控制的 **JUnit** for Java。
  - **浏览器自动化工具**：**[Selenium](../S/selenium.md) [WebDriver](../W/webdriver.md)** 可用于自动导航不同语言版本的 Web 应用程序。
  - **移动测试平台**：**Appium** 和 **Xamarin.UITest** 支持本地化移动应用程序的自动化。
  - **操作系统模拟器**：适用于不同操作系统版本和区域设置的模拟器和模拟器有助于在各种环境中测试应用程序，而无需物理设备。
  - **自定义脚本**：使用 **Python** 或 **JavaScript** 等编程语言编写自定义脚本，以自动执行本地化内容的[verification](../V/verification.md)。
  这些工具通常集成到 CI/CD 管道中，以确保在整个开发生命周期中持续[localization testing](../L/localization-testing.md)。

- **伪本地化工具**：这些工具通过用重音字符或其他脚本替换原始语言中的字符来模拟翻译。示例包括 **PseudoLocalizer** 和 **AccChecker**。
  - **翻译管理系统 (TMS)**：**Crowdin**、**Transifex** 和 **Smartling** 等平台有助于管理和自动化翻译工作流程，包括测试。
  - **自动化视觉测试工具**：**Applitools** 和 **Percy** 等工具捕获本地化 UI 的屏幕截图，以检测文本溢出或错位等视觉问题。
  - **国际化 (i18n) 库**：特定于框架的库，例如用于 JavaScript 的 **i18next** 或 **.NET 的全球化和本地化**功能有助于管理动态内容本地化。
  - **特定于语言的测试框架**：某些框架提供对 [localization testing](../L/localization-testing.md) 的内置支持，例如带有 **ResourceBundle** 控制的 **JUnit** for Java。
  - **浏览器自动化工具**：**[Selenium](../S/selenium.md) [WebDriver](../W/webdriver.md)** 可用于自动导航不同语言版本的 Web 应用程序。
  - **移动测试平台**：**Appium** 和 **Xamarin.UITest** 支持本地化移动应用程序的自动化。
  - **操作系统模拟器**：适用于不同操作系统版本和区域设置的模拟器和模拟器有助于在各种环境中测试应用程序，而无需物理设备。
  - **自定义脚本**：使用 **Python** 或 **JavaScript** 等编程语言编写自定义脚本，以自动执行本地化内容的[verification](../V/verification.md)。

### 挑战和解决方案

#### 本地化测试中遇到哪些常见挑战？

[Localization testing](../L/localization-testing.md) 确保软件适用于特定区域或语言。常见的挑战包括：

- **文本扩展**：翻译后的文本可能更长或更短，影响 UI 布局并需要动态设计解决方案。
  - **字符编码**：确保正确的编码以支持特殊字符并防止显示问题。
  - **日期和时间格式**：日期、时间和时区处理的变化可能会导致功能错误或用户混乱。
  - **文化细微差别**：颜色、图标和图像可能带有不同的含义，需要仔细考虑以避免冒犯。
  - **法律要求**：不同地区有软件必须遵守的特定法律标准。
  - **付款和货币处理**：确保准确的货币换算并支持本地支付方式。
  - **输入法**：支持各种键盘布局和输入法，例如某些语言的从右到左（RTL）文本。
  - **资源文件**：管理和维护多组资源文件可能很复杂且容易出错。
  - **自动[test script](../T/test-script.md) 适应**：脚本可能需要进行重大调整才能处理本地化版本，包括定位器和验证点的更改。

  ```
  // Example of a potential issue in automated scripts:
  // A date field validation script may fail if it expects a specific format:
  assert(dateField.text === '03/25/2023'); // Fails for '25/03/2023'
  ```

- **性能**：本地化版本可能有不同的性能特征，需要有针对性的测试。
  - **第三方服务集成**：确保地图或天气等服务已本地化并正常运行。
  应对这些挑战需要结合**技术解决方案**、**文化理解**和**严格的测试**，以确保跨不同地区的无缝用户体验。

- **文本扩展**：翻译后的文本可能更长或更短，影响 UI 布局并需要动态设计解决方案。
  - **字符编码**：确保正确的编码以支持特殊字符并防止显示问题。
  - **日期和时间格式**：日期、时间和时区处理的变化可能会导致功能错误或用户混乱。
  - **文化细微差别**：颜色、图标和图像可能带有不同的含义，需要仔细考虑以避免冒犯。
  - **法律要求**：不同地区有软件必须遵守的特定法律标准。
  - **付款和货币处理**：确保准确的货币换算并支持本地支付方式。
  - **输入法**：支持各种键盘布局和输入法，例如某些语言的从右到左（RTL）文本。
  - **资源文件**：管理和维护多组资源文件可能很复杂且容易出错。
  - **自动[test script](../T/test-script.md) 适应**：脚本可能需要进行重大调整才能处理本地化版本，包括定位器和验证点的更改。
  - **性能**：本地化版本可能有不同的性能特征，需要有针对性的测试。
  - **第三方服务集成**：确保地图或天气等服务已本地化并正常运行。

#### 如何减轻或克服这些挑战？

缓解[localization testing](../L/localization-testing.md) 中的挑战涉及战略规划和资源的有效利用。以下是一些方法：

- **尽可能自动化**：使用自动化框架处理重复性任务，确保一致性并节省时间。例如，跨不同区域设置自动验证 UI 元素。

  ```
  // Example pseudocode for automated UI checks
  function verifyLocalizedUI(elementId, expectedText) {
    const element = getElementById(elementId);
    if (element.text !== expectedText) {
      throw new Error(`Text for ${elementId} does not match expected localized text.`);
    }
  }
  ```

- **利用本地化平台**：利用专门从事本地化管理的工具来简化流程并保持翻译一致性。
  - **优先级**：根据您的用户群和业务需求，专注于最关键的语言和功能。
  - **使用伪本地化**：使用占位符文本进行测试，以确保 UI 元素可以处理不同的语言和字符长度。
  - **让母语人士参与**：为了进行细致入微的语言检查，请让母语人士参与来验证文化相关性和正确性。
  - **持续集成**：将 [localization testing](../L/localization-testing.md) 集成到您的 CI/CD 管道中，以便尽早且经常发现问题。
  - **众包测试**：考虑众包测试平台以从不同的地区获得快速反馈。
  - **保持更新**：及时了解语言变化和区域趋势，以确保您的测试保持相关性。
  - **文档**：维护本地化要求和[test cases](../T/test-case.md)的清晰文档，以确保清晰度和可重复性。
  通过采用这些策略，您可以降低本地化问题的风险，并确保为所有目标市场提供高质量的用户体验。

- **尽可能自动化**：使用自动化框架处理重复性任务，确保一致性并节省时间。例如，跨不同区域设置自动验证 UI 元素。
  - **利用本地化平台**：利用专门从事本地化管理的工具来简化流程并保持翻译一致性。
  - **优先级**：根据您的用户群和业务需求，专注于最关键的语言和功能。
  - **使用伪本地化**：使用占位符文本进行测试，以确保 UI 元素可以处理不同的语言和字符长度。
  - **让母语人士参与**：为了进行细致入微的语言检查，请让母语人士参与来验证文化相关性和正确性。
  - **持续集成**：将 [localization testing](../L/localization-testing.md) 集成到您的 CI/CD 管道中，以便尽早且经常发现问题。
  - **众包测试**：考虑众包测试平台以从不同的地区获得快速反馈。
  - **保持更新**：及时了解语言变化和区域趋势，以确保您的测试保持相关性。
  - **文档**：维护本地化要求和[test cases](../T/test-case.md)的清晰文档，以确保清晰度和可重复性。

#### 本地化测试的最佳实践有哪些？

[localization testing](../L/localization-testing.md) 的最佳实践包括：

- **吸引母语人士**：确保母语人士审查应用程序，以捕捉自动化工具可能遗漏的细微差别。
  - **使用伪本地化**：使用伪本地化文本测试应用程序，以识别文本扩展、字符编码和布局的潜在问题。
  - $

    ```
    ```伪本地化（'你好，世界！'）； // 输出伪本地化字符串

  ```
  - **Automate where possible**: Create automated tests to verify locale-specific formats like dates, currencies, and numbers.
  - **Cultural sensitivity**: Be aware of cultural norms and taboos to avoid offensive content.
  - **Test on local infrastructure**: Run tests on servers and devices located in the target locale to account for local network conditions and services.
  - **Local regulations compliance**: Ensure the application complies with local laws and regulations, such as data privacy laws.
  - **Iterative testing**: Conduct localization testing throughout the development cycle to catch issues early.
  - **Visual inspection**: Manually inspect UI elements for truncation, overlapping, and alignment issues.
  - **Contextual testing**: Validate that the context is preserved in translation, not just the literal text.
  - **Fallback mechanisms**: Implement fallback options for missing translations or resources.
  - **Performance testing**: Check that localized versions do not negatively impact the application's performance.
  - **Accessibility**: Ensure that localized content is accessible, including support for screen readers and alternative input methods.
  By following these practices, you can enhance the quality of your localized software and provide a better experience for users across different regions and cultures.
  ```

- **吸引母语人士**：确保母语人士审查应用程序，以捕捉自动化工具可能遗漏的细微差别。
  - **使用伪本地化**：使用伪本地化文本测试应用程序，以识别文本扩展、字符编码和布局的潜在问题。
  - $

    ```
    ```

#### 自动化如何应用于本地化测试？

[localization testing](../L/localization-testing.md) 中的自动化可以显着简化跨不同语言和地区验证软件功能的过程。自动化测试可以设计为**验证 UI 元素**，例如按钮、菜单和对话框，确保文本正确显示，没有重叠或截断，并且针对目标受众进行了正确本地化。
  使用**参数化测试**，自动化框架可以迭代各种本地化数据集，检查每种支持语言的一致性和正确性。此方法允许重用[test cases](../T/test-case.md)，其中仅输入数据根据所测试的区域设置而更改。
  自动化脚本还可以用于动态地在不同的**区域设置**之间切换，从而使测试能够在一次运行中涵盖多种语言配置。这对于验证日期、时间和数字格式以及可能因区域设置而异的排序算法特别有用。
  **伪本地化**可以自动化，以确保软件可以处理不同长度的翻译字符串，并且对于非标准字符仍然有效。该技术涉及用更改后的版本替换原始文本，其中包括扩展字符和符号以模仿不同的语言。
  对于 **从右到左 (RTL)** 语言，自动化可以验证布局方向性和文本对齐方式，确保 UI 正确适应 RTL 脚本。
  为了处理[localization testing](../L/localization-testing.md)的复杂性，自动化工程师经常将**[localization testing](../L/localization-testing.md)工具**与其自动化框架集成。这些工具可以自动检测缺失的翻译、占位符的错误使用以及其他常见的本地化问题。
  通过自动执行重复且耗时的任务，[test automation](../T/test-automation.md) 使团队能够专注于更复杂的本地化挑战，最终确保为国际用户提供更高质量的产品。

#### 您如何处理从右向左阅读的语言（如阿拉伯语和希伯来语）的本地化测试？

由于独特的布局和文本方向，处理从右向左 (RTL) 阅读的语言（例如阿拉伯语和希伯来语）的 [localization testing](../L/localization-testing.md) 需要特别注意细节。以下是一些策略：

- **镜像 UI**：确保针对 RTL 语言正确镜像用户界面。这包括文本和元素的布局、导航和对齐。
  - **使用 Unicode** ：实现 Unicode 编码以支持 RTL 脚本和特殊字符。
  - **文本扩展**：考虑文本扩展，因为从英语到 RTL 语言的翻译可以将文本长度增加最多 30%。
  - **字体支持**：验证字体是否支持 RTL 字符并且它们是否正确呈现。
  - **输入字段**：测试输入字段以确保它们正确对齐并显示 RTL 文本。
  - **文化细微差别**：注意可能影响界面的文化细微差别，例如图标、颜色和图像。
  - **自动视觉测试**：使用支持视觉测试的工具自动检测布局问题。
  - **双向文本**：测试可能混合 RTL 和从左到右 (LTR) 文本的双向文本场景。
  - **自动化[Test Scripts](../T/test-script.md)** ：调整自动化测试脚本以适应 RTL 输入并相应地验证 UI。
  RTL 语言的 [test script](../T/test-script.md) 片段示例：

  ```
  describe('RTL Layout Test', () => {
    it('should display text fields with RTL text', () => {
      const inputField = getElementById('name-input');
      inputField.sendKeys('مثال');
      expect(inputField.getText()).toEqual('مثال');
    });
  });
  ```请记住**与母语人士进行验证**以确保本地化的准确性和适当性，并**在添加新功能或修改现有功能时定期更新您的[test cases](../T/test-case.md)**。

- **镜像 UI**：确保针对 RTL 语言正确镜像用户界面。这包括文本和元素的布局、导航和对齐。
  - **使用 Unicode** ：实现 Unicode 编码以支持 RTL 脚本和特殊字符。
  - **文本扩展**：考虑文本扩展，因为从英语到 RTL 语言的翻译可以将文本长度增加最多 30%。
  - **字体支持**：验证字体是否支持 RTL 字符并且它们是否正确呈现。
  - **输入字段**：测试输入字段以确保它们正确对齐并显示 RTL 文本。
  - **文化细微差别**：注意可能影响界面的文化细微差别，例如图标、颜色和图像。
  - **自动视觉测试**：使用支持视觉测试的工具自动检测布局问题。
  - **双向文本**：测试可能混合 RTL 和从左到右 (LTR) 文本的双向文本场景。
  - **自动化[Test Scripts](../T/test-script.md)** ：调整自动化测试脚本以适应 RTL 输入并相应地验证 UI。

### 实际应用

#### 您能提供成功的本地化测试示例吗？

成功的[localization testing](../L/localization-testing.md) 可确保软件在文化和语言上适合目标受众。以下是示例：
  **Netflix** 在本地化方面表现出色，为不同地区量身定制内容和字幕，导致全球订阅量大幅增长。
  **Microsoft Office** 套件提供了 [localization testing](../L/localization-testing.md) 的绝佳示例，其用户界面、帮助内容和模板适合不同语言和地区，保持了功能和用户体验的一致性。
  **Airbnb** 实施了广泛的本地化策略，包括货币、日期格式和本地内容，以增强用户体验，从而增加来自非英语国家的预订。
  **Pokémon Go** 通过纳入特定地区的 Pokémon 并将游戏翻译成多种语言，成功实现了游戏本地化，这有助于其在全球范围内的流行。
  **Uber** 通过集成本地地图、支付方式以及对从右到左语言的支持来本地化其应用程序，这对于其拓展新市场至关重要。
  要自动化[localization testing](../L/localization-testing.md)，请考虑使用以下工具：

  ```
  Selenium WebDriver for UI testing across different locales.
  ```

  ```
  Applanga for automating the translation update process.
  ```

  ```
  Pseudo-localization techniques to detect unlocalized strings.
  ```请记住，不仅要验证文本翻译，还要验证文化差异、法律要求和本地功能。

#### 糟糕的本地化测试会带来哪些现实后果？

糟糕的 [localization testing](../L/localization-testing.md) 可能会导致一些现实世界的后果：

- **用户不满意**：如果用户遇到翻译不佳或文化上不合适的内容，可能会导致沮丧和负面的用户体验。
  - **品牌损害**：本地化错误可能会损害品牌形象，使其显得粗心或不尊重特定市场或文化。
  - **法律影响**：不准确的本地化可能会导致不遵守当地法律和法规，并可能导致罚款或法律诉讼。
  - **市场份额减少**：未能正确本地化可能会使其难以与提供更量身定制的用户体验的本地产品竞争。
  - **支持成本增加**：由于本地化不佳而产生的误解可能会导致支持请求大量涌入，从而给客户服务资源带来压力。
  - **产品延迟**：在开发周期后期发现本地化问题可能会导致产品发布延迟，影响上市时间和潜在收入。
  有效的[localization testing](../L/localization-testing.md)对于避免这些后果并确保产品在不同地区和文化中受到好评至关重要。

- **用户不满意**：如果用户遇到翻译不佳或文化上不合适的内容，可能会导致沮丧和负面的用户体验。
  - **品牌损害**：本地化错误可能会损害品牌形象，使其显得粗心或不尊重特定市场或文化。
  - **法律影响**：不准确的本地化可能会导致不遵守当地法律和法规，并可能导致罚款或法律诉讼。
  - **市场份额减少**：未能正确本地化可能会使其难以与提供更量身定制的用户体验的本地产品竞争。
  - **支持成本增加**：由于本地化不佳而产生的误解可能会导致支持请求大量涌入，从而给客户服务资源带来压力。
  - **产品延迟**：在开发周期后期发现本地化问题可能会导致产品发布延迟，影响上市时间和潜在收入。

#### 本地化测试如何应用于移动应用程序？

移动应用程序的 [Localization testing](../L/localization-testing.md) 可确保应用程序在不同的区域设置中正常运行。这涉及验证**文本翻译**、**日期和时间格式**、**货币**以及其他特定于语言环境的元素。考虑到文本扩展或收缩可能会影响 UI 元素，它还会检查各种语言设置下的正确布局和功能。
  自动化本地化测试可以使用 Android 的 Appium 或 Espresso 以及 iOS 的 XCTest 等框架来实现。这些测试可以以编程方式切换设备区域设置并验证不同语言的 UI 元素。例如：

  ```
  Locale locale = new Locale("es", "ES");
  Locale.setDefault(locale);
  Configuration config = new Configuration();
  config.locale = locale;
  getInstrumentation().getContext().getResources().updateConfiguration(config, null);
  ```此代码片段将西班牙的区域设置设置为西班牙语，这可以是检查应用程序的西班牙语本地化的大型自动化测试的一部分。
  请记住在本地化测试中包含**辅助功能检查**，因为文本转语音和其他辅助技术必须与本地化内容正确配合。
  总之，移动应用的 [localization testing](../L/localization-testing.md) 旨在通过自动化本地化资源和 UI 元素的 [verification](../V/verification.md) 来确保所有用户（无论其语言或地区如何）获得无缝的用户体验。

#### 本地化测试如何应用于 Web 应用程序？

用于 Web 应用程序的 [Localization testing](../L/localization-testing.md) 确保应用程序的行为符合不同地理区域的用户的预期。这不仅涉及验证文本的翻译，还涉及验证日期、时间、货币和数值等数据的格式。此外，它还包括检查是否符合当地法规和文化差异。
  对于 Web 应用程序，[localization testing](../L/localization-testing.md) 至关重要，因为来自世界各地的不同用户群访问该应用程序。验证应用程序是否自动检测用户的区域设置或允许他们选择其首选语言和区域设置至关重要。
  在用于 Web 应用程序的 [test automation](../T/test-automation.md) 中，您可以利用 **[Selenium](../S/selenium.md) [WebDriver](../W/webdriver.md)** 或类似工具来模拟不同的区域设置。这可以通过更改浏览器设置或传递特定于区域设置的参数来完成。以下是使用 [WebDriver](../W/webdriver.md) 的 TypeScript 示例：

  ```
  const { Builder } = require('selenium-webdriver');
  let driver = new Builder()
      .forBrowser('firefox')
      .setFirefoxOptions(new firefox.Options().addArguments("--lang=es"))
      .build();
  ```此代码片段将浏览器语言设置为西班牙语，这对于测试 Web 应用程序的西班牙语本地化非常有用。
  自动化测试应涵盖**UI元素**、**内容**和**功能工作流程**，以确保它们正确适应本地化设置。如果适用，包括对从右到左 (RTL) 语言的检查至关重要，因为布局和导航可能会发生显着变化。
  通过将 [localization testing](../L/localization-testing.md) 合并到自动化套件中，您可以确保 Web 应用程序为所有用户提供无缝且与文化相关的体验，无论他们位于何处。

#### 本地化测试如何应用于桌面应用程序？

用于桌面应用程序的[Localization testing](../L/localization-testing.md) 可确保软件针对特定区域或语言进行正确调整。这不仅涉及验证文本的翻译，还涉及文化规范、货币格式、日期和时间格式以及其他特定于语言环境的元素的适当性。
  可以设计自动化测试来切换应用程序的区域设置并验证以下内容：

- **用户界面元素**
    正确翻译并适合其分配的空间。

- **输入字段**
    接受并处理特定于区域设置的数据格式。

- **功能**
    在不同的区域设置中保持一致。
  以下示例说明了如何使用伪代码在桌面应用程序中自动执行简单的区域设置更改和[verification](../V/verification.md)：

  ```
  function testLocalization(locale) {
    setApplicationLocale(locale);
    assertEqual(getWindowTitle(), expectedTitleForLocale);
    assertEqual(getDateInputFormat(), expectedDateFormatForLocale);
    // Additional assertions for other locale-specific elements
  }
  ```对于每个受支持的区域设置，您可以使用适当的参数调用`testLocalization`。这可确保应用程序按照不同地区的用户的预期运行。
  请记住，**自动化**是有效覆盖多种区域设置和语言组合的关键。然而，至关重要的是用 **[manual testing](../M/manual-testing.md)** 来补充自动化检查，以捕获自动化测试可能遗漏的上下文和文化适当性的细微差别。

- **用户界面元素**
    正确翻译并适合其分配的空间。

- **输入字段**
    接受并处理特定于区域设置的数据格式。

- **功能**
    在不同的区域设置中保持一致。
