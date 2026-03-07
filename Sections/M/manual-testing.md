# Manual Testing

<!-- TOC START -->
- [Related Terms:](#related-terms)
- [Questions about Manual Testing ?](#questions-about-manual-testing)
  - [Basics and Importance](#basics-and-importance)
    - [What is manual testing?](#what-is-manual-testing)
    - [Why is manual testing important?](#why-is-manual-testing-important)
    - [What are the key differences between manual testing and automated testing?](#what-are-the-key-differences-between-manual-testing-and-automated-testing)
    - [What are the advantages and disadvantages of manual testing?](#what-are-the-advantages-and-disadvantages-of-manual-testing)
    - [What are the key principles of manual testing?](#what-are-the-key-principles-of-manual-testing)
  - [Types of Manual Testing](#types-of-manual-testing)
    - [What are the different types of manual testing?](#what-are-the-different-types-of-manual-testing)
    - [What is black box testing?](#what-is-black-box-testing)
    - [What is white box testing?](#what-is-white-box-testing)
    - [What is grey box testing?](#what-is-grey-box-testing)
    - [What is the difference between functional and non-functional testing?](#what-is-the-difference-between-functional-and-non-functional-testing)
  - [Manual Testing Process](#manual-testing-process)
    - [What are the stages in the manual testing life cycle?](#what-are-the-stages-in-the-manual-testing-life-cycle)
    - [What is test planning and what does it involve?](#what-is-test-planning-and-what-does-it-involve)
    - [What is test case design and what are the key elements of a good test case?](#what-is-test-case-design-and-what-are-the-key-elements-of-a-good-test-case)
    - [What is test execution and what are the steps involved?](#what-is-test-execution-and-what-are-the-steps-involved)
    - [What is test closure and what does it involve?](#what-is-test-closure-and-what-does-it-involve)
  - [Manual Testing Tools](#manual-testing-tools)
    - [What tools are used in manual testing?](#what-tools-are-used-in-manual-testing)
    - [What is the role of a test management tool in manual testing?](#what-is-the-role-of-a-test-management-tool-in-manual-testing)
    - [What is the role of a defect tracking tool in manual testing?](#what-is-the-role-of-a-defect-tracking-tool-in-manual-testing)
    - [What are some examples of manual testing tools?](#what-are-some-examples-of-manual-testing-tools)
  - [Manual Testing Best Practices](#manual-testing-best-practices)
    - [What are some best practices for manual testing?](#what-are-some-best-practices-for-manual-testing)
    - [How can manual testing be made more effective?](#how-can-manual-testing-be-made-more-effective)
    - [What are some common mistakes to avoid in manual testing?](#what-are-some-common-mistakes-to-avoid-in-manual-testing)
<!-- TOC END -->

Manual testing

is the process of manually checking software functionalities against expected outcomes.

## Related Terms:

- [Automated Testing](https://naodeng.com.cn/en/wiki/automated-testing)
- [Test Automation](https://naodeng.com.cn/en/wiki/test-automation)

## Questions about Manual Testing ?

### Basics and Importance

#### What is manual testing?

  [Manual testing](https://naodeng.com.cn/en/wiki/manual-testing) is the process of manually executing [test cases](https://naodeng.com.cn/en/wiki/test-case) without the use of automation tools. Testers perform this type of testing by following a set of predefined [test cases](https://naodeng.com.cn/en/wiki/test-case) to ensure that the software behaves as expected. It involves the tester interacting with the application's interface, providing inputs, and observing the outputs to verify the correctness of the application's behavior.
  Since [manual testing](https://naodeng.com.cn/en/wiki/manual-testing) relies on human observation, it is particularly useful for detecting usability issues, understanding the user experience, and finding unexpected behavior that automated tests might miss. Testers use their intuition, experience, and understanding of the software to explore functionalities and report any discrepancies from the [expected results](https://naodeng.com.cn/en/wiki/expected-result).
  In [manual testing](https://naodeng.com.cn/en/wiki/manual-testing), the tester acts as an end user and verifies that all features of the application are working correctly. It is often used for [exploratory testing](https://naodeng.com.cn/en/wiki/exploratory-testing), ad-hoc testing, and [usability testing](https://naodeng.com.cn/en/wiki/usability-testing), where the tester's creativity and insights are crucial.
  Despite the rise of [automated testing](https://naodeng.com.cn/en/wiki/automated-testing), [manual testing](https://naodeng.com.cn/en/wiki/manual-testing) remains an integral part of the software development lifecycle, especially for scenarios that are difficult to automate or require human judgment. It allows for a more flexible and interactive approach to testing, which can be critical in the early stages of development and for tests that are not run frequently enough to warrant automation.

#### Why is manual testing important?

  [Manual testing](https://naodeng.com.cn/en/wiki/manual-testing) remains crucial despite the advancements in [test automation](https://naodeng.com.cn/en/wiki/test-automation) due to several reasons:

  - **[Exploratory Testing](https://naodeng.com.cn/en/wiki/exploratory-testing)** : It allows testers to perform exploratory testing where they can leverage their intuition and experience to uncover issues that scripted tests may not catch.
  - **User Experience** : Manual testing is essential for assessing user experience, ensuring that the software is intuitive and user-friendly.
  - **Complex Scenarios** : Some tests, especially those involving complex user interactions or non-deterministic environments, are difficult to automate and are better suited for manual execution.
  - **Initial Development Phases** : In the early stages of development, when features are still evolving, manual testing can be more efficient than trying to maintain automated tests for a rapidly changing codebase.
  - **Cost-Effectiveness** : For small projects or when the frequency of certain tests is low, manual testing can be more cost-effective than the initial investment required for automation.
  - **Learning and Feedback** : Manual testing provides immediate feedback and learning opportunities about the application, which can be invaluable for new team members or when familiarizing with new features.
  In essence, [manual testing](https://naodeng.com.cn/en/wiki/manual-testing) complements [automated testing](https://naodeng.com.cn/en/wiki/automated-testing) by covering aspects that are not easily quantifiable or automatable, providing a human perspective that is essential for delivering a high-quality user experience.

  - **[Exploratory Testing](https://naodeng.com.cn/en/wiki/exploratory-testing)** : It allows testers to perform exploratory testing where they can leverage their intuition and experience to uncover issues that scripted tests may not catch.
  - **User Experience** : Manual testing is essential for assessing user experience, ensuring that the software is intuitive and user-friendly.
  - **Complex Scenarios** : Some tests, especially those involving complex user interactions or non-deterministic environments, are difficult to automate and are better suited for manual execution.
  - **Initial Development Phases** : In the early stages of development, when features are still evolving, manual testing can be more efficient than trying to maintain automated tests for a rapidly changing codebase.
  - **Cost-Effectiveness** : For small projects or when the frequency of certain tests is low, manual testing can be more cost-effective than the initial investment required for automation.
  - **Learning and Feedback** : Manual testing provides immediate feedback and learning opportunities about the application, which can be invaluable for new team members or when familiarizing with new features.

#### What are the key differences between manual testing and automated testing?

  [Manual testing](https://naodeng.com.cn/en/wiki/manual-testing) involves human testers executing [test cases](https://naodeng.com.cn/en/wiki/test-case) without the assistance of tools or scripts. [Automated testing](https://naodeng.com.cn/en/wiki/automated-testing), on the other hand, relies on pre-scripted tests that run automatically to compare actual outcomes with predicted outcomes.
  Key differences include:

  - **Speed** : Automated tests run much faster than manual tests.
  - **Repeatability** : Automated tests can be run repeatedly with consistent accuracy, while manual testing may vary due to human error or changes in tester focus.
  - **Cost** : Manual testing requires less upfront investment but can be more costly in the long run due to its time-consuming nature. Automated testing requires a higher initial investment for tools and script development but can be more cost-effective over time.
  - **Complexity** : Automated testing can handle complex test cases more efficiently than manual testing.
  - **[Test Coverage](https://naodeng.com.cn/en/wiki/test-coverage)** : Automated testing can execute a large number of tests in a short time, which increases the test coverage.
  - **Reliability** : Automated tests eliminate human errors, providing more reliable results.
  - **Maintenance** : Automated test scripts require maintenance to adapt to changes in the application, whereas manual test cases may be more flexible to changes.
  - **Feedback** : Automated testing provides quick feedback to developers due to its rapid execution.
  - **Skillset** : Automated testing requires testers to have programming knowledge to write test scripts, while manual testing relies on analytical and exploratory skills.
  In summary, [automated testing](https://naodeng.com.cn/en/wiki/automated-testing) offers speed, repeatability, and reliability, whereas [manual testing](https://naodeng.com.cn/en/wiki/manual-testing) provides flexibility and requires less technical skill to execute.

  - **Speed** : Automated tests run much faster than manual tests.
  - **Repeatability** : Automated tests can be run repeatedly with consistent accuracy, while manual testing may vary due to human error or changes in tester focus.
  - **Cost** : Manual testing requires less upfront investment but can be more costly in the long run due to its time-consuming nature. Automated testing requires a higher initial investment for tools and script development but can be more cost-effective over time.
  - **Complexity** : Automated testing can handle complex test cases more efficiently than manual testing.
  - **[Test Coverage](https://naodeng.com.cn/en/wiki/test-coverage)** : Automated testing can execute a large number of tests in a short time, which increases the test coverage.
  - **Reliability** : Automated tests eliminate human errors, providing more reliable results.
  - **Maintenance** : Automated test scripts require maintenance to adapt to changes in the application, whereas manual test cases may be more flexible to changes.
  - **Feedback** : Automated testing provides quick feedback to developers due to its rapid execution.
  - **Skillset** : Automated testing requires testers to have programming knowledge to write test scripts, while manual testing relies on analytical and exploratory skills.

#### What are the advantages and disadvantages of manual testing?

  Advantages of [manual testing](https://naodeng.com.cn/en/wiki/manual-testing):

  - **Flexibility** : Manual testing allows for on-the-fly adjustments as testers explore and interact with the software.
  - **Human Insight** : Testers can use their intuition and experience to identify issues that automated tests might miss, such as subtle UI inconsistencies or complex user experience issues.
  - **No Need for Scripts** : It doesn't require writing test scripts, which can be beneficial for exploratory testing or when the application is in the early stages of development.
  - **Cost-Effective for Small Projects** : For small projects with limited scope, manual testing can be more cost-effective than setting up an automated testing environment.
  Disadvantages of [manual testing](https://naodeng.com.cn/en/wiki/manual-testing):

  - **Time-Consuming** : Manual tests take more time to execute as they require human intervention for each step.
  - **Less Reliable** : Humans are prone to error, leading to inconsistencies in test results due to factors like fatigue or oversight.
  - **Not Scalable** : As the application grows, the manual testing effort multiplies, making it difficult to manage and execute within tight deadlines.
  - **Limited Coverage** : It's impractical to manually execute a large number of test cases with complex scenarios, leading to limited test coverage.
  - **No Reusability** : Test cases need to be executed from scratch each time, as opposed to automated tests which can be run multiple times with little additional cost.
  - **Slow Feedback** : The time taken to manually execute tests delays feedback to developers, potentially slowing down the development cycle.
  - **Flexibility** : Manual testing allows for on-the-fly adjustments as testers explore and interact with the software.
  - **Human Insight** : Testers can use their intuition and experience to identify issues that automated tests might miss, such as subtle UI inconsistencies or complex user experience issues.
  - **No Need for Scripts** : It doesn't require writing test scripts, which can be beneficial for exploratory testing or when the application is in the early stages of development.
  - **Cost-Effective for Small Projects** : For small projects with limited scope, manual testing can be more cost-effective than setting up an automated testing environment.
  - **Time-Consuming** : Manual tests take more time to execute as they require human intervention for each step.
  - **Less Reliable** : Humans are prone to error, leading to inconsistencies in test results due to factors like fatigue or oversight.
  - **Not Scalable** : As the application grows, the manual testing effort multiplies, making it difficult to manage and execute within tight deadlines.
  - **Limited Coverage** : It's impractical to manually execute a large number of test cases with complex scenarios, leading to limited test coverage.
  - **No Reusability** : Test cases need to be executed from scratch each time, as opposed to automated tests which can be run multiple times with little additional cost.
  - **Slow Feedback** : The time taken to manually execute tests delays feedback to developers, potentially slowing down the development cycle.

#### What are the key principles of manual testing?

  The key principles of [manual testing](https://naodeng.com.cn/en/wiki/manual-testing) revolve around a tester's expertise, intuition, and understanding of the user experience. **Attention to detail** is paramount, as testers must meticulously explore and interact with the application to identify potential issues. **Understanding the end-user perspective** is crucial, as [manual testing](https://naodeng.com.cn/en/wiki/manual-testing) aims to ensure the software is intuitive and meets user requirements.
  **[Test coverage](https://naodeng.com.cn/en/wiki/test-coverage)** is another principle, where testers must ensure that all features and functionalities are thoroughly checked. This includes executing **[exploratory testing](https://naodeng.com.cn/en/wiki/exploratory-testing)**, which relies on the tester's creativity and experience to discover defects that may not be covered by predefined [test cases](https://naodeng.com.cn/en/wiki/test-case).
  **Documentation** plays a significant role, with testers required to maintain clear and concise records of [test cases](https://naodeng.com.cn/en/wiki/test-case), execution results, and defect reports. This helps in ensuring **reproducibility** of tests and facilitates communication with other team members.
  **Flexibility** is essential, as manual testers must be able to adapt their testing approach in response to new insights and changes in the application or its environment. This includes being open to **feedback** and incorporating it into the testing process.
  Lastly, **critical thinking** and **problem-solving skills** are vital, as manual testers often need to identify the root cause of a defect and understand its potential impact on the system. Testers must be able to think beyond the obvious and anticipate user behavior in various scenarios.

### Types of Manual Testing

#### What are the different types of manual testing?

  Different types of [manual testing](https://naodeng.com.cn/en/wiki/manual-testing) include:

  - **[Exploratory Testing](https://naodeng.com.cn/en/wiki/exploratory-testing)** : Testers explore the software to identify defects without predefined test cases, relying on their experience and intuition.
  - **Ad-hoc Testing** : Similar to exploratory testing but more random and unstructured, focusing on finding defects in a less systematic manner.
  - **[Usability Testing](https://naodeng.com.cn/en/wiki/usability-testing)** : Evaluates the user interface and user experience by observing real users as they interact with the application.
  - **[Accessibility Testing](https://naodeng.com.cn/en/wiki/accessibility-testing)** : Ensures the software is usable by people with disabilities, checking compliance with accessibility standards.
  - **[Compatibility Testing](https://naodeng.com.cn/en/wiki/compatibility-testing)** : Verifies that the software works as expected across different devices, operating systems, browsers, and networks.
  - **[Performance Testing](https://naodeng.com.cn/en/wiki/performance-testing)** : Assesses the responsiveness, stability, scalability, and speed of the software under various conditions.
  - **[Load Testing](https://naodeng.com.cn/en/wiki/load-testing)** : A subset of performance testing that checks the system's behavior under expected load conditions.
  - **[Stress Testing](https://naodeng.com.cn/en/wiki/stress-testing)** : Another subset of performance testing where the system is pushed beyond its normal operational capacity to see how it handles extreme conditions.
  - **Smoke Testing** : A preliminary test to check the basic functionality of the application, often performed after a new build or release.
  - **[Sanity Testing](https://naodeng.com.cn/en/wiki/sanity-testing)** : A focused form of testing to verify that a particular function or bug fix works as intended.
  - **[Regression Testing](https://naodeng.com.cn/en/wiki/regression-testing)** : Ensures that new code changes have not adversely affected existing functionality.
  - **[Acceptance Testing](https://naodeng.com.cn/en/wiki/acceptance-testing)** : Determines if the software meets business requirements and is ready for deployment, often conducted by the end-user.
  - **[Alpha Testing](https://naodeng.com.cn/en/wiki/alpha-testing)** : Conducted in-house to identify all possible issues before releasing the product to real users.
  - **[Beta Testing](https://naodeng.com.cn/en/wiki/beta-testing)** : Performed by real users in a real environment to provide feedback on product quality before the final release.
  - **[Exploratory Testing](https://naodeng.com.cn/en/wiki/exploratory-testing)** : Testers explore the software to identify defects without predefined test cases, relying on their experience and intuition.
  - **Ad-hoc Testing** : Similar to exploratory testing but more random and unstructured, focusing on finding defects in a less systematic manner.
  - **[Usability Testing](https://naodeng.com.cn/en/wiki/usability-testing)** : Evaluates the user interface and user experience by observing real users as they interact with the application.
  - **[Accessibility Testing](https://naodeng.com.cn/en/wiki/accessibility-testing)** : Ensures the software is usable by people with disabilities, checking compliance with accessibility standards.
  - **[Compatibility Testing](https://naodeng.com.cn/en/wiki/compatibility-testing)** : Verifies that the software works as expected across different devices, operating systems, browsers, and networks.
  - **[Performance Testing](https://naodeng.com.cn/en/wiki/performance-testing)** : Assesses the responsiveness, stability, scalability, and speed of the software under various conditions.
  - **[Load Testing](https://naodeng.com.cn/en/wiki/load-testing)** : A subset of performance testing that checks the system's behavior under expected load conditions.
  - **[Stress Testing](https://naodeng.com.cn/en/wiki/stress-testing)** : Another subset of performance testing where the system is pushed beyond its normal operational capacity to see how it handles extreme conditions.
  - **Smoke Testing** : A preliminary test to check the basic functionality of the application, often performed after a new build or release.
  - **[Sanity Testing](https://naodeng.com.cn/en/wiki/sanity-testing)** : A focused form of testing to verify that a particular function or bug fix works as intended.
  - **[Regression Testing](https://naodeng.com.cn/en/wiki/regression-testing)** : Ensures that new code changes have not adversely affected existing functionality.
  - **[Acceptance Testing](https://naodeng.com.cn/en/wiki/acceptance-testing)** : Determines if the software meets business requirements and is ready for deployment, often conducted by the end-user.
  - **[Alpha Testing](https://naodeng.com.cn/en/wiki/alpha-testing)** : Conducted in-house to identify all possible issues before releasing the product to real users.
  - **[Beta Testing](https://naodeng.com.cn/en/wiki/beta-testing)** : Performed by real users in a real environment to provide feedback on product quality before the final release.

#### What is black box testing?

  [Black box testing](https://naodeng.com.cn/en/wiki/black-box-testing) is a method of [software testing](https://naodeng.com.cn/en/wiki/software-testing) that examines the functionality of an application without peering into its internal structures or workings. This technique focuses on what the software does rather than how it does it. [Test cases](https://naodeng.com.cn/en/wiki/test-case) are created using the software's specifications and requirements, ensuring that all features are tested from the user's perspective.
  Testers input data and examine output without knowing how and where the inputs are worked upon. This approach can be applied to virtually all levels of [software testing](https://naodeng.com.cn/en/wiki/software-testing): unit, integration, system, and acceptance. It is particularly useful in situations where the tester does not have access to the source code or when the complexity of the source code is irrelevant to the functionality being tested.
  **Key aspects** of [black box testing](https://naodeng.com.cn/en/wiki/black-box-testing) include:

  - **Functional Validity** : Checking if the software behaves as expected.
  - **Error Identification** : Finding bugs without knowing the underlying code.
  - **User Environment Simulation** : Mimicking user behavior to ensure the software meets user requirements.
  Since [black box testing](https://naodeng.com.cn/en/wiki/black-box-testing) is oblivious to the internal structure, it can miss certain types of defects that are related to the software's internal logic. However, it is an essential part of a comprehensive testing strategy, complementing white box and [grey box testing](https://naodeng.com.cn/en/wiki/grey-box-testing) methods.

  - **Functional Validity** : Checking if the software behaves as expected.
  - **Error Identification** : Finding bugs without knowing the underlying code.
  - **User Environment Simulation** : Mimicking user behavior to ensure the software meets user requirements.

#### What is white box testing?

  [White box testing](https://naodeng.com.cn/en/wiki/white-box-testing), also known as **clear box testing**, **[glass box testing](https://naodeng.com.cn/en/wiki/glass-box-testing)**, or **[structural testing](https://naodeng.com.cn/en/wiki/structural-testing)**, is a method of [software testing](https://naodeng.com.cn/en/wiki/software-testing) where the tester has full visibility into the internal workings of the item being tested. Unlike [black box testing](https://naodeng.com.cn/en/wiki/black-box-testing), which focuses on externally observable behavior, [white box testing](https://naodeng.com.cn/en/wiki/white-box-testing) requires knowledge of the code structure, implementation details, and programming skills.
  In [white box testing](https://naodeng.com.cn/en/wiki/white-box-testing), testers design [test cases](https://naodeng.com.cn/en/wiki/test-case) based on the **source code** to verify the flow of inputs through the code, the functioning of conditional loops, and the handling of data structures among other things. It allows testers to evaluate paths within a unit, statements, branches, and conditions.
  Common techniques used in [white box testing](https://naodeng.com.cn/en/wiki/white-box-testing) include:

  - **Statement Coverage** : Ensuring every statement in the code has been executed at least once.
  - **Branch Coverage** : Ensuring every branch (true/false) has been executed.
  - **Path Coverage** : Ensuring every possible route through a given part of the code is executed.
  [White box testing](https://naodeng.com.cn/en/wiki/white-box-testing) is typically performed at the **unit level** during the development phase. It can be automated, and tools like code analyzers and debuggers are often used to facilitate the process.
  Testers can also use [white box testing](https://naodeng.com.cn/en/wiki/white-box-testing) to perform **security audits**, checking for vulnerabilities within the code.
  Given the audience's expertise in [test automation](https://naodeng.com.cn/en/wiki/test-automation), it's understood that [white box testing](https://naodeng.com.cn/en/wiki/white-box-testing) can be integrated into a CI/CD pipeline, allowing for continuous validation of code changes and early detection of issues.

  - **Statement Coverage** : Ensuring every statement in the code has been executed at least once.
  - **Branch Coverage** : Ensuring every branch (true/false) has been executed.
  - **Path Coverage** : Ensuring every possible route through a given part of the code is executed.

#### What is grey box testing?

  [Grey box testing](https://naodeng.com.cn/en/wiki/grey-box-testing) is a hybrid approach that combines elements of both **black box** and **[white box testing](https://naodeng.com.cn/en/wiki/white-box-testing)** methodologies. It requires partial knowledge of the internal workings of the application, which typically includes understanding of the [database](https://naodeng.com.cn/en/wiki/database) schema and algorithmic flow, but not the full source code. Testers in [grey box testing](https://naodeng.com.cn/en/wiki/grey-box-testing) have access to detailed design documents and [database](https://naodeng.com.cn/en/wiki/database) diagrams, which help them design [test cases](https://naodeng.com.cn/en/wiki/test-case) that are more effective in finding hidden errors.
  The approach is particularly useful when testing web applications, where testers can utilize knowledge of HTML, JavaScript, and server communications to craft tests that explore potential security vulnerabilities or integration issues. [Grey box testing](https://naodeng.com.cn/en/wiki/grey-box-testing) is also applied in [integration testing](https://naodeng.com.cn/en/wiki/integration-testing), [penetration testing](https://naodeng.com.cn/en/wiki/penetration-testing), and for testing networking protocols.
  Testers use tools that help them interact with the application's interfaces at a level deeper than a typical end-user but without requiring the deep dive into the codebase that [white box testing](https://naodeng.com.cn/en/wiki/white-box-testing) demands. Examples of such tools include:

  ```
  - Web application proxies
  - Database query tools
  - Code analysis tools
  - Debuggers
  ```
  The main advantage of [grey box testing](https://naodeng.com.cn/en/wiki/grey-box-testing) is that it provides a balance between the high-level perspective of [black box testing](https://naodeng.com.cn/en/wiki/black-box-testing) and the detailed perspective of [white box testing](https://naodeng.com.cn/en/wiki/white-box-testing), allowing testers to focus on the most critical areas of an application with a reasonable understanding of the underlying structures. This leads to more thorough testing than [black box testing](https://naodeng.com.cn/en/wiki/black-box-testing) alone, without the extensive time investment required for full [white box testing](https://naodeng.com.cn/en/wiki/white-box-testing).

#### What is the difference between functional and non-functional testing?

  [Functional testing](https://naodeng.com.cn/en/wiki/functional-testing) focuses on verifying that each function of the software application operates in conformance with the requirement specification. This type of testing validates the behavior of an application by providing appropriate input and examining the output against the defined [functional requirements](https://naodeng.com.cn/en/wiki/functional-requirements). It includes various tests such as unit tests, integration tests, system tests, and acceptance tests.
  [Non-functional testing](https://naodeng.com.cn/en/wiki/non-functional-testing), on the other hand, refers to aspects that are not related to specific behaviors or functions of the system. It checks the non-functional aspects (performance, usability, reliability, etc.) of the software application. [Non-functional testing](https://naodeng.com.cn/en/wiki/non-functional-testing) is designed to assess the readiness of a system according to nonfunctional parameters which never get addressed by [functional testing](https://naodeng.com.cn/en/wiki/functional-testing). Types of [non-functional testing](https://naodeng.com.cn/en/wiki/non-functional-testing) include [performance testing](https://naodeng.com.cn/en/wiki/performance-testing), [load testing](https://naodeng.com.cn/en/wiki/load-testing), [stress testing](https://naodeng.com.cn/en/wiki/stress-testing), [security testing](https://naodeng.com.cn/en/wiki/security-testing), [compatibility testing](https://naodeng.com.cn/en/wiki/compatibility-testing), and [usability testing](https://naodeng.com.cn/en/wiki/usability-testing).
  In essence, **[functional testing](https://naodeng.com.cn/en/wiki/functional-testing)** ensures the software does what it's supposed to do, while **[non-functional testing](https://naodeng.com.cn/en/wiki/non-functional-testing)** ensures the software will perform well in the user's environment under various conditions. Both are critical for assessing the overall quality and user experience of the software.

### Manual Testing Process

#### What are the stages in the manual testing life cycle?

  The [manual testing](https://naodeng.com.cn/en/wiki/manual-testing) life cycle consists of several stages:

  1. **Requirement Analysis** : Understanding the application's functionality and identifying testable requirements.
  2. **Test Planning** : Defining the scope and objectives, determining the resources (time, manpower, tools), and outlining the test strategy.
  3. **[Test Case](https://naodeng.com.cn/en/wiki/test-case) Development** : Creating test cases and test scripts, which includes defining the conditions, inputs, actions, and expected results.
  4. **[Test Environment](https://naodeng.com.cn/en/wiki/test-environment) [Setup](https://naodeng.com.cn/en/wiki/setup)** : Preparing the hardware and software environment where the testing will be conducted, including any necessary test data.
  5. **[Test Execution](https://naodeng.com.cn/en/wiki/test-execution)** : Running the test cases manually, logging the outcome of each test case, and reporting any defects found.
  6. **Defect Logging** : Recording the details of any defects or issues found during test execution in a defect tracking tool.
  7. **Test Cycle Closure** : Evaluating the test cycle's effectiveness, ensuring all test cases are executed and defects are either fixed or acknowledged, and creating a test closure report.
  Each stage is critical to ensure the thoroughness and effectiveness of the [manual testing](https://naodeng.com.cn/en/wiki/manual-testing) process. Testers must be meticulous and organized, as the quality of the testing can significantly impact the overall quality of the software product.

  1. **Requirement Analysis** : Understanding the application's functionality and identifying testable requirements.
  2. **Test Planning** : Defining the scope and objectives, determining the resources (time, manpower, tools), and outlining the test strategy.
  3. **[Test Case](https://naodeng.com.cn/en/wiki/test-case) Development** : Creating test cases and test scripts, which includes defining the conditions, inputs, actions, and expected results.
  4. **[Test Environment](https://naodeng.com.cn/en/wiki/test-environment) [Setup](https://naodeng.com.cn/en/wiki/setup)** : Preparing the hardware and software environment where the testing will be conducted, including any necessary test data.
  5. **[Test Execution](https://naodeng.com.cn/en/wiki/test-execution)** : Running the test cases manually, logging the outcome of each test case, and reporting any defects found.
  6. **Defect Logging** : Recording the details of any defects or issues found during test execution in a defect tracking tool.
  7. **Test Cycle Closure** : Evaluating the test cycle's effectiveness, ensuring all test cases are executed and defects are either fixed or acknowledged, and creating a test closure report.

#### What is test planning and what does it involve?

  Test planning is a critical phase in the [software testing](https://naodeng.com.cn/en/wiki/software-testing) life cycle, where a detailed blueprint is created to guide the entire testing process. It involves defining the **objectives**, **scope**, **approach**, and **resources** required for testing. A [test plan](https://naodeng.com.cn/en/wiki/test-plan) outlines the **[test strategy](https://naodeng.com.cn/en/wiki/test-strategy)**, **schedule**, **deliverables**, and **risk management** plans to ensure comprehensive coverage and efficient execution.
  Key components of test planning include:

  - **Test Objectives** : Clear goals for what the testing aims to achieve.
  - **Test Scope** : Boundaries of what will and will not be tested.
  - **[Test Strategy](https://naodeng.com.cn/en/wiki/test-strategy)** : High-level decisions on how testing will be approached, including the choice between manual and automated testing, and the types of tests to be performed.
  - **Resource Allocation** : Identification and assignment of personnel, tools, and environments necessary for testing.
  - **Schedule and Milestones** : A timeline for test activities, including start and end dates for test cycles.
  - **Risk Analysis** : Identification of potential risks and the formulation of mitigation strategies.
  - **Test Deliverables** : Documentation to be produced, such as test plans, test cases, test scripts, and defect reports.
  - **Entry and Exit Criteria** : Conditions that must be met to start testing and criteria for concluding the test phases.
  Effective test planning ensures that testing is aligned with project objectives, conducted efficiently, and provides valuable insights into [software quality](https://naodeng.com.cn/en/wiki/software-quality). It sets the stage for successful [test execution](https://naodeng.com.cn/en/wiki/test-execution) and helps manage expectations of stakeholders.

  - **Test Objectives** : Clear goals for what the testing aims to achieve.
  - **Test Scope** : Boundaries of what will and will not be tested.
  - **[Test Strategy](https://naodeng.com.cn/en/wiki/test-strategy)** : High-level decisions on how testing will be approached, including the choice between manual and automated testing, and the types of tests to be performed.
  - **Resource Allocation** : Identification and assignment of personnel, tools, and environments necessary for testing.
  - **Schedule and Milestones** : A timeline for test activities, including start and end dates for test cycles.
  - **Risk Analysis** : Identification of potential risks and the formulation of mitigation strategies.
  - **Test Deliverables** : Documentation to be produced, such as test plans, test cases, test scripts, and defect reports.
  - **Entry and Exit Criteria** : Conditions that must be met to start testing and criteria for concluding the test phases.

#### What is test case design and what are the key elements of a good test case?

  [Test case](https://naodeng.com.cn/en/wiki/test-case) design is the process of creating a set of conditions or variables under which a tester will determine whether a system under test satisfies requirements or works correctly. The key elements of a good [test case](https://naodeng.com.cn/en/wiki/test-case) include:

  - **Clear Objectives** : Each test case should have a clear objective and should be linked to specific requirements.
  - **Preconditions** : Define any specific conditions that must be met before the test is executed.
  - **[Test Data](https://naodeng.com.cn/en/wiki/test-data)** : Include the necessary data that will be used for testing, or references to where such data can be found.
  - **Steps to Execute** : Provide detailed steps for the tester to follow, ensuring repeatability and consistency.
  - **[Expected Results](https://naodeng.com.cn/en/wiki/expected-result)** : Clearly state what outcomes are expected when the test case is executed correctly.
  - **[Postconditions](https://naodeng.com.cn/en/wiki/postcondition)** : Describe the state of the system after the test case execution, if applicable.
  - **Traceability** : Reference the requirements or user stories to ensure coverage and traceability.
  - **Unambiguity** : Write the test case in a way that leaves no room for interpretation to maintain consistency across different testers.
  - **Idempotence** : Design test cases so that they can be run multiple times and still produce the same results.
  - **Clean-Up** : Include steps to revert any changes made during the test, ensuring the system returns to its pre-test state.
  A well-designed [test case](https://naodeng.com.cn/en/wiki/test-case) not only helps in validating the functionality of the application but also serves as a document for future testing cycles, facilitating maintenance and [regression testing](https://naodeng.com.cn/en/wiki/regression-testing).

  - **Clear Objectives** : Each test case should have a clear objective and should be linked to specific requirements.
  - **Preconditions** : Define any specific conditions that must be met before the test is executed.
  - **[Test Data](https://naodeng.com.cn/en/wiki/test-data)** : Include the necessary data that will be used for testing, or references to where such data can be found.
  - **Steps to Execute** : Provide detailed steps for the tester to follow, ensuring repeatability and consistency.
  - **[Expected Results](https://naodeng.com.cn/en/wiki/expected-result)** : Clearly state what outcomes are expected when the test case is executed correctly.
  - **[Postconditions](https://naodeng.com.cn/en/wiki/postcondition)** : Describe the state of the system after the test case execution, if applicable.
  - **Traceability** : Reference the requirements or user stories to ensure coverage and traceability.
  - **Unambiguity** : Write the test case in a way that leaves no room for interpretation to maintain consistency across different testers.
  - **Idempotence** : Design test cases so that they can be run multiple times and still produce the same results.
  - **Clean-Up** : Include steps to revert any changes made during the test, ensuring the system returns to its pre-test state.

#### What is test execution and what are the steps involved?

  [Test execution](https://naodeng.com.cn/en/wiki/test-execution) in software [test automation](https://naodeng.com.cn/en/wiki/test-automation) is the process where automated scripts are run against the software under test to verify that it behaves as expected. The steps involved in [test execution](https://naodeng.com.cn/en/wiki/test-execution) are as follows:

  1. **Environment [Setup](https://naodeng.com.cn/en/wiki/setup)**: Ensure the [test environment](https://naodeng.com.cn/en/wiki/test-environment) is configured correctly with all necessary hardware, software, network settings, and data.
  2. **[Test Data](https://naodeng.com.cn/en/wiki/test-data) Preparation**: Create or load the [test data](https://naodeng.com.cn/en/wiki/test-data) required for the [test cases](https://naodeng.com.cn/en/wiki/test-case).
  3. **Execution Scheduling**: Determine the order and timing of [test cases](https://naodeng.com.cn/en/wiki/test-case), possibly using a Continuous Integration (CI) tool to schedule and trigger tests.
  4. **Running Tests**: Execute the automated [test scripts](https://naodeng.com.cn/en/wiki/test-script) using the selected [test automation](https://naodeng.com.cn/en/wiki/test-automation) tool or framework.
  5. **Monitoring**: Observe the [test execution](https://naodeng.com.cn/en/wiki/test-execution) to ensure that tests are running as expected. This may involve checking the status of test runs, watching for timeouts or errors, and ensuring that the [test environment](https://naodeng.com.cn/en/wiki/test-environment) remains stable.
  6. **Results Analysis**: Review the output from the test runs, including pass/fail status for each [test case](https://naodeng.com.cn/en/wiki/test-case), logs, screenshots, and other artifacts.
  7. **Defect Logging**: Log any failures or issues identified during [test execution](https://naodeng.com.cn/en/wiki/test-execution) into a defect tracking system, with sufficient detail to enable debugging.
  8. **Result Reporting**: Generate reports summarizing the [test execution](https://naodeng.com.cn/en/wiki/test-execution) outcomes, including metrics such as pass rate, coverage, and defect counts.
  9. **Cleanup**: Reset the [test environment](https://naodeng.com.cn/en/wiki/test-environment) to a clean state, ready for subsequent test runs or other activities.
  Throughout these steps, it's crucial to maintain clear documentation and ensure that any deviations from [expected results](https://naodeng.com.cn/en/wiki/expected-result) are investigated and addressed promptly.

  1. **Environment [Setup](https://naodeng.com.cn/en/wiki/setup)**: Ensure the [test environment](https://naodeng.com.cn/en/wiki/test-environment) is configured correctly with all necessary hardware, software, network settings, and data.
  2. **[Test Data](https://naodeng.com.cn/en/wiki/test-data) Preparation**: Create or load the [test data](https://naodeng.com.cn/en/wiki/test-data) required for the [test cases](https://naodeng.com.cn/en/wiki/test-case).
  3. **Execution Scheduling**: Determine the order and timing of [test cases](https://naodeng.com.cn/en/wiki/test-case), possibly using a Continuous Integration (CI) tool to schedule and trigger tests.
  4. **Running Tests**: Execute the automated [test scripts](https://naodeng.com.cn/en/wiki/test-script) using the selected [test automation](https://naodeng.com.cn/en/wiki/test-automation) tool or framework.
  5. **Monitoring**: Observe the [test execution](https://naodeng.com.cn/en/wiki/test-execution) to ensure that tests are running as expected. This may involve checking the status of test runs, watching for timeouts or errors, and ensuring that the [test environment](https://naodeng.com.cn/en/wiki/test-environment) remains stable.
  6. **Results Analysis**: Review the output from the test runs, including pass/fail status for each [test case](https://naodeng.com.cn/en/wiki/test-case), logs, screenshots, and other artifacts.
  7. **Defect Logging**: Log any failures or issues identified during [test execution](https://naodeng.com.cn/en/wiki/test-execution) into a defect tracking system, with sufficient detail to enable debugging.
  8. **Result Reporting**: Generate reports summarizing the [test execution](https://naodeng.com.cn/en/wiki/test-execution) outcomes, including metrics such as pass rate, coverage, and defect counts.
  9. **Cleanup**: Reset the [test environment](https://naodeng.com.cn/en/wiki/test-environment) to a clean state, ready for subsequent test runs or other activities.

#### What is test closure and what does it involve?

  Test closure is the final phase of the testing cycle, marking the completion of the testing process. It involves several key activities:

  - **Evaluating deliverables** : Ensure all test objectives are met and all deliverables are accounted for and up to standard.
  - **Reporting** : Compile a comprehensive test summary report detailing the testing outcomes, coverage, defect analysis, and assessment of the quality of the test object.
  - **Documentation** : Archive all relevant test artifacts, such as test cases, test data, and defect logs, for future reference or audits.
  - **Lessons learned** : Conduct a retrospective meeting to discuss what went well, what didn't, and identify improvements for future testing cycles.
  - **Release criteria check** : Verify that the product meets the exit criteria defined in the test planning phase before it is released.
  - **Formal closure** : Obtain formal sign-off from stakeholders, indicating acceptance of the testing effort and the product's readiness for release.
  These activities ensure a structured and traceable end to the testing efforts, providing valuable insights for future projects and maintaining the integrity of the testing process.

  - **Evaluating deliverables** : Ensure all test objectives are met and all deliverables are accounted for and up to standard.
  - **Reporting** : Compile a comprehensive test summary report detailing the testing outcomes, coverage, defect analysis, and assessment of the quality of the test object.
  - **Documentation** : Archive all relevant test artifacts, such as test cases, test data, and defect logs, for future reference or audits.
  - **Lessons learned** : Conduct a retrospective meeting to discuss what went well, what didn't, and identify improvements for future testing cycles.
  - **Release criteria check** : Verify that the product meets the exit criteria defined in the test planning phase before it is released.
  - **Formal closure** : Obtain formal sign-off from stakeholders, indicating acceptance of the testing effort and the product's readiness for release.

### Manual Testing Tools

#### What tools are used in manual testing?

  In [manual testing](https://naodeng.com.cn/en/wiki/manual-testing), tools are generally less complex than those used in [automated testing](https://naodeng.com.cn/en/wiki/automated-testing). They support various testing activities ranging from [test management](https://naodeng.com.cn/en/wiki/test-management) to defect tracking. Here's a concise list of tools commonly used in [manual testing](https://naodeng.com.cn/en/wiki/manual-testing):

  - **[Test Management](https://naodeng.com.cn/en/wiki/test-management) Tools**: Tools like TestRail, Zephyr, and Quality Center are used to organize and manage [test cases](https://naodeng.com.cn/en/wiki/test-case), plans, and runs. They help in tracking the progress and reporting the status of testing activities.
  - **Defect Tracking Tools**: [Jira](https://naodeng.com.cn/en/wiki/jira), Bugzilla, and Mantis are popular choices for recording, tracking, and managing defects discovered during testing. They facilitate collaboration between testers and developers to resolve issues.
  - **Documentation Tools**: Microsoft Word and Google Docs are used to create [test plans](https://naodeng.com.cn/en/wiki/test-plan), [test cases](https://naodeng.com.cn/en/wiki/test-case), and testing reports. They help in maintaining a clear and accessible record of the testing process.
  - **Spreadsheet Tools**: Microsoft Excel and Google Sheets are often used for [test case management](https://naodeng.com.cn/en/wiki/test-case-management), particularly in smaller projects or organizations without dedicated [test management](https://naodeng.com.cn/en/wiki/test-management) software.
  - **Collaboration Tools**: Slack, Microsoft Teams, and Confluence aid communication among team members, which is crucial for coordinating [manual testing](https://naodeng.com.cn/en/wiki/manual-testing) efforts and sharing insights.
  - **Screen Capture and Annotation Tools**: Snagit and LightShot are used to take screenshots or record videos of defects, which are then annotated to provide visual evidence and context for developers.
  These tools support the [manual testing](https://naodeng.com.cn/en/wiki/manual-testing) process by enhancing organization, communication, and documentation, but they do not automate the execution of tests.

  - **[Test Management](https://naodeng.com.cn/en/wiki/test-management) Tools**: Tools like TestRail, Zephyr, and Quality Center are used to organize and manage [test cases](https://naodeng.com.cn/en/wiki/test-case), plans, and runs. They help in tracking the progress and reporting the status of testing activities.
  - **Defect Tracking Tools**: [Jira](https://naodeng.com.cn/en/wiki/jira), Bugzilla, and Mantis are popular choices for recording, tracking, and managing defects discovered during testing. They facilitate collaboration between testers and developers to resolve issues.
  - **Documentation Tools**: Microsoft Word and Google Docs are used to create [test plans](https://naodeng.com.cn/en/wiki/test-plan), [test cases](https://naodeng.com.cn/en/wiki/test-case), and testing reports. They help in maintaining a clear and accessible record of the testing process.
  - **Spreadsheet Tools**: Microsoft Excel and Google Sheets are often used for [test case management](https://naodeng.com.cn/en/wiki/test-case-management), particularly in smaller projects or organizations without dedicated [test management](https://naodeng.com.cn/en/wiki/test-management) software.
  - **Collaboration Tools**: Slack, Microsoft Teams, and Confluence aid communication among team members, which is crucial for coordinating [manual testing](https://naodeng.com.cn/en/wiki/manual-testing) efforts and sharing insights.
  - **Screen Capture and Annotation Tools**: Snagit and LightShot are used to take screenshots or record videos of defects, which are then annotated to provide visual evidence and context for developers.

#### What is the role of a test management tool in manual testing?

  A **[test management](https://naodeng.com.cn/en/wiki/test-management) tool** in [manual testing](https://naodeng.com.cn/en/wiki/manual-testing) serves as a central repository for all test-related activities. It facilitates the organization, documentation, and tracking of the testing process, ensuring that [manual testing](https://naodeng.com.cn/en/wiki/manual-testing) efforts are systematic and transparent. Key roles include:

  - **Test Planning** : Helps in defining and managing test plans, outlining the scope, objectives, and strategies of testing activities.
  - **[Test Case Management](https://naodeng.com.cn/en/wiki/test-case-management)** : Allows for creating, storing, and maintaining test cases, as well as mapping them to requirements to ensure coverage.
  - **[Test Execution](https://naodeng.com.cn/en/wiki/test-execution) Tracking** : Enables recording of test execution results, providing visibility into the testing progress and outcomes.
  - **[Defect Management](https://naodeng.com.cn/en/wiki/defect-management)** : Integrates with or includes a defect tracking system to log, assign, and track bugs found during manual testing.
  - **Reporting and Metrics** : Generates reports and dashboards that offer insights into the effectiveness of the testing process, highlighting areas of risk and success.
  - **Collaboration** : Facilitates communication and collaboration among team members by sharing test artifacts and status updates in real-time.
  By providing these capabilities, a [test management](https://naodeng.com.cn/en/wiki/test-management) tool enhances the efficiency, accuracy, and traceability of [manual testing](https://naodeng.com.cn/en/wiki/manual-testing) efforts, even for experienced [test automation](https://naodeng.com.cn/en/wiki/test-automation) engineers who may occasionally need to perform manual tests.

  - **Test Planning** : Helps in defining and managing test plans, outlining the scope, objectives, and strategies of testing activities.
  - **[Test Case Management](https://naodeng.com.cn/en/wiki/test-case-management)** : Allows for creating, storing, and maintaining test cases, as well as mapping them to requirements to ensure coverage.
  - **[Test Execution](https://naodeng.com.cn/en/wiki/test-execution) Tracking** : Enables recording of test execution results, providing visibility into the testing progress and outcomes.
  - **[Defect Management](https://naodeng.com.cn/en/wiki/defect-management)** : Integrates with or includes a defect tracking system to log, assign, and track bugs found during manual testing.
  - **Reporting and Metrics** : Generates reports and dashboards that offer insights into the effectiveness of the testing process, highlighting areas of risk and success.
  - **Collaboration** : Facilitates communication and collaboration among team members by sharing test artifacts and status updates in real-time.

#### What is the role of a defect tracking tool in manual testing?

  In [manual testing](https://naodeng.com.cn/en/wiki/manual-testing), a **defect tracking tool** is essential for organizing and managing the process of identifying, documenting, and resolving defects discovered during testing. It serves as a centralized repository for all defect-related information, allowing testers and developers to **communicate effectively** about issues.
  Key roles of a defect tracking tool include:

  - **Recording Defects** : Testers log defects with details like description, severity, steps to reproduce, and screenshots.
  - **Tracking Progress** : The tool allows for monitoring the status of defects from discovery through to resolution.
  - **Prioritization** : Defects can be prioritized based on severity, frequency, or impact, helping teams to address the most critical issues first.
  - **Assigning Responsibility** : Defects can be assigned to specific team members for investigation and resolution.
  - **Historical Data** : It provides a historical record of defects, which can be useful for future projects and regression testing.
  - **Metrics and Reporting** : The tool generates reports and metrics that help in assessing the quality of the software and the efficiency of the testing process.
  By using a defect tracking tool, teams can ensure that no defects slip through the cracks, and they can improve the overall quality of the software product. It also facilitates better resource allocation and project management by providing clear visibility into the defect resolution workflow.

  - **Recording Defects** : Testers log defects with details like description, severity, steps to reproduce, and screenshots.
  - **Tracking Progress** : The tool allows for monitoring the status of defects from discovery through to resolution.
  - **Prioritization** : Defects can be prioritized based on severity, frequency, or impact, helping teams to address the most critical issues first.
  - **Assigning Responsibility** : Defects can be assigned to specific team members for investigation and resolution.
  - **Historical Data** : It provides a historical record of defects, which can be useful for future projects and regression testing.
  - **Metrics and Reporting** : The tool generates reports and metrics that help in assessing the quality of the software and the efficiency of the testing process.

#### What are some examples of manual testing tools?

  [Manual testing](https://naodeng.com.cn/en/wiki/manual-testing) tools typically encompass a variety of applications and aids that facilitate the [manual testing](https://naodeng.com.cn/en/wiki/manual-testing) process. These tools do not automate the testing process but support testers in executing and managing tests. Examples include:

  - **Spreadsheets and Documents** : Microsoft Excel or Google Sheets for test case management and tracking results.
  - **[Test Case Management](https://naodeng.com.cn/en/wiki/test-case-management) Tools** : Tools like TestRail, Zephyr, or TestLink help organize and manage test cases, plan testing activities, and report on the status of testing.
  - **Defect Tracking Tools** : JIRA, Bugzilla, or MantisBT are used to report, track, and manage defects found during testing.
  - **[Exploratory Testing](https://naodeng.com.cn/en/wiki/exploratory-testing) Aids** : Session-based test management tools like Rapid Reporter facilitate note-taking and time management during exploratory testing sessions.
  - **Collaboration Tools** : Confluence, Slack, or Trello can be used for sharing information, collaborating on test plans, and coordinating testing efforts.
  - **Screen Capture and Annotation Tools** : Snagit or Greenshot for taking screenshots and annotating them to highlight issues.
  - **[API Testing](https://naodeng.com.cn/en/wiki/api-testing) Tools** : Postman or Insomnia for manual API testing, allowing testers to send requests and analyze responses.
  - **Performance Monitoring Tools** : Tools like Browser DevTools or New Relic to manually monitor and analyze performance issues.
  These tools help streamline the [manual testing](https://naodeng.com.cn/en/wiki/manual-testing) process, making it more efficient and organized, but they do not replace the need for a human tester to execute the tests.

  - **Spreadsheets and Documents** : Microsoft Excel or Google Sheets for test case management and tracking results.
  - **[Test Case Management](https://naodeng.com.cn/en/wiki/test-case-management) Tools** : Tools like TestRail, Zephyr, or TestLink help organize and manage test cases, plan testing activities, and report on the status of testing.
  - **Defect Tracking Tools** : JIRA, Bugzilla, or MantisBT are used to report, track, and manage defects found during testing.
  - **[Exploratory Testing](https://naodeng.com.cn/en/wiki/exploratory-testing) Aids** : Session-based test management tools like Rapid Reporter facilitate note-taking and time management during exploratory testing sessions.
  - **Collaboration Tools** : Confluence, Slack, or Trello can be used for sharing information, collaborating on test plans, and coordinating testing efforts.
  - **Screen Capture and Annotation Tools** : Snagit or Greenshot for taking screenshots and annotating them to highlight issues.
  - **[API Testing](https://naodeng.com.cn/en/wiki/api-testing) Tools** : Postman or Insomnia for manual API testing, allowing testers to send requests and analyze responses.
  - **Performance Monitoring Tools** : Tools like Browser DevTools or New Relic to manually monitor and analyze performance issues.

### Manual Testing Best Practices

#### What are some best practices for manual testing?

  Best practices for [manual testing](https://naodeng.com.cn/en/wiki/manual-testing), considering the audience's expertise in [test automation](https://naodeng.com.cn/en/wiki/test-automation), include:

  - **Prioritize [test cases](https://naodeng.com.cn/en/wiki/test-case)**
    based on risk and impact. Focus on critical functionalities first.

  - **Keep [test cases](https://naodeng.com.cn/en/wiki/test-case) clear and concise**
    to ensure they are easy to follow and repeatable.

  - **Use [exploratory testing](https://naodeng.com.cn/en/wiki/exploratory-testing)**
    to uncover issues that structured testing might miss.

  - **Document defects thoroughly**
    , including steps to reproduce, expected vs. actual results, and screenshots if applicable.

  - **Perform [regression testing](https://naodeng.com.cn/en/wiki/regression-testing)**
    after fixes and enhancements to ensure new changes haven't introduced new issues.

  - **Peer review [test cases](https://naodeng.com.cn/en/wiki/test-case)**
    to improve test coverage and catch mistakes.

  - **Stay updated**
    with the latest testing techniques and tools to enhance manual testing processes.

  - **Balance manual and [automated testing](https://naodeng.com.cn/en/wiki/automated-testing)**
    by identifying which tests are best suited for automation and which require a human touch.

  - **Communicate effectively**
    with the development team to ensure a clear understanding of features and requirements.

  - **Maintain a well-organized [test environment](https://naodeng.com.cn/en/wiki/test-environment)**
    to ensure consistency and reliability in test results.

  - **Be adaptable**
    and ready to adjust testing strategies as the project evolves.
  By integrating these practices, manual testers can complement automated processes and contribute to a robust testing strategy.

  - **Prioritize [test cases](https://naodeng.com.cn/en/wiki/test-case)**
    based on risk and impact. Focus on critical functionalities first.

  - **Keep [test cases](https://naodeng.com.cn/en/wiki/test-case) clear and concise**
    to ensure they are easy to follow and repeatable.

  - **Use [exploratory testing](https://naodeng.com.cn/en/wiki/exploratory-testing)**
    to uncover issues that structured testing might miss.

  - **Document defects thoroughly**
    , including steps to reproduce, expected vs. actual results, and screenshots if applicable.

  - **Perform [regression testing](https://naodeng.com.cn/en/wiki/regression-testing)**
    after fixes and enhancements to ensure new changes haven't introduced new issues.

  - **Peer review [test cases](https://naodeng.com.cn/en/wiki/test-case)**
    to improve test coverage and catch mistakes.

  - **Stay updated**
    with the latest testing techniques and tools to enhance manual testing processes.

  - **Balance manual and [automated testing](https://naodeng.com.cn/en/wiki/automated-testing)**
    by identifying which tests are best suited for automation and which require a human touch.

  - **Communicate effectively**
    with the development team to ensure a clear understanding of features and requirements.

  - **Maintain a well-organized [test environment](https://naodeng.com.cn/en/wiki/test-environment)**
    to ensure consistency and reliability in test results.

  - **Be adaptable**
    and ready to adjust testing strategies as the project evolves.

#### How can manual testing be made more effective?

  To enhance the effectiveness of [manual testing](https://naodeng.com.cn/en/wiki/manual-testing), consider the following strategies:

  - **Prioritize [test cases](https://naodeng.com.cn/en/wiki/test-case)**
    based on risk and impact. Focus on critical functionalities that affect the user experience directly.

  - **Leverage [exploratory testing](https://naodeng.com.cn/en/wiki/exploratory-testing)**
    to uncover issues that scripted tests may miss. This allows testers to use their creativity and intuition.

  - **Use checklists**
    to ensure all areas are covered without the rigidity of formal test cases.

  - **[Pair testing](https://naodeng.com.cn/en/wiki/pair-testing)**
    can be beneficial, where two testers work together to find defects; one operates the software while the other takes notes and thinks of new test scenarios.

  - **Implement [session-based testing](https://naodeng.com.cn/en/wiki/session-based-testing)**
    to manage and track exploratory testing efforts, ensuring accountability and coverage.

  - **Review and refine**
    test cases regularly to remove redundancies and keep them up-to-date with the application changes.

  - **Utilize mind maps**
    to visualize test coverage and identify gaps in testing.

  - **Continuously learn**
    about the application under test; deeper understanding leads to more insightful test scenarios.

  - **Collaborate with developers**
    to gain insights into the code changes that might affect testing.

  - **Gather feedback**
    from stakeholders to align testing efforts with business requirements and user needs.

  - **Automate repetitive tasks**
    that don't require human judgment, such as data setup, to allow more time for actual testing.

  - **Invest in tester training**
    to keep skills sharp and knowledge current, especially in areas like new testing techniques or domain expertise.
  By applying these strategies, manual testers can maximize their efficiency and contribute to higher [software quality](https://naodeng.com.cn/en/wiki/software-quality).

  - **Prioritize [test cases](https://naodeng.com.cn/en/wiki/test-case)**
    based on risk and impact. Focus on critical functionalities that affect the user experience directly.

  - **Leverage [exploratory testing](https://naodeng.com.cn/en/wiki/exploratory-testing)**
    to uncover issues that scripted tests may miss. This allows testers to use their creativity and intuition.

  - **Use checklists**
    to ensure all areas are covered without the rigidity of formal test cases.

  - **[Pair testing](https://naodeng.com.cn/en/wiki/pair-testing)**
    can be beneficial, where two testers work together to find defects; one operates the software while the other takes notes and thinks of new test scenarios.

  - **Implement [session-based testing](https://naodeng.com.cn/en/wiki/session-based-testing)**
    to manage and track exploratory testing efforts, ensuring accountability and coverage.

  - **Review and refine**
    test cases regularly to remove redundancies and keep them up-to-date with the application changes.

  - **Utilize mind maps**
    to visualize test coverage and identify gaps in testing.

  - **Continuously learn**
    about the application under test; deeper understanding leads to more insightful test scenarios.

  - **Collaborate with developers**
    to gain insights into the code changes that might affect testing.

  - **Gather feedback**
    from stakeholders to align testing efforts with business requirements and user needs.

  - **Automate repetitive tasks**
    that don't require human judgment, such as data setup, to allow more time for actual testing.

  - **Invest in tester training**
    to keep skills sharp and knowledge current, especially in areas like new testing techniques or domain expertise.

#### What are some common mistakes to avoid in manual testing?

  Common mistakes to avoid in [manual testing](https://naodeng.com.cn/en/wiki/manual-testing) include:

  - **Neglecting Test Documentation** : Skipping the creation of detailed test cases and test plans can lead to unstructured testing and missed defects.
  - **Insufficient [Test Coverage](https://naodeng.com.cn/en/wiki/test-coverage)** : Focusing only on happy paths without considering edge cases, error conditions, or negative scenarios can leave critical bugs undetected.
  - **Testing without a Clear Objective** : Executing tests without a clear understanding of the requirements or objectives can result in ineffective testing efforts.
  - **Ignoring User Experience** : Focusing solely on functional aspects and not considering usability can lead to a product that meets requirements but fails to satisfy users.
  - **Overlooking Non-Functional Aspects** : Neglecting performance, security, and compatibility testing can cause significant issues post-release.
  - **Resistance to Repetitive Testing** : Avoiding retesting and regression testing due to monotony can lead to defects slipping through when changes are made.
  - **Not Prioritizing [Test Cases](https://naodeng.com.cn/en/wiki/test-case)** : Failing to prioritize test cases based on risk and impact can result in important tests being left until too late in the cycle.
  - **Poor [Bug](https://naodeng.com.cn/en/wiki/bug) Reporting** : Writing vague or incomplete bug reports can hinder the defect fixing process and lead to misunderstandings.
  - **Testing in Isolation** : Not collaborating with developers, business analysts, and other stakeholders can lead to a lack of shared understanding and missed requirements.
  - **Becoming Biased** : Allowing assumptions or previous knowledge to influence testing can cause testers to overlook defects.
  - **Not Adapting to Changes** : Being inflexible and not updating test cases when requirements change can result in testing that is no longer relevant or effective.
  - **Neglecting Test Documentation** : Skipping the creation of detailed test cases and test plans can lead to unstructured testing and missed defects.
  - **Insufficient [Test Coverage](https://naodeng.com.cn/en/wiki/test-coverage)** : Focusing only on happy paths without considering edge cases, error conditions, or negative scenarios can leave critical bugs undetected.
  - **Testing without a Clear Objective** : Executing tests without a clear understanding of the requirements or objectives can result in ineffective testing efforts.
  - **Ignoring User Experience** : Focusing solely on functional aspects and not considering usability can lead to a product that meets requirements but fails to satisfy users.
  - **Overlooking Non-Functional Aspects** : Neglecting performance, security, and compatibility testing can cause significant issues post-release.
  - **Resistance to Repetitive Testing** : Avoiding retesting and regression testing due to monotony can lead to defects slipping through when changes are made.
  - **Not Prioritizing [Test Cases](https://naodeng.com.cn/en/wiki/test-case)** : Failing to prioritize test cases based on risk and impact can result in important tests being left until too late in the cycle.
  - **Poor [Bug](https://naodeng.com.cn/en/wiki/bug) Reporting** : Writing vague or incomplete bug reports can hinder the defect fixing process and lead to misunderstandings.
  - **Testing in Isolation** : Not collaborating with developers, business analysts, and other stakeholders can lead to a lack of shared understanding and missed requirements.
  - **Becoming Biased** : Allowing assumptions or previous knowledge to influence testing can cause testers to overlook defects.
  - **Not Adapting to Changes** : Being inflexible and not updating test cases when requirements change can result in testing that is no longer relevant or effective.
