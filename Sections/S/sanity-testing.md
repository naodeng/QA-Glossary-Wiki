# Sanity Testing


<!-- TOC START -->
- [Related Terms:](#related-terms)
- [Questions about Sanity Testing ?](#questions-about-sanity-testing)
  - [Basics and Importance](#basics-and-importance)
    - [What is sanity testing in software testing?](#what-is-sanity-testing-in-software-testing)
    - [Why is sanity testing important in the software development lifecycle?](#why-is-sanity-testing-important-in-the-software-development-lifecycle)
    - [How does sanity testing differ from smoke testing?](#how-does-sanity-testing-differ-from-smoke-testing)
    - [What are the key benefits of performing sanity testing?](#what-are-the-key-benefits-of-performing-sanity-testing)
    - [What is the role of sanity testing in Agile methodology?](#what-is-the-role-of-sanity-testing-in-agile-methodology)
  - [Process and Techniques](#process-and-techniques)
    - [What are the steps involved in the sanity testing process?](#what-are-the-steps-involved-in-the-sanity-testing-process)
    - [What techniques are commonly used in sanity testing?](#what-techniques-are-commonly-used-in-sanity-testing)
    - [How do you determine which functionalities to test in sanity testing?](#how-do-you-determine-which-functionalities-to-test-in-sanity-testing)
    - [What is the typical duration of a sanity test?](#what-is-the-typical-duration-of-a-sanity-test)
    - [How is sanity testing performed in a continuous integration environment?](#how-is-sanity-testing-performed-in-a-continuous-integration-environment)
  - [Tools and Practices](#tools-and-practices)
    - [What tools are commonly used for sanity testing?](#what-tools-are-commonly-used-for-sanity-testing)
    - [How can automation be incorporated into sanity testing?](#how-can-automation-be-incorporated-into-sanity-testing)
    - [What are some best practices for effective sanity testing?](#what-are-some-best-practices-for-effective-sanity-testing)
    - [Can sanity tests be reused or are they typically unique for each software version?](#can-sanity-tests-be-reused-or-are-they-typically-unique-for-each-software-version)
    - [How do you document the results of a sanity test?](#how-do-you-document-the-results-of-a-sanity-test)
<!-- TOC END -->

Sanity testing

, a subset of

regression testing

, ensures that code modifications function correctly. If issues arise, it halts the build.

## Related Terms:

- [Build Verification Testing](../B/build-verification-testing.md)

## Questions about Sanity Testing ?

### Basics and Importance

#### What is sanity testing in software testing?

  [Sanity testing](../S/sanity-testing.md) is a subset of [regression testing](../R/regression-testing.md) focused on verifying specific functionality after minor changes or [bug](../B/bug.md) fixes. It's a quick, non-exhaustive check to ensure that a particular function or [bug](../B/bug.md) is working as expected post-modification. Unlike smoke testing, which is broad and shallow, [sanity testing](../S/sanity-testing.md) is narrow and deep, concentrating on one or a few areas of functionality.
  When determining functionalities to test, prioritize those directly affected by recent code changes. [Sanity testing](../S/sanity-testing.md) is typically brief, often completed in a matter of hours, and is crucial for maintaining quality in fast-paced development environments like Agile.
  In continuous integration, sanity tests are triggered after a successful build and smoke test. They serve as a gatekeeper, ensuring that new changes do not disrupt key features before more rigorous testing is performed.
  Common techniques include targeted [retesting](../R/retesting.md) and using [exploratory testing](../E/exploratory-testing.md) to focus on affected functionalities. While sanity tests can be reused, they often require updates to align with the latest application changes.
  Automation plays a significant role in [sanity testing](../S/sanity-testing.md), enabling rapid execution of these focused tests. Automated sanity tests are scripted, maintained in version control, and integrated into the CI/CD pipeline.
  Results should be documented clearly and concisely, often in [test management](../T/test-management.md) tools or integrated into the CI/CD reporting mechanisms.
  Best practices include maintaining a lean [test suite](../T/test-suite.md), focusing on critical functionalities, and ensuring tests are easy to update. Tools like [Selenium](../S/selenium.md), TestComplete, or specific CI tools like Jenkins or CircleCI are commonly used to facilitate [sanity testing](../S/sanity-testing.md).

#### Why is sanity testing important in the software development lifecycle?

  [Sanity testing](../S/sanity-testing.md) is crucial in the software development lifecycle as it ensures that recent changes or [bug](../B/bug.md) fixes have not adversely affected existing functionalities. It acts as a **quick health check** post a minor code change, verifying that a particular function or [bug](../B/bug.md) is working as expected. This targeted testing approach saves time and resources by not [retesting](../R/retesting.md) the entire application, focusing only on the affected areas and their related functionalities.
  By confirming that the core aspects of a release are functioning correctly, [sanity testing](../S/sanity-testing.md) helps maintain a stable build and prevents the propagation of glaring issues into later stages of development. It's particularly important when there are **frequent releases or continuous deployments**, as it allows for rapid validation of critical functionality without the overhead of a full regression suite.
  In an **Agile environment**, sanity tests are often automated to provide immediate feedback on the stability of the application after each [iteration](../I/iteration.md). They serve as a gatekeeper, ensuring that the most recent changes are sound before moving on to more extensive testing phases or before a build is promoted to the next environment.
  [Sanity testing](../S/sanity-testing.md)'s importance is underscored by its role in maintaining a high level of confidence in the software's reliability, especially when time constraints or resource limitations make full [regression testing](../R/regression-testing.md) impractical. It helps teams prioritize issues, streamline the development process, and deliver quality software at a faster pace.

#### How does sanity testing differ from smoke testing?

  [Sanity testing](../S/sanity-testing.md) and smoke testing are both subsets of [acceptance testing](../A/acceptance-testing.md), yet they serve different purposes and occur at different stages of the software release cycle. **Smoke testing** is a preliminary test that checks the basic functionality of an application after a new build to ensure that the major features are working and that the build is stable enough for further testing. It's like an initial health check of the software.
  In contrast, **[sanity testing](../S/sanity-testing.md)** is a more focused form of testing that is performed after receiving a software build with minor changes or in a stable development phase. It ensures that the specific issue or functionality that was updated works as expected without performing exhaustive testing. [Sanity testing](../S/sanity-testing.md) is usually unscripted and helps in verifying the rationality of the system, ensuring that the proposed functionality works roughly as intended.
  While smoke testing is broad and shallow, [sanity testing](../S/sanity-testing.md) is narrow and deep. Smoke testing is often automated, acting as a gatekeeper for further testing, whereas [sanity testing](../S/sanity-testing.md) can be either manual or automated and is used to check specific components after changes have been made.
  In essence, smoke testing asks "Does the application broadly function?" while [sanity testing](../S/sanity-testing.md) asks "Do the recent changes make sense and function correctly?" Both are critical in the software development lifecycle but are applied at different points and for different reasons.

#### What are the key benefits of performing sanity testing?

  [Sanity testing](../S/sanity-testing.md) offers several key benefits:

  - **Quick Feedback** : It provides immediate validation of core functionalities after minor changes, ensuring that any defects are identified quickly.
  - **Cost-Effective** : By focusing on specific areas, it saves time and resources compared to a full regression test.
  - **Focus on Critical Issues** : Sanity testing zeroes in on critical functionalities, which can be crucial for decision-making processes regarding further testing or releases.
  - **Simplifies Testing** : It simplifies the assessment of a particular segment of the application, making it easier to perform and understand.
  - **Enhances Quality** : Regular sanity checks help maintain a high quality of the product by catching issues in the early stages of development.
  - **Supports Continuous Integration** : In a CI environment, sanity tests can be run automatically to verify that new code commits have not disrupted key features.
  [Sanity testing](../S/sanity-testing.md) is a strategic approach to verify that a particular function or [bug](../B/bug.md) fix works as intended. It's a subset of [regression testing](../R/regression-testing.md) and is often used as a checkpoint to determine if the application is ready for further, more extensive testing. By incorporating sanity tests into the [test suite](../T/test-suite.md), teams can ensure that the most crucial aspects of the software are always in working order, which is especially beneficial in fast-paced development environments where frequent changes are made.

  - **Quick Feedback** : It provides immediate validation of core functionalities after minor changes, ensuring that any defects are identified quickly.
  - **Cost-Effective** : By focusing on specific areas, it saves time and resources compared to a full regression test.
  - **Focus on Critical Issues** : Sanity testing zeroes in on critical functionalities, which can be crucial for decision-making processes regarding further testing or releases.
  - **Simplifies Testing** : It simplifies the assessment of a particular segment of the application, making it easier to perform and understand.
  - **Enhances Quality** : Regular sanity checks help maintain a high quality of the product by catching issues in the early stages of development.
  - **Supports Continuous Integration** : In a CI environment, sanity tests can be run automatically to verify that new code commits have not disrupted key features.

#### What is the role of sanity testing in Agile methodology?

  In Agile methodology, **[sanity testing](../S/sanity-testing.md)** serves as a focused check to ensure that a specific function or [bug](../B/bug.md) fix works as intended after a minor change or in a new build. It's a quick, narrow regression test to validate that the code changes have not disrupted existing functionality. [Sanity testing](../S/sanity-testing.md) is typically done after **smoke testing** and before more extensive [regression testing](../R/regression-testing.md) or [user acceptance testing](../U/user-acceptance-testing.md) (UAT).
  Agile teams often employ sanity tests during continuous integration and deployment (CI/CD) to verify that recent commits haven't introduced any major issues. This is crucial in Agile's iterative development cycle, where changes are frequent and rapid.
  Since Agile emphasizes **user satisfaction** and **working software**, [sanity testing](../S/sanity-testing.md) aligns with these principles by quickly confirming that the most recent changes haven't compromised the user experience or core functionality. It helps maintain a stable product for the next [iteration](../I/iteration.md) of development.
  Sanity tests are usually **manual** but can be automated for efficiency. They are often derived from a subset of regression tests that are most relevant to the recent changes. While they can be reused, they should be regularly reviewed and updated to align with the evolving software.
  **Documentation** for sanity tests should be concise, capturing the essence of what was tested and the outcome. This documentation aids in communication within the team and serves as a reference for future testing cycles.
  **Best practices** include prioritizing tests based on the impact of changes, keeping sanity tests lean, and ensuring they are easily maintainable and adaptable to changes in the software.

### Process and Techniques

#### What are the steps involved in the sanity testing process?

  [Sanity testing](../S/sanity-testing.md) involves a subset of tests focused on validating specific functionality after minor changes. Here's a concise rundown of the steps:

  1. **Identify Changed Features** : Pinpoint the features impacted by recent code changes.
  2. **Select [Test Cases](../T/test-case.md)** : Choose relevant test cases that cover the affected functionalities.
  3. **Set Up [Test Environment](../T/test-environment.md)** : Prepare the environment to reflect the production setup.
  4. **Execute Tests** : Run the selected test cases manually or through automated scripts.
  5. **Analyze Results** : Evaluate test outcomes to ensure the changes work as expected.
  6. **Report Findings** : Document any defects or issues and communicate them to the development team.
  7. **Retest** : After fixes, retest to confirm issues are resolved.
  Remember, sanity tests are quick, targeted, and not exhaustive. They ensure that a particular function or [bug](../B/bug.md) fix works without unintended side effects.

  1. **Identify Changed Features** : Pinpoint the features impacted by recent code changes.
  2. **Select [Test Cases](../T/test-case.md)** : Choose relevant test cases that cover the affected functionalities.
  3. **Set Up [Test Environment](../T/test-environment.md)** : Prepare the environment to reflect the production setup.
  4. **Execute Tests** : Run the selected test cases manually or through automated scripts.
  5. **Analyze Results** : Evaluate test outcomes to ensure the changes work as expected.
  6. **Report Findings** : Document any defects or issues and communicate them to the development team.
  7. **Retest** : After fixes, retest to confirm issues are resolved.

#### What techniques are commonly used in sanity testing?

  [Sanity testing](../S/sanity-testing.md) commonly employs a focused and narrow set of techniques to verify that a particular function or [bug](../B/bug.md) fix works as expected after a minor code change. Here are some techniques used:

  - **Selective [Test Case](../T/test-case.md) Execution** : Running a subset of test cases that are directly related to the recent code changes.
  - **[Priority](../P/priority.md)-based Testing** : Executing tests for critical functionalities first to ensure they are not affected by recent changes.
  - **[Exploratory Testing](../E/exploratory-testing.md)** : Informal testing where the tester actively controls the design of the tests as they are performed.
  - **Retest All** : In some cases, sanity testing may involve re-running all existing test cases for the modified component to ensure no new issues have been introduced.
  - **[Test Case](../T/test-case.md) Sampling** : Choosing a few test cases that represent the larger set of tests to quickly verify the system's health.
  Incorporating automation into [sanity testing](../S/sanity-testing.md) involves scripting these techniques to be executed automatically:

  ```
  // Example of an automated sanity test script
  describe('Sanity Test Suite', () => {
    it('should verify critical functionality A works', () => {
      // Test steps for functionality A
    });
    it('should verify critical functionality B works', () => {
      // Test steps for functionality B
    });
    // Additional test cases...
  });
  ```
  Automated sanity tests are typically integrated into the CI/CD pipeline to run after each build deployment. Results are documented in [test reports](../T/test-report.md) generated by the automation framework or CI tool, which are then reviewed to make decisions about the stability of the build.

  - **Selective [Test Case](../T/test-case.md) Execution** : Running a subset of test cases that are directly related to the recent code changes.
  - **[Priority](../P/priority.md)-based Testing** : Executing tests for critical functionalities first to ensure they are not affected by recent changes.
  - **[Exploratory Testing](../E/exploratory-testing.md)** : Informal testing where the tester actively controls the design of the tests as they are performed.
  - **Retest All** : In some cases, sanity testing may involve re-running all existing test cases for the modified component to ensure no new issues have been introduced.
  - **[Test Case](../T/test-case.md) Sampling** : Choosing a few test cases that represent the larger set of tests to quickly verify the system's health.

#### How do you determine which functionalities to test in sanity testing?

  Determining which functionalities to test in **[sanity testing](../S/sanity-testing.md)** involves focusing on the most critical aspects of the software that have been recently modified or impacted by code changes. To select these functionalities, consider the following criteria:

  - **Recent [Bug](../B/bug.md) Fixes** : Prioritize functionalities that have undergone recent bug fixes to ensure the fixes are effective and have not introduced new issues.
  - **New Features** : Test new features that are critical for the application's operation and are likely to be used frequently by end-users.
  - **High-Risk Areas** : Identify areas of the application that are prone to errors or have a history of issues, as these are more likely to break with new changes.
  - **Core Functionalities** : Focus on the core functionalities that are essential for the application to run smoothly, as any issues here can render the software unusable.
  - **Dependencies** : Consider functionalities that have dependencies on the modified code, as changes can have cascading effects on related features.
  Use a risk-based approach to prioritize testing efforts, ensuring that the most impactful and critical areas are covered. Collaborate with developers, product managers, and other stakeholders to understand the scope of changes and their potential impact on the application. This collaboration helps in creating a targeted sanity [test suite](../T/test-suite.md) that is both efficient and effective.

  - **Recent [Bug](../B/bug.md) Fixes** : Prioritize functionalities that have undergone recent bug fixes to ensure the fixes are effective and have not introduced new issues.
  - **New Features** : Test new features that are critical for the application's operation and are likely to be used frequently by end-users.
  - **High-Risk Areas** : Identify areas of the application that are prone to errors or have a history of issues, as these are more likely to break with new changes.
  - **Core Functionalities** : Focus on the core functionalities that are essential for the application to run smoothly, as any issues here can render the software unusable.
  - **Dependencies** : Consider functionalities that have dependencies on the modified code, as changes can have cascading effects on related features.

#### What is the typical duration of a sanity test?

  The typical duration of a **sanity test** varies depending on the scope of the changes made to the software and the size of the project. Generally, sanity tests are brief, often taking anywhere from **15 minutes to a few hours** to execute. These tests are designed to be quick checks to ensure that the most crucial functions work as expected after minor modifications.
  Since [sanity testing](../S/sanity-testing.md) is a subset of [regression testing](../R/regression-testing.md), it focuses on specific areas rather than the entire application. The duration is kept short to facilitate rapid feedback to the development team. In a **continuous integration** environment, sanity tests may run even faster, as they are automated and executed as soon as a new build is available.
  For experienced [test automation](../T/test-automation.md) engineers, it's essential to have a well-optimized suite of sanity tests that can be triggered automatically. This suite should be concise yet comprehensive enough to cover the critical functionalities that could be affected by recent code changes. The speed of execution can be further enhanced by parallel execution and efficient [test management](../T/test-management.md) practices.
  Remember, the goal of [sanity testing](../S/sanity-testing.md) is to quickly determine whether it's reasonable to proceed with further, more exhaustive testing. Therefore, the duration should align with this objective, ensuring a balance between thoroughness and time efficiency.

#### How is sanity testing performed in a continuous integration environment?

  In a **continuous integration (CI)** environment, [sanity testing](../S/sanity-testing.md) is typically automated and integrated into the CI pipeline. The process is as follows:

  1. **Code Commit** : Developers push code to the repository, triggering the CI pipeline.
  2. **Build** : The CI server compiles the code into an executable application.
  3. **Deploy** : The build is deployed to a test environment automatically.
  4. **Sanity [Test Suite](../T/test-suite.md)** : A predefined suite of sanity tests is executed. These tests are a subset of the regression suite, focusing on critical functionalities.
  5. **[Test Execution](../T/test-execution.md)** : Automated scripts run the sanity tests. These scripts are often written in a high-level language and managed by a test framework.
  6. **Results Analysis** : Test results are automatically collected and analyzed. Failures halt the pipeline, and stakeholders are notified.
  7. **Feedback Loop** : Developers receive immediate feedback on the build's sanity, allowing for quick fixes if necessary.

  ```
  // Example of a sanity test script in TypeScript
  import { expect } from 'chai';
  import { login, getUserProfile } from './appActions';
  describe('Sanity Test Suite', () => {
    it('should successfully log in and retrieve user profile', async () => {
      const loginResponse = await login('user', 'password');
      expect(loginResponse).to.be.true;
      const profile = await getUserProfile();
      expect(profile).to.have.property('username');
    });
  });
  ```
  Automated sanity tests are designed to be **fast** and **focused**, providing a quick check to ensure that the most crucial parts of the application are functioning after each build. Results are typically logged into a [test management](../T/test-management.md) tool or directly into the CI system for easy access and review.

  1. **Code Commit** : Developers push code to the repository, triggering the CI pipeline.
  2. **Build** : The CI server compiles the code into an executable application.
  3. **Deploy** : The build is deployed to a test environment automatically.
  4. **Sanity [Test Suite](../T/test-suite.md)** : A predefined suite of sanity tests is executed. These tests are a subset of the regression suite, focusing on critical functionalities.
  5. **[Test Execution](../T/test-execution.md)** : Automated scripts run the sanity tests. These scripts are often written in a high-level language and managed by a test framework.
  6. **Results Analysis** : Test results are automatically collected and analyzed. Failures halt the pipeline, and stakeholders are notified.
  7. **Feedback Loop** : Developers receive immediate feedback on the build's sanity, allowing for quick fixes if necessary.

### Tools and Practices

#### What tools are commonly used for sanity testing?

  Common tools for **[sanity testing](../S/sanity-testing.md)** include:

  - **[Selenium](../S/selenium.md)** : A popular framework for web applications that supports multiple languages and browsers.
  - **Appium** : Extends Selenium's framework to mobile applications.
  - **TestComplete** : Offers a user-friendly interface and scripting languages for automated testing.
  - **JUnit**
    (for Java) and
    **[NUnit](../N/nunit.md)**
    (for .NET): Frameworks for unit testing that can be adapted for sanity checks.

  - **[Postman](../P/postman.md)** : For API sanity testing, allowing quick checks on RESTful services.
  - **QTP/UFT** : A versatile tool from Micro Focus for functional and regression testing.
  - **Rational Functional Tester** : IBM's solution for automated functional and regression testing.
  - **[Cypress](../C/cypress.md)** : A modern end-to-end testing framework designed for web applications.
  - **Robot Framework** : A keyword-driven test automation framework for acceptance testing and acceptance test-driven development (ATDD).
  These tools can be integrated into **CI/CD pipelines** to execute sanity tests automatically after each build. Scripts are typically written in the language supported by the tool, such as Python, Java, or JavaScript.

  ```
  // Example of a simple sanity check using Selenium WebDriver in JavaScript
  const { Builder, By } = require('selenium-webdriver');
  (async function example() {
      let driver = await new Builder().forBrowser('firefox').build();
      try {
          await driver.get('http://www.example.com');
          const element = await driver.findElement(By.id('important-element'));
          if (element.isDisplayed()) {
              console.log('Sanity test passed.');
          } else {
              console.log('Sanity test failed.');
          }
      } finally {
          await driver.quit();
      }
  })();
  ```
  Automation scripts for [sanity testing](../S/sanity-testing.md) are often **specific to the release** or build being tested, focusing on critical functionalities that were recently modified.

  - **[Selenium](../S/selenium.md)** : A popular framework for web applications that supports multiple languages and browsers.
  - **Appium** : Extends Selenium's framework to mobile applications.
  - **TestComplete** : Offers a user-friendly interface and scripting languages for automated testing.
  - **JUnit**
    (for Java) and
    **[NUnit](../N/nunit.md)**
    (for .NET): Frameworks for unit testing that can be adapted for sanity checks.

  - **[Postman](../P/postman.md)** : For API sanity testing, allowing quick checks on RESTful services.
  - **QTP/UFT** : A versatile tool from Micro Focus for functional and regression testing.
  - **Rational Functional Tester** : IBM's solution for automated functional and regression testing.
  - **[Cypress](../C/cypress.md)** : A modern end-to-end testing framework designed for web applications.
  - **Robot Framework** : A keyword-driven test automation framework for acceptance testing and acceptance test-driven development (ATDD).

#### How can automation be incorporated into sanity testing?

  Incorporating automation into [sanity testing](../S/sanity-testing.md) can streamline the process and ensure that critical functionalities work as expected after minor changes. To automate sanity tests, follow these steps:

  1. **Identify critical paths**
    that are stable and unlikely to change frequently. These should be the focus of your sanity suite.

  2. **Create automated [test scripts](../T/test-script.md)**
    for these critical functionalities using a preferred test automation tool.

  3. **Integrate with a CI/CD pipeline**
    to trigger the sanity suite post-build or after deployment to a staging environment.

  4. Use
    **assertions**
    to validate the expected outcomes of the tests.

  5. **Prioritize speed and stability**
    in your tests to quickly assess the health of the application.

  6. **Maintain and update**
    the test suite as necessary to adapt to any changes in the application's critical paths.

  ```
  // Example of a simple automated sanity test script
  describe('Sanity Test', () => {
    it('should login successfully with valid credentials', async () => {
      await navigateToLoginPage();
      await enterCredentials('user@example.com', 'password123');
      await submitLoginForm();
      expect(await isLoggedIn()).toBe(true);
    });
  });
  ```
  Ensure that the automated sanity tests are **self-contained** and **independent** to avoid cascading failures. Regularly **review and refine** the suite to discard obsolete tests and add new ones for recent features. By automating [sanity testing](../S/sanity-testing.md), you can achieve faster feedback loops and more efficient use of testing resources.

  1. **Identify critical paths**
    that are stable and unlikely to change frequently. These should be the focus of your sanity suite.

  2. **Create automated [test scripts](../T/test-script.md)**
    for these critical functionalities using a preferred test automation tool.

  3. **Integrate with a CI/CD pipeline**
    to trigger the sanity suite post-build or after deployment to a staging environment.

  4. Use
    **assertions**
    to validate the expected outcomes of the tests.

  5. **Prioritize speed and stability**
    in your tests to quickly assess the health of the application.

  6. **Maintain and update**
    the test suite as necessary to adapt to any changes in the application's critical paths.

#### What are some best practices for effective sanity testing?

  To ensure effective [sanity testing](../S/sanity-testing.md), follow these best practices:

  - **Prioritize critical paths**
    by focusing on the most important features and functionalities that have undergone recent changes.

  - **Maintain a checklist**
    of sanity test cases to streamline the process and ensure consistency across test cycles.

  - **Keep tests simple**
    and straightforward, avoiding complex scenarios that are better suited for comprehensive testing phases.

  - **Automate where possible**
    to speed up the process and enable frequent re-running of sanity tests, especially in a CI/CD pipeline.

  - **Use version control**
    for your sanity test scripts to track changes and facilitate collaboration among team members.

  - **Validate fixes**
    and new features quickly to confirm they work as expected without introducing new issues.

  - **Isolate [test environment](../T/test-environment.md)**
    to ensure that the sanity testing is not affected by external factors and provides reliable results.

  - **Document results**
    concisely, focusing on pass/fail status and critical observations that require immediate attention.

  - **Communicate effectively**
    with the development team to quickly address any issues found during sanity testing.

  - **Review and update**
    your sanity test suite regularly to reflect changes in the application and to remove obsolete or redundant tests.
  By adhering to these practices, you can maximize the efficiency and effectiveness of your [sanity testing](../S/sanity-testing.md) efforts, ensuring that the software is stable and ready for further testing or release.

  - **Prioritize critical paths**
    by focusing on the most important features and functionalities that have undergone recent changes.

  - **Maintain a checklist**
    of sanity test cases to streamline the process and ensure consistency across test cycles.

  - **Keep tests simple**
    and straightforward, avoiding complex scenarios that are better suited for comprehensive testing phases.

  - **Automate where possible**
    to speed up the process and enable frequent re-running of sanity tests, especially in a CI/CD pipeline.

  - **Use version control**
    for your sanity test scripts to track changes and facilitate collaboration among team members.

  - **Validate fixes**
    and new features quickly to confirm they work as expected without introducing new issues.

  - **Isolate [test environment](../T/test-environment.md)**
    to ensure that the sanity testing is not affected by external factors and provides reliable results.

  - **Document results**
    concisely, focusing on pass/fail status and critical observations that require immediate attention.

  - **Communicate effectively**
    with the development team to quickly address any issues found during sanity testing.

  - **Review and update**
    your sanity test suite regularly to reflect changes in the application and to remove obsolete or redundant tests.

#### Can sanity tests be reused or are they typically unique for each software version?

  Sanity tests can often be **reused** across different software versions, especially when the changes between versions are incremental and do not significantly affect the areas of functionality that the sanity tests cover. These tests are designed to quickly evaluate whether the core functionalities are working as expected after minor changes or [bug](../B/bug.md) fixes.
  However, when a new feature is introduced or significant changes are made to the existing functionality, sanity tests may need to be **updated or rewritten** to reflect the new context. It's essential to review the scope of the changes in each release and adjust the sanity tests accordingly to ensure they remain relevant and effective.
  In practice, maintaining a **modular and flexible** [test suite](../T/test-suite.md) can facilitate the reuse of sanity tests. By designing tests that are independent and can be easily combined, you can mix and match [test cases](../T/test-case.md) to create an appropriate sanity [test suite](../T/test-suite.md) for each version of the software.
  Automation plays a key role in enabling the reuse of sanity tests. Automated tests can be quickly **adapted and executed**, saving time and effort compared to [manual testing](../M/manual-testing.md). It's crucial to keep the automation code well-organized and to use version control to manage changes to the [test scripts](../T/test-script.md).
  In summary, while sanity tests can be reused across software versions, they should be **regularly reviewed and updated** to ensure they align with the current state of the application and provide meaningful feedback on its sanity.

#### How do you document the results of a sanity test?

  Documenting the results of a sanity test should be **straightforward** and **concise**. Follow these guidelines:

  - **Summarize the outcome** : Begin with a clear statement indicating whether the sanity test passed or failed.
  - **List tested functionalities** : Provide a bullet-point list of the specific functionalities checked.
  - **Detail failures** : For any failed tests, include a brief description of the issue, steps to reproduce, and any relevant screenshots or error messages.
  - **Reference [test cases](../T/test-case.md)** : Link to detailed test cases or scripts used for the sanity test, if applicable.
  - **Include environment details** : Note the testing environment, software version, and configuration.
  - **Record [test data](../T/test-data.md)** : Mention any specific data sets used, which can be critical for reproducing issues.
  - **State impact** : Assess the impact of any failures on the overall system.
  - **Recommendations** : Offer immediate recommendations or actions taken, such as filing bug reports or halting a release.
  Use Markdown for formatting:

  ```
  - **Outcome**: Passed/Failed
  - **Functionalities Tested**:
    - Login process
    - Payment gateway integration
    - New user registration
  - **Failures**:
    - Payment gateway integration: Timeout error when processing payments. Steps to reproduce: [Link to test case]. Screenshot: ![Error Screenshot](url).
  - **Environment**: Windows 10, Software v2.3.1, Test Environment B
  - **Test Data Used**: Test Credit Card #1234
  - **Impact**: Payment processing critical for release. Failure blocks release.
  - **Recommendations**: Bug reported (ID #98765), suggest rollback to previous stable version.
  ```
  Ensure the documentation is **up-to-date** and **accessible** to all relevant team members.

  - **Summarize the outcome** : Begin with a clear statement indicating whether the sanity test passed or failed.
  - **List tested functionalities** : Provide a bullet-point list of the specific functionalities checked.
  - **Detail failures** : For any failed tests, include a brief description of the issue, steps to reproduce, and any relevant screenshots or error messages.
  - **Reference [test cases](../T/test-case.md)** : Link to detailed test cases or scripts used for the sanity test, if applicable.
  - **Include environment details** : Note the testing environment, software version, and configuration.
  - **Record [test data](../T/test-data.md)** : Mention any specific data sets used, which can be critical for reproducing issues.
  - **State impact** : Assess the impact of any failures on the overall system.
  - **Recommendations** : Offer immediate recommendations or actions taken, such as filing bug reports or halting a release.
