# Software Testing


<!-- TOC START -->
- [Questions about Software Testing ?](#questions-about-software-testing)
  - [Basics and Importance](#basics-and-importance)
    - [What is software testing?](#what-is-software-testing)
    - [Why is software testing important?](#why-is-software-testing-important)
    - [What are the different levels of software testing?](#what-are-the-different-levels-of-software-testing)
    - [What is the role of a software tester?](#what-is-the-role-of-a-software-tester)
    - [What is the difference between quality assurance and testing?](#what-is-the-difference-between-quality-assurance-and-testing)
  - [Testing Techniques](#testing-techniques)
    - [What is the difference between white box and black box testing?](#what-is-the-difference-between-white-box-and-black-box-testing)
    - [What is grey box testing?](#what-is-grey-box-testing)
    - [What is static testing and dynamic testing?](#what-is-static-testing-and-dynamic-testing)
    - [What is exploratory testing?](#what-is-exploratory-testing)
    - [What is the difference between functional and non-functional testing?](#what-is-the-difference-between-functional-and-non-functional-testing)
  - [Testing Tools and Automation](#testing-tools-and-automation)
    - [What is automated testing?](#what-is-automated-testing)
    - [What are the benefits of automated testing?](#what-are-the-benefits-of-automated-testing)
    - [What are some popular tools for automated testing?](#what-are-some-popular-tools-for-automated-testing)
    - [What is the difference between Selenium and QTP?](#what-is-the-difference-between-selenium-and-qtp)
    - [What is the role of Jenkins in testing?](#what-is-the-role-of-jenkins-in-testing)
  - [Test Management](#test-management)
    - [What is a test case?](#what-is-a-test-case)
    - [What is a test plan?](#what-is-a-test-plan)
    - [What is a test suite?](#what-is-a-test-suite)
    - [What is defect management?](#what-is-defect-management)
    - [What is the role of a test manager?](#what-is-the-role-of-a-test-manager)
  - [Advanced Concepts](#advanced-concepts)
    - [What is performance testing?](#what-is-performance-testing)
    - [What is load testing?](#what-is-load-testing)
    - [What is stress testing?](#what-is-stress-testing)
    - [What is usability testing?](#what-is-usability-testing)
    - [What is security testing?](#what-is-security-testing)
<!-- TOC END -->

Software testing

confirms that a software product or application functions correctly, achieves its intended goals, and is free of defects.

## Questions about Software Testing ?

### Basics and Importance

#### What is software testing?

  [Software testing](../S/software-testing.md) is the **process of evaluating** and **verifying** that a software application or system does what it is supposed to do. The purpose of testing can be assurance of quality, [verification](../V/verification.md) of functionality, performance evaluation, or finding defects. Testing involves the execution of a software component or system component to evaluate one or more properties of interest.
  In the context of [test automation](../T/test-automation.md), [software testing](../S/software-testing.md) typically refers to the use of **automated tools and frameworks** to execute pre-scripted tests on a software application before it is released into production. Automated tests can range from simple unit tests that verify individual functions to complex end-to-end tests that validate integrated system workflows.
  The goal of [automated testing](../A/automated-testing.md) is to **increase efficiency**, **reduce [test execution](../T/test-execution.md) time**, and provide **consistent [test coverage](../T/test-coverage.md)**. It is particularly useful for [regression testing](../R/regression-testing.md), which ensures that new changes do not introduce new defects into existing functionality. Automated tests can be run frequently and can be integrated into the continuous integration and deployment pipeline, allowing for early detection of issues and faster feedback to developers.

  ```
  // Example of a simple automated test case in TypeScript
  describe('Login Functionality', () => {
    it('should authenticate user with valid credentials', () => {
      const result = login('validUser', 'validPassword');
      expect(result).toBe(true);
    });
  });
  ```
  [Automated testing](../A/automated-testing.md) requires careful planning and design to be effective and should be maintained as the software evolves to ensure continued relevance and effectiveness.

#### Why is software testing important?

  [Software testing](../S/software-testing.md) is crucial because it ensures that software functions **correctly**, **safely**, and **efficiently** before it is deployed to users. It identifies defects and errors that may have been introduced during the development phase, improving the **quality** of the software and the **user experience**. Testing also verifies that software requirements are met and helps maintain **consistency** across different devices and platforms.
  Moreover, testing is essential for **risk management**, as it can prevent costly and potentially dangerous failures in real-world operation. It can also lead to **cost savings** in the long run by catching issues early, thereby reducing the need for patches and extensive maintenance after release.
  In the context of **regulatory compliance**, certain industries require software to meet specific standards before it can be released. Testing ensures compliance and avoids legal issues that might arise from releasing non-compliant software.
  Finally, in a competitive market, the **reputation** of a company can be significantly affected by the quality of its software products. Effective testing helps in building customer trust and loyalty by delivering a reliable and high-performing product.
  In summary, [software testing](../S/software-testing.md) is an indispensable part of the software development lifecycle that contributes to the delivery of high-quality software, which in turn leads to customer satisfaction, reduced costs, and a strong market reputation.

#### What are the different levels of software testing?

  Different levels of [software testing](../S/software-testing.md) ensure that every aspect of the software is examined and validated at various stages of the development lifecycle. These levels include:

  - **[Unit Testing](../U/unit-testing.md)**: Focuses on individual components or units of code to verify that each one functions correctly in isolation. Typically, developers write and run these tests using frameworks like JUnit or [NUnit](../N/nunit.md).
  - **[Integration Testing](../I/integration-testing.md)**: Tests the interactions between integrated units or components to detect interface defects. This can be done using an incremental approach (combining units one by one) or by using stubs and drivers.
  - **[System Testing](../S/system-testing.md)**: Validates the complete and fully integrated software product to ensure it meets the specified requirements. This level encompasses a wide range of testing types, including functional and non-functional tests.
  - **[Acceptance Testing](../A/acceptance-testing.md)**: Conducted to determine whether the system is ready for release, often involving stakeholders or end-users. It includes verifying the system against user requirements and can be subdivided into Alpha and [Beta testing](../B/beta-testing.md) phases.
  - **[Regression Testing](../R/regression-testing.md)**: Performed after changes (like enhancements, patches, or configuration changes) to the software to ensure that existing functionality remains unaffected. This is where [test automation](../T/test-automation.md) is particularly beneficial to repeatedly run a set of [test cases](../T/test-case.md).
  Each level builds upon the previous one, ensuring that issues are caught and resolved as early as possible in the development process. [Test automation](../T/test-automation.md) can be applied at all these levels to improve efficiency and reliability.

  - **[Unit Testing](../U/unit-testing.md)**: Focuses on individual components or units of code to verify that each one functions correctly in isolation. Typically, developers write and run these tests using frameworks like JUnit or [NUnit](../N/nunit.md).
  - **[Integration Testing](../I/integration-testing.md)**: Tests the interactions between integrated units or components to detect interface defects. This can be done using an incremental approach (combining units one by one) or by using stubs and drivers.
  - **[System Testing](../S/system-testing.md)**: Validates the complete and fully integrated software product to ensure it meets the specified requirements. This level encompasses a wide range of testing types, including functional and non-functional tests.
  - **[Acceptance Testing](../A/acceptance-testing.md)**: Conducted to determine whether the system is ready for release, often involving stakeholders or end-users. It includes verifying the system against user requirements and can be subdivided into Alpha and [Beta testing](../B/beta-testing.md) phases.
  - **[Regression Testing](../R/regression-testing.md)**: Performed after changes (like enhancements, patches, or configuration changes) to the software to ensure that existing functionality remains unaffected. This is where [test automation](../T/test-automation.md) is particularly beneficial to repeatedly run a set of [test cases](../T/test-case.md).

#### What is the role of a software tester?

  The role of a **software tester** involves designing, developing, and executing [test cases](../T/test-case.md) to verify software functionality against requirements. Testers ensure that the software behaves as expected under various conditions by conducting different types of tests, such as unit, integration, system, and [acceptance testing](../A/acceptance-testing.md). They are responsible for identifying defects, reporting them to the development team, and verifying fixes once implemented.
  Software testers also play a crucial role in the **[test automation](../T/test-automation.md)** process. They write automation scripts using languages and frameworks suitable for the application under test. Testers maintain and improve existing [test automation](../T/test-automation.md) infrastructure, ensuring that automated tests are integrated into the continuous integration and delivery pipeline. They must select appropriate tools for [test case management](../T/test-case-management.md), defect tracking, and reporting to enhance the testing process.
  In addition to technical tasks, testers collaborate with developers, product managers, and stakeholders to understand requirements and ensure that quality standards are met throughout the software development lifecycle. They provide valuable feedback on product usability, performance, and security, contributing to the overall quality of the final product.
  Testers must continuously update their skills to keep pace with evolving testing methodologies and tools. They are expected to advocate for best practices in testing and contribute to the development of a culture that prioritizes quality in software development.

#### What is the difference between quality assurance and testing?

  [Quality Assurance](../Q/quality-assurance.md) (QA) and testing are closely related concepts in software development, but they serve distinct purposes.
  **QA** is a proactive process that focuses on preventing defects by ensuring that the processes used to manage and create deliverables are adequate and effective. It encompasses the entire software development lifecycle and aims to improve the development and test processes so that defects do not arise when the product is being developed. QA activities include process definition and implementation, training, audits, and process improvement initiatives.
  **Testing**, on the other hand, is a reactive process and a subset of QA. It involves the actual execution of a system or application with the intent to find software [bugs](../B/bug.md). Testing is about [verification](../V/verification.md) and validation - ensuring that the software meets the business and technical requirements that guided its design and development and that it works as expected.
  In essence, QA is about **process** and **prevention**, while testing is about **product** and **detection**. QA aims to improve and stabilize production (and its processes) to avoid issues that lead to defects, while testing aims to identify defects in the product itself. Testing is a key activity within the broader QA process, which is concerned with the overall [quality management](../Q/quality-management.md) of the software and the development process.

### Testing Techniques

#### What is the difference between white box and black box testing?

  [White box testing](../W/white-box-testing.md), also known as clear, glass, or [structural testing](../S/structural-testing.md), involves testing the internal structures or workings of an application, as opposed to its functionality. In [white box testing](../W/white-box-testing.md), [test cases](../T/test-case.md) are derived based on an application's internal code paths, code structures, and the implementation of the software itself. Testers require knowledge of the internal code and are typically developers or testers with development skills.
  [Black box testing](../B/black-box-testing.md), on the other hand, treats the software as a "black box"—without any knowledge of internal implementation. [Test cases](../T/test-case.md) are written based on the software's specifications and requirements. [Black box testing](../B/black-box-testing.md) focuses on testing the software with various inputs and validating the outputs against the expected outcomes. It is typically performed by testers who do not need to know the coding or internal structure of the application.
  In summary, **[white box testing](../W/white-box-testing.md)** is code-based testing where testers need to understand the internal workings of the application, while **[black box testing](../B/black-box-testing.md)** is input/output-driven testing that does not require knowledge of the code. The choice between the two depends on the testing objectives, with [white box testing](../W/white-box-testing.md) being suitable for algorithm testing, security, and optimization, and [black box testing](../B/black-box-testing.md) being ideal for validation and [verification](../V/verification.md) of software behavior.

#### What is grey box testing?

  [Grey box testing](../G/grey-box-testing.md) is a hybrid approach that combines elements of both **black box** and **[white box testing](../W/white-box-testing.md)** methodologies. It requires partial knowledge of the internal workings of the application, which allows testers to design [test cases](../T/test-case.md) with a better understanding of the system. This approach is particularly useful when testing web applications.
  In [grey box testing](../G/grey-box-testing.md), testers have access to detailed design documents and [database](../D/database.md) schemas but do not have full visibility of the source code. They use this information to create tests that cover both the application's user interface and its underlying structures, such as [databases](../D/database.md) and servers.
  Testers might use tools like **debuggers** or **monitoring systems** to observe the behavior of the application during [test execution](../T/test-execution.md). This allows them to identify issues related to data flow and exception handling that would not be as easily found through [black box testing](../B/black-box-testing.md) alone.
  [Grey box testing](../G/grey-box-testing.md) is effective for **[integration testing](../I/integration-testing.md)**, **[security testing](../S/security-testing.md)**, and **networking testing**. It helps in identifying issues related to data communication, user permissions, and session management, which are critical for the overall security and performance of the application.
  By leveraging the strengths of both black box and [white box testing](../W/white-box-testing.md), [grey box testing](../G/grey-box-testing.md) provides a more comprehensive understanding of the application's behavior and potential vulnerabilities. It is a strategic choice for [test automation](../T/test-automation.md) engineers looking to optimize [test coverage](../T/test-coverage.md) and efficiency.

#### What is static testing and dynamic testing?

  [Static testing](../S/static-testing.md) and [dynamic testing](../D/dynamic-testing.md) are two methodologies used to detect defects in software applications.
  **[Static testing](../S/static-testing.md)** involves examining the code, requirements, or documentation **without executing** the program. It's typically done in the earlier stages of the development lifecycle. Techniques include reviews, walkthroughs, [inspections](../I/inspection.md), and desk-checking. Static analysis tools can also be used to automatically evaluate code against coding standards, find potential [bugs](../B/bug.md), and ensure compliance with best practices.
  **[Dynamic testing](../D/dynamic-testing.md)**, on the other hand, requires the code to be **executed**. It verifies the functional behavior of the software by running it under various conditions. This type of testing checks for the correct output from given inputs and is performed in an environment that simulates real-world use. [Dynamic testing](../D/dynamic-testing.md) can be further categorized into [unit testing](../U/unit-testing.md), [integration testing](../I/integration-testing.md), [system testing](../S/system-testing.md), and [acceptance testing](../A/acceptance-testing.md).
  Both testing types are complementary. [Static testing](../S/static-testing.md) helps identify issues early, which can be more cost-effective to fix, while [dynamic testing](../D/dynamic-testing.md) validates the software's operational behavior and performance under stress. Combining both approaches ensures a more thorough evaluation of the software's quality.

#### What is exploratory testing?

  [Exploratory testing](../E/exploratory-testing.md) is an approach to [software testing](../S/software-testing.md) that emphasizes the personal freedom and responsibility of the individual tester to continually optimize the quality of their work by treating test-related learning, test design, [test execution](../T/test-execution.md), and test result interpretation as mutually supportive activities that run in parallel throughout the project. It contrasts with more traditional, scripted testing where [test cases](../T/test-case.md) are designed in advance, specifying both the steps to be taken and the expected outcome in detail.
  In [exploratory testing](../E/exploratory-testing.md), testers are not constrained by a predefined set of [test cases](../T/test-case.md), allowing them to probe the software more creatively and responsively. They explore the application by designing and executing tests on-the-fly and learning about the system's behavior and risks as they progress. This approach is particularly useful when there are no or limited specifications or in complex, changing environments where it is difficult to predict how the software should behave in all situations.
  Testers use their skills, experience, and intuition to discover, investigate, and learn about the system. They may use tools to assist in testing, but the core of [exploratory testing](../E/exploratory-testing.md) is the tester's active engagement with the product, often documenting their findings and ideas as they go, rather than following a pre-scripted plan.
  [Exploratory testing](../E/exploratory-testing.md) is not random testing; it is a structured and thoughtful process that relies on the tester's intelligence, creativity, and insights about what is most important to examine at any given moment. It is often used in conjunction with other testing methods to ensure a well-rounded testing process.

#### What is the difference between functional and non-functional testing?

  [Functional testing](../F/functional-testing.md) focuses on evaluating the **compliance** of a system's behavior with specified requirements by testing features and operational aspects. It answers the question, "Does the software do what it's supposed to do?" Examples include unit, integration, system, and [acceptance testing](../A/acceptance-testing.md).
  [Non-functional testing](../N/non-functional-testing.md), on the other hand, assesses the **readiness** of a system according to criteria not covered by [functional requirements](../F/functional-requirements.md). It evaluates characteristics like performance, usability, reliability, and security. This form of testing answers questions like, "How well does the software perform?" or "How secure is the software?" Common types include performance, load, stress, usability, and [security testing](../S/security-testing.md).
  While functional tests validate specific actions and responses of the application, non-functional tests measure the application's overall operation under various conditions. Both are critical for ensuring a comprehensive understanding of the software's quality.

### Testing Tools and Automation

#### What is automated testing?

  [Automated testing](../A/automated-testing.md) is the process of executing **[test cases](../T/test-case.md)** using software tools that run pre-scripted tests on a software application without manual intervention. This method is used to validate the functionality, reliability, and stability of software products. Automated tests can be run repeatedly at any time of day, providing immediate feedback to the development team.
  Here's a basic example in TypeScript using a hypothetical testing framework:

  ```
  describe('Login Functionality', () => {
    it('should authenticate user with valid credentials', () => {
      const loginPage = new LoginPage();
      loginPage.enterUsername('validUser');
      loginPage.enterPassword('validPass');
      loginPage.submit();
      expect(loginPage.isLoginSuccessful()).toBeTruthy();
    });
  });
  ```
  In this example, a **[test script](../T/test-script.md)** is written to automate the process of testing a login functionality. The script navigates to the login page, enters valid credentials, submits the form, and verifies that the login was successful.
  [Automated testing](../A/automated-testing.md) is particularly useful for **[regression testing](../R/regression-testing.md)**, which ensures that new changes do not break existing functionality. It's also beneficial for executing **complex [test cases](../T/test-case.md)** that are difficult to perform manually, or for tests that need to be run on multiple platforms and devices. However, it's not a silver bullet; automated tests require maintenance as the application evolves, and they can be initially costly to set up.

#### What are the benefits of automated testing?

  [Automated testing](../A/automated-testing.md) offers several benefits that can significantly enhance the efficiency and effectiveness of the software development lifecycle:

  - **Consistency and Accuracy** : Automation ensures tests are performed identically every time, eliminating human error.
  - **Speed** : Automated tests run much faster than manual tests, enabling quicker feedback and faster development cycles.
  - **Increased Coverage** : Automation can easily increase the scope and depth of tests, improving software quality.
  - **Reusability** : Test scripts are reusable across different versions of the application, even if the user interface changes.
  - **Efficiency** : Once created, automated tests can be run any number of times with minimal additional cost.
  - **Early [Bug](../B/bug.md) Detection** : Automated tests can be integrated into the continuous integration pipeline, allowing for early detection of defects.
  - **Parallel Execution** : Tests can be run in parallel on different machines, reducing the time needed for execution.
  - **Cost Reduction** : While there's an initial investment, over time, automated testing reduces the cost of testing by decreasing the effort required for each test cycle.
  - **Improved Reporting** : Automated tools can generate detailed logs and reports, providing insights into test execution and outcomes.
  - **Better Resource Allocation** : Automation frees up QA engineers to focus on more complex testing tasks that require human judgment.
  These benefits contribute to a more robust, efficient, and reliable software development process, ultimately leading to a higher quality product.

  - **Consistency and Accuracy** : Automation ensures tests are performed identically every time, eliminating human error.
  - **Speed** : Automated tests run much faster than manual tests, enabling quicker feedback and faster development cycles.
  - **Increased Coverage** : Automation can easily increase the scope and depth of tests, improving software quality.
  - **Reusability** : Test scripts are reusable across different versions of the application, even if the user interface changes.
  - **Efficiency** : Once created, automated tests can be run any number of times with minimal additional cost.
  - **Early [Bug](../B/bug.md) Detection** : Automated tests can be integrated into the continuous integration pipeline, allowing for early detection of defects.
  - **Parallel Execution** : Tests can be run in parallel on different machines, reducing the time needed for execution.
  - **Cost Reduction** : While there's an initial investment, over time, automated testing reduces the cost of testing by decreasing the effort required for each test cycle.
  - **Improved Reporting** : Automated tools can generate detailed logs and reports, providing insights into test execution and outcomes.
  - **Better Resource Allocation** : Automation frees up QA engineers to focus on more complex testing tasks that require human judgment.

#### What are some popular tools for automated testing?

  Popular tools for [automated testing](../A/automated-testing.md) include:

  - **[Selenium](../S/selenium.md)** : An open-source tool that supports multiple languages and browsers. It's widely used for web application testing.
  - **Appium** : An open-source tool for mobile application testing. It supports both iOS and Android platforms.
  - **JUnit**
    and
    **TestNG** : Frameworks for unit testing in Java. They offer annotations to identify test methods and various other features to organize tests.

  - **[Cypress](../C/cypress.md)** : A modern JavaScript-based end-to-end testing framework that runs in the browser.
  - **[Postman](../P/postman.md)** : A tool for API testing, which allows for easy creation and execution of API requests and automated tests.
  - **Cucumber** : Supports Behavior-Driven Development (BDD) with a plain language parser that allows for test script writing in natural language.
  - **Robot Framework** : A keyword-driven test automation framework for acceptance level testing and acceptance test-driven development (ATDD).
  - **SpecFlow** : A .NET tool for BDD that uses the Gherkin language to create human-readable tests.
  - **HP UFT (formerly QTP)** : A commercial tool for functional and regression testing with a visual interface for test automation.
  - **SoapUI** : A tool for testing SOAP and REST web services, focusing on API testing.
  - **LoadRunner** : A performance testing tool by Micro Focus that simulates user activity for load, stress, and scalability testing.
  - **[JMeter](../J/jmeter.md)** : An open-source tool designed for load testing and measuring performance.
  Each tool has its own strengths and is chosen based on the specific requirements of the project, such as the type of application under test, the programming languages involved, and the preferred testing methodologies.

  - **[Selenium](../S/selenium.md)** : An open-source tool that supports multiple languages and browsers. It's widely used for web application testing.
  - **Appium** : An open-source tool for mobile application testing. It supports both iOS and Android platforms.
  - **JUnit**
    and
    **TestNG** : Frameworks for unit testing in Java. They offer annotations to identify test methods and various other features to organize tests.

  - **[Cypress](../C/cypress.md)** : A modern JavaScript-based end-to-end testing framework that runs in the browser.
  - **[Postman](../P/postman.md)** : A tool for API testing, which allows for easy creation and execution of API requests and automated tests.
  - **Cucumber** : Supports Behavior-Driven Development (BDD) with a plain language parser that allows for test script writing in natural language.
  - **Robot Framework** : A keyword-driven test automation framework for acceptance level testing and acceptance test-driven development (ATDD).
  - **SpecFlow** : A .NET tool for BDD that uses the Gherkin language to create human-readable tests.
  - **HP UFT (formerly QTP)** : A commercial tool for functional and regression testing with a visual interface for test automation.
  - **SoapUI** : A tool for testing SOAP and REST web services, focusing on API testing.
  - **LoadRunner** : A performance testing tool by Micro Focus that simulates user activity for load, stress, and scalability testing.
  - **[JMeter](../J/jmeter.md)** : An open-source tool designed for load testing and measuring performance.

#### What is the difference between Selenium and QTP?

  [Selenium](../S/selenium.md) and QTP (QuickTest Professional), now known as UFT (Unified [Functional Testing](../F/functional-testing.md)), are both automation tools used for testing web applications, but they differ in several aspects:

  - **Open Source vs. Commercial**: [Selenium](../S/selenium.md) is an open-source tool, which means it is free to use and can be modified by anyone. UFT, on the other hand, is a commercial product developed by Micro Focus and requires a paid license.
  - **Language Support**: [Selenium](../S/selenium.md) supports multiple programming languages like Java, C#, Python, Ruby, and JavaScript, allowing for flexibility in [test script](../T/test-script.md) development. UFT primarily uses VBScript.
  - **Browser Compatibility**: [Selenium](../S/selenium.md) supports a wide range of browsers including Chrome, Firefox, Internet Explorer, Safari, and Opera. UFT has more limited browser support.
  - **Operating System Support**: [Selenium](../S/selenium.md) can run on various operating systems such as Windows, macOS, and Linux. UFT is mostly limited to Windows.
  - **Integration with Other Tools**: [Selenium](../S/selenium.md) easily integrates with other tools like Jenkins for CI/CD, and it can be used with various frameworks like TestNG or JUnit. UFT has built-in integration features but might not offer the same level of flexibility.
  - **Community and Support**: Being open-source, [Selenium](../S/selenium.md) has a large community for support and collaboration. UFT, being proprietary, relies on official support from Micro Focus and might have a smaller user community.
  - **IDE Support**: [Selenium](../S/selenium.md) has an IDE plugin for browsers for record-and-playback features, while UFT comes with a full-fledged IDE.
  - **Mobile Testing**: [Selenium](../S/selenium.md) can be extended to mobile testing with Appium. UFT has a sister tool, UFT Mobile, for mobile testing.
  In summary, the choice between [Selenium](../S/selenium.md) and UFT may depend on factors like budget, language preference, browser support, and the need for a robust commercial support structure.

  - **Open Source vs. Commercial**: [Selenium](../S/selenium.md) is an open-source tool, which means it is free to use and can be modified by anyone. UFT, on the other hand, is a commercial product developed by Micro Focus and requires a paid license.
  - **Language Support**: [Selenium](../S/selenium.md) supports multiple programming languages like Java, C#, Python, Ruby, and JavaScript, allowing for flexibility in [test script](../T/test-script.md) development. UFT primarily uses VBScript.
  - **Browser Compatibility**: [Selenium](../S/selenium.md) supports a wide range of browsers including Chrome, Firefox, Internet Explorer, Safari, and Opera. UFT has more limited browser support.
  - **Operating System Support**: [Selenium](../S/selenium.md) can run on various operating systems such as Windows, macOS, and Linux. UFT is mostly limited to Windows.
  - **Integration with Other Tools**: [Selenium](../S/selenium.md) easily integrates with other tools like Jenkins for CI/CD, and it can be used with various frameworks like TestNG or JUnit. UFT has built-in integration features but might not offer the same level of flexibility.
  - **Community and Support**: Being open-source, [Selenium](../S/selenium.md) has a large community for support and collaboration. UFT, being proprietary, relies on official support from Micro Focus and might have a smaller user community.
  - **IDE Support**: [Selenium](../S/selenium.md) has an IDE plugin for browsers for record-and-playback features, while UFT comes with a full-fledged IDE.
  - **Mobile Testing**: [Selenium](../S/selenium.md) can be extended to mobile testing with Appium. UFT has a sister tool, UFT Mobile, for mobile testing.

#### What is the role of Jenkins in testing?

  Jenkins plays a crucial role in **continuous integration (CI)** and **continuous delivery (CD)** pipelines, automating the execution of [test suites](../T/test-suite.md) and providing immediate feedback on the health of the software. It can be configured to trigger tests on various events, such as a commit to a version control system or on a scheduled basis.
  With Jenkins, you can:

  - **Automate [test execution](../T/test-execution.md)** : Run tests automatically on code changes to quickly identify issues.
  - **Parallelize tests** : Execute tests in parallel to reduce the time taken for the test suite to run.
  - **Manage [test environments](../T/test-environment.md)** : Set up and tear down test environments as part of the pipeline.
  - **Integrate with [test tools](../T/test-tool.md)** : Connect with a variety of testing frameworks and tools using plugins.
  - **Visualize test results** : Generate reports and dashboards to analyze test outcomes.
  - **Notify stakeholders** : Send notifications on test results to developers and teams.
  Example of a Jenkins pipeline script to run tests:

  ```
  pipeline {
      agent any
      stages {
          stage('Build') {
              steps {
                  // Build your application
              }
          }
          stage('Test') {
              steps {
                  // Run your test suite
                  sh 'execute-tests.sh'
              }
              post {
                  always {
                      // Collect and archive test reports
                      junit '**/target/surefire-reports/TEST-*.xml'
                  }
              }
          }
      }
  }
  ```
  In essence, Jenkins enhances the testing process by automating it, thus ensuring that [software quality](../S/software-quality.md) is assessed continuously and issues are detected and addressed promptly.

  - **Automate [test execution](../T/test-execution.md)** : Run tests automatically on code changes to quickly identify issues.
  - **Parallelize tests** : Execute tests in parallel to reduce the time taken for the test suite to run.
  - **Manage [test environments](../T/test-environment.md)** : Set up and tear down test environments as part of the pipeline.
  - **Integrate with [test tools](../T/test-tool.md)** : Connect with a variety of testing frameworks and tools using plugins.
  - **Visualize test results** : Generate reports and dashboards to analyze test outcomes.
  - **Notify stakeholders** : Send notifications on test results to developers and teams.

### Test Management

#### What is a test case?

  A **[test case](../T/test-case.md)** is a set of conditions or variables under which a tester will determine whether an application or software system is working correctly. It's essentially a specific scenario comprising a sequence of steps, [expected results](../E/expected-result.md), and [actual results](../A/actual-result.md), designed to verify a particular function or feature of the software.
  Each [test case](../T/test-case.md) includes:

  - **[Test Case](../T/test-case.md) ID** : A unique identifier for tracking.
  - **Description** : A brief about what is being tested.
  - **Preconditions** : Any requirements that must be met before execution.
  - **Test Steps** : Detailed instructions for execution.
  - **[Expected Result](../E/expected-result.md)** : The anticipated outcome if the software operates correctly.
  - **[Actual Result](../A/actual-result.md)** : The behavior observed when the test is executed.
  - **[Postconditions](../P/postcondition.md)** : The state of the system after test execution.
  - **Status** : Pass or fail based on whether the actual result matches the expected result.
  [Test cases](../T/test-case.md) are fundamental in both manual and [automated testing](../A/automated-testing.md), providing a clear framework for testers to validate software functionality. In [automated testing](../A/automated-testing.md), [test cases](../T/test-case.md) are scripted using tools and languages specific to the testing environment, such as [Selenium](../S/selenium.md) with Java or Python, and can be executed repeatedly without manual intervention.

  ```
  // Example of a simple automated test case in TypeScript using a testing framework
  describe('Login Functionality', () => {
    it('should log in with valid credentials', () => {
      browser.url('https://example.com/login');
      $('#username').setValue('testuser');
      $('#password').setValue('testpass');
      $('#login').click();
      expect(browser).toHaveUrl('https://example.com/dashboard');
    });
  });
  ```
  Well-designed [test cases](../T/test-case.md) are crucial for effective [test coverage](../T/test-coverage.md) and ensuring that the software meets its requirements.

  - **[Test Case](../T/test-case.md) ID** : A unique identifier for tracking.
  - **Description** : A brief about what is being tested.
  - **Preconditions** : Any requirements that must be met before execution.
  - **Test Steps** : Detailed instructions for execution.
  - **[Expected Result](../E/expected-result.md)** : The anticipated outcome if the software operates correctly.
  - **[Actual Result](../A/actual-result.md)** : The behavior observed when the test is executed.
  - **[Postconditions](../P/postcondition.md)** : The state of the system after test execution.
  - **Status** : Pass or fail based on whether the actual result matches the expected result.

#### What is a test plan?

  A **[test plan](../T/test-plan.md)** is a formal document detailing the strategy, resources, scope, and schedule of intended test activities. It defines the objectives and milestones of the testing phase within a project and serves as a blueprint for action. A [test plan](../T/test-plan.md) typically includes:

  - **Test objectives** : Clear goals for what the testing should achieve.
  - **Test scope** : The features to be tested and the ones to be excluded.
  - **[Test strategy](../T/test-strategy.md)** : The high-level approach to be taken for testing.
  - **Resource allocation** : Assignment of personnel and tools for test execution.
  - **[Test environment](../T/test-environment.md)** : Specifications of the hardware and software where tests will be executed.
  - **Test schedule** : Timelines for test preparation, execution, and evaluation.
  - **Risk analysis** : Potential risks in the testing process and mitigation plans.
  - **Entry and exit criteria** : Conditions that must be met to start and conclude testing phases.
  - **Deliverables** : Artifacts to be produced, such as test cases, reports, and defect logs.
  It's a guide that aligns the test team's work with the project's objectives and ensures that critical aspects of the software are verified systematically. A well-crafted [test plan](../T/test-plan.md) is essential for efficient [test management](../T/test-management.md) and serves as a reference point throughout the testing process.

  - **Test objectives** : Clear goals for what the testing should achieve.
  - **Test scope** : The features to be tested and the ones to be excluded.
  - **[Test strategy](../T/test-strategy.md)** : The high-level approach to be taken for testing.
  - **Resource allocation** : Assignment of personnel and tools for test execution.
  - **[Test environment](../T/test-environment.md)** : Specifications of the hardware and software where tests will be executed.
  - **Test schedule** : Timelines for test preparation, execution, and evaluation.
  - **Risk analysis** : Potential risks in the testing process and mitigation plans.
  - **Entry and exit criteria** : Conditions that must be met to start and conclude testing phases.
  - **Deliverables** : Artifacts to be produced, such as test cases, reports, and defect logs.

#### What is a test suite?

  A **[test suite](../T/test-suite.md)** is a collection of **[test cases](../T/test-case.md)** that are grouped together to test a software application or a specific functionality within the application. In [automated testing](../A/automated-testing.md), a [test suite](../T/test-suite.md) can be executed by a [test runner](../T/test-runner.md) and is often structured in a way that allows for batch execution of multiple tests. It serves as a container for tests that are logically related, either by their testing purpose, such as a feature set, or by their level, such as integration or [system testing](../S/system-testing.md).
  [Test suites](../T/test-suite.md) are typically organized in a hierarchy, with the suite at the top level and individual [test cases](../T/test-case.md) or smaller suites beneath it. This allows for better management and execution of tests, as well as the aggregation of test results. [Test suites](../T/test-suite.md) can be designed to run as part of continuous integration (CI) pipelines, enabling regular feedback on the health of the codebase.
  In code, a [test suite](../T/test-suite.md) might be represented as a class or module, depending on the programming language and testing framework used. For example, in a Java-based framework like JUnit, a [test suite](../T/test-suite.md) could be annotated with `@RunWith(Suite.class)` and include a list of test classes to run:

  ```
  @RunWith(Suite.class)
  @Suite.SuiteClasses({
      TestClassOne.class,
      TestClassTwo.class
  })
  public class ExampleTestSuite {
      // This class remains empty, it is used only as a holder for the above annotations
  }
  ```
  [Test suites](../T/test-suite.md) are essential for organizing and maintaining a large number of automated tests, making them more maintainable and scalable. They also facilitate targeted testing and can be used to group tests for specific test runs, such as smoke testing or [regression testing](../R/regression-testing.md).

#### What is defect management?

  [Defect management](../D/defect-management.md) is the systematic process of identifying, documenting, tracking, and resolving defects in a software product. It begins when a defect is discovered and continues until it is either fixed and verified or deemed irrelevant and dismissed. Effective [defect management](../D/defect-management.md) involves several key steps:

  - **Identification** : Recognizing a defect through testing or user feedback.
  - **Documentation** : Recording the defect with sufficient detail, including steps to reproduce, severity, and potential impact.
  - **Prioritization** : Assessing the defect's urgency and importance to determine the order in which defects should be addressed.
  - **Assignment** : Allocating the defect to the appropriate team or individual for resolution.
  - **Resolution** : Correcting the defect through code changes or configuration adjustments.
  - **[Verification](../V/verification.md)** : Testing the fix to ensure the defect is resolved and has not introduced new issues.
  - **Closure** : Officially closing the defect once it is verified and meets the acceptance criteria.
  Throughout this process, communication and collaboration among team members are crucial. [Defect management](../D/defect-management.md) tools facilitate this by providing a centralized platform for tracking and managing defects. These tools often integrate with other software development and testing tools, enabling a seamless workflow from defect discovery to resolution.
  In the context of [test automation](../T/test-automation.md), [defect management](../D/defect-management.md) ensures that automated tests remain effective in catching regressions and that any new defects introduced by code changes are promptly addressed, maintaining the software's overall quality and reliability.

  - **Identification** : Recognizing a defect through testing or user feedback.
  - **Documentation** : Recording the defect with sufficient detail, including steps to reproduce, severity, and potential impact.
  - **Prioritization** : Assessing the defect's urgency and importance to determine the order in which defects should be addressed.
  - **Assignment** : Allocating the defect to the appropriate team or individual for resolution.
  - **Resolution** : Correcting the defect through code changes or configuration adjustments.
  - **[Verification](../V/verification.md)** : Testing the fix to ensure the defect is resolved and has not introduced new issues.
  - **Closure** : Officially closing the defect once it is verified and meets the acceptance criteria.

#### What is the role of a test manager?

  The **test manager** plays a crucial role in overseeing the testing process and ensuring that the software meets quality standards. Their responsibilities include:

  - **Strategizing**
    the overall test approach and methodology.

  - **Planning**
    and
    **scheduling**
    testing activities, ensuring resources are allocated effectively.

  - **Managing**
    the test team, including hiring, training, and mentoring testers.

  - **Coordinating**
    with other teams, such as development and operations, to ensure alignment and integration of testing within the software development lifecycle.

  - **Monitoring**
    and
    **reporting**
    on testing progress, test coverage, and the status of defects.

  - **Risk management**
    , identifying potential quality issues and taking proactive steps to mitigate them.

  - **Budgeting**
    for testing activities, including tools, environments, and personnel.

  - **Ensuring**
    compliance with industry standards and regulatory requirements.

  - **Evaluating**
    and
    **implementing**
    test tools and technologies to enhance testing efficiency and effectiveness.

  - **Maintaining**
    and
    **improving**
    the test environment and infrastructure.
  Test managers must possess a deep understanding of [software testing](../S/software-testing.md) principles and practices, as well as strong leadership and communication skills to effectively guide their teams and interact with stakeholders. They play a pivotal role in the success of [test automation](../T/test-automation.md) efforts by ensuring that the right processes, tools, and people are in place to deliver high-quality software.

  - **Strategizing**
    the overall test approach and methodology.

  - **Planning**
    and
    **scheduling**
    testing activities, ensuring resources are allocated effectively.

  - **Managing**
    the test team, including hiring, training, and mentoring testers.

  - **Coordinating**
    with other teams, such as development and operations, to ensure alignment and integration of testing within the software development lifecycle.

  - **Monitoring**
    and
    **reporting**
    on testing progress, test coverage, and the status of defects.

  - **Risk management**
    , identifying potential quality issues and taking proactive steps to mitigate them.

  - **Budgeting**
    for testing activities, including tools, environments, and personnel.

  - **Ensuring**
    compliance with industry standards and regulatory requirements.

  - **Evaluating**
    and
    **implementing**
    test tools and technologies to enhance testing efficiency and effectiveness.

  - **Maintaining**
    and
    **improving**
    the test environment and infrastructure.

### Advanced Concepts

#### What is performance testing?

  [Performance testing](../P/performance-testing.md) is a type of [non-functional testing](../N/non-functional-testing.md) that evaluates how a system performs under various conditions. It primarily focuses on **speed**, **scalability**, **reliability**, and **resource usage** of software applications. Performance tests are designed to simulate different scenarios, including high user loads, limited computational resources, and large data input/output, to identify potential bottlenecks and ensure the software meets performance criteria.
  Key sub-types of [performance testing](../P/performance-testing.md) include:

  - **[Load Testing](../L/load-testing.md)** : Determines how the system behaves under expected user loads.
  - **[Stress Testing](../S/stress-testing.md)** : Assesses system stability under extreme conditions.
  - **[Endurance Testing](../E/endurance-testing.md)** : Checks system performance with a normal workload over an extended period.
  - **Spike Testing** : Evaluates system reaction to sudden large spikes in user load.
  - **[Volume Testing](../V/volume-testing.md)** : Tests the system’s ability to handle large volumes of data.
  - **[Scalability Testing](../S/scalability-testing.md)** : Determines if the system can scale up or out and the effects on performance.
  [Performance testing](../P/performance-testing.md) tools often provide metrics such as response times, throughput rates, and resource utilization levels, which help in identifying performance-related issues. Common tools include **Apache [JMeter](../J/jmeter.md)**, **LoadRunner**, and **Gatling**.

  ```
  // Example of a simple JMeter test plan snippet
  ThreadGroup num_threads=50 ramp_up=10s {
      HTTPSampler domain="www.example.com" path="/api/test" method="GET"
  }
  ```
  [Performance testing](../P/performance-testing.md) is crucial for validating that the software will perform well under its expected workload and beyond, ensuring a positive user experience and system reliability.

  - **[Load Testing](../L/load-testing.md)** : Determines how the system behaves under expected user loads.
  - **[Stress Testing](../S/stress-testing.md)** : Assesses system stability under extreme conditions.
  - **[Endurance Testing](../E/endurance-testing.md)** : Checks system performance with a normal workload over an extended period.
  - **Spike Testing** : Evaluates system reaction to sudden large spikes in user load.
  - **[Volume Testing](../V/volume-testing.md)** : Tests the system’s ability to handle large volumes of data.
  - **[Scalability Testing](../S/scalability-testing.md)** : Determines if the system can scale up or out and the effects on performance.

#### What is load testing?

  [Load testing](../L/load-testing.md) is a type of **[non-functional testing](../N/non-functional-testing.md)** that evaluates how a system performs under an anticipated load over a given period. The primary goal is to identify performance bottlenecks before the software application goes live.
  During [load testing](../L/load-testing.md), the system is subjected to increasing volumes of requests until it reaches the threshold of its specified capacity. Key metrics such as response times, throughput rates, and resource utilization are measured to ensure the application can handle high traffic without degradation in performance.
  [Load testing](../L/load-testing.md) tools, such as Apache [JMeter](../J/jmeter.md) or LoadRunner, simulate multiple users accessing the application simultaneously. These tools provide insights into how the system behaves under stress and help in tuning the performance.
  It's crucial to distinguish [load testing](../L/load-testing.md) from **[stress testing](../S/stress-testing.md)**. While [load testing](../L/load-testing.md) checks the system's performance under expected load conditions, [stress testing](../S/stress-testing.md) pushes the system beyond its limits to see how it handles extreme conditions.
  In summary, [load testing](../L/load-testing.md) is essential for validating that an application can meet its performance objectives and provide a good user experience under peak load conditions. It's a critical step in ensuring that the application is robust, reliable, and ready for release.

#### What is stress testing?

  [Stress testing](../S/stress-testing.md) is a type of **[non-functional testing](../N/non-functional-testing.md)** that evaluates a system's performance under extreme conditions. It involves subjecting the system to loads and demands that are beyond its normal operational capacity to determine how it behaves under high stress and to identify its breaking point. The goal is to ensure the system remains reliable and fails gracefully, providing valuable insights into its **thresholds and limitations**.
  During [stress testing](../S/stress-testing.md), various parameters may be pushed to their limits, such as:

  - **CPU usage**
  - **Memory consumption**
  - **Disk I/O**
  - **Network traffic**
  This form of testing can reveal **synchronization issues**, **race conditions**, and **memory leaks** that might not surface under normal conditions. It's particularly important for **critical applications** where downtime can lead to significant problems or costs.
  Automated tools are often used to simulate the high stress conditions, and the results are analyzed to identify any potential bottlenecks or weaknesses in the system. This information is crucial for developers to optimize the system's performance and stability before it goes live.
  In summary, [stress testing](../S/stress-testing.md) is about pushing a system to its limits to ensure it can withstand extreme conditions and to discover potential points of failure that could compromise its performance and reliability.

  - **CPU usage**
  - **Memory consumption**
  - **Disk I/O**
  - **Network traffic**

#### What is usability testing?

  [Usability testing](../U/usability-testing.md) is a technique used to evaluate a product by testing it on users. This form of testing is crucial for gauging how intuitive and user-friendly a software application is. It involves observing real users as they attempt to complete tasks on the product and identifying any usability problems, collecting qualitative and quantitative data, and determining the participant's satisfaction with the product.
  Unlike other testing methods that may focus on functional correctness, [usability testing](../U/usability-testing.md) is concerned with the user experience aspect. It aims to uncover how the software can be improved to provide a better user experience, which includes ensuring that the interface is easy to navigate, information is easy to find, and the product is pleasant to use.
  During [usability testing](../U/usability-testing.md), participants are typically asked to perform a series of tasks while observers watch, listen, and take notes. The goal is to identify any confusion or issues users face, which could potentially lead to frustration or errors.
  Key metrics often evaluated during [usability testing](../U/usability-testing.md) include:

  - **Task success rate** : Whether users can successfully complete tasks.
  - **Error rate** : How often users make errors and the severity of these errors.
  - **Task completion time** : How long it takes for users to complete tasks.
  - **User satisfaction** : How users feel about their interactions with the product.
  [Usability testing](../U/usability-testing.md) can be conducted at various stages of development, from early prototypes to the final product, allowing for iterative improvements. It is an essential component of user-centered design and helps ensure that the software will meet the intended users' needs and expectations.

  - **Task success rate** : Whether users can successfully complete tasks.
  - **Error rate** : How often users make errors and the severity of these errors.
  - **Task completion time** : How long it takes for users to complete tasks.
  - **User satisfaction** : How users feel about their interactions with the product.

#### What is security testing?

  [Security testing](../S/security-testing.md) is a process aimed at uncovering vulnerabilities, threats, and risks in software that could potentially lead to a security breach. Its objective is to ensure that the software system is capable of protecting data and maintaining functionality as intended even when faced with malicious attacks or other security threats.
  Key aspects of [security testing](../S/security-testing.md) include:

  - **[Verification](../V/verification.md) of authentication and authorization**
    mechanisms to ensure that users are who they claim to be and have appropriate access.

  - **Validation of data encryption**
    to protect sensitive information during storage and transmission.

  - **Assessment of software and infrastructure**
    for known vulnerabilities using tools like vulnerability scanners.

  - **[Penetration testing](../P/penetration-testing.md)**
    , which simulates attacks to identify exploitable weaknesses.

  - **Security code reviews**
    to detect security-specific coding flaws.

  - **Configuration and deployment management testing**
    to ensure secure deployment settings.
  [Security testing](../S/security-testing.md) is crucial in the development lifecycle and should be integrated into the continuous integration/continuous deployment (CI/CD) pipeline. Automated [security testing](../S/security-testing.md) tools, such as static application [security testing](../S/security-testing.md) (SAST), dynamic application [security testing](../S/security-testing.md) (DAST), and interactive application [security testing](../S/security-testing.md) (IAST), can be used to identify security issues early and frequently.
  In summary, [security testing](../S/security-testing.md) protects against unauthorized access and data breaches, ensuring the confidentiality, integrity, and availability of the software system.

  - **[Verification](../V/verification.md) of authentication and authorization**
    mechanisms to ensure that users are who they claim to be and have appropriate access.

  - **Validation of data encryption**
    to protect sensitive information during storage and transmission.

  - **Assessment of software and infrastructure**
    for known vulnerabilities using tools like vulnerability scanners.

  - **[Penetration testing](../P/penetration-testing.md)**
    , which simulates attacks to identify exploitable weaknesses.

  - **Security code reviews**
    to detect security-specific coding flaws.

  - **Configuration and deployment management testing**
    to ensure secure deployment settings.
